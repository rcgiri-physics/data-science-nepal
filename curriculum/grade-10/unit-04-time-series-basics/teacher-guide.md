# Teacher guide — Grade 10, Unit 4: Time series basics

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Trend, season and noise | 40–45 min |
| 2 | Fitting a trend | 40–45 min |
| 3 | Anomalies | 40–45 min |
| P | Unit project: Climate or weather? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/time_series.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Plot 12 monthly values by hand; mark the seasonal peak; compute a yearly average.

## Common misconceptions
* A warm month proves climate change; weather ≠ climate.
* Trend lines from short series are unreliable.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Trend, season and noise**
1. Is a yearly warm summer a trend?  
   *Answer:* No, it is seasonality.
2. Why use annual means for trend?  
   *Answer:* They average out the seasonal cycle.
3. What is noise?  
   *Answer:* Random variation not explained by trend or season.

**Lesson 2: Fitting a trend**
1. Slope 0.03 °C/yr is how much per decade?  
   *Answer:* 0.3 °C.
2. Why try different start years?  
   *Answer:* To check how sensitive the trend is.
3. Weather vs climate?  
   *Answer:* Weather is short-term; climate is long-term pattern.

**Lesson 3: Anomalies**
1. Anomaly = ?  
   *Answer:* Observed − usual (baseline) value for that month.
2. Why subtract a monthly baseline?  
   *Answer:* To remove the seasonal cycle.
3. Positive anomaly means…  
   *Answer:* Warmer than usual.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.
