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
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics (⚠️ unit numbers to be added after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
