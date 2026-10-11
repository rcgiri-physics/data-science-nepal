# Grade 8 · Unit 5: Summarising data

> Track: A (no-code) · Tools: paper, calculator · Lessons: 3
> Datasets: `class-survey-synthetic`

**Big idea.** One number can summarise a whole list — but which number depends on the shape of the data and the question.

**What you will be able to do**

* I can find mean, median, mode and range.
* I can choose the best summary for a skewed list.
* I can explain what a summary hides.

**Words to know:** mean (मध्यक / औसत), median (मध्यिका), mode (बहुलक), range (विस्तार), outlier (अपवादात्मक मान), spread, skewed. Full list: `curriculum/framework/glossary.md`.

### Before you start
From Unit 4: dot plots and histograms show where values cluster and how spread out they are. In this unit we put
those two ideas, **centre** and **spread**, into numbers. Your Grade 8 Maths book covers the formulas; here we focus
on choosing and interpreting them.

---

## Lesson 1: Mean, median and mode

**Hook (5 min).** Five students' pocket money for a week: 20, 20, 30, 40, 90 rupees. What is a "typical" amount?
Each of you write one number before we calculate anything.

### Explanation
A **measure of centre** is one number that stands for a whole list. There are three common ones.

**Mean** (average) = sum of all values ÷ number of values.
For 20, 20, 30, 40, 90: sum = 200, count = 5, mean = 200 ÷ 5 = **40** rupees.
Think of the mean as **fair sharing**: if the five students put all their money in one pot (Rs 200) and shared it
equally, each would get Rs 40. It is also the **balance point** of a dot plot: if the number line were a see-saw with
the dots as weights, it would balance at the mean.

**Median** = the middle value when the list is **sorted**.
* Odd count: the middle one. 20, 20, **30**, 40, 90 → median = **30**.
* Even count: the mean of the two middle values. 10, 12, **18**, **20**, 27, 31 → median = (18 + 20) ÷ 2 = **19**.
* Position of the median in a sorted list of *n* values: the ((n + 1) ÷ 2)th value. For n = 36 that is the 18.5th,
  i.e. halfway between the 18th and 19th.
Half the values are at or below the median and half at or above.

**Mode** = the most frequent value (or category). 20, 20, 30, 40, 90 → mode = **20**. A list can have two modes
(**bimodal**) or none (all values different). The mode is the only centre that works for **categorical** data: the
modal travel mode in our class is "walk".

**Range** = largest − smallest. It is a simple measure of **spread**: 90 − 20 = **70** rupees.

**Worked example: the whole class.** Travel minutes for the 36 students, sorted:

5, 7, 10, 10, 10, 11, 12, 18, 19, 20, 21, 23, 27, 27, 27, 27, 28, **29, 30**, 31, 32, 33, 35, 35, 37, 40, 40, 41, 42,
42, 43, 48, 50, 52, 53, 54

* Sum = 1,069; mean = 1,069 ÷ 36 ≈ **29.7** minutes.
* The 18th and 19th values are 29 and 30; median = **29.5** minutes.
* Mode = **27** minutes (four times). Range = 54 − 5 = **49** minutes.

Mean and median are almost the same here, because the dot plot is roughly **symmetric**: no extreme values pull one
side.

### Activity (20 min)
1. Compute mean, median, mode and range for the pocket-money list (check: 40, 30, 20, 70).
2. Take the class's own `travel_minutes` (or the 36 values above). Sort them on a strip of paper, then find all four.
3. **Human median:** the whole class lines up in order of travel time. The person in the middle (or the two in the
   middle) is the median. Ask: if the student with the longest trip suddenly moved twice as far away, would the
   median change? Would the mean?

### Common mistakes
* Forgetting to **sort** before finding the median.
* Giving the *position* of the median (18.5th) instead of its *value* (29.5).
* Thinking the mode is the biggest value. It is the most *frequent*.
* Rounding too early; round only the final answer.

**Check (5 min).**
1. Mean of 20, 20, 30, 40, 90?
2. Median of 20, 20, 30, 40, 90?
3. Mode and range?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Which summary when?

**Hook (5 min).** A village has 9 families earning about 15,000 rupees a month and one family (the owner of a hydro
company) earning 300,000. A news report says "the average family in the village earns 43,500 rupees". Is that fair?

### Explanation
An **outlier** is a value far from the rest. Outliers can be real (a rich family, a very long journey) or errors (a
height of 1,550 cm). Either way, they affect the mean far more than the median.

**Worked example.** Incomes: nine families at 15,000 and one at 300,000.
* Mean = (9 × 15,000 + 300,000) ÷ 10 = (135,000 + 300,000) ÷ 10 = 435,000 ÷ 10 = **43,500**.
* Median: sorted, the 5th and 6th values are both 15,000 → median = **15,000**.
Nine of the ten families earn far less than the "average". The mean is pulled up by one value; the median ignores
how far away the extreme value is and only cares that it is on the high side.

When a dot plot or histogram has a **long tail** on one side, the data are **skewed**:
* **Right-skewed** (long tail to the right, towards big values): incomes, land owned, distance to school, house prices,
  earthquake magnitudes. Mean > median.
* **Left-skewed** (long tail to the left): marks on an easy test (most score high, a few very low). Mean < median.
* **Symmetric**: mean ≈ median.

**Which summary to report**

| Situation | Best centre | Why |
|---|---|---|
| Roughly symmetric numbers, no outliers | mean (or median) | mean uses every value |
| Skewed numbers or outliers | median | not pulled by extremes |
| Categories | mode | the only one that makes sense |
| You need a total (e.g. food for a trip) | mean | total = mean × count |

It is often best to report **both** mean and median; the gap between them tells the reader the data are skewed.

### Activity (20 min)
1. Compute the mean and median income with and without the hydro-company family. Which summary changed more?
2. In groups, decide which number a newspaper should report and write the headline. Then write a headline that is
   technically true but misleading.
3. For each list, decide the best centre and say why: (a) marks out of 20: 15, 16, 16, 17, 18, 18, 19; (b) minutes
   of daily load-shedding in five towns: 0, 0, 0, 0, 240; (c) favourite fruits: mango, apple, mango, banana, mango.

### Common mistakes
* Always reporting the mean because "average means mean".
* Deleting outliers to make the numbers look nicer. Check them; keep real ones and say how they affect the summary.
* Saying "most people earn the average": with skewed data, most people earn less than the mean.

**Check (5 min).**
1. Incomes: 9 × 15,000 and 1 × 300,000 — mean?
2. Median of the same list?
3. Which is more typical and why?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Spread and what summaries hide

**Hook (5 min).** Two classes both have a mean of 8 hours of sleep. Are the two classes the same? What might be
different?

### Explanation
Centre is half the story. **Spread** (variability) tells us how much values differ from each other. Two groups can
share a mean and be very different:

| | Values (hours of sleep) | Mean | Range |
|---|---|---|---|
| Class A | 7, 8, 8, 9 | 32 ÷ 4 = 8 | 9 − 7 = 2 |
| Class B | 5, 6, 10, 11 | 32 ÷ 4 = 8 | 11 − 5 = 6 |

In Class A everyone sleeps about 8 hours. In Class B half the students sleep too little and half sleep a lot. A
health worker would worry about Class B, and the mean alone would hide that.

The **range** is easy but uses only the two most extreme values, so one outlier can make it huge. In Grade 10 you
will learn better measures of spread (interquartile range and standard deviation). For now: **always look at the
graph, not just the summary.** The famous lesson of statistician Francis Anscombe's "quartet" (1973) is that very
different data can have identical summaries.

A complete description of a numerical variable mentions:
1. **Centre** (median or mean, with unit);
2. **Spread** (range, with unit);
3. **Shape** (symmetric, skewed, clusters, gaps);
4. **Unusual values** (outliers, and whether they look real or like errors).

Example: "Travel times in our class are centred around 30 minutes (median 29.5), and spread from 5 to 54 minutes
(range 49). The distribution is roughly symmetric with no outliers; most students take between 10 and 50 minutes."

### Activity (20 min)
1. For Class A and Class B, compute the mean and range, and draw both dot plots on **the same number line** (one
   above the other).
2. Write one sentence comparing them that a health worker would find useful.
3. Using the class `sleep_hours` column, write the four-part description (centre, spread, shape, unusual values).

### Common mistakes
* Describing data with the centre alone.
* Forgetting units ("the range is 6": 6 what?).
* Thinking a big range always means most values are spread out: one outlier is enough.

**Check (5 min).**
1. Mean of class A (7, 8, 8, 9)?
2. Mean and range of class B (5, 6, 10, 11)?
3. What do these tell us that the means alone do not?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* **Mean** = sum ÷ count (fair share, balance point). **Median** = middle of the sorted list. **Mode** = most
  frequent. **Range** = max − min.
* Outliers and skew pull the mean towards the tail; the **median** resists them.
* Right-skewed data (incomes, distances): mean > median. Report the median, or both.
* For categories use the **mode**.
* Describe a variable with **centre, spread, shape and unusual values**, always with units, and always look at the
  graph.

## Practice exercises
1. ★ Find the mean, median, mode and range of: 4, 7, 7, 8, 9, 12.
2. ★ Find the median of: 31, 12, 45, 19, 27, 38, 22 (careful!).
3. ★ What is the modal favourite subject in the class table (Maths 12, Social 11, Nepali 6, Science 5, English 2)?
   Why can you not find the mean favourite subject?
4. ★★ Six students' marks are 12, 15, 15, 16, 18 and one missing. The mean of all six is 15. What is the missing mark?
5. ★★ The daily wages (Rs) of 7 workers are 800, 850, 850, 900, 950, 1,000 and 6,000 (the supervisor). Find the mean
   and median. Which better describes a typical worker?
6. ★★ Rainfall in mm on the 10 days of a trek: 0, 0, 0, 2, 0, 35, 0, 0, 1, 0. Find the mean, median and mode. Which
   one would you tell someone planning the trek, and why?
7. ★★ Write a list of 5 numbers with mean 10 and median 8.
8. ★★ Write a four-part description of the class `height_cm` column using these summaries: min 139 cm,
   median 155 cm, mean 155.4 cm, max 171 cm, mode 155 cm, and no value far from the others.
9. ★★★ "The average Nepali household owns 1.2 hectares of land, so most households own about 1.2 hectares." Explain
   why this could be false.
10. ★★★ A school reports the mean SEE GPA rose from 2.8 to 3.0. Give two different stories about the students that
    would both produce this change.

## Exercises with real data
**R1. Rain at stations across Nepal (RD-09).** From the Open Data Nepal table *Annual rainfall by station*, choose one
year and 10–15 stations. Find the mean, median and range of annual rainfall. Is the distribution skewed? Which
station is the outlier, and is it plausibly real? (Hint: some stations near Pokhara get more than 3,500 mm a year.)
*Offline fallback:* the 12 values of `rain_mm` for one year in `climate_monthly_synthetic.csv`.

**R2. Earthquake magnitudes (RD-05).** Using the 2015 USGS list (≈300 values of `mag`), find the median and mode
magnitude (sorting 300 values by hand is long: work in groups, one class interval each, or use a spreadsheet's
`MEDIAN` and `MODE` functions). Would the mean be above or below the median? Why?

**R3. Prices at the market (RD-08).** Take one week of tomato prices (minimum and maximum, Rs per kg) from the
Kalimati dataset or from today's prices on <https://kalimatimarket.gov.np>. Compute the mean of the daily averages
and the range over the week. Repeat for one week in a different season. Write two sentences comparing them.

## Unit project: What's typical in our class?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose two numerical variables from your
class table. For each: compute mean, median, mode and range; draw a dot plot; mark any outliers; write the four-part
description; and state which centre you would report and why. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Khan Academy, "Summarizing quantitative data" (free videos and practice, English):
  <https://www.khanacademy.org/math/statistics-probability>.
* Search "Anscombe's quartet" or "Datasaurus Dozen": a dinosaur and a star with exactly the same mean and spread.
