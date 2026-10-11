# Teacher guide — Grade 8, Unit 3: Collecting and recording

**Time:** 3 lessons + project (about 5 periods). **Track:** A (no-code).

| # | Lesson | Time |
|---|---|---|
| 1 | Consent and privacy | 40–45 min |
| 2 | Tally and frequency | 40–45 min |
| 3 | A tidy table | 40–45 min |
| P | Unit project: Collect our class data | 2 periods |

## Before you start
* Materials: Tally sheets, printed consent line, class roll for codes.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
All eight units run on paper, calculators and the blackboard. Computers are optional (spreadsheet or CODAP, https://codap.concord.org); every activity below has a paper version.

## Common misconceptions
* Writing names 'for convenience'. Use codes: even small classes can embarrass or expose people.
* Mixing units in a column (minutes and hours).

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Consent and privacy**
1. Why do we use codes instead of names?  
   *Answer:* To protect privacy and avoid embarrassment.
2. What should a consent statement say?  
   *Answer:* Why we collect, how we will use it, and that saying no is fine.
3. Is it ok to publish a table of each student's weight with names?  
   *Answer:* No.

**Lesson 2: Tally and frequency**
1. Tally for 7 is…  
   *Answer:* |||| || (one group of five plus two).
2. In a frequency table the counts must add to…  
   *Answer:* The total number of students asked.
3. Frequencies: walk 12, bus 5, cycle 3. How many students?  
   *Answer:* 20.

**Lesson 3: A tidy table**
1. Why should every value in travel_minutes use minutes?  
   *Answer:* Mixed units can't be compared or averaged.
2. What should one row be in our class table?  
   *Answer:* One student (by code).
3. A blank cell means…  
   *Answer:* Missing: record it as missing and mention it; don't guess.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Extends the Grade 8 compulsory Maths statistics chapter (pie chart, mean, median, mode) with question-forming, data collection and interpretation.

## Answers: practice exercises
1. 4 = `||||` · 9 = `卌 ||||` · 13 = `卌 卌 |||`.
2. Must include: who is asking, why, what is recorded (with codes), who sees it, that "no" is fine.
3. 36 students; Maths 12/36 ≈ 33%.
4. A: 18/30 = 60%; B: 21/42 = 50%. Class A has the bigger share although B has more walkers.
5. 135–139: 1 · 140–144: 3 · 145–149: 3 · 150–154: 2 · 155–159: 4 · 160–164: 2 · 165–169: 2 · 170–174: 1 ·
   total 18.
6. Example: (A) 8, 06:00 · (B) 7.5, 05:30 · (C) 8, 06:00 (assumed 10 pm to 6 am) · (D) NA, NA. Assumptions:
   "up at 6" is 6 am; C's sleep is calculated, not reported.
7. A 0 is a real value and pulls the mean down. Example: 2, 3, 4 and a missing → mean of 2, 3, 4 = 3; with a false
   0 the mean becomes 9 ÷ 4 = 2.25.
8. Yes: the only Rai student who comes by motorbike is identifiable by anyone who knows the class. Remove or
   combine the ethnicity column (or merge small groups into "other") before sharing; share only what the question
   needs.
9. (i) "main mode" column (the mode used for the longest part): simple, one value per cell. (ii) two columns,
   `walk_minutes` and `bus_minutes`: keeps full information. (Or a yes/no column for each mode.)
10. e.g. codes not names; only the nurse/teacher holds the key; results reported only for groups of ≥ 5; paper
    destroyed after use; parents' consent.

## Real-data exercises: notes
* **R1** With the link as written (Apr–Dec 2015, M ≥ 4, Nepal box) expect ≈ 300 events. On 2026-10-11 the file had
  304: 4.0–4.4: 185 · 4.5–4.9: 82 · 5.0–5.4: 26 · 5.5–5.9: 5 · ≥ 6.0: 6 (7.8 on 25 April, 7.3 on 12 May, plus 6.1,
  6.3, 6.6, 6.7). Counts change slightly if USGS revises
  the catalogue; that is fine. Offer the fallback freely.
* **R2** The station table is wide (one column per year), so it breaks "one column per variable" (year is a
  variable). Missing years may be blank or marked with a symbol; discuss. Grade 9 Unit 1 tidies exactly this kind of
  table.
* **R3** Check consent statements before students start.
