# Teacher guide — Grade 11, Unit 2: SQL: joins and window functions (lite)

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code: SQL).

| # | Lesson | Time |
|---|---|---|
| 1 | Window functions: RANK | 40–45 min |
| 2 | Shares and running totals | 40–45 min |
| 3 | INNER vs LEFT JOIN | 40–45 min |
| P | Unit project: Top districts per province | 2 periods |

## Before you start
* Materials: Notebook `notebooks/sql_windows.ipynb`. SQLite ≥ 3.25 (included with current Python and in-browser Python).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Do 'rank within belt' with strips of paper grouped by belt.

## Common misconceptions
* GROUP BY and PARTITION BY are the same (GROUP BY collapses rows; windows keep them).
* INNER JOIN silently drops unmatched rows.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Window functions: RANK**
1. GROUP BY vs PARTITION BY?  
   *Answer:* GROUP BY collapses rows; PARTITION BY keeps them.
2. Highest rank in a belt with 16 districts?  
   *Answer:* 16 (ranks run from 1 to 16 if no ties).
3. What does ORDER BY inside OVER do?  
   *Answer:* Sets the order used for ranking/running totals.

**Lesson 2: Shares and running totals**
1. Percent of belt formula?  
   *Answer:* 100 × population ÷ SUM(population) OVER (PARTITION BY belt).
2. Running total needs…  
   *Answer:* An ORDER BY inside OVER.
3. Why useful?  
   *Answer:* Shows concentration, e.g. few districts hold half the people.

**Lesson 3: INNER vs LEFT JOIN**
1. INNER JOIN rows = ?  
   *Answer:* Only matching rows.
2. LEFT JOIN adds…  
   *Answer:* Unmatched left rows with NULL values on the right.
3. Safe habit?  
   *Answer:* Compare row counts before and after joining.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics. Also maps to NEB DBMS/SQL content.
