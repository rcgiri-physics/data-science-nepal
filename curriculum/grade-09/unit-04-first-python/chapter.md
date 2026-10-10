# Grade 9 · Unit 4: First steps in Python

> Track: B (code: Python) · Tools: Python in the browser (JupyterLite) or Colab · Lessons: 3
> Datasets: `class-survey-synthetic`

**Big idea.** Python lets us tell a computer what to do with data step by step: store values, repeat actions and reuse ideas in functions.

**What you will be able to do**

* I can store values in variables and lists, and read items by position.
* I can use a for loop and an if statement to process a list.
* I can write and test a small function.

**Words to know:** program, variable (चर), value, list, index, loop, condition, function, argument, return value, error message. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/first_python.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
You need no programming experience. You do need Grade 8's mean, median and range, because we will teach the
computer to calculate them. Open the notebook: a notebook is a page of **cells**; click a code cell and press
**Shift + Enter** to run it. The result appears underneath.

---

## Lesson 1: Variables and lists

**Hook (5 min).** Where does a computer keep the number 25 so it can use it again later? How would it keep the travel
times of 36 students?

### Explanation
A **program** is a list of instructions the computer follows in order, top to bottom. Python is a programming
language that is popular in data science because it reads almost like English and has excellent tools for tables
(pandas, Unit 5) and charts (Unit 6).

**Variables.** A variable is a **name** attached to a **value**. The `=` sign means "make this name refer to this
value" (assignment), *not* "is equal to".

```python
age = 14
name = "Sita"
sleep_hours = 8.2
print(name, "is", age, "years old and slept", sleep_hours, "hours")
```

Output: `Sita is 14 years old and slept 8.2 hours`

Values have **types**: `14` is an integer (`int`), `8.2` a decimal number (`float`), `"Sita"` text (a string, `str`),
`True`/`False` a Boolean (`bool`). Text always goes in quotes.

Python does arithmetic with `+ - * /`, powers with `**`, and whole-number division with `//` and remainder with `%`:

```python
minutes = 135
hours = minutes // 60       # 2
left_over = minutes % 60    # 15
print(hours, "hours and", left_over, "minutes")
```

Anything after `#` is a **comment** for humans; Python ignores it.

**Lists.** A list stores many values in order, inside square brackets:

```python
travel = [53, 27, 40, 23, 11, 48, 21, 7, 12, 52]   # minutes, first 10 students
print(len(travel))      # how many items: 10
print(travel[0])        # first item: 53
print(travel[-1])       # last item: 52
print(travel[0:3])      # items 0, 1, 2: [53, 27, 40]
```

Positions (**indexes**) start at **0**, not 1. `travel[0]` is the first item; `travel[9]` is the tenth (and last).
`travel[10]` gives an `IndexError` because there is no eleventh item. Negative indexes count from the end.

Lists can change:

```python
travel[1] = 30          # correct the second value
travel.append(19)       # add a value at the end
print(travel)
print(sum(travel), min(travel), max(travel), sorted(travel))
```

`sum`, `min`, `max`, `sorted` and `len` are **built-in functions**: Python's tools that work on lists.

**Error messages are friends.** When something is wrong, Python stops and prints an error. Read the **last line**
first: `NameError: name 'travl' is not defined` means you spelled a name wrong; `SyntaxError` means the grammar is
wrong (a missing bracket or quote); `TypeError` usually means you mixed types (`"5" + 3`).

### Activity (20 min) — PRIMM
1. **Predict** what each cell in section 1 of the notebook prints, write your prediction, then **run** it.
2. **Investigate:** what does `travel[2:5]` give? `travel[-2]`? What happens with `travel[20]`?
3. **Modify:** make a list `heights` of 8 classmates' heights (cm). Print its length, first and last item, the
   smallest and largest.
4. **Make:** compute the range of `heights` (largest − smallest) and print it in a sentence with the unit.

### Common mistakes
* Forgetting that indexes start at 0.
* Writing `print(travel[1, 2])` instead of `travel[1:3]`.
* Mismatched quotes or brackets (`"Sita'`, `[1, 2`).
* Using a variable before giving it a value.

**Check (5 min).**
1. minutes = [5, 20, 35]; minutes[0]?
2. len(minutes)?
3. = or ==: which assigns?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Loops and conditions

**Hook (5 min).** Adding 36 numbers by hand takes a few minutes. Adding 3 million (one per person in a province)
would take years. How do we make the computer do the same step again and again?

### Explanation
A **for loop** repeats some lines once for **each item** in a list:

```python
travel = [53, 27, 40, 23, 11, 48, 21, 7, 12, 52]
total = 0
for m in travel:
    total = total + m
print("Total minutes:", total)
```

Read it as: "start with total = 0; for each value `m` in the list, add `m` to total". After the loop, `total` is 294.
The variable `m` takes each value in turn: 53, then 27, then 40…

**Indentation matters.** The lines that belong inside the loop are **indented** (4 spaces). The `print` is not
indented, so it runs once, after the loop finishes. Indent it and it runs 10 times. In Python, indentation is part
of the grammar, not decoration.

An **if statement** runs lines only when a condition is `True`:

```python
long_trips = 0
for m in travel:
    if m > 30:
        long_trips = long_trips + 1
print(long_trips, "students travel more than 30 minutes")
```

Conditions use comparison operators: `==` (equal — two signs!), `!=` (not equal), `<`, `>`, `<=`, `>=`, and combine
with `and`, `or`, `not`. Add other cases with `elif` ("else if") and `else`:

```python
for m in travel[:4]:
    if m <= 15:
        label = "short"
    elif m <= 40:
        label = "medium"
    else:
        label = "long"
    print(m, label)
```

**A pattern you will use forever:** start a variable (a counter, a total or an empty list), loop over the data,
update the variable inside the loop, use the result after the loop.

### Activity (20 min) — PRIMM
1. **Predict** the total and the count of long trips, then run section 2 of the notebook.
2. **Investigate:** move `print` inside the loop (indent it). What changes? Why?
3. **Modify:** count trips of **15 minutes or less**.
4. **Make:** loop over the list and build a new list of the trips longer than 30 minutes (start with
   `long_list = []` and use `long_list.append(m)`).

### Common mistakes
* `if m = 30:` (one `=` assigns; comparisons need `==`).
* Forgetting the colon `:` at the end of `for` and `if` lines.
* Mixing tabs and spaces, or indenting by different amounts.
* Resetting the counter inside the loop.

**Check (5 min).**
1. What does 'for m in minutes' do?
2. Why is indentation important?
3. Count of values > 30 uses…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Functions

**Hook (5 min).** You have now calculated a mean four times this year. How could you write the steps **once** and
use them for any list?

### Explanation
A **function** packages steps under a name. You **define** it once with `def`, then **call** it as often as you like:

```python
def my_mean(values):
    """Return the mean (average) of a list of numbers."""
    total = 0
    for v in values:
        total = total + v
    return total / len(values)

print(my_mean([20, 20, 30, 40, 90]))   # 40.0
```

* `values` is a **parameter**: a name for whatever list you pass in (the **argument**).
* `return` sends the result back to where the function was called. Without `return` the function gives back `None`.
* The text in triple quotes is a **docstring**: it explains what the function does.

The median needs the list sorted, then the middle value (or the mean of the two middle values):

```python
def my_median(values):
    """Return the median of a list of numbers."""
    s = sorted(values)
    n = len(s)
    middle = n // 2
    if n % 2 == 1:            # odd count: one middle value
        return s[middle]
    else:                     # even count: mean of the two middle values
        return (s[middle - 1] + s[middle]) / 2

print(my_median([20, 20, 30, 40, 90]))   # 30
print(my_median([1, 2, 3, 4]))           # 2.5
```

For n = 4, `middle` = 2, so the two middle values are `s[1]` and `s[2]`, the 2nd and 3rd items. Tracing through a
small example by hand like this is how programmers check their thinking.

**Test with small lists whose answers you know.** `assert` stops the program with an error if a statement is false,
and does nothing if it is true:

```python
assert my_mean([2, 4, 6]) == 4
assert my_median([5, 1, 3]) == 3
assert my_median([1, 2, 3, 4]) == 2.5
print("All tests passed")
```

**Why functions?** Write once, use many times; fix a mistake in one place; give a name to an idea, so the program
reads like a description of the analysis. Python already has many functions for data (the `statistics` module has
`mean` and `median`; pandas in Unit 5 has hundreds). Writing your own once helps you understand what they do.

### Activity (20 min) — PRIMM
1. **Predict** `my_mean([20, 20, 30, 40, 90])` and `my_median([1, 2, 3, 4])`, then run section 3.
2. **Investigate:** what happens with `my_mean([])`? Why? (Read the error message.)
3. **Modify:** write `my_range(values)` that returns max − min. Test it with `assert`.
4. **Make:** write `count_above(values, limit)` that returns how many values are above `limit`. Use it to count
   students sleeping more than 8 hours in the class list from the notebook.

### Common mistakes
* Printing inside the function instead of returning (you can't then use the result).
* Forgetting to call the function (`my_mean` without brackets is the function itself, not its answer).
* Sorting the original list by accident (`values.sort()` changes it); `sorted(values)` makes a copy.

**Check (5 min).**
1. What does return do?
2. my_median([1, 2, 3, 4])?
3. Why test with small lists?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* A program runs top to bottom. `=` assigns a value to a name. Types: `int`, `float`, `str`, `bool`.
* Lists hold values in order; indexes start at 0; `len`, `sum`, `min`, `max`, `sorted` work on lists.
* `for x in list:` repeats indented lines once per item; `if / elif / else` choose; `==` compares.
* Counter/total pattern: start, loop and update, use after the loop.
* `def name(parameters): … return result`; test with `assert` on small examples.
* Read error messages from the last line up.

## Practice exercises
1. ★ What does this print? `x = 7` then `x = x + 3` then `print(x * 2)`.
2. ★ `days = ["Sun", "Mon", "Tue", "Wed"]`. What are `days[1]`, `days[-1]`, `len(days)`, `days[1:3]`?
3. ★ What is wrong? `if age = 14: print("Grade 9")`.
4. ★★ Write a loop that prints each value of `[5, 12, 30, 45]` converted to hours (÷ 60), rounded to 2 decimals
   (`round(x, 2)`).
5. ★★ Write a loop that counts how many items in `["walk", "bus", "walk", "bicycle", "walk"]` are `"walk"`.
6. ★★ Write `percent(part, whole)` returning part ÷ whole × 100. Test: `percent(26, 36)` ≈ 72.2.
7. ★★ Trace by hand: what does `my_median([9, 1, 5, 7])` return? Show `s`, `n` and `middle`.
8. ★★★ Write `my_mode(values)` returning the most frequent value. (Hint: loop, and use `values.count(v)`.)
9. ★★★ Write `fahrenheit_to_celsius(f)` using C = (F − 32) × 5 ÷ 9 and convert a list of temperatures
   `[59, 68, 86, 104]` with a loop.
10. ★★★ This function has a bug. Find and fix it, then write an `assert` that would have caught it.

```python
def count_long(values, limit):
    count = 0
    for v in values:
        count = 0
        if v > limit:
            count = count + 1
    return count
```

## Exercises with real data
**R1. A week of real weather (RD-06).** Look up yesterday's and the past week's maximum temperature for your town on
Open-Meteo or a weather app. Type the 7 values into a Python list. Use your functions to compute the mean, median and
range, and print one sentence with units.
*Offline fallback:* the first 7 values of `mean_temp_c` from `climate_monthly_synthetic.csv`, typed in by hand.

**R2. Earthquake list (RD-05).** Copy the magnitudes of the 15 strongest 2015 earthquakes from the USGS list (or your
Unit 3 SQL result) into a Python list. Count how many are 6.0 or more, compute the mean, and write a loop that labels
each as "moderate" (< 5), "strong" (5–5.9) or "major" (≥ 6).

**R3. Prices (RD-08).** Make a list of 10 daily tomato prices (Rs/kg) from the Kalimati data or today's market page.
Write a function `percent_change(old, new)` and use it in a loop to print the day-to-day change.

## Unit project: My first data script
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Write a short script (in the notebook) that
stores one variable from your class data in a list, uses your own `my_mean`, `my_median` and `my_range` functions
(with `assert` tests), counts values above a threshold with a loop, and prints a three-sentence summary. Full brief and
rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* CS50's Introduction to Programming with Python (CS50P, free, Harvard): <https://cs50.harvard.edu/python/>.
* Python's official tutorial: <https://docs.python.org/3/tutorial/> (sections 3–4).
* Pythontutor (<https://pythontutor.com>) shows your code running step by step — excellent for loops and functions.
