"""CI gate: every dataset folder needs a DATASET_CARD.md with a verified licence.

A card starts with a YAML front-matter block (between '---' lines) that must contain
the required keys below. Run: python tools/validate_dataset_cards.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "name", "source_url", "publisher", "licence", "licence_status",
    "date_accessed", "grades", "synthetic", "redistribution_allowed",
]
LICENCE_STATUS = {"verified", "partly-verified", "synthetic-cc0", "not-redistributed"}


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("card must start with a YAML front-matter block")
    block = text.split("---", 2)[1]
    return yaml.safe_load(block) or {}


def main() -> int:
    problems: list[str] = []
    folders = [p for p in (ROOT / "datasets").iterdir() if p.is_dir()]
    if not folders:
        problems.append("no dataset folders found")
    for folder in sorted(folders):
        card = folder / "DATASET_CARD.md"
        if not card.exists():
            problems.append(f"{folder.name}: missing DATASET_CARD.md")
            continue
        try:
            meta = read_front_matter(card)
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{folder.name}: {exc}")
            continue
        for key in REQUIRED:
            if key not in meta or meta[key] in (None, ""):
                problems.append(f"{folder.name}: missing '{key}'")
        if meta.get("licence_status") not in LICENCE_STATUS:
            problems.append(f"{folder.name}: licence_status must be one of {sorted(LICENCE_STATUS)}")
        if meta.get("synthetic") and "SYNTHETIC" not in card.read_text(encoding="utf-8"):
            problems.append(f"{folder.name}: synthetic dataset card must say SYNTHETIC in the body")
        # Rule: nothing in raw/ or clean/ unless redistribution is allowed.
        has_files = any(
            f.is_file() and f.name != ".gitkeep"
            for sub in ("raw", "clean") if (folder / sub).exists()
            for f in (folder / sub).rglob("*")
        )
        if has_files and not meta.get("redistribution_allowed") and not meta.get("synthetic"):
            problems.append(f"{folder.name}: has data files but redistribution_allowed is false")
    if problems:
        print("Dataset card problems:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"OK: {len(folders)} dataset cards valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
