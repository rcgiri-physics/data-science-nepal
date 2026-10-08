# Teacher guide — Grade 11, Unit 1: Bigger data and performance basics

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Measuring: time and memory | 40–45 min |
| 2 | Types and vectorising | 40–45 min |
| 3 | Indexes in databases | 40–45 min |
| P | Unit project: Make it faster, prove it | 2 periods |

## Before you start
* Materials: Notebook `notebooks/bigger_data.ipynb` (generates its own 500,000-row synthetic table).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Phone-book analogy: find a name in an unsorted vs alphabetically sorted book (index).

## Common misconceptions
* Faster computer = no need for good code.
* Loops over rows are fine in pandas; use column operations.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Measuring: time and memory**
1. Why measure first?  
   *Answer:* To fix the real bottleneck.
2. Name two things you can measure.  
   *Answer:* Time and memory.
3. Why repeat timings?  
   *Answer:* Results vary run to run.

**Lesson 2: Types and vectorising**
1. int8 holds values from…  
   *Answer:* −128 to 127.
2. Why prefer df['a'].sum() to a loop?  
   *Answer:* It runs in optimised compiled code.
3. Risk of too-small types?  
   *Answer:* Overflow: values too big wrap or fail.

**Lesson 3: Indexes in databases**
1. What does an index speed up?  
   *Answer:* Lookups/filters on the indexed column.
2. What does it cost?  
   *Answer:* Extra space and slower writes.
3. Which column would you index for WHERE station = 7?  
   *Answer:* station.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.
