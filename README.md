# डेटा विज्ञान / Data Science Nepal

A free, openly licensed, bilingual (Nepali + English) data science curriculum for
**Grades 8–12** in Nepal's schools, built around **Nepali datasets** (fetched from their publishers, with synthetic practice tables included), with teacher-ready
materials, designed so the Curriculum Development Centre (CDC) can adopt or adapt it.

> **Learning on your own, anywhere in the world?** The methods here work with any data; the Nepali datasets are the
> worked examples. Start with the [book](book/) (student edition) and the free in-browser notebooks, no install needed.

> **Version 0.1.0.** Flagship units: Grade 8 Unit 1 and Grade 9 Unit 3. See [ROADMAP.md](ROADMAP.md) for what is next.

## Read it as a book
The curriculum is also a **book in two editions** — a *student edition* to learn from on your own and a *teacher
edition* with teacher guides, full answer keys and a handbook on teaching data-science foundations — plus a part on how
to keep learning after Grade 12 (study methods, roadmap, books, courses, careers). Build the PDFs with
`python tools/build_book.py` (see [book/README.md](book/README.md)); GitHub Actions also builds them as an artifact.

Every chapter has worked examples (the code in them is run in CI), common mistakes, a unit summary, graded practice
exercises and **exercises with real data** from 20 free datasets ([docs/datasets/free-datasets.md](docs/datasets/free-datasets.md)),
each with an offline fallback.

## Who is it for?
* **Students (13–18):** book-like chapters, notebooks, mini-projects.
* **Teachers / CDC reviewers:** facilitation guides, alignment maps, rubrics, pilot kit.

## Two tracks
| Track | Tools | Use it in |
|---|---|---|
| **A: No-code** | paper, calculator, spreadsheet, [CODAP](https://codap.concord.org) | compulsory Maths / Science / Social / Health (all students) |
| **B: Code** | SQL (SQLite), Python (pandas) in the browser via JupyterLite | optional Computer Science, ICT clubs, Grades 11–12 |

## Scope and sequence
| Grade | Theme | Unit count |
|---|---|---|
| 8 | Data detectives (no code) | 8 |
| 9 | Data wranglers (spreadsheets → SQL → first Python) | 8 |
| 10 | Data analysts (Python, intro ML, dashboards) | 8 |
| 11 | Data scientists I (uncertainty, time, space) | 8 |
| 12 | Data scientists II (modelling, capstone) | 8 |
| Beyond 12 | Pathways and careers | 1 chapter |

Browse: [`curriculum/`](curriculum/) · Framework: [`curriculum/framework/`](curriculum/framework/) ·
Book: [`book/`](book/) · Teachers: [`docs/for-teachers/`](docs/for-teachers/) and [`book/teaching/`](book/teaching/) ·
After Grade 12: [`book/beyond/`](book/beyond/) · CDC pack: [`docs/for-cdc/`](docs/for-cdc/)

## Try it in 5 minutes
1. **No computer?** Print `curriculum/grade-08/unit-01-what-is-data/worksheets/` and follow the teacher guide.
2. **With a computer:** `pip install -r requirements.txt`, then `mkdocs serve` for the site, or open
   `curriculum/grade-09/unit-03-sql-basics/notebooks/census_sql.ipynb` in Jupyter / JupyterLite.
3. **Offline school bundle:** `python tools/build_offline_bundle.py` → `dist/school-bundle.zip`.
4. **The book (PDF):** `python tools/build_book.py` → `dist/data-science-nepal-student.pdf` and `…-teacher.pdf`.

## About this material
Built for Nepal's schools and open to learners everywhere. This material was structured and drafted with the
assistance of AI, then curated, verified and adapted by the author. Third-party sources are credited in
[THIRD_PARTY.md](THIRD_PARTY.md); please report anything that looks uncredited by opening an issue.

## Licences and credit
* Content: **CC BY 4.0**; code: **MIT**; datasets keep their own licence (see dataset cards).
* Reuse is free with credit — see [ATTRIBUTION.md](ATTRIBUTION.md).

## Contribute
Teachers, students, statisticians, translators: see [CONTRIBUTING.md](CONTRIBUTING.md). You do
not need to code — open an issue with the "new dataset" or "teacher feedback" template.

Maintainer: Ram Chandra Giri (rcgiri.physics@gmail.com)
