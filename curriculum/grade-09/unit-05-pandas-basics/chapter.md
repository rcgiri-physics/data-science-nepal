# Grade 9 · Unit 5: Tables in pandas

> Track: B (code: pandas) · Tools: Python, pandas · Lessons: 4
> Datasets: `census-districts`

**Big idea.** pandas holds a table in a DataFrame; we select, filter, sort and group with short commands — the same ideas as SQL.

**What you will be able to do**

* I can load a CSV into a DataFrame and inspect it.
* I can select columns and filter rows.
* I can sort rows and create new columns.
* I can group and summarise, and check the result.

**Words to know:** library, DataFrame, Series, column, index, filter (Boolean mask), method, groupby, aggregate. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/pandas_basics.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
From Unit 4: variables, lists, functions, `==` vs `=`. From Unit 3: `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`.
Throughout this unit, each pandas command is shown with its **SQL twin**, because the ideas are the same.

| Idea | Spreadsheet | SQL | pandas |
|---|---|---|---|
| choose columns | hide columns | `SELECT a, b` | `df[["a", "b"]]` |
| keep rows | filter | `WHERE …` | `df[condition]` |
| sort | sort | `ORDER BY a DESC` | `df.sort_values("a", ascending=False)` |
| top n | sort + look | `LIMIT 5` | `.head(5)` |
| new column | formula, fill down | `a / b AS rate` | `df["rate"] = df["a"] / df["b"]` |
| group summary | pivot table | `GROUP BY` | `df.groupby("g").agg(...)` |

---

## Lesson 1: Load and inspect

**Hook (5 min).** Someone hands you a table you have never seen. Before calculating anything, what five things do you
check first?

### Explanation
**pandas** is a Python **library** (a package of ready-made tools) for tables. Its main object is the **DataFrame**:
a table with named columns and numbered rows. Each column on its own is a **Series**.

```python
import pandas as pd

df = pd.read_csv("districts_synthetic.csv")   # in the notebook: data_file("census-districts", "districts_synthetic.csv")
print(df.shape)       # (rows, columns)
df.head()             # first 5 rows
```

`import pandas as pd` loads the library under the short name `pd` (everyone uses this name). `read_csv` reads a CSV
file into a DataFrame. In the notebook a helper `data_file(...)` finds the file for you; in your own projects, put the
CSV in the same folder as the notebook and use its name.

**The five-step inspection** (do this every time):

```python
print(df.shape)          # 1. size: (77, 11)
print(df.columns)        # 2. column names
print(df.dtypes)         # 3. types: int64, float64, str
print(df.isna().sum())   # 4. missing values per column
df.describe()            # 5. quick summary of numeric columns
```

* `df.shape` → `(77, 11)`: 77 districts, 11 columns. It is an **attribute** (no brackets).
* `df.dtypes` shows each column's type: `int64` (whole numbers), `float64` (decimals), `str` or `object` (text).
  A numeric column that shows as text means something in it is not a number (Unit 2!).
* `df.isna().sum()` counts missing values per column (all 0 here).
* `df.describe()` gives count, mean, standard deviation, min, quartiles and max for every numeric column. For
  example `literacy_pct`: mean 72.8, min 61.3, median (50%) 73.1, max 83.6.

`head()`, `describe()` and `isna()` are **methods**: functions that belong to the DataFrame, called with a dot and
brackets.

### Activity (20 min) — PRIMM
1. **Predict** the shape and the type of each column, then run section 1 of the notebook.
2. Run `df.describe()`. Which district has the smallest population? (Look at min, then find it with
   `df.sort_values("population").head(1)`.)
3. **Investigate:** what do `df.tail(3)` and `df.sample(3)` do?
4. **Make:** load the class survey (`class_survey_synthetic.csv`) and do the five-step inspection.

### Common mistakes
* `df.shape()` with brackets (it is not a method) → `TypeError`.
* Skipping inspection and analysing a column of numbers stored as text.
* Wrong file path → `FileNotFoundError`: check the file name and folder.

**Check (5 min).**
1. Which method shows the first rows?
2. What does .shape return?
3. Why check dtypes?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Select and filter

**Hook (5 min).** Show only the Hill districts with literacy above 80%. Write it in SQL first (you know how!), then
guess the pandas version.

### Explanation
**Selecting columns.** One column → a Series; a **list** of columns → a DataFrame (note the double brackets):

```python
df["literacy_pct"]                          # one column (Series)
df[["district", "literacy_pct"]]           # two columns (DataFrame)
df["literacy_pct"].mean()                  # 72.77...
```

**Filtering rows** happens in two steps. First a **condition** gives `True`/`False` for every row (a **Boolean
mask**); then `df[mask]` keeps the `True` rows:

```python
is_hill = df["ecological_belt"] == "Hill"   # 77 True/False values
hill = df[is_hill]                         # 39 rows
print(len(hill))
```

Usually we write it in one line. To **combine** conditions use `&` (and), `|` (or), `~` (not), with **brackets around
each condition**:

```python
top_hill = df[(df["ecological_belt"] == "Hill") & (df["literacy_pct"] > 80)]
top_hill[["district", "literacy_pct"]]
```

This returns 9 districts (Hill-01, Hill-06, Hill-10, Hill-11, Hill-13, Hill-18, Hill-26, Hill-28, Hill-39).

SQL twin:

```sql
SELECT district, literacy_pct
FROM districts
WHERE ecological_belt = 'Hill' AND literacy_pct > 80;
```

Useful shortcuts:

```python
df[df["province"].isin([1, 3])]                    # SQL: WHERE province IN (1, 3)
df[df["literacy_pct"].between(60, 65)]             # SQL: BETWEEN 60 AND 65
df.query("ecological_belt == 'Terai' and province == 2")   # SQL-like text
```

### Activity (20 min) — PRIMM
1. **Predict** how many rows each filter returns, then run section 2.
2. Write three filters and, beside each, its SQL `WHERE` twin: (a) province 7; (b) Mountain districts with more than
   80,000 people; (c) districts in province 1 or 3 with literacy below 70%.
3. **Investigate:** remove the brackets in the combined filter. What error appears? Why?

### Common mistakes
* `and` / `or` instead of `&` / `|` → "The truth value of a Series is ambiguous".
* Missing brackets around each condition.
* `=` instead of `==` inside a condition.

**Check (5 min).**
1. df[df['ecological_belt']=='Hill'] does what?
2. Combine two conditions with…
3. SQL twin of a filter?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Sort and new columns

**Hook (5 min).** Which districts have the most people living abroad? Which have the most people abroad **per 1,000
residents**? Will it be the same list?

### Explanation
**Sorting:**

```python
df.sort_values("absentee_population", ascending=False).head(5)
```

`ascending=False` = largest first (SQL `DESC`). Sort by several columns with lists:
`df.sort_values(["ecological_belt", "literacy_pct"], ascending=[True, False])`.

**New columns** are made by arithmetic on whole columns at once (no loop needed — pandas does each row for you):

```python
df["abroad_per_1000"] = 1000 * df["absentee_population"] / df["population"]
df["density"] = df["population"] / df["area_km2"]
df["female_share"] = df["female"] / df["population"]
```

Now compare:

```python
by_count = df.sort_values("absentee_population", ascending=False).head(5)
by_rate = df.sort_values("abroad_per_1000", ascending=False).head(5)
print(by_count[["district", "absentee_population", "abroad_per_1000"]].round(1))
print(by_rate[["district", "absentee_population", "abroad_per_1000"]].round(1))
```

| Top 5 by count | count | per 1,000 | | Top 5 by rate | count | per 1,000 |
|---|---|---|---|---|---|---|
| Terai-17 | 112,031 | 96.7 | | Hill-10 | 51,891 | 121.4 |
| Terai-09 | 111,228 | 69.2 | | Hill-39 | 21,548 | 121.2 |
| Terai-14 | 72,610 | 96.5 | | Hill-36 | 20,528 | 120.7 |
| Terai-13 | 63,998 | 71.0 | | Hill-17 | 44,427 | 117.9 |
| Terai-22 | 62,658 | 102.7 | | Hill-20 | 23,940 | 114.6 |

The two lists share **no** districts. Big Terai districts have the most people abroad because they have the most
people; the Hill districts in the right-hand list lose the biggest **share** of their people. Which list matters
depends on the question: a remittance bank cares about counts; a planner worried about villages without young
workers cares about rates.

**Methods return new tables.** `df.sort_values(...)` gives a **sorted copy**; `df` itself is unchanged. To keep the
result, assign it: `df_sorted = df.sort_values(...)`. Adding a column with `df["new"] = …` *does* change `df`.

### Activity (20 min) — PRIMM
1. **Predict** whether the two top-5 lists will overlap. Run section 3.
2. Add `density` and find the 5 most and least crowded districts.
3. **Make:** add `household_size = population / households`. Which belt has the largest households? (You will
   confirm with `groupby` in Lesson 4.)

### Common mistakes
* Expecting `df.sort_values(...)` to sort `df` permanently.
* Integer vs decimal: pandas division always gives decimals, so no `1.0 *` trick is needed (unlike SQLite).
* Long chains of `.round()` too early; round only for display.

**Check (5 min).**
1. df['rate'] = 1000*df.a/df.b creates…
2. Why rank by rate not count?
3. ascending=False means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: Group and summarise

**Hook (5 min).** Mean literacy by belt, and by province — each in one line of code. (In Unit 1 this took a pivot
table; in Unit 3 a `GROUP BY`.)

### Explanation
`groupby` splits the rows into groups; an **aggregate** then summarises each group. Three common forms:

```python
df.groupby("ecological_belt").size()                       # rows per group (SQL COUNT(*))
df.groupby("ecological_belt")["literacy_pct"].mean()       # one column, one statistic
df.groupby("ecological_belt").agg(
    n_districts=("district", "count"),
    total_population=("population", "sum"),
    mean_literacy=("literacy_pct", "mean"),
).round(1)
```

The last one ("named aggregation") reads as `new_name=("column", "function")` and gives:

| ecological_belt | n_districts | total_population | mean_literacy |
|---|---|---|---|
| Hill | 39 | 11907289 | 77.1 |
| Mountain | 16 | 1060048 | 65.8 |
| Terai | 22 | 14366042 | 70.2 |

SQL twin: `SELECT ecological_belt, COUNT(district), SUM(population), AVG(literacy_pct) FROM districts GROUP BY
ecological_belt`.

Functions you can use: `"count"`, `"sum"`, `"mean"`, `"median"`, `"min"`, `"max"`, `"std"`.

**Always check a grouped result:**

```python
counts = df.groupby("province").size()
assert counts.sum() == len(df) == 77      # every district is in exactly one group
by_belt = df.groupby("ecological_belt")["population"].sum()
assert by_belt.sum() == df["population"].sum()
```

**Group rates the right way.** To get the share of people abroad for each belt, sum first, then divide:

```python
belt = df.groupby("ecological_belt")[["absentee_population", "population"]].sum()
belt["abroad_per_1000"] = 1000 * belt["absentee_population"] / belt["population"]
belt.round(1)
```

Taking `df.groupby("ecological_belt")["abroad_per_1000"].mean()` instead gives the mean of district rates, which
weights a tiny district the same as a huge one (Unit 1's warning, again).

### Activity (20 min) — PRIMM
1. **Predict** the number of rows in each grouped result, then run section 4.
2. Group by province: count of districts, total population, mean literacy. Check that counts add to 77.
3. Compute household size by belt the right way (sum population ÷ sum households).
4. **Make:** answer "Which province has the most people abroad per 1,000?" with a weighted rate.

### Common mistakes
* Forgetting `.reset_index()` when you want the group names back as a normal column (try it).
* Averaging rates instead of summing parts and wholes.
* Not checking that group counts add up.

**Check (5 min).**
1. groupby('belt').size() returns…
2. How can you check a grouped result?
3. SQL twin?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* `pd.read_csv` loads a table; inspect with `shape`, `columns`, `dtypes`, `isna().sum()`, `describe()`.
* `df["col"]` → Series; `df[["a", "b"]]` → DataFrame.
* Filter with a Boolean mask: `df[(cond1) & (cond2)]`; `isin`, `between`, `query`.
* `sort_values(..., ascending=False)`; new columns by arithmetic on whole columns.
* `groupby(...).agg(name=("col", "func"))` = SQL `GROUP BY`; check counts and totals with `assert`.
* For group rates, sum the parts and wholes first, then divide.

## Practice exercises
Use the synthetic district table in the notebook.
1. ★ Show the columns `district`, `province` and `population` for the first 10 rows.
2. ★ How many districts are in province 2? (Two ways: filter + `len`, and `groupby` + `size`.)
3. ★ What is the median population of all districts?
4. ★★ List Terai districts with more than 600,000 people, sorted by population (largest first). Write the SQL twin.
5. ★★ Add `male_share` and find the district with the highest male share.
6. ★★ For each belt, the minimum and maximum literacy (`agg`).
7. ★★ Which province has the highest **weighted** household size (sum population ÷ sum households)?
8. ★★★ Count how many districts in each belt have literacy above the overall median. (Hint: make a True/False column
   and `sum` it in a `groupby`.)
9. ★★★ Explain the difference between `df.sort_values("population")` and
   `df = df.sort_values("population")`.
10. ★★★ Write a function `top_n(df, column, n)` that returns the `n` rows with the largest values of `column`, showing
    `district` and that column. Test it on population.

## Exercises with real data
**R1. Tourism trend in pandas (RD-10).** Load the tourist arrivals CSV from Open Data Nepal. Inspect it (five steps).
Add a column `air_share = arrivals_by_air / total` (use the real column names). Which year had the highest share
arriving by air? Compute the percent change in total arrivals between the first and last year.
*Offline fallback:* group `climate_monthly_synthetic.csv` by `year` and compute total rain per year.

**R2. Kalimati prices (RD-08).** Load the Kalimati CSV (≈ 9 MB; it may take a few seconds). Filter one commodity
(e.g. "Tomato Big(Nepali)" — check the exact spelling with `df["Commodity"].unique()`). Group by year and compute the
mean of the `Average` column. In which year was it most expensive? (Note: the dataset covers June 2013 – May 2021, so
2013 and 2021 are part-years — say so in your answer.)

**R3. South Asia indicators (RD-01).** Download a World Bank indicator for South Asian countries (one CSV). Filter
the latest year, sort by value, and compute the mean of the 8 countries. Is the mean of countries the same as the
value for "South Asia" in the file? Why not?

## Unit project: Same question, SQL and pandas
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose one question about the districts
(e.g. "Which belt has the most people abroad per 1,000?"). Answer it twice — in SQL (Unit 3) and in pandas — show
both, check that the numbers match with `assert`, and write the finding with one limit. Full brief and rubric:
`project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Kaggle Learn "Pandas" (free, short lessons in the browser).
* pandas "10 minutes to pandas" (<https://pandas.pydata.org/docs/user_guide/10min.html>).
* Wes McKinney, *Python for Data Analysis*, 3rd edition — free to read online at <https://wesmckinney.com/book/>
  (by the creator of pandas; Grade 10–11 level).
