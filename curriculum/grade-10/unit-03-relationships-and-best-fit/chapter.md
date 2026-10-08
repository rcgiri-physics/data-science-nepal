# Grade 10 · Unit 3: Relationships and the line of best fit

> Track: B (code) · Tools: Python, numpy, matplotlib · Lessons: 3
> Datasets: `kathmandu-air-quality`, `climate-monthly`

**Big idea.** A scatter plot shows if two variables move together; a line of best fit summarises it; correlation is not causation.

**What you will be able to do**

* I can draw and describe a scatter plot.
* I can compute and interpret a correlation and slope.
* I can explain why correlation does not prove cause.

**Words to know:** scatter plot, correlation, slope, residual, line of best fit (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/best_fit.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Scatter plots and correlation

**Hook (5 min).** Does a dirtier PM2.5 day usually come with dirtier PM10?

**Concept (≤ 5 min).** Describe direction, strength and shape. Correlation r runs from −1 to +1: sign gives direction, size gives strength for straight-line relationships.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Plot PM2.5 vs PM10; guess r before computing; compute and compare.

**Check (5 min).**
1. r = −0.9 means…
2. r = 0 means…
3. Does r show cause?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: The line of best fit

**Hook (5 min).** Draw the line you think fits best. Is it the same as your neighbour's?

**Concept (≤ 5 min).** Least squares chooses the line that minimises the sum of squared vertical misses (residuals). Slope = change in y per 1 unit of x.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Fit by eye with a ruler first; then np.polyfit; compare slopes; interpret in words.

**Check (5 min).**
1. Slope 1.6 for PM10 vs PM2.5 means…
2. What is a residual?
3. Why squares?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Correlation is not causation

**Hook (5 min).** Ice-cream sales and drownings rise together. Does ice-cream cause drowning?

**Concept (≤ 5 min).** A third factor (a confounder, like hot weather) can drive both. Only careful design (experiments) or strong reasoning can support cause.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Find two variables in the climate table that correlate because of the season; name the hidden factor; propose how to test a causal claim.

**Check (5 min).**
1. What is a confounder?
2. Give an example.
3. What design supports causal claims?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Two variables, one honest line

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
