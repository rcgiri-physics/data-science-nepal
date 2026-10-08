# Teacher guide — Grade 9, Unit 4: First steps in Python

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code: Python).

| # | Lesson | Time |
|---|---|---|
| 1 | Variables and lists | 40–45 min |
| 2 | Loops and conditions | 40–45 min |
| 3 | Functions | 40–45 min |
| P | Unit project: My first data script | 2 periods |

## Before you start
* Materials: Notebook `notebooks/first_python.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Do 'human computer': one student acts as the loop, another as the variable box, with index cards. Then type it later.

## Common misconceptions
* = assigns, == compares.
* Indexes start at 0.
* Indentation is part of Python's grammar.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Variables and lists**
1. minutes = [5, 20, 35]; minutes[0]?  
   *Answer:* 5.
2. len(minutes)?  
   *Answer:* 3.
3. = or ==: which assigns?  
   *Answer:* = assigns; == compares.

**Lesson 2: Loops and conditions**
1. What does 'for m in minutes' do?  
   *Answer:* Repeats the indented steps once for each value m in the list.
2. Why is indentation important?  
   *Answer:* It shows which lines are inside the loop/if.
3. Count of values > 30 uses…  
   *Answer:* A loop with an if and a counter.

**Lesson 3: Functions**
1. What does return do?  
   *Answer:* Sends a result back to where the function was called.
2. my_median([1, 2, 3, 4])?  
   *Answer:* 2.5.
3. Why test with small lists?  
   *Answer:* You can check the answer by hand.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming (⚠️ confirm exact grade and unit in the CDC syllabus PDF); compulsory ICT/Maths data handling.
