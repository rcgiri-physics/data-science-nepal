# Grade 11 · Unit 6: Time series and seasonality

> Track: B (code) · Tools: Python, pandas, numpy · Lessons: 3
> Datasets: `climate-monthly`

**Big idea.** Separate the repeating seasonal cycle from the long-run trend before judging change; report the trend with uncertainty.

**What you will be able to do**

* I can compute additive and multiplicative seasonal indices and de-seasonalise a series.
* I can fit a trend to a de-seasonalised series and test its sensitivity.
* I can put a bootstrap confidence interval on a trend, resampling the right units.

**Words to know:** seasonal index, additive, multiplicative, de-seasonalise (seasonally adjust), decomposition, trend, residual, autocorrelation, block bootstrap. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/seasonality.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Grade 10 Unit 4 (trend, season, noise, annual means, anomalies) and Unit 3 of this grade (bootstrap). Setup:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

climate = pd.read_csv("climate_monthly_synthetic.csv")      # 1991–2020, synthetic
climate["t"] = climate["year"] + (climate["month"] - 0.5) / 12   # time in years, mid-month
```

`t` turns each month into a decimal year (January 1991 = 1991.04), so a fitted slope is "per year".

---

## Lesson 1: Seasonal indices

**Hook (5 min).** Was January 2020 (10.9 °C, say) colder than July 2019 (26.5 °C)? Obviously — but is that interesting?
How can we compare months from different seasons in a way that *is* interesting?

### Explanation
A **seasonal index** measures how much each calendar month typically differs from the overall level.

**Additive** (for temperature, where the seasonal swing is roughly the same size every year):

> seasonal index for month *m* = mean of all month-*m* values − overall mean

```python
overall = climate["mean_temp_c"].mean()
season_idx = climate.groupby("month")["mean_temp_c"].mean() - overall
print(season_idx.round(2))
print(round(season_idx.sum(), 6))       # 0: additive indices sum to zero
```

Result: January −7.8 °C, April −0.1, July +7.9, October −0.1, December −6.7 °C. The twelve indices sum to 0.

**De-seasonalise** by subtracting each row's index:

```python
climate["temp_sa"] = climate["mean_temp_c"] - climate["month"].map(season_idx)

fig, axes = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
axes[0].plot(climate["t"], climate["mean_temp_c"])
axes[0].set_title("Original (synthetic)")
axes[1].plot(climate["t"], climate["temp_sa"])
axes[1].set_title("Seasonally adjusted")
axes[1].set_xlabel("Year")
plt.tight_layout()
plt.show()
```

The SD of the series drops from 5.7 °C to 0.86 °C once the season is removed: most of the month-to-month variation was
just the seasons. What remains is **trend + noise**, and the slow rise becomes visible. Government statisticians
publish "seasonally adjusted" figures (unemployment, prices, tourist arrivals) for the same reason.

**Multiplicative** indices (for rain, sales, tourists — where the seasonal swing grows with the level):

> seasonal index for month *m* = mean of month-*m* values ÷ overall mean

```python
rain_idx = climate.groupby("month")["rain_mm"].mean() / climate["rain_mm"].mean()
print(rain_idx.round(2))     # Jul 3.67 (3.7 times an average month), Nov 0.15
```

De-seasonalise by **dividing**. Indices average to 1.

(This is the same idea as Grade 10's anomalies: an anomaly is the value minus its month's baseline. Seasonal
adjustment keeps the overall level; anomalies centre it on zero.)

### Activity (20 min) — PRIMM
1. **Predict** the warmest and coldest months' indices; compute additive indices for temperature.
2. De-seasonalise and plot both series. Compare their SDs.
3. Compute multiplicative indices for rain. What share of a year's rain falls in July on average?
4. **Make:** for a tourist-arrivals series (seasonal peaks in autumn and spring), which kind of index would you use, and
   why?

### Common mistakes
* Additive indices for a strongly multiplicative series (or the reverse).
* Comparing raw January and July values to talk about change.
* Forgetting that indices estimated from few years are noisy.

**Check (5 min).**
1. Seasonal indices sum to…
2. Why de-seasonalise?
3. Is a cold January evidence against warming?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Trend with a fitted line

**Hook (5 min).** How fast is this synthetic place warming — per decade? Would you get the same answer from monthly
data and from annual means?

### Explanation
Fit a least-squares line to the de-seasonalised monthly series:

```python
slope, intercept = np.polyfit(climate["t"], climate["temp_sa"], 1)
print(f"{slope * 10:.2f} °C per decade")       # 0.28 °C per decade
```

Annual means (Grade 10) give the same 0.28 °C per decade: both methods remove the season. Monthly data give 12 times
as many points, but neighbouring months are **not independent** (a warm spell can last several months), so they do not
carry 12 times as much information.

**Autocorrelation** measures how similar a series is to itself shifted by one step:

```python
print(round(climate["mean_temp_c"].autocorr(1), 2))     # 0.85 — mostly the season
print(round(climate["temp_sa"].autocorr(1), 2))         # 0.10 — after removing it
```

Most of the raw series' autocorrelation came from the season. Real climate series often keep noticeable
autocorrelation after adjustment (El Niño years, long dry spells), which makes trends less certain than naive
calculations suggest.

**Sensitivity again.** Fit the trend from different start years and on the last 10, 15, 20, 30 years. A trend that
flips sign when you move the start by three years is not a robust finding.

**Trend ≠ forecast.** A fitted line summarises the past; projecting it decades ahead assumes nothing changes in the
causes. Climate projections use physical models and emissions scenarios.

### Activity (20 min) — PRIMM
1. **Predict** whether the monthly and annual methods agree; run both.
2. Compute autocorrelations before and after seasonal adjustment.
3. Make a table of trends starting in 1991, 1996, 2001, 2006, 2011.
4. **Make:** plot the de-seasonalised series with the fitted line and a 12-month rolling mean.

### Common mistakes
* Fitting a line to the raw seasonal series.
* Treating 360 monthly values as 360 independent pieces of information.
* Reporting a trend without its period.

**Check (5 min).**
1. Slope 0.03/yr → per decade?
2. Why try different start years?
3. Short series risk?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Trend with uncertainty

**Hook (5 min).** 0.28 °C per decade. Could a series with **no** real trend have produced a slope like that just from
noisy years? How sure are we?

### Explanation
Use the bootstrap (Unit 3) — but resample the **right units**. Months within a year are related, so resampling single
months would pretend we have more independent information than we do. Resample **whole years** (a simple **block
bootstrap**: each year is a block of 12 months, or one annual mean):

```python
annual = climate.groupby("year")["mean_temp_c"].mean()
rng = np.random.default_rng(0)
years = annual.index.to_numpy()
boot_slopes = []
for _ in range(1000):
    pick = rng.choice(years, size=len(years), replace=True)   # resample years
    sample = annual.loc[pick]
    boot_slopes.append(np.polyfit(sample.index, sample.values, 1)[0] * 10)
low, high = np.percentile(boot_slopes, [2.5, 97.5])
print(f"trend 0.28 °C/decade, 95% CI {low:.2f} to {high:.2f}")   # about 0.18 to 0.39
```

The interval excludes 0: in this series, the warming trend is unlikely to be just year-to-year noise.

**Shorter records, wider intervals:**

| Period | Trend (°C/decade) | 95% bootstrap CI |
|---|---|---|
| 1991–2020 (30 yr) | 0.28 | 0.18 to 0.39 |
| 2005–2020 (16 yr) | 0.34 | 0.12 to 0.64 |
| 2011–2020 (10 yr) | 0.10 | −0.39 to 0.76 |

Ten years cannot tell warming from cooling; thirty years can. This is why climate is judged over decades.

**Rain is noisier.** The trend in annual rain totals is about +119 mm per decade, but its bootstrap interval runs from
about −28 to +274 mm: it includes 0 — no clear evidence of a rainfall trend in this series.

**What a trend interval does not tell you:** the cause (greenhouse gases, local land use, station moved, instrument
changed), or what happens next. Real station records also have **inhomogeneities** — a station moved from a city centre
to an airport can create a fake jump. Climate scientists correct for these before computing trends.

### Activity (20 min) — PRIMM
1. **Predict** whether the 30-year interval includes 0; run the bootstrap.
2. Repeat for 2005–2020 and 2011–2020; fill in the table.
3. Bootstrap the trend in annual rain; does its interval include 0?
4. **Make:** plot the bootstrap slopes as a histogram with lines at 0 and at the observed slope.

### Common mistakes
* Resampling months instead of years.
* Saying "the interval excludes 0, so climate change is caused by…" (the interval is about the size of the trend, not
  its cause).
* Ignoring that real station data may have breaks.

**Check (5 min).**
1. Why resample whole years?
2. Interval excludes 0 means…
3. Does it prove cause?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Additive seasonal index = month mean − overall mean (sum 0); multiplicative = month mean ÷ overall mean (average 1).
* De-seasonalise by subtracting (or dividing by) the index; the rest is trend + noise.
* Fit trends to de-seasonalised or annual data; report per decade with the period; test sensitivity to start year.
* Neighbouring values are autocorrelated; resample whole years (block bootstrap) for trend intervals.
* Short records give wide intervals; intervals say nothing about causes or the future; real records need homogenisation.

## Practice exercises
1. ★ Additive indices: Jan −7.8, Jul +7.9 °C. A January is 10.2 °C. What is its seasonally adjusted value?
   (Hint: subtract the index.) Is that January warmer or colder than usual, if the overall mean is 18.5 °C?
2. ★ Multiplicative index for July rain is 3.67 and an average month has 132 mm. Expected July rain?
3. ★ Why do we resample years rather than months?
4. ★★ Compute additive indices for rain and explain why they are less sensible than multiplicative ones.
5. ★★ Fit separate trends for the four seasons (Dec–Feb, Mar–May, Jun–Aug, Sep–Nov) on de-seasonalised data. Which
   season warms fastest?
6. ★★ Compute a 95% bootstrap interval for the trend in **January** temperature only. Why is it wider than the annual
   one?
7. ★★ Seasonally adjust monthly rain multiplicatively and find the month with the largest adjusted value. What does
   it mean?
8. ★★★ Simulate a series with **no** trend (`overall + season_idx + noise`, noise SD 0.86) for 30 years and bootstrap
   the trend 200 times. How often does the 95% interval exclude 0? What should it be?
9. ★★★ A station moved in 2005 to a place 1 °C cooler. Simulate this jump in the synthetic data (subtract 1 °C from
   2005 on) and recompute the trend. What would a careless analyst conclude?
10. ★★★ Explain the difference between a seasonally adjusted series, an anomaly series and a 12-month rolling mean.
    When would you use each?

## Exercises with real data
**R1. Your town, properly (RD-07).** Using 1991–2023 NASA POWER monthly temperature for your town: seasonal indices,
de-seasonalised series, trend per decade with a year-block bootstrap interval, and the sensitivity table. Compare with
the synthetic numbers.
*Offline fallback:* the synthetic table, as in the lessons.

**R2. Tourists' seasons (RD-10 or MoCTCA reports).** Find monthly tourist arrivals for several years (Nepal Tourism
Statistics reports publish them). Compute multiplicative seasonal indices. Which months are peak season? Seasonally
adjust and look for a trend (and for shocks like 2015 and 2020).

**R3. Vegetable price seasons (RD-08).** For tomatoes in the Kalimati data, compute monthly multiplicative indices of the
average price. When is the cheapest month? Seasonally adjust and fit a 2013–2021 trend with a bootstrap interval.

## Unit project: Climate or weather?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Produce a seasonal decomposition (indices,
adjusted series), a trend with a year-block bootstrap interval, a sensitivity table, and a conclusion that separates
weather from climate and names what the analysis cannot show (cause, station changes, future). Full brief and rubric:
`project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Rob Hyndman and George Athanasopoulos, *Forecasting: Principles and Practice* (free online textbook,
  <https://otexts.com/fpp3/>), chapters on decomposition.
* Berkeley Earth and Copernicus climate pages: how professional temperature records are homogenised.
