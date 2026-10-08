# Teacher guide — Grade 12, Unit 4: Overfitting and generalising

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Underfitting and overfitting | 40–45 min |
| 2 | Choosing complexity with validation | 40–45 min |
| 3 | Simple can win | 40–45 min |
| P | Unit project: Find the sweet spot | 2 periods |

## Before you start
* Materials: Notebook `notebooks/overfitting.ipynb` (generates its own noisy curve).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Fit a wiggly line vs a straight line through 8 points on paper, then test with 8 new points.

## Common misconceptions
* More complex = more accurate.
* Zero training error is the goal.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Underfitting and overfitting**
1. Training error with more complexity…  
   *Answer:* Falls (or stays equal).
2. Test error with too much complexity…  
   *Answer:* Rises (overfitting).
3. What is noise?  
   *Answer:* Random variation unrelated to the pattern.

**Lesson 2: Choosing complexity with validation**
1. Which data choose complexity?  
   *Answer:* Validation data.
2. Why not test data?  
   *Answer:* It would no longer be unseen.
3. What is cross-validation?  
   *Answer:* Repeating train/validation splits to average the error.

**Lesson 3: Simple can win**
1. When do simple models shine?  
   *Answer:* With little or noisy data.
2. Why prefer explainable models in public service?  
   *Answer:* People can check and challenge decisions.
3. Is overfitting only a polynomial problem?  
   *Answer:* No: all flexible models can overfit.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics (⚠️ add unit numbers after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
