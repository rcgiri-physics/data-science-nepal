# Grade 10 · Unit 1: pandas deep-dive: cleaning a real-world series

> Track: B (code) · Tools: Python, pandas · Lessons: 4
> Datasets: `kathmandu-air-quality`

**Big idea.** Most data work is preparation: parse dates, fix error codes, handle missing values, and summarise by time or group.

**What you will be able to do**

* I can parse dates and replace error codes with missing values.
* I can handle missing values explicitly.
* I can group a daily series by month and weekday.

**Words to know:** NaN, parse, resample, groupby, rolling mean (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/pandas_cleaning.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Parsing and error codes

**Hook (5 min).** Why does 2020-01-02 sort correctly but '2/1/2020' may not?

**Concept (≤ 5 min).** Convert text dates with pd.to_datetime. Replace error codes (-999) with NaN so they don't distort summaries; log how many.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Load the air table, parse dates, replace -999, count missing values before and after.

**Check (5 min).**
1. Why replace -999 with NaN?
2. What does pd.to_datetime do?
3. What must you record?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Missing values

**Hook (5 min).** A third of the winter readings are missing. Does the mean still mean something?

**Concept (≤ 5 min).** Options: drop, fill with a stated rule, or leave NaN and let pandas skip them. Each choice changes results. Check if missingness clusters (e.g., one month).

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Count missing by month; compute the mean with NaN skipped vs filled with the overall mean; discuss.

**Check (5 min).**
1. pandas mean() on a column with NaN does what by default?
2. Why is filling with the mean risky?
3. What should you check about missing data?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Group by month and weekday

**Hook (5 min).** Is the air worse in winter? Is it better on weekends?

**Concept (≤ 5 min).** Extract month/weekday from dates and use groupby to summarise. Compare patterns with a bar chart.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Group by month and by day-of-week; chart both; state one pattern and one doubt.

**Check (5 min).**
1. df.groupby('month')['pm25'].mean() returns…
2. Why chart as well as print?
3. What is a doubt you'd raise?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: Rolling means

**Hook (5 min).** Daily numbers jump around. How can we see the trend?

**Concept (≤ 5 min).** A rolling mean averages the last k days to smooth noise. Bigger windows smooth more but react slower.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Plot 7-day and 30-day rolling means; describe how the picture changes.

**Check (5 min).**
1. What does a 7-day rolling mean do?
2. Bigger window → ?
3. Does smoothing remove real spikes?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Clean series report

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
