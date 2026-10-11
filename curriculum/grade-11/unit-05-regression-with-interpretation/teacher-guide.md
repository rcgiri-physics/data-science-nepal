# Teacher guide — Grade 11, Unit 5: Regression with interpretation

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Simple regression revisited | 40–45 min |
| 2 | Multiple regression | 40–45 min |
| 3 | Checking the model | 40–45 min |
| P | Unit project: Explain it, don't just fit it | 2 periods |

## Before you start
* Materials: Notebook `notebooks/regression.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Use a printed scatter of birth weight vs visits; draw a line; read its slope.

## Common misconceptions
* Coefficient = causal effect. It is an association given the other variables.
* High R² means a good model.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Simple regression revisited**
1. Slope 0.04 kg per visit means…  
   *Answer:* Each extra visit goes with about 0.04 kg higher birth weight on average.
2. What does the intercept mean?  
   *Answer:* The predicted y when x = 0 (may not make sense).
3. What is minimised?  
   *Answer:* The sum of squared residuals.

**Lesson 2: Multiple regression**
1. 'Holding visits fixed' means…  
   *Answer:* Comparing mothers with the same number of visits.
2. Why might a coefficient shrink when adding a predictor?  
   *Answer:* Predictors share information.
3. Does a coefficient show cause?  
   *Answer:* Not by itself.

**Lesson 3: Checking the model**
1. What does R² = 0.4 mean?  
   *Answer:* 40% of the variation in y is explained by the model.
2. What pattern in residuals is a warning?  
   *Answer:* A curve or funnel shape.
3. Is high R² always good?  
   *Answer:* No: it depends on purpose and can reflect overfitting.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. Each extra bag of fertiliser is associated with about 15 kg more rice per ropani on average; 120 kg per ropani is the
   predicted yield with no fertiliser (meaningful only if such plots are in the data).
2. With *k* dummies plus an intercept the columns add up to the intercept column (perfect collinearity); one category
   must be the reference that the others are compared with.
3. "…75% of the variation in the outcome; 25% is left unexplained."
4. Quintile 2, 4 visits: 2.544 + 0.124 + 0.208 ≈ 2.88 kg; quintile 5: ≈ 3.06 kg. Difference 0.186 kg = 3 × 0.062 (the
   wealth coefficient, visits held fixed).
5. Coefficients: intercept 0.150, visits +0.074, wealth +0.022 → each extra visit goes with about 7 percentage points
   higher probability of facility delivery, wealth held fixed. Predictions here range 0.17–0.81, but in general a
   linear model can predict below 0 or above 1 (impossible probabilities) — logistic regression (Grade 12) fixes this.
6. Mean residual by wealth: quintile 1 −0.09, 2 −0.06, 3 0.00, 4 +0.02, 5 +0.14 kg — the visits-only model
   systematically under-predicts rich mothers' babies and over-predicts poor ones: wealth is a missing predictor.
7. Students who study more also tend to take more tuition; a model with both cannot tell which one matters, and the
   coefficients swing between samples.
8. Who the workers were (sample), what else differs between more- and less-schooled workers (family wealth, location,
   ability — confounders), whether it is an experiment or observational, the interval for the coefficient, whether the
   relationship is linear.
9. `fake` correlates 0.98 with wealth: coefficients split arbitrarily (wealth 0.053, fake 0.026) and their bootstrap
   intervals become wide and include 0 (≈ −0.02 to 0.12 and −0.05 to 0.10) although wealth clearly matters.
10. Yes: bootstrap R² ≈ 0.06 to 0.12.

Lesson 3: bootstrap 95% intervals (1,000 resamples, seed 0) — visits 0.033 to 0.068 kg; wealth 0.046 to 0.079 kg.

## Real-data exercises: notes
* **R1** Flipper coefficient shrinks once species is included (species differ in both size and flipper length).
* **R2** The income coefficient usually shrinks when a health-system variable is added — those variables are partly how
  income works.
* **R3** Expect −0.5 to −0.6 °C per 100 m; adding latitude changes it little within Nepal's narrow latitude range.
