# Grade 9 · Unit 8: Grade 9 project: which districts are changing?

> Track: A/B (project) · Tools: spreadsheet or SQL/pandas · Lessons: 2
> Datasets: `census-districts`, `kathmandu-air-quality`

**Big idea.** Put the PPDAC cycle together: ask, plan, wrangle, analyse and communicate a story from a district table.

**What you will be able to do**

* I can plan a data investigation on a plan card.
* I can clean, analyse and chart data with a spreadsheet, SQL or pandas, keeping a log.
* I can present a claim with evidence, reasoning and limits, and defend it in an oral check.

**Words to know:** PPDAC, plan card, cleaning log, claim, evidence, limitation, reproducible. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/project_template.ipynb` (the five PPDAC headings, ready to fill in).

### Before you start
This unit uses **everything** from Grade 9: tidy tables and pivots (Unit 1), cleaning and logs (Unit 2), SQL
(Unit 3), Python and pandas (Units 4–5), charts (Unit 6) and rates (Unit 7). Choose the tools you are most confident
with: a spreadsheet project is as good as a code project if the thinking is good.

---

## Lesson 1: Plan and clean

**Hook (5 min).** A good project fits in one sentence. Say yours to a partner in under 15 seconds. Can they repeat it
back?

### Explanation
**The plan card** is one page you fill in *before* touching the data. It saves hours of aimless charts.

| Plan card | Example (air quality) |
|---|---|
| **Question** (one statistical question) | How much worse is Kathmandu's air in winter than in the monsoon? |
| **Why it matters / who cares** | Parents and schools deciding outdoor activities |
| **Data** (source, licence, synthetic or real) | `air_daily_synthetic.csv`, CC0, synthetic; real ODN file later (RD-12) |
| **Variables** (with units) | `date`, `pm25` (µg/m³) |
| **Rate / summary** | median PM2.5 by season; share of days above 40 µg/m³ |
| **Method** (tool and steps) | pandas: clean → add month → group → box plot |
| **Chart planned** | box plot of PM2.5 by month |
| **Risks** | missing days (25), error codes (−999), one station ≠ whole city, synthetic numbers |
| **Roles** | data steward, analyst/driver, storyteller |

**Choosing a good question.** Good Grade 9 questions compare groups, describe change, or relate two variables, and
are answerable with the data you have:
* "Which belt has the most people abroad per 1,000 residents?" (districts)
* "Do districts with more secondary schools per 100,000 people have higher literacy?" (districts + schools)
* "How much worse is winter air than monsoon air?" (air)
* "Which province has the largest households?" (districts)
* With real data: "Which provinces grew fastest between the 2011 and 2021 censuses?" (RD-13)

Avoid questions the data cannot answer: "Why do people go abroad?" needs interviews, not a district table.

**Cleaning comes next**, with a log (Unit 2). For the example:

```python
import pandas as pd

air = pd.read_csv("air_daily_synthetic.csv", parse_dates=["date"])
print(air.shape, (air["pm25"] == -999).sum(), air["pm25"].isna().sum())   # (731, 3) 4 25
air["pm25"] = air["pm25"].mask(air["pm25"] == -999)                       # error code -> missing
air["month"] = air["date"].dt.month
print(air["pm25"].notna().sum(), "valid days")                            # 702
```

`parse_dates` makes `date` a real date, so `.dt.month` can pull out the month. `.mask(condition)` replaces values
where the condition is true with missing.

### Activity (20 min)
1. In your group, agree on a question and fill in the plan card. Show it to your teacher for a quick OK.
2. Load and inspect your data (five-step inspection, Unit 5).
3. Clean it, writing every step in the cleaning log.
4. Decide who does what for Lesson 2 (roles rotate: data steward, analyst/driver, storyteller).

### Common mistakes
* Skipping the plan and "seeing what the data say".
* A question too big ("Is Nepal developing?") or not about variation ("What is Terai-09's population?").
* Cleaning without logging.

**Check (5 min).**
1. What does a plan card contain?
2. Why log cleaning steps?
3. Name one risk in district tables.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Analyse and present

**Hook (5 min).** You have two minutes to convince the class. What is your claim, and which single chart proves it?

### Explanation
**Analysis** follows the plan: the summaries and rates you chose, then one or two charts. Worked example continued:

```python
by_month = air.groupby("month")["pm25"].median().round(1)
print(by_month)

winter = air.loc[air["month"].isin([12, 1, 2]), "pm25"]
monsoon = air.loc[air["month"].isin([6, 7, 8]), "pm25"]
print("winter median", winter.median(), "| monsoon median", monsoon.median())
print("share of days above 40:", round(100 * (air["pm25"] > 40).sum() / air["pm25"].notna().sum(), 1), "%")
```

Results (synthetic): monthly medians range from about 11 µg/m³ in June to about 94 in January; winter median 92.9,
monsoon median 12.9 µg/m³; PM2.5 was above 40 µg/m³ on 421 of 702 valid days (60%).

```python
import matplotlib.pyplot as plt

months = range(1, 13)
plt.boxplot([air.loc[air["month"] == m, "pm25"].dropna() for m in months])
plt.xticks(list(months), ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"])
plt.title("Daily PM2.5 by month, 2019–2020 (synthetic data)")
plt.ylabel("PM2.5 (µg/m³)")
plt.show()
```

**Conclusion** (CER + limit), as on the poster:

> **Claim:** Winter air is far more polluted than monsoon air — about seven times higher.
> **Evidence:** median PM2.5 92.9 µg/m³ in Dec–Feb vs 12.9 in Jun–Aug (702 valid days, 2019–2020); box plot by month.
> **Reasoning:** the whole winter box sits above the whole monsoon box, so the difference is consistent, not caused
> by a few days. Rain washes particles out of the air; in winter, cold still air traps smoke and dust (a known
> pattern — check it in a source).
> **Limits:** synthetic data shaped like Kathmandu, one "station", 29 days missing or invalid; real values must come
> from the real dataset (RD-12).

**The poster** (Grade 8 Unit 7 design rules): claim headline; one main chart; key numbers; question and method box;
"what we cannot say" box; source and "synthetic" label; names and roles; AI-use line.

**The two-minute talk:** claim (15 s) → evidence, pointing at the chart (60 s) → limit and next step (30 s) → one
question from the audience.

**The oral check** (2 minutes per student, with the teacher): "Show me where you cleaned the −999s. Why the median?
What would change your conclusion?" It checks that every group member understands the work, especially if anyone
used an AI assistant.

### Activity (20 min)
1. Run the planned analysis; make the chart; check numbers with a second method (e.g. pandas and a pivot table, or an
   `assert` that counts add up).
2. Build the poster.
3. Give the two-minute talk to another group; collect two stars and a wish; improve one thing.
4. Teacher oral checks during the gallery walk.

### Common mistakes
* Many charts and no claim.
* A claim stronger than the evidence ("the air is deadly") or causal without support.
* Forgetting the "synthetic" label, the source, or the limit box.

**Check (5 min).**
1. What are the three parts of a conclusion?
2. Why an oral check?
3. What goes in the limit box?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* PPDAC from start to finish: a one-sentence question, a plan card, logged cleaning, planned analysis, a CER
  conclusion with limits.
* One strong chart beats many weak ones.
* Check every number twice (two methods, or `assert`).
* Label synthetic data; credit sources and AI help; be ready to explain every step in an oral check.

## Practice exercises
1. ★ Write three statistical questions you could answer with the synthetic district table, and one you could not.
2. ★ Fill in a plan card for "Which province has the largest households?".
3. ★★ For the air example, compute the median PM2.5 for each **season**: winter (Dec–Feb), spring (Mar–May), monsoon
   (Jun–Aug), autumn (Sep–Nov). Which season comes second?
4. ★★ Rewrite this conclusion so it meets the CER + limit standard: "Air is bad in winter. Look at the chart."
5. ★★ Your project uses `literacy_pct` averaged across districts for each belt. What question will the oral check
   probably ask? Prepare an answer.
6. ★★★ The air data have 29 missing or invalid days. Find which months they fall in. Could they change the
   conclusion? Argue both ways.
7. ★★★ Plan a project that **joins** the districts and schools tables. Write the plan card and the SQL or pandas
   steps (no need to run them).
8. ★★★ The WHO 2021 guideline for 24-hour PM2.5 is 15 µg/m³. On what share of valid days is the synthetic PM2.5 above
   it? Why should you check the guideline value in the WHO document rather than trust this book or a website?

## Exercises with real data
**R1. Real air, real winter (RD-12 or RD-06).** Repeat the worked example with the real Kathmandu air-quality file from
Open Data Nepal (filter PM2.5 and one station). Do the winter and monsoon medians look like the synthetic ones?
*Offline fallback:* the synthetic file, as in the lesson.

**R2. Which districts are changing? (RD-13).** The real flagship: from the census portal, collect 2011 and 2021
population for the districts of your province. Compute growth rates (Unit 7), find the fastest-growing and any
shrinking districts, and present a poster with a map sketch or bar chart.

**R3. Your own question (RD-01 / RD-02 / RD-05 / RD-06 / RD-07).** Choose any dataset from
`docs/datasets/free-datasets.md` and complete a full PPDAC project with the same plan card.

## Unit project: Which districts are changing?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Groups of three produce: the plan card, the
cleaned data and cleaning log, at least three queries or pandas steps and one chart, a poster, a two-minute talk and
individual oral checks. This is Grade 9's flagship project. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* The UK Royal Statistical Society's "PPDAC" and Statistics New Zealand's "CensusAtSchool" resources: more project
  ideas built on the same cycle.
* Look at Nepali news data journalism (e.g. data stories in national newspapers) and identify their plan: question,
  data, method, claim.

---

### End of Grade 9: are you ready for Grade 10?
You are ready if you can:
- [ ] keep a table tidy and use formulas, sorting, filtering and pivot tables;
- [ ] clean missing values, error codes, inconsistent names, units and BS/AD dates, with a log;
- [ ] write SQL with `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING` and `JOIN`;
- [ ] write Python with lists, loops, `if`, and functions with tests;
- [ ] load, inspect, filter, sort, add columns and group in pandas;
- [ ] draw bar charts, histograms, box plots and scatter plots, and describe them;
- [ ] compute rates with the right denominator, weighted group rates and growth rates;
- [ ] complete a PPDAC project and defend it in an oral check.
