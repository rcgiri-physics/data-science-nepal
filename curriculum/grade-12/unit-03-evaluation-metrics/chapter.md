# Grade 12 · Unit 3: Evaluation metrics

> Track: B (code) · Tools: Python, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** Accuracy hides the kind of mistakes a model makes. Precision, recall and the confusion matrix show who is missed or wrongly flagged.

**What you will be able to do**

* I can read a confusion matrix.
* I can compute precision, recall and F1.
* I can choose a threshold based on the cost of errors.

**Words to know:** confusion matrix, precision, recall, F1, false positive, false negative (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/metrics.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: The confusion matrix

**Hook (5 min).** A model flags 100 mothers for follow-up. How many were truly in need?

**Concept (≤ 5 min).** True/false positives and negatives count right and wrong calls. Different mistakes hurt different people.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Build the 2×2 table by hand from 40 cases; then from the notebook.

**Check (5 min).**
1. False negative means…
2. False positive means…
3. Rows+columns sum to…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Precision, recall, F1

**Hook (5 min).** Accuracy is 90% yet every sick child is missed. How?

**Concept (≤ 5 min).** Precision = TP ÷ (TP+FP): of those flagged, how many were right. Recall = TP ÷ (TP+FN): of the true cases, how many were found. F1 balances both.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute them by hand and with the library; construct a case where accuracy is high but recall is 0.

**Check (5 min).**
1. Precision formula?
2. Recall formula?
3. Why can accuracy mislead?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Choosing a threshold

**Hook (5 min).** Missing a case or a false alarm — which is worse?

**Concept (≤ 5 min).** Lower thresholds raise recall and lower precision; choose by the cost of each error and the capacity to act.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Plot precision and recall for several thresholds; justify a choice for a given scenario.

**Check (5 min).**
1. Lower threshold → recall?
2. Who decides the costs?
3. What capacity limit matters?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Choose the threshold

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
