# Grade 11 · Unit 3: Uncertainty: bootstrap and confidence intervals

> Track: B (code) · Tools: Python, numpy · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `health-synthetic`

**Big idea.** A sample gives one estimate; resampling shows how much it could vary. A confidence interval is a range that reflects that uncertainty.

**What you will be able to do**

* I can explain sampling variation.
* I can build a bootstrap confidence interval.
* I can interpret an interval correctly.

**Words to know:** sampling variation, bootstrap, resample, confidence interval, estimate (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/bootstrap.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Sampling variation

**Hook (5 min).** Two schools survey 100 students each about sleep. Will they get the same mean?

**Concept (≤ 5 min).** Different samples give different estimates. This random wobble is sampling variation; it shrinks as samples grow.

**Activity (20 min).** Draw 10 samples of 20 slips; plot the 10 means; discuss the spread.

**Check (5 min).**
1. Will two samples give the same mean?
2. Bigger sample → ?
3. What causes the difference?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: The bootstrap

**Hook (5 min).** We have only one sample. How do we imitate drawing many?

**Concept (≤ 5 min).** Resample the sample with replacement, compute the statistic each time; the spread of those values shows the uncertainty.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Run bootstrap_means on 100 records; plot the histogram; read off the middle 95%.

**Check (5 min).**
1. 'With replacement' means…
2. What do we compute each time?
3. Middle 95% gives…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Interpreting intervals

**Hook (5 min).** A poll says 55% ± 4. What does ± 4 mean?

**Concept (≤ 5 min).** A wide interval means the estimate is uncertain; a narrow one, precise. It speaks of the estimate of the population value — not of individual cases — and not of bias in the sampling.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compare intervals for n = 25, 100, 400; write correct and incorrect interpretations.

**Check (5 min).**
1. Which is narrower, n=25 or n=400?
2. Does a narrow interval fix a biased sample?
3. Is a 95% interval where 95% of the data lie?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: How sure are we?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
