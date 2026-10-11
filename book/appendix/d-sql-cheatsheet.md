# Appendix D — SQL cheat sheet (SQLite)

## Query shape (always in this order)
```text
SELECT   columns, expressions AS names
FROM     table AS t
JOIN     other AS o ON t.key = o.key
WHERE    row conditions
GROUP BY grouping columns
HAVING   group conditions
ORDER BY column DESC
LIMIT    n;
```
Runs logically as: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.

## Basics
| Task | SQL |
|---|---|
| all columns | `SELECT * FROM districts;` |
| some columns | `SELECT district, population FROM districts;` |
| condition | `WHERE ecological_belt = 'Terai' AND literacy_pct > 70` |
| several values | `WHERE province IN (1, 3, 7)` |
| range | `WHERE literacy_pct BETWEEN 60 AND 65` |
| text pattern | `WHERE district LIKE 'Hill-1%'` |
| missing | `WHERE x IS NULL` / `IS NOT NULL` |
| sort | `ORDER BY population DESC` |
| top n | `ORDER BY population DESC LIMIT 5` |
| calculated column | `ROUND(population / area_km2, 1) AS density` |
| avoid whole-number division | `1.0 * a / b` |
| comment | `-- this is a comment` |

## Aggregates and groups
| Task | SQL |
|---|---|
| count rows | `COUNT(*)` |
| count non-null values | `COUNT(column)` |
| total, mean, min, max | `SUM(x)`, `AVG(x)`, `MIN(x)`, `MAX(x)` |
| per group | `SELECT ecological_belt, COUNT(*) FROM districts GROUP BY ecological_belt;` |
| filter groups | `HAVING COUNT(*) >= 12` |
| weighted rate | `100.0 * SUM(part) / SUM(whole)` |

## Joins
| Join | Keeps |
|---|---|
| `JOIN` (inner) | rows matching in both tables |
| `LEFT JOIN` | all left rows; NULLs where no match |
| anti-join | `LEFT JOIN … WHERE right.key IS NULL` → unmatched rows |

Check row counts before and after every join. Aggregate the "many" side first in one-to-many joins.

## Window functions
| Task | SQL |
|---|---|
| rank within groups | `RANK() OVER (PARTITION BY belt ORDER BY population DESC)` |
| row number / dense rank | `ROW_NUMBER() OVER (...)`, `DENSE_RANK() OVER (...)` |
| group total on each row | `SUM(population) OVER (PARTITION BY belt)` |
| share of group | `100.0 * population / SUM(population) OVER (PARTITION BY belt)` |
| running total | `SUM(x) OVER (PARTITION BY g ORDER BY t ROWS UNBOUNDED PRECEDING)` |
| previous / next row | `LAG(x) OVER (ORDER BY t)`, `LEAD(x) OVER (ORDER BY t)` |
| quartile groups | `NTILE(4) OVER (ORDER BY x)` |
| rolling mean (7 rows) | `AVG(x) OVER (ORDER BY date ROWS 6 PRECEDING)` |

Filter on window results in an outer query or CTE.

## CTEs and indexes
```text
WITH ranked AS (
    SELECT district, RANK() OVER (ORDER BY population DESC) AS r FROM districts
)
SELECT * FROM ranked WHERE r <= 5;

CREATE INDEX idx_station ON readings(station);
EXPLAIN QUERY PLAN SELECT AVG(pm25) FROM readings WHERE station = 7;
```

## SQL from Python
```text
import sqlite3, pandas as pd
con = sqlite3.connect(":memory:")
pd.read_csv("districts_synthetic.csv").to_sql("districts", con, index=False)
result = pd.read_sql("SELECT ecological_belt, COUNT(*) AS n FROM districts GROUP BY ecological_belt", con)
```

## Common errors
`no such column: Terai` → text needs single quotes · too many rows → JOIN without ON · `misuse of aggregate` → aggregate
in WHERE (use HAVING) · integer results like 0 → use `1.0 *`.
