# Teacher guide — Grade 10, Unit 5: What is a model? (and a first look at machine learning)

**Time:** 3 lessons + project (about 5 periods). **Track:** A then B.

| # | Lesson | Time |
|---|---|---|
| 1 | Unplugged: models from cards | 40–45 min |
| 2 | Code: k-NN and a baseline | 40–45 min |
| 3 | Limits and misuse | 40–45 min |
| P | Unit project: Model vs baseline | 2 periods |

## Before you start
* Materials: Printed 30-card training set (visits, wealth → delivery in a facility); notebook `notebooks/knn_intro.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
The unplugged lesson is the heart of this unit: do k-NN on a printed grid with cards and coloured pins.

## Common misconceptions
* Models understand; they only find patterns in past data.
* High accuracy on training data means a good model; test on unseen data.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Unplugged: models from cards**
1. What is training data?  
   *Answer:* Examples the model learns from.
2. Why keep test data hidden?  
   *Answer:* To check it works on cases it has not seen.
3. Which cards are 'nearest'?  
   *Answer:* The ones with the closest values on the features.

**Lesson 2: Code: k-NN and a baseline**
1. What is a baseline?  
   *Answer:* A very simple rule to beat, e.g. always the majority.
2. Why test on unseen data?  
   *Answer:* Training accuracy can flatter the model.
3. k = 1 problem?  
   *Answer:* Follows noise; may overfit.

**Lesson 3: Limits and misuse**
1. Can a model be unfair?  
   *Answer:* Yes: it can copy bias in the training data.
2. Name a high-stakes use needing caution.  
   *Answer:* e.g. health care, loans, scholarships.
3. Who should decide?  
   *Answer:* People accountable for the outcome, not the model alone.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.
