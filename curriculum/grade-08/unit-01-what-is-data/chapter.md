# Grade 8 · Unit 1: What is data?

> Track: A (no-code) · Tools: paper, calculator · Lessons: 3
> Datasets: `class-survey-synthetic`

**Big idea.** Data are recorded facts about people, places or things. Before we analyse anything we must know what one row is, what each column measures, and who collected it.

**What you will be able to do**

* I can tell numerical from categorical data.
* I can name who collects some of Nepal's official data.
* I can read a small table: rows, columns, units.

**Words to know:** data (तथ्याङ्क), variable (चर), categorical (वर्गीय), numerical (सङ्ख्यात्मक), row (पङ्क्ति), column (स्तम्भ), unit (एकाइ). Full list: `curriculum/framework/glossary.md`.

### Before you start
Nothing! This is the first unit of the book. You need a pencil, a notebook and some curiosity. If you have done
statistics in Grade 7 or 8 Maths (mean, bar charts) that will help later, but it is not needed here.

---

## Lesson 1: Data are everywhere

**Hook (5 min).** Write five facts about yourself that someone could record on a form: for example your age, the
village or tole you live in, how you come to school, how many minutes it takes, your favourite subject.
*Predict first:* which of your five facts could you add up or average with a classmate's?

### Explanation
**Data** are facts that someone has *recorded* so they can be looked at later. Your age in the school register, the
rainfall measured each morning at the Kathmandu airport weather station, the price of tomatoes at Kalimati market
today: all of these are data. A fact you only remember is not yet data; once it is written in a register, typed into
a phone or stored in a computer, it becomes data that other people can use.

A **variable** is one kind of fact that can *vary*, that is, be different from one person (or place, or day) to the
next. "Minutes to reach school" is a variable: Sita takes 10 minutes, Bikash takes 45. "Name of our school" is not a
variable inside our class, because it is the same for everyone.

Variables come in two main types, and almost everything we do later depends on telling them apart.

| Type | What it does | Examples | Can we average it? |
|---|---|---|---|
| **Numerical** (सङ्ख्यात्मक) | Counts or measures an amount | age in years, height in cm, number of siblings, rainfall in mm, price in rupees | Yes |
| **Categorical** (वर्गीय) | Puts things into groups or labels | travel mode (walk/bus/cycle), mother tongue, favourite subject, province, ward number | No: we count how many are in each group |

There are two sub-types of numerical data. **Counts** can only be whole numbers (siblings: 0, 1, 2…). **Measurements**
can take any value in between (height 154.5 cm). Both are numerical.

**The ward-number trap.** Ward 4 is written with a number, but it is a *label*. If one student lives in ward 2 and
another in ward 6, their "average ward" is 4, which is nonsense: ward 4 might be on the other side of town. The test
is simple: **does doing arithmetic on it make sense?** If not, it is categorical even if it looks like a number.
Phone numbers, roll numbers, SEE symbol numbers and postal codes are all categorical for the same reason.

**Worked example.** A Grade 8 class in Dhangadhi fills in this form. Classify each variable.

| Question on the form | Type | Why |
|---|---|---|
| How many minutes does it take you to reach school? | numerical (measurement) | an amount of time |
| How do you usually come to school? | categorical | groups: walk, bus, cycle, motorbike |
| How many brothers and sisters do you have? | numerical (count) | whole numbers |
| Which ward do you live in? | categorical | a label, not an amount |
| What is your mother tongue? | categorical | groups: Tharu, Nepali, Doteli, Maithili… |
| How tall are you? | numerical (measurement) | in centimetres |

### Activity (20 min)
1. In groups of three, take the 20 variable cards (worksheet `w1-sort-cards.md`) or write them yourselves:
   height, mother tongue, ward number, shoe size, bus or walk, rainfall in mm, number of goats at home, blood group,
   temperature in °C, mobile phone brand, date of birth, house number, marks in Maths, favourite festival, minutes of
   load-shedding, caste/ethnic group, number of rooms at home, district, school roll number, kilometres to the
   nearest health post.
2. Sort them into two piles, **numerical** and **categorical**.
3. Put the cards your group argued about in a third pile called **tricky**. Shoe size, date of birth, marks and
   house number usually end up here. For each tricky card, apply the arithmetic test and write one sentence.
4. Groups compare piles. Any card two groups disagree on is discussed by the whole class.

*Computer version:* make the same two lists in a spreadsheet, one column for the variable and one for its type.

### Common mistakes
* "It has a number in it, so it is numerical." Check the arithmetic test: roll numbers and wards fail it.
* "Data must be numbers." Names of festivals and mother tongues are data too; most of Nepal's census is categorical.
* Confusing a *variable* (a column, such as "height") with a *value* (one entry, such as "152 cm").

**Check (5 min).**
1. Is 'favourite colour' numerical or categorical?
2. Give one numerical variable about your school.
3. Why is a ward number categorical even though it looks like a number?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Who collects Nepal's data?

**Hook (5 min).** Who tells us how many people live in Nepal? Who tells us tomorrow's weather? Who knows how many
students are in Grade 8 in your district? How do *they* know? Predict an answer for each before the lesson.

### Explanation
Most of the numbers you read in newspapers come from a few organisations whose job is to collect data carefully and
regularly. Knowing **who collected the data and why** is the first step in deciding how far to trust it.

| Organisation | What it collects | Example you can look up |
|---|---|---|
| **National Statistics Office (NSO)** (राष्ट्रिय तथ्याङ्क कार्यालय), formerly the Central Bureau of Statistics | the census every ten years; surveys of living standards, labour, agriculture | Census 2021: 29,164,578 people (final result) |
| **Department of Hydrology and Meteorology (DHM)** | rainfall, temperature, river levels from stations across Nepal | daily weather and monsoon reports |
| **Ministry of Education, Science and Technology** and the **Center for Education and Human Resource Development** | schools, teachers, enrolment ("Flash reports") | number of students by grade and district |
| **Department of Health Services** | health-post and hospital records (HMIS), vaccinations | immunisation coverage |
| **Nepal Rastra Bank** | prices, inflation, remittances, exchange rates | monthly inflation |
| **Election Commission** | voter lists and election results | registered voters by district |
| **Your school** | attendance, marks, enrolment | the class register |

A **census** counts *everyone*. Nepal's 2021 census was the twelfth. A **survey** asks only a *sample* of people and
uses their answers to estimate the whole country, which is cheaper and faster but less exact (Unit 2 explores
this). **Administrative data** are collected as a side effect of running something: the school register exists to
track attendance, but it also tells us how many students attend.

Every collector has a **purpose**, and the purpose shapes the data. The school register records who came to school,
not *why* someone was absent. A weather station at an airport measures the airport, not the village on the hill
above it. When you meet a dataset, ask the four source questions:

1. **Who** collected it?
2. **Why** did they collect it?
3. **How** did they collect it: counted, measured, asked?
4. **When** and **where** was it collected, and who might be missing?

### Activity (20 min)
1. Your teacher gives (or writes up) eight questions:
   *How many students are in Grade 8 in my district? How much rain fell in Pokhara in July? How many people speak
   Maithili as their mother tongue? What is the price of onions this week? How many babies received the measles
   vaccine last year? How many tourists came to Nepal last year? How many voters are registered in my ward? How many
   students were absent from our class yesterday?*
2. In pairs, match each question to the organisation most likely to collect the answer.
3. Choose one and answer the four source questions about it. For "Why did they collect it?", think of the job the
   organisation is trying to do.
4. Share: which question was hardest to match, and why?

### Common mistakes
* Believing a number because it is "official". Official data can be old, incomplete or measured differently from
  what you think. Ask the four source questions every time.
* Thinking a survey counts everyone. Only a census tries to.

**Check (5 min).**
1. Which organisation runs the national census?
2. Why should we ask 'who collected this data and why'?
3. Name one thing a school could measure itself.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Reading a table

**Hook (5 min).** Look at this table of five students. Before reading anything else, say: what is one row? What is
one column?

| student_code | travel_mode | travel_minutes | siblings | height_cm |
|---|---|---|---|---|
| S01 | walk | 53 | 0 | 155 |
| S02 | motorbike | 27 | 5 | 165 |
| S03 | walk | 40 | 0 | 160 |
| S04 | bicycle | 23 | 1 | 155 |
| S05 | bicycle | 11 | 1 | 145 |

### Explanation
A data table is the most common way to store data, and almost every tool you will meet (paper, spreadsheet, SQL,
Python) uses the same idea:

* each **row** is one *case*: one student, one district, one day;
* each **column** is one *variable*;
* each **cell** holds one *value*.

The column names tell you the variable, and the part after the underscore often tells you the **unit**:
`travel_minutes` is in minutes, `height_cm` in centimetres. A number without a unit is a mystery: is 160 the height
in centimetres, or the weight of a sack of rice in kilograms?

`student_code` is an **identifier**: it tells us *which* student the row belongs to without naming them. It is not a
variable we analyse; we never average codes.

**How to read a table in five steps**

1. Read the **title and source**: what is this about, who made it, when?
2. Decide what **one row** is.
3. Go through the **columns**: name, type (numerical or categorical) and unit.
4. Look for **blanks or odd values** (a height of 16 cm is probably a typing error for 160).
5. Write **one question** the table could answer, and one it *cannot*.

**Worked example** with the table above.
1. No title or source is shown, which is a weakness; we should ask.
2. One row = one student.
3. `travel_mode` categorical; `travel_minutes` numerical, minutes; `siblings` numerical count; `height_cm` numerical,
   centimetres; `student_code` identifier.
4. Nothing odd, but S01 walks for 53 minutes, which is long; worth checking, not deleting.
5. Can answer: "Do students who walk take longer than those who cycle?" Cannot answer: "Why does S02 come by
   motorbike?" (no column for that) or "How do students in another school travel?" (they are not in the table).

### Activity (20 min)
1. Use the printed 10-row class table (worksheet `w2-read-a-table.md`).
2. Circle one row and write what it represents.
3. Underline one column; for every column write its type and unit.
4. Find anything that looks odd and write why.
5. Write one question the table *can* answer and one it *cannot*. Swap with a neighbour and check each other.

### Common mistakes
* Counting the identifier as a variable to analyse.
* Ignoring units: comparing 1.5 (hours) with 90 (minutes) as if 90 were bigger.
* "Fixing" an odd value by guessing. Mark it and ask the person who recorded it.

**Check (5 min).**
1. A table has columns: student_code, travel_mode, travel_minutes, height_cm. How many variables?
2. Which of those are numerical?
3. What does one row represent?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Data are recorded facts; a **variable** is a fact that varies between cases.
* **Numerical** variables count or measure; **categorical** variables label groups. Use the arithmetic test.
* Numbers used as labels (ward, roll number, phone number) are categorical.
* Nepal's official data come from the NSO, DHM, the education and health ministries, Nepal Rastra Bank and others.
* Always ask **who, why, how, when/where** about a dataset.
* In a table, one row is one case, one column is one variable; check units and identifiers before analysing.

## Practice exercises
★ = recall · ★★ = apply · ★★★ = think deeper

1. ★ Classify as numerical or categorical: (a) district, (b) monthly rainfall in mm, (c) blood group,
   (d) number of mobile phones in a household, (e) SEE symbol number, (f) weight of a newborn baby.
2. ★ For each numerical variable in question 1, say whether it is a count or a measurement.
3. ★ Name the organisation you would ask for: (a) the number of tourists in 2019, (b) the rainfall in Jumla last
   August, (c) the inflation rate last month.
4. ★★ A form asks "Age: ____". Ramesh writes "13", Gita writes "13 years 4 months", Hari writes "2068 BS". Why is
   this a problem, and how should the form be improved?
5. ★★ Write a table with 4 rows and 4 columns about your family or friends (use codes, not names). Label one row,
   one column, and give every numerical column a unit.
6. ★★ "Exam marks" can be numerical, but "Division" (Distinction, First, Second) is categorical. Explain the
   difference using the arithmetic test. Is there an order in the categories? (Categories with a natural order are
   called **ordinal**.)
7. ★★ The school register says 42 students were present on Monday. List two things the register cannot tell you.
8. ★★★ A news site says "Nepal's population is 30 million". Which of the four source questions would you ask first,
   and why?
9. ★★★ Temperature in °C is numerical. Is it sensible to say 20 °C is "twice as hot" as 10 °C? Discuss. (Hint: what
   does 0 °C mean?)
10. ★★★ Design a 6-question form to learn how students in your school use mobile phones. Make at least two questions
    numerical and two categorical, and give the unit for every numerical one.

## Exercises with real data
These use free datasets from `docs/datasets/free-datasets.md`. No internet? Use the offline fallback.

**R1. Tourists in Nepal (RD-10).** Your teacher downloads the Open Data Nepal file *Total annual tourist arrivals by
mode of transportation, 2001–2014* and prints it (it has about 14 rows).
(a) What is one row? (b) List every column with its type and unit. (c) Answer the four source questions using the
dataset page. (d) Write one question the table can answer and one it cannot.
*Offline fallback:* use `class_survey_synthetic.csv` (printed) and answer (a)–(d).

**R2. A first look at the census (RD-11 / RD-13).** Look at the Census 2021 results page
(<https://censusnepal.cbs.gov.np/results>) or a printed table of population by district.
(a) Find your own district's population. (b) Which columns are numerical and which categorical?
(c) The census asks about mother tongue: is that numerical or categorical? How many categories do you think there
are? (The 2021 census recorded more than 100 languages; check the exact number on the results page.)
*Offline fallback:* `districts_synthetic.csv` (fictional districts): repeat (b).

**R3. Data around us (RD-20).** For one week, write down one piece of data you see each day (a price, a score, a
temperature on a phone, a bus fare). For each, record: the value, the unit, the variable type and who collected it.

## Unit project: My data portrait
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Make a one-page "portrait" of yourself as
data: 8–10 variables with type and unit, a small table of one week of something you measure (sleep, travel time,
water you drink), and three sentences on what the data show and what they leave out. Full brief and rubric:
`project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* CODAP (free, in the browser, no sign-in): <https://codap.concord.org>. Open a sample document and find one
  numerical and one categorical attribute.
* National Statistics Office: <https://nsonepal.gov.np>. Browse the list of surveys it runs.
