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
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. Train 0.5 / test 6.0 → overfit. Train 4.0 / test 4.1 with noise SD 1 → underfit (both errors far above the noise).
2. Validation once; training 4 times.
3. More data; regularisation; limits on complexity (tree depth, larger *k*); fewer features; early stopping.
4. k = 1 gives very high training accuracy and lower validation accuracy (overfit); very large *k* approaches the
   baseline (underfit); the best region is moderate *k* — with this weak synthetic signal differences are small.
5. 5-fold CV accuracy (all 1,500 rows): depth 1 0.609 ± 0.029, 2 0.604, 3 0.608, 5 0.602, 10 0.573, unlimited 0.553. The
   one-SE rule picks **depth 1** (a single split — on visits).
6. With noise SD 0.5, degrees 2–5 all reach ≈ 0.53–0.55 test RMSE (near the noise); degree 8 still overfits (2.17).
   Less noise lets moderate complexity do well; the noise floor drops.
7. At 11 bags/ha: degree 2 predicts ≈ 5.3 (truth 4.6); degree 8 predicts ≈ 64 — absurd. Never extrapolate complex
   fits.
8. Bias: systematic error from a too-simple shape (degree 1 always misses the bend). Variance: sensitivity to the
   particular sample (degree 12 changes wildly between samples). Total error balances both.
9. Choosing among 1,000 options on the test set picks one that was lucky there; 71% is optimistic. They needed a
   validation set or nested cross-validation, and one untouched test set.
10. Ridge with degree-8 features (scaled): CV RMSE ≈ 2.22 (alpha 0.001), 2.15 (0.1), 2.12 (1), 2.14 (10), 2.58 (100) —
    moderate regularisation tames the wiggles; too much makes it underfit.

Lesson 2: the single validation split picks degree 6 (2.25) over degree 2 (2.32); 5-fold CV picks degree 2 (2.06). Refit
degree 2 on 40 trials: test RMSE 2.12; peak at about 3.5 bags/ha. Make (200 training trials): degree-8 test RMSE falls
to ≈ 2.1.

## Real-data exercises: notes
* **R1** Degrees 2–4 usually generalise; a seasonal model `a + b·sin(2πm/12) + c·cos(2πm/12)` uses only 3 parameters and
  matches the cyclic shape.
* **R2** A straight line on log income is hard to beat; high degrees flail at the extremes.
* **R3** Shallow trees (depth 2–4) are near-perfect for penguins.
