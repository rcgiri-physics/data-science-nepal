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
