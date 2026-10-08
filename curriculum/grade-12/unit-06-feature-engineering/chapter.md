# Grade 12 · Unit 6: Feature engineering

> Track: B (code) · Tools: Python, pandas, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** How we represent the data — bins, flags, interactions, categories — often matters more than the choice of model.

**What you will be able to do**

* I can create features from raw columns.
* I can encode categories.
* I can compare feature sets with cross-validation.

**Words to know:** feature, encoding, interaction, cross-validation, scaling (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/features.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Creating features

**Hook (5 min).** What could we compute from age, visits and wealth that a model can't see itself?

**Concept (≤ 5 min).** Transform columns into more informative ones: thresholds, ratios, logs, interactions. Use domain knowledge.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Brainstorm 5 features for a task; implement two.

**Check (5 min).**
1. Name a ratio feature.
2. What is an interaction?
3. Why use domain knowledge?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Encoding categories

**Hook (5 min).** Models need numbers. How do we feed in 'Hill', 'Terai', 'Mountain'?

**Concept (≤ 5 min).** One-hot encoding makes a 0/1 column per category. Don't encode categories as 1, 2, 3 (it implies an order).

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** One-hot encode belt; compare to a wrong numeric encoding.

**Check (5 min).**
1. One-hot of 3 categories makes…
2. Why not 1, 2, 3?
3. What is get_dummies?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Comparing feature sets honestly

**Hook (5 min).** Did the new feature really help or was it luck?

**Concept (≤ 5 min).** Use cross-validation to compare feature sets and report the average and spread, not one lucky split. Avoid leakage.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compare four feature sets with 5-fold CV; pick one; explain.

**Check (5 min).**
1. Why 5-fold CV?
2. What is leakage in features?
3. Pick the simplest set that is…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Feature challenge

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
