# Grade 10 · Unit 4: Time series basics

> Track: B (code) · Tools: Python, pandas · Lessons: 3
> Datasets: `climate-monthly`

**Big idea.** Data over time have trend, seasonality and noise. Separate them before claiming something has changed.

**What you will be able to do**

* I can plot a time series and spot trend and seasonal pattern.
* I can compute annual means and a trend per decade.
* I can explain why a seasonal swing is not a trend.

**Words to know:** trend, seasonality, noise, annual mean, anomaly (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/time_series.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Trend, season and noise

**Hook (5 min).** July is hotter than January every year. Is that a 'trend'?

**Concept (≤ 5 min).** Seasonality repeats within a year; trend is a long-run direction; noise is random wobble. Compare same-month values or annual means to see the trend.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Plot the series; mark seasonal peaks; compute annual means.

**Check (5 min).**
1. Is a yearly warm summer a trend?
2. Why use annual means for trend?
3. What is noise?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Fitting a trend

**Hook (5 min).** How fast is the temperature rising in this table — and how sure are you?

**Concept (≤ 5 min).** Fit a line to annual means; the slope times 10 gives change per decade. Short series give uncertain slopes; say so.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute slope per decade; try different start years and see how the slope changes.

**Check (5 min).**
1. Slope 0.03 °C/yr is how much per decade?
2. Why try different start years?
3. Weather vs climate?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Anomalies

**Hook (5 min).** Is 20 °C warm? For which month?

**Concept (≤ 5 min).** An anomaly is the difference from the usual value for that month. It removes seasonality so unusual months stand out.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute monthly anomalies and plot yearly mean anomalies.

**Check (5 min).**
1. Anomaly = ?
2. Why subtract a monthly baseline?
3. Positive anomaly means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Climate or weather?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
