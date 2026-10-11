# Grade 12 · Unit 3: Evaluation metrics: who is missed, who is wrongly flagged

> Track: B (code) · Tools: Python, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** Accuracy hides the kind of mistakes a model makes. Precision, recall and the confusion matrix show who is missed or wrongly flagged.

**What you will be able to do**

* I can build and read a confusion matrix.
* I can compute accuracy, precision, recall and F1 by hand and with scikit-learn, and explain when accuracy misleads.
* I can choose a threshold from the costs of errors and the capacity to act, and justify it.

**Words to know:** positive class, true positive (TP), false positive (FP), false negative (FN), true negative (TN), confusion matrix, precision, recall (sensitivity), specificity, F1 score, class imbalance, threshold, precision–recall trade-off. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/metrics.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Unit 2 (logistic regression, probabilities, thresholds). In this unit the **positive class** — the thing we want to
find — is **home delivery**: those are the women a health worker should visit. Setup:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

h = pd.read_csv("health_synthetic.csv")
h["home"] = 1 - h["institutional_delivery"]          # 1 = delivered at home (positive class)
train, test = train_test_split(h, test_size=0.25, random_state=0)
cols = ["antenatal_visits", "wealth_quintile"]
model = LogisticRegression().fit(train[cols], train["home"])
p_home = model.predict_proba(test[cols])[:, 1]        # probability of home delivery
y = test["home"].to_numpy()                           # 202 of 375 test women delivered at home
```

---

## Lesson 1: The confusion matrix

**Hook (5 min).** A model flags 270 women for a home visit. A newspaper asks: "How many of them really needed it? And how
many women who needed a visit did the model miss?" Can accuracy answer either question?

### Explanation
Every prediction of a yes/no model falls into one of four boxes:

| | **Predicted positive** (flagged: "home") | **Predicted negative** (not flagged) |
|---|---|---|
| **Actually positive** (delivered at home) | **TP** true positive — found ✔ | **FN** false negative — **missed** ✘ |
| **Actually negative** (delivered in facility) | **FP** false positive — false alarm ✘ | **TN** true negative — correctly left ✔ |

This 2 × 2 table is the **confusion matrix**. All four boxes add up to the number of cases.

```python
from sklearn.metrics import confusion_matrix

pred = (p_home >= 0.5).astype(int)                     # threshold 0.5
tn, fp, fn, tp = confusion_matrix(y, pred).ravel()
print(dict(TP=tp, FP=fp, FN=fn, TN=tn))               # {'TP': 157, 'FP': 113, 'FN': 45, 'TN': 60}
```

Reading it: the model flagged 157 + 113 = 270 women. **157** really delivered at home (found); **113** were false alarms.
It **missed 45** women who delivered at home. It correctly left out 60.

`confusion_matrix(y_true, y_pred)` puts actual classes in rows and predicted in columns, ordered 0 then 1, so `.ravel()`
gives TN, FP, FN, TP — a frequent source of confusion; check with a tiny example.

**Different mistakes, different harms.** Here a false negative (a woman who delivers at home without a visit) can be
dangerous; a false positive costs a health worker's time. In other settings the balance is different: a false positive
in a fraud model can block an innocent person's account; a false negative in a cancer screening misses a disease.

### Activity (20 min) — PRIMM
1. **Unplugged:** your teacher gives 40 cards with an actual label and a predicted label. Sort them into the four boxes
   and count.
2. **Predict** the four numbers for threshold 0.5, then run the code.
3. **Investigate:** check by hand that TP + FN = 202 (all home deliveries) and TP + FP = 270 (all flagged).
4. **Make:** the confusion matrix at threshold 0.6.

### Common mistakes
* Mixing up which class is "positive".
* Reading rows as predictions and columns as actual (check the library's convention).
* Talking about "errors" without saying which kind.

**Check (5 min).**
1. False negative means…
2. False positive means…
3. Rows+columns sum to…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Precision, recall, F1

**Hook (5 min).** A model for a rare disease has 98% accuracy — and finds none of the sick children. How is that
possible?

### Explanation
From the four boxes:

| Measure | Formula | Question it answers | At threshold 0.5 |
|---|---|---|---|
| **Accuracy** | (TP + TN) ÷ all | What share of all predictions were right? | (157 + 60) ÷ 375 = 0.579 |
| **Precision** | TP ÷ (TP + FP) | Of those we **flagged**, how many were right? | 157 ÷ 270 = 0.581 |
| **Recall** (sensitivity) | TP ÷ (TP + FN) | Of the real positives, how many did we **find**? | 157 ÷ 202 = 0.777 |
| **Specificity** | TN ÷ (TN + FP) | Of the real negatives, how many did we leave alone? | 60 ÷ 173 = 0.347 |
| **F1** | 2 × P × R ÷ (P + R) | One number balancing precision and recall | 0.665 |

```python
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

print("accuracy ", round(accuracy_score(y, pred), 3))
print("precision", round(precision_score(y, pred), 3))
print("recall   ", round(recall_score(y, pred), 3))
print("F1       ", round(f1_score(y, pred), 3))
```

**Why accuracy misleads: class imbalance.** When one class is rare, "always predict the common class" scores high
accuracy and finds nobody. Example with low birth weight (under 2.5 kg, about 17.5% of babies):

```python
low = (h["birth_weight_kg"] < 2.5).astype(int)
always_no = np.zeros(len(low), dtype=int)
print("accuracy", round(accuracy_score(low, always_no), 3), "| recall", recall_score(low, always_no, zero_division=0))
# accuracy 0.825 | recall 0.0
```

82.5% accurate — and every low-birth-weight baby missed. For rare but important events (disease, fraud, floods,
dropping out of school) report **recall and precision**, not just accuracy.

**F1** is the harmonic mean of precision and recall: it is high only when **both** are high. It is a convenient summary
for comparing models, but it hides the trade-off; decisions should look at precision and recall separately.

### Activity (20 min) — PRIMM
1. Compute all five measures by hand from your Lesson 1 matrix; check with scikit-learn.
2. Run the low-birth-weight example. Then fit a logistic regression for `low` on visits and wealth and report recall at
   threshold 0.5. What happens? (Hint: almost no predicted probability exceeds 0.5.)
3. **Make:** invent a 100-case confusion matrix with accuracy above 90% and recall below 20%.

### Common mistakes
* Reporting accuracy for imbalanced problems.
* Confusing precision ("of flagged") with recall ("of real").
* Treating F1 as the decision instead of a summary.

**Check (5 min).**
1. Precision formula?
2. Recall formula?
3. Why can accuracy mislead?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Choosing a threshold

**Hook (5 min).** The health post can make about **120 visits** this month. Missing a woman who will deliver at home is
worse than visiting a woman who would have gone to a facility anyway. What threshold should the model use?

### Explanation
Moving the threshold trades precision against recall:

```python
rows = []
for t in (0.4, 0.5, 0.6, 0.7):
    pr = (p_home >= t).astype(int)
    rows.append(dict(threshold=t, flagged=int(pr.sum()),
                     precision=round(precision_score(y, pr), 3), recall=round(recall_score(y, pr), 3)))
print(pd.DataFrame(rows))
```

| Threshold | Flagged | Precision | Recall |
|---|---|---|---|
| 0.4 | 343 | 0.557 | 0.946 |
| 0.5 | 270 | 0.581 | 0.777 |
| 0.6 | 151 | 0.609 | 0.455 |
| 0.7 | 34 | 0.765 | 0.129 |

* **Lower threshold** → more women flagged → **recall up** (fewer missed), **precision down** (more false alarms).
* **Higher threshold** → fewer flagged → precision up, recall down.

**Choosing.** Three considerations:
1. **Costs of each error**, decided with the people affected (health workers, mothers, managers) — not by the analyst
   alone.
2. **Capacity:** with 120 visits, flagging 270 is not possible. Rank women by `p_home` and visit the top 120:

```python
order = np.argsort(-p_home)                       # highest probability first
top = order[:120]
print("precision", round(y[top].mean(), 3), "| recall", round(y[top].sum() / y.sum(), 3))
# precision 0.617 | recall 0.366
```

   With capacity for 120, about 62% of visits reach women who would deliver at home, and 37% of all such women are
   reached. The analyst's honest message: "the model helps prioritise, but capacity, not the model, is the main limit —
   and 63% of home deliveries will not get a visit."
3. **Fairness across groups** (Unit 5): one threshold can give very different recall in different belts.

**Curves** show all thresholds at once: plot precision and recall against the threshold, or precision against recall
(the precision–recall curve). scikit-learn's `precision_recall_curve` computes the points. The **ROC curve** (true
positive rate vs false positive rate) and its area (**AUC**) are also common; for rare positives the precision–recall
view is usually more informative.

### Activity (20 min) — PRIMM
1. **Predict** how precision and recall change as the threshold falls; run the table.
2. Plot precision and recall against thresholds from 0.3 to 0.75 (step 0.01) on one chart.
3. Compute precision and recall for visiting the top 60, 120 and 240 women.
4. **Make:** write a half-page recommendation to the health post: threshold or top-*k* rule, expected found/missed
   numbers, and who should agree to it.

### Common mistakes
* Using 0.5 because it is the default.
* Choosing a threshold the organisation cannot act on.
* Optimising one number without asking the people affected.

**Check (5 min).**
1. Lower threshold → recall?
2. Who decides the costs?
3. What capacity limit matters?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Define the positive class; the confusion matrix counts TP, FP, FN, TN.
* Accuracy = right ÷ all; precision = TP ÷ flagged; recall = TP ÷ real positives; specificity = TN ÷ real negatives;
  F1 balances precision and recall.
* With imbalanced classes, accuracy can be high while recall is zero.
* Thresholds trade recall against precision; choose with the costs of errors, capacity to act and fairness, together
  with the people affected. A top-*k* rule matches fixed capacity.

## Practice exercises
1. ★ TP = 40, FP = 10, FN = 20, TN = 130. Compute accuracy, precision, recall, specificity and F1.
2. ★ In a flood-warning system, what are a false positive and a false negative? Which is worse?
3. ★ Why is recall also called sensitivity in medicine?
4. ★★ A school's dropout model flags 50 students; 20 actually drop out; overall 30 students drop out. Precision? Recall?
5. ★★ Use `precision_recall_curve` to find the lowest threshold with precision ≥ 0.6. What recall does it give?
6. ★★ Show with numbers why "always predict facility delivery" has recall 0 for home deliveries, and compute its
   accuracy on the test set.
7. ★★ Compute recall at threshold 0.5 separately for Hill, Mountain and Terai women. Any concern?
8. ★★★ The health post can visit 120 women. A second model has the same overall accuracy but higher precision in the
   top 120. Which should they use, and why does accuracy not decide this?
9. ★★★ Design a confusion-matrix "cost table" (e.g. FN costs 10 points, FP costs 1) and find the threshold with the
   lowest total cost. How sensitive is the choice to the cost ratio?
10. ★★★ Explain to a non-expert why a COVID test with 99% specificity can still give many false positives when the
    disease is rare (base-rate effect). Use 10,000 people and a 1% infection rate.

## Exercises with real data
**R1. Penguins as a yes/no (RD-17).** Make the task "Is it a Chinstrap?" (the rarest species). Fit logistic regression;
show accuracy, precision and recall at 0.5; then choose a threshold for recall ≥ 0.9 and report the precision.
*Offline fallback:* the health table.

**R2. Big earthquakes (RD-05).** Using a year of USGS data with depth, magnitude and location, define "magnitude ≥ 5"
as the positive class and a naive rule (e.g. depth < 15 km). Compute the confusion matrix. Why is accuracy a poor
measure here?

**R3. Rain warnings (RD-06).** For your "rain tomorrow" model, choose thresholds for two users: a farmer drying grain
(missing rain is costly) and a school deciding to cancel sports day (false alarms are costly). Report precision and
recall for each.

## Unit project: Choose the threshold
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. For one classification task, produce the
confusion matrix at several thresholds, precision/recall/F1 table and curve, a capacity-based (top-*k*) analysis, a
cost-table analysis, and a one-page recommendation saying who should agree to the chosen threshold. Full brief and
rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* scikit-learn user guide, "Metrics and scoring" (<https://scikit-learn.org/stable/modules/model_evaluation.html>).
* Gerd Gigerenzer, *Risk Savvy* (2014): reading test results, false positives and base rates in plain language.
* Google Machine Learning Crash Course (free): "Classification: accuracy, precision, recall".
