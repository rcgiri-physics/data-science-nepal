# Teacher guide — Grade 12, Unit 1: The machine-learning workflow

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Define the task | 40–45 min |
| 2 | Split and baseline | 40–45 min |
| 3 | Train, compare, test | 40–45 min |
| P | Unit project: Workflow report | 2 periods |

## Before you start
* Materials: Notebook `notebooks/ml_workflow.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
ML concepts can be taught with cards (Grade 10 Unit 5) and printed confusion matrices. Code lessons need a lab day; the capstone can be done with spreadsheets and a decision rule, but call that 'a simple rule', not 'a model'.

## Common misconceptions
* Evaluate on the training data.
* Tune on the test set (then it is no longer 'unseen').

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Define the task**
1. What is the label?  
   *Answer:* The thing we want to predict.
2. What are features?  
   *Answer:* The inputs used to predict.
3. Why describe the decision?  
   *Answer:* A good model for the wrong decision can still harm.

**Lesson 2: Split and baseline**
1. Which set do we use to choose between models?  
   *Answer:* Validation.
2. Which set do we use only once?  
   *Answer:* Test.
3. Accuracy of always predicting the majority class is…  
   *Answer:* The baseline.

**Lesson 3: Train, compare, test**
1. What is data leakage?  
   *Answer:* Information from outside the training data (e.g. test rows) influencing training.
2. Why use a pipeline?  
   *Answer:* It keeps preprocessing inside training only.
3. What if the model barely beats baseline?  
   *Answer:* It adds little; reconsider features or the task.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics (⚠️ add unit numbers after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
