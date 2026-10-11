# Teacher guide — Grade 10, Unit 4: Time series basics

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Trend, season and noise | 40–45 min |
| 2 | Fitting a trend | 40–45 min |
| 3 | Anomalies | 40–45 min |
| P | Unit project: Climate or weather? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/time_series.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Plot 12 monthly values by hand; mark the seasonal peak; compute a yearly average.

## Common misconceptions
* A warm month proves climate change; weather ≠ climate.
* Trend lines from short series are unreliable.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Trend, season and noise**
1. Is a yearly warm summer a trend?  
   *Answer:* No, it is seasonality.
2. Why use annual means for trend?  
   *Answer:* They average out the seasonal cycle.
3. What is noise?  
   *Answer:* Random variation not explained by trend or season.

**Lesson 2: Fitting a trend**
1. Slope 0.03 °C/yr is how much per decade?  
   *Answer:* 0.3 °C.
2. Why try different start years?  
   *Answer:* To check how sensitive the trend is.
3. Weather vs climate?  
   *Answer:* Weather is short-term; climate is long-term pattern.

**Lesson 3: Anomalies**
1. Anomaly = ?  
   *Answer:* Observed − usual (baseline) value for that month.
2. Why subtract a monthly baseline?  
   *Answer:* To remove the seasonal cycle.
3. Positive anomaly means…  
   *Answer:* Warmer than usual.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. Trend: tourism growth; seasonality: monsoon peak in umbrella sales; noise: unusual weeks (a dry July).
2. 0.45 °C per decade; 1.8 °C over 40 years.
3. +0.6 °C.
4. Synthetic: highest 2010 (≈ 2,886 mm), lowest 2007 (≈ 825 mm) — a factor of 3.5 (the synthetic rain is very noisy).
5. Trend ≈ +111 mm per decade, but the SD of monsoon totals is ≈ 420 mm: the trend is small compared with year-to-year
   variation over 30 years — no confident claim.
6. January ≈ +0.40 °C/decade, July ≈ −0.13 °C/decade: winter warms faster in this table (real Himalayan records also
   often show stronger winter warming — a nice link, but check sources).
7. `climate.set_index("date")["mean_temp_c"].resample("YS").mean()` gives the same 30 values.
8. Every anomaly shifts by the same amount (+0.22 °C) because the baseline is cooler; the trend (0.28 °C/decade) does
   not change.
9. Annual anomalies 2015–2020: 0.76, 0.33, 0.68, 0.08, 0.15, 0.29 — fitting from 2015 gives −1.0 °C/decade, because
   2015 was the warmest year (a cherry-picked start). From 1991 the trend is +0.28.
10. Check: `df.groupby("month")` of the anomaly within the baseline years ≈ 0 (floating-point tiny values).

Lesson 1 Make: monsoon share of annual rain ≈ 87% on average in the synthetic table. Lesson 2 Make: fitting the
monthly series directly gives ≈ 0.32 °C/decade (the seasonal cycle adds noise and the series starts in January and ends
in December, which nudges the slope); residuals show the seasonal wave. Lesson 3: largest monthly anomaly June 2019
(+2.3 °C); weakest monsoon 2007.

## Real-data exercises: notes
* **R1** NASA POWER (MERRA-2 model) trends for Nepal grid cells are typically a few tenths of a °C per decade; values
  differ by place and are model-based, not station data.
* **R2** The world has warmed ≈ 0.2 °C per decade since the 1970s; recent years are the warmest on record.
* **R3** Dips appear in years of conflict and political crises; 2015 (earthquake) is just after this dataset ends —
  newer MoCTCA reports show it.
