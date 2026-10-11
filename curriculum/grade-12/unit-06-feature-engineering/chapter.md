# Grade 12 · Unit 6: Feature engineering

> Track: B (code) · Tools: Python, pandas, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** How we represent the data — bins, flags, interactions, categories — often matters more than the choice of model.

**What you will be able to do**

* I can create new features (flags, bins, ratios, logs, interactions, date parts) using domain knowledge.
* I can encode categorical variables correctly with one-hot encoding and explain why numeric codes can mislead.
* I can compare feature sets honestly with cross-validation and avoid feature leakage.

**Words to know:** feature engineering, flag (indicator), binning, ratio, log transform, interaction, one-hot encoding, reference category, `get_dummies`, `ColumnTransformer`, feature leakage, cross-validation. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/features.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Unit 1 (workflow, leakage), Unit 4 (cross-validation), Grade 11 Unit 5 (dummy variables). Setup:

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

h = pd.read_csv("health_synthetic.csv")
y = h["institutional_delivery"]
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

def cv_accuracy(columns):
    """Mean and SD of 5-fold cross-validated accuracy for logistic regression on the given columns."""
    model = make_pipeline(StandardScaler(), LogisticRegression())
    scores = cross_val_score(model, h[columns], y, cv=cv)
    return round(scores.mean(), 3), round(scores.std(), 3)
```

---

## Lesson 1: Creating features

**Hook (5 min).** A model sees `mother_age` as a number from 16 to 42. A midwife knows that very young and older mothers
face higher risks. How could we tell the model what the midwife knows?

### Explanation
A **feature** is any column given to a model. **Feature engineering** is creating better columns from the raw data,
usually with **domain knowledge** (what experts know about the problem). Common kinds:

| Kind | Idea | Example (health table) | pandas |
|---|---|---|---|
| **Flag** (indicator) | a yes/no for a meaningful threshold | 4 or more antenatal visits (the widely used "ANC4" indicator; WHO now recommends at least 8 contacts) | `(h["antenatal_visits"] >= 4).astype(int)` |
| **Bins** | group a number into ranges | age groups <20, 20–34, 35+ | `pd.cut(h["mother_age"], [0, 19, 34, 99])` |
| **Ratio / rate** | relate two numbers | people per room; PM2.5 ÷ PM10 | `a / b` |
| **Log** | compress skewed values | income, population, distance | `np.log10(x)` |
| **Interaction** | an effect that depends on another variable | visits × wealth | `a * b` |
| **Date parts** | month, weekday, season, festival | monsoon flag for rain data | `.dt.month` |
| **Aggregates** | summaries from related tables | number of previous births per mother | `groupby` then `merge` |

```python
h["visits_4plus"] = (h["antenatal_visits"] >= 4).astype(int)
h["poorest_two"] = (h["wealth_quintile"] <= 2).astype(int)
h["visits_x_wealth"] = h["antenatal_visits"] * h["wealth_quintile"]
h["teen_mother"] = (h["mother_age"] < 20).astype(int)
h["older_mother"] = (h["mother_age"] >= 35).astype(int)
print(h[["visits_4plus", "poorest_two", "teen_mother", "older_mother"]].mean().round(3))
```

**Why features help (sometimes).** Linear models can only draw straight-line relationships. A flag lets them capture a
jump at a threshold; an interaction lets the effect of visits differ by wealth; bins capture a U-shape (young and old
both higher risk). Tree models find thresholds themselves, but still benefit from ratios and aggregates they cannot
compute.

**Features must make sense and be available.** Only use information known at prediction time (no leakage); avoid
features that encode sensitive attributes through the back door (Unit 5); keep a written **feature dictionary**: name,
definition, reason.

### Activity (20 min) — PRIMM
1. Brainstorm five features for predicting facility delivery, with a reason from health knowledge for each.
2. **Predict** which will help most; create two of them in pandas.
3. Look at the facility-delivery rate by each new flag (`h.groupby("visits_4plus")["institutional_delivery"].mean()`).
4. **Make:** a feature dictionary table for your features.

### Common mistakes
* Creating features from the label or from information after the event.
* Hundreds of features with no reason (invites overfitting, Unit 4).
* No record of how a feature was computed.

**Check (5 min).**
1. Name a ratio feature.
2. What is an interaction?
3. Why use domain knowledge?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Encoding categories

**Hook (5 min).** Models need numbers. If we code Hill = 1, Mountain = 2, Terai = 3, what does the model think the
"distance" between Hill and Terai is? Does that mean anything?

### Explanation
**Numeric codes impose a false order and spacing.** A linear model with `belt_code` (Hill 1, Mountain 2, Terai 3) can
only make the outcome go steadily up (or down) from Hill to Mountain to Terai. Facility-delivery rates are actually
Hill 0.42, **Mountain 0.32**, Terai 0.49 — Mountain is lowest, not in the middle:

```python
from sklearn.linear_model import LinearRegression

h["belt_code"] = h["ecological_belt"].map({"Hill": 1, "Mountain": 2, "Terai": 3})
wrong = LinearRegression().fit(h[["belt_code"]], y)
print(wrong.predict(pd.DataFrame({"belt_code": [1, 2, 3]})).round(3))     # Hill 0.41, Mountain 0.44, Terai 0.48
print(y.groupby(h["ecological_belt"]).mean().round(3))                    # Hill 0.42, Mountain 0.32, Terai 0.49
```

The coded model predicts Mountain *above* Hill — the opposite of the data.

**One-hot encoding** makes one 0/1 column per category:

```python
dummies = pd.get_dummies(h["ecological_belt"], prefix="belt", drop_first=True).astype(int)
print(dummies.head(3))       # columns belt_Mountain, belt_Terai; Hill is the reference (both 0)
h = pd.concat([h, dummies], axis=1)
right = LinearRegression().fit(h[["belt_Mountain", "belt_Terai"]], y)
print(round(right.intercept_, 3), right.coef_.round(3))      # 0.421 [-0.096  0.071]
```

Now each belt gets its own value: Hill (reference) 0.421, Mountain 0.421 − 0.096 = 0.325, Terai 0.421 + 0.071 = 0.491 —
exactly the group rates.

* `drop_first=True` drops one category (the **reference**) for linear models, to avoid perfect collinearity (Grade 11).
  Trees and k-NN can keep all columns.
* **Ordinal** categories with a real order and roughly equal steps (wealth quintile 1–5, education level) can sometimes
  stay as numbers; check by comparing with one-hot.
* Categories with many levels (77 districts, 753 palikas) create many sparse columns; consider grouping rare categories
  into "other" or using a higher level (province).

**Inside a pipeline.** To encode during cross-validation without leakage and handle categories that appear only in new
data, use scikit-learn's `OneHotEncoder` inside a `ColumnTransformer`:

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

prep = ColumnTransformer([
    ("num", StandardScaler(), ["antenatal_visits", "wealth_quintile"]),
    ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), ["ecological_belt"]),
])
pipe = make_pipeline(prep, LogisticRegression())
scores = cross_val_score(pipe, h[["antenatal_visits", "wealth_quintile", "ecological_belt"]], y, cv=cv)
print(round(scores.mean(), 3))
```

### Activity (20 min) — PRIMM
1. **Predict** the coded model's predictions; run both regressions and compare with the true group rates.
2. One-hot encode belt with and without `drop_first`; look at the columns.
3. **Investigate:** fit the coded and one-hot versions inside the logistic pipeline and compare CV accuracy. Why might
   they be close here even though the coded model is conceptually wrong?
4. **Make:** encode `wealth_quintile` both as a number and one-hot; compare.

### Common mistakes
* Label-encoding nominal categories (1, 2, 3) for linear models.
* Encoding on the full data outside the pipeline (categories and scaling leak across folds).
* Forgetting categories unseen in training (use `handle_unknown="ignore"`).

**Check (5 min).**
1. One-hot of 3 categories makes…
2. Why not 1, 2, 3?
3. What is get_dummies?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Comparing feature sets honestly

**Hook (5 min).** You add a clever new feature and accuracy goes from 0.607 to 0.613. Did it help, or was it luck?

### Explanation
Compare feature sets with **cross-validation** and look at the **spread**, not just the mean:

```python
feature_sets = {
    "A: visits": ["antenatal_visits"],
    "B: visits + wealth": ["antenatal_visits", "wealth_quintile"],
    "C: B + age": ["antenatal_visits", "wealth_quintile", "mother_age"],
    "D: B + belt": ["antenatal_visits", "wealth_quintile", "belt_Mountain", "belt_Terai"],
    "E: engineered": ["visits_4plus", "poorest_two", "visits_x_wealth", "teen_mother", "older_mother",
                      "belt_Mountain", "belt_Terai"],
}
for name, cols in feature_sets.items():
    print(name, cv_accuracy(cols))
```

| Feature set | CV accuracy (mean ± SD) |
|---|---|
| A: visits | 0.609 ± 0.029 |
| B: visits + wealth | 0.607 ± 0.024 |
| C: B + age | 0.595 ± 0.034 |
| D: B + belt | 0.606 ± 0.029 |
| E: engineered | 0.595 ± 0.037 |

**Honest reading:** all differences (≤ 0.014) are much smaller than the spread between folds (≈ 0.03). No feature set is
clearly better; the **simplest — visits alone — is as good as any**. Engineered features did not help *here* because the
synthetic data were generated from visits and wealth directly; in real data, well-chosen features often matter more than
the model. This is a valuable, publishable result: "we tried these features; none improved on a one-feature model."

**Rules for honest comparison**
1. Decide the comparisons in advance; report all of them, not only the winner.
2. Use the same folds for every set (fixed `cv` object).
3. Keep all preprocessing inside the pipeline.
4. Prefer the simplest set within about one SD of the best (Unit 4).
5. Confirm the final choice once on the untouched test set.

**Feature leakage, again.** A feature that is suspiciously good is often a leak: `birth_weight_kg` (known only after
birth), a "follow-up visit done" column, or an ID that encodes the outcome. Ask for each feature: "Would I know this at
the moment of prediction?"

### Activity (20 min) — PRIMM
1. **Predict** which set wins; run the comparison.
2. Add your own engineered set (F). Does it beat A by more than one SD?
3. **Investigate:** add `birth_weight_kg` and see what happens. Why must it be excluded anyway?
4. **Make:** write a 5-line conclusion on which feature set to use and why.

### Common mistakes
* Declaring victory from a single split.
* Trying many sets and reporting only the best.
* Keeping a feature "because it helped" without asking whether it leaks.

**Check (5 min).**
1. Why 5-fold CV?
2. What is leakage in features?
3. Pick the simplest set that is…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Feature engineering turns raw columns into informative ones: flags, bins, ratios, logs, interactions, date parts,
  aggregates — guided by domain knowledge and recorded in a feature dictionary.
* Nominal categories → one-hot encoding (drop a reference for linear models); numeric codes impose false order and
  spacing.
* Encode and scale inside pipelines (`ColumnTransformer`, `OneHotEncoder`) to avoid leakage.
* Compare feature sets with the same CV folds; differences smaller than the spread are noise; prefer the simplest; report
  everything; watch for leaky features.

## Practice exercises
1. ★ Create a feature for "household crowding" from `population` and `households` in the district table.
2. ★ One-hot encode `province` (7 categories) with `drop_first=True`. How many columns?
3. ★ Why is `np.log10` useful for district population?
4. ★★ Using `pd.cut`, bin `mother_age` into <20, 20–34, 35+ and compute the facility-delivery rate in each bin.
5. ★★ Add the interaction `visits_x_wealth` to set B. Does CV accuracy change by more than one SD?
6. ★★ For the air table, create features: month, weekday, winter flag, and PM2.5 yesterday (`shift(1)`). Which are known
   at prediction time for "PM2.5 tomorrow"?
7. ★★ Explain why `drop_first` is not needed for a decision tree.
8. ★★★ Use a `ColumnTransformer` with `OneHotEncoder` for belt and `StandardScaler` for numeric columns; compare CV
   accuracy with set D. Should they match?
9. ★★★ A colleague's model reaches 0.95 accuracy on the health data after adding a column `followup_visit_done`. What do
   you suspect? How would you check?
10. ★★★ Design three engineered features for predicting tomorrow's rain from daily weather data, and explain how you would
    test whether they help.

## Exercises with real data
**R1. Penguin features (RD-17).** Create ratio features (bill length ÷ bill depth) and one-hot encode island and sex.
Compare feature sets for species classification with 5-fold CV. Which single engineered feature helps most?
*Offline fallback:* the health table, as in the lessons.

**R2. Countries (RD-01).** Predict life expectancy from GDP per capita (raw vs log), urban share and electricity access.
Compare MAE with 5-fold CV for raw vs log income. Explain the difference.

**R3. Prices with calendar features (RD-08).** For one vegetable's daily Kalimati price, create month, weekday, Dashain/
Tihar window flags (look up the dates each year) and last week's price. Which features help predict next week's price
(time-ordered split!)?

## Unit project: Feature challenge
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Write a feature dictionary, build at least four
feature sets (including a correctly encoded categorical), compare them with the same CV folds, report means and spreads,
check for leakage, choose with the simplest-within-one-SD rule, and test once. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Kaggle Learn, "Feature Engineering" (free).
* scikit-learn user guide, "Column transformer with mixed types" example.
* Max Kuhn and Kjell Johnson, *Feature Engineering and Selection* (free online, <https://bookdown.org/max/FES/>).
