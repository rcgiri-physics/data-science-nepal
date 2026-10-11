"""CI gate: run the Python and SQL code blocks printed in chapters, so the book never shows code that fails.

Each chapter's ```python blocks run top to bottom in one shared namespace (like cells of a notebook), in a temporary
folder that holds every shipped synthetic CSV, so `pd.read_csv("districts_synthetic.csv")` works. ```sql blocks run
against an in-memory SQLite database with these tables:

    districts, schools        census-districts
    survey                    class-survey-synthetic
    climate                   climate-monthly
    health                    health-synthetic
    air                       kathmandu-air-quality

A block is skipped when it contains `needs internet`, `not run`, or a `___` blank for students to fill in.
Run: python tools/check_chapter_code.py [chapter.md ...]
"""
from __future__ import annotations

import contextlib
import io
import os
import re
import shutil
import sqlite3
import sys
import tempfile
import traceback
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"^```(python|sql)[^\n]*\n(.*?)^```", re.S | re.M)
SKIP_MARKERS = ("needs internet", "not run", "___")
SQL_TABLES = {
    "districts": "census-districts/clean/districts_synthetic.csv",
    "schools": "census-districts/clean/schools_synthetic.csv",
    "survey": "class-survey-synthetic/clean/class_survey_synthetic.csv",
    "climate": "climate-monthly/clean/climate_monthly_synthetic.csv",
    "health": "health-synthetic/clean/health_synthetic.csv",
    "air": "kathmandu-air-quality/clean/air_daily_synthetic.csv",
}


def check_chapter(path: Path, workdir: Path) -> tuple[int, int, list[str]]:
    text = path.read_text(encoding="utf-8")
    namespace: dict = {"__name__": "__chapter__"}
    con = sqlite3.connect(":memory:")
    for table, rel in SQL_TABLES.items():
        pd.read_csv(ROOT / "datasets" / rel).to_sql(table, con, index=False)
    ran = skipped = 0
    problems: list[str] = []
    for match in BLOCK.finditer(text):
        lang, code = match.group(1), match.group(2)
        line = text.count("\n", 0, match.start()) + 1
        if any(m in code for m in SKIP_MARKERS):
            skipped += 1
            continue
        ran += 1
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                if lang == "python":
                    exec(compile(code, f"{path.name}:{line}", "exec"), namespace)  # noqa: S102 (our own chapters)
                else:
                    for stmt in [s for s in code.split(";") if s.strip() and not _only_comments(s)]:
                        con.execute(stmt).fetchall()
        except Exception:  # noqa: BLE001
            problems.append(f"{path.relative_to(ROOT)}:{line} ({lang})\n"
                            + "".join(traceback.format_exc(limit=1).splitlines(True)[-3:]))
        finally:
            plt.close("all")
    return ran, skipped, problems


def _only_comments(stmt: str) -> bool:
    return all(not ln.strip() or ln.strip().startswith("--") for ln in stmt.splitlines())


def main() -> int:
    targets = [Path(a).resolve() for a in sys.argv[1:]] or sorted(ROOT.glob("curriculum/grade-*/unit-*/chapter.md"))
    plt.show = lambda *a, **k: None  # charts are drawn but not displayed
    total_ran = total_skipped = 0
    all_problems: list[str] = []
    old_cwd = Path.cwd()
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        for csv in (ROOT / "datasets").glob("*/clean/*.csv"):
            shutil.copy(csv, workdir / csv.name)
        os.chdir(workdir)
        try:
            for path in targets:
                ran, skipped, problems = check_chapter(path, workdir)
                total_ran += ran
                total_skipped += skipped
                all_problems += problems
        finally:
            os.chdir(old_cwd)
    if all_problems:
        print("Chapter code problems:")
        for p in all_problems:
            print("  -", p)
        return 1
    print(f"OK: {len(targets)} chapters, {total_ran} code blocks ran, {total_skipped} skipped (internet / exercises)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
