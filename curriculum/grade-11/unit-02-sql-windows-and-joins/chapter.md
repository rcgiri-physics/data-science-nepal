# Grade 11 · Unit 2: SQL: joins and window functions (lite)

> Track: B (code: SQL) · Tools: SQLite via Python · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `census-districts`

**Big idea.** Window functions rank, compare and accumulate *within groups* without collapsing rows — a powerful step beyond GROUP BY.

**What you will be able to do**

* I can rank rows within groups.
* I can compute running totals and shares.
* I can compare join types (INNER vs LEFT).

**Words to know:** window function, PARTITION BY, RANK, running total, LEFT JOIN (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/sql_windows.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Window functions: RANK

**Hook (5 min).** Which is the biggest district *in each belt*?

**Concept (≤ 5 min).** A window function computes over a group of rows but keeps every row: RANK() OVER (PARTITION BY belt ORDER BY population DESC).

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Rank districts within belt; keep ranks ≤ 3.

**Check (5 min).**
1. GROUP BY vs PARTITION BY?
2. Highest rank in a belt with 16 districts?
3. What does ORDER BY inside OVER do?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Shares and running totals

**Hook (5 min).** What share of the belt's population lives in the biggest district?

**Concept (≤ 5 min).** SUM(...) OVER (PARTITION BY …) gives group totals on each row; with ORDER BY it becomes a running total.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute % of belt and cumulative share; find how many districts make up half of each belt.

**Check (5 min).**
1. Percent of belt formula?
2. Running total needs…
3. Why useful?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: INNER vs LEFT JOIN

**Hook (5 min).** Three districts have no school record. What happens in a join?

**Concept (≤ 5 min).** INNER JOIN keeps only matches; LEFT JOIN keeps all left rows with NULLs where no match. Always check row counts before and after a join.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Delete three school rows; count rows under each join; explain differences.

**Check (5 min).**
1. INNER JOIN rows = ?
2. LEFT JOIN adds…
3. Safe habit?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Top districts per province

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
