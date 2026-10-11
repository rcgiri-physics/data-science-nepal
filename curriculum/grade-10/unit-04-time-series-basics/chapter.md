# Grade 10 · Unit 4: Time series basics

> Track: B (code) · Tools: Python, pandas · Lessons: 3
> Datasets: `climate-monthly`

**Big idea.** Data over time have trend, seasonality and noise. Separate them before claiming something has changed.

**What you will be able to do**

* I can identify trend, seasonality and noise in a time series.
* I can fit a trend to annual means, express it per decade, and test how sensitive it is.
* I can compute anomalies from a baseline and explain why scientists use them.

**Words to know:** time series, trend (प्रवृत्ति), seasonality (मौसमी ढाँचा), noise, annual mean, baseline, anomaly (विचलन), climate, weather. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/time_series.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Unit 1 (dates, `groupby`, `resample`, rolling means) and Unit 3 (`np.polyfit`, slope). The table
`climate_monthly_synthetic.csv` has **synthetic** monthly mean temperature and rainfall for 1991–2020 (360 months), with
a gentle warming trend and a monsoon peak. Setup:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

climate = pd.read_csv("climate_monthly_synthetic.csv")
climate["date"] = pd.to_datetime(dict(year=climate["year"], month=climate["month"], day=1))
```

`pd.to_datetime` can build dates from separate year/month/day columns (we use day 1 of each month).

---

## Lesson 1: Trend, season and noise

**Hook (5 min).** July is hotter than January every year. Is that a "trend"? If this July is hotter than last July,
is that "climate change"?

### Explanation
A **time series** is a sequence of measurements in time order. Most can be thought of as three parts added together:

> value = **trend** + **seasonality** + **noise**

* **Trend:** the long-run direction (slowly warming, population growing).
* **Seasonality:** a pattern that repeats every year (or week, or day): hot summers and cold winters; the monsoon.
* **Noise:** the random wobble left over — a cold week, a late monsoon.

**Weather vs climate.** *Weather* is what happens today or this month. *Climate* is the long-term pattern, usually
judged over **30 years**. One hot month is weather; three decades of warming is climate.

```python
plt.figure(figsize=(10, 3))
plt.plot(climate["date"], climate["mean_temp_c"])
plt.ylabel("Mean temperature (°C)")
plt.title("Monthly mean temperature, 1991–2020 (synthetic data)")
plt.show()
```

The plot is dominated by the **seasonal cycle**: about 10–11 °C in January, 26 °C in July. Any trend is hidden
inside it. Two simple ways to remove seasonality:

1. **Annual means** — one value per year averages over all seasons:

```python
annual = climate.groupby("year")["mean_temp_c"].mean()
print(annual.round(2).head(3))     # 1991 17.73, 1992 18.21, 1993 18.34
print(annual.round(2).tail(3))     # 2018 18.55, 2019 18.61, 2020 18.75
```

2. **Compare the same month** across years (all Januaries, all Julys) — Lesson 3 builds on this.

**Seasonal profile.** The mean for each calendar month (over all years) shows the typical year:

```python
profile = climate.groupby("month")[["mean_temp_c", "rain_mm"]].mean().round(1)
print(profile)
```

In this synthetic table, rain is around 20–30 mm in each dry-season month and 236–487 mm in June–September: the
monsoon brings most of the year's rain (Nepal's real monsoon brings roughly 80% of annual rainfall).

### Activity (20 min) — PRIMM
1. **Predict** where the yearly peaks and troughs are; run the monthly plot and mark them.
2. Compute and plot the annual means. Is there an upward trend? Is every year warmer than the last?
3. Compute the seasonal profile and draw it as a bar chart for rain and a line for temperature.
4. **Make:** what share of each year's rain falls in June–September? (Sum by year with and without a month filter.)

### Common mistakes
* Reading a seasonal rise as a trend.
* Concluding "it's getting colder" from a cold winter.
* Averaging rain (use **totals** per year) when the question is "how much rain fell".

**Check (5 min).**
1. Is a yearly warm summer a trend?
2. Why use annual means for trend?
3. What is noise?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Fitting a trend

**Hook (5 min).** How fast is the temperature rising in this table? Guess a number in °C per decade. How sure are you?

### Explanation
Fit a least-squares line (Unit 3) to the **annual means**:

```python
slope, intercept = np.polyfit(annual.index, annual.values, 1)
print(f"{slope * 10:.2f} °C per decade")     # 0.28 °C per decade

plt.plot(annual.index, annual.values, marker="o")
plt.plot(annual.index, intercept + slope * annual.index, color="black")
plt.ylabel("Annual mean temperature (°C)")
plt.show()
```

The slope is in °C **per year**; multiplying by 10 gives °C **per decade**, the unit climate scientists usually use.
Over 30 years, 0.28 °C per decade adds up to about 0.8 °C.

**How sure are we? Sensitivity checks.** A trend from a short or noisy series can change a lot depending on the years
you choose:

| Start year | Trend (°C per decade) |
|---|---|
| 1991 | 0.28 |
| 2000 | 0.30 |
| 2010 | 0.11 |

Starting in 2010 uses only 11 noisy years and gives a much smaller slope. This is why climate trends need long records,
and why someone who wants to argue "warming has stopped" may pick a convenient start year (**cherry-picking**, Grade
8 Unit 4). Report the period, and check that your conclusion holds for reasonable alternatives. Grade 11 Unit 3 adds a
proper uncertainty range (a confidence interval) using the bootstrap.

**Trends are descriptions, not forecasts.** Extending the line to 2100 assumes the same steady change continues —
real climate projections use physical models and scenarios, not straight lines.

### Activity (20 min) — PRIMM
1. **Predict** the trend per decade; fit it to annual means.
2. Fit trends starting in 1991, 2000, 2005 and 2010 (filter `annual.loc[start:]`). Make a small table. What does this
   tell you about short series?
3. Fit a trend to annual **total rain** (`sum` by year). Is it large compared with the year-to-year variation?
4. **Make:** fit a trend to the monthly series directly (without annual means). Is the slope similar? Why is the
   residual plot ugly?

### Common mistakes
* Fitting a line to monthly data and reporting the seasonal swing as part of the "trend".
* Reporting a slope without its period and units.
* Treating a fitted line as a prediction for the far future.

**Check (5 min).**
1. Slope 0.03 °C/yr is how much per decade?
2. Why try different start years?
3. Weather vs climate?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Anomalies

**Hook (5 min).** Is 20 °C warm? In January, very! In July, unusually cold. How can we compare months fairly?

### Explanation
An **anomaly** is the difference between a value and the **usual** value for that time of year:

> anomaly = observed − baseline (for the same calendar month)

The **baseline** is the average over a reference period, usually 30 years (here 1991–2020, the current World
Meteorological Organization standard period).

```python
baseline = climate.groupby("month")["mean_temp_c"].mean()        # 12 values, one per month
climate["anomaly"] = climate["mean_temp_c"] - climate["month"].map(baseline)
annual_anom = climate.groupby("year")["anomaly"].mean()

colors = ["tab:red" if v > 0 else "tab:blue" for v in annual_anom]
plt.bar(annual_anom.index, annual_anom.values, color=colors)
plt.axhline(0, color="black")
plt.ylabel("Anomaly vs 1991–2020 (°C)")
plt.title("Annual temperature anomaly (synthetic data)")
plt.show()
```

`.map(baseline)` looks up each row's month in the 12-value baseline. Anomalies remove the seasonal cycle, so:
* every month can be compared with every other ("January 2017 was 1 °C warmer than a usual January");
* different places can be compared (a mountain station and a Terai station have very different temperatures but
  may have similar anomalies);
* the trend becomes visible as a shift from mostly blue (below 0) bars in the early years to mostly red bars later.
  This "warming stripes" style of chart is used by climate scientists worldwide.

In this synthetic table the warmest year relative to the baseline is 2015. With a baseline of the whole period, the
anomalies of all years average to zero by construction.

### Activity (20 min) — PRIMM
1. **Predict** which years will have positive anomalies; compute and plot annual mean anomalies.
2. Which single month had the largest positive anomaly? (`climate.loc[climate["anomaly"].idxmax()]`)
3. **Modify:** compute rainfall anomalies as a **percent of normal** (observed ÷ baseline × 100). Which monsoon was the
   weakest?
4. **Make:** a "warming stripes" picture: one thin vertical bar per year, coloured by anomaly, no axes.

### Common mistakes
* Subtracting one overall mean instead of the month's own baseline (leaves the season in).
* Comparing anomalies computed with different baselines.
* Reading anomalies as temperatures.

**Check (5 min).**
1. Anomaly = ?
2. Why subtract a monthly baseline?
3. Positive anomaly means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Time series = trend + seasonality + noise. Weather is short-term; climate is the ~30-year pattern.
* Remove seasonality with annual means, same-month comparisons or anomalies.
* Fit trends to annual means; report °C per decade with the period; check sensitivity to start year; don't
  extrapolate far.
* Anomaly = observed − monthly baseline (e.g. 1991–2020); compares months, places and shows trends clearly.
* Rain: use totals per period; percent of normal for anomalies.

## Practice exercises
Use the synthetic climate table.
1. ★ Name trend, seasonality and noise in: monthly sales of umbrellas in Pokhara over 10 years.
2. ★ A slope of 0.045 °C per year is how much per decade? Over 40 years?
3. ★ The baseline for July is 26.3 °C. July 2016 was 26.9 °C. Anomaly?
4. ★★ Which year had the highest annual total rain? The lowest? How different are they?
5. ★★ Compute the trend in **monsoon** (Jun–Sep) rain totals. Compare it with the year-to-year SD of monsoon totals.
   Would you claim the monsoon is changing?
6. ★★ Compare the trend in January temperature with the trend in July temperature (fit each separately). Which
   season warms faster in this table?
7. ★★ Resample the monthly series to annual means using `set_index("date").resample("YS")` and check it equals the
   `groupby("year")` result.
8. ★★★ Use a 1991–2005 baseline instead of 1991–2020. How do the annual anomalies change? Does the trend change?
9. ★★★ A news site says "Temperatures have not risen since 2015!" using this table. Show with numbers why this is
   cherry-picking.
10. ★★★ Write a function `anomalies(df, value_col, base_start, base_end)` that returns the DataFrame with an anomaly
    column. Test that anomalies in the baseline period average to (almost) zero for each month.

## Exercises with real data
**R1. Your town's climate (RD-07).** Download NASA POWER monthly temperature for your town, 1991–2023. Tidy it (Unit 1,
R3), compute annual means, the trend per decade, and anomalies against 1991–2020. Draw warming stripes. Is your
town warming faster or slower than the synthetic table?
*Offline fallback:* the synthetic table, as in the lessons.

**R2. Nepal in the global picture (RD-02).** From Our World in Data, download annual temperature anomalies (chart
`annual-temperature-anomalies`; filter "World" and, if available, "Asia" or Nepal). Plot them, fit a trend for
1991–latest, and compare with your town.

**R3. Tourists over time (RD-10).** Plot tourist arrivals 2001–2014 (Open Data Nepal). Fit a trend. Which years are far
below the trend line (big negative residuals)? Look up what happened in those years.

## Unit project: Climate or weather?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Answer "Is the climate in this table (or your
town) changing, or is it just weather?": show the seasonal profile, annual means with a trend and its sensitivity to
start year, anomalies with a stripes or bar chart, and a conclusion that separates weather from climate and states
the limits (synthetic or modelled data, one location, short record). Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Ed Hawkins' "Show Your Stripes" (<https://showyourstripes.info>): warming stripes for countries and regions,
  including Nepal.
* ICIMOD's Hindu Kush Himalaya Assessment (free reports): how the mountains are warming faster than the global
  average.
* Department of Hydrology and Meteorology (<https://www.dhm.gov.np>): Nepal's official weather and climate data.
