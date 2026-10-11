# Grade 10 · Unit 8: Project: Air in my city

> Track: B (project) · Tools: Python, pandas, matplotlib, optional Streamlit · Lessons: 2
> Datasets: `kathmandu-air-quality`

**Big idea.** Run the whole PPDAC cycle on a year of PM2.5: clean, analyse, conclude honestly and publish.

**What you will be able to do**

* I can plan a reproducible analysis with a cited health limit and a plan for missing data.
* I can produce a cleaned dataset, a data-quality report, summaries, exceedance counts and charts in one notebook.
* I can write a conclusion with claim, evidence, reasoning and limits, and publish it as a report or dashboard.

**Words to know:** reproducible, guideline value, standard, exceedance, data-quality report, robustness check. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/air_in_my_city.ipynb` (PPDAC template).

### Before you start
This project uses all of Grade 10: cleaning dates and codes (Unit 1), distributions and outliers (Unit 2), relationships
(Unit 3), time series (Unit 4), honest use of models and AI (Units 5–6) and dashboards (Unit 7). Work in groups of three
with rotating roles: data steward (cleaning and log), analyst (code and charts), storyteller (conclusion, poster or
dashboard text).

---

## Lesson 1: Plan and clean

**Hook (5 min).** A good question names the **place**, the **pollutant**, the **period** and the **comparison**. "Is
Kathmandu's air bad?" fails all four. Rewrite it so it passes.

### Explanation
**The question.** Examples that pass:
* "In which months of 2019–2020 was daily PM2.5 most often above the WHO guideline?"
* "How much higher was PM2.5 in winter (Dec–Feb) than in the monsoon (Jun–Aug)?"
* "Did 2020 have fewer polluted days than 2019?" (Think about what happened in spring 2020 — the COVID-19 lockdown —
  and whether synthetic data can show it.)

**The limit value — cite it.** Health limits change and websites copy old values. Use the primary documents:
* **WHO Global Air Quality Guidelines (2021):** 24-hour PM2.5 guideline 15 µg/m³; annual 5 µg/m³.
* **Nepal's National Ambient Air Quality Standards:** set a 24-hour PM2.5 standard (40 µg/m³ in the 2012 standards);
  check the current government notice before using it.
Write in your plan which value you use, from which document and year, and why. Using **both** (a strict health
guideline and the national legal standard) is often the most informative.

**Plan for missing data.** Decide *before* analysing: days with no valid reading are not "clean days". Count
exceedances as "days above the limit **out of days with data**", and report how many days are missing in each month.

**Reproducibility.** Anyone should be able to run your notebook from top to bottom on the same file and get the same
numbers. So: load the raw file (never edit it by hand), do every cleaning step in code, print a log, and keep all
choices (limit, seasons, window) as named variables at the top.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "air_daily_synthetic.csv"   # swap for the real file later
LIMIT_WHO = 15                          # µg/m³, WHO 2021 24-hour guideline
LIMIT_NEPAL = 40                        # µg/m³, Nepal NAAQS 24-hour PM2.5 (check current notice)

raw = pd.read_csv(DATA_FILE)
air = raw.copy()
air["date"] = pd.to_datetime(air["date"], format="%Y-%m-%d")
log = {
    "rows": len(air),
    "error_codes": int((air["pm25"] == -999).sum()),
    "blank": int(air["pm25"].isna().sum()),
}
air["pm25"] = air["pm25"].replace(-999, np.nan)
air["month"] = air["date"].dt.month
air["year"] = air["date"].dt.year
log["valid_days"] = int(air["pm25"].notna().sum())
print(log)    # {'rows': 731, 'error_codes': 4, 'blank': 25, 'valid_days': 702}
```

**The data-quality report** (half a page): rows, period, error codes, missing days by month, duplicates, impossible
values, outlier flags (within-month rule, Unit 2) and the decision for each.

### Activity (20 min) — PRIMM
1. Fill in the **Problem** and **Plan** sections of the notebook: question, limit values with citations, seasons,
   missing-data rule, chart plan, roles.
2. Run and extend the cleaning cell; print the log.
3. Write the data-quality report: count missing days by month and flag within-month outliers.

### Common mistakes
* Quoting a limit from memory or a blog.
* Counting missing days as clean days.
* Cleaning in a spreadsheet by hand, then analysing in code (not reproducible).

**Check (5 min).**
1. What must you cite for the limit?
2. Why plan for missing data?
3. What is a one-line question?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Analyse and publish

**Hook (5 min).** You have two minutes on the school assembly to tell the city something true about its air. What
will you say, and what number will you put on the slide?

### Explanation
**Summaries and exceedances by month:**

```python
monthly = air.groupby("month")["pm25"].agg(
    valid_days="count",
    median="median",
    above_nepal=lambda s: (s > LIMIT_NEPAL).sum(),
    above_who=lambda s: (s > LIMIT_WHO).sum(),
)
monthly["pct_above_nepal"] = (100 * monthly["above_nepal"] / monthly["valid_days"]).round(0)
print(monthly)
```

Synthetic result for the Nepal standard (40 µg/m³): **every** valid day was above it in January, February, March,
November and December; 87% in October, 76% in April, 29–31% in May and September, and almost none in June–August.

**The main chart:**

```python
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.bar(monthly.index, monthly["pct_above_nepal"], color="tab:red")
ax.set_xticks(range(1, 13), ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"])
ax.set_ylim(0, 100)
ax.set_ylabel("% of days above 40 µg/m³")
ax.set_title("Share of days above Nepal's PM2.5 standard, 2019–2020 (synthetic data)")
plt.show()
```

**Robustness checks** — does the conclusion survive reasonable changes?
* Use the WHO guideline instead of the Nepal standard.
* Use 2019 only and 2020 only.
* Use interpolated values for missing days.
If the main message stays the same, say so; if it changes, that is part of the story.

**The conclusion (CER + limits):**

> **Claim:** Polluted air is a winter problem: from November to March almost every day breaks Nepal's 24-hour PM2.5
> standard, while the monsoon months are almost always below it.
> **Evidence:** 100% of valid days above 40 µg/m³ in Nov–Mar; 0–2% in Jun–Aug (702 valid days, 2019–2020).
> **Reasoning:** the pattern repeats in both years and with the stricter WHO guideline (even more days exceed it), so
> it is not an accident of one year or one limit.
> **Limits:** synthetic data shaped like Kathmandu; one location; 29 missing or invalid days; daily means hide hourly
> peaks; exceedance depends on which official limit is used.
> **AI use:** (one line).

**Publishing.** Choose: a two-page report (notebook exported to PDF/HTML), a poster, or the Unit 7 dashboard adapted to
your question. Whatever the format: question, method, one main chart, key numbers, conclusion, limits, source and
licence, "synthetic" label if needed.

### Activity (20 min) — PRIMM
1. Run the monthly exceedance table and main chart; add a second chart (e.g. box plots by month or a 7-day rolling
   mean with the limit as a horizontal line, `ax.axhline(LIMIT_NEPAL)`).
2. Do at least two robustness checks.
3. Write the conclusion; peer-review with two stars and a wish; oral check with the teacher.
4. Publish in your chosen format.

### Common mistakes
* "The air is deadly" — dramatic claims without the health evidence to back them.
* Showing only the yearly mean (hides the seasonal story).
* Forgetting the robustness checks or the limits.

**Check (5 min).**
1. Three parts of a conclusion?
2. Name two limits in this study.
3. Why disclose AI use?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* A good question names place, pollutant, period and comparison.
* Cite limit values from primary documents (WHO 2021 guideline; Nepal's national standard) and say which you used.
* Missing days are not clean days: report exceedances out of valid days and missing days per month.
* Reproducible notebook: raw file untouched, all choices as variables at the top, printed cleaning log.
* Summaries and exceedances by month, one main chart, robustness checks, CER conclusion with limits, then publish.

## Practice exercises
1. ★ Rewrite as a good project question: "Is the air bad in winter?"
2. ★ A month has 31 days: 25 valid, 20 above the limit. What percent of valid days were above? Why not divide by 31?
3. ★ Why should the limit values be variables at the top of the notebook?
4. ★★ Compute, for the synthetic data, the percent of valid days above the WHO 15 µg/m³ guideline in each month. In
   which months is it below 100%?
5. ★★ Compare the number of days above 40 µg/m³ in 2019 and 2020. Is the difference meaningful?
6. ★★ Add a 7-day rolling mean line and a horizontal line at the Nepal standard to a daily plot. Which months does the
   smooth line stay above the standard?
7. ★★★ A classmate's notebook gives different exceedance counts from yours for the same file. List three possible
   reasons and how you would find which one it is.
8. ★★★ Your city council asks you to "prove that traffic causes the pollution". What can and can't your data show?
   What extra data would help?

## Exercises with real data
**R1. The real thing (RD-12).** Do the whole project on the real Kathmandu PM2.5 file (Open Data Nepal, CC BY-SA, via
OpenAQ). Check whether the spring 2020 lockdown shows up (compare March–May 2020 with the same months of other years).
*Offline fallback:* the synthetic file.

**R2. Another city (RD-06 / OpenAQ).** If PM2.5 data exist for another Nepali city (OpenAQ lists stations), repeat the
analysis there and compare. If not, compare **weather** (rain and temperature from Open-Meteo) between Kathmandu and
your town, and discuss how weather could explain pollution differences.

**R3. Health context (RD-18).** Find the WHO's estimate of deaths attributable to ambient air pollution in Nepal (Global
Health Observatory) and the WHO 2021 guideline document. Use them, correctly cited, in your report's introduction (class
use only: CC BY-NC-SA).

## Unit project: Air in my city
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Hand in: the reproducible notebook (with log and
data-quality report), the published report/poster/dashboard, the robustness checks, a one-paragraph CER conclusion with
limits, and the AI-use line; plus individual oral checks. This is Grade 10's flagship project. Full brief and rubric:
`project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* WHO Global Air Quality Guidelines (2021), summary for policy makers (free PDF).
* IQAir and OpenAQ maps for current air quality in Nepal (<https://openaq.org>).
* ICIMOD's work on air pollution in the Hindu Kush Himalaya.

---

### End of Grade 10: are you ready for Grade 11?
You are ready if you can:
- [ ] parse dates, handle error codes and missing values in pandas, and keep a log;
- [ ] describe distributions with the right summaries (mean/SD vs median/IQR) and handle outliers in context;
- [ ] fit and interpret a least-squares line, check residuals, and discuss causation honestly;
- [ ] separate trend, seasonality and noise; compute trends per decade and anomalies;
- [ ] build and fairly evaluate a simple classifier against a baseline on unseen data;
- [ ] explain how AI learns, why it hallucinates and is biased, and use it responsibly;
- [ ] build a small dashboard and review it with a checklist;
- [ ] run a reproducible PPDAC project with robustness checks.
