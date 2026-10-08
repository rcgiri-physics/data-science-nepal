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
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics (⚠️ unit numbers to be added after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
