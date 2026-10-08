"""Assemble the website source and build it with MkDocs (and optionally JupyterLite).

MkDocs wants everything under one docs folder; this repo keeps curriculum/ and datasets/ at the top level, so we stage a
copy in .site_src/ and build from there.

Usage:
    python tools/build_site.py            # builds site/
    python tools/build_site.py --lite     # also builds JupyterLite into site/lite (needs jupyterlite-core + pyodide kernel)
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / ".site_src"
SKIP = shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints", ".gitkeep")


def stage() -> None:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    shutil.copytree(ROOT / "docs", STAGE, ignore=SKIP)
    shutil.copytree(ROOT / "curriculum", STAGE / "curriculum", ignore=SKIP)
    shutil.copytree(ROOT / "datasets", STAGE / "datasets", ignore=shutil.ignore_patterns("raw", "__pycache__"))
    shutil.copytree(ROOT / "community", STAGE / "community", ignore=SKIP)
    shutil.copytree(ROOT / "pilots", STAGE / "pilots", ignore=SKIP)
    for f in ("README.md", "ROADMAP.md", "CONTRIBUTING.md", "GOVERNANCE.md", "ATTRIBUTION.md", "THIRD_PARTY.md",
              "CODE_OF_CONDUCT.md", "LICENSE-CONTENT.md"):
        shutil.copy(ROOT / f, STAGE / f)
    # README.md is the site home
    (STAGE / "index.md").write_text((ROOT / "README.md").read_text(encoding="utf-8"), encoding="utf-8")


def main() -> int:
    stage()
    rc = subprocess.call([sys.executable, "-m", "mkdocs", "build", "-q", "-f", str(ROOT / "mkdocs.yml")])
    if rc != 0:
        return rc
    if "--lite" in sys.argv:
        lite_src = ROOT / ".lite_contents"
        if lite_src.exists():
            shutil.rmtree(lite_src)
        lite_src.mkdir()
        shutil.copytree(ROOT / "curriculum", lite_src / "curriculum", ignore=shutil.ignore_patterns("__pycache__", "*.md"))
        shutil.copytree(ROOT / "datasets", lite_src / "datasets", ignore=shutil.ignore_patterns("raw", "scripts"))
        rc = subprocess.call(["jupyter", "lite", "build", "--contents", str(lite_src),
                              "--output-dir", str(ROOT / "site" / "lite")])
    return rc


if __name__ == "__main__":
    sys.exit(main())
