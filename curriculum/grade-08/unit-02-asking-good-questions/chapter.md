# Grade 8 · Unit 2: Asking good questions

> Track: A (no-code) · Tools: paper · Lessons: 3
> Datasets: `class-survey-synthetic`

**Big idea.** A good statistical question can be answered with data and expects variation in the answers. How we ask changes what we learn.

**What you will be able to do**

* I can tell a statistical question from a non-statistical one.
* I can spot a leading or biased question.
* I can choose between asking people and measuring.

**Words to know:** statistical question, survey (सर्वेक्षण), measurement, bias (पूर्वाग्रह), sample (नमुना), population (समष्टि). Full list: `curriculum/framework/glossary.md`.

### Before you start
From Unit 1: a **variable** varies between cases; variables are **numerical** or **categorical**; always ask who
collected data and why.

---

## Lesson 1: Statistical or not?

**Hook (5 min).** Which of these can data answer? *"How old is Ram?"* and *"How old are the students in our
school?"* Predict: what is the difference between them?

### Explanation
Every data investigation starts with a question. Data scientists use a four-step cycle that this book follows from
Grade 8 to Grade 12, called **PPDAC**: **P**roblem (the question), **P**lan, **D**ata, **A**nalysis, **C**onclusion.
If the question is poor, nothing later can rescue it.

A **statistical question** is one that
1. is about a **group** (of people, places, days…), not a single fact, and
2. **expects variation**: the answers will differ, and we want to describe or explain the differences.

| Question | Statistical? | Why |
|---|---|---|
| How old is Ram? | No | one person, one answer |
| How old are the students in our school? | Yes | many students, ages vary |
| What is the height of Sagarmatha? | No | one fixed value (8,848.86 m) |
| How much does the daily maximum temperature in Biratnagar vary during June? | Yes | 30 days, values vary |
| Did it rain in Pokhara yesterday? | No | one yes/no fact |
| On how many days did it rain in Pokhara last July? | Yes | answer is built from 31 days that vary |

Notice the last example: you can turn a non-statistical question into a statistical one by **widening it to a group
or a period** and asking about the pattern.

**Good questions are also clear and answerable.** "Are students healthy?" is too vague: what does "healthy" mean? A
sharper version is "How many hours do Grade 8 students in our school sleep on a school night?" It names:
* **who** (Grade 8 students in our school),
* **what** variable (hours of sleep), with a **unit** (hours),
* **when** (a school night).

There are three common kinds of statistical question:
* **Describe:** "How long do students in our class take to reach school?"
* **Compare:** "Do students who walk take longer than students who come by bus?"
* **Relate:** "Do students who sleep more get higher marks?" (Relationships need care; see Grade 10.)

### Activity (20 min)
1. Your teacher gives you 12 question strips (or copies them from the board). Examples: *How many siblings does Sita
   have? How many siblings do students in our class have? What is the capital of Karnali Province? What time does
   school start? What time do students wake up? How far is Janakpur from Kathmandu? How far do students in our class
   live from school? Is our school's tap water safe today? Which festival do students in our class like most? What
   was the price of rice yesterday? How did the price of rice change over the last 12 months? Who won the football
   match?*
2. Sort them into **statistical** and **not statistical**.
3. Rewrite three non-statistical ones to make them statistical. Label each rewritten question *describe*,
   *compare* or *relate*.
4. Improve one statistical question by adding who, what (with unit) and when.

### Common mistakes
* "How tall am I?" feels like data, but it has one answer. Widen it to a group.
* Questions too vague to measure ("Are students happy?"). Decide exactly what you would record.
* Questions that need data you cannot get (e.g. "How much do families earn?" is private and hard to ask honestly).

**Check (5 min).**
1. Is 'What is the height of Mount Everest?' statistical?
2. Make 'How many siblings does Sita have?' statistical.
3. Why must a statistical question allow variation?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Surveys, measurements and bias

**Hook (5 min).** Your teacher asks: *"Don't you agree our canteen food is terrible?"* What answer is the question
pushing you towards? Would you answer differently if the teacher who runs the canteen asked?

### Explanation
There are two main ways to get data about people:

* **Survey (asking):** a questionnaire or interview. Needed for opinions, habits, things only the person knows.
* **Measurement:** using an instrument (ruler, clock, scale, rain gauge, thermometer). Better whenever the thing can
  be measured, because memory and opinion are not involved.

"How long does it take you to reach school?" asked in a survey gets round guesses: 15, 20, 30 minutes. Timing the
journey with a clock gets 17, 23, 34. If you can measure, measure.

**Bias** means a *systematic* push in one direction: the answers are wrong in the same way again and again, not just
randomly. Surveys pick up bias in several ways:

| Kind of bias | Example | Fix |
|---|---|---|
| **Leading question** | "Don't you agree that…?" | Neutral wording: "How would you rate…? (1–5)" |
| **Loaded words** | "Do you support the *wasteful* new bus?" | Remove emotional words |
| **Social pressure** | "Do you study every evening?" asked by the teacher | Anonymous paper slips |
| **Unclear question** | "Do you use your phone a lot?" (what is "a lot"?) | "About how many hours yesterday? 0 / <1 / 1–2 / >2" |
| **Two questions in one** | "Is the library clean and quiet?" | Split into two questions |
| **Missing options** | "Do you walk or take the bus?" (some cycle) | Add "Other: ____" |

**Answer options matter.** A question with options (multiple choice) is easy to count. An open question ("Why do you
like Science?") gives richer answers but needs time to group. Use both, but mostly options.

### Activity (20 min)
1. Rewrite these three leading questions neutrally: *"Isn't maths the best subject?"*, *"Don't you think homework on
   Saturday is unfair?"*, *"Our school needs a new playground, right?"*
2. **Measure vs ask:** in pairs, *ask* your partner "How many seconds do you think it takes you to write your full
   name five times?" and write the answer. Then *measure* it with a clock or phone stopwatch.
3. Put every pair's "asked" and "measured" numbers on the board in two columns. Are the guesses too high or too
   low? Is the error random or mostly in one direction (bias)?

### Common mistakes
* Thinking only rude or obvious questions are biased. Even "Do you study every day?" is biased by social pressure.
* Collecting opinions when you could measure facts.
* Forgetting an "Other" or "Don't know" option.

**Check (5 min).**
1. Rewrite 'Isn't maths the best subject?' neutrally.
2. Name one way a sample can be biased.
3. Give one thing better measured than asked.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Fair samples

**Hook (5 min).** We want to know how Grade 8 students travel to school. We only ask the 5 students beside us. What
goes wrong? Predict: would the result be too high, too low, or just different?

### Explanation
The **population** is the whole group we want to learn about: all Grade 8 students in our school, or all households
in Nepal. Asking everyone is a **census**. Often that is too slow or costly, so we ask a **sample**, a smaller part
of the population, and use it to learn about the whole.

A sample is only useful if it **looks like the population**. Ways of choosing a sample:

* **Convenience sample:** whoever is nearby or easy. Friends sitting together often live in the same area and
  travel the same way, so the sample is biased.
* **Volunteer sample:** whoever chooses to answer. People with strong opinions answer more often. Online polls on
  news sites are like this.
* **Simple random sample:** every member of the population has the **same chance** of being chosen. Write every roll
  number on a slip, mix them in a box, draw without looking. This is fair because nobody's choice or habit decides
  who is in the sample.

**Bigger is not automatically better.** If a newspaper asks 10,000 readers on its website, the sample is huge but
only includes people who read that website and chose to answer. A random sample of 200 can be more trustworthy than a
biased sample of 10,000. Size reduces *random* error (luck); it does nothing about *bias*.

**Worked example.** Our class of 36 (the `class-survey-synthetic` table) has a true mean travel time of about
29.7 minutes. Suppose the 6 students nearest the door are S01, S06, S10, S14, S27, S36 (all walkers who live far
away): their mean is (53 + 48 + 52 + 54 + 50 + 40) ÷ 6 = 297 ÷ 6 = 49.5 minutes, much too high. A random draw of six
roll numbers will usually land much closer to 29.7, though it will rarely hit it exactly. That small "miss" is
**sampling variation**, which you will measure in Grade 11.

### Activity (20 min)
1. Write each student's roll number on a slip and fold it. Mix them in a box or bag.
2. Draw 6 slips. Those students tell the class their travel time (or use the class table). Calculate the mean of
   the 6.
3. Now take the 6 students sitting nearest the teacher's desk and calculate their mean.
4. Put both means on the board. Repeat the random draw twice more. Discuss: which method gets closer to the whole
   class's mean (calculated by the teacher)? Do the random samples all agree with each other?

### Common mistakes
* "Random" meaning "careless". A random sample needs a careful method (slips, dice, random number table).
* Believing a large sample cannot be biased.
* Forgetting who is *not* in the sampling list (absent students, students in another section).

**Check (5 min).**
1. What is a population?
2. Why is drawing names from a box fair?
3. Can a large sample still be biased?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Investigations follow **PPDAC**: Problem, Plan, Data, Analysis, Conclusion.
* A statistical question is about a group and expects variation; it names who, what (with unit) and when.
* Statistical questions **describe**, **compare** or **relate**.
* Measure when you can; ask when you must. Write survey questions neutrally, clearly, one idea at a time, with an
  "Other" option.
* **Bias** is a systematic push in one direction; a bigger sample does not remove it.
* A **simple random sample** gives everyone the same chance and is the fairest simple method.

## Practice exercises
1. ★ Statistical or not? (a) How many students in our school wear glasses? (b) What is the population of Lalitpur
   Metropolitan City? (c) How many hours a day do Grade 8 students spend on a phone? (d) What time does the sun rise
   in Ilam on 1 Baisakh?
2. ★ Define *population*, *sample* and *census* in your own words, with an example from your school.
3. ★★ Rewrite neutrally: (a) "Wouldn't it be better to have school on Saturdays off?" (b) "How much do you love
   the new library?" (c) "Do you agree that lazy students fail exams?"
4. ★★ "Do you have breakfast and lunch at school?" What is wrong? Fix it.
5. ★★ For each, say whether you would *ask* or *measure*, and how: (a) pulse rate after running, (b) favourite
   sport, (c) weight of school bags, (d) how safe students feel on the way to school.
6. ★★ Turn into a *compare* question: "How long do students take to reach school?" Then into a *relate* question.
7. ★★ A school of 600 students wants a random sample of 30. Describe exactly how to choose it.
8. ★★★ An FM radio station asks listeners to SMS whether they support a new road; 4,000 reply and 85% say yes. Give
   two reasons this may not represent the district's opinion.
9. ★★★ Using the worked example, explain why the 6 students nearest the door gave a mean much higher than the class
   mean. What does this tell you about convenience samples?
10. ★★★ Write a 5-question survey about how students in your school spend the hour after school. Swap with a partner
    who must find one possible bias in your survey.

## Exercises with real data
**R1. How does Nepal ask? (RD-13).** Find the Census 2021 household questionnaire (search the NSO website for "census
2021 questionnaire" or ask your teacher for a printout). (a) Find two questions with fixed options and two that are
open. (b) Find one question that could be affected by social pressure. (c) Why does the census *count* everyone
instead of sampling?

**R2. Real-time statistical questions (RD-06).** Look at the Open-Meteo or DHM weather for your town. Write three
statistical questions you could answer with a year of daily temperatures (one describe, one compare, one relate).
*Offline fallback:* write them about `climate_monthly_synthetic.csv`.

**R3. Sample vs whole (class data).** Using `class_survey_synthetic.csv` (printed), choose 6 students with a die
(roll twice: first roll = tens digit 0–3, second roll = units digit; ignore numbers outside 01–36). Compare your
sample's mean travel time with the class mean of 29.7 minutes. Pool all the samples from the class on the board: how
far away from 29.7 are most samples?

## Unit project: Our survey plan
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Plan (do not yet run) a survey of your
class: one statistical question, 5–8 neutral questions with options and units, a sampling method, and a list of
possible biases with how you will reduce each. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* "The census, explained" pages on the NSO website (<https://censusnepal.cbs.gov.np>).
* Try the "Sampling" simulation in CODAP or draw slips again 10 times and plot the 10 means as dots: you have just
  invented the idea behind Grade 11 Unit 3.
