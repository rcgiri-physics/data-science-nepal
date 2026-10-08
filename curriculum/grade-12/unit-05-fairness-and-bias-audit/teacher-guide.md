# Teacher guide — Grade 12, Unit 5: Fairness and bias audit

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code + discussion).

| # | Lesson | Time |
|---|---|---|
| 1 | Where bias comes from | 40–45 min |
| 2 | Audit by group | 40–45 min |
| 3 | Responding and reporting | 40–45 min |
| P | Unit project: Audit memo | 2 periods |

## Before you start
* Materials: Notebook `notebooks/fairness_audit.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Case cards: loans, scholarships, hospital triage — who is missed?

## Common misconceptions
* Removing the sensitive column makes the model fair (proxies remain).
* There is one correct definition of fairness.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Where bias comes from**
1. Name two sources of bias.  
   *Answer:* e.g. unrepresentative data; labels reflecting past unfairness; measurement differences.
2. Is bias only a coding problem?  
   *Answer:* No: it begins with data and decisions.
3. Who should be involved in checking?  
   *Answer:* Affected communities as well as technical people.

**Lesson 2: Audit by group**
1. Why show group sizes?  
   *Answer:* Small groups make estimates noisy.
2. Selection rate is…  
   *Answer:* The share predicted 'yes' in a group.
3. What gap matters most?  
   *Answer:* The one linked to the harm of the decision.

**Lesson 3: Responding and reporting**
1. Can you always 'fix' bias with a tweak?  
   *Answer:* No: sometimes the answer is not to use the model.
2. Why keep humans in the loop?  
   *Answer:* To catch errors and take responsibility.
3. What must the memo include?  
   *Answer:* Findings, limits and recommendations.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics (⚠️ add unit numbers after the NEB syllabus is read; see docs/for-cdc/competency-map.md).
