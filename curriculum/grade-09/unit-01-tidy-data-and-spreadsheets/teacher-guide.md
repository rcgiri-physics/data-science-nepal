# Teacher guide — Grade 9, Unit 1: Tidy data and spreadsheets

**Time:** 3 lessons + project (about 5 periods). **Track:** A/B (spreadsheet).

| # | Lesson | Time |
|---|---|---|
| 1 | Rows, columns and cell types | 40–45 min |
| 2 | Formulas | 40–45 min |
| 3 | Sort, filter and pivot | 40–45 min |
| P | Unit project: Spreadsheet fact sheet | 2 periods |

## Before you start
* Materials: Computers with a spreadsheet, or printed grids. Open `datasets/census-districts/clean/districts_synthetic.csv`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Spreadsheet units can be done as a paper grid: draw the table, write formulas as words ('sum of column C').

## Common misconceptions
* Merging cells and adding totals inside the data area breaks sorting and filtering.
* Typing numbers with units ('45 min') makes them text.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Rows, columns and cell types**
1. In the district table, what is one row?  
   *Answer:* One district.
2. Why avoid '45 min' in a cell?  
   *Answer:* It becomes text; use 45 and put 'min' in the header.
3. Why avoid merged cells?  
   *Answer:* They break sorting, filtering and formulas.

**Lesson 2: Formulas**
1. Formula for the sum of C2:C78?  
   *Answer:* =SUM(C2:C78)
2. What does COUNTIF(B2:B78,"Hill") do?  
   *Answer:* Counts the rows where column B equals Hill.
3. Why use ranges instead of typing numbers?  
   *Answer:* Formulas update automatically if data change.

**Lesson 3: Sort, filter and pivot**
1. Which tool answers 'total population for each belt'?  
   *Answer:* A pivot table (group by belt, sum population).
2. A filter on belt = Hill does what?  
   *Answer:* Shows only Hill rows (it does not delete the rest).
3. A pivot table in SQL is closest to…  
   *Answer:* GROUP BY.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

> **Note (2026-10-11 revision):** the chapter now uses the real column letters of `districts_synthetic.csv`
> (E = population, C = ecological_belt, J = literacy_pct). The check questions use generic ranges on purpose.

## Answers: practice exercises
1. `D10`; `G2:G78`.
2. (a) `=MAX(E2:E78)` (1,607,726) (b) `=COUNTIF(D2:D78,3)` (12) (c) `=SUM(F2:F78)` (5,957,747).
3. `COUNT` counts cells containing numbers; `COUNTA` counts all non-empty cells (text too).
4. Population ÷ households = average household size (persons per household); header `household_size`.
5. `=E2/$N$1` (format as percent).
6. Filter `ecological_belt` = Mountain, then sort by `literacy_pct` ascending; read the first three
   (Mountain-03 62.6, Mountain-15 63.0, Mountain-14 63.4). Or a sort by belt then literacy.
7. Tidy (long) form: columns `belt, year, population_million`; four rows: Mountain 2011 1.78, Mountain 2021 1.77,
   Hill 2011 11.39, Hill 2021 11.76 (numbers in cells, unit in header). Note: these numbers are illustrative.
8. It is the mean of 77 district percentages, each counting equally; big and small districts have equal weight.
   The people-weighted rate needs literate people ÷ people aged 5+ summed over districts.
9. Every row is divided by E2 (Hill-01's population) instead of its own population: the shares are wrong and
   many exceed 100%. Spot it by checking one row by hand or seeing values > 1.
10. e.g. total population (SUM), most crowded district (density column + sort: Terai-15, ≈ 954 people/km²),
    belt with most people (pivot: Terai), share of districts with literacy > 75% (COUNTIF ÷ 77); chart: bar chart of
    belt populations.

Lesson 2 activity: most crowded district is Terai-15 (1,116,962 people on 1,170.6 km² ≈ 954 per km²).
Lesson 3 activity: province 7 has 16 districts; provinces 1 and 7 tie for most districts (16); province 7 has the
most people (7,500,730).

## Real-data exercises: notes
* **R1** Typical problems: years as columns (wide), station name and number in one cell or two header rows,
  missing years blank or marked "-" / "NA" (which makes cells text). `AVERAGE` skips blanks but not text like "-";
  replace with blanks. Wettest stations are usually around Pokhara/Lumle (> 3,500 mm); driest in Mustang/Dolpa
  rain shadow.
* **R2** Population in 2000 ≈ 23–24 million; latest WDI ≈ 29.6 million (2025). GDP per capita and life expectancy
  rise; exact values depend on the download date.
* **R3** Bagmati and Madhesh have the largest populations; Madhesh has the largest households; check with the
  portal.
