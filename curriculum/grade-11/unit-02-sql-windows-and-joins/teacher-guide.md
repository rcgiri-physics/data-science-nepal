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

## Answers: practice exercises
1. `SELECT district, province, literacy_pct, RANK() OVER (PARTITION BY province ORDER BY literacy_pct DESC) AS r FROM districts;`
2. After a LEFT JOIN, `COUNT(*)` counts all left rows (77); `COUNT(s.n_secondary_schools)` counts only rows with school
   data.
3. `WITH b AS (SELECT district, population, AVG(population) OVER (PARTITION BY ecological_belt) AS belt_avg FROM districts) SELECT * FROM b WHERE population > belt_avg;` → 37 districts.
4. Rank by `1.0 * absentee_population / population DESC` within belt, keep rank 1: Hill-10 (121.4 per 1,000),
   Mountain-11 (81.2), Terai-10 (109.5).
5. `100.0 * households / SUM(households) OVER (PARTITION BY province)`: Terai-04 43.6% (province 2), Terai-07 41.5%
   (province 2), Hill-38 29.8% (4), Hill-02 25.7% (6), Terai-15 25.3% (3).
6. `LAG(population) OVER (PARTITION BY ecological_belt ORDER BY population DESC) - population`: Terai has the biggest
   first-to-second gap (Terai-09 vs Terai-17: 449,317).
7. Bottom quartile (NTILE 1 by literacy ascending): Mountain 14, Terai 4, Hill 2 — 14 of the 16 Mountain districts.
8. SQLite allows "bare columns" with MAX and happens to take the district from the max row, but standard SQL rejects it
   and other databases (or other aggregates like AVG) give arbitrary names. Use RANK/ROW_NUMBER as in Lesson 1.
9. Aggregate first: `WITH t AS (SELECT district_id, COUNT(*) AS n_teachers FROM teachers GROUP BY district_id) SELECT d.district, 1.0 * t.n_teachers / s.n_secondary_schools FROM districts d JOIN schools s USING (district_id) LEFT JOIN t USING (district_id);`
10. With thresholds 4 points and 90 per 1,000: Terai-14 (68.3 vs province avg 72.7; 96.5 per 1,000) and Terai-20
    (72.4 vs 76.4; 107.9).

Lesson 3 (district_id 5, 20, 60 removed = Mountain-02, Mountain-05, Hill-29): schools per 100,000 — inner join 75.26,
left join 74.38 (missing schools counted as nothing but their people kept), full table 75.50. Neither partial answer is
"right": report the missing districts. Lesson 3 Make: provinces 1, 4 and 5 each have one district without data.

## Real-data exercises: notes
* **R1** Kathmandu is first in Bagmati on population; growth leaders are often other valley or Terai districts — let the
  data decide.
* **R2** On 25 April 2015 aftershocks came minutes apart; gaps grow over the following weeks (Omori's law, a nice
  extension for curious students).
* **R3** Expect mismatches like Kavre/Kavrepalanchok, Nawalparasi East/West, Rukum East/West after 2015.
