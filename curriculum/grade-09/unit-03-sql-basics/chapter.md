# Grade 9 · Unit 3: SQL basics on district data

> Track: B (code: SQL/SQLite) · Tools: SQLite via Python (JupyterLite, Jupyter or Colab) · Lessons: 5 · Version: 0.1 draft (English)
> Datasets: `census-districts`

**Big idea.** SQL asks questions of tables in nearly plain English: choose columns, keep rows, order them, group them and join tables.

**What you will be able to do**

* I can write SELECT … FROM … WHERE … ORDER BY … LIMIT queries.
* I can summarise groups with COUNT, SUM, AVG and GROUP BY.
* I can join two tables and compute a rate.

**Words to know:** query, SELECT, WHERE, ORDER BY, GROUP BY, JOIN, key (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/census_sql.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: SELECT and WHERE

**Hook (5 min).** 'List the Terai districts with literacy above 70%.' How would you say that to a database?

**Concept (≤ 5 min).** A query has parts: SELECT (columns) FROM (table) WHERE (row condition). Text values use single quotes; keywords are not case-sensitive.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Predict then run: SELECT * FROM districts; SELECT district, literacy_pct …; add WHERE ecological_belt = 'Terai' AND literacy_pct > 70.

**Check (5 min).**
1. Which clause chooses columns?
2. Which keeps only some rows?
3. Write the condition for Hill districts.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: ORDER BY and LIMIT

**Hook (5 min).** Which five districts are the most populous?

**Concept (≤ 5 min).** ORDER BY sorts (ASC small→large, DESC large→small); LIMIT keeps the first n rows. Together: top-n queries.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Write top-5 and bottom-5 queries for population and literacy; swap to check each other's results.

**Check (5 min).**
1. Write 'the 3 smallest districts by area'.
2. What does DESC mean?
3. What does LIMIT 10 do?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: GROUP BY and aggregates

**Hook (5 min).** What is the total population of each belt? How many districts are in each?

**Concept (≤ 5 min).** Aggregates (COUNT, SUM, AVG, MIN, MAX) turn many rows into one number per group. GROUP BY says which groups. Every non-aggregate column in SELECT must be in GROUP BY.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Group by belt: count districts, sum population, average literacy. Predict the number of result rows (3).

**Check (5 min).**
1. GROUP BY ecological_belt returns how many rows if there are 3 belts?
2. What does AVG(literacy_pct) compute?
3. Which aggregate counts rows?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: JOIN: combining tables

**Hook (5 min).** Population is in one table, school counts in another. How do you put them side by side?

**Concept (≤ 5 min).** A JOIN matches rows from two tables using a shared key (district_id). Joining on names is fragile (spelling!) — keys are safer.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Join districts and schools; compute people per school; list the five districts with the most people per school.

**Check (5 min).**
1. What is the key in our JOIN?
2. Why not join on district names?
3. How many rows does a one-to-one JOIN of 77 + 77 give?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 5: A short SQL report

**Hook (5 min).** Your headteacher asks: 'What should we know about districts and schools?' Give three facts.

**Concept (≤ 5 min).** A report is queries + a sentence for each result + one limit. Write queries first, then plain-language findings.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Write three queries on one theme (e.g. schools per 100,000 people), run them, and write one finding and one limit for each.

**Check (5 min).**
1. What three things belong in each finding?
2. Why mention that the table is synthetic?
3. How can you make queries reusable?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Which districts are changing?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
