# Grade 10 · Unit 2: Distributions and outliers

> Track: B (code) · Tools: Python, pandas, matplotlib · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `kathmandu-air-quality`

**Big idea.** The shape of data — centre, spread, skew and outliers — decides which summary and which test is fair.

**What you will be able to do**

* I can describe a distribution's shape.
* I can choose mean vs median and SD vs IQR.
* I can flag outliers with a transparent rule.

**Words to know:** distribution, skew, quartile, IQR, standard deviation, outlier (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/distributions.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Describing shape

**Hook (5 min).** Is a 'typical PM2.5 day' a single number?

**Concept (≤ 5 min).** Describe centre, spread, shape (symmetric, skewed, multi-peaked) and unusual values. Histograms show shape.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Draw histograms of three variables; describe each in a sentence.

**Check (5 min).**
1. Right-skewed means…
2. Which summary suits a skewed variable?
3. What does a two-peak histogram suggest?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Spread: SD and IQR

**Hook (5 min).** Two cities have the same mean PM2.5. How could they still differ?

**Concept (≤ 5 min).** Standard deviation measures typical distance from the mean; the IQR (Q3−Q1) is the range of the middle half and is robust to outliers.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute SD and IQR for PM2.5 and PM10; compare.

**Check (5 min).**
1. IQR equals…
2. Which is robust to outliers?
3. Same mean, bigger SD means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Outliers: flag, investigate, decide

**Hook (5 min).** A reading of 400 appears once. Error or a real pollution event?

**Concept (≤ 5 min).** Flag with a rule (1.5×IQR), then investigate: instrument error? real event? Keep, fix or remove — and document the decision.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Flag outliers in the series; look at their dates; decide and log.

**Check (5 min).**
1. Rule for the upper fence?
2. Do outliers always get deleted?
3. What must you record?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: What does a typical day look like?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
