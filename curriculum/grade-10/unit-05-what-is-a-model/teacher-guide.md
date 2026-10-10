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

## Answers: practice exercises
1. (a) features humidity, pressure; label rain tomorrow (yes/no) → classification. (b) features area, location; label
   price → regression.
2. Baseline 150/200 = 75%; model 160/200 = 80%: 5 percentage points better.
3. √(3² + 4²) = 5.
4. Distances from (2, 2): B 1.0, A 1.41, E 1.41, C 2.83, D 3.61. k = 1 → B → ✘. k = 3 → B ✘, A ✘, E ✔ → ✘.
5. It is just a row number with no meaning; any "pattern" it finds is accidental (or reflects how the file was
   sorted), so it hurts predictions on new cases.
6. The test set was used to choose *k*, so it is no longer unseen; 0.66 is optimistically biased. Split the training
   rows into train/validation, choose *k* on validation, then report test accuracy once.
7. Training: baseline 0.558, rule 0.596; test: baseline 0.563, rule 0.660. The rule happens to do better on the test
   rows — with 300 cases, a few points of luck either way is normal.
8. Unscaled age: k = 15 → 0.62, k = 25 → 0.593; age ÷ 5: both 0.62. Age adds little information here and, unscaled,
   dominates the distance; scaling reduces its influence.
9. When the mistakes of the "more accurate" model fall on the most vulnerable group, or when the mistake it makes is the
   costly one (missing a high-risk mother), or when it can't be explained or audited.
10. k = 15 accuracy by belt (test rows): Hill 0.620 (142), Mountain 0.636 (22), Terai 0.662 (136). Mountain is based on
    only 22 cases — very uncertain.

## Real-data exercises: notes
* **R1** Bill length + flipper length separate the three species well: k-NN test accuracy typically ≈ 0.9+, baseline
  (Adelie) ≈ 0.44. Scaling matters (flipper mm range ~60, bill mm ~30).
* **R2** "Same as today" is a strong baseline for weather; in the monsoon, rain follows rain. A simple model may
  barely beat persistence — a good honest result.
* **R3** Census 2021: Mountain ≈ 6%, Hill ≈ 40%, Terai ≈ 54% of the population (check). The synthetic table has 10%
  Mountain, 46% Hill, 43% Terai — over-represents Mountain and Hill, under-represents Terai.
