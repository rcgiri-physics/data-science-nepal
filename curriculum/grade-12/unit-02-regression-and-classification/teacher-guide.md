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
