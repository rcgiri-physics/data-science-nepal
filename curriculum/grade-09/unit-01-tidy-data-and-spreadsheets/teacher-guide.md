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
