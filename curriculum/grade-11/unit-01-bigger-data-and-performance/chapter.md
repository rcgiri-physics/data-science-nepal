# Grade 11 · Unit 1: Bigger data and performance basics

> Track: B (code) · Tools: Python, pandas, SQLite · Lessons: 3
> Datasets: none

**Big idea.** When tables reach hundreds of thousands of rows, how we store and ask matters: types, memory, indexes and vectorised operations.

**What you will be able to do**

* I can measure time and memory.
* I can choose efficient column types.
* I can explain what an index does.

**Words to know:** row, memory, dtype, index, vectorised, benchmark (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/bigger_data.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Measuring: time and memory

**Hook (5 min).** Your notebook freezes on a big file. How do you find out why?

**Concept (≤ 5 min).** Measure before optimising: time a step with time.perf_counter, check memory with memory_usage. Compare after each change.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Generate 500,000 rows; measure memory and one group-by; record the numbers.

**Check (5 min).**
1. Why measure first?
2. Name two things you can measure.
3. Why repeat timings?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Types and vectorising

**Hook (5 min).** Why store hour of day (0–23) in 64 bits?

**Concept (≤ 5 min).** Smaller dtypes save memory; column (vectorised) operations beat Python loops by large factors.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Downcast columns; compare loop vs vectorised sum; record the speed-up.

**Check (5 min).**
1. int8 holds values from…
2. Why prefer df['a'].sum() to a loop?
3. Risk of too-small types?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Indexes in databases

**Hook (5 min).** Finding one name in a phone book vs in a pile of papers.

**Concept (≤ 5 min).** An index is a sorted lookup structure that speeds up WHERE queries on a column at the cost of space and slower writes.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Create an index in SQLite; time the same query before and after.

**Check (5 min).**
1. What does an index speed up?
2. What does it cost?
3. Which column would you index for WHERE station = 7?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Make it faster, prove it

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
