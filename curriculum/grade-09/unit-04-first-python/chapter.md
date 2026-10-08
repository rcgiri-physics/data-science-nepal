# Grade 9 · Unit 4: First steps in Python

> Track: B (code: Python) · Tools: Python in the browser (JupyterLite) or Colab · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `class-survey-synthetic`

**Big idea.** Python lets us tell a computer what to do with data step by step: store values, repeat actions and reuse ideas in functions.

**What you will be able to do**

* I can use variables, lists and loops.
* I can write a small function.
* I can compute a mean by hand-written code and with built-ins.

**Words to know:** variable, list, loop, function, print (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/first_python.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Variables and lists

**Hook (5 min).** Where does a computer keep the number 25 so it can use it later?

**Concept (≤ 5 min).** A variable is a named box (age = 25). A list holds many values ([5, 20, 35]); positions start at 0.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Predict then run: create a list of travel minutes; print its length and first item; change one value.

**Check (5 min).**
1. minutes = [5, 20, 35]; minutes[0]?
2. len(minutes)?
3. = or ==: which assigns?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Loops and conditions

**Hook (5 min).** Add 77 numbers by hand? Let the computer repeat.

**Concept (≤ 5 min).** A for loop repeats for each item; an if statement acts only when a condition is true. Indentation shows what belongs inside.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Write a loop to total a list; add an if to count values above 30.

**Check (5 min).**
1. What does 'for m in minutes' do?
2. Why is indentation important?
3. Count of values > 30 uses…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Functions

**Hook (5 min).** You have computed a mean four times. How do you avoid rewriting it?

**Concept (≤ 5 min).** def name(inputs): … return result. Functions make code reusable and easier to test.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Write my_mean and my_median; test with small lists whose answers you know.

**Check (5 min).**
1. What does return do?
2. my_median([1, 2, 3, 4])?
3. Why test with small lists?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: My first data script

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
