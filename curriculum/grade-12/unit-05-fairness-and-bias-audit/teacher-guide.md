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
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. Selection rate: the share of the group the model flags. Recall: of the group members who really are positive, the
   share the model flags.
2. Surname (often indicates caste/ethnicity), home village or ward, mother tongue, school attended, type of house.
3. Few positives: one or two cases more or less change the percentage a lot; intervals are wide.
4. A: 54/60 = 0.90; B: 6/12 = 0.50. The gap looks large, but B's recall rests on 12 cases (bootstrap interval roughly
   0.2–0.8) — investigate and collect more data before concluding; still worth flagging.
5. Adding belt dummies: overall recall 0.78; Mountain recall 1.0 (only 37 positives, very uncertain), Terai drops to 0.68;
   quintile gap remains (q4 0.60, q5 0.60). Changing features shifts who is missed.
6. Threshold 0.4 for quintiles 4–5: flagged rises from 400 to 462; recall q4 0.83, q5 0.92 (others unchanged). Needs
   agreement from the health office, health workers and community representatives — and capacity for 62 more visits.
7. False positive rate by quintile (threshold 0.5): q1 0.78, q2 0.73, q3 0.64, q4 0.49, q5 0.37 — poorer women get the
   most unnecessary visits. Usually a small harm (time), possibly a benefit (a health visit), but could feel intrusive.
8. Base rates differ (q1 0.62 vs q5 0.43). Equal selection rates would flag the same share in each quintile, which forces
   either more misses where need is higher or more false alarms where it is lower; equal recall then requires different
   selection rates.
9. Flagged students get help and stay, so the new data show "flagged-type" students not dropping out; the retrained model
   learns these features are low-risk and stops flagging them — help is withdrawn from exactly the students it worked
   for. Record interventions and evaluate them separately.
10. Facility records miss women who never reached a facility (home births without any contact), remote areas with poor
    record keeping, migrants and women without documents; they over-represent women near facilities.

Lesson 2 step 4: a visits-only model gives identical predictions here (400 flagged, same recall by quintile) — visits are
a proxy for wealth.

## Real-data exercises: notes
* **R1** Biscoe island has mostly Gentoo; errors (if any) concentrate between Adelie and Chinstrap on Dream island.
* **R2** Census 2021: Mountain ≈ 6% of population vs ≈ 10% of synthetic records; Terai ≈ 54% vs 43%.
* **R3** The COMPAS debate is the classic example that predictive parity and equal error rates conflict when base rates
  differ.
