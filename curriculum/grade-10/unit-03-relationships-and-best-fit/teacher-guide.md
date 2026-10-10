# Teacher guide — Grade 10, Unit 3: Relationships and the line of best fit

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Scatter plots and correlation | 40–45 min |
| 2 | The line of best fit | 40–45 min |
| 3 | Correlation is not causation | 40–45 min |
| P | Unit project: Two variables, one honest line | 2 periods |

## Before you start
* Materials: Notebook `notebooks/best_fit.ipynb`; ruler and string for the by-hand fit.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Do the line of best fit with a ruler on a printed scatter plot; estimate slope by two points.

## Common misconceptions
* A high correlation proves one causes the other.
* A line fits any data; check the scatter.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Scatter plots and correlation**
1. r = −0.9 means…  
   *Answer:* A strong negative straight-line relationship.
2. r = 0 means…  
   *Answer:* No straight-line relationship (curves possible).
3. Does r show cause?  
   *Answer:* No.

**Lesson 2: The line of best fit**
1. Slope 1.6 for PM10 vs PM2.5 means…  
   *Answer:* PM10 is about 1.6 µg/m³ higher for each 1 µg/m³ of PM2.5.
2. What is a residual?  
   *Answer:* Observed − predicted.
3. Why squares?  
   *Answer:* So positive and negative misses don't cancel.

**Lesson 3: Correlation is not causation**
1. What is a confounder?  
   *Answer:* A hidden factor that affects both variables.
2. Give an example.  
   *Answer:* Summer heat drives both ice-cream sales and swimming accidents.
3. What design supports causal claims?  
   *Answer:* A randomised experiment.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. (a) hours studied (b) altitude (c) rainfall.
2. ŷ = 25; residual = 22 − 25 = −3.
3. Any curve such as a U-shape (points at (−2, 4), (−1, 1), (0, 0), (1, 1), (2, 4)) has *r* = 0.
4. *b* = 0.8 × 10 ÷ 4 = 2.0; *a* = 50 − 2 × 20 = 10 → ŷ = 10 + 2*x*.
5. Slope −0.006 °C per metre (−0.6 °C per 100 m). 25 − 0.006 × (1,400 − 70) ≈ 17 °C. Wrong because of local effects:
   valleys, slope aspect, cloud and rain shadow, latitude; the lapse rate varies by season.
6. Jan–Jun slope ≈ −17.4 µg/m³ per month (falls into the monsoon); intercept ≈ 119. Over 12 months the pattern goes
   down then up (U-shape), so a straight line fits badly.
7. *r²* ≈ 0.97: the line accounts for about 97% of the day-to-day variation in PM10 in this synthetic data.
8. Sleep improves concentration (cause); students with fewer worries/better home conditions both sleep and study more
   (confounding); students who do well feel less stress and sleep better (reverse). An experiment (randomly encourage
   one group to sleep earlier) or comparing the same students across weeks helps.
9. Regressing *y* on *x* minimises vertical misses; *x* on *y* minimises horizontal misses — different lines unless
   *r* = ±1.
10. *r* = 0.90 (by hand and pandas).

Lesson 1 step 3: one fake point (10, 400) drops *r* from 0.986 to 0.953. Lesson 3 step 1: all months *r* = 0.67;
monsoon months only 0.33; dry months only 0.02 — the season explains most of the overall correlation.
Lesson 2 predictions: PM2.5 40 → PM10 ≈ 66; 100 → ≈ 165; typical residual (SD) ≈ 9 µg/m³.

## Real-data exercises: notes
* **R1** Roughly +5 to +8 years of life expectancy for each tenfold income increase in recent data; Nepal typically
  lives **longer** than its income predicts (positive residual) — a nice discussion of public health, remittances
  and other factors.
* **R2** Expect around −0.5 to −0.65 °C per 100 m; Jomsom (rain-shadow, windy valley) and Kathmandu (valley basin)
  may have notable residuals. Open-Meteo's grid smooths mountains, so high towns may look warmer than station data.
* **R3** Strong positive relationship. Plausible: lower child mortality → parents choose fewer children; also
  education, income and contraception access drive both (confounding).
