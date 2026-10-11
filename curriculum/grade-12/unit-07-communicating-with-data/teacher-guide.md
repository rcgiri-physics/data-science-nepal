# Teacher guide — Grade 12, Unit 7: Communicating with data

**Time:** 3 lessons + project (about 5 periods). **Track:** A/B.

| # | Lesson | Time |
|---|---|---|
| 1 | Action titles and honest charts | 40–45 min |
| 2 | The one-page memo | 40–45 min |
| 3 | Presenting and publishing | 40–45 min |
| P | Unit project: Story and memo | 2 periods |

## Before you start
* Materials: Notebook `notebooks/data_story.ipynb`; memo template in `docs/templates/policy-memo.md`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Write the memo on paper; draw the chart by hand.

## Common misconceptions
* More charts = more convincing.
* Hiding uncertainty makes you more credible (it does the opposite).

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Action titles and honest charts**
1. What is an action title?  
   *Answer:* A title that states the finding.
2. What goes in the caption?  
   *Answer:* Source, units and a limit.
3. Why a zero baseline for bars?  
   *Answer:* Otherwise differences look exaggerated.

**Lesson 2: The one-page memo**
1. What goes first?  
   *Answer:* The bottom line.
2. Why say what you don't know?  
   *Answer:* It builds trust and helps decisions.
3. Who is your audience?  
   *Answer:* A specific decision-maker, not 'everyone'.

**Lesson 3: Presenting and publishing**
1. How to show uncertainty plainly?  
   *Answer:* Use a range and a sentence like 'likely between X and Y'.
2. What do you publish with data work?  
   *Answer:* Licence, credits, source, limits.
3. Is Django required?  
   *Answer:* No: optional stretch.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 12 Computer Science (programming, databases, emerging technologies) and Maths/Statistics. Django (optional stretch): a student who knows HTML can turn the dashboard into a Django view — not required.

## Answers: practice exercises
1. e.g. "PM2.5 is highest from November to February, almost every day above the national standard".
2. What is shown (with units), the source and date, and a limit (plus "synthetic" when relevant).
3. "Each extra antenatal visit goes with about 40% higher odds of delivering in a facility."
4. Horizontal bars sorted from highest at top read more easily (labels fit, eyes scan down a ranked list).
5. "Province 6 has the highest share of people living abroad (94 per 1,000). We recommend starting migrant-family
   support there."
6. Facility-delivery rates with bootstrap 95% intervals (Grade 11 Unit 3): Mountain 0.33 (0.25–0.40), Hill 0.42
   (0.39–0.46), Terai 0.49 (0.45–0.53). Action title: "Mountain mothers are least likely to deliver in a facility
   (synthetic data)".
7. "Roads © OpenStreetMap contributors (ODbL); district boundaries: OCHA/HDX from Survey Department of Nepal [licence as
   on page]; population: National Statistics Office, Census 2021."
8. Assess with the checklist: right chart, sorted, honest scale, highlight, declutter, caption.
9. e.g. "We could not detect a change in monsoon rainfall over these 30 years; year-to-year swings are larger than any
   trend. Plans should prepare for both very wet and very dry years."
10. Chairperson: bottom line + action; newspaper: hook + human angle + the number + caution. Discuss what was lost and
    gained.

Lesson memo (synthetic): Province 6 districts range from Hill-02 (106.6 per 1,000) to Mountain-16 (53.1).

## Real-data exercises: notes
* **R1** Absent-population shares vary greatly between real districts and provinces; let students find the pattern
  in the census tables themselves and compare it with the synthetic story (it will differ — that is the point).
* **R2** Insist on plain language and a range.
* **R3** Use OWID's chart page source line in the caption.
