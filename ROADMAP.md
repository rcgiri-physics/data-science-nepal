# Roadmap

Where the project is heading and where contributors can help. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Available now (v0.1.0)
* 40 units (Grades 8–12), 123 lessons, with teacher guides, projects, quizzes and 28 runnable notebooks.
* Grade 8 Unit 1 and Grade 9 Unit 3 are the flagship units, with Nepali chapters and worksheets.
* Dataset cards with licences, synthetic practice tables, offline school bundle, website and in-browser Python.
* Capstone kit, Beyond-Grade-12 chapter, teacher training outline, pilot protocol.

## Added in October 2026
* All 40 chapters expanded (≈ 92,000 words): explanations with worked examples, runnable code checked in CI, common
  mistakes, unit summaries, graded practice exercises with answers, and exercises with real data.
* A directory of 20 free real datasets with licences and offline fallbacks (`docs/datasets/free-datasets.md`).
* The book: student and teacher PDF editions (`tools/build_book.py`), a teaching handbook (`book/teaching/`) and an
  "After Grade 12" part on how to keep learning (`book/beyond/`).

## Next
* **Classroom pilots** in 3–5 schools (urban/rural, public/private, with/without internet); results published in `pilots/`.
* **Nepali** versions of the remaining units, reviewed by teachers (`community/translations/`); update the two existing
  Nepali chapters to the expanded text; review the new glossary terms (marked †).
* **Quizzes**: add interpretation questions beyond the Check questions (every unit quiz now has 6–15).
* **Notebooks**: worked real-data notebooks for datasets whose licences allow classroom copies.
* **Real data**: add fetch links and checksums for each dataset's original source (`tools/fetch_data.py`), with the licence text copied into the dataset card.
* **Alignment**: page-level references to the CDC and NEB syllabi in `docs/for-cdc/competency-map.md`.
* **More lessons** where pilots show gaps; sketchnotes and printable PDFs.
* **Additional datasets** (rainfall, earthquake recovery, school flash reports, OpenStreetMap) once their licences are confirmed.
* **v1.0**: a frozen, citable edition after pilot evidence is in.

## Help wanted
Teachers · statisticians and university partners · Nepali-language editors · pilot schools.
