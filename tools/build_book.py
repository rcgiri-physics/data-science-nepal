"""Build the book as HTML and PDF: a student edition and a teacher edition, from the same markdown sources.

Sources (see book/README.md): book/front, book/parts (grade openers), curriculum/grade-*/unit-*/chapter.md (+ project.md,
and teacher-guide.md in the teacher edition), the capstone kit, book/teaching (teacher edition), book/beyond and the
appendices. The Python and SQL examples printed in chapters are run on the shipped synthetic data, and their printed
output, result tables and charts are placed under each example (as in a notebook).

PDF printing uses headless Chrome, Chromium or Edge (set CHROME=/path/to/browser if it is not found). The contents get
real page numbers in a second pass that reads the PDF outline with pypdf.

Usage:
    python tools/build_book.py                    # both editions -> dist/data-science-nepal-{student,teacher}.pdf
    python tools/build_book.py --edition student  # one edition
    python tools/build_book.py --html-only        # skip PDF printing
    python tools/build_book.py --no-run           # do not execute chapter code (faster drafts)
"""
from __future__ import annotations

import argparse
import ast
import base64
import contextlib
import datetime as dt
import html
import io
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify as md_slugify
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
TITLE = "Data Science from Nepal"
SUBTITLE = "डेटा विज्ञान · A foundation course for Grades 8–12"
FENCE = re.compile(r"^```([\w+-]*)[^\n]*\n(.*?)^```[ \t]*$", re.S | re.M)
SKIP_MARKERS = ("needs internet", "not run", "___")
SQL_TABLES = {
    "districts": "census-districts/clean/districts_synthetic.csv",
    "schools": "census-districts/clean/schools_synthetic.csv",
    "survey": "class-survey-synthetic/clean/class_survey_synthetic.csv",
    "climate": "climate-monthly/clean/climate_monthly_synthetic.csv",
    "health": "health-synthetic/clean/health_synthetic.csv",
    "air": "kathmandu-air-quality/clean/air_daily_synthetic.csv",
}


# --------------------------------------------------------------------------------------------- book structure
def section(path: Path, shift: int, title: str | None = None, toc: bool = True, toc_max: int = 2) -> dict:
    return {"path": path, "shift": shift, "title": title, "toc": toc, "toc_max": toc_max}


def heading(text: str, level: int) -> dict:
    return {"md": f"{'#' * level} {text}\n", "shift": 0, "toc": True}


def structure(edition: str) -> list[dict]:
    teacher = edition == "teacher"
    b = ROOT / "book"
    items: list[dict] = [section(b / "front/01-preface.md", 0, toc_max=1)]
    items.append(heading("Getting started", 1))
    for name in ("02-how-to-use-this-book.md", "03-setting-up.md", "04-the-data-science-cycle.md"):
        items.append(section(b / "front" / name, 1))
    if teacher:
        items += teaching_part()
    for grade in ("08", "09", "10", "11", "12"):
        items.append(section(b / f"parts/grade-{grade}.md", 0))
        for unit in sorted((ROOT / "curriculum" / f"grade-{grade}").glob("unit-*")):
            items.append(section(unit / "chapter.md", 1, toc=True))
            items.append(section(unit / "project.md", 2, toc=False))
            if teacher:
                items.append(section(unit / "teacher-guide.md", 2, toc=False))
        if grade == "12":
            kit = ROOT / "curriculum/grade-12/capstone-kit"
            items.append(section(kit / "README.md", 1, title="Grade 12 · Capstone kit"))
            for name in ("client-brief.md", "data-agreement-template.md", "model-card-template.md", "rubric.md"):
                items.append(section(kit / name, 2, toc=False))
    items.append(heading("Part 6 — After Grade 12: how to keep learning", 1))
    for p in sorted((b / "beyond").glob("*.md")):
        items.append(section(p, 1, toc=not p.name.startswith("00")))
    items.append(heading("Appendices", 1))
    items.append(section(ROOT / "docs/datasets/free-datasets.md", 1, title="Appendix A — Free real datasets"))
    items.append(section(ROOT / "curriculum/framework/glossary.md", 1, title="Appendix B — Glossary: English / नेपाली"))
    for p in sorted((b / "appendix").glob("*.md")):
        items.append(section(p, 1))
    if not teacher:
        items.append({"md": star_answers(), "shift": 1, "toc": True})
    return items


def teaching_part() -> list[dict]:
    b = ROOT / "book/teaching"
    out = [heading("Handbook — Teaching data-science foundations (Grades 8–12)", 1)]
    for p in sorted(b.glob("*.md")):
        out.append(section(p, 1, toc=not p.name.startswith("00")))
    return out


# --------------------------------------------------------------------------------------------- answers (student)
def star_answers() -> str:
    """Appendix G: answers to the one-star practice exercises, taken from the teacher guides."""
    out = ["# Appendix G — Answers to ★ practice exercises\n",
           "Answers to the recall (★) exercises. The teacher edition contains answers to every exercise.\n"]
    for unit in sorted(ROOT.glob("curriculum/grade-*/unit-*")):
        chapter = (unit / "chapter.md").read_text(encoding="utf-8")
        guide = (unit / "teacher-guide.md").read_text(encoding="utf-8")
        title = chapter.splitlines()[0].lstrip("# ").strip()
        practice = block_after(chapter, "## Practice exercises")
        answers = block_after(guide, "## Answers: practice exercises")
        if not practice or not answers:
            continue
        stars = {int(m.group(1)) for m in re.finditer(r"^(\d+)\. ★(?!★)", practice, re.M)}
        numbered = split_numbered(answers)
        picked = [(n, numbered[n]) for n in sorted(stars) if n in numbered]
        if picked:
            out.append(f"### {title}\n")
            out += [f"{n}. {text}\n" for n, text in picked]
            out.append("")
    return "\n".join(out)


def block_after(text: str, marker: str) -> str:
    i = text.find(marker)
    if i < 0:
        return ""
    rest = text[i + len(marker):]
    m = re.search(r"^## ", rest, re.M)
    return rest[: m.start()] if m else rest


def split_numbered(text: str) -> dict[int, str]:
    parts = re.split(r"^(\d+)\. ", text, flags=re.M)
    out = {}
    for k in range(1, len(parts) - 1, 2):
        out[int(parts[k])] = parts[k + 1].strip()
    return out


# --------------------------------------------------------------------------------------------- running examples
class Runner:
    """Runs a chapter's code blocks in order (like a notebook) and returns HTML to show under each block."""

    def __init__(self, workdir: Path):
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import pandas as pd

        self.plt, self.pd = plt, pd
        plt.show = lambda *a, **k: None
        self.workdir = workdir

    def start_chapter(self) -> None:
        self.ns: dict = {"__name__": "__book__"}
        self.con = sqlite3.connect(":memory:")
        for table, rel in SQL_TABLES.items():
            self.pd.read_csv(ROOT / "datasets" / rel).to_sql(table, self.con, index=False)

    def run(self, lang: str, code: str) -> str:
        if any(m in code for m in SKIP_MARKERS) or lang not in ("python", "sql"):
            return ""
        old = Path.cwd()
        os.chdir(self.workdir)
        try:
            return self._python(code) if lang == "python" else self._sql(code)
        except Exception as exc:  # noqa: BLE001
            return f'<div class="output error">Example did not run while building: {html.escape(str(exc))}</div>'
        finally:
            os.chdir(old)
            self.plt.close("all")

    def _python(self, code: str) -> str:
        tree = ast.parse(code)
        last = tree.body[-1] if tree.body and isinstance(tree.body[-1], ast.Expr) else None
        body = ast.Module(body=tree.body[:-1] if last else tree.body, type_ignores=[])
        buf = io.StringIO()
        value = None
        with contextlib.redirect_stdout(buf):
            exec(compile(body, "<book>", "exec"), self.ns)  # noqa: S102 (our own chapters)
            if last is not None:
                value = eval(compile(ast.Expression(last.value), "<book>", "eval"), self.ns)  # noqa: S307
        parts = []
        text = buf.getvalue().rstrip()
        if text:
            parts.append(text_output(text))
        if isinstance(value, (self.pd.DataFrame, self.pd.Series)):
            parts.append(table_output(value if isinstance(value, self.pd.DataFrame) else value.to_frame()))
        for num in self.plt.get_fignums():
            fig = self.plt.figure(num)
            png = io.BytesIO()
            fig.savefig(png, format="png", dpi=110, bbox_inches="tight")
            data = base64.b64encode(png.getvalue()).decode()
            parts.append(f'<div class="figure"><img alt="chart produced by the example above" '
                         f'src="data:image/png;base64,{data}"></div>')
        return "\n".join(parts)

    def _sql(self, code: str) -> str:
        result = None
        for stmt in [s for s in code.split(";") if s.strip()]:
            if all(not ln.strip() or ln.strip().startswith("--") for ln in stmt.splitlines()):
                continue
            cur = self.con.execute(stmt)
            if cur.description:
                result = self.pd.DataFrame(cur.fetchall(), columns=[d[0] for d in cur.description])
        return table_output(result) if result is not None else ""


def text_output(text: str, max_lines: int = 30) -> str:
    lines = text.splitlines()
    if len(lines) > max_lines:
        lines = lines[:max_lines] + [f"… ({len(lines) - max_lines} more lines)"]
    return f'<div class="output"><pre>{html.escape(chr(10).join(lines))}</pre></div>'


def table_output(df, max_rows: int = 12) -> str:
    note = ""
    if len(df) > max_rows:
        note = f'<p class="rows-note">first {max_rows} of {len(df)} rows</p>'
        df = df.head(max_rows)
    table = df.to_html(border=0, classes="result", float_format=lambda x: f"{x:,.3f}".rstrip("0").rstrip("."))
    return f'<div class="output">{table}{note}</div>'


def with_outputs(md_text: str, runner: Runner | None) -> str:
    """Insert raw-HTML output blocks after each code block of a chapter."""
    if runner is None:
        return md_text
    runner.start_chapter()

    def repl(m: re.Match) -> str:
        out = runner.run(m.group(1).lower(), m.group(2))
        return m.group(0) + ("\n\n" + out + "\n" if out else "")

    return FENCE.sub(repl, md_text)


# --------------------------------------------------------------------------------------------- markdown → html
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+\.) ")


def shift_headings(md_text: str, shift: int, title: str | None) -> str:
    """Shift heading levels, optionally retitle the first heading, and add the blank line python-markdown needs
    before a list that directly follows a paragraph line."""
    out, in_code, first = [], False, True
    for line in md_text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        prev = out[-1] if out else ""
        if (not in_code and LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev)
                and not prev.startswith((" ", "\t", "|", ">")) and not line.startswith(" ")):
            out.append("")
        if not in_code and re.match(r"^#{1,6} ", line):
            hashes, text = line.split(" ", 1)
            if first and title:
                text = title
            first = False
            line = "#" * min(6, len(hashes) + shift) + " " + text
        out.append(line)
    return "\n".join(out) + "\n"


def to_html(md_text: str, prefix: str) -> tuple[str, list[tuple[int, str, str]]]:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "codehilite", "toc", "sane_lists", "md_in_html", "attr_list"],
        extension_configs={
            "codehilite": {"guess_lang": False, "css_class": "highlight"},
            "toc": {"slugify": lambda value, sep: prefix + md_slugify(value, sep), "toc_depth": "1-2"},
        },
    )
    body = md.convert(md_text)
    heads = []

    def walk(tokens):
        for t in tokens:
            heads.append((t["level"], t["id"], html.unescape(re.sub(r"<[^>]+>", "", t["name"]))))
            walk(t["children"])

    walk(md.toc_tokens)
    # relative links do not work in print: keep the text, drop the link
    body = re.sub(r'<a href="(?!https?:|mailto:|#)[^"]*">(.*?)</a>', r'<span class="ref">\1</span>', body, flags=re.S)
    return body, heads


# --------------------------------------------------------------------------------------------- assembly
CSS = """
:root { --ink:#1d1d1f; --muted:#5f6368; --line:#d0d4da; --accent:#1f4e8c; --code:#f5f7fa; }
@page { size: A4; margin: 18mm 17mm 20mm 17mm;
  @bottom-center { content: counter(page); font: 9pt "Segoe UI", "Noto Sans", sans-serif; color: #666; }
  @bottom-left { content: "__FOOTER__"; font: 7.5pt "Segoe UI", "Noto Sans", sans-serif; color: #999; } }
@page :first { @bottom-center { content: none; } @bottom-left { content: none; } }
html { font-size: 10.3pt; }
body { font-family: "Noto Serif", Cambria, Georgia, "Nirmala UI", "Noto Serif Devanagari", "Noto Sans Devanagari", serif;
  color: var(--ink); line-height: 1.45; }
h1, h2, h3, h4, h5 { font-family: "Segoe UI", "Noto Sans", "Nirmala UI", "Noto Sans Devanagari", sans-serif;
  color: var(--accent); line-height: 1.2; break-after: avoid; }
h1 { font-size: 24pt; break-before: page; margin: 0 0 14pt; padding-top: 30mm; border-bottom: 3px solid var(--accent); }
h2 { font-size: 16pt; break-before: page; margin: 0 0 10pt; padding-bottom: 4pt; border-bottom: 1px solid var(--line); }
h3 { font-size: 12.5pt; margin: 16pt 0 6pt; }
h4 { font-size: 11pt; margin: 12pt 0 4pt; }
h5, h6 { font-size: 10.3pt; margin: 10pt 0 4pt; }
h1 + h2, h1 + p + h2 { break-before: avoid; }
p, li { orphans: 3; widows: 3; }
table { border-collapse: collapse; margin: 6pt 0 10pt; font-size: 8.8pt; width: auto; max-width: 100%; }
th, td { border: 1px solid var(--line); padding: 2.5pt 5pt; vertical-align: top; }
th { background: #eef2f7; }
tr { break-inside: avoid; }
pre, code { font-family: Consolas, "DejaVu Sans Mono", "Noto Sans Mono", monospace; font-size: 8.4pt; }
code { background: var(--code); padding: 0 2pt; border-radius: 2pt; }
.highlight, pre { background: var(--code); border: 1px solid #e3e7ec; border-radius: 3pt; padding: 5pt 7pt;
  white-space: pre-wrap; overflow-wrap: anywhere; }
.highlight pre { background: none; border: none; padding: 0; margin: 0; }
.output { border-left: 3px solid #9ab; margin: -4pt 0 10pt 6pt; padding: 2pt 0 2pt 8pt; break-inside: avoid; }
.output::before { content: "Output"; display: block; font: 7pt "Segoe UI", sans-serif; color: #789; text-transform: uppercase; letter-spacing: .5pt; }
.output pre { background: #fbfcfd; border: none; padding: 2pt 0; }
.output table.result { font-family: Consolas, monospace; font-size: 7.8pt; }
.output.error { color: #a33; }
.rows-note { font-size: 7.5pt; color: var(--muted); margin: 0; }
.figure img { max-width: 13.5cm; max-height: 9cm; display: block; margin: 2pt 0; }
blockquote { margin: 8pt 0; padding: 4pt 10pt; border-left: 3px solid #c9a227; background: #fffaf0; }
.ref { font-style: italic; }
a { color: var(--accent); text-decoration: none; }
.titlepage { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.titlepage .t1 { font: 700 30pt "Segoe UI", "Noto Sans", sans-serif; color: var(--accent); margin-bottom: 8pt; }
.titlepage .t2 { font: 15pt "Nirmala UI", "Noto Sans Devanagari", "Segoe UI", sans-serif; color: var(--muted); }
.titlepage .ed { margin-top: 26pt; font: 600 14pt "Segoe UI", sans-serif; }
.titlepage .meta { margin-top: 40pt; font-size: 10pt; color: var(--muted); }
.credits { break-before: page; font-size: 9.3pt; }
.toc { break-before: page; }
.toc h1 { break-before: avoid; padding-top: 0; }
.toc ul { list-style: none; padding-left: 0; margin: 0; }
.toc li { display: flex; gap: 6pt; font-size: 9.6pt; margin: 1.5pt 0; break-inside: avoid; }
.toc li.l1 { font: 600 10.5pt "Segoe UI", sans-serif; margin-top: 7pt; color: var(--accent); }
.toc li.l2 { padding-left: 12pt; }
.toc li .dots { flex: 1; border-bottom: 1px dotted #bbb; margin-bottom: 4pt; }
"""


def build_html(edition: str, runner: Runner | None, pages: dict[str, int] | None = None) -> tuple[str, list]:
    bodies, toc_entries = [], []
    for k, item in enumerate(structure(edition)):
        if "md" in item:
            md_text = shift_headings(item["md"], item["shift"], None)
        else:
            raw = item["path"].read_text(encoding="utf-8")
            if item["path"].name == "chapter.md":
                raw = with_outputs(raw, runner)
            md_text = shift_headings(raw, item["shift"], item.get("title"))
        body, heads = to_html(md_text, prefix=f"s{k}-")
        bodies.append(body)
        if item.get("toc", True):
            toc_entries += [(lvl, hid, text) for lvl, hid, text in heads if lvl <= item.get("toc_max", 2)]
    toc = ['<nav class="toc"><h1 id="contents">Contents</h1><ul>']
    for lvl, hid, text in toc_entries:
        num = (pages or {}).get(norm(text), "")
        toc.append(f'<li class="l{lvl}"><a href="#{hid}">{html.escape(text)}</a><span class="dots"></span>'
                   f'<span class="pg">{num}</span></li>')
    toc.append("</ul></nav>")
    version = re.search(r'version = "([^"]+)"', (ROOT / "pyproject.toml").read_text(encoding="utf-8")).group(1)
    label = "Teacher edition" if edition == "teacher" else "Student edition"
    today = dt.date.today().isoformat()
    title_page = f"""<section class="titlepage"><div class="t1">{TITLE}</div><div class="t2">{SUBTITLE}</div>
<div class="ed">{label}</div>
<div class="meta">Ram Chandra Giri and contributors<br>Version {version} · built {today}<br>
Text CC BY 4.0 · Code MIT · Datasets: see each source</div></section>"""
    credits = f"""<section class="credits"><p><strong>{TITLE}</strong> ({label}). Version {version}, built {today}.</p>
<p>“Data Science from Nepal (डेटा विज्ञान)” by Ram Chandra Giri and contributors is licensed
under Creative Commons Attribution 4.0 International (CC BY 4.0), <span class="ref">https://creativecommons.org/licenses/by/4.0/</span>.
You may copy, print, translate and adapt this book for any purpose, including textbooks, provided you give credit, link
to the licence and say if changes were made. Code examples are MIT-licensed.</p>
<p><strong>Data.</strong> Practice tables shipped with the book are <strong>SYNTHETIC</strong> (invented numbers, CC0) and
must never be quoted as facts about Nepal. Real datasets keep their publishers' licences, listed in Appendix A; credit the
publisher whenever you use them.</p>
<p><strong>Source and corrections:</strong> https://github.com/rcgiri-physics/data-science-nepal</p>
<p>Code examples in the chapters were run while building this edition; their printed output and charts appear under
each example.</p></section>"""
    style = CSS.replace("__FOOTER__", f"{TITLE} · {label}") + HtmlFormatter(style="friendly").get_style_defs(".highlight")
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE} — {label}</title>'
           f"<style>{style}</style></head><body>{title_page}{credits}{''.join(toc)}{''.join(bodies)}</body></html>")
    return doc, toc_entries


def norm(text: str) -> str:
    """Matching key for headings: Chrome's PDF outline may drop spaces at line breaks, so ignore all whitespace."""
    return re.sub(r"\s+", "", text).lower()


# --------------------------------------------------------------------------------------------- pdf
def find_browser() -> str | None:
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"):
        if shutil.which(name):
            return shutil.which(name)
    return None


def print_pdf(browser: str, html_path: Path, pdf_path: Path) -> None:
    with tempfile.TemporaryDirectory() as profile:
        cmd = [browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
               "--generate-pdf-document-outline", f"--user-data-dir={profile}",
               f"--print-to-pdf={pdf_path}", html_path.resolve().as_uri()]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=900)


def outline_pages(pdf_path: Path) -> dict[str, int]:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    pages: dict[str, int] = {}

    def walk(items):
        for it in items:
            if isinstance(it, list):
                walk(it)
            else:
                title = norm(it.title)
                half = len(title) // 2
                if len(title) % 2 == 0 and title[:half] == title[half:]:    # Chrome sometimes doubles titles
                    title = title[:half]
                pages.setdefault(title, reader.get_destination_page_number(it) + 1)

    walk(reader.outline)
    return pages


# --------------------------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--edition", choices=["student", "teacher", "both"], default="both")
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--no-run", action="store_true")
    args = ap.parse_args()
    DIST.mkdir(exist_ok=True)
    editions = ["student", "teacher"] if args.edition == "both" else [args.edition]
    browser = None if args.html_only else find_browser()
    if not args.html_only and browser is None:
        print("No Chrome/Chromium/Edge found: writing HTML only. Set CHROME=/path/to/browser to print PDFs.")
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        for csv in (ROOT / "datasets").glob("*/clean/*.csv"):
            shutil.copy(csv, workdir / csv.name)
        runner = None if args.no_run else Runner(workdir)
        for edition in editions:
            html_path = DIST / f"data-science-nepal-{edition}.html"
            doc, toc = build_html(edition, runner)
            html_path.write_text(doc, encoding="utf-8")
            print(f"wrote {html_path.relative_to(ROOT)} ({len(toc)} contents entries)")
            if browser:
                pdf_path = DIST / f"data-science-nepal-{edition}.pdf"
                print_pdf(browser, html_path, pdf_path)
                pages = outline_pages(pdf_path)
                doc, _ = build_html(edition, runner, pages)       # second pass: page numbers in the contents
                html_path.write_text(doc, encoding="utf-8")
                print_pdf(browser, html_path, pdf_path)
                from pypdf import PdfReader

                n = len(PdfReader(str(pdf_path)).pages)
                missing = sum(1 for _, _, t in toc if norm(t) not in pages)
                print(f"wrote {pdf_path.relative_to(ROOT)} ({n} pages; {missing} contents entries without a page number)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
