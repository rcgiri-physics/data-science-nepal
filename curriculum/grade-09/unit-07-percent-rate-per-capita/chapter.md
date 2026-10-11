# Grade 9 · Unit 7: Percent, rate and per-capita

> Track: A/B · Tools: calculator, spreadsheet or pandas · Lessons: 3
> Datasets: `census-districts`

**Big idea.** Fair comparison needs rates. Per-capita and per-1,000 measures remove the effect of size; percentage points and percent change are not the same.

**What you will be able to do**

* I can compute shares, rates, ratios and per-capita values, and choose the scale (per 100, 1,000, 100,000).
* I can choose and state the right denominator, and combine rates correctly (weighted, not averaged).
* I can compute percent change, percentage-point change and an annual growth rate.

**Words to know:** numerator (अंश), denominator (हर), share, rate (दर), ratio (अनुपात), per capita (प्रतिव्यक्ति), weighted average, percentage point, growth rate. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/rates.ipynb` (or use a spreadsheet; every calculation is shown both ways).

### Before you start
Grade 8 Unit 6 introduced counts vs rates and percentage points. This unit goes further: denominators, ratios,
weighted rates from groups, and growth over time — the arithmetic behind most news stories about Nepal's economy,
population and schools.

---

## Lesson 1: Share, percent and per 1,000

**Hook (5 min).** Which tells you more: "4,000 people from our district live abroad" or "4 in every 1,000 people from
our district live abroad"? What would you need to know to compare with another district?

### Explanation
Every rate is a fraction: **numerator ÷ denominator**.
* The **numerator** is what you count (people abroad, girls enrolled, road deaths).
* The **denominator** is the group the count comes from (all residents, all students, all people).

Then choose a **scale** so the number is easy to read:

| Scale | Multiply by | Good for | Example |
|---|---|---|---|
| share | 1 | proportions, between 0 and 1 | 0.068 |
| percent | 100 | common things | 6.8% |
| per 1,000 | 1,000 | births, deaths, migrants | 68 per 1,000 |
| per 100,000 | 100,000 | rare things: road deaths, diseases | 12 per 100,000 |

**Ratios** compare two groups instead of a part with a whole:
* **Sex ratio** = males per 100 females. Nepal's Census 2021 reported a sex ratio of about **95.6**: fewer males than
  females, partly because many men work abroad.
* **Pupil–teacher ratio** = students per teacher.
* **Dependency ratio** = (people aged 0–14 + 65+) per 100 people aged 15–64.

**Per capita** means per person: GDP per capita, electricity used per capita, rice produced per capita. It divides a
total by the population.

**Worked example (synthetic).** People abroad per 1,000 residents:

| District | Population | Absentee | Per 1,000 |
|---|---|---|---|
| Terai-09 | 1,607,726 | 111,228 | 69.2 |
| Terai-03 | 878,299 | 47,834 | 54.5 |
| Hill-25 | 421,197 | 47,947 | 113.8 |
| Hill-04 | 313,431 | 24,176 | 77.1 |
| Mountain-01 | 107,373 | 7,065 | 65.8 |
| Mountain-04 | 84,648 | 5,315 | 62.8 |
| Mountain-03 | 70,970 | 4,415 | 62.2 |
| Mountain-05 | 26,942 | 1,072 | 39.8 |

Hill-25 has about the same number of people abroad as Terai-03 (≈ 48,000) but more than twice the rate: about one
person in nine.

Spreadsheet: `=1000*K2/E2`. pandas:

```python
import pandas as pd
df = pd.read_csv("districts_synthetic.csv")
df["abroad_per_1000"] = 1000 * df["absentee_population"] / df["population"]
df["sex_ratio"] = 100 * df["male"] / df["female"]
df[["district", "abroad_per_1000", "sex_ratio"]].round(1).head()
```

### Activity (20 min)
1. For the 8 districts above, rank by count and by rate. Which district moves the most?
2. Compute the sex ratio for three districts. What would a sex ratio of 100 mean?
3. **Make:** choose one more rate from the table (e.g. households per km², people per secondary school) and say what
   the numerator and denominator are.

### Common mistakes
* Choosing a scale that gives awkward numbers (0.0000124 instead of 1.24 per 100,000).
* Mixing up a ratio (males per 100 females) with a share (males per 100 people).
* Forgetting to say the scale ("the rate is 69").

**Check (5 min).**
1. 12 of 200 as a percent?
2. 12 of 200 per 1,000?
3. Why per 1,000 for rare things?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Choosing a denominator

**Hook (5 min).** "Girls' enrolment is 50%." Fifty percent of what? All students? All girls of school age? All girls
in the district? Each gives a different number — and answers a different question.

### Explanation
**The denominator defines the question.** Three "girls" indicators that sound alike:

| Indicator | Numerator | Denominator | Question it answers |
|---|---|---|---|
| Girls' **share of enrolment** | girls enrolled | all students enrolled | Are classrooms balanced? |
| Girls' **enrolment rate** | girls enrolled | girls of school age | Are girls going to school? |
| Girls **per school** | girls enrolled | number of schools | How crowded are schools? |

A district could have a 50% girls' share (balanced classrooms) while only 60% of girls of school age are enrolled
(and maybe only 60% of boys, too). Our synthetic schools table lets us compute the first and third, but **not** the
second: it has no "children of school age" column. Knowing what you *cannot* compute is part of the skill.

**Combining rates: sum first, then divide (weighted).** Suppose:

| District | Population | Literacy |
|---|---|---|
| A | 1,000,000 | 80% |
| B | 50,000 | 50% |

* **Unweighted average** of the two rates: (80 + 50) ÷ 2 = **65%**.
* **Weighted** (true rate for all people): literate people = 800,000 + 25,000 = 825,000; total = 1,050,000 →
  825,000 ÷ 1,050,000 ≈ **78.6%**.

The unweighted average treats the small district as if it were as big as the large one. Unless you really want the
"average district", **sum the numerators and the denominators, then divide**:

```python
schools = pd.read_csv("schools_synthetic.csv")
m = df.merge(schools, on="district_id")
belt = m.groupby("ecological_belt")[["enrolment_girls", "enrolment_boys"]].sum()
belt["girls_share_pct"] = 100 * belt["enrolment_girls"] / (belt["enrolment_girls"] + belt["enrolment_boys"])
belt.round(1)
```

In a spreadsheet: `=SUMIF(belt,"Hill",girls) / (SUMIF(belt,"Hill",girls) + SUMIF(belt,"Hill",boys))`.

**Denominators can mislead too.**
* Road deaths **per vehicle** fall when vehicles increase fast, even if deaths per person rise.
* A hospital's death rate per **patient** is high if it treats the sickest patients.
* "Per capita" uses the population **living there** — census, projection, or the absent population included? Check.

### Activity (20 min)
1. For each indicator, write the numerator and the correct denominator: (a) pupil–teacher ratio; (b) share of
   households with electricity; (c) infant mortality rate (hint: per 1,000 live births); (d) GDP per capita.
2. Compute girls' share of enrolment for each belt the weighted way, and also as the mean of district shares. Are they
   different? Why only a little here?
3. Explain in two sentences why the synthetic table cannot give the girls' *enrolment rate*.

### Common mistakes
* Averaging percentages across groups of different sizes.
* A denominator that does not contain the numerator (girls enrolled ÷ total population).
* Not stating the denominator in the chart title or caption.

**Check (5 min).**
1. Girls' share of enrolment divides by…
2. Why can two 'girls' percentages differ?
3. Always state the denominator in…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Percent change and percentage points

**Hook (5 min).** Girls' share of enrolment grew from 48% to 50%. Headline A: "up 2%". Headline B: "up 4.2%". Is the
change big or small? Which headline is honest?

### Explanation
Two kinds of change:
* **Absolute change** = new − old. For percentages it is measured in **percentage points**: 50% − 48% = **2
  percentage points**.
* **Relative (percent) change** = (new − old) ÷ old × 100 = 2 ÷ 48 × 100 ≈ **4.2%**.

Headline A is confusing ("2%" of what?); Headline B is technically right but sounds bigger. The honest version gives
both values: **"Girls' share rose from 48% to 50% (2 percentage points)."**

**Growth over several years.** Nepal's population was 26,494,504 in the 2011 census and 29,164,578 in 2021.
* Total change: 29,164,578 − 26,494,504 = 2,670,074 people.
* Percent change: 2,670,074 ÷ 26,494,504 ≈ **10.1%** over the decade.
* Is that 1.01% per year? Not quite: growth **compounds** (each year's growth builds on the previous year's total).
  The **average annual growth rate** is

  > (new ÷ old)^(1 ÷ years) − 1 = (1.1008)^(1/10) − 1 ≈ **0.96% per year**.

  NSO reports **0.92%**, because the two censuses were about 10.4 years apart (June 2011 to November 2021) and NSO
  uses a slightly different (exponential) formula. Small details like the exact dates matter when you check
  official numbers.

```python
old, new, years = 26_494_504, 29_164_578, 10
growth = (new / old) ** (1 / years) - 1
print(f"{100 * (new - old) / old:.1f}% over the decade, {100 * growth:.2f}% per year")
```

**Index numbers** compare many years with one base year set to 100: index = value ÷ base value × 100. Prices are
usually shown this way: the consumer price index (CPI) published by Nepal Rastra Bank. An index of 125 means prices are
25% higher than in the base year.

**Traps:**
* A 50% fall followed by a 50% rise ends 25% lower (100 → 50 → 75).
* Percent changes on small bases look huge: 2 → 6 cases is "+200%".
* Comparing "percent change" of two different-sized starting points: a district growing from 10,000 to 12,000 (+20%)
  added fewer people than one growing from 1,000,000 to 1,050,000 (+5%).

### Activity (20 min)
1. For each pair compute percentage points and percent change, and write a fair headline: 48% → 50%; 80% → 84%;
   60% → 45%; 5% → 10%; 92% → 96%.
2. A district grew from 400,000 to 460,000 people in 10 years. Compute the decade percent change and the average
   annual growth rate.
3. Rice cost Rs 80/kg in a base year (index 100). Two years later it is Rs 92. What is the index? What percent rise?

### Common mistakes
* "Percent" when you mean "percentage points".
* Dividing a decade's percent change by 10 for an annual rate (close for small rates, wrong for large ones).
* Starting from the new value instead of the old one.

**Check (5 min).**
1. 48% → 50%: points?
2. Relative change?
3. Fair headline wording?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Rate = numerator ÷ denominator × scale (100, 1,000, 100,000). Ratios compare two groups (sex ratio = males per 100
  females). Per capita = per person.
* The denominator defines the question; say it in every title and caption; know what you cannot compute.
* Combine groups by **summing numerators and denominators**, not averaging rates.
* Percentage points (absolute) vs percent change (relative); give old and new values.
* Annual growth = (new ÷ old)^(1/years) − 1; index = value ÷ base × 100.

## Practice exercises
1. ★ 35 of 1,400 students failed. Give it as a share, a percent and per 1,000.
2. ★ A school has 840 students and 28 teachers. Pupil–teacher ratio?
3. ★ A village has 1,180 males and 1,250 females. Sex ratio?
4. ★★ Three classes have pass rates 90% (of 20), 70% (of 40), 50% (of 10). What is the school's overall pass rate?
   Compare with the simple average of the three rates.
5. ★★ For each, name the numerator and denominator: (a) literacy rate; (b) remittances as % of GDP;
   (c) hospital beds per 10,000 people; (d) students per computer.
6. ★★ Literacy rose from 65.9% (2011) to 76.2% (2021) in Nepal (census, population aged 5+). Give the change in
   percentage points and as percent change. Write an honest one-sentence headline.
7. ★★ A district's population went from 250,000 to 300,000 in 10 years. Find the percent change and the average
   annual growth rate.
8. ★★★ "Road deaths per 10,000 vehicles fell by half in ten years, so roads are safer." Explain why this might be
   false.
9. ★★★ Using the synthetic table, compute the sex ratio by belt (sum males ÷ sum females × 100). Which belt has the
   lowest? Suggest a reason that would apply to real data.
10. ★★★ Prices rose 10% one year and 10% the next. Did they rise 20% in total? Compute exactly.

## Exercises with real data
**R1. Remittances (RD-01).** From the World Bank, download "Personal remittances, received (% of GDP)"
(`BX.TRF.PWKR.DT.GD.ZS`) for Nepal and three neighbours. Which country depends most on remittances? For Nepal, find
the change in percentage points between 2000 and the latest year. Why is "% of GDP" a better comparison than the
amount in US dollars?

**R2. Census growth by province (RD-13).** From the census results portal, get 2011 and 2021 population for the 7
provinces. Compute decade percent change and average annual growth rate for each. Which province grew fastest? Which
might have lost people? Rank by growth rate, not by count.
*Offline fallback:* invent a 2011 column for 5 synthetic districts by multiplying by 0.9, then compute growth.

**R3. Prices and an index (RD-08).** Choose one vegetable in the Kalimati data. Take its mean price in 2014 as index
100 and compute an index for each year to 2020. Which year was most expensive? Compare with a second vegetable.

## Unit project: Rate detective
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Find a news story about Nepal that uses a
number (population, migration, prices, enrolment, health). Find the source data, recompute the number with the right
numerator, denominator and scale, check percent vs percentage points, and write a "rate detective" report: what the
article got right, what it got wrong or left out, and a corrected headline. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Our World in Data, "Per capita" and "growth rate" explainers; many charts let you switch between total and per
  capita — try it.
* Nepal Rastra Bank's "Current Macroeconomic and Financial Situation" reports (<https://www.nrb.org.np>): practise
  reading percent changes in real tables.
