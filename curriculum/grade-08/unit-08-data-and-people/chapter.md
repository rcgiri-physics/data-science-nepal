# Grade 8 · Unit 8: Data and people

> Track: A (no-code) · Tools: paper, case cards · Lessons: 3
> Datasets: `class-survey-synthetic`, `census-districts`

**Big idea.** Data are about people. Who is counted, who is missing, and how data are used can help or harm real lives.

**What you will be able to do**

* I can ask who is missing from a dataset and why it matters.
* I can identify sensitive data and protect privacy.
* I can judge whether a data-based decision is fair.

**Words to know:** missing data, representation, privacy (गोपनीयता), sensitive data, anonymise, fairness (निष्पक्षता), harm. Full list: `curriculum/framework/glossary.md`.

### Before you start
You met consent and codes in Unit 3, biased samples in Unit 2, and "Who or what is missing from this data?" at the
end of every lesson this year. This unit makes that question the main topic.

---

## Lesson 1: Who is missing?

**Hook (5 min).** A company runs a phone survey to find out how many children in a district go to school. It calls
2,000 households with a mobile phone. Who is never asked? Would the result be too high or too low?

### Explanation
Every dataset has edges. Some people, places or events are **inside** the data; others are **missing**. Missing
people are invisible to anyone who uses the data, and decisions made from the data may ignore them.

Common reasons people go missing:

| Reason | Example in Nepal | Likely effect |
|---|---|---|
| **No access** to the collection method | phone or online surveys miss households without phones/internet, often poorer or remote | results look better off than reality |
| **Not at home / away** | migrant workers abroad; seasonal workers; students in hostels | the "absent population" must be counted separately (the census does) |
| **No documents** | children without birth registration; people without citizenship papers | missing from school or health records |
| **Language** | forms only in Nepali or English | speakers of other languages answer less or wrongly |
| **Fear or stigma** | people may hide a disability, an illness or their caste | under-counting of sensitive groups |
| **Who was absent that day** | the attendance survey misses sick or working children | results describe only those present |
| **Unmapped places** | a village not on the map is not visited | whole communities missing |

Missing data is not only about *people*. A rainfall dataset may have no stations in the high mountains; a road-crash
dataset may record only crashes reported to the police.

**Why it matters.** If a health survey misses the poorest households, it overestimates health; resources then go to
places that look worse, and the missing places get less. "Not in the data" too easily becomes "not a problem".

**What to do about it.**
1. **Ask the question** every time: who is counted, who is missing, and how might that change the result?
2. **Use more than one method:** paper forms and visits as well as phones; several languages.
3. **Report it:** say clearly who your data do not cover (the "what we cannot say" box from Unit 7).

### Activity (20 min)
1. In groups, read three case cards: (a) a phone survey about school attendance; (b) an online poll about a new bus
   route; (c) a school's attendance report used to decide which students get a free lunch.
2. For each case, list: who is counted, who is missing, and whether the result will be too high, too low, or just
   different.
3. Suggest one change that would include more of the missing people.
4. Share one case with the class.

### Common mistakes
* Assuming the data cover "everyone" because the dataset is big.
* Thinking missing people don't matter if they are a small number. Small groups can be the ones most in need.

**Check (5 min).**
1. Who might an online poll miss?
2. Why does missing data matter?
3. How could you include more people?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Privacy and sensitive data

**Hook (5 min).** Look at this list and decide privately: which facts about you would you happily share with the whole
school? Your favourite food · your exam marks · your weight · your home address · your caste · your religion · the
name of your best friend · whether you have an illness · your family's income · your phone number.

### Explanation
**Privacy** (गोपनीयता) means people get to decide who knows things about them. Some data are **sensitive**: if they
became known, a person could be embarrassed, treated unfairly, put in danger, or lose money. Commonly sensitive data:
* health and disability;
* caste, ethnicity, religion, political opinions;
* family income, debts, land;
* exact location (home address, GPS position, daily routes);
* identity numbers (citizenship, phone numbers, passwords);
* information about children.

Different people feel differently about the same field, and that is important: you cannot decide for someone else that
"it's fine to share".

**Nepal's law.** The *Individual Privacy Act, 2075* (2018) protects personal information, including about body, home,
property, documents, data and communications; collecting and sharing personal data generally needs the person's
consent. You do not need to know the law in detail, but you should know that privacy is a **right**, not just good
manners.

**How data scientists protect privacy**
1. **Collect only what you need** (data minimisation). If the question is about travel time, do not collect caste.
2. **Anonymise:** remove names, phone numbers, addresses; use codes.
3. **Aggregate:** publish counts and summaries for groups, not individual rows.
4. **Small-group rule:** do not publish a group with fewer than 5 people (or combine small groups into "other").
5. **Keep it safe:** paper in a locked drawer; files with a password; delete when the project ends.
6. **Think about combinations:** "Grade 8, girl, cycles, lives in ward 4" may point to exactly one person even with
   no name.

### Activity (20 min)
1. Individually, rank the 10 fields from the hook from "fine to share" (1) to "very private" (10).
2. In groups, compare rankings. Where do you disagree most? Why might different people rank differently?
3. Write a "collect only what you need" checklist for your class survey (Unit 3): which variables does your
   question really need? Which could be dropped?
4. Look at the synthetic class table. Could any row be identified even without a name? Which column combinations are
   risky?

### Common mistakes
* "It's anonymous, so it's safe." Combinations of columns can still identify someone.
* Collecting sensitive data "in case it's useful".
* Sharing screenshots of class data in social media groups.

**Check (5 min).**
1. Give two sensitive data fields.
2. What does 'collect only what you need' mean?
3. Small group, 'anonymous' data — risk?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Fair or unfair?

**Hook (5 min).** A school gives scholarships using only exam marks. Rita has to work in her family's shop every
evening and scores a little lower than students who have private tuition. Is the scholarship rule fair?

### Explanation
Data are increasingly used to make **decisions** about people: who gets a scholarship, a loan, a job interview, a
place in a programme, extra help. A decision rule that uses data can look neutral ("we just use the numbers") and still
be unfair, because:

* **What is measured is not what matters.** Marks measure performance on one exam, not potential or effort under
  difficult conditions.
* **The data reflect past unfairness.** If girls in a district had fewer chances to study, their marks reflect that,
  and a rule based on marks repeats it.
* **Some people are missing or poorly measured** (Lesson 1).
* **The same rule affects groups differently.** A rule requiring an online form excludes families without internet.

**Fairness is a decision, not a number.** Data can show who benefits and who is harmed; people must then decide what
is fair. Different ideas of fairness can conflict: "treat everyone the same" vs "give more help to those who started
with less". Reasonable people disagree, and the disagreement should be open, not hidden inside a formula.

**Five questions for any data-based decision**
1. **Who collected the data, and for what purpose?**
2. **What was measured, and what was left out?**
3. **Who is missing or poorly represented?**
4. **Who benefits from the decision, and who could be harmed?**
5. **Can people see the rule, question it and appeal?**

In Grade 10 (AI literacy) and Grade 12 (fairness audit) you will apply these questions to computer models that make
predictions about people.

### Activity (20 min)
1. In groups, take one decision card: (a) scholarships by exam marks only; (b) a bank lending only to people with a
   salary slip; (c) a free-lunch programme for students whose attendance is above 90%.
2. Use the five questions to argue **for** the rule, then **against** it.
3. Suggest a change that makes the rule fairer, and say who might still lose out.
4. As a class, write "**Our data rules**" — a charter of 6–8 rules for how our class collects and uses data.

### Common mistakes
* "The computer/formula decided, so it's fair."
* Deciding fairness from your own point of view only. Ask how it looks to the person who loses out.

**Check (5 min).**
1. Name one question to ask about any data-based decision.
2. Is data always neutral?
3. Write one rule for our class data charter.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Every dataset leaves people out; missing people often have the most need. Ask **who is counted, who is missing,
  and how that changes the result**.
* Sensitive data (health, caste, religion, income, location, identity numbers, children) need extra care.
  Privacy is a right in Nepal (Individual Privacy Act, 2075).
* Protect privacy: collect only what you need, anonymise, aggregate, small-group rule, keep data safe, think about
  combinations.
* Data-based decisions can be unfair even when they "just use the numbers". Use the **five questions**.
* Fairness is decided by people, openly.

## Practice exercises
1. ★ List three groups who might be missing from a survey done only in Kathmandu by smartphone.
2. ★ Which of these are sensitive: shoe size, HIV status, favourite cricket team, citizenship number, home GPS
   location, number of siblings? Explain one choice.
3. ★ What does "aggregate" mean? Give an example from the class survey.
4. ★★ A class has one student who speaks Tamang at home. The class table (no names) shows mother tongue and travel
   mode. Explain the privacy risk and how to fix it before sharing the table.
5. ★★ A district health office counts births at hospitals only. Who is missing? Would the count be too high or too
   low? What other source could help?
6. ★★ Apply the five questions to: "Students with attendance below 80% cannot sit the final exam."
7. ★★ A rainfall map of Nepal has no stations above 4,000 m. What might someone wrongly conclude?
8. ★★★ A new app predicts which students will drop out, using attendance, marks and distance from school. Write two
   ways it could help and two ways it could harm students.
9. ★★★ "Treat everyone the same" and "give more help to those with less" are two ideas of fairness. Describe a school
   decision where they lead to different rules.
10. ★★★ Write your own data charter: 6 rules, each one sentence, for a club that collects data about members.

## Exercises with real data
**R1. Who does the census count? (RD-13).** Nepal's census reports an **absent population**: people who usually live
in a household but are abroad. On the census results page, find the absent population for Nepal or your province.
Why is it important to count them separately? Who might still be missed by the census?

**R2. Mapped and unmapped (RD-16).** Open <https://www.openstreetmap.org> and look at your municipality. Are the
schools, health posts and roads you know about on the map? Make a list of three things that are missing. Who would be
affected if a planner used only this map? (OpenStreetMap can be improved by anyone: Kathmandu Living Labs runs
mapping activities in Nepal.)

**R3. Missing stations (RD-09).** In the *Annual rainfall by station* table, how many stations are in the mountains
compared with the Terai and Hill? What does that mean for statements about "Nepal's rainfall"?

## Unit project: Our data charter
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Write and present a class data charter: 6–8
rules covering consent, privacy, missing people, fairness and honesty, each with a one-line reason and an example from
your year's work. Display it beside your Unit 7 posters. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Caroline Criado Perez, *Invisible Women* (2019): how data that leave out half the population lead to unfair
  decisions (for older students and teachers).
* Kathmandu Living Labs (<https://kathmandulivinglabs.org>): open mapping projects in Nepal.

---

### End of Grade 8: are you ready for Grade 9?
You are ready if you can:
- [ ] tell numerical from categorical variables (and spot numbers that are really labels);
- [ ] write a statistical question and a neutral survey question;
- [ ] collect data with consent and record it in a tidy table;
- [ ] draw and choose bar charts, dot plots, histograms, line graphs and pie charts;
- [ ] find and choose between mean, median, mode and range;
- [ ] compare places with rates, and use percentage points correctly;
- [ ] write a claim–evidence–reasoning statement with a limitation;
- [ ] ask who is missing and protect people's privacy.
