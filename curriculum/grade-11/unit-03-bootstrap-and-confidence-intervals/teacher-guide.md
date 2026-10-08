# Teacher guide — Grade 11, Unit 3: Uncertainty: bootstrap and confidence intervals

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Sampling variation | 40–45 min |
| 2 | The bootstrap | 40–45 min |
| 3 | Interpreting intervals | 40–45 min |
| P | Unit project: How sure are we? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/bootstrap.ipynb`; bag of numbered slips for the unplugged version.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Write 20 values on slips, draw with replacement 20 times, compute the mean; repeat 10 times; plot the means.

## Common misconceptions
* A 95% interval means 95% of data lie inside it. It describes the uncertainty of the estimate.
* Bootstrapping creates new information; it only reveals variability of this sample.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Sampling variation**
1. Will two samples give the same mean?  
   *Answer:* Usually not.
2. Bigger sample → ?  
   *Answer:* Less variation in the estimate.
3. What causes the difference?  
   *Answer:* Chance in who ends up in each sample.

**Lesson 2: The bootstrap**
1. 'With replacement' means…  
   *Answer:* Each draw is put back, so items can repeat.
2. What do we compute each time?  
   *Answer:* The statistic (e.g. mean).
3. Middle 95% gives…  
   *Answer:* A 95% bootstrap interval.

**Lesson 3: Interpreting intervals**
1. Which is narrower, n=25 or n=400?  
   *Answer:* n = 400.
2. Does a narrow interval fix a biased sample?  
   *Answer:* No.
3. Is a 95% interval where 95% of the data lie?  
   *Answer:* No: it concerns the uncertainty of the estimate.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.
