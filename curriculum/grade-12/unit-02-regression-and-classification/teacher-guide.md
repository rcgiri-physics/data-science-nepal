# Teacher guide — Grade 12, Unit 2: Regression and classification

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Regression: predicting a number | 40–45 min |
| 2 | Classification: predicting a category | 40–45 min |
| 3 | Choosing and explaining | 40–45 min |
| P | Unit project: Explain a prediction | 2 periods |

## Before you start
* Materials: Notebook `notebooks/reg_class.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
ML concepts can be taught with cards (Grade 10 Unit 5) and printed confusion matrices. Code lessons need a lab day; the capstone can be done with spreadsheets and a decision rule, but call that 'a simple rule', not 'a model'.

## Common misconceptions
* Logistic regression predicts a class directly (it predicts a probability first).
* Bigger coefficient = more important if scales differ.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Regression: predicting a number**
1. Regression predicts…  
   *Answer:* A number.
2. Coefficient 0.05 for visits means…  
   *Answer:* +0.05 kg per extra visit, other features fixed.
3. Same as Grade 11 least squares?  
   *Answer:* Yes: same line.

**Lesson 2: Classification: predicting a category**
1. Probability range?  
   *Answer:* 0 to 1.
2. What turns a probability into a class?  
   *Answer:* A threshold.
3. Who chooses the threshold?  
   *Answer:* People, based on costs of different mistakes.

**Lesson 3: Choosing and explaining**
1. Predict rainfall in mm: type?  
   *Answer:* Regression.
2. Predict 'pass/fail': type?  
   *Answer:* Classification.
3. Why favour explainable models?  
   *Answer:* People affected deserve to understand decisions.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. (a) regression (count; Poisson-type models later) (b) classification (c) regression (d) multi-class classification.
2. z = 0 → 0.5; z = 2 → 1 ÷ (1 + e^−2) ≈ 0.88; z = −2 → ≈ 0.12.
3. Odds 3 = p ÷ (1 − p) → p = 3 ÷ 4 = 0.75.
4. z = −1.593 + 0.345 × 4 + 0.088 × 3 ≈ 0.05 → p ≈ 0.51.
5. 1.41² ≈ 1.99 (about double the odds); 1.41⁴ ≈ 3.97.
6. Linear predictions range from about 0.15 to 0.73 on this test set — inside 0–1 here only because the features are
   limited; with stronger features it would go outside. Logistic regression always gives valid probabilities and
   models the S-shaped relationship.
7. MAE 0.334 kg, RMSE 0.422 kg; RMSE squares errors, so a few large misses raise it more.
8. Depth 2: test accuracy 0.576, 4 leaves — and its rules reduce to "4 or more visits → facility" (the Grade 10 rule!).
   Depth 10: 0.579 with 35 leaves. Same accuracy; give the health post the depth-2 version.
9. The model's uncertainty is large; 0.49 and 0.51 are practically the same. Better: a "grey zone" (e.g. 0.4–0.6)
   reviewed by a person, or decisions based on several pieces of information; always allow appeal.
10. e.g. "In our records, babies of mothers who had more check-ups during pregnancy, and from better-off families,
    weighed a little more at birth — about 60 grams more for each extra check-up. But these two things explain only a
    small part of why babies differ, so we cannot predict any one baby's weight well. The data are invented for teaching."

Lesson 1 Make: quintile 3, 5 visits → ≈ 3.01 kg (± about 0.33 kg typical error). Adding age and belt dummies leaves
test MAE at ≈ 0.335 kg — no improvement. Lesson 2: flagged counts at thresholds 0.3/0.4/0.5/0.6 = 34/151/270/343 of
375; for 120 visits, a threshold just under 0.4 (check the exact count).

## Real-data exercises: notes
* **R1** Flipper length explains most of the variation in body mass (R² ≈ 0.75); species classification ≈ 0.95+.
* **R2** Nepal typically sits near the decision boundary; a good discussion of what a "probability" means for a
  country.
* **R3** A farmer spraying expensive pesticide that rain would wash off wants high precision for "no rain".
