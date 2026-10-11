# Teacher guide — Grade 12, Unit 3: Evaluation metrics

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | The confusion matrix | 40–45 min |
| 2 | Precision, recall, F1 | 40–45 min |
| 3 | Choosing a threshold | 40–45 min |
| P | Unit project: Choose the threshold | 2 periods |

## Before you start
* Materials: Notebook `notebooks/metrics.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Fill a 2×2 table with counts using bean seeds or tally marks.

## Common misconceptions
* High accuracy = good model (especially with imbalanced classes).
* Precision and recall are the same thing.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: The confusion matrix**
1. False negative means…  
   *Answer:* The model said 'no' but the truth was 'yes' (a missed case).
2. False positive means…  
   *Answer:* The model said 'yes' but the truth was 'no'.
3. Rows+columns sum to…  
   *Answer:* The total number of cases.

**Lesson 2: Precision, recall, F1**
1. Precision formula?  
   *Answer:* TP ÷ (TP + FP).
2. Recall formula?  
   *Answer:* TP ÷ (TP + FN).
3. Why can accuracy mislead?  
   *Answer:* With rare positives, always saying 'no' scores high but finds nobody.

**Lesson 3: Choosing a threshold**
1. Lower threshold → recall?  
   *Answer:* Rises (and precision usually falls).
2. Who decides the costs?  
   *Answer:* People responsible, with affected communities.
3. What capacity limit matters?  
   *Answer:* How many cases can actually be followed up.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. Accuracy 170/200 = 0.85; precision 40/50 = 0.80; recall 40/60 = 0.667; specificity 130/140 = 0.929; F1 = 0.727.
2. FP: warning but no flood (people evacuate needlessly; trust falls). FN: flood without warning (lives and property at
   risk) — usually worse, but too many false alarms make people ignore warnings.
3. It measures how sensitive the test is to the condition: the share of people who have it that the test detects.
4. Precision 20/50 = 0.40; recall 20/30 = 0.667.
5. Lowest threshold with precision ≥ 0.6 is about 0.61, giving recall ≈ 0.46.
6. It predicts "facility" for everyone, so TP = 0 → recall 0; its accuracy on this test set is 0.461 (only 46% delivered in
   a facility here).
7. Recall at 0.5: Hill 0.789 (95 home deliveries), Mountain 0.739 (23), Terai 0.774 (84). Mountain is lowest but based on
   only 23 women — watch it, collect more data (Unit 5).
8. The second: with fixed capacity, what matters is how many of the 120 visits reach the right women (precision at
   top-*k*). Accuracy averages over everyone, including those who will never be visited.
9. With FN cost ≥ 2 × FP cost, the cheapest threshold in 0.30–0.75 is 0.30 (flag almost everyone): the model is weak, so
   visiting everyone is cheapest if capacity allowed. A real lesson: sometimes the best "model" is universal coverage.
10. 10,000 people, 100 infected: test finds ~99 of them (if sensitivity 99%) and wrongly flags 1% of 9,900 ≈ 99 healthy
    people. So about half of positive results are false positives.

Lesson 2 step 2: the low-birth-weight model's highest predicted probability is ≈ 0.40, so at threshold 0.5 it predicts
no low birth weights: recall 0. Lesson 3: top 60 → precision 0.733, recall 0.218; top 120 → 0.617, 0.366; top 240 →
0.579, 0.688.

## Real-data exercises: notes
* **R1** Chinstrap is ≈ 20% of penguins; bill length + depth separate it well, so high recall is achievable with good
  precision.
* **R2** Magnitude ≥ 5 events are a small share of catalogue events; "always no" has high accuracy.
* **R3** Farmer: low threshold (high recall for rain). School: higher threshold (high precision).
