# The book

The curriculum can be read as one book in two editions, built from the same markdown sources:

* **Student edition** — front matter, the 40 chapters (with unit project briefs), the capstone kit, "After Grade 12",
  appendices, and answers to the ★ exercises.
* **Teacher edition** — everything in the student edition (except Appendix G) plus each unit's teacher guide (timings,
  misconceptions, answers to all exercises and notes on the real-data exercises) and the handbook *Teaching
  data-science foundations*.

## Build

```bash
pip install -r requirements.txt
python tools/build_book.py
```

Output: `dist/data-science-nepal-student.pdf` and `dist/data-science-nepal-teacher.pdf` (plus the HTML they are printed
from). Printing needs Chrome, Chromium or Edge; set `CHROME=/path/to/browser` if it is not found. `--html-only` skips
printing; `--no-run` skips executing chapter code. The GitHub Actions workflow `build-book.yml` builds both PDFs as a
downloadable artifact.

While building, the Python and SQL examples in every chapter are run on the shipped synthetic data and their output,
result tables and charts are placed under each example. (`tools/check_chapter_code.py` runs the same code in CI.)

## Where the content lives

| Book part | Source |
|---|---|
| Preface, How to use, Setting up, The cycle | `book/front/` |
| Part openers for Grades 8–12 | `book/parts/` |
| Chapters, project briefs, teacher guides | `curriculum/grade-*/unit-*/` (`chapter.md`, `project.md`, `teacher-guide.md`) |
| Capstone kit | `curriculum/grade-12/capstone-kit/` |
| Handbook: Teaching data-science foundations | `book/teaching/` |
| After Grade 12: how to keep learning | `book/beyond/` |
| Appendix A: Free real datasets | `docs/datasets/free-datasets.md` |
| Appendix B: Glossary | `curriculum/framework/glossary.md` |
| Appendices C–F: cheat sheets and formulas | `book/appendix/` |
| Appendix G: Answers to ★ exercises | generated from the teacher guides |

Edit the source files, not the generated HTML/PDF. Chapter text stays in `curriculum/` so the website, notebooks and book
never drift apart.
