# Grade 10 · Unit 1: pandas deep-dive: cleaning a real-world series

> Track: B (code) · Tools: Python, pandas · Lessons: 4
> Datasets: `kathmandu-air-quality`

**Big idea.** Most data work is preparation: parse dates, fix error codes, handle missing values, and summarise by time or group.

**What you will be able to do**

* I can parse dates and use them to index and slice a time series.
* I can find, count and handle missing values and error codes, and justify my choice.
* I can summarise a series by month and weekday.
* I can smooth a noisy series with a rolling mean and resample it.

**Words to know:** datetime, NaN (not a number), time series, imputation, interpolation, resample, rolling mean (चलायमान औसत), window. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/pandas_cleaning.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
From Grade 9: pandas basics (Unit 5), cleaning logs (Unit 2), `groupby`. In Grade 9 you cleaned the air table in a
spreadsheet; now you will do the same in code, which is **repeatable**: rerun the notebook on next year's file and
every step happens again, exactly. The table is **synthetic** (2019–2020, daily PM2.5 and PM10, with 25 blanks and 4
error codes).

---

## Lesson 1: Parsing and error codes

**Hook (5 min).** Sort these as text: `2/1/2020`, `10/1/2020`, `2020-01-02`, `2020-01-10`. Which order is right? Is
`2/1/2020` the 2nd of January or the 1st of February?

### Explanation
When pandas reads a CSV, dates arrive as **text**. Text sorts letter by letter, so `10/1/2020` comes before
`2/1/2020`. And `2/1/2020` is ambiguous: 2 January (day first, as in Nepal and Britain) or February 1 (month first, as
in the USA). Convert text to real **datetime** values:

```python
import pandas as pd
import numpy as np

air = pd.read_csv("air_daily_synthetic.csv")
print(air.dtypes)                                     # date is text (str/object)
air["date"] = pd.to_datetime(air["date"], format="%Y-%m-%d")
print(air["date"].dtype)                              # datetime64
print(air["date"].min(), air["date"].max())           # 2019-01-01 … 2020-12-31
```

`format="%Y-%m-%d"` says exactly how the text is written (`%Y` 4-digit year, `%m` month, `%d` day). If a value does
not match, pandas raises an error — good: you find the problem instead of guessing. For day-first text use
`format="%d/%m/%Y"`. You can also parse while reading: `pd.read_csv(..., parse_dates=["date"])`.

Once a column is a datetime, the `.dt` accessor gives its parts:

```python
air["year"] = air["date"].dt.year
air["month"] = air["date"].dt.month
air["weekday"] = air["date"].dt.day_name()      # Monday, Tuesday, …
air[["date", "year", "month", "weekday"]].head(3)
```

**Error codes → NaN.** pandas marks a missing number as **NaN** ("not a number", `np.nan`). Summaries skip NaN by
default; they do **not** skip −999. So convert codes to NaN and **count what you changed**:

```python
n_codes = (air["pm25"] == -999).sum()
n_blank_before = air["pm25"].isna().sum()
air["pm25"] = air["pm25"].replace(-999, np.nan)
print(f"{n_codes} error codes replaced; missing before {n_blank_before}, after {air['pm25'].isna().sum()}")
# 4 error codes replaced; missing before 25, after 29
```

A cleaner habit for real files: tell `read_csv` which values mean missing, `pd.read_csv(path, na_values=[-999])`.

**Check that the series is complete.** A daily series should have one row per day. Compare the number of rows with
the number of days in the period:

```python
expected = pd.date_range(air["date"].min(), air["date"].max(), freq="D")
print(len(expected), len(air), air["date"].duplicated().sum())   # 731 731 0
```

2020 was a leap year, so 2019–2020 has 365 + 366 = 731 days. If rows were missing, `air.set_index("date").reindex(expected)`
would insert them as NaN rows, which is much better than silently skipping days.

### Activity (20 min) — PRIMM
1. **Predict** the dtype of `date` before and after `to_datetime`, then run section 1 of the notebook.
2. Replace −999 in `pm25` and check `pm10` too. Print a one-line log for each column.
3. **Investigate:** what happens with `pd.to_datetime("31/12/2020", format="%Y-%m-%d")`? Read the error.
4. **Make:** check that the series has no missing or duplicated days.

### Common mistakes
* Leaving dates as text, then wondering why sorting or plotting is wrong.
* Letting pandas guess the format (`dayfirst` confusions).
* `air["pm25"].replace(-999, np.nan)` without assigning the result back.

**Check (5 min).**
1. Why replace -999 with NaN?
2. What does pd.to_datetime do?
3. What must you record?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Missing values

**Hook (5 min).** Imagine a third of the winter readings were missing. Would the yearly mean still mean something?
Would it be too high or too low?

### Explanation
First **find** missing values, then **look for patterns**, then **decide** — and log it.

```python
print(air["pm25"].isna().sum(), "missing of", len(air))          # 29 of 731
print(air.groupby("month")["pm25"].apply(lambda s: s.isna().sum()))
```

`apply` runs a small function on each group; `lambda s: s.isna().sum()` is a tiny unnamed function: "count the
missing values in this group". In our table the 29 missing days are spread over the year (at most 6 in a month), so
they are unlikely to bias the monthly means much.

**The options**

| Option | pandas | When reasonable | Risk |
|---|---|---|---|
| Leave as NaN | (default: `mean()` skips NaN) | few, scattered missing values | none, if reported |
| Drop rows | `air.dropna(subset=["pm25"])` | analysis needs complete rows | sample shrinks; may bias if missing is not random |
| Fill with a constant | `fillna(air["pm25"].mean())` | almost never for time series | hides missingness; shrinks spread; wrong in seasonal data |
| Fill from neighbours | `ffill()` (copy last value) or `interpolate()` (straight line between neighbours) | short gaps in smooth series | invents data; fine for 1–2 days, bad for weeks |

**A worked comparison.** Filling every gap with the overall mean (52.8) puts winter-level values into June and
summer-level values into January. It also reduces the standard deviation (from 33.0 to 32.3) because 29 values sit
exactly at the centre. Interpolation uses each gap's neighbours and keeps the season. Whatever you do:
1. keep the original column (e.g. create `pm25_filled`, don't overwrite `pm25`);
2. write how many values you filled and how;
3. check that your conclusion does not depend on the choice (compute it both ways).

```python
air["pm25_interp"] = air["pm25"].interpolate()
print(round(air["pm25"].mean(), 1), round(air["pm25_interp"].mean(), 1))   # 52.8 53.0
```

The two means differ by only 0.2 µg/m³, so our yearly conclusion is **robust** to the choice. If they had differed a
lot, that itself would be a finding to report.

### Activity (20 min) — PRIMM
1. **Predict** in which months most values are missing; then count by month.
2. Compute the overall and January mean three ways: NaN skipped, filled with the overall mean, interpolated.
3. Plot January 2020 raw and interpolated on one chart (`plt.plot(x, y, marker="o")`) to see what interpolation
   invents.
4. Write the missing-value paragraph of your cleaning log.

### Common mistakes
* Filling with the mean "to get rid of NaN".
* Using `dropna()` on the whole table, dropping rows because a column you don't need is missing.
* Not reporting how many values were filled.

**Check (5 min).**
1. pandas mean() on a column with NaN does what by default?
2. Why is filling with the mean risky?
3. What should you check about missing data?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Group by month and weekday

**Hook (5 min).** Is the air worse in winter? Is it better at weekends, when (in Nepal) Saturday is the day off and
there is less traffic? Predict both before computing.

### Explanation
With date parts as columns, `groupby` summarises by time:

```python
monthly = air.groupby("month")["pm25"].mean().round(1)
print(monthly)
```

Synthetic result (µg/m³): January 93.3, February 91.4, March 73.7, April 50.9, May 28.8, June 12.8, July 13.6,
August 15.7, September 34.0, October 55.7, November 74.6, December 92.4 — a strong **seasonal cycle**, high in winter,
low in the monsoon.

```python
order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
by_day = air.groupby("weekday")["pm25"].mean().reindex(order).round(1)
print(by_day)
```

`reindex(order)` puts the days in calendar order (Nepal's week starts on Sunday) instead of alphabetical order.
Result: about 49–55 µg/m³ on every day; the lowest are Sunday (49.2) and Saturday (50.8) — a much smaller
difference than between seasons.

**Is a difference real?** A 4 µg/m³ weekday difference when daily values vary by ±33 could easily be chance. Grade 11
(permutation tests) shows how to check. For now, compare the size of a difference with the spread: a 80 µg/m³
seasonal difference is unmistakable; a 4 µg/m³ weekday difference is doubtful. This is also **synthetic** data: real
Kathmandu air may show a weekend effect.

**Resampling** changes the time scale of a series: daily → monthly. It needs the date as the **index**:

```python
s = air.set_index("date")["pm25"]
monthly_series = s.resample("MS").mean()     # "MS" = month start; one value per month, 24 months
print(len(monthly_series))
```

Unlike `groupby("month")`, which merges January 2019 and January 2020, `resample` keeps every month of every year
separate.

### Activity (20 min) — PRIMM
1. **Predict** the dirtiest and cleanest months; run the monthly `groupby` and draw a bar chart.
2. Run the weekday summary. Is the weekend lower? By how much compared with the seasonal difference?
3. **Modify:** use `median` instead of `mean`. Does the pattern change?
4. **Make:** resample to monthly means and plot the 24 values as a line. Compare January 2019 with January 2020.

### Common mistakes
* Alphabetical weekday order on charts.
* Confusing `groupby("month")` (all Januaries together) with `resample("MS")` (each month separately).
* Claiming a small difference is real without comparing it to the spread.

**Check (5 min).**
1. df.groupby('month')['pm25'].mean() returns…
2. Why chart as well as print?
3. What is a doubt you'd raise?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: Rolling means

**Hook (5 min).** Daily PM2.5 jumps up and down. How could you see the slow rise into winter and fall into the monsoon
without the day-to-day noise?

### Explanation
A **rolling mean** (moving average) replaces each day by the mean of a **window** of days around or before it. A 7-day
rolling mean on 10 January averages 4–10 January.

```python
import matplotlib.pyplot as plt

s = air.set_index("date")["pm25"]
plt.plot(s.index, s, alpha=0.3, label="daily")
plt.plot(s.index, s.rolling(7, min_periods=4).mean(), label="7-day mean")
plt.plot(s.index, s.rolling(30, min_periods=15).mean(), label="30-day mean")
plt.title("PM2.5, 2019–2020 (synthetic data)")
plt.ylabel("PM2.5 (µg/m³)")
plt.legend()
plt.show()
```

* The window size controls smoothing: **bigger windows are smoother but react later** and blur short events.
* `min_periods` says how many non-missing days are needed; without it, any NaN in the window gives NaN.
* By default the window is **trailing** (today and the days before). `center=True` centres it, which lines peaks up
  with the dates but cannot be computed for the most recent days.

**Smoothing hides as well as reveals.** The highest 7-day mean is 103.2 µg/m³ (week ending 26 January 2020), but
single days were higher. A health warning should look at daily values; a trend story at smoothed ones. Always keep
the raw series visible (faint) under the smooth line so readers can see both.

### Activity (20 min) — PRIMM
1. **Predict** how the 7-day and 30-day lines will differ, then plot them.
2. Find the date of the highest 7-day mean (`idxmax()`) and the highest single day. How do they compare?
3. **Modify:** try `center=True`. What changes near the start and end of the series?
4. **Make:** a 7-day rolling **median**. When is it better than the mean?

### Common mistakes
* Plotting only the smoothed line (readers cannot see the real variation).
* Forgetting that a trailing window shifts peaks later.
* Using a window longer than the pattern you want to see (a 90-day window hides the season).

**Check (5 min).**
1. What does a 7-day rolling mean do?
2. Bigger window → ?
3. Does smoothing remove real spikes?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* `pd.to_datetime(…, format=…)` turns text into dates; `.dt.year/.month/.day_name()` gives parts; check every day
  is present with `pd.date_range`.
* Convert error codes to NaN (`replace`, or `na_values` when reading) and log counts.
* Missing values: find, look for patterns, decide (leave, drop, interpolate), keep the original column, check
  robustness.
* `groupby` by month/weekday merges years; `resample` keeps each period; order weekdays properly.
* Rolling means smooth noise; bigger windows smooth more and react later; show raw data too.

## Practice exercises
Use the synthetic air table in the notebook.
1. ★ Convert the text `"25/04/2015"` to a datetime (day first). Which weekday was it?
2. ★ How many days in the table have PM2.5 above 100 µg/m³ (after cleaning)?
3. ★ What is the median PM10 for July?
4. ★★ Create `season` with Dec–Feb "winter", Mar–May "spring", Jun–Aug "monsoon", Sep–Nov "autumn" (use `map` with a
   dictionary). Mean PM2.5 by season?
5. ★★ Compare the 2019 and 2020 annual mean PM2.5. Is the difference large compared with the seasonal difference?
6. ★★ Fill missing PM2.5 with `ffill()` and compare the annual mean with the interpolated version.
7. ★★ Resample to weekly means (`"W"`). How many weeks have a mean above 80?
8. ★★★ Compute the ratio PM2.5 ÷ PM10 per day. Plot its 30-day rolling mean. Does the ratio change with the
   seasons?
9. ★★★ Write a function `clean_air(path)` that loads a file, parses dates, replaces −999, adds month and weekday,
   and returns the DataFrame plus a log dictionary of counts. Test it with `assert` on the shipped file.
10. ★★★ Insert 30 consecutive NaN days in December (on a copy) and compare the annual mean computed with NaN skipped
    vs interpolated. Explain why long gaps in a seasonal series are dangerous.

## Exercises with real data
**R1. Real Kathmandu air (RD-12).** Download the Open Data Nepal air-quality file. It is in **long** format (one row
per location, parameter and time). Filter `parameter == "pm25"` and one location; parse dates; check for negative or
impossible values; resample to daily means; compute monthly means; compare with the synthetic table. Write a cleaning
log.
*Offline fallback:* the synthetic table, as in the lessons.

**R2. A year of weather (RD-06).** Download one year of daily maximum temperature and rain for your town from
Open-Meteo (`skiprows=3`). Parse dates, add month, compute monthly mean temperature and monthly **total** rain
(`sum`, not `mean`), plot a 7-day rolling mean of temperature.

**R3. NASA POWER, tidied (RD-07).** Read the NASA POWER monthly CSV (find the line number of `-END HEADER-` and use
`skiprows`). Replace −999; reshape from wide (JAN…DEC columns) to long with
`df.melt(id_vars=["PARAMETER", "YEAR"], value_vars=[...], var_name="month", value_name="value")`; convert rain from mm
per day to mm per month.

## Unit project: Clean series report
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Produce a notebook that cleans a daily series
(synthetic air or a real one from R1–R3), with a printed cleaning log (counts of codes, missing values, decisions), a
monthly summary table, a chart with raw and rolling-mean lines, and a robustness check (your conclusion computed two
ways). Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* pandas user guide, "Time series / date functionality" (<https://pandas.pydata.org/docs/user_guide/timeseries.html>).
* Wes McKinney, *Python for Data Analysis* (free online), chapter "Time Series".
