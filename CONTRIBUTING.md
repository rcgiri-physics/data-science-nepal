# Contributing

Everyone is welcome — teachers, students, statisticians, translators, developers.

## Ways to help
1. **New dataset** (with a dataset card — licence is mandatory): open the *new-dataset* issue.
2. **New problem / project** for an existing unit: open *new-lesson*.
3. **Translation** (Nepali, and later Maithili, Nepal Bhasa, Tharu…): see `community/translations/`.
4. **Fix an error**: open *bug* or send a pull request.
5. **Teacher feedback / pilot report**: open *teacher-feedback*, or add a file to `pilots/`.
6. **Student gallery**: see `community/student-gallery/README.md` (consent required).

## Ground rules
* **Never commit a dataset without a verified licence in its card.**
* **Never commit restricted data** (DHS, census/NLSS microdata, anything needing registration).
* No personal data about real children. Anonymise; get consent.
* Follow the lesson anatomy in `docs/pedagogy/lesson-anatomy.md` and the PPDAC headings.
* Notebooks must run top-to-bottom offline: `python tools/check_notebooks.py`.
* Run `python tools/validate_dataset_cards.py` before opening a PR.

## Review
One maintainer plus one subject reviewer (teacher or statistician) per PR. Labels:
`grade-8`…`grade-12`, `dataset`, `translation`, `needs-teacher-review`.

By contributing you agree your content is licensed CC BY 4.0 and your code MIT.
Contributors are credited in `CONTRIBUTORS.md`.
