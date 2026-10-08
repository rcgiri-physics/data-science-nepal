# Grade 12 · Unit 5: Fairness and bias audit

> Track: B (code + discussion) · Tools: Python, scikit-learn · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `health-synthetic`

**Big idea.** A model can be accurate overall and still work worse for some groups. An audit compares errors and selection rates across groups and asks who is harmed.

**What you will be able to do**

* I can compare metrics across groups.
* I can explain sources of bias.
* I can write a short audit with recommendations.

**Words to know:** bias, fairness, audit, selection rate, group, representation (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/fairness_audit.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Where bias comes from

**Hook (5 min).** A model trained mostly on city data is used in a mountain district. What goes wrong?

**Concept (≤ 5 min).** Bias enters through who is in the data, how things are measured, labels that reflect past decisions, and how the model is used.

**Activity (20 min).** Analyse three cases; mark the bias source in each.

**Check (5 min).**
1. Name two sources of bias.
2. Is bias only a coding problem?
3. Who should be involved in checking?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Audit by group

**Hook (5 min).** Is the model equally good for everyone?

**Concept (≤ 5 min).** Compare accuracy, recall, selection rate and group sizes. Small groups give noisy numbers.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Run the group audit; add a group size column; identify the biggest gap.

**Check (5 min).**
1. Why show group sizes?
2. Selection rate is…
3. What gap matters most?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Responding and reporting

**Hook (5 min).** You find a gap. What do you do?

**Concept (≤ 5 min).** Options: collect better data, change the task, adjust thresholds with community agreement, add human review, or decide not to deploy. Report honestly, including limits.

**Activity (20 min).** Write the audit memo with findings, limits and three recommendations.

**Check (5 min).**
1. Can you always 'fix' bias with a tweak?
2. Why keep humans in the loop?
3. What must the memo include?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Audit memo

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
