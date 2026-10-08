# Grade 12 · Unit 4: Overfitting and generalising

> Track: B (code) · Tools: Python, numpy · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: none

**Big idea.** A model that memorises its training data fails on new data. Complexity must be matched to how much data and noise we have.

**What you will be able to do**

* I can recognise overfitting from train vs test error.
* I can choose model complexity using validation data.
* I can explain why simple models can generalise better.

**Words to know:** overfitting, underfitting, complexity, generalise, validation error (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/overfitting.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Underfitting and overfitting

**Hook (5 min).** A student memorises last year's exam answers. Will they do well on this year's?

**Concept (≤ 5 min).** Underfit models are too simple; overfit models chase noise. Training error always falls with complexity; test error falls then rises.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit polynomials of increasing degree; tabulate train and test error.

**Check (5 min).**
1. Training error with more complexity…
2. Test error with too much complexity…
3. What is noise?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Choosing complexity with validation

**Hook (5 min).** How do we pick the degree without peeking at the test set?

**Concept (≤ 5 min).** Use validation data (or cross-validation) to choose; touch the test set once.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Split train into train/validation; choose the degree with the lowest validation error.

**Check (5 min).**
1. Which data choose complexity?
2. Why not test data?
3. What is cross-validation?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Simple can win

**Hook (5 min).** Is a simple, explainable model a failure?

**Concept (≤ 5 min).** With limited data a simple model often generalises as well or better, is easier to check and explain, and is safer for public decisions.

**Activity (20 min).** Compare a degree-3 and degree-12 fit; write a recommendation for a public office.

**Check (5 min).**
1. When do simple models shine?
2. Why prefer explainable models in public service?
3. Is overfitting only a polynomial problem?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Find the sweet spot

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
