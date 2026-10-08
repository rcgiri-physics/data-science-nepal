# Grade 11 · Unit 6: Time series and seasonality

> Track: B (code) · Tools: Python, pandas, numpy · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `climate-monthly`

**Big idea.** Separate the repeating seasonal cycle from the long-run trend before judging change; report the trend with uncertainty.

**What you will be able to do**

* I can compute seasonal indices.
* I can de-seasonalise a series.
* I can fit a trend with a bootstrap interval.

**Words to know:** seasonal index, de-seasonalise, trend, residual, uncertainty (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/seasonality.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Seasonal indices

**Hook (5 min).** Why can't we compare January 2020 with July 2019 directly?

**Concept (≤ 5 min).** Subtract each month's long-run average from the year-average to get a seasonal index; removing it leaves trend + noise.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute indices for temperature; de-seasonalise; plot before/after.

**Check (5 min).**
1. Seasonal indices sum to…
2. Why de-seasonalise?
3. Is a cold January evidence against warming?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Trend with a fitted line

**Hook (5 min).** How fast is it changing per decade?

**Concept (≤ 5 min).** Fit a line to the de-seasonalised series; multiply slope by 10 for per-decade change. Longer series give steadier trends.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit the trend; try starting from different years; compare.

**Check (5 min).**
1. Slope 0.03/yr → per decade?
2. Why try different start years?
3. Short series risk?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Trend with uncertainty

**Hook (5 min).** How sure are we that the trend isn't zero?

**Concept (≤ 5 min).** Bootstrap years (resample whole years with replacement) and refit; the spread of slopes gives an interval. If it excludes 0 there is evidence of a trend in this series.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Bootstrap the slope 1,000 times; report the 95% interval.

**Check (5 min).**
1. Why resample whole years?
2. Interval excludes 0 means…
3. Does it prove cause?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Climate or weather?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
