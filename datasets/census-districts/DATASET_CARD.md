---
name: census-districts
source_url: https://censusnepal.cbs.gov.np/results
publisher: National Statistics Office (NSO) Nepal - REAL data; this folder ships only
  a SYNTHETIC look-alike
licence: 'Synthetic tables: CC0. Real preliminary census data on Open Data Nepal:
  CC BY-SA (re-check final results terms)'
licence_status: synthetic-cc0
date_accessed: '2026-10-07'
grades:
- 8
- 9
- 10
- 11
- 12
synthetic: true
redistribution_allowed: true
---

# Census districts (SYNTHETIC practice tables)

**SYNTHETIC: every number in `clean/*.csv` is invented** by `tools/make_synthetic_data.py` (seed 2026).
District names such as `Hill-07` are fictional on purpose. Do not quote these numbers as facts about Nepal.

## Files
* `districts_synthetic.csv` - 77 rows. `district_id, district, ecological_belt, province, population, households, area_km2, male, female, literacy_pct, absentee_population`
* `schools_synthetic.csv` - 77 rows. `district_id, n_secondary_schools, enrolment_girls, enrolment_boys` (join on `district_id`)

## Real data (to use after checking the licence)
1. Open the landing page in `source.yml`, read the licence, copy the direct CSV link into `source.yml`.
2. `python tools/fetch_data.py census-districts`, then paste the printed sha256 into `source.yml`.
3. The real file keeps its own licence (CC BY-SA on ODN) and must not be committed unless the maintainers agree; `raw/` is git-ignored.

## Known problems / ethics
Real census tables have Nepali/English district names and BS-vs-AD issues. Never use microdata (restricted).
Sensitive attributes (caste/ethnicity, disability) need careful framing: describe groups, never rank people.
