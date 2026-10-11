# Grade 11 · Unit 1: Bigger data and performance

> Track: B (code) · Tools: Python, pandas, SQLite · Lessons: 3
> Datasets: none

**Big idea.** When tables reach hundreds of thousands of rows, how we store and ask matters: types, memory, indexes and vectorised operations.

**What you will be able to do**

* I can measure the time and memory a step uses, and find the real bottleneck.
* I can choose smaller data types and replace Python loops with vectorised operations.
* I can create a database index and show, with measurements, when it helps.

**Words to know:** performance, bottleneck, benchmark, memory, byte, data type (dtype), downcasting, category, vectorised, index (database), query plan. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/bigger_data.ipynb` (generates its own synthetic data; runs offline).

### Before you start
Grades 9–10: pandas, `groupby`, SQL. School computers in Nepal are often old and low on memory, so writing efficient code
is not a luxury: it decides whether an analysis runs at all. This unit generates a **synthetic** table of 500,000
hourly air readings so that everyone has the same "big" data:

```python
import time
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)          # a seeded random generator: same numbers every run
n = 500_000
readings = pd.DataFrame({
    "station": rng.integers(1, 51, n),                       # 50 stations
    "hour": rng.integers(0, 24, n),                          # hour of day 0–23
    "pm25": rng.gamma(2.0, 25.0, n).round(1),                # right-skewed PM2.5 values
    "belt": rng.choice(["Mountain", "Hill", "Terai"], n),
})
print(readings.shape)                                         # (500000, 4)
```

`500_000` is just 500000 written with underscores for readability. A **seed** (`2026`) makes the "random" numbers
repeatable, so your results match the book.

---

## Lesson 1: Measuring: time and memory

**Hook (5 min).** Your notebook freezes on a big file and the fan starts roaring. Which step is slow? Guessing is
usually wrong. How could you find out for sure?

### Explanation
**Measure before you optimise.** Programmers say most of a program's time is spent in a small part of the code (the
**bottleneck**). Speeding up anything else is wasted effort. Measure, change one thing, measure again.

**Time.** `time.perf_counter()` reads a precise clock; subtract two readings:

```python
start = time.perf_counter()
means = readings.groupby("station")["pm25"].mean()
elapsed = time.perf_counter() - start
print(f"groupby took {elapsed * 1000:.1f} ms")
```

Timings vary from run to run (other programs, caching), so repeat a few times and report the typical (median) value.
In Jupyter, `%timeit expression` does the repeating for you.

**Memory.** Each value occupies bytes: an `int64` or `float64` uses 8 bytes; text uses much more, because each string is
a separate Python object.

```python
mem = readings.memory_usage(deep=True)
print((mem / 1e6).round(1))                       # MB per column
print(round(mem.sum() / 1e6, 1), "MB total")     # about 39 MB
```

`deep=True` counts the real size of text. On our table: `station`, `hour` and `pm25` take 4 MB each (500,000 × 8
bytes), while `belt` (text) takes about 27 MB — **two-thirds of the table for a column with only three different
values**.

**Rule of thumb:** pandas needs roughly 5–10 times the file size in RAM to work comfortably. A 1 GB CSV on a laptop with
4 GB of RAM will struggle. Options: load only the columns you need (`usecols=`), use smaller types (Lesson 2), read in
pieces (`chunksize=`), or let a database do the work (Lesson 3).

### Activity (20 min) — PRIMM
1. **Predict** which column uses the most memory; run the memory cell.
2. Time three steps: `groupby("station").mean()`, `sort_values("pm25")`, and `readings[readings["pm25"] > 100]`.
   Repeat each 3 times and record the median.
3. **Investigate:** time `pd.read_csv` on a saved copy (`readings.to_csv("big.csv", index=False)`), with and without
   `usecols=["station", "pm25"]`.

### Common mistakes
* Optimising before measuring.
* Trusting a single timing.
* Forgetting `deep=True` (text columns look tiny without it).

**Check (5 min).**
1. Why measure first?
2. Name two things you can measure.
3. Why repeat timings?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Types and vectorising

**Hook (5 min).** Hour of day is a number from 0 to 23. Why store it in 64 bits (able to hold numbers up to about 9
quintillion)? And why does a `for` loop over 500,000 values feel slow when `.sum()` is instant?

### Explanation
**Choose the smallest safe type.**

| dtype | Bytes | Range / precision | Good for |
|---|---|---|---|
| `int8` | 1 | −128 to 127 | hour (0–23), month, station number < 128 |
| `int16` | 2 | −32,768 to 32,767 | ward numbers, years |
| `int32` | 4 | about ±2.1 billion | populations |
| `int64` | 8 | about ±9.2 × 10¹⁸ | the default |
| `float32` | 4 | about 6–7 significant digits | measurements like 52.8 |
| `float64` | 8 | about 15–16 significant digits | the default; precise calculations |
| `category` | 1–2 per value + one copy of each label | few distinct values | belt, province, travel mode |

```python
small = readings.astype({"station": "int8", "hour": "int8", "pm25": "float32", "belt": "category"})
print(round(small.memory_usage(deep=True).sum() / 1e6, 1), "MB")    # about 3.5 MB, ~11 times smaller
```

A **category** stores each distinct label once and keeps a small integer code per row: `belt` falls from 27 MB to
0.5 MB. Groupby on categories is also faster.

**Risks of too-small types.** An `int8` cannot hold 200: values **overflow** (wrap around to negative numbers) or
raise an error. `float32` keeps only about 7 significant digits, fine for PM2.5 but not for money in paisa over a
national budget. Check `min()` and `max()` before downcasting.

**Vectorise: let pandas loop for you.** A Python `for` loop handles one value at a time, with Python checking types at
every step. pandas and NumPy column operations run a loop written in compiled C code over the whole array at once.

```python
start = time.perf_counter()
total = 0.0
for value in readings["pm25"]:          # Python loop: one value at a time
    total += value
loop_time = time.perf_counter() - start

start = time.perf_counter()
total_vec = readings["pm25"].sum()     # vectorised
vec_time = time.perf_counter() - start
print(f"loop {loop_time:.3f} s, vectorised {vec_time:.4f} s, about {loop_time / vec_time:.0f} times faster")
```

On a typical computer the vectorised sum is tens of times faster (our test: about 40×). The same applies to
arithmetic (`readings["pm25"] * 2`), comparisons (`readings["pm25"] > 100`), conditional values
(`np.where(readings["pm25"] > 40, "high", "ok")`) and string methods (`.str.upper()`). Avoid `iterrows()` and row-wise
`apply` on big tables when a column operation exists.

### Activity (20 min) — PRIMM
1. **Predict** the memory after downcasting; run it.
2. Check that downcasting did not change results: compare `readings.groupby("belt")["pm25"].mean()` with the same on
   `small` (tiny float32 rounding differences are expected).
3. Time the loop vs vectorised sum. **Modify:** time a loop that labels each value "high"/"ok" vs `np.where`.
4. **Investigate:** what happens with `pd.Series([100, 120]).astype("int8") + 50`?

### Common mistakes
* Downcasting without checking the range.
* Using `float32` for values that need many digits.
* Writing loops over rows "because it's clearer" on large data.

**Check (5 min).**
1. int8 holds values from…
2. Why prefer df['a'].sum() to a loop?
3. Risk of too-small types?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Indexes in databases

**Hook (5 min).** Find the phone number of "Ram Thapa" in a phone book sorted by name, and then in a box of 10,000
unsorted cards. Why is one so much faster?

### Explanation
Without help, a database answering `WHERE station = 7` must read **every** row (a **full table scan**). An **index** is
an extra sorted structure (usually a B-tree) on one or more columns that lets the database jump to matching rows, like
the alphabetical order of a phone book.

```python
import sqlite3

con = sqlite3.connect(":memory:")
readings.to_sql("readings", con, index=False)
query = "SELECT AVG(pm25) FROM readings WHERE station = 7"

def time_query(sql, repeats=20):
    start = time.perf_counter()
    for _ in range(repeats):
        con.execute(sql).fetchall()
    return (time.perf_counter() - start) / repeats

before = time_query(query)
con.execute("CREATE INDEX idx_station ON readings(station)")
after = time_query(query)
print(f"before {before * 1000:.1f} ms, after {after * 1000:.1f} ms")
print(con.execute("EXPLAIN QUERY PLAN " + query).fetchall())
```

`EXPLAIN QUERY PLAN` shows how SQLite will run a query: after the index it says `SEARCH readings USING INDEX
idx_station (station=?)` instead of `SCAN readings`. Our test was about 5× faster; the gain grows with table size and
with how **selective** the condition is (station 7 is 2% of rows).

**Indexes have costs:**
* **space** (a copy of the column, sorted, plus pointers);
* **slower writes** (every insert or update must also update the index);
* **little benefit** for conditions matching a large share of rows (e.g. `belt = 'Hill'`, a third of the table), for
  small tables, or for columns never used in `WHERE`, `JOIN` or `ORDER BY`.

So index columns you **filter or join on often** with **many distinct values** (station, district_id, date).

**Bigger than memory.** When data no longer fit in RAM, keep them in a database file (SQLite, PostgreSQL) and pull only
the summary you need with SQL: `pd.read_sql("SELECT station, AVG(pm25) FROM readings GROUP BY station", con)`. Tools like
DuckDB and Polars (Grade 12 and beyond) are designed for this.

### Activity (20 min) — PRIMM
1. **Predict** the speed-up; run the before/after timing and the query plan.
2. Time `WHERE belt = 'Hill'` with and without an index on `belt`. Is it worth it?
3. **Make:** add a composite index on `(station, hour)` and time `WHERE station = 7 AND hour = 8`.

### Common mistakes
* Indexing every column.
* Measuring once, on a tiny table.
* Forgetting that indexes slow down inserts.

**Check (5 min).**
1. What does an index speed up?
2. What does it cost?
3. Which column would you index for WHERE station = 7?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Measure first (`time.perf_counter`, `%timeit`, `memory_usage(deep=True)`); repeat timings; fix the bottleneck.
* Smallest safe dtypes (`int8/16/32`, `float32`, `category`) can cut memory ~10×; check ranges first.
* Vectorised column operations beat Python loops by large factors; avoid row loops on big data.
* Database indexes speed up selective lookups and joins, at the cost of space and slower writes; check with
  `EXPLAIN QUERY PLAN`.
* For data larger than memory: load fewer columns, read in chunks, or aggregate inside a database.

## Practice exercises
1. ★ How many bytes do 1,000,000 values take as `int64`? As `int8`?
2. ★ Which dtype would you choose for: month; district_id (1–77); population; temperature in °C; province name?
3. ★ What does `EXPLAIN QUERY PLAN` tell you?
4. ★★ Time `readings.groupby("belt")["pm25"].mean()` on `readings` and on `small`. Which is faster? Why?
5. ★★ Write a vectorised version of: `for i in range(len(df)): df.loc[i, "pm25_mg"] = df.loc[i, "pm25"] / 1000`.
6. ★★ Read the saved `big.csv` in chunks of 100,000 rows (`pd.read_csv(..., chunksize=100_000)`) and compute the mean
   PM2.5 without loading the whole file at once. (Hint: keep a running sum and count.)
7. ★★ Why might an index on `hour` (24 values) help less than an index on `station` (50 values)? When could it still
   help?
8. ★★★ Explain overflow with `int8`: what is 127 + 1? Why is silent overflow dangerous in data analysis?
9. ★★★ A school's results database has 2 million rows: student_id, subject, mark, year. Which indexes would you create
   for these frequent queries: one student's marks; average mark per subject per year? Justify.
10. ★★★ Design and run a fair benchmark comparing `apply(lambda x: x * 2)` with `* 2` on a column. Report the median of
    5 runs.

## Exercises with real data
**R1. A real big file (RD-08).** The Kalimati prices CSV (≈ 9 MB, about 200,000 rows) is a real "medium" dataset. Load
it, measure memory with `deep=True`, convert `Commodity` and `Unit` to `category` and the date to datetime, and measure
again. Time a `groupby` of mean price by commodity before and after.
*Offline fallback:* the generated 500,000-row table.

**R2. Earthquakes worldwide (RD-05).** Download a larger USGS file (e.g. all magnitude ≥ 2.5 earthquakes worldwide for
one year — tens of thousands of rows). Store it in SQLite, index `mag` or `time`, and time a query for magnitude ≥ 6
before and after.

**R3. Hourly weather (RD-06).** Download **hourly** temperature for Kathmandu for five years from Open-Meteo (about
44,000 rows). Downcast types, resample to daily means, and compare memory and speed.

## Unit project: Make it faster, prove it
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Take a slow analysis (provided, or one of your
own), measure it, find the bottleneck, apply at least two improvements (types, vectorising, indexes, fewer columns),
check that results are unchanged, and report before/after times and memory in a table with a one-paragraph
explanation. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* pandas "Scaling to large datasets" guide (<https://pandas.pydata.org/docs/user_guide/scale.html>).
* SQLite "Query Planning" documentation (<https://sqlite.org/queryplanner.html>): how indexes work, with diagrams.
* DuckDB (<https://duckdb.org>): an in-process database that runs SQL very fast on files larger than memory.
