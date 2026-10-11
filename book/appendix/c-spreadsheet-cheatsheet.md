# Appendix C — Spreadsheet and CODAP cheat sheet

Works in LibreOffice Calc, Google Sheets and Excel (menu names differ slightly).

## Tidy rules
One row per case · one column per variable · one value per cell · one header row · units in the header, numbers in the
cells · no merged cells · no totals inside the data · missing = empty (or `NA`), never 0.

## References
| Write | Means |
|---|---|
| `E2` | column E, row 2 |
| `E2:E78` | range from E2 to E78 |
| `$N$1` | absolute reference (does not change when copied) |
| `Sheet2!A1` | a cell on another sheet |

## Functions
| Formula | Does |
|---|---|
| `=SUM(E2:E78)` | total |
| `=AVERAGE(J2:J78)` | mean |
| `=MEDIAN(J2:J78)` | median |
| `=MODE(J2:J78)` | mode (numbers) |
| `=MIN(...)`, `=MAX(...)` | smallest, largest |
| `=QUARTILE(J2:J78, 1)` | lower quartile (3 = upper) |
| `=STDEV(J2:J78)` | standard deviation (sample) |
| `=COUNT(E2:E78)` | count numbers |
| `=COUNTA(B2:B78)` | count non-empty cells |
| `=COUNTBLANK(B2:B732)` | count empty cells |
| `=COUNTIF(C2:C78,"Terai")` | count where condition holds |
| `=COUNTIF(B2:B732,-999)` | count error codes |
| `=SUMIF(C2:C78,"Terai",E2:E78)` | sum where condition holds |
| `=AVERAGEIF(C2:C78,"Hill",J2:J78)` | mean where condition holds |
| `=ROUND(x, 1)` | round (only at the end) |
| `=IF(J2>75,"high","low")` | condition |
| `=TRIM(A2)`, `=PROPER(A2)`, `=LEN(A2)` | clean text: spaces, Title Case, length |
| `=VLOOKUP(A2, lookup!A:B, 2, FALSE)` | look up a standard name (exact match) |
| `=CORREL(X2:X78, Y2:Y78)` | correlation *r* |
| `=SLOPE(Y, X)`, `=INTERCEPT(Y, X)` | least-squares line |
| `=TEXT(A2,"000")` | keep leading zeros in codes |

## Rates
* Percent: `=100*K2/E2` · per 1,000: `=1000*K2/E2` · share of a fixed total: `=E2/$N$1`
* Percent change: `=(new-old)/old*100` · percentage points: `=new%-old%`
* Weighted group rate: `=SUMIF(belt,"Hill",part)/SUMIF(belt,"Hill",whole)`

## Sort, filter, pivot
* **Sort:** select the whole table → Data → Sort (never one column alone).
* **Filter:** Data → AutoFilter / Filter; remember to clear it.
* **Pivot table:** Insert → Pivot Table: Rows = grouping column; Values = column + Sum/Average/Count. (= SQL `GROUP BY`.)

## Charts
Select data → Insert → Chart. Bar for categories (axis from 0), line for time, scatter (XY) for two numbers. Always add
title, axis labels with units, and source.

## CODAP quick steps (<https://codap.concord.org>)
1. Drag a CSV file onto the CODAP page → a table appears.
2. **Graph** button → drag a column name onto the x-axis (and another onto y).
3. Categorical on x → dot/bar view; numerical → dot plot; two numerical → scatter plot.
4. Ruler menu on the graph: add mean, median, box plot, movable line, least-squares line.
5. Drag a categorical column onto the graph's middle to split by group.
