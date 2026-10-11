# Teacher guide — Grade 12, Unit 6: Feature engineering

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Creating features | 40–45 min |
| 2 | Encoding categories | 40–45 min |
| 3 | Comparing feature sets honestly | 40–45 min |
| P | Unit project: Feature challenge | 2 periods |

## Before you start
* Materials: Notebook `notebooks/features.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Brainstorm features on cards for predicting 'will a student reach school late?'.

## Common misconceptions
* More features is always better.
* Features using future information (leakage).

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Creating features**
1. Name a ratio feature.  
   *Answer:* e.g. people per school.
2. What is an interaction?  
   *Answer:* A product of two features capturing a joint effect.
3. Why use domain knowledge?  
   *Answer:* It suggests meaningful features.

**Lesson 2: Encoding categories**
1. One-hot of 3 categories makes…  
   *Answer:* 3 columns of 0/1.
2. Why not 1, 2, 3?  
   *Answer:* It implies order and distance that aren't real.
3. What is get_dummies?  
   *Answer:* A pandas function for one-hot encoding.

**Lesson 3: Comparing feature sets honestly**
1. Why 5-fold CV?  
   *Answer:* It averages over several splits to reduce luck.
2. What is leakage in features?  
   *Answer:* Using information that won't be available at prediction time.
3. Pick the simplest set that is…  
   *Answer:* About as good as the best.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. `df["persons_per_household"] = df["population"] / df["households"]`.
2. 6 columns (7 provinces minus the reference).
3. Population is right-skewed (27,000 to 1.6 million); a log makes differences relative ("10 times bigger") and stops a
   few large districts dominating a linear model.
4. Facility-delivery rate: < 20: 0.466 (234 women); 20–34: 0.441 (811); 35+: 0.429 (455) — small differences in this
   synthetic data (age was not built into the generator).
5. B + interaction: 0.603 ± 0.025 vs B 0.607 ± 0.024 — no meaningful change.
6. Month, weekday, winter flag and yesterday's PM2.5 are all known today for predicting tomorrow; "PM2.5 today" is also
   fine if the prediction is made after today's reading; anything from tomorrow would be leakage.
7. Trees split on one column at a time; a full set of one-hot columns causes no algebraic problem (there is no solving
   of a linear system), and keeping all categories can make splits clearer.
8. ColumnTransformer version: 0.605 vs set D 0.606 — they should match closely (same information; small differences
   from where scaling is applied).
9. Leakage: the follow-up visit probably happened because of (or after) the delivery outcome, or is recorded only for
   certain outcomes. Check when the column is filled in, and test the model with it removed.
10. e.g. rain in the past 3 days, humidity change from yesterday, monsoon-month flag; compare with time-ordered CV
    (train on earlier periods, validate on later), report mean ± SD.

Lesson 2 step 3: CV accuracy with numeric belt code 0.602 vs one-hot ≈ 0.605 — close because belt adds little beyond
visits and wealth in this synthetic data; the coding is still conceptually wrong, as the regression in the lesson shows.

## Real-data exercises: notes
* **R1** Bill length ÷ depth separates Gentoo from the others strongly; island one-hot helps Adelie vs Chinstrap.
* **R2** log₁₀ GDP gives clearly lower MAE: the relationship is roughly linear in log income.
* **R3** Festival flags must be built from the BS calendar dates for each year; last week's price usually dominates.
