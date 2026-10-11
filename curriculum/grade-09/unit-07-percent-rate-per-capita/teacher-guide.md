# Teacher guide — Grade 9, Unit 7: Percent, rate and per-capita

**Time:** 3 lessons + project (about 5 periods). **Track:** A/B.

| # | Lesson | Time |
|---|---|---|
| 1 | Share, percent and per 1,000 | 40–45 min |
| 2 | Choosing a denominator | 40–45 min |
| 3 | Percent change and percentage points | 40–45 min |
| P | Unit project: Rate detective | 2 periods |

## Before you start
* Materials: Notebook `notebooks/rates.ipynb` (or spreadsheet).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Spreadsheet units can be done as a paper grid: draw the table, write formulas as words ('sum of column C').

## Common misconceptions
* A rate with the wrong denominator misleads (girls enrolled ÷ all enrolled ≠ ÷ girls of school age).
* Percent of a percent confusion.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Share, percent and per 1,000**
1. 12 of 200 as a percent?  
   *Answer:* 6%.
2. 12 of 200 per 1,000?  
   *Answer:* 60 per 1,000.
3. Why per 1,000 for rare things?  
   *Answer:* Small percents are hard to read; per 1,000 gives readable numbers.

**Lesson 2: Choosing a denominator**
1. Girls' share of enrolment divides by…  
   *Answer:* Total enrolment (girls + boys).
2. Why can two 'girls' percentages differ?  
   *Answer:* Different denominators answer different questions.
3. Always state the denominator in…  
   *Answer:* The chart title or caption.

**Lesson 3: Percent change and percentage points**
1. 48% → 50%: points?  
   *Answer:* 2 points.
2. Relative change?  
   *Answer:* 2 ÷ 48 ≈ 4.2%.
3. Fair headline wording?  
   *Answer:* State 'percentage points' for the difference.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
1. 0.025; 2.5%; 25 per 1,000.
2. 840 ÷ 28 = 30 students per teacher.
3. 100 × 1,180 ÷ 1,250 = 94.4 males per 100 females.
4. Passes: 18 + 28 + 5 = 51 of 70 → 72.9%. Simple average of rates = 70%: the big class (70%) and small class (50%)
   are wrongly given equal weight with the small 90% class.
5. (a) literate people aged 5+ ÷ people aged 5+; (b) remittances received ÷ GDP; (c) hospital beds ÷ population
   × 10,000; (d) students ÷ computers.
6. +10.3 percentage points; percent change 10.3 ÷ 65.9 ≈ 15.6%. Headline: "Literacy rose from 65.9% to 76.2% between
   the 2011 and 2021 censuses, up about 10 percentage points."
7. +20% over the decade; annual growth (1.2)^(0.1) − 1 ≈ 1.84% per year.
8. Vehicles may have grown much faster than deaths: deaths per vehicle can fall while deaths per person (and the
   total) rise. Check deaths per 100,000 people and the counts.
9. Synthetic sums: Hill 84.4, Mountain 87.9, Terai 97.2 males per 100 females; Hill lowest. In real data, hill
   districts with heavy male labour migration have low sex ratios.
10. No: 1.1 × 1.1 = 1.21 → 21%.

Lesson 2 activity: weighted girls' share by belt — Hill 50.16%, Mountain 50.15%, Terai 50.11%; mean of district
shares — Hill 50.24%, Mountain 50.05%, Terai 49.80%. Small differences because district shares are all close to 50%;
the method matters much more when rates vary a lot.
Lesson 3 activity: 400,000 → 460,000 is +15%, about 1.41% per year. Rice index = 92 ÷ 80 × 100 = 115 (15% rise).

## Real-data exercises: notes
* **R1** Nepal's remittances are among the highest shares in the world (around a quarter of GDP in recent years);
  % of GDP compares economies of different sizes.
* **R2** Census 2021 vs 2011: Bagmati and Madhesh had the largest increases in count; some hill/mountain districts
  lost people (provincial totals all grew modestly; check the portal). Annual growth national 0.92% (NSO).
* **R3** Index with 2014 = 100; spikes appear in years with supply shocks (e.g. 2015 blockade period). Let students
  find and explain them.
