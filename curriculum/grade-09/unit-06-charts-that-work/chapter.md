# Grade 9 · Unit 6: Charts that work

> Track: B (code: matplotlib) · Tools: Python, matplotlib · Lessons: 3
> Datasets: `census-districts`

**Big idea.** Choose the chart that fits the question — histogram for distribution, bar for categories, scatter for relationships — and label it honestly.

**What you will be able to do**

* I can draw bar charts and histograms in Python and choose sensible bins.
* I can read and draw box plots and use them to compare groups.
* I can draw a scatter plot and describe a relationship without claiming cause.

**Words to know:** figure, axis (अक्ष), bin, histogram (आयतचित्र), box plot, quartile (चतुर्थांश), interquartile range, outlier, scatter plot, correlation (सहसम्बन्ध). Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/charts.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
From Grade 8 Unit 4: which graph for which data, and how graphs mislead. From Unit 5: loading, filtering and grouping
in pandas. Every chart in this unit starts with these lines:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("districts_synthetic.csv")
schools = pd.read_csv("schools_synthetic.csv")
```

---

## Lesson 1: Histograms and bar charts

**Hook (5 min).** What is the difference between a bar chart of ecological belts and a histogram of literacy? Sketch
both before running any code.

### Explanation
**matplotlib** is Python's standard charting library; `pyplot` (imported as `plt`) gives simple commands. Every chart
follows the same recipe:

1. make the chart (`plt.bar`, `plt.hist`, `plt.scatter`, …);
2. label it (`plt.title`, `plt.xlabel`, `plt.ylabel`) — **always with units**;
3. show it (`plt.show()`).

**Bar chart — categories.** First count, then draw:

```python
counts = df["ecological_belt"].value_counts()      # Hill 39, Terai 22, Mountain 16
plt.bar(counts.index, counts.values)
plt.title("Number of districts by ecological belt (synthetic data)")
plt.xlabel("Ecological belt")
plt.ylabel("Number of districts")
plt.show()
```

`value_counts()` counts each category and sorts from most to least. For a horizontal bar chart (easier to read with
long names), use `plt.barh`.

**Histogram — the distribution of one numerical variable.** `plt.hist` splits the range into **bins** of equal width
and counts the values in each:

```python
plt.hist(df["literacy_pct"], bins=10, edgecolor="black")
plt.title("Literacy rate in 77 districts (synthetic data)")
plt.xlabel("Literacy (%)")
plt.ylabel("Number of districts")
plt.show()
```

**Bins change the picture.** With 5 bins the shape looks smooth and simple; with 30 bins it looks jagged, with gaps.
Neither is "true": try a few and describe what stays the same. A good start is a number of bins near the square root
of the number of values (√77 ≈ 9). You can also give exact bin edges: `bins=range(60, 86, 2)` makes bins 60–62,
62–64, … 84–86.

**Describe a histogram** with the Grade 8 four-part description: centre, spread, shape (symmetric? skewed? more
than one peak?), unusual values.

**Several charts side by side** use `plt.subplots`:

```python
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, b in zip(axes, [5, 10, 30]):
    ax.hist(df["literacy_pct"], bins=b, edgecolor="black")
    ax.set_title(f"{b} bins")
    ax.set_xlabel("Literacy (%)")
axes[0].set_ylabel("Districts")
plt.tight_layout()
plt.show()
```

Note: with `axes`, the labelling commands start with `set_` (`ax.set_title`).

### Activity (20 min) — PRIMM
1. **Predict** the tallest bar in the belt bar chart, then run it.
2. Draw the literacy histogram with 5, 10 and 30 bins. Write one sentence on what changes and one on what stays.
3. **Modify:** histogram of `population`. Is it symmetric or skewed? Where is the long tail?
4. **Make:** bar chart of the number of districts per province, in province order (`.sort_index()`).

### Common mistakes
* A histogram of a categorical variable, or a bar chart with one bar per district.
* Forgetting axis labels and units, or "(synthetic data)" in the title.
* Calling `plt.show()` before labels: labels set afterwards appear on the next, empty chart.

**Check (5 min).**
1. Bars or histogram for 'belt'?
2. What is a bin?
3. Why try different bin counts?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Box plots and outliers

**Hook (5 min).** How could one picture compare literacy in the three belts, showing the typical value, the spread
and any unusual districts all at once?

### Explanation
**Quartiles** split sorted data into four equal parts:
* **Q1** (lower quartile): 25% of values are below it;
* **Q2** = the **median**: 50% below;
* **Q3** (upper quartile): 75% below.

The **interquartile range** IQR = Q3 − Q1 is the spread of the **middle half** of the data. Unlike the range, it is
not affected by a single extreme value.

A **box plot** (box-and-whisker plot) draws:
* a **box** from Q1 to Q3, with a **line at the median**;
* **whiskers** out to the most extreme values that are still within 1.5 × IQR of the box;
* **dots** for values beyond that — possible **outliers**.

**Worked example (Hill districts, synthetic).** Q1 = 74.3, median = 77.5, Q3 = 79.9, so IQR = 5.6 and
1.5 × IQR = 8.4. Values below 74.3 − 8.4 = 65.9 count as outliers: Hill-24 (65.4%) and Hill-35 (64.6%) appear as dots.

```python
belts = ["Mountain", "Hill", "Terai"]
groups = [df.loc[df["ecological_belt"] == b, "literacy_pct"] for b in belts]
plt.boxplot(groups)
plt.xticks([1, 2, 3], belts)
plt.title("Literacy by ecological belt (synthetic data)")
plt.ylabel("Literacy (%)")
plt.show()
```

Box plots are excellent for **comparing groups**: compare the medians (lines), the boxes (do the middle halves
overlap?) and the outliers. Here Hill's box sits entirely above Mountain's: the difference is consistent, not just in
the medians. pandas can make the same chart in one line: `df.boxplot(column="literacy_pct", by="ecological_belt")`.

**What to do with outliers.** Investigate, don't delete:
1. Is it an **error** (a typo, a unit mistake, an error code)? Fix it if you can, and log it (Unit 2).
2. Is it **real**? Then it may be the most interesting district in the table — why is Hill-35 so low? Keep it and
   mention it.
3. If you leave it out of one calculation, say so and show the result with and without it.

### Activity (20 min) — PRIMM
1. **Predict** which belt has the highest median and which has outliers. Run the box plot.
2. Use `df.groupby("ecological_belt")["literacy_pct"].describe()` to read Q1, median and Q3 for each belt, and check
   the outlier rule for one belt by hand.
3. **Make:** a box plot of `abroad_per_1000` by belt (create the column first, as in Unit 5). Write a comparison
   sentence.

### Common mistakes
* Reading the box as "the range". It is the middle 50%.
* Thinking every dot is an error.
* Comparing box plots drawn on different y-axes.

**Check (5 min).**
1. What does the line in the box show?
2. What is an outlier?
3. Should you delete outliers automatically?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Scatter plots

**Hook (5 min).** Do districts with more secondary schools per person have higher literacy? Predict: strong
relationship, weak relationship, or none?

### Explanation
A **scatter plot** puts one numerical variable on each axis and draws **one dot per case** (per district). It shows
whether two variables move together.

```python
m = df.merge(schools, on="district_id")              # pandas JOIN (SQL: JOIN … ON district_id)
m["schools_per_100k"] = 100000 * m["n_secondary_schools"] / m["population"]

plt.scatter(m["schools_per_100k"], m["literacy_pct"])
plt.title("Schools and literacy in 77 districts (synthetic data)")
plt.xlabel("Secondary schools per 100,000 people")
plt.ylabel("Literacy (%)")
plt.show()
```

`df.merge(other, on="key")` is pandas' JOIN.

**Describe a relationship with four words:**
* **Direction:** positive (up to the right: more of one, more of the other), negative (down to the right), or none.
* **Form:** roughly a straight line (linear) or a curve.
* **Strength:** how tightly the dots follow the pattern: strong, moderate, weak.
* **Unusual points:** dots far from the pattern.

The **correlation coefficient** *r* measures the strength of a straight-line relationship, from −1 (perfect negative)
through 0 (none) to +1 (perfect positive):

```python
r = m["schools_per_100k"].corr(m["literacy_pct"])
print(round(r, 2))   # 0.18: a weak positive relationship
```

As a rough guide: |r| < 0.3 weak, 0.3–0.7 moderate, > 0.7 strong. Always look at the plot too; *r* can be fooled by
curves and outliers.

**Correlation is not causation.** Even a strong relationship does not show that one variable *causes* the other.
There may be a **third variable** (a *confounder*) behind both: districts closer to cities might have both more
schools and more literate adults. Or the cause might run the other way. Or it might be chance. Grade 11 shows how
experiments and careful comparisons get closer to causes.

### Activity (20 min) — PRIMM
1. **Predict** the direction and strength, then run the schools-and-literacy scatter. Compute *r*.
2. **Modify:** plot `abroad_per_1000` (x) against `literacy_pct` (y). Describe it with the four words and compute
   *r*.
3. Colour the dots by belt: loop over belts and call `plt.scatter` once per belt with `label=b`, then `plt.legend()`.
   Does the pattern hold within each belt?
4. Propose one third variable that could explain the relationship you see.

### Common mistakes
* Joining dots with lines (`plt.plot`) when the x-axis is not time.
* Saying "X causes Y" from a scatter plot.
* Ignoring that a few extreme districts can create (or hide) a pattern.

**Check (5 min).**
1. What does each dot represent?
2. If points slope upward, what do we call it?
3. Does it prove one causes the other?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Recipe: make → label (with units and source) → show. `plt.subplots` for several charts.
* Bar chart = categories (`value_counts`); histogram = one numerical variable (try several bin counts).
* Quartiles Q1, median, Q3; IQR = Q3 − Q1; box plots compare groups; outliers are beyond 1.5 × IQR — investigate,
  don't delete.
* Scatter plot = two numerical variables; describe direction, form, strength, unusual points; *r* from −1 to +1.
* Correlation is not causation: look for a third variable.

## Practice exercises
1. ★ Which chart: (a) number of students by travel mode; (b) distribution of heights; (c) height vs weight;
   (d) heights of boys vs girls?
2. ★ For the values 2, 4, 4, 5, 7, 8, 9, 10, 12, 30: find Q1, median, Q3, IQR and check whether 30 is an outlier.
   (Use the median of each half for the quartiles.)
3. ★ What do `plt.xlabel` and `ax.set_xlabel` have in common, and when do you use each?
4. ★★ Draw a histogram of `area_km2` with 10 bins. Describe the shape.
5. ★★ Draw a horizontal bar chart (`plt.barh`) of the 10 most populous districts, largest at the top.
6. ★★ Box plot of `household_size` by belt. Which belt has the biggest households? Any outliers?
7. ★★ Scatter plot of `area_km2` vs `population`. Describe it and compute *r*. Does a bigger area mean more people?
8. ★★★ Using the class survey, draw a scatter plot of `sleep_hours` vs `travel_minutes`. Describe it. Would you
   expect a relationship? Why?
9. ★★★ A news report says: "Districts with more mobile phones have higher literacy, so phones make people literate."
   Give two other explanations.
10. ★★★ Make the same literacy histogram twice, once with the y-axis from 0 and once with `plt.ylim(5, 15)`. How can
    the second mislead?

## Exercises with real data
**R1. Life and wealth (RD-03 / RD-01).** Download GDP per capita and life expectancy for all countries for one year
(Gapminder or World Bank). Draw a scatter plot (GDP on the x-axis) and find Nepal (plot it in a different colour).
Describe the relationship. Try `plt.xscale("log")`: what changes, and why might economists prefer it?
*Offline fallback:* scatter of `rain_mm` vs `mean_temp_c` from `climate_monthly_synthetic.csv`.

**R2. Earthquake magnitudes and depths (RD-05).** Load the USGS 2015 Nepal file. Draw a histogram of `mag` (bins of
0.1 from 4.0 to 8.0) and a scatter of `depth` vs `mag`. Why are so many depths exactly 10 km? (Read the USGS notes on
fixed depths, or ask your teacher.)

**R3. Child mortality in South Asia (RD-02).** Load the OWID child-mortality CSV for Nepal, India, Bangladesh, Sri
Lanka (remember the User-Agent tip). Draw one line per country (`plt.plot` with `label=`), add a legend, title,
axis labels and source note (`plt.figtext(0.01, 0.01, "Source: …")`).

## Unit project: One chart, one claim
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose one claim about the districts and make
the **single best chart** to support it (with title, axis labels, units, source and "synthetic" note). Add a
one-sentence caption, one limitation, and one alternative chart you tried and rejected (with why). Full brief and
rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* The matplotlib gallery (<https://matplotlib.org/stable/gallery/>): find a chart, copy its code, change it.
* "From Data to Viz" (<https://www.data-to-viz.com>): a decision tree for choosing charts.
* Gapminder Tools (<https://www.gapminder.org/tools/>): the moving bubble chart of health and wealth.
