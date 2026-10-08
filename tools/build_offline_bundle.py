"""Build dist/school-bundle.zip: curriculum, shipped (synthetic) datasets, licences and a start page.

The bundle works from a USB stick with no internet. If you also want in-browser Python offline, build
JupyterLite first (see jupyterlite/README.md) and it is added automatically from jupyterlite/_output.

Usage:  python tools/build_offline_bundle.py
"""
from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
INCLUDE = ["curriculum", "datasets", "docs", "README.md", "LICENSE-CONTENT.md", "LICENSE-CODE",
           "ATTRIBUTION.md", "THIRD_PARTY.md", "requirements.txt"]
SKIP_PARTS = {".venv", "__pycache__", ".ipynb_checkpoints", ".git"}

START = """<!doctype html><meta charset="utf-8"><title>Data Science Nepal - school bundle</title>
<h1>डेटा विज्ञान / Data Science Nepal</h1>
<p>Open <code>curriculum/</code> for grades 8-12. Read <code>README.md</code> first. Licence: CC BY 4.0 (content), MIT (code).</p>
<p>Credit: see ATTRIBUTION.md.</p>
"""


def add_tree(zf: zipfile.ZipFile, base: Path, arc_prefix: str = "") -> int:
    n = 0
    paths = [base] if base.is_file() else sorted(base.rglob("*"))
    for p in paths:
        if p.is_dir() or SKIP_PARTS & set(p.parts):
            continue
        zf.write(p, (Path(arc_prefix) / p.relative_to(ROOT)).as_posix())
        n += 1
    return n


def main() -> int:
    DIST.mkdir(exist_ok=True)
    out = DIST / "school-bundle.zip"
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("START-HERE.html", START)
        for item in INCLUDE:
            p = ROOT / item
            if p.exists():
                count += add_tree(zf, p)
        lite = ROOT / "jupyterlite" / "_output"
        if lite.exists():
            for p in sorted(lite.rglob("*")):
                if p.is_file():
                    zf.write(p, ("jupyterlite/" + p.relative_to(lite).as_posix()))
                    count += 1
    print(f"wrote {out.relative_to(ROOT)} with {count} files ({out.stat().st_size/1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
