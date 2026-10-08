# Grade 9 — Data wranglers (tidy data and first code)

**Tools:** spreadsheet, SQLite, Python/pandas in the browser · **Units:** 8 · **Lessons:** 27 (+ projects)

Grade 9 teaches students to *wrangle* data: tidy tables, cleaning, then SQL (SQLite) and a first taste of Python and
pandas, always on district and school tables. Track A units (spreadsheet) run in compulsory classes; Track B units
(SQL, Python) fit optional Computer Science and clubs. Notebooks use the **synthetic** district table so they run offline;
swap in the real census table after `python tools/fetch_data.py census-districts`.

| Unit | Title | Lessons | Track | Project |
|---|---|---|---|---|
| 1 | [Tidy data and spreadsheets](unit-01-tidy-data-and-spreadsheets/chapter.md) | 3 | A/B (spreadsheet) | Spreadsheet fact sheet |
| 2 | [Cleaning data](unit-02-cleaning-data/chapter.md) | 4 | A/B (spreadsheet + notes) | Clean it and log it |
| 3 | [SQL basics on district data](unit-03-sql-basics/chapter.md) | 5 | B (code: SQL/SQLite) | Which districts are changing? |
| 4 | [First steps in Python](unit-04-first-python/chapter.md) | 3 | B (code: Python) | My first data script |
| 5 | [Tables in pandas](unit-05-pandas-basics/chapter.md) | 4 | B (code: pandas) | Same question, SQL and pandas |
| 6 | [Charts that work](unit-06-charts-that-work/chapter.md) | 3 | B (code: matplotlib) | One chart, one claim |
| 7 | [Percent, rate and per-capita](unit-07-percent-rate-per-capita/chapter.md) | 3 | A/B | Rate detective |
| 8 | [Grade 9 project: which districts are changing?](unit-08-grade-9-project/chapter.md) | 2 | A/B (project) | Which districts are changing? |

Flagship project: **Which districts are changing? — census-style table to poster plus a simple SQL report**

Each unit folder holds: `chapter.md` (student), `teacher-guide.md`, `project.md`, `quiz.yml`, `datasets.yml`
(and `notebooks/` where code is used). Nepali chapters: see `community/translations/STATUS.md`.
