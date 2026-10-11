# Teacher guide — Grade 9, Unit 8: Grade 9 project: which districts are changing?

**Time:** 2 lessons + project (about 4 periods). **Track:** A/B (project).

| # | Lesson | Time |
|---|---|---|
| 1 | Plan and clean | 40–45 min |
| 2 | Analyse and present | 40–45 min |
| P | Unit project: Which districts are changing? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/project_template.ipynb`; poster paper.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
The project can be done in a spreadsheet or on paper with a printed extract.

## Common misconceptions
* Skipping the Plan step leads to aimless charts.
* A poster without a 'what we cannot say' box.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Plan and clean**
1. What does a plan card contain?  
   *Answer:* Question, variables, rate/denominator, data source, risks.
2. Why log cleaning steps?  
   *Answer:* So others can check and repeat them.
3. Name one risk in district tables.  
   *Answer:* Sizes differ, so counts mislead; use rates.

**Lesson 2: Analyse and present**
1. What are the three parts of a conclusion?  
   *Answer:* Claim, evidence, reasoning (plus a limit).
2. Why an oral check?  
   *Answer:* To show you understand your own work.
3. What goes in the limit box?  
   *Answer:* What the data cannot tell us.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
1. e.g. "Which belt has the highest people-abroad rate?", "Do bigger districts have larger households?", "How does
   literacy vary across provinces?"; cannot: "Why do people migrate?" or anything about change over time (one year
   only).
2. Question as given; data: districts table (synthetic); variables `population`, `households`, `province`; summary:
   weighted household size = sum population ÷ sum households per province; chart: bar chart by province; risks:
   synthetic data, households defined differently in real census, averages hide variation within provinces.
3. Winter 92.9, autumn 55.9, spring 50.4, monsoon 12.85 µg/m³ → autumn is second (close to spring).
4. e.g. "In 2019–2020 (synthetic data), winter PM2.5 (median 92.9 µg/m³) was about seven times the monsoon level
   (12.9 µg/m³); the whole winter box plot lies above the monsoon one. Limit: one station, synthetic data, 29 days
   missing."
5. "Is that the literacy rate of the people in the belt?" Answer: no, it is the average district; the weighted rate
   would need literate-people counts (Units 1 and 7).
6. Missing/invalid days by month: Jan 1, Feb 2, Mar 6, Apr 1, May 3, Jun 5, Jul 1, Sep 2, Oct 1, Nov 4, Dec 3 —
   spread over the year, only a few per month, so they are unlikely to change the seasonal conclusion; but missing
   days in polluted months slightly lower those months' totals if values were filled with zeros (they must not be).
7. Example: "Do districts with more schools per 100,000 people have more girls enrolled per school?" — JOIN on
   `district_id`, compute two rates, scatter plot, *r*.
8. 584 of 702 valid days ≈ 83%. Guidelines are revised (WHO changed it in 2021 from 25 to 15 µg/m³) and websites
   copy old values; quote the primary source with its year.

Plan-card and poster are marked with the six-criterion rubric (`docs/pedagogy/assessment.md`).

## Real-data exercises: notes
* **R1** The real Kathmandu series shows the same strong winter peak and monsoon low; winter medians in the real data
  are typically far above the WHO guideline. Filter carefully: the file mixes parameters and locations.
* **R2** National annual growth 0.92% (NSO); Kathmandu valley and Terai districts grew; several hill and mountain
  districts (e.g. in Gandaki and Koshi hills) declined. Students must find their own province's figures.
* **R3** Approve the plan card before students download anything large.
