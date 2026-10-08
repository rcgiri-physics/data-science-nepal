"""CI gate: every unit folder is complete and consistent.

Checks per unit: chapter.md, teacher-guide.md, project.md, quiz.yml, datasets.yml exist; quiz is valid YAML with questions;
every dataset named in datasets.yml has a dataset card; every notebook mentioned in chapter.md exists.
Run: python tools/check_units.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["chapter.md", "teacher-guide.md", "project.md", "quiz.yml", "datasets.yml"]


def main() -> int:
    problems: list[str] = []
    units = sorted(ROOT.glob("curriculum/grade-*/unit-*"))
    for u in units:
        rel = u.relative_to(ROOT).as_posix()
        for name in REQUIRED:
            if not (u / name).exists():
                problems.append(f"{rel}: missing {name}")
        if (u / "quiz.yml").exists():
            quiz = yaml.safe_load((u / "quiz.yml").read_text(encoding="utf-8"))
            if not quiz.get("questions"):
                problems.append(f"{rel}: quiz has no questions")
        if (u / "datasets.yml").exists():
            for d in yaml.safe_load((u / "datasets.yml").read_text(encoding="utf-8")).get("datasets", []):
                if not (ROOT / "datasets" / d / "DATASET_CARD.md").exists():
                    problems.append(f"{rel}: dataset '{d}' has no dataset card")
        if (u / "chapter.md").exists():
            text = (u / "chapter.md").read_text(encoding="utf-8")
            for nb in re.findall(r"`notebooks/([\w\-]+\.ipynb)`", text):
                if not (u / "notebooks" / nb).exists():
                    problems.append(f"{rel}: chapter mentions missing notebook {nb}")
            if "## Unit project" not in text:
                problems.append(f"{rel}: chapter lacks the PPDAC project section")
    if problems:
        print("Unit problems:")
        for p in problems:
            print("  -", p)
        return 1
    n_lessons = sum((u / "chapter.md").read_text(encoding="utf-8").count("\n## Lesson ") for u in units)
    print(f"OK: {len(units)} units, {n_lessons} lessons")
    return 0


if __name__ == "__main__":
    sys.exit(main())
