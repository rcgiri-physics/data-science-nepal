# Teacher guide — Grade 12, Unit 6: Feature engineering

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Creating features | 40–45 min |
| 2 | Encoding categories | 40–45 min |
| 3 | Comparing feature sets honestly | 40–45 min |
| P | Unit project: Feature challenge | 2 periods |

## Before you start
* Materials: Notebook `notebooks/features.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Brainstorm features on cards for predicting 'will a student reach school late?'.

## Common misconceptions
* More features is always better.
* Features using future information (leakage).

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Creating features**
1. Name a ratio feature.  
   *Answer:* e.g. people per school.
2. What is an interaction?  
   *Answer:* A product of two features capturing a joint effect.
3. Why use domain knowledge?  
   *Answer:* It suggests meaningful features.

**Lesson 2: Encoding categories**
1. One-hot of 3 categories makes…  
   *Answer:* 3 columns of 0/1.
2. Why not 1, 2, 3?  
   *Answer:* It implies order and distance that aren't real.
3. What is get_dummies?  
   *Answer:* A pandas function for one-hot encoding.

**Lesson 3: Comparing feature sets honestly**
1. Why 5-fold CV?  
   *Answer:* It averages over several splits to reduce luck.
2. What is leakage in features?  
   *Answer:* Using information that won't be available at prediction time.
3. Pick the simplest set that is…  
   *Answer:* About as good as the best.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics (⚠️ add unit numbers after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
