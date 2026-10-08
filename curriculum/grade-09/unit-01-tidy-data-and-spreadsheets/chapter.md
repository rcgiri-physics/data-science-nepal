# Grade 9 · Unit 1: Tidy data and spreadsheets

> Track: A/B (spreadsheet) · Tools: Calc/Sheets/Excel · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: `census-districts`

**Big idea.** A spreadsheet is a table plus formulas. Data are easiest to analyse when each row is one thing, each column one variable and each cell one value.

**What you will be able to do**

* I can build a tidy table in a spreadsheet.
* I can use SUM, AVERAGE, COUNTIF and simple formulas.
* I can sort, filter and make a pivot table.

**Words to know:** cell, formula, tidy data, filter, pivot table (Nepali glossary: `curriculum/framework/glossary.md`).

---

## Lesson 1: Rows, columns and cell types

**Hook (5 min).** Why does 'sort' scramble a messy sheet but not a clean one?

**Concept (≤ 5 min).** In tidy data each row is one case, each column one variable, each cell one value. Cells have types: number, text, date. Keep one header row; no merged cells.

**Activity (20 min).** Open the district table; identify rows, columns, types; fix a deliberately messy copy (merged header, units in cells).

**Check (5 min).**
1. In the district table, what is one row?
2. Why avoid '45 min' in a cell?
3. Why avoid merged cells?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Formulas

**Hook (5 min).** How would you find the total population of the 77 districts without a calculator?

**Concept (≤ 5 min).** A formula starts with =. SUM, AVERAGE, MIN, MAX, COUNT and COUNTIF are enough for most early analysis. Use cell ranges (C2:C78) rather than typing numbers.

**Activity (20 min).** Compute total population, mean literacy, and COUNTIF(belt,"Terai"); add a column female share = female/population.

**Check (5 min).**
1. Formula for the sum of C2:C78?
2. What does COUNTIF(B2:B78,"Hill") do?
3. Why use ranges instead of typing numbers?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Sort, filter and pivot

**Hook (5 min).** Which five districts have the highest literacy? Which belt has the largest total population?

**Concept (≤ 5 min).** Sorting orders rows; filters show rows meeting a condition; a pivot table groups rows and summarises (sum, average, count) — it is GROUP BY in a spreadsheet.

**Activity (20 min).** Sort by literacy; filter the Terai districts; build a pivot table: belt vs sum of population and average of literacy.

**Check (5 min).**
1. Which tool answers 'total population for each belt'?
2. A filter on belt = Hill does what?
3. A pivot table in SQL is closest to…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Spreadsheet fact sheet

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
