# Grade 9 · Unit 5: Tables in pandas

> Track: B (code: pandas) · Tools: Python, pandas · Lessons: 4 · Version: 0.1 draft (English)
> Datasets: `census-districts`

**Big idea.** pandas holds a table in a DataFrame; we select, filter, sort and group with short commands — the same ideas as SQL.

**What you will be able to do**

* I can load and inspect a DataFrame.
* I can select columns and filter rows.
* I can add a new column and group-summarise.

**Words to know:** DataFrame, Series, read_csv, filter, groupby (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/pandas_basics.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Load and inspect

**Hook (5 min).** Before analysing, what do you check first when someone hands you a table?

**Concept (≤ 5 min).** read_csv loads a file; .shape, .head(), .dtypes, .describe() show size, first rows, types and quick summaries.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Load the district table; predict, then check shape and types; find any column that is text but should be numeric.

**Check (5 min).**
1. Which method shows the first rows?
2. What does .shape return?
3. Why check dtypes?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Select and filter

**Hook (5 min).** Show only Hill districts with literacy above 80%.

**Concept (≤ 5 min).** df['col'] picks a column; df[condition] keeps rows where the condition is True; combine with & and parentheses.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Write three filters; compare each with its SQL WHERE.

**Check (5 min).**
1. df[df['ecological_belt']=='Hill'] does what?
2. Combine two conditions with…
3. SQL twin of a filter?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Sort and new columns

**Hook (5 min).** Which districts have the most people abroad per 1,000 residents?

**Concept (≤ 5 min).** sort_values orders rows; you can create a column by arithmetic on columns: df['rate'] = 1000*a/b.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Add abroad_per_1000; show top-5 by count and top-5 by rate; explain the difference.

**Check (5 min).**
1. df['rate'] = 1000*df.a/df.b creates…
2. Why rank by rate not count?
3. ascending=False means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: Group and summarise

**Hook (5 min).** Mean literacy by belt and by province — in one line each.

**Concept (≤ 5 min).** groupby splits rows into groups; agg summarises each group (count, sum, mean). It is GROUP BY.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Write a groupby by belt, then by province; check that group counts add up to 77.

**Check (5 min).**
1. groupby('belt').size() returns…
2. How can you check a grouped result?
3. SQL twin?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Same question, SQL and pandas

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
