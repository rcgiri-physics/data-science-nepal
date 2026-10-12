# Grade 10 · Unit 3: Relationships and the line of best fit

> Track: B (code) · Tools: Python, numpy, matplotlib · Lessons: 3
> Datasets: `kathmandu-air-quality`, `climate-monthly`

**Big idea.** A scatter plot shows if two variables move together; a line of best fit summarises it; correlation is not causation.

**What you will be able to do**

* I can describe a relationship (direction, form, strength, unusual points) and compute *r*.
* I can fit a least-squares line, interpret its slope and intercept, and use residuals to check it.
* I can explain confounding and why correlation does not prove causation.

**Words to know:** explanatory variable, response variable, correlation coefficient (*r*), line of best fit, slope (ढलान), intercept, residual, prediction, extrapolation, confounder. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/best_fit.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic tables).

### Before you start
Grade 9 Unit 6 introduced scatter plots and *r*; Grade 8 Maths has the straight line *y = mx + c*. Setup used below:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

air = pd.read_csv("air_daily_synthetic.csv", parse_dates=["date"], na_values=[-999])
both = air.dropna(subset=["pm25", "pm10"])          # 702 days with both values
climate = pd.read_csv("climate_monthly_synthetic.csv")
```

---

## Lesson 1: Scatter plots and correlation

**Hook (5 min).** On a day when PM2.5 is high, is PM10 usually high too? PM2.5 particles are part of PM10 (PM10 counts
all particles smaller than 10 micrometres). Predict *r* before we compute it.

### Explanation
In a relationship we often call one variable **explanatory** (*x*, on the horizontal axis) and the other the
**response** (*y*, vertical) — the one we want to understand or predict. This is a choice about the question, not a
claim that *x* causes *y*.

```python
plt.scatter(both["pm25"], both["pm10"], s=8, alpha=0.5)
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("PM10 (µg/m³)")
plt.title("Daily PM2.5 and PM10, 2019–2020 (synthetic data)")
plt.show()
print(round(both["pm25"].corr(both["pm10"]), 3))     # 0.986
```

`s` sets dot size and `alpha` transparency, so 700 overlapping dots stay readable.

**What *r* measures.** The correlation coefficient

> *r* = (sum of z_x × z_y) ÷ (n − 1)

multiplies each point's z-scores. Points up-right of the centre (both z positive) or down-left (both negative)
contribute positive products; points in the other two corners contribute negative products. If most points lie in
the up-right/down-left corners, *r* is positive.

Properties:
* −1 ≤ *r* ≤ 1; the sign is the direction, the size the strength **of a straight-line pattern**.
* *r* has no units, and swapping *x* and *y* gives the same *r*.
* *r* = 0 means no **straight-line** relationship. A perfect U-shape can have *r* ≈ 0.
* One extreme point can change *r* a lot. **Always plot first.**

Here *r* = 0.986: a very strong positive linear relationship (by construction in this synthetic data; in real data
PM2.5 and PM10 are also strongly related because PM2.5 is part of PM10).

**Anscombe's quartet** (1973): four small datasets with the same mean, SD and *r* ≈ 0.82, but completely different
scatter plots — a line, a curve, a line with one outlier, and a vertical stack with one far point. The lesson: numbers
alone can hide everything.

### Activity (20 min) — PRIMM
1. **Predict** *r* for PM2.5 vs PM10, then plot and compute.
2. Compute *r* for monthly `mean_temp_c` vs `rain_mm` in the climate table. Plot it. Describe direction, form,
   strength.
3. **Investigate:** make a copy of the air data, add one fake day with PM2.5 = 10 and PM10 = 400, and recompute *r*.
   How much does one point change it?
4. **Make:** guess *r* for five scatter plots your teacher shows (or play "Guess the Correlation" online), then check.

### Common mistakes
* Computing *r* without plotting.
* Calling *r* = 0.5 "50% related" (it is not a percentage).
* Assuming a strong *r* means a straight line is the right model (check the shape).

**Check (5 min).**
1. r = −0.9 means…
2. r = 0 means…
3. Does r show cause?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: The line of best fit

**Hook (5 min).** Everyone draws, by eye, the line that fits the PM2.5–PM10 scatter best. Are all the lines the same?
How could we agree on the "best" one?

### Explanation
A straight line is *y* = *a* + *b x*:
* *b* = **slope**: change in *y* for each 1-unit increase in *x*;
* *a* = **intercept**: predicted *y* when *x* = 0.

For each point the line predicts ŷ ("y-hat"). The miss is the **residual**:

> residual = observed *y* − predicted ŷ

Points above the line have positive residuals; below, negative. The **least-squares line** is the one line that makes
the **sum of squared residuals** as small as possible. Squaring stops positive and negative misses cancelling and
punishes big misses more. Everyone who uses the method gets the same line, and there is a formula:

> *b* = *r* × (SD of *y* ÷ SD of *x*), *a* = mean of *y* − *b* × mean of *x*

The line always passes through the point (mean *x*, mean *y*).

```python
b, a = np.polyfit(both["pm25"], both["pm10"], 1)    # degree 1 = straight line; returns slope first
print(f"PM10 ≈ {a:.1f} + {b:.2f} × PM2.5")            # PM10 ≈ -0.1 + 1.65 × PM2.5

xs = np.linspace(0, 130, 50)
plt.scatter(both["pm25"], both["pm10"], s=8, alpha=0.4)
plt.plot(xs, a + b * xs, color="black")
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("PM10 (µg/m³)")
plt.show()
```

**Interpreting in words** (always with units and "on average"):
* Slope 1.65: "On days when PM2.5 is 1 µg/m³ higher, PM10 is on average about 1.65 µg/m³ higher." Or: PM10 is roughly
  1.65 times PM2.5.
* Intercept −0.1: the predicted PM10 when PM2.5 is 0 — here close to 0, which makes physical sense. Often the
  intercept has no sensible meaning (x = 0 may be far outside the data).

**Predicting.** For a day with PM2.5 = 80: PM10 ≈ −0.1 + 1.65 × 80 ≈ **132** µg/m³. Predicting inside the range of the
data (**interpolation**) is reasonable; predicting far outside it (**extrapolation**: PM2.5 = 500) is risky — the
relationship may change.

**Checking the fit with residuals.** Plot residuals against *x*. A good straight-line fit leaves residuals scattered
randomly around 0. A curve, a funnel (residuals growing with *x*) or clusters mean the line is missing something.

```python
both = both.assign(residual=both["pm10"] - (a + b * both["pm25"]))
plt.scatter(both["pm25"], both["residual"], s=8, alpha=0.4)
plt.axhline(0, color="black")
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("Residual (µg/m³)")
plt.show()
print(round(both["residual"].std(), 1))    # typical miss in µg/m³
```

`r²` (*r* squared) is the share of the variation in *y* that the line accounts for: 0.986² ≈ 0.97, so the line
accounts for about 97% of the day-to-day variation in PM10 (in this synthetic data).

### Activity (20 min) — PRIMM
1. With a ruler, draw your line by eye on a printed scatter; estimate its slope from two points on your line.
2. Fit the least-squares line with `np.polyfit`; compare slopes with your neighbours' by-eye slopes.
3. Write the slope and intercept in words with units. Predict PM10 for PM2.5 = 40 and 100.
4. Plot residuals. Do they look random? What is the typical miss?
5. **Make:** fit a line of `rain_mm` on `mean_temp_c` (climate table) and look at the residual plot. Is a straight line
   a good model here?

### Common mistakes
* Mixing up slope and intercept (`np.polyfit` returns the **slope first**).
* Interpreting the slope without units or without "on average".
* Extrapolating far beyond the data.
* Judging fit by *r* alone, without a residual plot.

**Check (5 min).**
1. Slope 1.6 for PM10 vs PM2.5 means…
2. What is a residual?
3. Why squares?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Correlation is not causation

**Hook (5 min).** In many towns, ice-cream sales and drownings rise and fall together. Does ice-cream cause drowning?
In our climate table, hot months are rainy months (*r* ≈ 0.67). Does heat cause rain? Does rain cause heat?

### Explanation
A correlation between X and Y can arise in several ways:

| Explanation | Diagram | Example |
|---|---|---|
| X causes Y | X → Y | more vaccination → fewer measles cases |
| Y causes X (**reverse causation**) | X ← Y | "hospitals cause death" (sick people go to hospitals) |
| A third variable causes both (**confounding**) | X ← Z → Y | ice-cream and drownings ← hot weather |
| Coincidence (**chance**) | — | small samples, or searching many pairs until one correlates |
| Selection | — | only studying people who came to the clinic |

In the climate table, temperature and rain both follow the **season** (Z): the monsoon arrives in the warm months
because of the large-scale circulation of air between the Indian Ocean and the Asian continent. Heat in Nepal does not
make the rain fall, and rain does not make the months warm. The season is the **confounder**.

**Spotting confounders.** Ask: "What else differs between the high-X and low-X cases?" In Grade 9 Unit 6 the
relationship between people abroad and literacy across districts disappeared **within** each belt — the belt was a
confounder.

**Getting closer to cause.**
1. **Randomised experiment:** randomly assign the cause (e.g. a new teaching method to half of the classes by drawing
   lots). Randomisation makes the groups alike in everything else, on average, including things we can't measure. This
   is the strongest design (Grade 11 Unit 4 analyses experiments).
2. **Compare like with like:** look within groups (within each season, belt, school type), or "control for" the
   confounder in a regression (Grade 11 Unit 5).
3. **Mechanism and consistency:** a plausible explanation, the effect appears in many places and studies, a
   dose–response pattern (more X, more Y), and the cause comes before the effect. Smoking and lung cancer were
   established this way before experiments on people would have been ethical.

### Activity (20 min) — PRIMM
1. Compute *r* between `mean_temp_c` and `rain_mm` for all months; then **within** the monsoon months only (Jun–Sep)
   and within the dry months only. What happens to the relationship? Name the confounder.
2. For each claim, suggest the most likely alternative explanation: (a) "Students who own more books get better marks,
   so books cause good marks"; (b) "Districts with more health posts have more recorded illnesses"; (c) "People who
   drink tea live longer".
3. **Make:** design a fair experiment to test whether a 10-minute morning reading session improves reading speed.
   Who gets the session? How do you decide? What do you measure?

### Common mistakes
* "Correlation proves nothing" — it is often the first clue; it just isn't proof.
* Forgetting reverse causation.
* Thinking a large sample removes confounding (it removes chance, not confounding).

**Check (5 min).**
1. What is a confounder?
2. Give an example.
3. What design supports causal claims?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Plot first; describe direction, form, strength and unusual points; *r* measures **linear** strength, −1 to 1.
* Least-squares line ŷ = *a* + *b x*: slope = average change in *y* per unit of *x* (with units); intercept may have no
  meaning; `np.polyfit(x, y, 1)` returns slope first.
* Residual = observed − predicted; residual plots check the fit; *r²* = share of variation accounted for.
* Interpolate with care; don't extrapolate far.
* Correlation can come from causation, reverse causation, confounding, chance or selection. Randomised experiments
  are the strongest evidence of cause.

## Practice exercises
1. ★ For each pair, which is the explanatory variable? (a) hours studied, exam mark; (b) altitude of a town, mean
   temperature; (c) rainfall, rice harvest.
2. ★ A line is ŷ = 5 + 2*x*. Predict *y* for *x* = 10. A point (10, 22) has what residual?
3. ★ Sketch a scatter plot with *r* ≈ 0 but a clear relationship.
4. ★★ Mean *x* = 20, mean *y* = 50, SD *x* = 4, SD *y* = 10, *r* = 0.8. Find the slope and intercept of the
   least-squares line.
5. ★★ For towns in Nepal, temperature falls about 0.6 °C for each 100 m of altitude (a typical lapse rate). Write
   this as a slope with units. If Biratnagar (≈ 70 m) has a mean annual temperature of about 25 °C, predict a town at
   1,400 m. Why might the prediction be wrong?
6. ★★ Fit a line of `pm25` on `month` for January–June only in the air data. Interpret the slope. Why would a straight
   line over all 12 months be a bad model?
7. ★★ Compute *r²* for PM2.5 vs PM10 and explain it in one sentence.
8. ★★★ A study finds that students who sleep more get higher marks (*r* = 0.4). List three possible explanations and
   design a study that could tell them apart.
9. ★★★ Explain why `np.polyfit(y, x, 1)` gives a different line from `np.polyfit(x, y, 1)`, even though *r* is the
   same.
10. ★★★ Use the formula *r* = Σ(z_x z_y)/(n − 1) to compute *r* by hand for (1, 2), (2, 3), (3, 5), (4, 4), (5, 6).
    Check with pandas.

## Exercises with real data
**R1. Health and wealth (RD-03 / RD-01).** For about 180 countries, plot life expectancy against **log** GDP per capita
(`np.log10`). Fit a least-squares line. Interpret the slope ("for each tenfold increase in income…"). Find Nepal's
residual: does Nepal live longer or shorter than its income predicts?
*Offline fallback:* the PM2.5–PM10 example.

**R2. Altitude and temperature (RD-06).** Use Open-Meteo to get the 2023 mean daily temperature for 8 towns at
different altitudes (e.g. Biratnagar, Janakpur, Pokhara, Kathmandu, Dhankuta, Jumla, Namche Bazaar, Jomsom; look up
each town's altitude). Plot temperature vs altitude, fit a line and find the °C change per 100 m. Which town has the
biggest residual, and why might that be?

**R3. Child mortality and fertility (RD-02).** From Our World in Data, get child mortality and the fertility rate for
all countries for one year. Plot, compute *r*, fit a line. Does lower child mortality *cause* lower fertility, or the
reverse, or a third factor? Write a paragraph using the five explanations from Lesson 3.

## Unit project: Two variables, one honest line
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose two variables (synthetic or real),
make the scatter plot, compute *r*, fit and interpret the line, check residuals, make one prediction inside the
data range, and write a conclusion that discusses causation honestly (at least one possible confounder). Full brief
and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* "Guess the Correlation" (online game) — train your eye.
* Tyler Vigen, *Spurious Correlations* (website and book): absurd correlations that show why cause needs more than *r*.
* Khan Academy, "Exploring bivariate numerical data" (free).
