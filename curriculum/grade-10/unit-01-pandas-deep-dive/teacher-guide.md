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
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology (⚠️ confirm unit numbers in the CDC syllabus PDF); compulsory Maths data handling/statistics.
