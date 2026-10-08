# Teacher guide — Grade 11, Unit 4: Is the difference real? Permutation tests

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | The idea of chance | 40–45 min |
| 2 | Run a permutation test | 40–45 min |
| 3 | Interpreting results honestly | 40–45 min |
| P | Unit project: Chance or real? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/permutation.ipynb`; cards for the unplugged version.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Write group labels on cards, shuffle, deal into two piles, record the difference; repeat 20 times.

## Common misconceptions
* A small p-value shows the difference is big or important (it doesn't).
* A large p-value proves no difference.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: The idea of chance**
1. What does shuffling labels imitate?  
   *Answer:* Groups being interchangeable (no real difference).
2. What do we compare to?  
   *Answer:* The observed difference.
3. What is chance variation?  
   *Answer:* Differences that arise from random assignment alone.

**Lesson 2: Run a permutation test**
1. p-value = ?  
   *Answer:* Share of shuffled differences as extreme as the observed.
2. Why 5,000 shuffles?  
   *Answer:* More shuffles give a steadier estimate.
3. What does a tiny p-value suggest?  
   *Answer:* Chance alone rarely produces such a difference.

**Lesson 3: Interpreting results honestly**
1. Does small p show a large effect?  
   *Answer:* No: check the effect size.
2. Does large p show no difference?  
   *Answer:* No: maybe too little data.
3. What else to report?  
   *Answer:* Effect size, interval, how data were collected.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.
