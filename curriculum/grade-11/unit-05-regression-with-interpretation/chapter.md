# Grade 11 · Unit 5: Regression with interpretation

> Track: B (code) · Tools: Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** Regression estimates how an outcome changes with one or more variables, holding the others fixed — and must be read with care.

**What you will be able to do**

* I can fit and interpret simple and multiple linear regression in words with units.
* I can explain "holding other variables fixed" and why coefficients change when predictors are added.
* I can check a model with residual plots, R² and a bootstrap interval for a coefficient, and state its limits.

**Words to know:** outcome (response), predictor, coefficient, intercept, multiple regression, "holding fixed" (controlling for), confounding, collinearity, dummy variable, R², residual. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/regression.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Grade 10 Unit 3 (least-squares line, residuals, *r*, confounding) and Unit 3 of this grade (bootstrap). The synthetic
health table again; remember its relationships were **built in** by the generator (wealth and visits raise birth
weight), so the "right answers" are known and say nothing about real mothers.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = pd.read_csv("health_synthetic.csv")
y = h["birth_weight_kg"].to_numpy()

def fit(columns, data=h, outcome="birth_weight_kg"):
    """Least-squares fit of outcome on the given columns. Returns (coefficients, R²)."""
    X = np.column_stack([np.ones(len(data))] + [data[c] for c in columns])
    yy = data[outcome].to_numpy()
    coef, *_ = np.linalg.lstsq(X, yy, rcond=None)
    resid = yy - X @ coef
    r2 = 1 - (resid ** 2).sum() / ((yy - yy.mean()) ** 2).sum()
    return coef, r2
```

`np.linalg.lstsq` solves the least-squares problem for any number of predictors; the column of ones gives the
intercept.

---

## Lesson 1: Simple regression revisited

**Hook (5 min).** In Grade 10 the slope of the PM10–PM2.5 line was 1.65. What did that number mean, in words, with
units? Now predict: do babies of mothers with more antenatal visits weigh more? By how much per visit?

### Explanation
Simple linear regression: **ŷ = a + b x**.

```python
coef, r2 = fit(["antenatal_visits"])
print(coef.round(3), round(r2, 3))      # [2.653 0.077] 0.053
```

* **Slope b = 0.077 kg per visit:** "Babies of mothers who had one more antenatal visit weighed, on average, about
  0.08 kg (80 g) more."
* **Intercept a = 2.65 kg:** the predicted birth weight for a mother with 0 visits. Here it is meaningful (some mothers
  had 0 visits); often the intercept is outside the data and has no useful meaning.
* **R² = 0.053:** visits account for about 5% of the variation in birth weight. Most of the variation comes from
  other things (genes, mother's nutrition and health, length of pregnancy…).

Always check the relationship looks straight before trusting a line:

```python
print(h.groupby("antenatal_visits")["birth_weight_kg"].agg(["mean", "count"]).round(2))
```

Mean birth weight rises steadily from 2.61 kg (0 visits) to about 3.1 kg (6–7 visits) — roughly linear, although the
groups with 7 or 8 visits have only one record each and should not be over-read.

**Words matter.** Say "is associated with", "goes with", "on average" — not "causes", "increases", "makes". The slope
describes a pattern across mothers, not what would happen if one mother had an extra visit.

### Activity (20 min) — PRIMM
1. **Predict** the sign and size of the slope; run the fit.
2. Write the slope and intercept as two sentences with units.
3. **Modify:** fit birth weight on `wealth_quintile`. Interpret the slope.
4. **Make:** draw the scatter (with `alpha`, because many points overlap) and the two fitted lines.

### Common mistakes
* Slope without units, or as a percentage.
* Over-interpreting an intercept far from the data.
* Causal language from observational data.

**Check (5 min).**
1. Slope 0.04 kg per visit means…
2. What does the intercept mean?
3. What is minimised?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Multiple regression

**Hook (5 min).** Richer mothers tend to have more antenatal visits *and* heavier babies. So is the 77 g per visit
really about visits, or partly about wealth? How could we separate them?

### Explanation
**Multiple regression** uses several predictors at once:

> ŷ = a + b₁ × wealth + b₂ × visits

```python
coef, r2 = fit(["wealth_quintile", "antenatal_visits"])
print(coef.round(3), round(r2, 3))      # [2.544 0.062 0.052] 0.089
```

| Model | Visits coefficient (kg/visit) | Wealth coefficient (kg/quintile) | R² |
|---|---|---|---|
| visits only | 0.077 | — | 0.053 |
| wealth only | — | 0.079 | 0.069 |
| both | 0.052 | 0.062 | 0.089 |

**Interpreting a coefficient in multiple regression:** "**Among mothers in the same wealth quintile**, each extra
antenatal visit is associated with about 52 g higher birth weight, on average." This is what "holding wealth fixed" or
"controlling for wealth" means: comparing like with like on the other predictors.

**Why did the visits coefficient shrink from 77 to 52 g?** Visits and wealth are correlated (*r* ≈ 0.36). In the
visits-only model, part of the wealth effect "leaked" into the visits coefficient, because wealthier mothers have more
visits. Adding wealth removes that part — this is **adjusting for a confounder** (Grade 10 Unit 3) inside a model.

**Categorical predictors need dummy variables.** To include ecological belt, make 0/1 columns for all but one category
(the **reference** category):

```python
h["mountain"] = (h["ecological_belt"] == "Mountain").astype(int)
h["terai"] = (h["ecological_belt"] == "Terai").astype(int)          # Hill is the reference
coef, r2 = fit(["wealth_quintile", "antenatal_visits", "mountain", "terai"])
print(coef.round(3))      # mountain ≈ +0.002, terai ≈ −0.022 kg compared with Hill
```

"Compared with Hill mothers of the same wealth and visits, Terai mothers' babies weighed about 22 g less on average" —
a tiny difference.

**Limits of "controlling for":**
* You can only hold fixed what you **measured**. Unmeasured confounders (mother's nutrition, distance to a facility)
  remain.
* **Collinearity:** if two predictors move almost together (e.g. household income and wealth quintile), the model cannot
  tell their effects apart; coefficients become unstable.
* Coefficients describe **associations in this data**, given the other predictors. They become causal only under strong
  assumptions or with randomised designs.

### Activity (20 min) — PRIMM
1. **Predict** whether the visits coefficient will go up or down when wealth is added; run both fits; fill in the table.
2. Compute the correlation between wealth and visits.
3. Add `mother_age`. Does anything change? (In this synthetic data age was not built in, so its coefficient is about 0.)
4. **Make:** add the belt dummies and interpret one belt coefficient in a full sentence.

### Common mistakes
* Interpreting a coefficient without "holding the others fixed".
* Coding a category as 1, 2, 3 (implies equal steps and an order) instead of dummies.
* Adding every available variable "to be safe".

**Check (5 min).**
1. 'Holding visits fixed' means…
2. Why might a coefficient shrink when adding a predictor?
3. Does a coefficient show cause?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Checking the model

**Hook (5 min).** Our best model has R² = 0.09. Is that a bad model? A weather model with R² = 0.95 for tomorrow's
temperature based on today's — is that a great model?

### Explanation
**R²** is the share of the variation in the outcome accounted for by the model (0 to 1). It answers "how much of
the differences between babies does the model capture?" — 9% here. Whether that is "good" depends on the purpose:
* For **explaining** an association (is visits linked to birth weight, given wealth?), a low R² is normal and fine:
  birth weight depends on many things. The coefficient can still be estimated precisely.
* For **predicting** an individual baby's weight, R² = 0.09 is useless: predictions would be off by about the same as
  guessing the mean.
* A very high R² can come from predictors that are almost the same as the outcome (today's temperature predicting
  tomorrow's), or from too many predictors for too little data (**overfitting**, Grade 12).

**Residual plots** check whether a straight-line model is reasonable:

```python
X = np.column_stack([np.ones(len(h)), h["wealth_quintile"], h["antenatal_visits"]])
coef, *_ = np.linalg.lstsq(X, y, rcond=None)
pred = X @ coef
resid = y - pred
plt.scatter(pred, resid, s=6, alpha=0.4)
plt.axhline(0, color="black")
plt.xlabel("Predicted birth weight (kg)")
plt.ylabel("Residual (kg)")
plt.show()
print(round(resid.std(), 3))      # typical size of a miss, in kg
```

Warning signs: a **curve** (the relationship is not straight), a **funnel** (misses get bigger for larger predictions),
**clusters** (a missing categorical variable), or a few huge residuals (outliers or data errors).

**How precise is a coefficient? Bootstrap it** (resample whole records):

```python
rng = np.random.default_rng(0)
boot = []
for _ in range(1000):
    idx = rng.integers(0, len(h), len(h))         # resample rows with replacement
    c, _ = fit(["wealth_quintile", "antenatal_visits"], data=h.iloc[idx])
    boot.append(c[2])                              # visits coefficient
print(np.percentile(boot, [2.5, 97.5]).round(3))  # roughly 0.03 to 0.07 kg per visit
```

The interval excludes 0: in this data the association between visits and birth weight, holding wealth fixed, is clearly
positive — though small (30–70 g per visit) and not proof of cause.

**A model report** states: the question; outcome and predictors with units; coefficients with intervals, in words; R²
and what it means for the purpose; residual check; what was not measured; and "association, not causation" unless the
design supports more.

### Activity (20 min) — PRIMM
1. **Predict** what the residual plot will look like; draw it. Any warning signs?
2. Bootstrap the visits and wealth coefficients; report both intervals.
3. Compute R² for the three models in Lesson 2's table. Which predictor adds most?
4. **Make:** write a 6-line model report for the two-predictor model.

### Common mistakes
* Judging a model only by R².
* Forgetting the residual plot.
* Reporting coefficients without intervals.

**Check (5 min).**
1. What does R² = 0.4 mean?
2. What pattern in residuals is a warning?
3. Is high R² always good?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Simple regression: slope = average change in outcome per unit of predictor (units, "on average", "associated").
* Multiple regression: each coefficient compares cases that are equal on the other predictors; coefficients change when
  correlated predictors are added (adjusting for confounders).
* Categories enter as 0/1 dummy variables against a reference category.
* Only measured confounders can be held fixed; collinearity blurs effects.
* R² = share of variation explained; judge it by purpose. Check residual plots; bootstrap coefficient intervals; write a
  model report.

## Practice exercises
1. ★ A model says ŷ (rice yield, kg per ropani) = 120 + 15 × (fertiliser bags). Interpret 15 and 120.
2. ★ Why do we need *k* − 1 dummy variables for a category with *k* levels?
3. ★ R² = 0.75. Complete: "The model accounts for…"
4. ★★ Using the fitted two-predictor model (2.544 + 0.062 × wealth + 0.052 × visits), predict birth weight for a mother
   in quintile 2 with 4 visits, and in quintile 5 with 4 visits. What is the difference, and which coefficient is it?
5. ★★ Fit institutional delivery (0/1) on visits and wealth (a "linear probability model"). Interpret the visits
   coefficient as percentage points. What is odd about predictions from such a model? (Hint: can they go below 0?)
6. ★★ Make a residual plot of the visits-only model against **wealth**. What pattern do you see, and what does it mean?
7. ★★ Explain collinearity with an example from school data (e.g. hours of study and hours of tuition).
8. ★★★ A news story says: "Each extra year of schooling increases income by Rs 3,000 a month (regression on 2,000
   workers)." List three things you would want to know before believing "increases".
9. ★★★ Simulate the leak: create `fake = h["wealth_quintile"] + noise` (`np.random.default_rng(1).normal(0, 0.3,
   len(h))`) and fit birth weight on wealth and fake. What happens to the coefficients and their bootstrap intervals?
10. ★★★ Bootstrap R² for the two-predictor model. Is R² itself uncertain?

## Exercises with real data
**R1. Penguin body mass (RD-17).** Regress body mass on flipper length; then add species dummies. How does the flipper
coefficient change? Interpret it "holding species fixed". Check residuals by species.
*Offline fallback:* the health table, as in the lessons.

**R2. Countries (RD-01 / RD-02).** For one recent year, regress life expectancy on log₁₀ GDP per capita and on the share
of people with electricity access (or child mortality). How does the income coefficient change when you add the second
predictor? Discuss confounding at country level.

**R3. Temperature and altitude, holding latitude fixed (RD-06).** With 12–15 Nepali towns (altitude, latitude, 2023 mean
temperature from Open-Meteo), regress temperature on altitude, then on altitude and latitude. Interpret the altitude
coefficient per 100 m in both models.

## Unit project: Explain it, don't just fit it
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Answer one question with a multiple regression:
compare single- and multi-predictor coefficients, interpret each in words with units, bootstrap intervals, check
residuals, and write a model report that names unmeasured confounders and avoids causal language unless justified. Full
brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* OpenIntro Statistics (free), chapters on linear and multiple regression.
* Gareth James et al., *An Introduction to Statistical Learning* (free PDF, Python edition), chapter 3.
* Judea Pearl and Dana Mackenzie, *The Book of Why* (2018): causation explained for general readers.
