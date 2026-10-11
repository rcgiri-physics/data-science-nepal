# 6. Teaching SQL and Python to beginners

Many teachers who will teach Track B units are not programmers themselves. This chapter is for you: you do not need to
be an expert to teach well, but you do need a few good routines.

## PRIMM: Predict, Run, Investigate, Modify, Make

PRIMM (developed by Sue Sentance and colleagues for school computing) structures every code activity in this book:

1. **Predict** — before running, students write what they think the code will do. ("How many rows will this return?")
2. **Run** — run it and compare with the prediction.
3. **Investigate** — trace, annotate, change one thing at a time, explain each line to a partner.
4. **Modify** — change the code to do something slightly different ('Mountain' instead of 'Terai').
5. **Make** — write new code for a new but similar task.

Why it works: students read code before writing it (as we read before we write in languages); predictions make them
think; small modifications build confidence before blank-page tasks.

## Scaffolding fades over the years

| Grade | Notebooks |
|---|---|
| 9 | fill-in-the-blank cells, every step explained |
| 10 | partial skeletons with comments |
| 11–12 | blank cells with a checklist of what to produce |

## Pair programming

Two students, one computer: the **driver** types, the **navigator** reads, checks and thinks ahead. Swap every 10
minutes. Pair programming halves the number of computers needed and reduces "stuck" time, because two people rarely get
stuck on the same thing. In a lab of 15 computers, a class of 45 works as 15 groups of three (driver, navigator, data
steward).

## Errors are normal: teach debugging explicitly

Show students that **professional programmers see errors all day**. Teach a routine:

1. **Read the last line of the error message first** (`NameError`, `KeyError`, `SyntaxError`…).
2. Find the line number; look at that line and the one above.
3. Check the usual suspects: spelling and capital letters, quotes and brackets, `=` vs `==`, indentation, column names
   (`df.columns`), file paths.
4. Print things: `print(df.shape)`, `print(type(x))`, `df.head()`.
5. Change one thing at a time.
6. If still stuck after 5 minutes: ask a neighbour, then the teacher — describing what you expected and what happened.

Keep a class **"error wall"**: each new error message, what it meant, how it was fixed.

## Common beginner errors (Python and SQL)

| Error | Usual cause |
|---|---|
| `NameError: name 'df' is not defined` | cell that creates `df` not run (run all cells from the top) |
| `KeyError: 'Literacy'` | wrong column name (case, spaces): check `df.columns` |
| `SyntaxError` | missing bracket, quote or colon |
| `IndentationError` | inconsistent spaces |
| `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | numbers stored as text (clean, convert) |
| `ValueError: The truth value of a Series is ambiguous` | `and`/`or` instead of `&`/`|` in pandas filters |
| `no such column: Terai` (SQL) | text value without single quotes |
| SQL result has too many rows | JOIN without `ON` |

## Teaching with very few computers

* **One computer + projector:** the teacher drives, students predict on paper (PRIMM still works); rotate a student to
  the keyboard for "Modify".
* **Unplugged SQL and algorithms:** cards, slips, roles (Grade 9 Unit 3, Grade 10 Unit 5).
* **Phones:** JupyterLite runs in a modern phone browser for short tasks (small screens make long code hard; use for
  running and modifying, not writing from scratch).
* **Station rotation:** one group at the computers, one doing the paper version, one doing exercises; rotate every 15
  minutes.

## Should students learn SQL or Python first?

This book uses spreadsheets → SQL → Python because each step builds on the previous idea (a pivot table *is* a
`GROUP BY`; a `GROUP BY` *is* a pandas `groupby`) and because SQL's vocabulary is close to English. SQL also matches the
DBMS content in the Grade 9–10 optional Computer Science syllabus. Python then adds loops, functions and libraries.

## Your own learning as a teacher

Work through the Grade 9 chapters as a student before teaching them: two hours per unit is enough. Then the free
courses listed in *After Grade 12* (CS50P, Kaggle Learn Python/pandas/SQL) take you well beyond what you need to teach
Grades 9–12. Learning alongside students is fine — say "Let's find out together" and model the debugging routine.
