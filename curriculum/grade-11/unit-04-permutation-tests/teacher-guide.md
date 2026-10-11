# Teacher guide — Grade 11, Unit 4: Is the difference real? Permutation tests

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | The idea of chance | 40–45 min |
| 2 | Run a permutation test | 40–45 min |
| 3 | Interpreting results honestly | 40–45 min |
| P | Unit project: Chance or real? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/permutation.ipynb`; cards for the unplugged version.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Write group labels on cards, shuffle, deal into two piles, record the difference; repeat 20 times.

## Common misconceptions
* A small p-value shows the difference is big or important (it doesn't).
* A large p-value proves no difference.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: The idea of chance**
1. What does shuffling labels imitate?  
   *Answer:* Groups being interchangeable (no real difference).
2. What do we compare to?  
   *Answer:* The observed difference.
3. What is chance variation?  
   *Answer:* Differences that arise from random assignment alone.

**Lesson 2: Run a permutation test**
1. p-value = ?  
   *Answer:* Share of shuffled differences as extreme as the observed.
2. Why 5,000 shuffles?  
   *Answer:* More shuffles give a steadier estimate.
3. What does a tiny p-value suggest?  
   *Answer:* Chance alone rarely produces such a difference.

**Lesson 3: Interpreting results honestly**
1. Does small p show a large effect?  
   *Answer:* No: check the effect size.
2. Does large p show no difference?  
   *Answer:* No: maybe too little data.
3. What else to report?  
   *Answer:* Effect size, interval, how data were collected.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. H₀: girls and boys in our school have the same mean sleep; the sex labels are interchangeable with respect to sleep.
2. 140 ÷ 2,000 = 0.07.
3. False. p is the probability of data at least this extreme **if** H₀ were true, not the probability that H₀ is true.
4. Mountain − Terai visits = −0.51 (2.62 vs 3.14); p < 0.001 (no shuffle of 5,000 was as extreme). Sentence: "Mountain
   women in this synthetic sample had about half a visit fewer on average; chance is a very poor explanation; the data
   are observational and synthetic."
5. The small sample has only 6 Mountain records; p ≈ 1 — far too little data to tell anything (not evidence of "no
   difference").
6. Replace `.mean()` by `np.median(...)`. Median birth weight facility − home = +0.05 kg, p ≈ 0.12.
7. We usually don't know the direction in advance and should be surprised by either. One-sided only if the direction
   was fixed before seeing data and the other direction would be treated exactly like "no effect" (rare).
8. Volunteer teachers may be more motivated; sections differ; p = 0.01 only says chance is unlikely, not that the
   programme caused it. Redesign: randomly assign sections (or students) to the programme, measure before and after.
9. Two "hits" out of 40 is what chance alone produces (≈ 5%); treat them as hypotheses to test on new data.
10. Both simulate sampling variation of the same difference. If the 95% bootstrap interval excludes 0, the two-sided
    p-value is usually below about 0.05 (and vice versa, approximately).

Lesson 1 cards: observed difference 0.8 − 0.3 = 0.5; with 10 vs 10, exact permutation p ≈ 0.07 — suggestive, not
convincing. Lesson 3 step 2: bootstrap 95% CI for Hill − Mountain facility share ≈ 0.015 to 0.177. Step 3: in our run 2
of 100 random splits gave p < 0.05.

## Real-data exercises: notes
* **R1** Adelie males are heavier by roughly 600–700 g; p is essentially 0 — a large effect with a clear mechanism.
* **R2** Years are not independent if there is a trend; with 15 vs 15 years differences need to be large to stand out.
* **R3** Holidays cluster in certain seasons (Dashain/Tihar in autumn), so compare with nearby ordinary days.
