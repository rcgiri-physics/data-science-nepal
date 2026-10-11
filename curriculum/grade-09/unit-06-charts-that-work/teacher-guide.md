# Teacher guide — Grade 9, Unit 6: Charts that work

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code: matplotlib).

| # | Lesson | Time |
|---|---|---|
| 1 | Histograms and bar charts | 40–45 min |
| 2 | Box plots and outliers | 40–45 min |
| 3 | Scatter plots | 40–45 min |
| P | Unit project: One chart, one claim | 2 periods |

## Before you start
* Materials: Notebook `notebooks/charts.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Draw the same charts on graph paper from a 15-row extract (Grade 8 Unit 4 skills).

## Common misconceptions
* Bar chart ≠ histogram: bars for categories, bins for numerical ranges.
* Correlation (scatter pattern) is not proof of cause.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Histograms and bar charts**
1. Bars or histogram for 'belt'?  
   *Answer:* Bar chart (categorical).
2. What is a bin?  
   *Answer:* A range of values counted together.
3. Why try different bin counts?  
   *Answer:* Shapes can look different; avoid being fooled by one choice.

**Lesson 2: Box plots and outliers**
1. What does the line in the box show?  
   *Answer:* The median.
2. What is an outlier?  
   *Answer:* A value far from the rest.
3. Should you delete outliers automatically?  
   *Answer:* No: investigate first; they may be errors or important facts.

**Lesson 3: Scatter plots**
1. What does each dot represent?  
   *Answer:* One district.
2. If points slope upward, what do we call it?  
   *Answer:* A positive relationship.
3. Does it prove one causes the other?  
   *Answer:* No: other factors may drive both.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
1. (a) bar chart (b) histogram (or box plot) (c) scatter plot (d) side-by-side box plots (or two histograms on one
   scale).
2. Halves: 2, 4, 4, 5, 7 and 8, 9, 10, 12, 30 → Q1 = 4, median = (7 + 8) ÷ 2 = 7.5, Q3 = 10, IQR = 6;
   upper fence 10 + 9 = 19 → 30 is an outlier. (Software uses slightly different quartile rules; small differences
   are fine.)
3. Both set the x-axis label. `plt.xlabel` works on the current single chart; `ax.set_xlabel` on one chosen panel when
   using `plt.subplots`.
4. Right-skewed: most districts 1,000–2,500 km², a long tail up to about 5,500 km² (Mountain districts are large).
5. `top = df.sort_values("population").tail(10)`; `plt.barh(top["district"], top["population"])` (sorting
   ascending then `barh` puts the largest at the top).
6. Medians: Hill 4.62, Mountain 4.64, Terai 4.59 — very similar; no outliers by the 1.5 × IQR rule.
7. *r* ≈ −0.34: a moderate **negative** relationship — bigger (mountain) districts tend to have fewer people. Area
   does not mean more people.
8. *r* ≈ 0.03: no relationship. Plausible: travel time hardly changes sleep in this (synthetic) class; real data
   might differ if long journeys mean early waking.
9. Richer districts have more phones *and* more schools (income as third variable); urban districts have both;
   literate people may buy more phones (reverse direction).
10. The cut axis makes small differences in counts look large (Grade 8 Unit 4).

Lesson 3 activity: `abroad_per_1000` vs literacy: *r* ≈ 0.37 overall (moderate positive). **But within belts** it is
weak or negative (Hill 0.12, Mountain −0.39, Terai −0.04): the overall pattern comes mostly from differences
*between* belts (Mountain districts have both low literacy and low emigration). This is a lovely, simple example of a
confounder (belt) — make sure students see it in step 3.

## Real-data exercises: notes
* **R1** Strong positive but curved relationship; on a log x-axis it is roughly a straight line, because each
  *doubling* of income goes with a similar gain in life expectancy. Nepal sits in the lower-middle income group with
  a life expectancy higher than many countries of similar income.
* **R2** Histogram right-skewed; 253 of 304 events at exactly 10 km — USGS uses a fixed default depth when depth is
  poorly constrained.
* **R3** Check legend, source note, units ("% of children dying before age 5").
