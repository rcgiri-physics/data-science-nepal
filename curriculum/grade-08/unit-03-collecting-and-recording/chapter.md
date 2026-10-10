# Grade 8 · Unit 3: Collecting and recording

> Track: A (no-code) · Tools: paper, tally sheets, optional spreadsheet · Lessons: 3
> Datasets: `class-survey-synthetic`

**Big idea.** Good data start with consent, careful recording and a clean table. Messy recording makes every later step harder.

**What you will be able to do**

* I can collect data with consent.
* I can use tally marks and frequency tables.
* I can record data in a tidy table with units.

**Words to know:** consent (सहमति), tally (गणना चिह्न), frequency (बारम्बारता), tidy table, anonymous (बेनामी), missing value (हराएको मान). Full list: `curriculum/framework/glossary.md`.

### Before you start
From Unit 2: a statistical question, a neutral survey, and a fair (random) sample. Now we actually collect the data.

---

## Lesson 1: Consent and privacy

**Hook (5 min).** Would you be happy if your height, your marks and your family's income were pinned on the school
notice board next to your name? Which of those would bother you most, and why?

### Explanation
Data about people belong, in an important sense, to those people. Before collecting data from anyone we need their
**consent** (सहमति): a free, informed "yes".

* **Free:** they can say no, or stop halfway, with no punishment and no pressure. A teacher asking students puts
  pressure on them just by being the teacher, so make "no" easy (for example, a blank slip counts as "no").
* **Informed:** they know *what* you will collect, *why*, *who* will see it, and *what happens to it afterwards*.
* For students under 18, parents or guardians may also need to agree for anything beyond simple classroom
  activities (see `community/student-data-consent.md`).

**Privacy** means people control who sees information about them. We protect privacy by:

1. **Collecting only what we need.** If the question is about travel time, do not ask about caste or income.
2. **Using codes instead of names.** S01, S02… The list linking codes to names (if one is needed at all) is kept by
   the teacher and destroyed afterwards. Data with codes and no names are called **anonymous** or
   **de-identified**.
3. **Being careful with small groups.** In a class with only one Tamang student who cycles, the row "Tamang,
   bicycle, 32 minutes" identifies that person even without a name. Combine small groups or do not publish them.
4. **Some data are sensitive:** health, disability, caste/ethnicity, religion, family income, marks. Ask only with a
   very good reason and extra care.

**A consent statement** (2–4 lines) says: who you are, why you are collecting, what you will collect, who will see
it, and that saying no is fine. Example:

> *We are Grade 8 Section B, studying how students travel to school. We will record your travel mode and time with a
> code, not your name. Only our class will see the table, and we will shred the paper after the project. You can say
> no or skip any question.*

### Activity (20 min)
1. In pairs, role-play asking for consent: one asks, one may say yes or no. Swap.
2. As a class, write a consent statement for the travel survey you will run in Lesson 2.
3. Assign anonymous codes: the teacher reads the roll list privately and gives each student a slip with a code.
4. Discuss: which variables in `class_survey_synthetic.csv` would be sensitive in a real class? Which could identify
   a person even without a name?

### Common mistakes
* Writing names "just for convenience". Use codes from the start.
* Thinking consent is needed only for "serious" data. Every survey of people needs it.
* Collecting extra variables "in case they are useful". Collect only what your question needs.

**Check (5 min).**
1. Why do we use codes instead of names?
2. What should a consent statement say?
3. Is it ok to publish a table of each student's weight with names?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Tally and frequency

**Hook (5 min).** Count how many of you walk, take a bus, cycle or come by motorbike. How do you keep track without
losing count when people call out answers quickly?

### Explanation
A **tally** records each observation with one stroke. Every fifth stroke crosses the previous four: `||||` with a line
through it, written here as `卌`. Groups of five make counting fast and mistakes easy to spot.

| Count | Tally |
|---|---|
| 3 | `|||` |
| 5 | `卌` |
| 7 | `卌 ||` |
| 12 | `卌 卌 ||` |

A **frequency table** lists each category with its **frequency** (बारम्बारता), the number of times it occurs. Add
a **total** row: it must equal the number of people asked. If it does not, someone was counted twice or missed.

**Worked example.** The 36 students in `class_survey_synthetic.csv` travel like this:

| Travel mode | Tally | Frequency | Relative frequency |
|---|---|---|---|
| walk | `卌 卌 卌 卌 卌 |` | 26 | 26/36 ≈ 0.72 = 72% |
| bus | `卌` | 5 | 5/36 ≈ 14% |
| bicycle | `|||` | 3 | 3/36 ≈ 8% |
| motorbike | `||` | 2 | 2/36 ≈ 6% |
| **Total** | | **36** | **100%** |

**Relative frequency** = frequency ÷ total. It lets us compare groups of different sizes: 26 walkers out of 36 (72%)
is a bigger share than 30 walkers out of 50 (60%), even though 30 > 26. (Rounded percentages may add to 99% or 101%;
that is fine, just say so.)

For **numerical** data with many different values (travel minutes from 5 to 54), we group values into **classes** of
equal width, such as 0–9, 10–19, 20–29… and tally each class. This is a *grouped frequency table*, the basis of the
histogram in Unit 4.

| Minutes | 0–9 | 10–19 | 20–29 | 30–39 | 40–49 | 50–59 | Total |
|---|---|---|---|---|---|---|---|
| Frequency | 2 | 7 | 9 | 7 | 7 | 4 | 36 |

### Activity (20 min)
1. Draw a tally sheet on the board with the categories walk, bus, bicycle, motorbike, other.
2. Each student comes up and adds one stroke (or a "tally-keeper" records answers called out in turn).
3. Copy the tally into a frequency table with a total row and a relative frequency column.
4. Check: does the total equal the number of students present today? If not, find out why.
5. Extension: collect travel minutes too and build a grouped frequency table with classes 0–9, 10–19, …

### Common mistakes
* Forgetting the total, or a total that does not match the number asked.
* Overlapping classes like 10–20 and 20–30 (where does 20 go?). Use 10–19, 20–29.
* Classes of unequal width without saying so.

**Check (5 min).**
1. Tally for 7 is…
2. In a frequency table the counts must add to…
3. Frequencies: walk 12, bus 5, cycle 3. How many students?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: A tidy table

**Hook (5 min).** Two students recorded "travel: 20 min" and "travel: half an hour". A third wrote "far". Can we
compare them easily? What would you need to do first?

### Explanation
Raw answers are often messy. Before analysing we put them into a **tidy table**. The rules (we meet them again in
Grade 9 with spreadsheets and Grade 10 with Python) are:

1. **One row per case** (one student).
2. **One column per variable**, with a short clear name (`travel_minutes`, not "How long does it take you to come to
   school?").
3. **One value per cell.** Not "walk + bus"; if that matters, make a rule (main mode only) or two columns.
4. **One unit per column**, written in the column name or a note. Decide the unit *before* collecting.
5. **Consistent spelling of categories:** `walk`, not "Walk", "walking" and "on foot" in the same column.
6. **Missing values are marked, not guessed.** Use a clear marker such as `NA` (not available), and never 0 unless
   the true answer is zero. Zero siblings is a real answer; "did not answer" is missing.

**Worked example.** Messy answers on paper slips:

| Slip | What was written |
|---|---|
| A | "Walk, about 20 min, 2 brothers 1 sister" |
| B | "bus — half an hour" |
| C | "Walking. 1 hr" |
| D | "Cycle 15 minutes, no siblings" |
| E | "bus, 25" (siblings left blank) |

Tidy table (unit: minutes; siblings = brothers + sisters):

| student_code | travel_mode | travel_minutes | siblings |
|---|---|---|---|
| S01 | walk | 20 | 3 |
| S02 | bus | 30 | NA |
| S03 | walk | 60 | NA |
| S04 | bicycle | 15 | 0 |
| S05 | bus | 25 | NA |

Notice: "half an hour" → 30, "1 hr" → 60; "Walking" → `walk`; "Cycle" → `bicycle`; blank siblings → `NA`, not 0.
For slip E we assumed 25 means minutes, which is reasonable but is an **assumption**; write it down in a short
"notes" list under the table.

### Activity (20 min)
1. Collect the class's raw paper answers from Lesson 2 (or use 10 messy slips your teacher writes).
2. Agree on column names, units and category spellings as a class *before* anyone copies.
3. Each pair converts 5 slips into tidy rows.
4. Swap with a neighbour and check: any mixed units? Any blanks recorded as 0? Any spelling differences?
5. Write the "notes" list: every assumption you made.

### Common mistakes
* Mixing units (minutes and hours) in one column.
* Writing 0 for a missing value: it changes the average.
* Different spellings of the same category, which split one group into several when counting.

**Check (5 min).**
1. Why should every value in travel_minutes use minutes?
2. What should one row be in our class table?
3. A blank cell means…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Collect data about people only with **free, informed consent**; collect only what you need.
* Use **codes, not names**; take care with small groups and sensitive variables.
* **Tallies** in groups of five, then a **frequency table** with a total that equals the number asked.
* **Relative frequency** (share or percent) compares groups of different sizes.
* Group numerical values into equal, non-overlapping **classes**.
* A **tidy table**: one row per case, one column per variable, one value per cell, one unit per column, consistent
  categories, missing marked as `NA` and assumptions written down.

## Practice exercises
1. ★ Draw the tally for 4, 9 and 13.
2. ★ Write a 3-line consent statement for a survey about breakfast habits.
3. ★ A frequency table shows: Maths 12, Social 11, Nepali 6, Science 5, English 2. How many students? What percent
   chose Maths? (Round to the nearest whole percent.)
4. ★★ Class A: 18 of 30 walk. Class B: 21 of 42 walk. Which class has a bigger *share* of walkers?
5. ★★ Make a grouped frequency table for these heights (cm) with classes 135–139, 140–144, …:
   139, 141, 143, 143, 145, 146, 148, 150, 152, 155, 155, 156, 159, 160, 161, 165, 166, 170.
6. ★★ Tidy these answers into a table with columns `code, sleep_hours, wake_time`: "8 hrs, up at 6" · "seven and a
   half hours, wake 5:30" · "I sleep at 10 and wake at 6" · "don't know". List your assumptions.
7. ★★ Why is it a problem to write "0" when a student does not say how many siblings they have? Use the mean to
   explain.
8. ★★★ A class table has one Rai student who comes by motorbike. The table has no names. Could someone still
   identify that student? What should you do before sharing the table with another class?
9. ★★★ A student wants to record "travel mode" when some students walk part of the way and take a bus for the rest.
   Suggest two different tidy ways to record this, and one advantage of each.
10. ★★★ Your school wants to collect students' health data (height, weight, eyesight). Write three rules for keeping
    this data private.

## Exercises with real data
**R1. Tally real earthquakes (RD-05).** Your teacher downloads the USGS list of earthquakes in the Nepal region in
2015 with magnitude 4 or more (link in `docs/datasets/free-datasets.md`) and prints the `mag` column (about 300
values), or shows it on a screen. Make a tally and grouped frequency table with classes 4.0–4.4, 4.5–4.9, 5.0–5.4,
5.5–5.9, 6.0 and over. Which class has the most earthquakes? Where is the 7.8 Gorkha earthquake of 25 April 2015?
*Be kind: some classmates' families were affected; anyone may choose fallback data instead.*
*Offline fallback:* tally `travel_minutes` from the class table in classes of 10.

**R2. Check a real table for tidiness (RD-09).** Look at the Open Data Nepal table *Annual rainfall by station
2004–2015*. Which tidy-table rules does it follow? Does it have one row per station or one row per station-year? Are
there missing values, and how are they marked?
*Offline fallback:* check `air_daily_synthetic.csv` (it uses `-999` for sensor errors: is that a good marker?).

**R3. A real collection (RD-20).** With consent, record the travel mode and travel time of 20 students from another
class (codes only). Build the tally, frequency table and tidy table. Write your notes list.

## Unit project: Collect our class data
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Run the survey you planned in Unit 2: get
consent, collect, tally, build the tidy class table with a notes list. This table is used in Units 4–7. Full brief and
rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Read `community/student-data-consent.md`: the consent form this project uses for real student data.
* Hadley Wickham's article "Tidy Data" (Journal of Statistical Software, 2014) is where the tidy rules come from; it
  is advanced, but the first two pages are readable after this unit.
