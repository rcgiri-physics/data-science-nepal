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
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming (⚠️ confirm exact grade and unit in the CDC syllabus PDF); compulsory ICT/Maths data handling.
