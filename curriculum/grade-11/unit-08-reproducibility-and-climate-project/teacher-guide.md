# Teacher guide — Grade 11, Unit 8: Reproducibility, Git and the climate project

**Time:** 3 lessons + project (about 5 periods). **Track:** B (project).

| # | Lesson | Time |
|---|---|---|
| 1 | Git basics | 40–45 min |
| 2 | Seeds, environments, notes | 40–45 min |
| 3 | Project: analyse and publish | 40–45 min |
| P | Unit project: Climate or weather? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/climate_project.ipynb`; Git installed (https://git-scm.com).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Practise 'commit messages' on paper by describing each change in one line.

## Common misconceptions
* Saving as final_v2_REAL_final.ipynb is version control.
* Setting a seed makes a result true; it only makes it repeatable.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Git basics**
1. What does git commit record?  
   *Answer:* A snapshot with a message.
2. Why write clear messages?  
   *Answer:* So you know what and why later.
3. Which command shows changes waiting?  
   *Answer:* git status.

**Lesson 2: Seeds, environments, notes**
1. Why set a seed?  
   *Answer:* So random results can be repeated.
2. What else affects reproducibility?  
   *Answer:* Library/Python versions and data versions.
3. Does a seed make a result correct?  
   *Answer:* No: only repeatable.

**Lesson 3: Project: analyse and publish**
1. What proves it is reproducible?  
   *Answer:* Someone else reruns it and gets the same results.
2. What goes in the limits?  
   *Answer:* Synthetic data, one series, short period, weather vs climate.
3. What do you disclose?  
   *Answer:* AI help used, data licence and source.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics (⚠️ unit numbers to be added after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
