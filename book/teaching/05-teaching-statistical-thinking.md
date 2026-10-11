# 5. Teaching statistical thinking

Statistics is often taught as formulas. Students then calculate a standard deviation correctly and have no idea what it
means. This curriculum puts **meaning first and formulas second**.

## Five principles

1. **Variability is the point.** If everyone were the same there would be nothing to study. Start every topic with
   variation: "Why are these numbers different?"
2. **Look before you calculate.** A dot plot, histogram or scatter plot first; summaries second. (Anscombe's quartet,
   Grade 10 Unit 3.)
3. **Simulate before you formalise.** Drawing slips from a bag (Grade 8 Unit 2, Grade 11 Unit 3), shuffling labels
   (Grade 11 Unit 4) and resampling with the computer make sampling variation and p-values visible. Formulas then
   become summaries of something students have *seen*.
4. **Context gives meaning.** "PM2.5 = 39.7" means nothing; "39.7 in June, three times the June median" is a story.
5. **Always ask how sure.** From Grade 8 ("would another sample of six give the same mean?") to Grade 11 intervals.

## Common misconceptions and how to address them

| Misconception | Grade(s) | What helps |
|---|---|---|
| "Numbers are numerical" (ward numbers, roll numbers) | 8 | the arithmetic test: does averaging make sense? |
| "The mean is always the average to report" | 8, 10 | the income example with one rich family; skewed data |
| "A bigger sample can't be biased" | 8, 11 | the FM-radio SMS poll; bootstrap intervals that miss biased truth |
| "Counts compare places fairly" | 8, 9 | the six districts whose ranking reverses by rate |
| "Percentage points = percent" | 8, 9 | 60% → 66%: 6 points, 10% change; ask for both |
| "Correlation means cause" | 9, 10 | ice cream and drownings; temperature and rain both driven by season |
| "An outlier is an error — delete it" | 10 | flag → investigate → decide; the earthquake main shock |
| "A 95% interval contains 95% of the data" | 11 | plot individual values next to the interval |
| "p < 0.05 means important/true" | 11 | huge samples with tiny effects; multiple testing demo |
| "High accuracy = good model" | 10, 12 | baselines; imbalanced classes (low birth weight) |
| "Training score shows performance" | 10, 12 | the student who memorised last year's exam |
| "Computers are objective" | 8, 10, 12 | bias audits; who is missing from training data |

When a misconception appears, **don't just correct it**: create a situation where it fails (a counter-example), let
students discover the failure, then explain.

## Using real and synthetic data well

* **Synthetic data** let you control the lesson: you know the true answer (Grade 11 bootstrap "population"), and every
  student gets the same numbers. Always say "this is invented".
* **Real data** bring surprise and relevance. Use them in exercises and projects; expect messiness; that is part of the
  lesson.
* When real data contradict a textbook claim, celebrate: that is science.

## Probability and intuition

Students in Nepal often meet probability only as coin and die formulas. Build intuition with:
* repeated physical experiments (dice, slips, cards) and class-pooled results;
* natural frequencies ("3 in 10 people", "94 in every 1,000") rather than decimals;
* simple simulations in Python (`rng.choice`, `rng.integers`) from Grade 9 onwards.

## Linking with the Maths syllabus

| Maths topic | Data-science link in this book |
|---|---|
| Statistics (mean, median, mode, pie charts) | G8 U4–5 (purpose, choosing, misleading graphs) |
| Percentages, ratio and proportion | G8 U6, G9 U7 (rates, percentage points, growth) |
| Coordinate geometry, straight lines | G10 U3 (line of best fit), G11 U7 (coordinates, distance) |
| Probability | G8 U2 (random samples), G11 U3–4 (simulation) |
| Sequences, compound interest | G9 U7 (growth rates) |
| Trigonometry | G11 U7 (haversine distance) |
| Functions and graphs | G12 U2 (logistic function), U4 (polynomials) |
