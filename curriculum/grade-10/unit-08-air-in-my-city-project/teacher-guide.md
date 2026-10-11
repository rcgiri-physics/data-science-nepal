# Teacher guide — Grade 10, Unit 8: Project: Air in my city

**Time:** 2 lessons + project (about 4 periods). **Track:** B (project).

| # | Lesson | Time |
|---|---|---|
| 1 | Plan and clean | 40–45 min |
| 2 | Analyse and publish | 40–45 min |
| P | Unit project: Air in my city | 2 periods |

## Before you start
* Materials: Notebook `notebooks/air_in_my_city.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Printed monthly summary table; poster instead of dashboard.

## Common misconceptions
* One station represents the whole city.
* Quoting health thresholds from memory; check the current official value and cite it.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Plan and clean**
1. What must you cite for the limit?  
   *Answer:* The organisation and document it came from.
2. Why plan for missing data?  
   *Answer:* It affects counts and means.
3. What is a one-line question?  
   *Answer:* e.g. 'In which months is PM2.5 most often above the limit?'

**Lesson 2: Analyse and publish**
1. Three parts of a conclusion?  
   *Answer:* Claim, evidence, reasoning.
2. Name two limits in this study.  
   *Answer:* One station; missing days; (synthetic) data.
3. Why disclose AI use?  
   *Answer:* Honesty and fair assessment.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. e.g. "How many days in Dec–Feb 2019–2020 had daily PM2.5 above Nepal's 24-hour standard in Kathmandu, compared with
   Jun–Aug?"
2. 20 ÷ 25 = 80% of valid days. Dividing by 31 treats 6 unknown days as clean, understating the problem.
3. So changing a choice (e.g. a revised standard) updates every result consistently, and readers see the assumptions.
4. WHO 15 µg/m³: Jan–Apr and Nov–Dec 100%; Oct 98%; Sep 91%; May 83%; Aug 47%; Jul 44%; Jun 36% — below 100% in
   May–Oct.
5. 2019: 209 of 348 valid days; 2020: 212 of 354 — about 60% both years; no meaningful difference (synthetic data
   has no lockdown effect built in).
6. The 7-day mean stays above 40 from about October to April (it crosses the line during April–May and
   September–October); it is below 40 throughout June–August.
7. Different handling of −999 (left in, or replaced by 0), different denominator (all days vs valid days), `>` vs `>=`,
   different file versions, different date parsing (day-first). Compare the logs line by line.
8. The data show when and how much PM2.5 was high, not why. Traffic counts, fuel use, brick-kiln and burning
   records, weather (inversions, wind), source-apportionment studies, or natural experiments (strikes, lockdowns)
   would help.

## Real-data exercises: notes
* **R1** Real data show the same seasonal pattern; spring 2020 lockdown (late March–May) often shows lower PM2.5 than
  the same weeks in nearby years, though spring forest fires can mask it. Let students argue from their own numbers.
* **R2** OpenAQ station availability changes; Open-Meteo weather is always available.
* **R3** The GHO page gives modelled attributable deaths with uncertainty ranges — teach students to quote the range,
  the year and the source.
