# Teacher guide — Grade 8, Unit 1: What is data?

**Time:** 3 lessons + project (about 5 periods). **Track:** A (no-code).

| # | Lesson | Time |
|---|---|---|
| 1 | Data are everywhere | 40–45 min |
| 2 | Who collects Nepal's data? | 40–45 min |
| 3 | Reading a table | 40–45 min |
| P | Unit project: My data portrait | 2 periods |

## Before you start
* Materials: 20 cards per group (see worksheets/w1-sort-cards.md), printed table (worksheets/w2-read-a-table.md), pencils.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
All eight units run on paper, calculators and the blackboard. Computers are optional (spreadsheet or CODAP, https://codap.concord.org); every activity below has a paper version.

## Common misconceptions
* "Ward number is a number so I can average it." It is a label (categorical): arithmetic on it has no meaning.
* Confusing a *row* (one student) with a *column* (one variable).
* Thinking data must be numbers; names and colours are data too.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Data are everywhere**
1. Is 'favourite colour' numerical or categorical?  
   *Answer:* Categorical.
2. Give one numerical variable about your school.  
   *Answer:* Any measured/counted one, e.g. number of students in Grade 8.
3. Why is a ward number categorical even though it looks like a number?  
   *Answer:* It is a label; adding or averaging ward numbers means nothing.

**Lesson 2: Who collects Nepal's data?**
1. Which organisation runs the national census?  
   *Answer:* The National Statistics Office (NSO) of Nepal.
2. Why should we ask 'who collected this data and why'?  
   *Answer:* Purpose and method affect what is included and whether we can trust it.
3. Name one thing a school could measure itself.  
   *Answer:* e.g. daily attendance, rainfall in a rain gauge, travel time.

**Lesson 3: Reading a table**
1. A table has columns: student_code, travel_mode, travel_minutes, height_cm. How many variables?  
   *Answer:* 4 (student_code is an ID; 3 are real variables).
2. Which of those are numerical?  
   *Answer:* travel_minutes and height_cm.
3. What does one row represent?  
   *Answer:* One student.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Extends the Grade 8 compulsory Maths statistics chapter (pie chart, mean, median, mode) with question-forming, data collection and interpretation.

## Answers: practice exercises
1. (a) categorical (b) numerical (c) categorical (d) numerical (e) categorical: a label (f) numerical.
2. (b) measurement · (d) count · (f) measurement.
3. (a) Ministry of Culture, Tourism and Civil Aviation / Department of Tourism (also Nepal Tourism Board);
   (b) Department of Hydrology and Meteorology; (c) Nepal Rastra Bank (NSO also publishes price indices).
4. Three formats and two calendars: they cannot be compared or averaged. Better: "Age in completed years: ___" or
   ask for date of birth in one stated calendar (BS or AD) and calculate.
5. Check: codes not names; one row per person; units written (cm, minutes, years).
6. Marks can be averaged; divisions cannot (the "average" of First and Second Division is meaningless). Divisions
   do have an order (Distinction > First > Second), so they are **ordinal** categorical.
7. Any two: why students were absent; who arrived late; whether students were learning; attendance in other
   classes; who left early.
8. "Who collected it?" and "When?" first: the census 2021 final count was about 29.2 million; "30 million" may be a
   projection, a rounded figure or an error. Then "how" (census or estimate?).
9. No. 0 °C is not "no heat"; it is where water freezes. Ratios only make sense when zero means "none" (for
   example 20 mm of rain *is* twice 10 mm). This stretch idea (interval vs ratio scales) is enough at this level.
10. Accept any form with ≥2 numerical (hours per day, number of apps, age when first used a phone) and ≥2
    categorical (phone owner: self/family/none, main use: study/games/social), units given, no names.

## Real-data exercises: notes
* **R1** One row = one year. Columns: year (time label; treat as categorical/ordered here), arrivals by air,
  arrivals by land, total arrivals (counts, persons), earnings (money, check unit on the page: usually NPR or US$
  in thousands/millions). Source: MoCTCA via Open Data Nepal, collected at airports and border points. Can answer:
  "Did arrivals grow between 2001 and 2014?" Cannot answer: "Why did they fall?" or anything after 2014.
* **R2** Population and households are numerical counts; district and province are categorical. Mother tongue is
  categorical with more than 100 categories (124 languages were reported in 2021; confirm on the results page).
  Handle sensitive variables (caste, religion) as "describing groups", never ranking them.
* **R3** Good for a homework check-in; ask two students to read out one example each.
