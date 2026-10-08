# Grade 11 · Unit 5: Regression with interpretation

> Track: B (code) · Tools: Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** Regression estimates how an outcome changes with one or more variables, holding the others fixed — and must be read with care.

**What you will be able to do**

* I can fit a multiple linear regression.
* I can interpret coefficients in words.
* I can check residuals and R² sensibly.

**Words to know:** regression, coefficient, R², residual, predictor (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/regression.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Simple regression revisited

**Hook (5 min).** In Grade 10 we drew a line. What did the slope mean?

**Concept (≤ 5 min).** y ≈ a + b x. The slope b is the average change in y per unit x. Least squares picks a, b minimising squared residuals.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit birth weight on visits; interpret the slope in words.

**Check (5 min).**
1. Slope 0.04 kg per visit means…
2. What does the intercept mean?
3. What is minimised?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Multiple regression

**Hook (5 min).** Does wealth matter after accounting for visits?

**Concept (≤ 5 min).** Including several predictors lets us interpret each coefficient 'holding others fixed'. Predictors that move together can blur which one matters.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit with wealth and visits; compare coefficients with the single-predictor fits.

**Check (5 min).**
1. 'Holding visits fixed' means…
2. Why might a coefficient shrink when adding a predictor?
3. Does a coefficient show cause?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Checking the model

**Hook (5 min).** R² = 0.4. Good?

**Concept (≤ 5 min).** R² is the share of variation explained; judge by residual plots, purpose and limits. Patterns in residuals mean the model misses something.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Plot residuals; look for patterns; compute R²; add a predictor and compare.

**Check (5 min).**
1. What does R² = 0.4 mean?
2. What pattern in residuals is a warning?
3. Is high R² always good?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Explain it, don't just fit it

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
