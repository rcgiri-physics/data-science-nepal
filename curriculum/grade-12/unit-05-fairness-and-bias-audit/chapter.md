# Grade 12 · Unit 5: Fairness and a bias audit

> Track: B (code + discussion) · Tools: Python, scikit-learn · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** A model can be accurate overall and still work worse for some groups. An audit compares errors and selection rates across groups and asks who is harmed.

**What you will be able to do**

* I can identify where bias can enter a data-and-model pipeline.
* I can run a group audit: sizes, base rates, selection rates, accuracy, recall, precision and error rates, with
  uncertainty.
* I can respond to audit findings and write an honest audit memo.

**Words to know:** bias (पूर्वाग्रह), fairness (निष्पक्षता), protected or sensitive attribute, group, base rate, selection rate, false negative rate, demographic parity, equal opportunity, proxy, label bias, human in the loop, audit. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/fairness_audit.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Unit 3 (confusion matrix, recall, precision, thresholds), Grade 10 Units 5–6 (limits of models, AI bias), Grade 8
Unit 8 (who is missing, fairness is a decision). Setup — the visit-list model from Unit 3, with "home delivery" as the
positive class:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score

h = pd.read_csv("health_synthetic.csv")
h["home"] = 1 - h["institutional_delivery"]
train, test = train_test_split(h, test_size=0.4, random_state=2, stratify=h["home"])
cols = ["antenatal_visits", "wealth_quintile"]
model = LogisticRegression().fit(train[cols], train["home"])
test = test.assign(pred=(model.predict_proba(test[cols])[:, 1] >= 0.5).astype(int))
```

---

## Lesson 1: Where bias comes from

**Hook (5 min).** A model to predict which children need nutrition support is trained on records from city hospitals,
then used in a remote mountain district. What could go wrong? List three things before reading on.

### Explanation
"Bias" in machine learning means **systematic** differences in how well, or how fairly, a system works for different
groups. It can enter at every step:

| Stage | Source of bias | Example |
|---|---|---|
| **Who is in the data** | representation | few Mountain-belt records; a phone survey misses poor households |
| **How things are measured** | measurement | health-post records are complete in towns, patchy in remote areas |
| **What the label is** | label bias | "delivered in a facility" reflects past *access*, not just choice; "arrested" ≠ "committed a crime" |
| **Which features** | proxies | a postcode or surname can stand in for caste or ethnicity even if those columns are removed |
| **The model** | optimisation | maximising overall accuracy favours the largest group |
| **Deployment** | use and context | a model built for one district used in another; predictions used to *deny* help instead of to *offer* it |
| **Feedback loops** | self-reinforcement | areas flagged more get inspected more, find more, get flagged more |

**Removing a sensitive column is not enough.** If wealth, village or school are strongly linked to caste or ethnicity,
the model can learn the same pattern through these **proxies**. Fairness must be checked by measuring outcomes for
groups, which sometimes means keeping the sensitive attribute **for auditing** (with consent and protection), even
if it is not used for prediction.

**Who should check?** Not only the analyst. The people affected, the people who will use the predictions, and
someone independent. Fairness questions are about values, not just numbers.

### Activity (20 min)
1. In groups, read three cases: (a) a scholarship model trained on past winners (mostly from private schools); (b) a
   loan-scoring app that uses phone data (who has a smartphone?); (c) the health visit list in this unit.
2. For each case, mark the stages in the table where bias could enter, and who could be harmed.
3. For case (c): is `wealth_quintile` a fair feature for deciding who gets a *visit*? For deciding who gets a *loan*?
   Why might the answer differ?

### Common mistakes
* "The model can't be biased; we removed caste."
* Treating bias as only a technical bug.
* Auditing without involving the people affected.

**Check (5 min).**
1. Name two sources of bias.
2. Is bias only a coding problem?
3. Who should be involved in checking?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Audit by group

**Hook (5 min).** The model's overall recall is 74%: it finds about three in four women who will deliver at home. Is it
equally good for poor and better-off women? For the Mountain belt?

### Explanation
A **group audit** computes the same measures for each group and puts them side by side:

```python
def audit(g):
    return pd.Series({
        "n": len(g),
        "base_rate": g["home"].mean(),                  # share who actually delivered at home
        "selection_rate": g["pred"].mean(),             # share flagged for a visit
        "accuracy": (g["pred"] == g["home"]).mean(),
        "recall": recall_score(g["home"], g["pred"]),   # share of home deliveries found
        "precision": precision_score(g["home"], g["pred"]),
    })

print(test.groupby("ecological_belt").apply(audit).round(3))
print(test.groupby("wealth_quintile").apply(audit).round(3))
```

**By belt** (test set, 600 women):

| Belt | n | Base rate | Selection rate | Recall | Precision |
|---|---|---|---|---|---|
| Hill | 284 | 0.59 | 0.67 | 0.74 | 0.66 |
| Mountain | 59 | 0.63 | 0.75 | 0.76 | 0.64 |
| Terai | 257 | 0.51 | 0.65 | 0.73 | 0.57 |

Recall is similar across belts. But the Mountain group is small: a bootstrap interval for its recall runs from about
**0.61 to 0.89**, so we cannot say much about it.

**By wealth quintile:**

| Quintile | n | Base rate | Selection rate | Recall | Precision |
|---|---|---|---|---|---|
| 1 (poorest) | 130 | 0.62 | 0.85 | **0.89** | 0.65 |
| 2 | 99 | 0.70 | 0.76 | 0.77 | 0.71 |
| 3 | 126 | 0.58 | 0.69 | 0.73 | 0.61 |
| 4 | 134 | 0.49 | 0.54 | **0.59** | 0.53 |
| 5 (richest) | 111 | 0.43 | 0.51 | 0.69 | 0.59 |

The model **misses 41% of quintile-4 women** who deliver at home, but only 11% of quintile-1 women. Its decisions rest
mostly on antenatal visits, and better-off women tend to have more visits, so better-off women who will still deliver
at home are under-flagged. (Activity step 4 shows that removing `wealth_quintile` from the features changes nothing:
visits act as a **proxy** for wealth.) Whether that is acceptable depends on
the purpose: if visits aim at the *most disadvantaged*, perhaps; if visits aim at *everyone who will deliver at home*,
this is a gap to fix.

**Common fairness measures** (they answer different questions and usually cannot all be equal at once):
* **Demographic parity:** equal selection rates across groups.
* **Equal opportunity:** equal **recall** (equal chance of being found, among those who need it).
* **Predictive parity:** equal **precision** (a flag means the same thing in every group).
* **Equal error rates:** similar false negative and false positive rates.

When base rates differ between groups (they do here), a single model generally cannot satisfy all of these at once.
Choosing which matters most is a **values decision** for the people involved.

### Activity (20 min) — PRIMM
1. **Predict** which group will have the lowest recall; run both audits.
2. Bootstrap 95% intervals for recall in each belt (resample within the group).
3. **Investigate:** add the false negative rate (1 − recall) and the false positive rate to the audit.
4. **Make:** what happens to the recall gap across quintiles if you remove `wealth_quintile` from the features? Is the
   model then "fairer"? Better?

### Common mistakes
* Reporting group numbers without group sizes or uncertainty.
* Looking only at accuracy by group.
* Declaring a model "fair" because one measure is equal.

**Check (5 min).**
1. Why show group sizes?
2. Selection rate is…
3. What gap matters most?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Responding and reporting

**Hook (5 min).** Your audit shows the model misses 41% of home deliveries in one wealth group. Your manager says "fix
the code by tomorrow". What are your options — and is "fix the code" the right frame?

### Explanation
**Options after finding a gap** (often several together):
1. **Better data:** collect more records from under-represented groups; improve measurement in remote areas; add
   features that reflect need (distance to facility, previous home births) rather than proxies.
2. **Change the task or the label:** predict *risk of a complicated birth* instead of *past behaviour*, if that is what
   visits are for.
3. **Adjust decisions, openly:** different thresholds per group, or a rule like "everyone in quintile 4 with fewer than 4
   visits is also visited" — only with the agreement of the people affected and clear justification.
4. **Human in the loop:** health workers review the list and add women they know need a visit; the model ranks, people
   decide.
5. **Monitor after deployment:** repeat the audit every month; watch for drift and feedback loops.
6. **Do not deploy** if harms cannot be reduced, or if a simpler, transparent rule serves people better.

**The audit memo** (one page):
* **Purpose and decision** the model supports; who is affected.
* **Data:** source, period, synthetic or real, who is missing.
* **Overall performance** vs baseline.
* **Group findings:** table with sizes, base rates, selection rates, recall/precision, intervals.
* **Interpretation:** which gaps matter for this purpose, and why.
* **Limits:** small groups, synthetic data, attributes not available.
* **Recommendations** (2–4), with who must agree.
* **Contact** and date; plan for re-auditing.

Model cards (Unit 8, `capstone-kit/model-card-template.md`) package the same information for anyone who uses a model.

### Activity (20 min)
1. In groups, choose two responses for the quintile-4 gap and argue their benefits and risks.
2. Write the one-page audit memo for the visit-list model.
3. Present your top recommendation in one minute; the class votes on which recommendation they would accept as mothers,
   as health workers, as the district health office.

### Common mistakes
* Hiding the findings because they are uncomfortable.
* Only technical fixes, with no change in how the model is used.
* "Fair" thresholds chosen by the analyst alone.

**Check (5 min).**
1. Can you always 'fix' bias with a tweak?
2. Why keep humans in the loop?
3. What must the memo include?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Bias can enter through representation, measurement, labels, proxies, optimisation, deployment and feedback loops.
* Removing a sensitive column does not remove bias; audit outcomes by group (with consent and protection).
* A group audit shows n, base rate, selection rate, accuracy, recall, precision and error rates — with intervals.
* Fairness measures (demographic parity, equal opportunity, predictive parity) conflict when base rates differ; choose
  with the people affected.
* Responses: better data, better task/label, open decision rules, human review, monitoring, or not deploying. Report in
  an audit memo.

## Practice exercises
1. ★ Define selection rate and recall for a group, in words.
2. ★ Give an example of a proxy for a sensitive attribute in Nepal.
3. ★ Why does a small group give an unreliable recall?
4. ★★ Group A: 100 women, 60 home deliveries, model finds 54. Group B: 20 women, 12 home deliveries, model finds 6.
   Compute recall for each. What would you say about the gap?
5. ★★ Add `ecological_belt` dummies to the model. Rerun the audit by belt and by quintile. What changes?
6. ★★ Lower the threshold for quintiles 4–5 only (e.g. 0.4) and recompute recall and the total number flagged. Who must
   agree before doing this?
7. ★★ Compute the false positive rate by quintile. Who gets the most unnecessary visits? Is that a harm?
8. ★★★ Explain why equal selection rates (demographic parity) and equal recall cannot both hold here. Use the base
   rates.
9. ★★★ A school uses a dropout-risk model and then gives extra attention to flagged students, who then stay. Next year
   the model is retrained on the new data. Describe the feedback loop and its risks.
10. ★★★ Write the "who is missing" paragraph of the audit memo for a model trained on the synthetic health table if it
    were real data from facility records.

## Exercises with real data
**R1. Penguins by island (RD-17).** Train a species classifier, then audit accuracy by island and by sex. Are some
groups much smaller? Do errors concentrate anywhere? (A harmless dataset to practise the audit mechanics.)
*Offline fallback:* the health table, as in the lessons.

**R2. Who is in the data? (RD-13 vs synthetic).** Compare the belt and (if available) wealth distribution of the
synthetic table with census or survey figures for Nepal. Which groups would a model trained on it under-serve?

**R3. A published audit (RD-20).** Read a summary of a well-known AI audit (e.g. "Gender Shades", facial analysis, 2018;
or ProPublica's 2016 analysis of a criminal-risk tool and the debate that followed). Summarise: groups compared, measures
used, findings, and the disagreement about which fairness measure matters.

## Unit project: Audit memo
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Audit one classification model by at least two
group variables (with sizes and bootstrap intervals), test one response (feature change, threshold change or human
rule) and its trade-offs, and write the one-page audit memo with recommendations and who must agree. Full brief and
rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Solon Barocas, Moritz Hardt and Arvind Narayanan, *Fairness and Machine Learning* (free online book,
  <https://fairmlbook.org>).
* Cathy O'Neil, *Weapons of Math Destruction* (2016).
* Joy Buolamwini, *Unmasking AI* (2023), and the "Gender Shades" project.
