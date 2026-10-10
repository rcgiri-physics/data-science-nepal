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
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
1. 20.
2. `"Mon"`, `"Wed"`, `4`, `["Mon", "Tue"]`.
3. `=` assigns; comparison needs `==`; also the body should be on its own indented line:
   `if age == 14:` newline, 4 spaces, `print("Grade 9")`.
4. `for m in [5, 12, 30, 45]:` → `print(round(m / 60, 2))` → 0.08, 0.2, 0.5, 0.75.
5. `count = 0`, loop, `if mode == "walk": count = count + 1` → 3. (Or `modes.count("walk")`.)
6. `def percent(part, whole): return part / whole * 100`; `assert round(percent(26, 36), 1) == 72.2`.
7. `s = [1, 5, 7, 9]`, `n = 4`, `middle = 2`, even → `(s[1] + s[2]) / 2 = (5 + 7) / 2 = 6.0`.
8. ```
   def my_mode(values):
       best, best_count = None, 0
       for v in values:
           if values.count(v) > best_count:
               best, best_count = v, values.count(v)
       return best
   ```
   (Ties: returns the first value reaching the highest count — discuss.)
9. `(f - 32) * 5 / 9` → 15.0, 20.0, 30.0, 40.0.
10. `count = 0` inside the loop resets the counter every time, so the function returns 1 or 0 (only the last value
    counts). Move it above the loop. Test: `assert count_long([10, 50, 60], 30) == 2` (the buggy version returns 1).

## Real-data exercises: notes
* **R1** Check units (°C) and that students write the source and dates.
* **R2** From the 2015 USGS list (2026-10-11): 7.8, 7.3, 6.7, 6.6, 6.3, 6.1 are ≥ 6.0 (6 values); the next nine are
  5.0–5.9 (values vary slightly with catalogue revisions).
* **R3** `def percent_change(old, new): return (new - old) / old * 100`; watch for division by zero if a price is
  missing (0).
