# Grade 8 · Unit 4: Showing data

> Track: A (no-code); optional CODAP · Tools: graph paper, optional CODAP · Lessons: 3
> Datasets: `class-survey-synthetic`, `census-districts`

**Big idea.** A graph is an argument made visible. The right graph helps the eye; a careless one can mislead.

**What you will be able to do**

* I can draw a bar chart, dot plot and line graph from a table.
* I can choose a graph that fits the data.
* I can spot a misleading graph.

**Words to know:** bar chart (स्तम्भचित्र), pie chart (वृत्तचित्र), dot plot (बिन्दुचित्र), histogram (आयतचित्र), line graph (रेखाचित्र), axis, scale, title. Full list: `curriculum/framework/glossary.md`.

### Before you start
From Unit 3: frequency tables (counts per category), grouped frequency tables for numbers, and the tidy class table.
From Unit 1: numerical vs categorical. **The type of variable decides the type of graph.**

---

## Lesson 1: Bar charts and dot plots

**Hook (5 min).** Here are 20 travel times in minutes: 53, 27, 40, 23, 11, 48, 21, 7, 12, 52, 10, 41, 27, 54, 32,
10, 5, 35, 42, 19. Without drawing anything, what is a typical time? Now look at the dot plot your teacher draws.
Which was easier?

### Explanation
Our eyes are excellent at comparing **lengths** and **positions**, and poor at comparing long lists of numbers.
A graph turns numbers into lengths and positions.

**Bar chart** — for a **categorical** variable. One bar per category; the length shows the count (or a value such as
population). Rules:
* bars have **equal width** and **gaps** between them (the categories are separate);
* the value axis **starts at zero**, because the eye compares whole bar lengths;
* order bars in a useful way: largest to smallest, or a natural order (Mountain, Hill, Terai).

**Dot plot** — for a **numerical** variable with a small number of cases (up to about 50). Draw a number line, then
put one dot for each case above its value; stack dots that land on the same value. A dot plot shows:
* where values **cluster** (most students take 20–45 minutes),
* **gaps** and **unusual values** (one student takes 90 minutes?),
* the **spread** from smallest to largest.

**Histogram** — for a numerical variable with many cases. Use the grouped frequency table from Unit 3: one bar per
class, bars **touching** (because the number line is continuous), height = frequency. Think of it as a dot plot where
dots are piled into class "buckets".

**Worked example.** From the 36-student class table:

```
Travel mode (bar chart, counts)
walk       ██████████████████████████  26
bus        █████                        5
bicycle    ███                          3
motorbike  ██                           2
           0    5    10   15   20   25
```

```
Travel minutes (histogram, classes of 10 minutes)
 9 |         ██
 8 |         ██
 7 |     ██  ██  ██  ██
 6 |     ██  ██  ██  ██
 5 |     ██  ██  ██  ██
 4 |     ██  ██  ██  ██  ██
 3 |     ██  ██  ██  ██  ██
 2 | ██  ██  ██  ██  ██  ██
 1 | ██  ██  ██  ██  ██  ██
   +------------------------
     0-  10- 20- 30- 40- 50-
```
The histogram shows travel times spread quite evenly from 10 to 50 minutes, with few very short or very long trips.

**Every graph needs:** a title that says what and where/when, labelled axes **with units**, a sensible scale with equal
steps, and the data source.

### Activity (20 min)
1. On graph paper, draw a bar chart of `travel_mode` from your class table (or the frequency table in Unit 3).
2. Draw a dot plot of `travel_minutes`: number line from 0 to 60, one dot per student.
3. Write two sentences about the dot plot: where most values are, and anything unusual.
4. *CODAP version:* drag the class CSV into CODAP, make a graph, drag `travel_mode` to the x-axis (bar chart), then
   `travel_minutes` (dot plot). Try the "fuse dots into bars" option to get a histogram.

### Common mistakes
* Using a bar chart for a numerical variable with many values (one bar per student is not a summary).
* Bars of different widths, or a value axis that does not start at zero.
* No units on the axis ("time" — seconds? minutes? hours?).

**Check (5 min).**
1. Which graph suits 'favourite subject'?
2. What can a dot plot show that a table hides?
3. What must every graph have?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Line graphs and pie charts

**Hook (5 min).** You have (a) the temperature at noon each day for a week and (b) the share of students who walk,
bus and cycle. Which graph fits each? Predict before the lesson.

### Explanation
**Line graph** — for **change over time**. Time goes on the horizontal axis, in order and with equal spacing (if a
year is missing, leave a gap; do not squeeze the axis). Points are joined because the time between them is
continuous. Line graphs show **trends** (going up, going down) and **seasons** (repeating patterns).

**Worked example with real data.** Our World in Data (RD-02) reports the share of children in Nepal who die before
their fifth birthday:

| Year | 1960 | 1970 | 1980 | 1990 | 2000 | 2010 | 2020 |
|---|---|---|---|---|---|---|---|
| Child mortality (%) | 33.0 | 26.8 | 20.8 | 13.8 | 7.9 | 4.8 | 3.0 |

*Source: Our World in Data, child-mortality chart (UN IGME estimates), downloaded 2026-10-11.*

Plotted as a line graph (years on the x-axis, percent on the y-axis from 0 to 35), it shows one of the most important
stories in Nepal's history: in 1960 about **one child in three** died before age five; by 2020 about **one in 33**.
Asking *why* (vaccination, clean water, health posts, mothers' education) is how data lead to real questions.

**Pie chart** — for **parts of one whole**, when the parts add to 100%. Each slice's angle is its share of 360°:

> angle = (frequency ÷ total) × 360°

For the class table: walk 26/36 × 360° = 260°, bus 5/36 × 360° = 50°, bicycle 3/36 × 360° = 30°, motorbike
2/36 × 360° = 20°. Check: 260 + 50 + 30 + 20 = 360°.

Pie charts work only with a few categories (up to about 5) and when the "whole" makes sense. A bar chart is almost
always easier to read, because comparing angles is hard for the eye. Use a pie when the message is "this is most of
the whole".

### Activity (20 min)
1. Draw a line graph of the child-mortality table above. Use a y-axis from 0 to 35 with steps of 5.
2. Describe the trend in one sentence. In which decade did the percentage fall the most?
3. Convert the class travel-mode frequencies to angles and draw a pie chart with a protractor. Label each slice with
   its percent.
4. Discuss: would a bar chart or the pie chart show the travel data better? Why?

### Common mistakes
* A pie chart for values that are not parts of one whole (e.g. "minutes for each student").
* Joining points with lines when the x-axis is categories, not time (provinces in a line graph).
* Uneven time spacing (1960, 1990, 2000, 2020 equally spaced on the axis).

**Check (5 min).**
1. Which graph shows change over days?
2. Walk 12, bus 5, cycle 3 of 20: percent who walk?
3. Why would a pie chart of 'minutes by student' be wrong?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Misleading graphs

**Hook (5 min).** A newspaper bar chart shows Ward A's bar five times taller than Ward B's. The numbers are 52 and 50
households with taps. How is that possible?

### Explanation
A graph can be accurate and still give a false impression. The most common tricks:

| Trick | What happens | How to catch it |
|---|---|---|
| **Truncated axis** | The y-axis starts at 48, so 52 vs 50 looks like 4 vs 2 | Read where the axis starts |
| **Uneven scale** | Steps of 10, then 50, then 100 | Check the spacing of the numbers |
| **3D and pictures** | A coin drawn twice as tall is also twice as wide: it looks 4 times bigger | Compare numbers, not areas |
| **Cherry-picking** | Showing only the years where the line goes up | Ask what happened before and after |
| **Missing context** | "Cases doubled!" from 2 to 4 | Ask "out of how many?" |
| **Two y-axes** | Two lines on different scales seem to move together | Read both axes |
| **Claim beyond the data** | Title says "Our school is the best" from a chart of 3 schools | Compare the title with what is plotted |

**When is a non-zero axis fine?** For **line graphs** of things that never get near zero (body temperature,
exchange rate), starting at a sensible value shows the change better. For **bar charts**, always start at zero,
because bar length *is* the message.

**Worked example.** The heights of the bars in the hook:
* With the axis starting at 48: Ward A bar = 52 − 48 = 4 units, Ward B bar = 50 − 48 = 2 units → looks 2 times
  bigger. (If it started at 49.5, it would look 2.5 ÷ 0.5 = **5 times** bigger.)
* With the axis starting at 0: 52 vs 50 → Ward A is only 4% bigger.

### Activity (20 min)
1. Your teacher shows four "bad" graphs (from newspapers, social media or drawn on the board).
2. In groups, for each graph: name the trick, say what impression it gives, and what the honest message is.
3. Redraw one graph honestly on graph paper.
4. *Challenge:* draw a deliberately misleading graph of the class travel data, then swap with another group who must
   find your trick.

### Common mistakes
* Reading the shape of a graph before reading its axes.
* Thinking every non-zero axis is cheating (fine for line graphs of values far from zero, never for bars).
* Trusting a graph because it looks professional.

**Check (5 min).**
1. Axis starts at 48 instead of 0 — effect?
2. Name one more way to mislead with a graph.
3. What is the first thing you check on a graph?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* **Categorical → bar chart** (or pie for parts of a whole). **Numerical → dot plot** (small data) **or histogram**
  (many values). **Change over time → line graph.**
* Every graph needs a title, labelled axes with units, equal scale steps and a source.
* Bar charts start at zero; histogram bars touch; time axes are evenly spaced.
* Pie slice angle = share × 360°.
* Read the axes first: truncated axes, uneven scales, 3D, cherry-picking and missing context all mislead.

## Practice exercises
1. ★ Name the best graph: (a) number of students by favourite festival, (b) monthly rainfall in Pokhara over a year,
   (c) heights of 30 students, (d) share of Nepal's population in Mountain, Hill and Terai.
2. ★ Why do histogram bars touch but bar-chart bars do not?
3. ★ Favourite subjects: Maths 12, Social 11, Nepali 6, Science 5, English 2. Draw a bar chart in order from largest to
   smallest.
4. ★★ Work out the pie-chart angles for exercise 3. Check that they add to 360°.
5. ★★ Draw a dot plot of these sleep hours (round to the nearest half hour first): 8.2, 6.7, 7.1, 8.1, 8.6, 6.7, 8.7,
   6.6, 7.2, 8.9, 9.7, 7.9. Describe what you see.
6. ★★ Using the child-mortality table, by how many percentage points did child mortality fall from 1990 to 2010? By
   what fraction did it fall (from 13.8 to 4.8)?
7. ★★ A chart shows enrolment rising from 980 to 1,000 with the y-axis from 970 to 1,000. Describe the impression,
   then redraw it honestly.
8. ★★★ A poster shows two bags of rice, one drawn twice as tall as the other, to show that the price doubled. Why
   does this exaggerate the change?
9. ★★★ The synthetic district table gives population by ecological belt: Mountain 1,060,048, Hill 11,907,289, Terai
   14,366,042. Choose a graph and draw it. Explain your choice. (Remember: this table is synthetic.)
10. ★★★ Find a graph in a newspaper or on social media. Stick or sketch it in your notebook and write a three-line
    review: what it shows, one strength, one problem.

## Exercises with real data
**R1. Tourists over time (RD-10).** Use the Open Data Nepal tourist arrivals table (2001–2014). Draw a line graph of
total arrivals by year. Mark any year where arrivals fell, and write one question about why (look up events of that
year). Draw a second line for arrivals by air: is most tourism by air or by land?
*Offline fallback:* line graph of `mean_temp_c` for the 12 months of one year in `climate_monthly_synthetic.csv`.

**R2. South Asia's children (RD-02).** From the Our World in Data child-mortality chart, copy the values for Nepal,
India, Bangladesh and Sri Lanka for 1990 and 2020 (or use the table in Lesson 2 for Nepal). Draw a grouped bar chart
(two bars per country). Which country has always had the lowest rate? Which improved most between 1990 and 2020?

**R3. Earthquake magnitudes (RD-05).** Use the grouped frequency table you made in Unit 3, exercise R1, to draw a
histogram. Describe its shape: where is the tallest bar, and which side has a long "tail"?

## Unit project: Graph gallery
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Make four graphs of your class data (one
bar chart, one dot plot or histogram, one pie chart, one line graph of something measured over a week), each with a
title, axes, units and a one-sentence message, plus one deliberately misleading graph with a note explaining the
trick. Display them as a gallery walk. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Our World in Data, <https://ourworldindata.org/country/nepal>: dozens of line graphs about Nepal; pick one and
  explain it to your family.
* Darrell Huff, *How to Lie with Statistics* (1954): a short, funny, classic book on misleading graphs and numbers.
