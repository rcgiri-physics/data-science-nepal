# Grade 12 · Unit 1: The machine-learning workflow

> Track: B (code) · Tools: Python, scikit-learn · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `health-synthetic`

**Big idea.** A trustworthy model follows a workflow: define the task, split the data, set a baseline, train, validate, and test once at the end.

**What you will be able to do**

* I can split data into train, validation and test sets.
* I can set and beat a baseline.
* I can explain data leakage.

**Words to know:** feature, label, train/test split, validation, baseline, data leakage (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/ml_workflow.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Define the task

**Hook (5 min).** Predict what, for whom, to do what?

**Concept (≤ 5 min).** Name the label, the features, the people affected and the decision. If you can't say how the prediction will be used, you can't judge the model.

**Activity (20 min).** Fill a task card: label, features, who is affected, how a prediction will be used.

**Check (5 min).**
1. What is the label?
2. What are features?
3. Why describe the decision?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Split and baseline

**Hook (5 min).** Why hide some data from the model?

**Concept (≤ 5 min).** Train on one part, tune on validation, and report once on test. A baseline (majority class) tells us what 'no skill' scores.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Make the 60/20/20 split; compute the baseline accuracy.

**Check (5 min).**
1. Which set do we use to choose between models?
2. Which set do we use only once?
3. Accuracy of always predicting the majority class is…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Train, compare, test

**Hook (5 min).** Is 78% good?

**Concept (≤ 5 min).** Compare to the baseline on validation data, then test once. Use pipelines so scaling is learned from training data only (avoids leakage).

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Train logistic regression with a pipeline; report validation and test results.

**Check (5 min).**
1. What is data leakage?
2. Why use a pipeline?
3. What if the model barely beats baseline?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Workflow report

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
