# Grade 11 · Unit 4: Is the difference real? Permutation tests

> Track: B (code) · Tools: Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** To ask if a difference between two groups could be just chance, shuffle the labels many times and see how often chance alone produces such a difference.

**What you will be able to do**

* I can state a null idea in plain words.
* I can run a permutation test.
* I can interpret a p-value without overclaiming.

**Words to know:** null hypothesis, permutation, p-value, chance, effect size (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/permutation.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: The idea of chance

**Hook (5 min).** Two cricket teams score 12 runs apart. Luck or skill?

**Concept (≤ 5 min).** A difference could arise by chance alone. We ask: if groups were interchangeable, how often would shuffling produce a difference this big?

**Activity (20 min).** Shuffle cards for two groups; record differences; compare with the observed one.

**Check (5 min).**
1. What does shuffling labels imitate?
2. What do we compare to?
3. What is chance variation?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Run a permutation test

**Hook (5 min).** How do we do 5,000 shuffles quickly?

**Concept (≤ 5 min).** Pool values, shuffle, split into group sizes, compute the difference; repeat. The p-value is the share of shuffles at least as extreme as observed.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Run the notebook; change the number of shuffles; try the Hill vs Mountain comparison.

**Check (5 min).**
1. p-value = ?
2. Why 5,000 shuffles?
3. What does a tiny p-value suggest?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Interpreting results honestly

**Hook (5 min).** p = 0.03 — headline: 'Proven!' What's wrong?

**Concept (≤ 5 min).** p-values don't measure importance, cause or truth of a claim; report the effect size, uncertainty and design. Many tests → more false alarms.

**Activity (20 min).** Rewrite three overclaiming headlines honestly.

**Check (5 min).**
1. Does small p show a large effect?
2. Does large p show no difference?
3. What else to report?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Chance or real?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
