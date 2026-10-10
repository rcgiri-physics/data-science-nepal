# Grade 9 · Unit 3: SQL basics on district data

> Track: B (code: SQL/SQLite) · Tools: SQLite via Python (JupyterLite, Jupyter or Colab) · Lessons: 5
> Datasets: `census-districts`

**Big idea.** SQL asks questions of tables in nearly plain English: choose columns, keep rows, order them, group them and join tables.

**What you will be able to do**

* I can write SELECT … FROM … WHERE … ORDER BY … LIMIT queries.
* I can summarise groups with COUNT, SUM, AVG and GROUP BY.
* I can join two tables and compute a rate.

**Words to know:** database (डाटाबेस), query (क्वेरी), SELECT, WHERE, ORDER BY, GROUP BY, JOIN, key (कुञ्जी), aggregate. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/census_sql.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
From Unit 1: sorting, filtering and pivot tables in a spreadsheet. **Everything in this unit is something you already
did with a pivot table — now you will say it in words a database understands.** From Unit 2: why keys are better
than names.

---

## Lesson 1: SELECT and WHERE

**Hook (5 min).** "List the Terai districts with literacy above 70%." How would you say that to a database? Write
your guess in plain English, as precisely as you can.

### Explanation
A **database** stores tables. **SQL** (Structured Query Language, said "S-Q-L" or "sequel") is the language almost
every database understands: banks, hospitals, the Election Commission's voter list, mobile apps. We use **SQLite**, a
small free database that runs inside Python, even in the browser with no installation.

In the notebook, the first cell loads two **synthetic** tables:
* `districts` — 77 rows: `district_id, district, ecological_belt, province, population, households, area_km2, male,
  female, literacy_pct, absentee_population`
* `schools` — 77 rows: `district_id, n_secondary_schools, enrolment_girls, enrolment_boys`

and defines a helper `q("…")` that runs a query and shows the result as a table.

A **query** is a question. The simplest has two parts:

```sql
SELECT district, population
FROM districts;
```

* `SELECT` lists the **columns** you want (`*` means all columns);
* `FROM` names the **table**.

To keep only some **rows**, add `WHERE` with a condition:

```sql
SELECT district, literacy_pct
FROM districts
WHERE ecological_belt = 'Terai' AND literacy_pct > 70;
```

This returns 12 Terai districts (Terai-01 with 78.1% down to Terai-15 with 70.3%).

**Rules of the language**
* Text values go in **single quotes**: `'Terai'`. Numbers do not: `70`.
* Comparison operators: `=`, `<>` (not equal), `<`, `>`, `<=`, `>=`.
* Combine conditions with `AND` (both true), `OR` (either true), `NOT`. Use brackets when mixing:
  `WHERE (ecological_belt = 'Hill' OR ecological_belt = 'Mountain') AND province = 3`.
* `IN` is shorter for several values: `WHERE province IN (1, 3, 7)`.
* `BETWEEN 60 AND 70` includes both ends.
* Keywords (`SELECT`, `select`) are not case-sensitive, but writing them in capitals makes queries easier to read.
  The **values** are case-sensitive: `'terai'` will not match `'Terai'`.
* The `;` ends a query; the notebook helper does not need it.

**Read a query in the order the database runs it:** first `FROM` (which table), then `WHERE` (which rows), then
`SELECT` (which columns).

### Activity (20 min) — PRIMM
**P**redict → **R**un → **I**nvestigate → **M**odify → **M**ake.
1. **Predict** how many rows `SELECT * FROM districts` returns, then **run** it.
2. Run `SELECT district, literacy_pct FROM districts`. How is it different?
3. **Investigate:** add `WHERE ecological_belt = 'Terai'`. How many rows now? Then add `AND literacy_pct > 70`.
4. **Modify:** change to Hill districts in province 3; then districts with literacy between 60 and 65.
5. **Make:** write a query for "Mountain districts with more than 100,000 people".

*No computer? "Unplugged SQL":* your teacher prints 12 district rows on cards. One student is the "database";
others call out queries ("SELECT district WHERE belt = Terai"); the database holds up matching cards.

### Common mistakes
* Double quotes or no quotes around text: `WHERE ecological_belt = Terai` fails (the database looks for a column
  called Terai).
* `=` vs `==`: SQL uses a single `=` for comparison.
* Forgetting brackets when mixing `AND` and `OR`.

**Check (5 min).**
1. Which clause chooses columns?
2. Which keeps only some rows?
3. Write the condition for Hill districts.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: ORDER BY and LIMIT

**Hook (5 min).** Which five districts are the most populous? Which three are the smallest by area? How did you do
this in a spreadsheet?

### Explanation
`ORDER BY` sorts the result; `LIMIT n` keeps the first *n* rows. Together they answer "top *n*" questions.

```sql
SELECT district, population
FROM districts
ORDER BY population DESC
LIMIT 5;
```

| district | population |
|---|---|
| Terai-09 | 1607726 |
| Terai-17 | 1158409 |
| Terai-15 | 1116962 |
| Terai-13 | 901249 |
| Terai-03 | 878299 |

* `ASC` (ascending, small → large, A → Z) is the default; `DESC` is descending.
* Sort by several columns: `ORDER BY ecological_belt, literacy_pct DESC` sorts by belt, and within each belt by
  literacy from high to low.
* You can sort by a **calculated column** and give it a name with `AS`:

```sql
SELECT district,
       population,
       area_km2,
       ROUND(population / area_km2, 1) AS density
FROM districts
ORDER BY density DESC
LIMIT 3;
```

`ROUND(x, 1)` keeps one decimal place. `AS density` names the new column (an **alias**).

**Clause order is fixed:** `SELECT … FROM … WHERE … ORDER BY … LIMIT …`. Writing them in another order is an error.

### Activity (20 min) — PRIMM
1. **Predict** then run the top-5 population query.
2. Write the bottom 5 by population (change one word).
3. Top 5 and bottom 5 by literacy. Swap queries with a partner and check each other's results.
4. **Make:** the three most crowded districts (density). Then the three most crowded **Hill** districts (add WHERE —
   where does it go?).

### Common mistakes
* Putting `WHERE` after `ORDER BY`.
* Expecting `LIMIT` to choose the "best" rows without `ORDER BY` (without sorting, you get whichever rows come first).
* Integer division: in SQLite `7 / 2` is `3`. Multiply by `1.0` first (`1.0 * 7 / 2` = 3.5) when both numbers are
  whole. (`population / area_km2` is fine because area has decimals.)

**Check (5 min).**
1. Write 'the 3 smallest districts by area'.
2. What does DESC mean?
3. What does LIMIT 10 do?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: GROUP BY and aggregates

**Hook (5 min).** What is the total population of each ecological belt? How many districts does each have? (Answer
this in one query — your pivot table from Unit 1 did it in one step.)

### Explanation
**Aggregate functions** turn many rows into one value: `COUNT(*)` (number of rows), `SUM(x)`, `AVG(x)` (mean),
`MIN(x)`, `MAX(x)`.

Without `GROUP BY`, they summarise the whole table:

```sql
SELECT COUNT(*) AS n_districts, SUM(population) AS total_population
FROM districts;
```

→ 77 districts, 27,333,379 people.

With `GROUP BY`, they summarise **each group** separately — exactly a pivot table:

```sql
SELECT ecological_belt,
       COUNT(*) AS n_districts,
       SUM(population) AS total_population,
       ROUND(AVG(literacy_pct), 1) AS avg_literacy
FROM districts
GROUP BY ecological_belt
ORDER BY total_population DESC;
```

| ecological_belt | n_districts | total_population | avg_literacy |
|---|---|---|---|
| Terai | 22 | 14366042 | 70.2 |
| Hill | 39 | 11907289 | 77.1 |
| Mountain | 16 | 1060048 | 65.8 |

**The GROUP BY rule:** every column in `SELECT` must either be in `GROUP BY` or be inside an aggregate. Asking for
`district` here makes no sense: which of the 39 Hill districts' names should appear in the one Hill row?

**Filtering groups with HAVING.** `WHERE` filters rows **before** grouping; `HAVING` filters groups **after**:

```sql
SELECT province, COUNT(*) AS n_districts, SUM(population) AS total_population
FROM districts
GROUP BY province
HAVING COUNT(*) >= 12
ORDER BY total_population DESC;
```

→ provinces 7, 1, 3 and 5 (16, 16, 12 and 12 districts).

### Activity (20 min) — PRIMM
1. **Predict** how many rows the belt query returns, then run it.
2. **Modify:** group by `province` instead. Which province has the most people? The highest average literacy?
3. Add `SUM(absentee_population)` to the belt query.
4. **Make:** for each belt, the minimum and maximum literacy. Then only the belts where the minimum is below 63
   (`HAVING`).

### Common mistakes
* Selecting a non-grouped column (SQLite may give a random value instead of an error, which is worse).
* Using `WHERE AVG(…) > 70` — aggregates belong in `HAVING`.
* Forgetting `AS`, which leaves ugly column names like `ROUND(AVG(literacy_pct), 1)`.

**Check (5 min).**
1. GROUP BY ecological_belt returns how many rows if there are 3 belts?
2. What does AVG(literacy_pct) compute?
3. Which aggregate counts rows?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: JOIN: combining tables

**Hook (5 min).** Population is in the `districts` table; school counts are in the `schools` table. How do you put
them side by side to compute "people per school"?

### Explanation
Real databases keep different topics in different tables (people, schools, health posts), linked by a **key**: a
column that identifies each row and appears in both tables. Our key is `district_id`.

A `JOIN` matches rows that share the key value:

```sql
SELECT d.district, d.population, s.n_secondary_schools,
       ROUND(1.0 * d.population / s.n_secondary_schools) AS people_per_school
FROM districts AS d
JOIN schools AS s ON d.district_id = s.district_id
ORDER BY people_per_school DESC
LIMIT 5;
```

* `d` and `s` are short **table aliases**; `d.population` means "population from the districts table".
* `ON d.district_id = s.district_id` is the **join condition**.
* `1.0 *` avoids whole-number division.

The top rows are Terai-15 and Terai-18 (about 1,698 people per secondary school each), then Terai-13, Terai-16 and
Hill-24.

**Why keys, not names?** If one table says `Kavre` and the other `Kavrepalanchok`, a join on names silently drops that
district. Keys don't have spelling. (Unit 2's lookup table is how you create keys when a source has only names.)

**Kinds of join**
* `JOIN` (inner join) keeps only rows whose key appears in **both** tables.
* `LEFT JOIN` keeps **all** rows of the first table, filling the other table's columns with `NULL` when there is no
  match — useful to discover which districts are missing from the second table.

Both our tables have the same 77 keys, so here every kind of join gives 77 rows. With real data, check row counts
before and after every join.

**A rate from two tables.** Girls' share of secondary enrolment by belt:

```sql
SELECT d.ecological_belt,
       ROUND(100.0 * SUM(s.enrolment_girls) / SUM(s.enrolment_girls + s.enrolment_boys), 1) AS girls_pct
FROM districts AS d
JOIN schools AS s ON d.district_id = s.district_id
GROUP BY d.ecological_belt
ORDER BY girls_pct;
```

Notice it computes `SUM(girls) / SUM(all)` per belt, the **true** share for all students in the belt, not the
average of 77 district percentages (Unit 1's warning).

### Activity (20 min) — PRIMM
1. **Predict** how many rows the join returns without `LIMIT`. Run it and check.
2. Run the people-per-school query. Change it to show the five districts with the **fewest** people per school.
3. Run the girls' share query.
4. **Make:** secondary schools per 100,000 people for each belt
   (`100000.0 * SUM(n_secondary_schools) / SUM(population)`). Which belt has the most schools for its population?

### Common mistakes
* Forgetting the `ON` condition: every row of one table is paired with every row of the other (77 × 77 = 5,929
  rows).
* Ambiguous column names: `district_id` exists in both tables, so write `d.district_id`.
* Not checking row counts after joining real data.

**Check (5 min).**
1. What is the key in our JOIN?
2. Why not join on district names?
3. How many rows does a one-to-one JOIN of 77 + 77 give?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 5: A short SQL report

**Hook (5 min).** Your head teacher asks: "What should we know about districts and schools?" You have 20 minutes and
a database. What three facts would you bring?

### Explanation
A query result is not yet an answer. A short **SQL report** turns queries into findings someone can use. For each
finding write:

1. **The question** in plain words.
2. **The query** (saved in the notebook, with a comment saying what it does).
3. **The number(s)** with units.
4. **What it means**, in one sentence a non-expert understands.
5. **One limit.**

Example:

> **Question:** Which belt has the most secondary schools for its population?
> **Query:** schools per 100,000 people by belt (notebook cell 7).
> **Result:** Hill 78.1, Mountain 76.2, Terai 73.3 schools per 100,000 people.
> **Meaning:** The three belts have a similar number of schools for their population; the Terai has slightly fewer.
> **Limit:** The table is **synthetic**; and school counts say nothing about school size, distance or quality — a
> Mountain school may serve a huge area.

**Comments make queries reusable.** In SQL, a line starting with `--` is a comment:

```sql
-- Secondary schools per 100,000 people, by ecological belt
SELECT d.ecological_belt,
       ROUND(100000.0 * SUM(s.n_secondary_schools) / SUM(d.population), 1) AS schools_per_100k
FROM districts AS d
JOIN schools AS s ON d.district_id = s.district_id
GROUP BY d.ecological_belt
ORDER BY schools_per_100k DESC;
```

### Activity (20 min) — PRIMM
1. Choose a theme: *schools*, *people abroad*, or *literacy*.
2. Write three queries on that theme (at least one `GROUP BY` and one `JOIN`).
3. For each, write the five-part finding.
4. Read one finding aloud to the class without showing the query: can classmates understand it?

### Common mistakes
* Reporting raw query output without explanation.
* Forgetting to say the table is synthetic.
* Findings without units ("Hill is 78.1").

**Check (5 min).**
1. What three things belong in each finding?
2. Why mention that the table is synthetic?
3. How can you make queries reusable?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* `SELECT columns FROM table WHERE row-condition ORDER BY column DESC LIMIT n` — always in this order.
* Text in single quotes; `AND`/`OR`/`NOT`, `IN`, `BETWEEN`; brackets when mixing.
* Aggregates `COUNT(*)`, `SUM`, `AVG`, `MIN`, `MAX`; `GROUP BY` = pivot table; `HAVING` filters groups.
* `JOIN … ON a.key = b.key` combines tables; keys beat names; check row counts.
* Compute group rates as `SUM(part) / SUM(whole)`, and use `1.0 *` to avoid whole-number division.
* A finding = question, query, number with units, meaning, limit.

## Practice exercises
Run these against the synthetic tables in the notebook. (Answers in the teacher guide.)
1. ★ List the district and province of every district in province 2.
2. ★ How many districts have literacy below 65%?
3. ★ The 5 districts with the most households.
4. ★★ For each province: number of districts and total population, largest population first.
5. ★★ The 3 Hill districts with the largest absentee population **rate** (per 100 people).
6. ★★ Average household size (`population / households`) for each belt. Which belt has the largest households?
7. ★★ Which districts have more girls than boys enrolled in secondary school? How many are there?
8. ★★★ Find the provinces whose average district literacy is above 72%, using `HAVING`.
9. ★★★ For each belt, compute the **people-weighted** female share `SUM(female) / SUM(population)` and the
   **average** of district female shares `AVG(1.0 * female / population)`. Are they the same? Why or why not?
10. ★★★ Explain in words what this query answers, then predict its first row:

```sql
SELECT d.province, ROUND(100.0 * SUM(s.enrolment_girls) / SUM(s.enrolment_girls + s.enrolment_boys), 1) AS girls_pct
FROM districts AS d JOIN schools AS s ON d.district_id = s.district_id
GROUP BY d.province
ORDER BY girls_pct DESC
LIMIT 1;
```

## Exercises with real data
**R1. Query the real census (RD-11).** Download the Census 2021 preliminary table from Open Data Nepal, load it into
the notebook (replace the synthetic file name with yours; see the dataset card), and repeat Lessons 1–3: top 5
districts by population, population by province, average household size by province. Compare with the synthetic
results: which patterns are similar, which differ?
*Offline fallback:* the synthetic tables (the notebook works as shipped).

**R2. Earthquakes in SQL (RD-05).** Load the USGS 2015 Nepal earthquake CSV into SQLite (in the notebook:
`pd.read_csv("query.csv").to_sql("quakes", con, index=False)`). Write queries: (a) the 10 strongest earthquakes;
(b) number of earthquakes per day in the first week after 25 April 2015 (hint: `substr(time, 1, 10)` gives the date
part); (c) average depth by magnitude class (`CAST(mag AS INTEGER)`).

**R3. Two real tables, one key (RD-01).** From the World Bank, download two indicators for South Asian countries
(e.g. population and internet users %). Load both as tables and `JOIN` on the country code (`countryiso3code`).
Compute the number of internet users (population × % ÷ 100) per country.

## Unit project: Which districts are changing?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Write a short SQL report with at least three
findings (five parts each) about districts and schools, using `WHERE`, `GROUP BY` and `JOIN`, and include the saved
queries. This is the start of the Grade 9 flagship project (Unit 8). Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* SQLBolt (<https://sqlbolt.com>): free interactive SQL lessons in the browser.
* Kaggle Learn "Intro to SQL" (free; uses a different database, the same ideas).
* SQLite's own documentation (<https://sqlite.org/lang.html>) when you want the exact rules.
