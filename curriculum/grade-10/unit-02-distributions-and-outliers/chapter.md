# Grade 10 · Unit 2: Distributions and outliers

> Track: B (code) · Tools: Python, pandas, matplotlib · Lessons: 3
> Datasets: `kathmandu-air-quality`

**Big idea.** The shape of data — centre, spread, skew and outliers — decides which summary and which test is fair.

**What you will be able to do**

* I can describe the shape of a distribution and explain what causes skew or two peaks.
* I can compute and interpret the standard deviation, IQR and z-scores.
* I can flag outliers with a rule, investigate them in context, and record a decision.

**Words to know:** distribution (वितरण), skewed, bimodal, standard deviation (मानक विचलन), variance, interquartile range, z-score, outlier, robust. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/distributions.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Grade 8 Unit 5 (mean, median, range, skew) and Grade 9 Unit 6 (histograms, quartiles, box plots). Unit 1 of this grade
cleaned the air table; every example starts with that cleaning:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

air = pd.read_csv("air_daily_synthetic.csv", parse_dates=["date"], na_values=[-999])
air["month"] = air["date"].dt.month
```

---

## Lesson 1: Describing shape

**Hook (5 min).** Someone asks, "What is a typical PM2.5 day in Kathmandu?" Is one number a good answer? Sketch what
you think the histogram of 700 days looks like.

### Explanation
A **distribution** tells us which values occur and how often. Its picture is the histogram; its description has four
parts (from Grade 8): **centre, spread, shape, unusual values**. Common shapes:

| Shape | Picture | Typical examples | Mean vs median |
|---|---|---|---|
| **Symmetric**, one peak | ▁▃▆█▆▃▁ | heights of students of one age; measurement errors | mean ≈ median |
| **Right-skewed** | █▆▄▃▂▁▁ | income, district population, rainfall per day, earthquake magnitudes | mean > median |
| **Left-skewed** | ▁▁▂▃▄▆█ | marks on an easy test, age at death in rich countries | mean < median |
| **Bimodal** (two peaks) | ▆█▃▂▃█▆ | a mixture of two groups (two seasons, boys and girls' heights) | can mislead |
| **Uniform** (flat) | ▅▅▅▅▅▅▅ | dice rolls, day of birth in the month | mean ≈ median |

**Why shape matters.** Means and standard deviations describe symmetric, one-peaked data well. For skewed data use the
median and IQR. For bimodal data, **no single centre is typical**: the "average" may fall in the valley where few
values are. Split the data into its groups and describe each.

**Worked example.** Daily PM2.5 (synthetic, 702 valid days) in bins of 10 µg/m³:

```
  0–10   ████████████████  83
 10–20   ██████████████    73
 20–30   ██████████████    72
 30–40   ██████████        52
 40–50   ███████████       55
 50–60   ██████████        53
 60–70   ████████████      61
 70–80   ███████████████   76
 80–90   ████████████      60
 90–100  █████████████     64
100–110  ███████           34
110–120  ███               16
120–130  █                  3
```

The distribution is very **wide** and roughly **two-humped**: a hump of clean monsoon days below 30 and a hump of
polluted winter days around 70–100. The mean (52.8) and median (52.8) both land in the middle, where there are
relatively few days. A better description: "Most monsoon days are below 20 µg/m³ and most winter days between 70 and
110 µg/m³." The cause of the two humps is the **season**, a variable not shown in the histogram. Splitting by season
(or month) gives one-peaked distributions.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3), sharex=True)
axes[0].hist(air.loc[air["month"].isin([6, 7, 8]), "pm25"].dropna(), bins=range(0, 140, 5))
axes[0].set_title("Jun–Aug")
axes[1].hist(air.loc[air["month"].isin([12, 1, 2]), "pm25"].dropna(), bins=range(0, 140, 5))
axes[1].set_title("Dec–Feb")
for ax in axes:
    ax.set_xlabel("PM2.5 (µg/m³)")
plt.tight_layout()
plt.show()
```

`sharex=True` gives both panels the same x-axis, so they can be compared fairly.

### Activity (20 min) — PRIMM
1. **Predict** the shape of three histograms: PM2.5 (all days), PM10 (all days), and population of the 77 synthetic
   districts. Then draw them.
2. Describe each with the four parts. For population, compare mean (354,979) and median (298,351): which way is the
   skew?
3. **Make:** split PM2.5 by season and describe each season's shape.

### Common mistakes
* Describing a two-peaked distribution with one number.
* Calling a distribution "normal" just because it has one peak.
* Choosing bins that hide the shape (too few) or make noise (too many).

**Check (5 min).**
1. Right-skewed means…
2. Which summary suits a skewed variable?
3. What does a two-peak histogram suggest?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Spread: SD and IQR

**Hook (5 min).** Two cities have the same mean PM2.5 of 50 µg/m³. In city A it is 45–55 every day; in city B it is
10 on some days and 120 on others. Which city would you rather live in? Which summary shows the difference?

### Explanation
**The standard deviation (SD)** measures the typical distance of values from their mean. Calculation for 4, 6, 8, 10,
12 (mean 8):

| Value | Deviation from mean | Squared |
|---|---|---|
| 4 | −4 | 16 |
| 6 | −2 | 4 |
| 8 | 0 | 0 |
| 10 | 2 | 4 |
| 12 | 4 | 16 |
| | sum = 0 (always!) | sum = 40 |

* The deviations always add to zero, so we **square** them first.
* **Variance** = mean of squared deviations. For a sample we divide by *n* − 1 instead of *n* (a small correction
  that makes sample estimates fairer): 40 ÷ 4 = 10.
* **SD** = √variance = √10 ≈ **3.16**. Square-rooting returns to the original units.

pandas: `pd.Series([4, 6, 8, 10, 12]).std()` → 3.162 (it divides by *n* − 1 by default; NumPy's `np.std` divides by
*n* unless you write `ddof=1`).

**A rule of thumb for one-peaked, roughly symmetric data**: about 68% of values lie within 1 SD of the mean and about
95% within 2 SD. (This "68–95" rule comes from the **normal distribution**, the bell curve, which Grade 11 uses.)

**The IQR** (Q3 − Q1, from Grade 9) is the spread of the middle half. It ignores the extreme quarter at each end, so it
is **robust**: a few extreme values barely change it. The SD uses every value and **squares** distances, so a single
huge outlier inflates it a lot.

| Summary pair | Use for | Robust? |
|---|---|---|
| mean and SD | roughly symmetric, one peak, no big outliers | no |
| median and IQR | skewed data, outliers, or when unsure | yes |

```python
for col in ["pm25", "pm10"]:
    q1, q3 = air[col].quantile([0.25, 0.75])
    print(col, "mean", round(air[col].mean(), 1), "SD", round(air[col].std(), 1),
          "median", round(air[col].median(), 1), "IQR", round(q3 - q1, 1))
```

Synthetic result: PM2.5 mean 52.8, SD 33.0, median 52.8, IQR 59.0; PM10 mean 87.7, SD 55.4, IQR 95.5. PM10 has the
bigger spread in µg/m³ — but also a bigger mean. To compare spread relative to size, use the **coefficient of
variation** = SD ÷ mean: PM2.5 0.62, PM10 0.63, almost the same.

**z-scores** say how many SDs a value is from the mean: *z* = (value − mean) ÷ SD. A June day with PM2.5 = 39.7 when
June's mean is 12.8 and SD is 8.5 has *z* = (39.7 − 12.8) ÷ 8.5 ≈ **3.2**: very unusual **for June**, though perfectly
ordinary for January. z-scores let you compare values from different groups or units.

### Activity (20 min) — PRIMM
1. Compute the SD of 4, 6, 8, 10, 12 by hand (table), then check with pandas.
2. **Predict** which is larger, the SD of PM2.5 for the whole year or for January only. Compute both. Why?
3. Compute SD and IQR for PM2.5 and PM10. Add one extreme fake value (1,000) to a copy of PM2.5 and recompute. Which
   summary changed more?
4. **Make:** compute the z-score of every day *within its month* (`groupby("month")["pm25"].transform(...)`) and list
   the 5 most unusual days.

### Common mistakes
* Forgetting to square-root (reporting the variance as the spread).
* Using mean ± 2 SD on skewed data (it can give negative pollution!).
* Comparing SDs of variables with very different means without the coefficient of variation.

**Check (5 min).**
1. IQR equals…
2. Which is robust to outliers?
3. Same mean, bigger SD means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Outliers: flag, investigate, decide

**Hook (5 min).** A June day shows PM2.5 = 39.7 µg/m³. In January that would be a clean day. In June it is three times
the usual value. Is it an outlier? An error? A real event (a forest fire? a festival? a broken sensor?)

### Explanation
Dealing with outliers has three steps: **flag → investigate → decide**, all written down.

**1. Flag with a rule.** The two common rules:
* **IQR rule:** below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR (the box-plot dots).
* **z-score rule:** |*z*| > 3 (only for roughly symmetric data).

**Context changes the answer.** Applied to the whole year, the IQR rule flags **no** PM2.5 days: Q1 = 21.6, Q3 = 80.6,
upper fence = 80.6 + 1.5 × 59.0 = 169.1, above the maximum (126.7). The year's spread is so wide (because of the
seasons) that nothing looks unusual. Applied **within each month**, the same rule flags 8 days:

```python
g = air.groupby("month")["pm25"]
q1 = g.transform(lambda s: s.quantile(0.25))
q3 = g.transform(lambda s: s.quantile(0.75))
iqr = q3 - q1
air["flag"] = (air["pm25"] < q1 - 1.5 * iqr) | (air["pm25"] > q3 + 1.5 * iqr)
print(air.loc[air["flag"], ["date", "pm25", "pm10"]])
```

`transform` returns a value for every row (the quartile of that row's month), so each day is compared with its own
month. The flagged days include 2019-06-08 (39.7) and 2019-06-12 (37.4) — high for June — and 2019-10-05 (9.4) —
low for October.

**2. Investigate.** For each flagged value ask:
* Is it **possible**? (negative pollution, 900 µg/m³, a 3-metre student — impossible → error)
* Do **other variables agree**? On 2019-06-08 PM10 was also high (68.3): two separate measurements rising together
  suggests a real event rather than one faulty reading.
* Is there an **explanation** in the world? (A dust storm, a fire, a festival with fireworks, a traffic strike on a
  clean day.) Check news or other sources for that date.
* Is it a **data-entry** problem? (A decimal point moved: 397 instead of 39.7.)

**3. Decide and record.**
* **Error, fixable** → fix it and log the fix.
* **Error, not fixable** → set to missing and log it.
* **Real** → **keep it**. Real extremes are often the most important data (the most polluted day is what a health
  warning is about). If one analysis is very sensitive to it, report results with and without.

| Date | Value | Flag rule | Evidence | Decision | Reason |
|---|---|---|---|---|---|
| 2019-06-08 | 39.7 | June IQR | PM10 also high | keep | consistent across pollutants; plausible event |

### Activity (20 min) — PRIMM
1. **Predict** how many outliers the whole-year IQR rule will flag; then compute it.
2. Run the within-month rule. List the flagged days.
3. For three flagged days, write an investigation row (evidence, decision, reason).
4. **Make:** apply the whole-year rule to the district `population` column. Which districts are flagged? Are they
   errors? (They are large Terai districts: real, keep them.)

### Common mistakes
* Deleting all flagged values automatically.
* Treating "unusual" as "wrong".
* Applying one rule to a mixture of groups (seasons, belts) without thinking about context.

**Check (5 min).**
1. Rule for the upper fence?
2. Do outliers always get deleted?
3. What must you record?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Describe distributions by centre, spread, shape, unusual values; watch for skew and two peaks (often two groups
  mixed).
* SD = typical distance from the mean (squares, average with *n* − 1, square-root); IQR = middle half; IQR and
  median are robust.
* 68–95 rule for bell-shaped data; coefficient of variation compares relative spread; z = (x − mean) ÷ SD.
* Outliers: flag (IQR or |z| > 3) → investigate (possible? other variables? explanation?) → decide (fix, missing,
  keep) → record. Context (month, group) matters.

## Practice exercises
1. ★ Describe the likely shape of: (a) monthly household income in a district; (b) the last digit of phone numbers;
   (c) heights of all Grade 10 boys and girls together.
2. ★ Compute the SD (divide by *n* − 1) of 2, 4, 4, 4, 5, 5, 7, 9 by hand. Check with pandas.
3. ★ Q1 = 30, Q3 = 70. What are the fences? Is 140 an outlier? Is 0?
4. ★★ Mean height 155 cm, SD 7 cm, roughly symmetric. About what share of students are between 141 and 169 cm?
5. ★★ Sita scored 72 in Maths (class mean 60, SD 8) and 80 in Nepali (mean 75, SD 4). In which subject did she do
   better *relative to the class*?
6. ★★ Draw box plots of PM2.5 by month (Grade 9 Unit 6). Which months have dots? Compare with the within-month flags.
7. ★★ Compute mean ± 2 SD for the whole-year PM2.5. Why is the lower limit nonsense?
8. ★★★ A dataset of student heights contains 16.0, 150, 155, 1,580 and 162. Investigate and decide for each odd value;
   write the log rows.
9. ★★★ Show with an example list why the SD is not robust but the IQR is.
10. ★★★ Why might an analyst who removes outliers before computing a city's "worst pollution days" mislead the
    public? Write a short paragraph.

## Exercises with real data
**R1. Real PM2.5 outliers (RD-12).** In the real Kathmandu file (one station, PM2.5, daily means), apply the
within-month IQR rule. Investigate the three highest flags: check the dates in news archives (fires, festivals,
strikes, dust storms). Write your decision table.
*Offline fallback:* the synthetic file (Lesson 3).

**R2. Rainfall is skewed (RD-06).** Download one year of daily rain for a town. Draw the histogram. What share of days
had zero rain? Compare mean and median daily rain. Which better describes "a typical day"? Which better describes "how
much rain fell this year"?

**R3. Earthquakes (RD-05).** For the 2015 USGS list, compute mean, median, SD and IQR of magnitude. Draw a histogram and
a box plot. Is the 7.8 main shock an outlier by the IQR rule? Should it be removed? (Obviously not — explain why in
words a newspaper reader would understand.)

## Unit project: What does a typical day look like?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Answer "What does a typical PM2.5 day look like
in each season?" with histograms by season, the right summaries (with a justification of mean/SD vs median/IQR),
an outlier decision table and a one-paragraph conclusion with limits. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* David Spiegelhalter, *The Art of Statistics* (2019), chapters 2–3: summarising and communicating data.
* Seeing Theory (<https://seeing-theory.brown.edu>): interactive visual introduction to probability and
  distributions.
