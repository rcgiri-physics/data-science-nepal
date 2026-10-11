# Teacher guide — Grade 10, Unit 6: AI literacy and ethics

**Time:** 3 lessons + project (about 5 periods). **Track:** A (no-code).

| # | Lesson | Time |
|---|---|---|
| 1 | How AI learns | 40–45 min |
| 2 | Hallucination and bias | 40–45 min |
| 3 | Responsible use | 40–45 min |
| P | Unit project: AI charter and audit | 2 periods |

## Before you start
* Materials: Case cards (printed), prompt card from `docs/pedagogy/ai-use-policy.md`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Entirely unplugged.

## Common misconceptions
* AI 'knows' facts; it generates likely text.
* Computers are objective, so AI decisions are fair.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: How AI learns**
1. What does an AI learn from?  
   *Answer:* Training data (examples).
2. Does it understand like a person?  
   *Answer:* No: it predicts patterns.
3. What happens with bad data?  
   *Answer:* Bad or biased predictions.

**Lesson 2: Hallucination and bias**
1. What is hallucination?  
   *Answer:* A confident but false or invented output.
2. How do you check?  
   *Answer:* Compare with the original source.
3. Give a source of bias.  
   *Answer:* Training data that under-represents some groups.

**Lesson 3: Responsible use**
1. What does 'explain, don't answer' mean?  
   *Answer:* Ask for explanations, then do the work yourself.
2. What must you never paste into a tool?  
   *Answer:* Private personal data about real people.
3. Why an oral check?  
   *Answer:* To show you understand your work.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. e.g. phone keyboard prediction, face unlock, social-media feeds, spam filters, bank fraud alerts, map/route apps,
   voice assistants, translation.
2. Training data: examples the system learns from. Token: a small piece of text (word or part-word) the model reads and
   writes. Hallucination: confident output that is false or invented.
3. "I used [tool] only to check grammar and spelling; the ideas and wording are mine."
4. Much more English–Nepali text (news, government documents, websites) exists than Tamang–Nepali text for training.
5. Training text written before 2015 (75 districts after 1962; 77 after Nawalparasi and Rukum were split in 2015), and
   web pages that copied old numbers; the model repeats a frequent pattern.
6. (a) "Explain how to approach question 5 and give me a similar example"; (b) "Explain the features of this kind of
   poem and give feedback on my draft"; (c) "Explain why my loop gives a KeyError" / "Review my code and point out
   bugs without rewriting it".
7. Find the original source/uploader; check reputable news; look for glitches (lips, hands, lighting, audio sync);
   reverse image/video search; check the date and context.
8. Benefits: fast feedback, consistency on simple criteria. Risks: bias against unusual or non-standard (e.g. Nepali-
   English) writing, errors without explanation, students writing for the machine, privacy. Fair use: feedback only,
   teacher marks, students can appeal, regular checks of disagreements.
9. Training images over-represent stereotyped scenes (poverty, traditional dress, terraces); harms: reinforces
   stereotypes about Nepal and farmers, affects how others see and treat them, erases diversity.
10. Analysis needs judgement: is the data clean? biased? is the difference real or noise? is it cause or correlation?
    which summary is fair? AI tools make confident mistakes that only someone who knows statistics can catch.

## Real-data exercises: notes
* **R1** Prepare in advance; keep personal data out. Census 2021: 29,164,578; life expectancy ≈ 70 (WPP/World Bank);
  remittances ≈ a quarter of GDP in recent years; river lengths vary by source — a good lesson in "which source?".
* **R2** Expect much better quality for Nepali than for less-resourced languages; respect speakers' judgement.
* **R3** E.g. rainfall stations under-represent high mountains; OSM under-maps remote rural areas; the synthetic
  health table over-represents Mountain/Hill relative to the census.
