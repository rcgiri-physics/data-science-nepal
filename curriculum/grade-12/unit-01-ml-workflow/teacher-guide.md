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
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. Label: crop failure (yes/no). Features: soil type, soil moisture at planting, variety, previous year's yield (known at
   planting); season rainfall and pest outbreaks are known only later — using them for a planting-time decision is
   leakage.
2. 1,400 / 300 / 300.
3. So each set has the same share of each class; otherwise a small or rare class might be under-represented by chance,
   distorting scores.
4. Decision: who gets extra classes; label: SEE GPA below a threshold; features known at decision time (Grade 9–10
   marks, attendance); must not: exclude students from opportunities, publish predictions, or label students in front of
   others; predictions add support, never remove it.
5. Maybe not: with 300 cases the standard error of an accuracy near 0.6 is about √(0.6 × 0.4 / 300) ≈ 0.028, so 5 points
   is under two SEs. Bootstrap the validation set or use cross-validation.
6. The scaler used means/SDs from validation and test rows; the model indirectly saw information about them, so scores
   are slightly optimistic.
7. Validation accuracy: k = 5 → 0.607 (train 0.724), 15 → 0.550, 25 → 0.577, 51 → 0.577. The differences are within
   noise; a larger *k* (25–51) gives a smaller train–validation gap and is safer. Point out how jumpy validation scores
   are with 300 cases.
8. Treat the test score as contaminated; report validation/cross-validation results honestly, and if possible collect a
   fresh test set (or hold out new data collected later).
9. Tomorrow's air depends on today's; a random split puts days from the same week in train and test, so the model
   "knows" the answer from neighbours; and in practice you always predict the future from the past.
10. 5-fold CV on the 1,200 non-test rows: logistic regression 0.600 ± 0.016 vs baseline 0.558 — the same conclusion (a
    small, consistent gain), with a sense of variability.

Lesson 2 Make: the "visits ≥ 4" rule scores 0.61 on validation — as good as any model. Lesson 3 leakage: adding
`birth_weight_kg` changes test accuracy little here (0.59) because the synthetic generator barely links them — but it
would still be wrong, because the feature is not available when the decision is made.

## Real-data exercises: notes
* **R1** Penguins: logistic regression and k-NN reach ≈ 0.95+; baseline ≈ 0.44. Remove rows with missing values first.
* **R2** Persistence is a strong baseline in the monsoon; time-based splits often show seasonal changes in difficulty.
* **R3** Many good answers conclude that a simple rule or better record-keeping is more useful than ML.
