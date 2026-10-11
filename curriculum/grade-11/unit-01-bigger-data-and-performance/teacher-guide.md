# Teacher guide — Grade 11, Unit 1: Bigger data and performance basics

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Measuring: time and memory | 40–45 min |
| 2 | Types and vectorising | 40–45 min |
| 3 | Indexes in databases | 40–45 min |
| P | Unit project: Make it faster, prove it | 2 periods |

## Before you start
* Materials: Notebook `notebooks/bigger_data.ipynb` (generates its own 500,000-row synthetic table).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Phone-book analogy: find a name in an unsorted vs alphabetically sorted book (index).

## Common misconceptions
* Faster computer = no need for good code.
* Loops over rows are fine in pandas; use column operations.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Measuring: time and memory**
1. Why measure first?  
   *Answer:* To fix the real bottleneck.
2. Name two things you can measure.  
   *Answer:* Time and memory.
3. Why repeat timings?  
   *Answer:* Results vary run to run.

**Lesson 2: Types and vectorising**
1. int8 holds values from…  
   *Answer:* −128 to 127.
2. Why prefer df['a'].sum() to a loop?  
   *Answer:* It runs in optimised compiled code.
3. Risk of too-small types?  
   *Answer:* Overflow: values too big wrap or fail.

**Lesson 3: Indexes in databases**
1. What does an index speed up?  
   *Answer:* Lookups/filters on the indexed column.
2. What does it cost?  
   *Answer:* Extra space and slower writes.
3. Which column would you index for WHERE station = 7?  
   *Answer:* station.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. 8,000,000 bytes (8 MB) as `int64`; 1,000,000 bytes (1 MB) as `int8`.
2. month `int8`; district_id `int8` (fits 1–77); population `int32`; temperature `float32`; province name `category`.
3. Whether SQLite will scan the whole table or search using an index (and which index).
4. Usually faster on `small` because grouping on a `category` uses integer codes; exact times vary.
5. `df["pm25_mg"] = df["pm25"] / 1000`.
6. ```
   total, count = 0.0, 0
   for chunk in pd.read_csv("big.csv", chunksize=100_000):
       total += chunk["pm25"].sum()
       count += chunk["pm25"].count()
   print(total / count)
   ```
7. `hour = 8` matches 1/24 ≈ 4% of rows vs 2% for one station; less selective conditions gain less. Still useful
   combined with another column (composite index) or for `ORDER BY hour`.
8. `int8` 127 + 1 wraps to −128 (NumPy warns for scalars; arrays can wrap silently, e.g. `[100, 120] + 50` →
   `[-106, -86]`). Wrong values look like real numbers and corrupt every later result.
9. Index on `student_id` (lookup one student); composite index on `(subject, year)` for the grouped average (or
   `(year, subject)`); no index on `mark` (rarely filtered).
10. Use `%timeit` or a loop of 5 runs with `time.perf_counter`, report the median; `* 2` is many times faster.

## Real-data exercises: notes
* **R1** Converting `Commodity`/`Unit` to category usually cuts memory by more than half; parse dates with an explicit
  format.
* **R2** Use the USGS search page or API with `minmagnitude=2.5` and one year; files of 20–40k rows.
* **R3** Open-Meteo `hourly=temperature_2m`; resample with `set_index("time").resample("D").mean()`.
