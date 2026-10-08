# Grade 12 · Unit 2: Regression and classification

> Track: B (code) · Tools: Python, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** Regression predicts a number; classification predicts a category. Simple models are often the most explainable.

**What you will be able to do**

* I can fit linear and logistic regression.
* I can interpret coefficients and predicted probabilities.
* I can choose regression vs classification.

**Words to know:** regression, classification, probability, coefficient, decision threshold (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/reg_class.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Regression: predicting a number

**Hook (5 min).** Predict a baby's birth weight from mother's wealth and visits.

**Concept (≤ 5 min).** Linear regression predicts a number; coefficients say how the prediction changes per unit of a feature, holding others fixed.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit with scikit-learn; check it equals the least-squares solution from Grade 11.

**Check (5 min).**
1. Regression predicts…
2. Coefficient 0.05 for visits means…
3. Same as Grade 11 least squares?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Classification: predicting a category

**Hook (5 min).** Will this mother deliver in a facility?

**Concept (≤ 5 min).** Logistic regression outputs a probability between 0 and 1; a threshold turns it into a class. The threshold is a human decision.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit logistic regression; get probabilities for two example mothers; change the threshold.

**Check (5 min).**
1. Probability range?
2. What turns a probability into a class?
3. Who chooses the threshold?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Choosing and explaining

**Hook (5 min).** Regression or classification? Simple or complex?

**Concept (≤ 5 min).** Match the method to the question and the audience. A simple, explainable model that is nearly as good is often the better choice in public services.

**Activity (20 min).** For four scenarios choose method and justify; write a plain-language explanation.

**Check (5 min).**
1. Predict rainfall in mm: type?
2. Predict 'pass/fail': type?
3. Why favour explainable models?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Explain a prediction

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
