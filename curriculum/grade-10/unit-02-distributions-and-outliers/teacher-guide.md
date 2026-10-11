# Teacher guide — Grade 10, Unit 2: Distributions and outliers

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Describing shape | 40–45 min |
| 2 | Spread: SD and IQR | 40–45 min |
| 3 | Outliers: flag, investigate, decide | 40–45 min |
| P | Unit project: What does a typical day look like? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/distributions.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Use printed 20-row extracts and graph paper; do the calculations with a calculator. The code lessons need a lab day, but every concept has a paper version.

## Common misconceptions
* Removing outliers automatically.
* Mean and SD are always the right summary.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Describing shape**
1. Right-skewed means…  
   *Answer:* A long tail to the high side.
2. Which summary suits a skewed variable?  
   *Answer:* The median.
3. What does a two-peak histogram suggest?  
   *Answer:* Maybe two groups or seasons mixed.

**Lesson 2: Spread: SD and IQR**
1. IQR equals…  
   *Answer:* Q3 − Q1.
2. Which is robust to outliers?  
   *Answer:* The IQR.
3. Same mean, bigger SD means…  
   *Answer:* More spread out values.

**Lesson 3: Outliers: flag, investigate, decide**
1. Rule for the upper fence?  
   *Answer:* Q3 + 1.5 × IQR.
2. Do outliers always get deleted?  
   *Answer:* No: investigate first.
3. What must you record?  
   *Answer:* The rule, the decision and the reason.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. (a) right-skewed; (b) roughly uniform; (c) possibly two humps (boys and girls), or one wide hump.
2. Mean 5; squared deviations 9, 1, 1, 1, 0, 0, 4, 16 = 32; ÷ 7 = 4.57; SD ≈ 2.14 (pandas 2.138). (Dividing by
   *n* gives exactly 2: a classic textbook example.)
3. IQR 40; fences 30 − 60 = −30 and 70 + 60 = 130 → 140 is an outlier; 0 is not.
4. 155 ± 2 × 7 = 141 to 169 → about 95%.
5. Maths z = (72 − 60) ÷ 8 = 1.5; Nepali z = (80 − 75) ÷ 4 = 1.25 → relatively better in Maths.
6. Dots appear in June, October and November (matching the within-month flags; box-plot quartile methods differ
   slightly).
7. 52.8 ± 2 × 33.0 → −13.1 to 118.7: negative pollution is impossible; the data are not bell-shaped (two humps, bounded
   at zero).
8. 16.0 → probably 160 (decimal slip) — fix only if confirmed, else missing; 1,580 → probably 158.0 — same; 150, 155,
   162 fine. Log each.
9. e.g. 10, 11, 12, 13, 14 (SD 1.58, IQR 2) vs 10, 11, 12, 13, 140 (SD 57.0, IQR 2).
10. The worst days are the point of the analysis; removing them understates exposure and risk.

Lesson 2 step 4 (most unusual within-month days by z): 2019-06-08 (z 3.15), 2019-08-23 (3.11), 2020-11-26 (3.05),
2019-10-05 (−2.93), 2019-06-12 (2.88). Lesson 3 Make: population outliers (whole-table IQR rule, upper fence
1,071,121) are Terai-09, Terai-15, Terai-17 — real; keep.

## Real-data exercises: notes
* **R1** High real values cluster in winter dry spells, around festivals (fireworks/Tihar in some years), and during
  spring forest-fire smoke (March–April). Low outliers can come from rain events or sensor problems.
* **R2** Most days have zero or tiny rain; median daily rain is often 0 mm while the mean is several mm. Median
  describes a typical day; the total (or mean × 365) describes the year.
* **R3** (2026-10-11 file) mean 4.48, median 4.4, SD 0.49, IQR 0.4, upper fence 5.2 → the 7.8 (and every quake above
  5.2) is flagged. They are real events — the most important rows of the dataset.
