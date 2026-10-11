# Grade 12 · Unit 2: Regression and classification

> Track: B (code) · Tools: Python, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** Regression predicts a number; classification predicts a category. Simple models are often the most explainable.

**What you will be able to do**

* I can fit a linear regression with scikit-learn, evaluate it with MAE and R², and explain its coefficients.
* I can fit a logistic regression, explain how it turns features into a probability, and apply a threshold.
* I can choose an appropriate, explainable method for a question and explain a single prediction in plain language.

**Words to know:** regression, classification, mean absolute error (MAE), logistic function (sigmoid), probability, odds, odds ratio, threshold, decision tree, explainability. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/reg_class.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Grade 11 Unit 5 (multiple regression with numpy) and Unit 1 of this grade (workflow, splits, baselines). Setup:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

h = pd.read_csv("health_synthetic.csv")
train, test = train_test_split(h, test_size=0.25, random_state=0)     # 1,125 train, 375 test
```

(For brevity this unit uses a simple train/test split; in a real project, choose models on a validation set as in
Unit 1.)

---

## Lesson 1: Regression: predicting a number

**Hook (5 min).** A health worker asks: "Can you predict a baby's birth weight from the mother's wealth quintile and
number of antenatal visits?" How would you judge whether the predictions are any good?

### Explanation
**Regression** predicts a **number**. Linear regression in scikit-learn:

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

features = ["wealth_quintile", "antenatal_visits"]
reg = LinearRegression().fit(train[features], train["birth_weight_kg"])
print(round(reg.intercept_, 3), reg.coef_.round(3))        # 2.527 [0.06 0.06]

pred = reg.predict(test[features])
print("MAE model   :", round(mean_absolute_error(test["birth_weight_kg"], pred), 3))       # 0.334 kg
baseline = np.full(len(test), train["birth_weight_kg"].mean())
print("MAE baseline:", round(mean_absolute_error(test["birth_weight_kg"], baseline), 3))   # 0.351 kg
print("R² on test  :", round(reg.score(test[features], test["birth_weight_kg"]), 3))       # 0.055
```

* The coefficients are exactly the least-squares solution from Grade 11 (check with `np.linalg.lstsq` on the same
  rows): about **60 g per wealth quintile** and **60 g per visit**, the other held fixed.
* **MAE** (mean absolute error) = average size of the miss, in the outcome's units: 0.334 kg. The regression
  **baseline** predicts the training mean for everyone: MAE 0.351 kg. The model improves the typical miss by only 17 g.
* `score` for a regressor returns **R²** (Grade 11): 0.055 on test. Birth weight depends on much more than wealth and
  visits.

**Which error measure?** MAE is easy to explain ("off by 0.33 kg on average"). **RMSE** (root mean squared error)
punishes big misses more. Always compare with a baseline and report in the outcome's units.

### Activity (20 min) — PRIMM
1. **Predict** whether the model will beat the mean baseline by much; run the cell.
2. Check the coefficients against `np.linalg.lstsq` on the training rows.
3. **Modify:** add `mother_age` and the belt dummies (`pd.get_dummies(h["ecological_belt"], drop_first=True)`). Does MAE
   improve on test?
4. **Make:** predict the birth weight of a baby whose mother is in quintile 3 with 5 visits, and write the sentence a
   health worker would understand — including how wrong it might be.

### Common mistakes
* Reporting R² alone, without the error in real units.
* Forgetting a baseline for regression.
* Treating a prediction for one baby as precise ("2.85 kg") when typical errors are ±0.33 kg.

**Check (5 min).**
1. Regression predicts…
2. Coefficient 0.05 for visits means…
3. Same as Grade 11 least squares?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Classification: predicting a category

**Hook (5 min).** "Will this mother deliver in a facility?" A linear regression on 0/1 can predict 1.3 or −0.2. What
would a better model output?

### Explanation
**Classification** predicts a **category**. **Logistic regression**, despite its name, is a classifier. It computes a
score like linear regression,

> z = b₀ + b₁ × visits + b₂ × wealth

and squeezes it into a **probability** between 0 and 1 with the **logistic (sigmoid) function**:

> p = 1 ÷ (1 + e^(−z))

z = 0 gives p = 0.5; large positive z gives p near 1; large negative z gives p near 0.

```python
from sklearn.linear_model import LogisticRegression

cols = ["antenatal_visits", "wealth_quintile"]
clf = LogisticRegression().fit(train[cols], train["institutional_delivery"])
print(clf.intercept_.round(3), clf.coef_.round(3))          # [-1.593] [[0.345 0.088]]

two_mothers = pd.DataFrame({"antenatal_visits": [1, 6], "wealth_quintile": [1, 5]})
print(clf.predict_proba(two_mothers)[:, 1].round(2))       # [0.24 0.71]
```

For mother A (1 visit, poorest quintile): z = −1.593 + 0.345 × 1 + 0.088 × 1 ≈ −1.16, p = 1 ÷ (1 + e^1.16) ≈ **0.24**.
For mother B (6 visits, richest quintile): p ≈ **0.71**. `predict_proba` returns two columns (probability of 0 and of
1); `[:, 1]` takes the probability of facility delivery.

**Interpreting coefficients through odds.** The **odds** are p ÷ (1 − p). Each extra visit multiplies the odds of
facility delivery by e^0.345 ≈ **1.41** (41% higher odds), holding wealth fixed; each wealth step multiplies them by
e^0.088 ≈ 1.09. These are **odds ratios**: they describe the association in this synthetic data, not a cause.

**From probability to class: the threshold.** `predict` uses 0.5 by default. But the threshold is a **human decision**
about the costs of errors (Unit 3):

```python
p_test = clf.predict_proba(test[cols])[:, 1]
for t in (0.3, 0.4, 0.5, 0.6):
    flagged_home = (p_test < t).sum()          # predicted "home": these women get a visit
    print(f"threshold {t}: {flagged_home} of {len(test)} women flagged for a visit")
```

At threshold 0.5, 270 of 375 women are predicted "home" and flagged; at 0.4, 151; at 0.3, only 34. A health post with
capacity for 150 visits might choose 0.4 — but should also ask how many true "home" deliveries each threshold misses.

### Activity (20 min) — PRIMM
1. **Predict** the probabilities for the two mothers; run the cell; check mother A by hand with the formula.
2. Compute the odds ratios with `np.exp(clf.coef_)` and write them in a sentence each.
3. **Investigate:** plot the predicted probability against visits for wealth quintiles 1 and 5 (an S-shaped curve
   each).
4. **Make:** count flagged women for thresholds 0.3–0.6 and recommend one for a health post that can make 120 visits.

### Common mistakes
* Treating logistic coefficients as changes in probability (they change the log-odds; the effect on probability
  depends on where you start).
* Forgetting that the threshold is a choice.
* Using `predict` when you need probabilities.

**Check (5 min).**
1. Probability range?
2. What turns a probability into a class?
3. Who chooses the threshold?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Choosing and explaining

**Hook (5 min).** A bank uses a model nobody can explain to reject a farmer's loan. A health post uses a rule written on
one page. Which would you trust? Which would you be allowed to question?

### Explanation
**Match the method to the question.**

| Question | Output | Method family |
|---|---|---|
| How much rain will fall tomorrow (mm)? | number | regression |
| Will it rain tomorrow (yes/no)? | category | classification |
| Which of 3 penguin species? | category (3 classes) | multi-class classification |
| How many tourists next month? | number over time | time-series regression/forecasting |

**Simple, explainable models first.** Linear and logistic regression and small **decision trees** can be explained to the
people affected:

```python
from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier(max_depth=2, random_state=0).fit(train[cols], train["institutional_delivery"])
print(export_text(tree, feature_names=cols))
print("tree test accuracy:", round(tree.score(test[cols], test["institutional_delivery"]), 3))
print("logistic test accuracy:", round(clf.score(test[cols], test["institutional_delivery"]), 3))
```

A depth-2 tree is a set of if–then rules ("if visits ≤ 3.5 and wealth ≤ 2.5 → home") that anyone can read.

**Explainability matters most when:**
* decisions affect people's rights, health, money or education;
* people need to be able to **challenge** a decision ("why was I not selected?");
* errors must be found and fixed;
* the organisation must justify its rules publicly.

Complex models (large tree ensembles, neural networks) can be more accurate when there is lots of data and complicated
patterns (images, speech). Use them when the gain is real and the risks are managed — and test whether the gain is real:
with weak features like ours, they rarely beat logistic regression.

**Explaining one prediction in plain language:**
> "The model estimates a 24% chance that Mother A will deliver in a facility. The main reasons are that she has had only
> one antenatal visit so far and is in the poorest wealth group. Mothers in our records with more visits were more likely
> to deliver in a facility. This is an estimate from past records, not a judgement about her; a health worker will visit
> to talk about her plans."

### Activity (20 min)
1. For four scenarios choose regression or classification and a simple first method: (a) monthly electricity demand of
   a town; (b) whether a student will need remedial maths; (c) the price of a plot of land; (d) which crop disease from
   leaf measurements.
2. Fit the depth-2 tree and write its rules as a one-page leaflet for health workers.
3. Write the plain-language explanation for mother B.

### Common mistakes
* Choosing the most complex model by default.
* Explanations full of jargon ("log-odds", "coefficients").
* Explaining a prediction as if it were a fact about the person.

**Check (5 min).**
1. Predict rainfall in mm: type?
2. Predict 'pass/fail': type?
3. Why favour explainable models?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Regression → numbers; judge with MAE/RMSE in real units and R², against a mean baseline. scikit-learn's
  `LinearRegression` = Grade 11 least squares.
* Logistic regression → probability via p = 1 ÷ (1 + e^(−z)); coefficients act on log-odds; e^coef = odds ratio.
* A threshold turns probabilities into classes; it is a human decision based on costs and capacity.
* Prefer simple, explainable models (linear, logistic, shallow trees) when they perform similarly — especially for
  decisions about people.
* Explain predictions in plain words, as estimates, with reasons and next steps.

## Practice exercises
1. ★ Regression or classification? (a) number of patients next week; (b) whether a loan is repaid; (c) a student's
   percentage; (d) which of 5 bus routes a passenger takes.
2. ★ Compute p for z = 0, z = 2 and z = −2.
3. ★ Odds of 3 to 1 — what probability?
4. ★★ With the fitted coefficients, compute by hand the probability for a mother with 4 visits in quintile 3.
5. ★★ An odds ratio of 1.41 per visit. What are the odds ratios for 2 extra visits? For 4?
6. ★★ Fit `LinearRegression` to the 0/1 label `institutional_delivery`. What is the range of its predictions on the test
   set? Why is logistic regression better here?
7. ★★ Compute RMSE and MAE for the birth-weight model. Why is RMSE larger?
8. ★★★ Fit a depth-2 and a depth-10 tree for facility delivery. Compare test accuracy and readability. Which would you
   give a health post?
9. ★★★ A model gives a woman a 0.49 probability; the threshold is 0.5. Explain why treating 0.49 and 0.51 very
   differently can be unfair, and suggest a better practice.
10. ★★★ Write a plain-language explanation of the birth-weight regression for a parents' meeting (100 words, no
    jargon, one limitation).

## Exercises with real data
**R1. Penguins (RD-17).** Regression: predict body mass from flipper length (MAE vs baseline). Classification: logistic
regression for species (3 classes) from bill length and depth; show predicted probabilities for two penguins and
explain one.
*Offline fallback:* the health table.

**R2. Countries (RD-01 / RD-02).** Classify countries as "child mortality below 2%" (yes/no) from GDP per capita and
access to electricity; fit logistic regression and a depth-2 tree; where does Nepal fall, and what probability does the
model give it?

**R3. Rain tomorrow, explained (RD-06).** With the Unit 1 R2 data, fit logistic regression for "rain tomorrow". Explain
the coefficient of "rain today" as an odds ratio. Choose a threshold for a farmer deciding whether to spray pesticide.

## Unit project: Explain a prediction
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Build one regression and one classification
model on the health table (or penguins), evaluate each against a baseline, choose a threshold with a written reason, and
write plain-language explanations for three individual predictions (one that is probably wrong). Full brief and
rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* *An Introduction to Statistical Learning* (free PDF, Python edition), chapter 4 (classification).
* Christoph Molnar, *Interpretable Machine Learning* (free online book): explaining models and predictions.
* StatQuest (Josh Starmer) videos on logistic regression and decision trees.
