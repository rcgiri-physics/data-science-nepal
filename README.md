# डेटा विज्ञान / Data Science Nepal

A free, openly licensed, bilingual (Nepali + English) data science curriculum for
**Grades 8–12** in Nepal's schools, built on **real Nepali data**, with teacher-ready
materials, designed so the Curriculum Development Centre (CDC) can adopt or adapt it.

> **Status: v0.1.0 (draft, pre-pilot).** Release candidate = Grade 8 Unit 1 + Grade 9 Unit 3; all other units are unreleased drafts. Content has not yet been classroom-tested and
> Nepali text needs teacher-editor review. See [ROADMAP.md](ROADMAP.md).

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
Teachers: [`docs/for-teachers/`](docs/for-teachers/) · CDC pack: [`docs/for-cdc/`](docs/for-cdc/)

## Try it in 5 minutes
1. **No computer?** Print `curriculum/grade-08/unit-01-what-is-data/worksheets/` and follow the teacher guide.
2. **With a computer:** `pip install -r requirements.txt`, then `mkdocs serve` for the site, or open
   `curriculum/grade-09/unit-03-sql-basics/notebooks/census_sql.ipynb` in Jupyter / JupyterLite.
3. **Offline school bundle:** `python tools/build_offline_bundle.py` → `dist/school-bundle.zip`.

## Licences and credit
* Content: **CC BY 4.0**; code: **MIT**; datasets keep their own licence (see dataset cards).
* Reuse is free with credit — see [ATTRIBUTION.md](ATTRIBUTION.md).

## Contribute
Teachers, students, statisticians, translators: see [CONTRIBUTING.md](CONTRIBUTING.md). You do
not need to code — open an issue with the "new dataset" or "teacher feedback" template.

Maintainer: Ram Chandra Giri (rcgiri.physics@gmail.com)
