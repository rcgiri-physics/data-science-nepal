# Teacher guide — Grade 12, Unit 8: Capstone with a community client

**Time:** 3 lessons + project (about 5 periods). **Track:** B/A (project).

| # | Lesson | Time |
|---|---|---|
| 1 | Scope and agree | 40–45 min |
| 2 | Build and audit | 40–45 min |
| 3 | Hand over and publish | 40–45 min |
| P | Unit project: Community capstone | 2 periods |

## Before you start
* Materials: Capstone kit in `curriculum/grade-12/capstone-kit/` (client brief, data agreement, model card, rubric); notebook `notebooks/capstone_template.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
A capstone with a simple rule and a printed table is acceptable; call it a 'simple rule' not a model.

## Common misconceptions
* Capstone = biggest model. It is the most useful, honest answer to the client's question.
* Student data from real people can be shared freely.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Scope and agree**
1. What does a data agreement cover?  
   *Answer:* Purpose, consent, storage, sharing, deletion.
2. Why define success first?  
   *Answer:* Otherwise we can't tell if the work helped.
3. May you share a client's data publicly?  
   *Answer:* Only if the agreement says so.

**Lesson 2: Build and audit**
1. What goes in a model card?  
   *Answer:* Purpose, data, performance, limits, groups affected.
2. What is the client's 'current way'?  
   *Answer:* The practice your model must beat.
3. Why audit before handover?  
   *Answer:* To avoid harm to under-served groups.

**Lesson 3: Hand over and publish**
1. What must be anonymised before publishing?  
   *Answer:* Anything identifying people or families.
2. What goes in the README?  
   *Answer:* How to rerun, data sources, versions, contacts.
3. Whose consent is required?  
   *Answer:* The client, data owners and guardians where students appear.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics.

## Answers: practice exercises
1. e.g. "Which Grade 9 students should be offered the Saturday maths support class next term, using last term's
   anonymised test scores and attendance? Deliverable: a ranked list template and a one-page rule, by Week 6."
2. Purpose; data fields and period (minimum necessary); consent; storage and access; sharing/publishing; deletion; output
   ownership/licence (any five).
3. More visits always find more people; comparing at different capacities confuses "better ranking" with "more work".
4. Seeds 7/1/2/3: the rule and the model are within about 0.01–0.02 of each other in precision and recall every time;
   tell the client the simple rule is as good, easier to explain and needs no computer.
5. Not for deciding who receives care or supplies; not for women outside the district/period of the data; not as an
   assessment of individual mothers; not to reduce visits for anyone already scheduled; not for insurance or loans.
6. Do not open/forward it; ask the client to delete it from chats; explain the agreement (only anonymised extracts via the
   agreed route); inform the teacher; record the incident.
7. A printed one-page rule and ranked-list template, a simple spreadsheet that works offline, instructions in Nepali, a
   paper backup — no dependence on internet or the students' laptops.
8. Recommend using the model only with a safeguard for Mountain-belt women (e.g. the current rule continues for them, or
   extra review), collect more Mountain data, re-audit after three months; state the gap openly in the model card.
9. Decline: it exposes and could shame identifiable households, goes beyond the agreed purpose and violates privacy and
   the class data charter; offer an aggregated, anonymised summary (e.g. payment rate by ward) if the client needs it.
10. Re-audit every 3–6 months and after any change (new road, new facility, new data system); stop if precision/recall
    drop below the current rule or group gaps widen; the health post in-charge decides, with a named maintainer.

Lesson 2 (seed 7): current rule 301 visits, precision 0.618, recall 0.741; model at same capacity 0.611 / 0.733.

## Real-data exercises: notes
* **R1** Approve the "client" and question; public data still need credits and licence checks.
* **R2** If the gallery is empty, use published case studies from Nepali data organisations.
* **R3** A complete synthetic run-through is a valid capstone for schools where no client is available; mark it with the
  same rubric but note the limits.
