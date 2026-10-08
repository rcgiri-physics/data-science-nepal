# Datasets

Rules (also enforced in CI by `tools/validate_dataset_cards.py`):

1. Every dataset folder has a `DATASET_CARD.md` with source, publisher, licence, licence status, date accessed, grades.
2. **Never commit a dataset without a verified licence in its card.**
3. **Real data is fetched from the original publisher** with `python tools/fetch_data.py <name>`; `raw/` is git-ignored.
4. The repo ships only small **SYNTHETIC** practice tables in `clean/` (CC0, invented numbers, fictional district names).
5. Restricted data (DHS, census/NLSS microdata) is never added.

| Folder | Grades | Ships | Real-data licence |
|---|---|---|---|
| `class-survey-synthetic` | 8–9 | 36-row survey | CC0 (synthetic) |
| `census-districts` | 8–12 | 77-row district table + schools table | real: CC BY-SA (ODN preliminary) |
| `kathmandu-air-quality` | 9–11 | 731 days of messy PM2.5 | real: CC BY-SA (ODN) |
| `climate-monthly` | 10–12 | 360 months temp + rain | real: CC BY 4.0 (World Bank CCKP) |
| `health-synthetic` | 11–12 | 1,500 records | real DHS: not redistributable |

To add a dataset: copy `docs/templates/DATASET_CARD_TEMPLATE.md`, fill every field, open a PR.
Full licence evidence: `docs/alignment/dataset-licence-register.md`.
