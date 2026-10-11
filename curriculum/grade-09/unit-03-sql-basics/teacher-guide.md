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
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
All results are for the synthetic tables. Every query in the chapter itself is run in CI by `tools/check_chapter_code.py`.
1. `SELECT district, province FROM districts WHERE province = 2;` → 3 rows.
2. `SELECT COUNT(*) FROM districts WHERE literacy_pct < 65;` → 9.
3. `… ORDER BY households DESC LIMIT 5` → Terai-09 (355,881), Terai-15, Terai-17, Terai-13, Terai-05.
4. `SELECT province, COUNT(*) AS n, SUM(population) AS pop FROM districts GROUP BY province ORDER BY pop DESC;` →
   7 (16, 7,500,730), 1 (16, 5,774,060), 3, 5, 6, 4, 2.
5. `SELECT district, ROUND(100.0 * absentee_population / population, 1) AS rate FROM districts WHERE ecological_belt = 'Hill' ORDER BY rate DESC LIMIT 3;`
   → Hill-10, Hill-36, Hill-39 (12.1 each; ties — discuss).
6. `SELECT ecological_belt, ROUND(1.0 * SUM(population) / SUM(households), 2) FROM districts GROUP BY ecological_belt;`
   → Hill 4.53, Mountain 4.59, Terai 4.63: Terai largest.
7. `SELECT COUNT(*) FROM schools WHERE enrolment_girls > enrolment_boys;` → 44 districts.
8. `SELECT province, AVG(literacy_pct) FROM districts GROUP BY province HAVING AVG(literacy_pct) > 72;` → provinces
   1 (72.7), 3 (76.4), 5 (78.0).
9. Hill 0.5422 vs 0.5423; Mountain 0.5322 vs 0.5321; Terai 0.5072 vs 0.5075. Very close here because female share
   varies little between districts, but in general they differ: the weighted one gives big districts more weight.
   The weighted one is the true share of all people.
10. "Which province has the highest girls' share of secondary enrolment?" → province 7, 51.3%.

Lesson activities: densest districts Terai-15 (954.2/km²), Terai-09, Terai-03; densest Hill: Hill-15, Hill-16,
Hill-05. Province with most people: 7. Highest average literacy: 5 (78.0). Min/max literacy by belt: Hill 64.6–83.6,
Mountain 62.6–73.7, Terai 61.3–78.1 (so `HAVING MIN(literacy_pct) < 63` returns Mountain and Terai).

## Real-data exercises: notes
* **R1** Real preliminary census: Kathmandu is the most populous district (≈ 2.0 million), followed by Morang,
  Rupandehi, Jhapa; Madhesh districts have larger households. Column names in the real file differ (often with
  spaces or Nepali): rename them first, e.g. `df.columns = [...]`.
* **R2** (a) 7.8 (25 Apr), 7.3 (12 May), 6.7, 6.6, 6.3, 6.1 … (b) 82 events on 25 April, 26 on 26 April, 12 on 27 April, then a few a day — the
  aftershock decay; (c) 253 of 304 depths are exactly 10 km (a default value for poorly constrained shallow quakes — a good
  data-quality discussion).
* **R3** Watch for aggregates in World Bank files (e.g. "South Asia") that are not countries; filter by country code.
