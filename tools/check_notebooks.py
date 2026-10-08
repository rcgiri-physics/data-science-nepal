"""CI gate: execute every notebook under curriculum/ top to bottom; fail on any error.

Notebooks run with their own folder as working directory and must not need the internet.
Run: python tools/check_notebooks.py [path-to-one-notebook]
"""
from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent


def run(path: Path) -> str | None:
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=120, kernel_name="python3",
                            resources={"metadata": {"path": str(path.parent)}})
    try:
        client.execute()
    except Exception as exc:  # noqa: BLE001
        return f"{path.relative_to(ROOT)}: {type(exc).__name__}: {str(exc)[:400]}"
    return None


def main() -> int:
    targets = [Path(a).resolve() for a in sys.argv[1:]] or sorted((ROOT / "curriculum").rglob("*.ipynb"))
    failures = [r for r in (run(p) for p in targets) if r]
    for p in targets:
        print("ran", p.relative_to(ROOT))
    if failures:
        print("FAILED:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"OK: {len(targets)} notebooks executed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
