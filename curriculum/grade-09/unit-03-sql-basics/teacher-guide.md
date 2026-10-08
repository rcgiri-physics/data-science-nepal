# Teacher guide — Grade 9, Unit 3: SQL basics on district data

**Time:** 5 lessons + project (about 7 periods). **Track:** B (code: SQL/SQLite).

| # | Lesson | Time |
|---|---|---|
| 1 | SELECT and WHERE | 40–45 min |
| 2 | ORDER BY and LIMIT | 40–45 min |
| 3 | GROUP BY and aggregates | 40–45 min |
| 4 | JOIN: combining tables | 40–45 min |
| 5 | A short SQL report | 40–45 min |
| P | Unit project: Which districts are changing? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/census_sql.ipynb`; unplugged extract printed.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
No computers? Do the unplugged version: print the 10-row extract of the table and carry out each SQL idea by hand (cross out rows for WHERE, sort strips for ORDER BY, make piles for GROUP BY, match ID cards for JOIN). Track B coding cannot be replaced fully; plan it for a lab day.

## Common misconceptions
* WHERE filters rows before grouping; it can't use aggregates (use HAVING).
* A JOIN needs a shared key; matching names is fragile.
* Quotes: text values use single quotes ('Terai').

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: SELECT and WHERE**
1. Which clause chooses columns?  
   *Answer:* SELECT.
2. Which keeps only some rows?  
   *Answer:* WHERE.
3. Write the condition for Hill districts.  
   *Answer:* WHERE ecological_belt = 'Hill'

**Lesson 2: ORDER BY and LIMIT**
1. Write 'the 3 smallest districts by area'.  
   *Answer:* SELECT district, area_km2 FROM districts ORDER BY area_km2 ASC LIMIT 3
2. What does DESC mean?  
   *Answer:* Descending: largest first.
3. What does LIMIT 10 do?  
   *Answer:* Returns at most 10 rows.

**Lesson 3: GROUP BY and aggregates**
1. GROUP BY ecological_belt returns how many rows if there are 3 belts?  
   *Answer:* 3.
2. What does AVG(literacy_pct) compute?  
   *Answer:* The mean literacy within each group.
3. Which aggregate counts rows?  
   *Answer:* COUNT(*).

**Lesson 4: JOIN: combining tables**
1. What is the key in our JOIN?  
   *Answer:* district_id.
2. Why not join on district names?  
   *Answer:* Spelling differences would break the match.
3. How many rows does a one-to-one JOIN of 77 + 77 give?  
   *Answer:* 77.

**Lesson 5: A short SQL report**
1. What three things belong in each finding?  
   *Answer:* The number, what it means in plain words, and a limit.
2. Why mention that the table is synthetic?  
   *Answer:* So no one mistakes invented numbers for real facts.
3. How can you make queries reusable?  
   *Answer:* Save them in a notebook with comments.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming (⚠️ confirm exact grade and unit in the CDC syllabus PDF); compulsory ICT/Maths data handling.
