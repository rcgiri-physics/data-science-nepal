# Teacher guide — Grade 10, Unit 1: pandas deep-dive: cleaning a real-world series

**Time:** 4 lessons + project (about 6 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Parsing and error codes | 40–45 min |
| 2 | Missing values | 40–45 min |
| 3 | Group by month and weekday | 40–45 min |
| 4 | Rolling means | 40–45 min |
| P | Unit project: Clean series report | 2 periods |

## Before you start
* Materials: Notebook `notebooks/pandas_cleaning.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Use printed 20-row extracts and graph paper; do the calculations with a calculator. The code lessons need a lab day, but every concept has a paper version.

## Common misconceptions
* Filling every missing value with the mean hides the problem.
* Dropping rows changes the sample; say how many.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Parsing and error codes**
1. Why replace -999 with NaN?  
   *Answer:* So it isn't treated as a real (very negative) reading.
2. What does pd.to_datetime do?  
   *Answer:* Turns text into real dates.
3. What must you record?  
   *Answer:* How many values were changed and why.

**Lesson 2: Missing values**
1. pandas mean() on a column with NaN does what by default?  
   *Answer:* Skips the NaN.
2. Why is filling with the mean risky?  
   *Answer:* It hides missingness and shrinks variability.
3. What should you check about missing data?  
   *Answer:* Whether they cluster in time/place.

**Lesson 3: Group by month and weekday**
1. df.groupby('month')['pm25'].mean() returns…  
   *Answer:* One average per month.
2. Why chart as well as print?  
   *Answer:* Patterns are easier to see.
3. What is a doubt you'd raise?  
   *Answer:* Missing data, one station, synthetic data.

**Lesson 4: Rolling means**
1. What does a 7-day rolling mean do?  
   *Answer:* Averages each day with the previous 6 days.
2. Bigger window → ?  
   *Answer:* Smoother, slower to react.
3. Does smoothing remove real spikes?  
   *Answer:* It can blur them: check the raw data too.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. `pd.to_datetime("25/04/2015", format="%d/%m/%Y")` → 2015-04-25, a **Saturday** (the day of the Gorkha earthquake).
2. 53 days above 100 µg/m³.
3. 22.0 µg/m³.
4. `air["season"] = air["month"].map({12: "winter", 1: "winter", 2: "winter", 3: "spring", …})`; means: winter 92.4,
   autumn 54.6, spring 50.7, monsoon 14.1 µg/m³.
5. 2019: 52.5; 2020: 53.1 — a 0.6 µg/m³ difference, tiny next to the ≈ 80 µg/m³ seasonal difference.
6. `ffill` mean 53.0, interpolation 53.0 (52.97): no practical difference for short gaps.
7. 30 of 105 weekly bins (`resample("W")` includes partial weeks at the ends) have a mean above 80.
8. The ratio is about 0.61 in every season in this synthetic table (it was generated that way). In real data the
   ratio often changes with season and source (dust vs smoke), which is why scientists look at it.
9. Check that the function does not modify a global table, returns `(df, log)`, and that tests check counts
   (4 codes, 29 missing, 731 rows).
10. With 30 December days removed: NaN-skipped mean 51.1, interpolated 52.4 (vs 52.8 complete). A long gap in the
    most polluted month biases the annual mean down; interpolation across a month is guesswork. Report the gap.

Weekday result (synthetic): Sunday 49.2, Saturday 50.8, Thursday 52.5, Friday 53.1, Monday 54.2, Wednesday 54.4,
Tuesday 55.1 µg/m³ — differences small relative to the spread.

## Real-data exercises: notes
* **R1** ODN/OpenAQ files often have columns like `location, parameter, value, unit, date.utc/local`; parse the
  local time, filter one parameter/location, `resample("D").mean()`. Negative values and long gaps occur.
* **R2** Monthly rain must be a **sum**; temperature a **mean**. Kathmandu's monsoon months (Jun–Sep) carry most
  of the annual rain.
* **R3** The `-END HEADER-` line number differs with the number of parameters; find it with a small loop
  (`for i, line in enumerate(open(path))`). After `melt`, map month names to numbers and multiply by days in month
  (`pd.Period(...).days_in_month`).
