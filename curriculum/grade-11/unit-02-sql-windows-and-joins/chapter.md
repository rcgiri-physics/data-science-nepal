# Grade 11 · Unit 2: SQL: window functions and joins

> Track: B (code: SQL) · Tools: SQLite via Python · Lessons: 3
> Datasets: `census-districts`

**Big idea.** Window functions rank, compare and accumulate *within groups* without collapsing rows — a powerful step beyond GROUP BY.

**What you will be able to do**

* I can rank rows within groups with `RANK`, `DENSE_RANK` and `ROW_NUMBER`.
* I can compute group totals, shares and running totals on every row with `SUM(...) OVER`.
* I can use common table expressions (`WITH`) to build queries in steps.
* I can choose between INNER and LEFT JOIN and check row counts.

**Words to know:** window function, partition, frame, rank, running total (cumulative), common table expression (CTE), subquery, inner join, left join, NULL. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/sql_windows.ipynb` (runs offline on the synthetic tables; SQLite 3.25 or newer supports window
functions).

### Before you start
Grade 9 Unit 3: `SELECT … WHERE … GROUP BY … ORDER BY … LIMIT`, `JOIN`. The synthetic tables `districts` (77 rows)
and `schools` (77 rows, key `district_id`) are loaded as before.

---

## Lesson 1: Window functions: RANK

**Hook (5 min).** "Which is the most populous district **in each belt**?" Try it with `GROUP BY`. Why can't
`SELECT ecological_belt, district, MAX(population) … GROUP BY ecological_belt` be trusted to show the right district?

### Explanation
`GROUP BY` **collapses** each group to one row, so the district names are lost. A **window function** computes a value
over a group of rows (a **window**) but **keeps every row**:

```sql
SELECT ecological_belt, district, population,
       RANK() OVER (PARTITION BY ecological_belt ORDER BY population DESC) AS rank_in_belt
FROM districts;
```

Read `OVER (...)` as "looking at":
* `PARTITION BY ecological_belt` — separate windows for Hill, Mountain, Terai (like `GROUP BY`, but without
  collapsing);
* `ORDER BY population DESC` — inside each window, the order used for ranking.

Every one of the 77 rows comes back, with its rank inside its own belt. To keep only the top 3 per belt, filter in an
outer query (window results cannot be used in `WHERE` of the same query, because `WHERE` runs before windows are
computed):

```sql
SELECT *
FROM (
    SELECT ecological_belt, district, population,
           RANK() OVER (PARTITION BY ecological_belt ORDER BY population DESC) AS r
    FROM districts
)
WHERE r <= 3
ORDER BY ecological_belt, r;
```

| ecological_belt | district | population | r |
|---|---|---|---|
| Hill | Hill-38 | 583424 | 1 |
| Hill | Hill-15 | 581215 | 2 |
| Hill | Hill-32 | 544871 | 3 |
| Mountain | Mountain-01 | 107373 | 1 |
| Mountain | Mountain-02 | 107066 | 2 |
| Mountain | Mountain-10 | 97733 | 3 |
| Terai | Terai-09 | 1607726 | 1 |
| Terai | Terai-17 | 1158409 | 2 |
| Terai | Terai-15 | 1116962 | 3 |

**Three ranking functions differ only for ties:**

| Values | `ROW_NUMBER()` | `RANK()` | `DENSE_RANK()` |
|---|---|---|---|
| 90 | 1 | 1 | 1 |
| 85 | 2 | 2 | 2 |
| 85 | 3 | 2 | 2 |
| 80 | 4 | 4 | 3 |

Use `ROW_NUMBER` when you need exactly *n* rows; `RANK` for competition-style ranks; `DENSE_RANK` for no gaps. With
ties, `WHERE r = 1` from `RANK` can return two winners: in province 3, Hill-18 and Hill-28 both have 82.9% literacy.

### Activity (20 min) — PRIMM
1. **Predict** how many rows the first query returns (77), then run it.
2. Run the top-3 query. **Modify:** top 2 by literacy in each province. Which provinces have ties?
3. Compare `RANK`, `DENSE_RANK` and `ROW_NUMBER` on literacy within province 3.
4. **Make:** the least populous district in each province.

### Common mistakes
* Putting the window function in `WHERE` (error) — use an outer query or a CTE.
* Forgetting `DESC` (rank 1 becomes the smallest).
* Assuming exactly one row per rank when ties are possible.

**Check (5 min).**
1. GROUP BY vs PARTITION BY?
2. Highest rank in a belt with 16 districts?
3. What does ORDER BY inside OVER do?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Shares and running totals

**Hook (5 min).** What share of the Terai's population lives in its single biggest district? How many districts hold
half of each belt's people?

### Explanation
Aggregates such as `SUM`, `AVG`, `COUNT` also work as window functions. Without `ORDER BY` inside `OVER`, they give the
**group total on every row**:

```sql
SELECT ecological_belt, district, population,
       SUM(population) OVER (PARTITION BY ecological_belt) AS belt_total,
       ROUND(100.0 * population / SUM(population) OVER (PARTITION BY ecological_belt), 1) AS pct_of_belt
FROM districts
ORDER BY pct_of_belt DESC
LIMIT 3;
```

→ Terai-09 holds 11.2% of the Terai's people; Mountain-01 and Mountain-02 hold 10.1% of the Mountain's each.

Similarly, comparing each district with its group average:

```sql
SELECT district, ecological_belt, literacy_pct,
       ROUND(literacy_pct - AVG(literacy_pct) OVER (PARTITION BY ecological_belt), 1) AS vs_belt_avg
FROM districts
ORDER BY vs_belt_avg DESC
LIMIT 3;
```

→ Mountain-05 and Terai-01 are both 7.9 points above their belt's average.

**Running totals.** With `ORDER BY` inside `OVER`, an aggregate accumulates row by row — a **cumulative** sum. The
**frame** `ROWS UNBOUNDED PRECEDING` says "from the first row of the partition up to this one":

```sql
SELECT ecological_belt, district, population,
       SUM(population) OVER (PARTITION BY ecological_belt ORDER BY population DESC
                             ROWS UNBOUNDED PRECEDING) AS running_total
FROM districts;
```

**Common table expressions (CTEs)** name an intermediate result with `WITH`, so a long query reads as steps:

```sql
WITH ranked AS (
    SELECT ecological_belt, population,
           SUM(population) OVER (PARTITION BY ecological_belt ORDER BY population DESC
                                 ROWS UNBOUNDED PRECEDING) * 1.0
           / SUM(population) OVER (PARTITION BY ecological_belt) AS cum_share
    FROM districts
)
SELECT ecological_belt, COUNT(*) + 1 AS districts_for_half
FROM ranked
WHERE cum_share < 0.5
GROUP BY ecological_belt;
```

→ Half of each belt's people live in its largest 13 Hill districts (of 39), 6 Mountain (of 16) and 7 Terai (of 22). This
kind of **concentration** measure tells planners where most people can be reached.

Other useful window functions: `LAG(x)` / `LEAD(x)` (the previous / next row's value — for changes over time),
`NTILE(4)` (split into quarters), `AVG(x) OVER (ORDER BY date ROWS 6 PRECEDING)` (a 7-row rolling mean, as in Grade 10).

### Activity (20 min) — PRIMM
1. **Predict** the largest `pct_of_belt`; run the shares query.
2. Run the CTE. **Investigate:** why `COUNT(*) + 1`? (Hint: which district crosses 50%?)
3. **Modify:** the same concentration measure for each province.
4. **Make:** use `NTILE(4) OVER (ORDER BY literacy_pct)` to put districts into literacy quartiles; count districts of each
   belt in each quartile.

### Common mistakes
* Forgetting `* 1.0` or `100.0` (integer division).
* Leaving out the frame and getting surprising running totals when there are ties in the ORDER BY column (the default
  frame groups ties together).
* Very long single queries instead of readable CTE steps.

**Check (5 min).**
1. Percent of belt formula?
2. Running total needs…
3. Why useful?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: INNER vs LEFT JOIN

**Hook (5 min).** Imagine three districts have no row in the `schools` table (the report from those districts never
arrived). After `JOIN`, how many districts remain? Will anyone notice they are gone?

### Explanation
* **INNER JOIN** keeps only rows with a match in **both** tables.
* **LEFT JOIN** keeps **every** row of the left table; where the right table has no match, its columns are `NULL`.
* (RIGHT and FULL OUTER JOIN exist too; recent SQLite versions support them. LEFT is by far the most common.)

Simulate missing reports on a copy:

```sql
CREATE TABLE schools_partial AS
SELECT * FROM schools WHERE district_id NOT IN (5, 20, 60);
```

```sql
SELECT COUNT(*) AS inner_rows
FROM districts AS d JOIN schools_partial AS s ON d.district_id = s.district_id;
```

```sql
SELECT COUNT(*) AS left_rows,
       SUM(s.district_id IS NULL) AS districts_without_school_data
FROM districts AS d LEFT JOIN schools_partial AS s ON d.district_id = s.district_id;
```

→ inner 74 rows; left 77 rows, 3 without school data. **The inner join silently dropped three districts** — and any
total you compute (national schools per 100,000) is now wrong without warning.

**Finding the unmatched rows** (an "anti-join"):

```sql
SELECT d.district_id, d.district
FROM districts AS d LEFT JOIN schools_partial AS s ON d.district_id = s.district_id
WHERE s.district_id IS NULL;
```

**NULL is not zero.** `NULL` means unknown. `SUM` and `AVG` skip NULLs; `COUNT(*)` counts rows but `COUNT(column)` counts
non-NULL values; `NULL = NULL` is not true (use `IS NULL`). Replace with a value only when you can justify it:
`COALESCE(s.n_secondary_schools, 0)` claims "zero schools", which is false here.

**One-to-many joins multiply rows.** If a table had one row per *school* (many per district), joining it to districts
repeats each district's population on every school row; summing population afterwards counts districts many times.
Aggregate the many-side first (one row per district), then join.

**The safe habit:** count rows before and after every join, and look at the unmatched rows.

### Activity (20 min) — PRIMM
1. Create `schools_partial`; **predict** the inner and left counts; run both.
2. List the missing districts with the anti-join.
3. Compute national secondary schools per 100,000 people (a) with the inner join, (b) with the left join, (c) with the
   full `schools` table. Which is right? How wrong is (a)?
4. **Make:** write a query that reports, for each province, how many districts have school data and how many don't.

### Common mistakes
* Using INNER JOIN by default without checking what was dropped.
* Treating NULL as 0.
* Summing after a one-to-many join.

**Check (5 min).**
1. INNER JOIN rows = ?
2. LEFT JOIN adds…
3. Safe habit?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Window functions: `func() OVER (PARTITION BY g ORDER BY x)` — compute within groups, keep all rows.
* `ROW_NUMBER`, `RANK`, `DENSE_RANK` differ on ties; filter ranks in an outer query or CTE.
* `SUM(x) OVER (PARTITION BY g)` gives group totals for shares; with `ORDER BY` and a frame, running totals; also `LAG`,
  `LEAD`, `NTILE`, rolling averages.
* `WITH name AS (...)` builds readable step-by-step queries.
* INNER JOIN drops unmatched rows; LEFT JOIN keeps them with NULL. NULL ≠ 0. Count rows before/after joins; aggregate
  before one-to-many joins.

## Practice exercises
Use the synthetic tables.
1. ★ Write a query giving each district's rank by literacy within its province (all 77 rows).
2. ★ What is the difference between `COUNT(*)` and `COUNT(s.n_secondary_schools)` after a LEFT JOIN?
3. ★ Rewrite with a CTE: "districts whose population is above their belt's average".
4. ★★ For each belt, the district with the highest absentee rate per 1,000 (use a window).
5. ★★ Each district's share of its **province's** households, top 5 overall.
6. ★★ Using `LAG`, order districts by population within each belt and compute the gap to the next larger district.
   Which belt has the biggest gap between its first and second district?
7. ★★ Put districts into literacy quartiles with `NTILE(4)`. How many Mountain districts are in the bottom quartile?
8. ★★★ Explain why `SELECT ecological_belt, district, MAX(population) FROM districts GROUP BY ecological_belt` might
   seem to work in SQLite but is not reliable SQL. Write the correct window version.
9. ★★★ A `teachers` table has one row per teacher with `district_id`. Write a query for teachers per secondary school
   in each district that avoids the one-to-many trap.
10. ★★★ Write a query that lists districts with literacy at least 4 points below their province average and also more
    than 90 absentees per 1,000 people.

## Exercises with real data
**R1. Real census rankings (RD-11 / RD-13).** Load real district populations (2021, and 2011 if you collected them in
Grade 9). Rank districts within each province by population and by growth rate. Which district is first in its
province on both? Compute the share of each province's population in its largest district.
*Offline fallback:* the synthetic tables.

**R2. Earthquake sequence (RD-05).** Load the 2015 USGS file into SQLite. Use `LAG(time)` ordered by time to compute the
time between consecutive earthquakes, and `ROW_NUMBER() OVER (PARTITION BY substr(time,1,10) ORDER BY mag DESC)` to find
the largest quake each day.

**R3. Joining two real sources (RD-01 + RD-11).** Join a table of district names from the census with a list of
districts from another source (e.g. rainfall stations' districts, Grade 9 Unit 2 lookup table). Use a LEFT JOIN and an
anti-join to list names that fail to match, then fix them with a lookup table.

## Unit project: Top districts per province
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Produce a short SQL report: top 3 districts per
province on two indicators (one count, one rate), each district's share of its province, a concentration measure, and
a join-quality check (row counts and unmatched rows). Write findings with limits. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* SQLite window functions documentation (<https://sqlite.org/windowfunctions.html>).
* "Mode SQL Tutorial" (free online) — advanced section on window functions.
