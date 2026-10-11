# Teacher guide — Grade 9, Unit 2: Cleaning data

**Time:** 4 lessons + project (about 6 periods). **Track:** A/B (spreadsheet + notes).

| # | Lesson | Time |
|---|---|---|
| 1 | Missing values and error codes | 40–45 min |
| 2 | Duplicates and inconsistent names | 40–45 min |
| 3 | Units and types | 40–45 min |
| 4 | BS and AD dates, and the cleaning log | 40–45 min |
| P | Unit project: Clean it and log it | 2 periods |

## Before you start
* Materials: Messy air-quality table (`datasets/kathmandu-air-quality/clean/air_daily_synthetic.csv`: 25 blanks, four -999 codes).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Spreadsheet units can be done as a paper grid: draw the table, write formulas as words ('sum of column C').

## Common misconceptions
* Deleting every row with a problem. Sometimes the missingness itself tells a story.
* Fixing silently without a log.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Missing values and error codes**
1. Why is -999 not a real PM2.5 reading?  
   *Answer:* Concentrations cannot be negative; it is an error code.
2. What happens to the mean if we leave -999 in?  
   *Answer:* It is pulled down, giving a wrong low value.
3. What goes in a cleaning log?  
   *Answer:* What was found, what was changed, why, and how many rows.

**Lesson 2: Duplicates and inconsistent names**
1. Why do inconsistent spellings matter for GROUP BY?  
   *Answer:* They create separate groups for the same thing.
2. What is a lookup table?  
   *Answer:* A table mapping each variant to one standard name.
3. How can you spot duplicates in a spreadsheet?  
   *Answer:* Sort, or use conditional formatting / remove-duplicates after copying.

**Lesson 3: Units and types**
1. 2.5 hours in minutes?  
   *Answer:* 150.
2. Why put the unit in the header?  
   *Answer:* So cells can stay numeric.
3. What is wrong with '1,50' in some systems?  
   *Answer:* A comma may be read as decimal point or thousands separator; agree a rule.

**Lesson 4: BS and AD dates, and the cleaning log**
1. Roughly, BS year minus 57 gives…  
   *Answer:* The AD year (approximately; month matters).
2. Why store ISO dates?  
   *Answer:* They sort correctly and are unambiguous.
3. Why keep the original column?  
   *Answer:* So changes are reversible and checkable.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
1. 0 (no Grade 9 student is 0: probably missing coded as 0), 999 (an error code), blank (missing). Treat all three as
   missing and log it.
2. 2024-03-05; 2015-04-25; 2000-01-01.
3. 180; 105; 15.
4. Total = 60 × 10 = 600; remove −999: 600 − (−999) = 1,599 for 9 values; mean ≈ 177.7. (Shows how badly one
   code distorts a mean.)
5. e.g. Kavre, Kabhrepalanchok, Kavrepalanchowk, KAVRE → standard "Kavrepalanchok", काभ्रेपलाञ्चोक.
6. 2081 Kartik → 2024 (October–November, −57); 2080 Falgun → 2024 (February–March, −56); 2082 Baisakh 1 = 14 April
   2025 (check calendar).
7. Leading zeros vanish (001 → 1), codes no longer sort or match as text. Format the column as text before typing/
   importing, or re-pad with `=TEXT(A2,"000")`.
8. Higher: winter is the most polluted season, so missing winter days remove high values; the mean of the remaining
   days underestimates the year.
9. (i) Ask the student / check the paper form (best, but slow); (ii) mark missing (safe, but loses data); (iii)
   assume hours → 90 or minutes → 1.5 (fast, but may be wrong and must be logged).
10. Example log: 1 standardised district names chitwan/Chitawan → Chitwan (2 rows); 2 removed unit "mm" from rain
    (1 row); 3 converted 2023-07-18 (AD) to BS 2080-04-02 or all to AD — chose one calendar, kept original column;
    4 rows 1 and 2 are duplicates (same date, district, rain) → kept one; 5 rain −99 → blank (error code); 6 final:
    3 rows, 1 missing rain.

## Real-data exercises: notes
* **R1** POWER rain is mm/day; July in Kathmandu ≈ 8–12 mm/day ≈ 250–370 mm/month. Annual (`ANN`) is a daily mean,
  not a total. A common mistake is to sum the monthly mm/day values.
* **R2** The ODN file is in long format with several parameters (pm25, pm10, o3…) and possibly multiple locations in
  rows; units column present; some negative or zero values. Good discussion of "tidy for what purpose".
* **R3** Station/district names differ in romanisation and in old vs new administrative names.
