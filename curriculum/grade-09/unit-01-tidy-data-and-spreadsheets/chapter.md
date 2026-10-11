# Grade 9 · Unit 1: Tidy data and spreadsheets

> Track: A/B (spreadsheet) · Tools: Calc/Sheets/Excel · Lessons: 3
> Datasets: `census-districts`

**Big idea.** A spreadsheet is a table plus formulas. Data are easiest to analyse when each row is one thing, each column one variable and each cell one value.

**What you will be able to do**

* I can recognise tidy data and fix untidy tables.
* I can use SUM, AVERAGE, MIN, MAX, COUNT, COUNTIF and simple calculated columns.
* I can sort, filter and build a pivot table.

**Words to know:** spreadsheet, cell, cell reference, range, formula, function, sort, filter, pivot table, tidy data (व्यवस्थित तथ्याङ्क). Full list: `curriculum/framework/glossary.md`.

### Before you start
From Grade 8: tidy tables (Unit 3), mean/median (Unit 5), rates (Unit 6). You need any spreadsheet program:
LibreOffice Calc (free, works offline), Google Sheets (free, needs internet) or Microsoft Excel. Formulas below
work in all three. Open `datasets/census-districts/clean/districts_synthetic.csv` (77 fictional districts; the
numbers are **synthetic**).

---

## Lesson 1: Rows, columns and cell types

**Hook (5 min).** Your teacher sorts two copies of the same table by population. One sorts perfectly; the other
scrambles: names end up next to the wrong numbers. What is different about the second copy?

### Explanation
A spreadsheet is a grid. Columns have letters (A, B, C…), rows have numbers (1, 2, 3…), and each **cell** has an
address called a **cell reference**: `E2` is column E, row 2. A block of cells is a **range**: `E2:E78` means E2 down
to E78.

Our district table opened in a spreadsheet looks like this:

| | A | B | C | D | E | F | G | … | J |
|---|---|---|---|---|---|---|---|---|---|
| **1** | district_id | district | ecological_belt | province | population | households | area_km2 | … | literacy_pct |
| **2** | 1 | Hill-01 | Hill | 5 | 229425 | 57325 | 2108.7 | … | 82.2 |
| **3** | 2 | Hill-02 | Hill | 6 | 543452 | 106859 | 2480.5 | … | 73.1 |

Row 1 is the **header** (column names). Rows 2 to 78 are the 77 districts. The full columns are: A `district_id`,
B `district`, C `ecological_belt`, D `province`, E `population`, F `households`, G `area_km2`, H `male`, I `female`,
J `literacy_pct`, K `absentee_population`.

**Tidy data** (the same rules as Grade 8 Unit 3, now enforced by software):
1. Each **row** is one case (one district).
2. Each **column** is one variable, with **one header row** of short names.
3. Each **cell** holds one value.

Spreadsheets also give every cell a **type**:
* **number** (right-aligned by default) — you can calculate with it;
* **text** (left-aligned) — labels, names;
* **date** — stored internally as a number of days, displayed as a date.

If you type `45 min` the cell becomes **text**, and `=AVERAGE` silently ignores it. Put the unit in the header
(`travel_minutes`) and keep the cells as numbers.

**Things that break tidy spreadsheets**

| Problem | Why it hurts | Fix |
|---|---|---|
| Merged cells in the header | sorting/filtering fails or mixes rows | one header row, one name per column |
| Two header rows ("Population" over "Male / Female") | software sees the second row as data | combine into `population_male`, `population_female` |
| Units in cells (`45 min`, `2,480 km²`) | numbers become text | unit in the header; number in the cell |
| Totals or notes inside the data | totals get sorted or averaged with districts | totals on a separate sheet or below a blank gap |
| Colour as data ("red rows are Mountain") | software cannot read colour | add a column `ecological_belt` |
| Blank rows in the middle | sort and filter stop at the blank | delete blank rows |
| Years as columns (`rain_2004`, `rain_2005`…) | wide format: hard to group and plot | one row per station-year (Grade 9 Unit 5 and Grade 10 show how) |

### Activity (20 min)
1. Open the district CSV. Click a few cells and look at the formula bar: which are numbers, which text?
2. Answer: what is one row? How many rows of data? How many variables?
3. Your teacher gives a deliberately **messy copy** (or make one yourself): a merged title row on top, `km²` typed
   into the area cells, a "TOTAL" row in the middle, and Mountain districts coloured red. Fix every problem so the
   table is tidy, then sort it by population to prove it works.

### Common mistakes
* Typing units into cells.
* Keeping a title row above the header ("Table 3.2: District data"): move it to a note or the sheet name.
* Sorting only one column: always select the whole table (or use the Sort menu, which extends the selection).

**Check (5 min).**
1. In the district table, what is one row?
2. Why avoid '45 min' in a cell?
3. Why avoid merged cells?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Formulas

**Hook (5 min).** How would you find the total population of 77 districts without a calculator, and make sure the
answer updates automatically if one district's number is corrected?

### Explanation
A **formula** starts with `=`. It can do arithmetic (`=E2/F2`) or call a **function** with a range
(`=SUM(E2:E78)`). When a cell in the range changes, the formula recalculates.

**The core functions**

| Function | What it does | District example | Result (synthetic) |
|---|---|---|---|
| `=SUM(E2:E78)` | adds | total population | 27,333,379 |
| `=AVERAGE(J2:J78)` | mean | mean of district literacy | 72.77 |
| `=MEDIAN(J2:J78)` | median | median district literacy | 73.1 |
| `=MIN(G2:G78)` / `=MAX(G2:G78)` | smallest / largest | smallest district area | 611.7 km² |
| `=COUNT(E2:E78)` | counts **numbers** | districts with a population | 77 |
| `=COUNTA(B2:B78)` | counts non-empty cells | districts with a name | 77 |
| `=COUNTIF(C2:C78,"Terai")` | counts cells meeting a condition | Terai districts | 22 |
| `=SUMIF(C2:C78,"Terai",E2:E78)` | adds where a condition holds | Terai population | 14,366,042 |
| `=AVERAGEIF(C2:C78,"Hill",J2:J78)` | mean where a condition holds | mean Hill literacy | 77.07 |

**Calculated columns.** In L1 type the header `female_share`. In L2 type `=I2/E2` (female ÷ population) and press
Enter. Then **fill down**: copy L2 and paste into L3:L78 (or double-click the small square at the cell's corner). The
spreadsheet changes the references for each row automatically: L3 becomes `=I3/E3`, and so on. This is called a
**relative reference**.

Sometimes you want one reference **not** to change, for example dividing every district's population by the national
total in a fixed cell, say N1. Write `=E2/$N$1`: the `$` signs make it an **absolute reference**. Copying the formula
down keeps `$N$1` fixed.

**Format, don't round.** To show 0.5428 as 54.3%, use the **Format → percent** button with one decimal place. The
cell still holds 0.5428…, so later calculations stay accurate. Rounding with `=ROUND(…)` changes the value itself;
do it only at the very end, if at all.

### Activity (20 min)
1. In cells below or beside the table (leave a blank column gap), compute: total population, mean literacy, median
   literacy, smallest and largest area, and the number of Terai, Hill and Mountain districts.
2. Add the column `female_share` = female ÷ population, fill down, format as percent.
3. Add the column `density` = population ÷ area_km2 (people per km²). Which district is the most crowded?
4. Check: do `COUNTIF` for the three belts add up to 77?

### Common mistakes
* Typing the numbers into a formula (`=229425+543452+…`) instead of using a range.
* Forgetting the `=`, so the formula appears as text.
* Copying a formula that should point to a fixed cell without `$`, so the reference slides down to empty cells
  (result `#DIV/0!`).
* Putting results inside the data table, where they get sorted along with the districts.

**Check (5 min).**
1. Formula for the sum of C2:C78?
2. What does COUNTIF(B2:B78,"Hill") do?
3. Why use ranges instead of typing numbers?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Sort, filter and pivot

**Hook (5 min).** Which five districts have the highest literacy? Which ecological belt has the largest total
population? You have 2 minutes and a 77-row table. Go!

### Explanation
**Sort** reorders the rows by one or more columns. Data → Sort, choose the column and the order (ascending A→Z,
small→large; descending large→small). Always sort the **whole table**, so each district keeps its own numbers.
Sorting by literacy descending puts Hill-26 (83.6%), Hill-06 (83.5%), Hill-18 (82.9%), Hill-28 (82.9%) and Hill-01
(82.2%) at the top.

**Filter** hides rows that do not meet a condition, without deleting them. Data → AutoFilter (Calc) / Filter
(Sheets/Excel) adds a drop-down button to each header. Choose `ecological_belt = Terai` and you see only the 22 Terai
rows. Functions like `SUBTOTAL` respect filters; plain `SUM` does not. Remove the filter to see all rows again.

**Pivot table** (Calc: Insert → Pivot Table; Sheets/Excel: Insert → Pivot table) groups rows and summarises each
group. You choose:
* **Rows:** the grouping variable (`ecological_belt`);
* **Values:** what to summarise and how (`population` → Sum; `literacy_pct` → Average; `district` → Count).

Result (synthetic data):

| ecological_belt | Count of district | Sum of population | Average of literacy_pct |
|---|---|---|---|
| Hill | 39 | 11,907,289 | 77.1 |
| Mountain | 16 | 1,060,048 | 65.8 |
| Terai | 22 | 14,366,042 | 70.2 |
| **Total** | **77** | **27,333,379** | **72.8** |

A pivot table is the spreadsheet version of what SQL calls `GROUP BY` (Unit 3) and pandas calls `groupby` (Unit 5).
Learning it here means you already understand the idea when you meet the code.

**A warning about averaging percentages.** The "Average of literacy_pct" for Terai (70.2) treats a small Terai
district the same as a huge one. It is the *average district*, not the literacy rate of *all Terai people*. To get
the people-weighted rate you would need the number of literate people in each district. Unit 7 returns to this.

### Activity (20 min)
1. Sort by `literacy_pct` descending; write down the top 5 and bottom 5.
2. Filter to show only province 7. How many districts? Remove the filter.
3. Build a pivot table: rows = `ecological_belt`; values = count of district, sum of population, average of
   literacy_pct, sum of absentee_population.
4. Add a second pivot with rows = `province`. Which province has the most districts? The most people?
5. Write three sentences for a fact sheet, each with a number and a unit.

### Common mistakes
* Sorting a single column and breaking the rows.
* Forgetting that a filter is still on, and wondering why rows have "disappeared".
* Averaging percentages and calling it the group's rate.

**Check (5 min).**
1. Which tool answers 'total population for each belt'?
2. A filter on belt = Hill does what?
3. A pivot table in SQL is closest to…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Tidy: one row per case, one column per variable, one value per cell, one header row; no merged cells, units in
  cells, totals inside data or colour-as-data.
* Formulas start with `=`; use ranges (`E2:E78`) and functions (`SUM`, `AVERAGE`, `MEDIAN`, `MIN`, `MAX`, `COUNT`,
  `COUNTIF`, `SUMIF`, `AVERAGEIF`).
* Fill down with **relative** references; fix a cell with **absolute** `$N$1`.
* Format numbers for display; don't round the stored value.
* **Sort** reorders, **filter** hides, **pivot** groups and summarises (= SQL `GROUP BY`).
* An average of percentages is not the group's overall rate.

## Practice exercises
1. ★ Write the cell reference for: column D, row 10; the range from G2 to G78.
2. ★ Write formulas for: (a) the largest population, (b) the number of districts in province 3 (province is column
   D), (c) the total households.
3. ★ What is the difference between `COUNT` and `COUNTA`?
4. ★★ In M2 you write `=E2/F2` and fill down. What does column M measure? Give it a good header name.
5. ★★ Cell N1 holds the total population. Write the formula in O2 for each district's share of the national
   population, so that it can be filled down correctly.
6. ★★ Describe step by step how to find the three Mountain districts with the lowest literacy.
7. ★★ This table is untidy. Redraw it tidy:

   | Belt | 2011 pop | 2021 pop |
   |---|---|---|
   | Mountain | 1.78 million | 1.77 million |
   | Hill | 11.39 million | 11.76 million |

8. ★★★ The pivot shows "Average of literacy_pct" for the whole table as 72.8%. Explain why this might not be the
   literacy rate of the people in these 77 districts.
9. ★★★ You fill down `=I2/$E$2` by mistake. What will column L show? How would you spot the mistake?
10. ★★★ Plan a one-page "fact sheet" about the synthetic districts: four facts, which formula or pivot produces each,
    and one chart.

## Exercises with real data
**R1. Tidy a real table (RD-09).** Download *Annual rainfall by station 2004–2015* from Open Data Nepal and open it in
a spreadsheet. List every way it is untidy (wide years? units? blanks? notes?). Fix the header and types. Use
`AVERAGE` across each row to get each station's mean annual rainfall, then sort to find the wettest and driest
stations. Write the station names and values.
*Offline fallback:* use `climate_monthly_synthetic.csv`: compute the mean `rain_mm` for each month with a pivot
table (rows = month).

**R2. A country fact sheet (RD-01).** On <https://data.worldbank.org/country/nepal> download (CSV) population,
GDP per capita and life expectancy for Nepal. In a spreadsheet, keep only the years 2000–latest. Compute the change in
each indicator from 2000 to the latest year (difference and percent change). Write three fact-sheet sentences with
units and source.

**R3. Census by province (RD-13).** From the Census 2021 results portal, copy population and households for the 7
provinces into a sheet. Add calculated columns: share of national population (absolute reference!) and average
household size. Sort by household size.

## Unit project: Spreadsheet fact sheet
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Make a one-page fact sheet about the
districts (synthetic, or a real table from R2/R3): four facts produced by formulas or pivot tables (show the formula
next to each), one chart, and a note about the source and what the table cannot tell. Full brief and rubric:
`project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* LibreOffice Calc Guide (free PDF, LibreOffice documentation): chapters on formulas and pivot tables.
* Google's free "Spreadsheet" lessons in Applied Digital Skills, or search "pivot table tutorial LibreOffice".
* Hadley Wickham, "Tidy Data" (2014): the paper behind the tidy rules (sections 1–2 are readable now).
