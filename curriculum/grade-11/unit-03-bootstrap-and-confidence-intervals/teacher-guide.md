# Teacher guide — Grade 11, Unit 3: Uncertainty: bootstrap and confidence intervals

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Sampling variation | 40–45 min |
| 2 | The bootstrap | 40–45 min |
| 3 | Interpreting intervals | 40–45 min |
| P | Unit project: How sure are we? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/bootstrap.ipynb`; bag of numbered slips for the unplugged version.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Write 20 values on slips, draw with replacement 20 times, compute the mean; repeat 10 times; plot the means.

## Common misconceptions
* A 95% interval means 95% of data lie inside it. It describes the uncertainty of the estimate.
* Bootstrapping creates new information; it only reveals variability of this sample.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Sampling variation**
1. Will two samples give the same mean?  
   *Answer:* Usually not.
2. Bigger sample → ?  
   *Answer:* Less variation in the estimate.
3. What causes the difference?  
   *Answer:* Chance in who ends up in each sample.

**Lesson 2: The bootstrap**
1. 'With replacement' means…  
   *Answer:* Each draw is put back, so items can repeat.
2. What do we compute each time?  
   *Answer:* The statistic (e.g. mean).
3. Middle 95% gives…  
   *Answer:* A 95% bootstrap interval.

**Lesson 3: Interpreting intervals**
1. Which is narrower, n=25 or n=400?  
   *Answer:* n = 400.
2. Does a narrow interval fix a biased sample?  
   *Answer:* No.
3. Is a 95% interval where 95% of the data lie?  
   *Answer:* No: it concerns the uncertainty of the estimate.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. Parameter: the share of all Pokhara voters supporting the bus park (unknown). Statistic: 52% in the sample of 400.
2. 8 ÷ √16 = 2 cm; 8 ÷ √64 = 1 cm.
3. Without replacement, a resample of size *n* is just the same sample reordered; the statistic never changes.
   With replacement each resample is a different plausible sample.
4. "Support is estimated at 48%; values from about 45% to 51% are consistent with the poll (sampling error only)." No:
   50% is inside the interval, so a lead or a tie is possible — and non-sampling errors may be larger.
5. n = 50 (`random_state=3`): mean 28.9, CI ≈ 26.7–31.1 (width ≈ 4.3 years); n = 200: mean 29.4, CI ≈ 28.3–30.5 (width
   ≈ 2.2) — about half, as expected for 4× data.
6. 90% interval for n = 50: ≈ 27.1–30.7, narrower; less confidence needs a smaller range.
7. Hill 0.421 (0.385–0.460, n = 696), Mountain 0.325 (0.248–0.395, n = 157), Terai 0.491 (0.451–0.530, n = 647).
   Mountain's is widest: smallest group.
8. Phone sampling misses households without phones (likely poorer → bias up); people under-report income; non-response;
   mismeasured informal income. The CI covers only random sampling error.
9. With five values a resample can only rearrange/repeat five numbers; the bootstrap distribution is lumpy and too
   narrow, so intervals are too short (coverage falls). The sample is too small to stand in for the population.
10. In our test: n = 10 → 89.5% coverage; n = 100 → 94.5%. Percentile bootstrap intervals are too narrow for small
    samples.

Lesson 2 Make: low birth weight share in the sample ≈ 0.14 (CI ≈ 0.08–0.21). Difference facility − home mean birth
weight ≈ +0.01 kg (CI ≈ −0.15 to +0.18): no clear difference. Lesson 3: 200-sample coverage 94.5%.

## Real-data exercises: notes
* **R1** July totals vary a lot year to year; the interval for the mean is much narrower than the range of individual
  Julys — a perfect illustration of the "not individual values" point. Trends make "the mean of 30 years" a moving
  target.
* **R2** Gentoo is clearly heavier; Adelie and Chinstrap intervals overlap.
* **R3** NLSS/LFS reports contain standard-error tables in appendices.
