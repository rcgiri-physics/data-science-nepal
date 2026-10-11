# Grade 10 · Unit 5: What is a model? (and a first look at machine learning)

> Track: A then B · Tools: paper cards, Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** A model is a simplified rule that predicts. We build one by finding patterns in examples and test it on examples it has not seen.

**What you will be able to do**

* I can explain what a model is, and the difference between training and test data.
* I can compare a model with a baseline using accuracy on unseen data.
* I can run k-nearest neighbours and explain what *k* does.
* I can say when a model should not be used, and who should decide.

**Words to know:** model, feature, label (target), training data, test data, prediction, accuracy, baseline, classification, k-nearest neighbours (k-NN), overfitting. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/knn_intro.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Unit 3's line of best fit was already a model: a rule that predicts PM10 from PM2.5. Now we predict a **category**
(yes/no). The table `health_synthetic.csv` has 1,500 **invented** mother–child records (real health survey data such as
DHS cannot be redistributed). Columns: `record_id, ecological_belt, mother_age, wealth_quintile` (1 poorest … 5
richest), `antenatal_visits` (check-ups during pregnancy), `institutional_delivery` (1 = baby born in a health
facility, 0 = not), `birth_weight_kg`. The relationships were **built into** the generator, so findings say nothing
about real women in Nepal.

---

## Lesson 1: Unplugged: models from cards

**Hook (5 min).** Your teacher shows 20 cards from past cases — each with two numbers and a label ✔ or ✘ — and then a
new card with no label. How would you guess its label? Write your rule before you see anyone else's.

### Explanation
A **model** is a rule that turns inputs into a prediction. You use models all the time: "dark clouds in the west →
it will rain"; "this student usually scores well → she will pass". A data model is the same idea, made from data:

* **Features** (inputs): what we know about a case — number of antenatal visits, wealth quintile.
* **Label** (target): what we want to predict — institutional delivery, yes or no.
* **Training data**: past cases with known labels, used to *build* the rule.
* **Test data**: other cases with known labels, kept **hidden** while building, used only to *check* the rule.

Predicting a category (yes/no, which species, which belt) is **classification**. Predicting a number (PM10, price) is
**regression** (Unit 3's line).

**Why hide the test data?** A rule can be made to fit the training cards perfectly ("card 7 is ✔, card 8 is ✘…") and
still be useless for new cards. Only cases the model has never seen tell us how it will do in real life. This is the
single most important idea in machine learning.

**Nearest neighbours.** A natural rule: find the training cards **most similar** to the new card and copy their labels.
To decide which cards are "nearest", place cards on a grid (visits across, wealth up) and measure the straight-line
distance:

> distance between (*x*₁, *y*₁) and (*x*₂, *y*₂) = √((*x*₁ − *x*₂)² + (*y*₁ − *y*₂)²)

This is Pythagoras' theorem from Maths. With the **3 nearest** cards voting, the majority label wins.

### Activity (20 min)
1. In groups, take 30 training cards (visits, wealth, label ✔/✘) and place them on a large grid drawn on paper.
2. Each group gets 8 test cards (labels folded under). For each, find the 3 nearest training cards (measure with a
   ruler if close) and predict by majority vote.
3. Unfold the labels. How many of 8 were correct? Write it as a percent (**accuracy**).
4. Try the "always ✘" rule on the same 8 cards. Did your model beat it?

### Common mistakes
* Peeking at test labels before predicting (that is cheating — and in real projects it happens by accident!).
* Forgetting that both features need to be on similar scales for distance to be fair (visits 0–8 and wealth 1–5 are
  similar enough here; age 16–42 would dominate).

**Check (5 min).**
1. What is training data?
2. Why keep test data hidden?
3. Which cards are 'nearest'?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Code: k-NN and a baseline

**Hook (5 min).** A model gets 70% of predictions right. Is that good? What if 70% of the cases were "no", so that
answering "no" every time also gets 70%?

### Explanation
**Accuracy** = correct predictions ÷ all predictions, measured on the **test** data. It means nothing on its own: we
compare with a **baseline**, the simplest sensible rule. For classification the usual baseline is "always predict the
most common label" (the **majority class**).

```python
import pandas as pd
import numpy as np

h = pd.read_csv("health_synthetic.csv")
X = h[["antenatal_visits", "wealth_quintile"]].to_numpy(dtype=float)   # features
y = h["institutional_delivery"].to_numpy()                            # label
train, test = slice(0, 1200), slice(1200, 1500)                       # first 1,200 rows train, last 300 test

majority = int(round(y[train].mean()))           # 0.44 of training cases are 1 → majority is 0
baseline_acc = (y[test] == majority).mean()
print("baseline accuracy:", round(baseline_acc, 3))     # 0.563
```

A model must beat **56.3%** to be worth anything.

**Model 1: a one-line rule.** "Predict 1 if the mother had 4 or more antenatal visits." We chose the threshold 4 by
trying 1–6 on the **training** data only (4 was best there).

```python
rule_pred = (X[test][:, 0] >= 4).astype(int)
print("rule accuracy:", round((rule_pred == y[test]).mean(), 3))   # 0.66
```

**Model 2: k-nearest neighbours** in code — exactly the card game:

```python
def knn_predict(x, k=5):
    d = np.sqrt(((X[train] - x) ** 2).sum(axis=1))        # distance to every training case
    nearest = np.argsort(d, kind="stable")[:k]            # positions of the k smallest distances
    return int(round(y[train][nearest].mean()))           # majority vote (mean of 0/1 labels, rounded)

for k in (1, 5, 15, 25):
    preds = np.array([knn_predict(x, k) for x in X[test]])
    print("k =", k, "test accuracy", round((preds == y[test]).mean(), 3))
```

Synthetic results: k = 1: 0.567 · k = 5: 0.547 · k = 15: 0.640 · k = 25: 0.647.

**What *k* does.**
* **Small *k*** (1, 5): the prediction follows a few nearby cases, including their noise and accidents. It can fit
  the training data closely but generalise badly — **overfitting**.
* **Large *k***: predictions are smoother and steadier, but if *k* is too large (say 1,000) every case gets the
  overall majority — **underfitting**, back to the baseline.
* Choose *k* using data the test set has not touched (Grade 12 uses a "validation set" or cross-validation for this).

**Read the results honestly.** The best k-NN (≈ 65%) beats the baseline (56%) by about 8–9 percentage points — but a
one-line rule (66%) does just as well. Complex is not automatically better. And with only 300 test cases, differences
of 1–2 points could be luck.

### Activity (20 min) — PRIMM
1. **Predict** the baseline accuracy from the share of 1s; run the baseline cell.
2. Run the one-line rule. Try thresholds 3 and 5 on the **training** rows and choose the best before looking at test
   accuracy.
3. Run k-NN for k = 1, 5, 15, 25. **Investigate:** compute training accuracy too (predict the training rows). Where
   is the gap between training and test accuracy largest?
4. **Make:** add `mother_age` as a third feature. Does accuracy improve? (Watch the scale problem: age ranges over 26
   years, visits over 8.)

### Common mistakes
* Reporting training accuracy as if it were test accuracy.
* Choosing *k* or a threshold by looking at **test** accuracy (the test set is then no longer "unseen").
* Forgetting to compare with a baseline.

**Check (5 min).**
1. What is a baseline?
2. Why test on unseen data?
3. k = 1 problem?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Limits and misuse

**Hook (5 min).** A district health office wants to use the model to decide which pregnant women get a follow-up visit
from a health worker. The model says "this woman will probably deliver at home". What could go wrong?

### Explanation
A model learns **patterns from the past**. That is its power and its danger:
* **It copies the past, including unfairness.** If poorer women in the past had less access to facilities, a model
  learns "poor → home delivery" — fine for *predicting*, harmful if used to *decide* who deserves help or resources in
  a way that repeats the disadvantage.
* **It is only as good as its data.** If Mountain-belt women are few in the training data (157 of 1,500 here), the
  model will be less reliable for them.
* **It makes mistakes, and mistakes have costs.** Predicting "facility delivery" for a woman who then delivers at home
  without support could cost a life; the opposite mistake wastes a visit. These costs are not equal (Grade 12 Unit 3
  measures them separately).
* **It describes correlation, not cause.** The model "knows" that visits and facility delivery go together, not that
  visits *cause* it.
* **It can drift.** When a new road or birthing centre opens, the past no longer predicts the future.

**Five questions before using a model on people** (extending Grade 8 Unit 8):
1. **What exactly does it predict**, and how was "correct" measured?
2. **Who is in the training data, and who is missing or few?**
3. **How accurate is it on unseen data — and for each group?**
4. **What happens when it is wrong, and to whom?** Which mistakes are worse?
5. **Who decides, and can people question or appeal?** A model should support, not replace, accountable human
   judgement in high-stakes decisions.

A good use here might be: "use predictions to *add* women to a follow-up list (never remove anyone), and check monthly
that every belt is served". A bad use: "skip visits to women the model says will deliver in a facility anyway".

### Activity (20 min)
1. In groups, discuss three scenarios with the five questions: (a) the follow-up visit list; (b) a school using a
   model on attendance and marks to decide which students may sit the SEE; (c) a bank using a model to approve
   loans for small farmers.
2. For each, write: one sensible use, one misuse, and who should make the final decision.
3. Using the notebook, compute k-NN test accuracy separately for each `ecological_belt`. Is the model equally good
   for everyone?

### Common mistakes
* "The computer decided, so it is objective."
* Judging a model only by overall accuracy, not by who bears its mistakes.
* Forgetting that synthetic-data results say nothing about real people.

**Check (5 min).**
1. Can a model be unfair?
2. Name a high-stakes use needing caution.
3. Who should decide?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* A model is a rule from inputs (**features**) to a prediction (**label**); classification predicts categories,
  regression numbers.
* Build on **training** data, judge on hidden **test** data; never tune on the test set.
* Accuracy means nothing without a **baseline** (majority class).
* k-NN: find the *k* nearest training cases and vote; small *k* overfits, large *k* underfits; features need similar
  scales.
* Simple rules can match complex models.
* Models copy the past; ask the five questions; humans stay accountable.

## Practice exercises
1. ★ In each problem name the features and the label: (a) predicting whether it rains tomorrow from today's humidity
   and pressure; (b) predicting a house's price from area and location; which is classification, which regression?
2. ★ A test set has 200 cases: 150 "no", 50 "yes". What is the baseline accuracy? A model gets 160 right. How much
   better than the baseline is it?
3. ★ Compute the distance between (3, 2) and (6, 6).
4. ★★ For the training points A (1, 1, ✘), B (2, 1, ✘), C (4, 4, ✔), D (5, 4, ✔), E (3, 3, ✔), predict the label of
   (2, 2) with k = 1 and k = 3.
5. ★★ Why would including `record_id` as a feature be a bad idea?
6. ★★ A student tunes *k* by trying 1 to 50 and picking the best **test** accuracy (0.66 at k = 31). Why is 0.66 too
   optimistic? What should they have done?
7. ★★ Compute the baseline and the "visits ≥ 4" rule's accuracy for the training rows. Is the rule better on the
   training or the test rows? Is that surprising?
8. ★★★ Add `mother_age ÷ 5` instead of `mother_age` as a feature (so its range is similar to the others). Compare
   test accuracy with the unscaled version. Explain.
9. ★★★ Describe a situation where a model with **lower** accuracy is better to use than one with higher accuracy.
10. ★★★ Write `accuracy_by_group(preds, y, groups)` that returns accuracy for each group. Use it on the k = 15 model and
    `ecological_belt`.

## Exercises with real data
**R1. Penguins (RD-17).** Load Palmer penguins (CC0). Remove rows with missing values. Use `bill_length_mm` and
`flipper_length_mm` to classify species with your k-NN function (shuffle first with `df.sample(frac=1,
random_state=0)`, then train on 250 rows, test on the rest). Compare with the majority baseline. Which *k* works best
on a validation split you made from the training rows?
*Offline fallback:* the health table, as in the lessons.

**R2. Weather tomorrow (RD-06).** Download a year of daily data for your town (temperature, rain). Make a label "rain
tomorrow" (`(df["rain"].shift(-1) > 1).astype(int)`) and features "rain today" and "temperature today". Train on
January–September, test on October–December. Does a model beat "it will be like today" (a persistence baseline)?

**R3. Who is in the data? (RD-13).** Using census results, compare the share of Nepal's population in each ecological
belt with the share of records in `health_synthetic.csv` (Mountain 157, Hill 696, Terai 647). Which belt is over- or
under-represented? How could that affect a model trained on it?

## Unit project: Model vs baseline
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Build and compare three classifiers on the
health table (or penguins): the majority baseline, a one-line rule chosen on training data, and k-NN with *k* chosen
without using the test set. Report test accuracy for each, accuracy by belt, and a one-page "should this be used?"
memo using the five questions. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Google's "Teachable Machine" (<https://teachablemachine.withgoogle.com>): train an image model in the browser and
  see training vs testing in action.
* Elements of AI (<https://www.elementsofai.com>, free online course, University of Helsinki).
* Kaggle Learn "Intro to Machine Learning" (free).
