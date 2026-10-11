# Grade 12 · Unit 1: The machine-learning workflow

> Track: B (code) · Tools: Python, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** A trustworthy model follows a workflow: define the task, split the data, set a baseline, train, validate, and test once at the end.

**What you will be able to do**

* I can define a prediction task with a task card: label, features, people affected, decision.
* I can split data into training, validation and test sets and compute a baseline.
* I can train and compare models with scikit-learn pipelines, avoid data leakage, and report a single final test score.

**Words to know:** task card, label, feature, train/validation/test split, stratify, baseline, pipeline, fit, predict, score, hyperparameter, data leakage, generalisation. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/ml_workflow.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Grade 10 Unit 5 (models, baselines, train/test, k-NN) and Grade 11 Units 3–5 (uncertainty, regression). This grade uses
**scikit-learn** (`sklearn`), the standard Python library for machine learning; it is included in `requirements.txt`
and in JupyterLite's Pyodide kernel. Every scikit-learn model has the same three methods: `fit` (learn from data),
`predict` (make predictions), `score` (evaluate).

```python
import numpy as np
import pandas as pd

h = pd.read_csv("health_synthetic.csv")          # 1,500 SYNTHETIC records
features = ["antenatal_visits", "wealth_quintile", "mother_age"]
X = h[features]                                    # capital X: the table of features
y = h["institutional_delivery"]                    # small y: the label (1 = facility, 0 = home)
```

---

## Lesson 1: Define the task

**Hook (5 min).** "Build an AI for the health post." Before writing one line of code: predict **what**, **for whom**, to
do **what**? Write three questions you would ask the health post.

### Explanation
Most failed machine-learning projects fail **before** any code: the task was vague, the label measured the wrong
thing, or nobody planned how predictions would be used. Start with a **task card**:

| Task card | Example |
|---|---|
| **Decision it supports** | Which pregnant women should a health worker visit to discuss facility delivery? |
| **Label** (what we predict) | `institutional_delivery` (1 = birth in a facility) — predicting **0** flags a woman for a visit |
| **Unit** (one row is…) | one pregnancy/birth |
| **Features** (known *at decision time*) | antenatal visits **so far**, wealth quintile, mother's age |
| **Who is affected** | pregnant women, health workers, the health post |
| **How predictions are used** | add women to a visit list; never remove anyone from care |
| **Cost of errors** | missing a woman who would deliver at home (worse) vs an unnecessary visit (cheaper) |
| **Success** | more facility deliveries; fewer missed high-risk women; workload manageable |
| **What we will not do** | use caste/ethnicity; share individual predictions outside the health post |

**Features must be available when the decision is made.** Birth weight is known only after the birth, so it cannot be
a feature for a decision made during pregnancy — using it would be **leakage** (information from the future).

**Is ML even needed?** If a simple rule ("visit everyone with fewer than 4 antenatal visits") works almost as well and
everyone understands it, use the rule. Grade 10 found that such a rule matched k-NN.

### Activity (20 min)
1. In groups, fill in a task card for one scenario: (a) the visit list above; (b) predicting which students might drop
   out of Grade 10, to offer support; (c) predicting next week's PM2.5 to warn schools.
2. For each feature you list, write when it becomes known. Remove any that are not known at decision time.
3. Swap cards with another group: can they find a missing stakeholder or an unfair use?

### Common mistakes
* Starting with "which algorithm?" instead of "which decision?".
* Features from the future (leakage).
* No plan for how predictions will (and won't) be used.

**Check (5 min).**
1. What is the label?
2. What are features?
3. Why describe the decision?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Split and baseline

**Hook (5 min).** A student practises with the same 50 questions until they score 100%. Then they sit the real exam. Why
is the practice score a poor guide? What does this have to do with machine learning?

### Explanation
We need to know how a model will do on **new** cases, so we hide data from it:

| Set | Share | Used for | How often |
|---|---|---|---|
| **Training** | 60% | fitting models | as often as you like |
| **Validation** | 20% | comparing models, choosing settings (hyperparameters) | as often as you like |
| **Test** | 20% | the final, honest estimate | **once**, at the very end |

If you choose between models using the test set, the test score becomes optimistic (you picked the model that got lucky
on it) — it is no longer "unseen".

```python
from sklearn.model_selection import train_test_split

X_tmp, X_test, y_tmp, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_tmp, y_tmp, test_size=0.25, random_state=1, stratify=y_tmp)
print(len(X_train), len(X_val), len(X_test))       # 900 300 300
```

* The second split takes 25% of the remaining 80% = 20% of the whole.
* `stratify=y` keeps the share of 1s the same in every set (44%), which matters when one class is rare.
* `random_state` fixes the shuffle so results are reproducible (Grade 11 Unit 8).
* For **time series**, never shuffle: train on the past, validate and test on later periods.

**Baseline first:**

```python
from sklearn.dummy import DummyClassifier

baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print("baseline validation accuracy:", round(baseline.score(X_val, y_val), 3))     # 0.557
```

Always predicting 0 ("home delivery") is right 55.7% of the time on validation. Any model must beat this to be useful.

### Activity (20 min) — PRIMM
1. **Predict** the sizes of the three sets; run the split.
2. Check that each set has about 44% ones (`y_train.mean()` etc.). Re-run without `stratify` — what changes?
3. Compute the baseline on validation and on training.
4. **Make:** a second baseline — the Grade 10 rule "1 if visits ≥ 4" — and its validation accuracy.

### Common mistakes
* Peeking at test results "just to see".
* Shuffling time-ordered data.
* Splitting after some data-dependent step (scaling, feature selection) on the whole table — leakage (Lesson 3).

**Check (5 min).**
1. Which set do we use to choose between models?
2. Which set do we use only once?
3. Accuracy of always predicting the majority class is…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Train, compare, test

**Hook (5 min).** A model reaches 82% accuracy on its training data. Is that good news? What would you check first?

### Explanation
**Train several candidate models on the training set and compare them on validation:**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

candidates = {
    "logistic regression": make_pipeline(StandardScaler(), LogisticRegression()),
    "k-NN (k = 25)": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=25)),
    "tree (depth 3)": DecisionTreeClassifier(max_depth=3, random_state=0),
    "tree (no limit)": DecisionTreeClassifier(random_state=0),
}
for name, model in candidates.items():
    model.fit(X_train, y_train)
    print(f"{name:20s} train {model.score(X_train, y_train):.3f}   validation {model.score(X_val, y_val):.3f}")
```

| Model | Train | Validation |
|---|---|---|
| logistic regression | 0.609 | 0.597 |
| k-NN (k = 25) | 0.627 | 0.577 |
| tree (depth 3) | 0.620 | 0.610 |
| tree (no limit) | **0.820** | 0.597 |

The unlimited tree "learns" the training data (82%) but is no better on validation: it has **overfitted** (Unit 4).
Logistic regression and the shallow tree are close on validation; we choose **logistic regression** because it is
simpler to explain (Unit 2) and the 1-point difference is within the noise of 300 validation cases.

**Test once:**

```python
final = candidates["logistic regression"]
print("test accuracy:", round(final.score(X_test, y_test), 3))     # 0.587
print("baseline test accuracy:", round(baseline.score(X_test, y_test), 3))    # 0.560
```

**Honest report:** on unseen data the model is right 58.7% of the time against 56.0% for always guessing "home" — a
small gain. These synthetic features carry little information about the outcome; a better model will not fix that.
Better *data* (distance to a facility, previous births, road access) might.

**Pipelines prevent leakage.** `StandardScaler` rescales each feature to mean 0 and SD 1 (important for k-NN and
helpful for logistic regression). The means and SDs must be learned **from the training data only**; scaling the whole
table first would let information from validation/test rows leak into training. A `make_pipeline(scaler, model)` learns
the scaler inside `fit` on the training set and applies the *same* scaling when predicting — automatically.

**Other common leaks:** a feature recorded after the outcome (birth weight); duplicates of the same person in train and
test; target information hidden in an ID or date; choosing features by looking at all the data.

### Activity (20 min) — PRIMM
1. **Predict** which model will have the biggest gap between train and validation; run the comparison.
2. Choose a model with a written reason. Only then run the test cell — once.
3. **Investigate leakage:** add `birth_weight_kg` as a feature (it is known only after birth). Does the score change?
   Why is it still wrong to use?
4. **Make:** write a 3-line summary for the health post: task, baseline, model, test result, one limitation.

### Common mistakes
* Choosing the model with the best **training** score.
* Re-running the test after "improving" the model (the test set is now spent).
* Scaling before splitting.

**Check (5 min).**
1. What is data leakage?
2. Why use a pipeline?
3. What if the model barely beats baseline?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Start with a task card: decision, label, unit, features known at decision time, people affected, use, error costs,
  success.
* Split train/validation/test (e.g. 60/20/20, stratified, seeded); for time series split by time.
* Always compute a baseline; compare candidates on validation; test **once**.
* Pipelines learn preprocessing from training data only — preventing leakage.
* Report honestly: a small gain over baseline is a finding; better data often beats a fancier model.

## Practice exercises
1. ★ Name the label and three features for predicting whether a farmer's tomato crop will fail from weather and soil
   data. Which features are known at planting time?
2. ★ 2,000 rows: how many go to train, validation and test with a 70/15/15 split?
3. ★ Why `stratify=y`?
4. ★★ Write a task card for "predicting students' SEE results to allocate extra classes". Include two things the
   school must **not** do with the predictions.
5. ★★ A model's validation accuracy is 0.61 and the baseline's is 0.56. With 300 validation cases, is a 5-point gain
   convincing? How could you check? (Hint: Grade 11 bootstrap.)
6. ★★ Explain the leak: "We scaled all 1,500 rows, then split, then trained k-NN."
7. ★★ Train k-NN for k = 5, 15, 25, 51 and plot train and validation accuracy against k. Which k would you choose?
8. ★★★ Your team has run the test set five times while improving the model. What should you do now?
9. ★★★ Predicting next week's air quality: why must the split be by time? What goes wrong with a random split?
10. ★★★ Use `cross_val_score` with 5 folds on the training+validation data (`X_tmp`) for logistic regression and the
    baseline. Report means and spreads. Is the conclusion the same as with one validation split?

## Exercises with real data
**R1. Penguins workflow (RD-17).** Full workflow on Palmer penguins (species from bill and flipper measurements):
task card, stratified 60/20/20 split, baseline, three candidate models in pipelines, validation comparison, one
test score, and a 3-line summary.
*Offline fallback:* the health table, as in the lessons.

**R2. Rain tomorrow (RD-06).** From two years of Open-Meteo daily data for your town, build features known today
(today's rain, temperature, humidity, month) and the label "rain > 1 mm tomorrow". Split by **time** (first 18 months
train, next 3 validation, last 3 test). Compare with the persistence baseline ("same as today").

**R3. Task card for a real problem (RD-20).** Interview a teacher, health worker or ward official about one decision they
make often. Write the task card. Decide, with reasons, whether ML is appropriate at all.

## Unit project: Workflow report
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Hand in a notebook and a one-page report: task
card, split description, baseline, at least three candidates compared on validation, the chosen model with reasons,
one test result, leakage checks, and a plain-language summary with limits. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* scikit-learn user guide, "Getting started" and "Common pitfalls" (<https://scikit-learn.org/stable/>).
* Kaggle Learn, "Intro to Machine Learning" and "Intermediate Machine Learning" (free; covers leakage).
* Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, chapter 2 (end-to-end project).
