# Teacher guide — Grade 11, Unit 6: Time series and seasonality

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Seasonal indices | 40–45 min |
| 2 | Trend with a fitted line | 40–45 min |
| 3 | Trend with uncertainty | 40–45 min |
| P | Unit project: Climate or weather? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/seasonality.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Plot 3 years of monthly values on one sheet of graph paper with years overlaid.

## Common misconceptions
* A cold winter disproves warming (weather vs climate).
* A trend line from 5 years shows the long-run trend.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Seasonal indices**
1. Seasonal indices sum to…  
   *Answer:* About 0 (if defined relative to the mean).
2. Why de-seasonalise?  
   *Answer:* To see the trend without the yearly cycle.
3. Is a cold January evidence against warming?  
   *Answer:* No: weather varies.

**Lesson 2: Trend with a fitted line**
1. Slope 0.03/yr → per decade?  
   *Answer:* 0.3.
2. Why try different start years?  
   *Answer:* To test sensitivity.
3. Short series risk?  
   *Answer:* Unreliable trend.

**Lesson 3: Trend with uncertainty**
1. Why resample whole years?  
   *Answer:* Months within a year are related.
2. Interval excludes 0 means…  
   *Answer:* A non-zero trend is likely in this series.
3. Does it prove cause?  
   *Answer:* No: it describes the trend, not the reason.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. 10.2 − (−7.8) = 18.0 °C; below the overall mean of about 18.5 °C, so a slightly cold January.
2. 3.67 × 132.7 ≈ 487 mm.
3. Months in the same year are related (autocorrelated); resampling them separately pretends there is more independent
   information and makes intervals too narrow.
4. Additive rain indices: about −105 to −113 mm in dry months and +354 mm in July. An additive index would predict
   negative rain for a dry month in a dry year; rain's seasonal swing scales with the level, so ratios fit better.
5. Trends (°C/decade, de-seasonalised): Dec–Feb 0.42, Sep–Nov 0.30, Jun–Aug 0.22, Mar–May 0.17 — winter fastest.
6. January only: 0.40 °C/decade, CI ≈ 0.15 to 0.67 — wider because one month per year is noisier than an annual mean
   of 12 months.
7. October 2020 (78.3 mm, adjusted ≈ 456 mm): an exceptionally wet October relative to a normal October (like a late
   monsoon).
8. In our simulation 9% of the intervals excluded 0 (should be about 5%): percentile-bootstrap intervals on 30 points
   are a little too narrow. Good discussion of methods having error rates too.
9. A −1 °C jump in 2005 turns the +0.28 °C/decade trend into about −0.22 °C/decade: a careless analyst would announce
   cooling. Station metadata and homogenisation matter.
10. Seasonally adjusted: same level as the data, season removed (for reading month-to-month change). Anomaly: difference
    from the month's baseline (for comparing places/periods). 12-month rolling mean: smooth trend, delayed (for seeing
    the long-run direction).

Lesson 2 sensitivity: trends from 1991 0.28, 1996 0.30, 2001 0.34, 2006 0.31, 2011 0.10 °C/decade. Lesson 1 Make: an
average July carries about 31% of the year's rain (synthetic).

## Real-data exercises: notes
* **R1** Expect positive trends of a few tenths of a degree per decade, CIs depend on the grid cell.
* **R2** Nepal's peak months are typically October–November and March–April; 2015 (earthquake) and 2020–21 (COVID-19)
  show as huge negative residuals.
* **R3** Tomato prices are often lowest in the winter harvest months and highest in the monsoon; check with the data.
