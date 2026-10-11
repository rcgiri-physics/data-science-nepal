# Grade 12 · Unit 7: Communicating with data

> Track: A/B · Tools: charts, writing, optional Streamlit · Lessons: 3
> Datasets: `census-districts`

**Big idea.** Analysis only matters if people understand and can act on it: action titles, honest charts, short memos and clear limits.

**What you will be able to do**

* I can design a chart with an action title, honest scales, highlighting and a complete caption.
* I can write a one-page memo with the bottom line first, evidence, uncertainty and a recommendation.
* I can present findings and uncertainty in plain language, and publish work with credits and licences.

**Words to know:** audience, action title, caption, highlight, decluttering, bottom line up front (BLUF), memo, uncertainty, plain language, licence, attribution. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/data_story.ipynb` (runs offline on the synthetic table).

### Before you start
This unit gathers communication skills you have practised since Grade 8 (Unit 7 posters, claim–evidence–reasoning) and
raises them to a professional level. Setup:

```python
import pandas as pd
import matplotlib.pyplot as plt

districts = pd.read_csv("districts_synthetic.csv")       # SYNTHETIC
by_province = districts.groupby("province")[["absentee_population", "population"]].sum()
by_province["abroad_per_1000"] = 1000 * by_province["absentee_population"] / by_province["population"]
national = 1000 * districts["absentee_population"].sum() / districts["population"].sum()    # 80.7
```

---

## Lesson 1: Action titles and honest charts

**Hook (5 min).** Two slides show the same chart. One is titled "Figure 3: Absentee population by province". The other
says "Province 6 loses the most people abroad: 94 in every 1,000". Which one will a busy official remember?

### Explanation
**Start from the audience and the message.** Before drawing, write one sentence: *what should the reader know or do
after seeing this?* That sentence becomes the **action title**.

| Topic title (weak) | Action title (strong) |
|---|---|
| Absentee population by province | Province 6 has the highest share of people living abroad: 94 per 1,000 |
| Literacy by belt | Mountain districts trail Hill districts by 11 points in literacy |
| PM2.5, 2019–2020 | Kathmandu's air breaks the national standard almost every winter day |

**Design an honest, clear chart (a checklist):**
1. **Right chart for the message** (Grade 9 Unit 6): bars to compare categories, lines for time, scatter for
   relationships.
2. **Sort** bars by value (unless there is a natural order).
3. **Honest scales:** bars start at zero; consistent axes when comparing charts; no 3D.
4. **Highlight** what matters (one colour), grey the rest; label values directly instead of a legend where possible.
5. **Declutter:** remove borders, heavy gridlines, unnecessary decimals.
6. **Caption:** what is shown, units, source and date, "synthetic" if so, and one limit.

```python
s = by_province["abroad_per_1000"].sort_values()
colors = ["tab:red" if p == s.idxmax() else "lightgrey" for p in s.index]

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.barh([f"Province {p}" for p in s.index], s.values, color=colors)
ax.axvline(national, color="black", linestyle="--", linewidth=1)
ax.text(national + 1, -0.6, f"national {national:.0f}", fontsize=9)
for i, v in enumerate(s.values):
    ax.text(v + 1, i, f"{v:.0f}", va="center", fontsize=9)
ax.set_xlabel("People living abroad per 1,000 residents")
ax.set_title("Province 6 has the highest share of people abroad (synthetic data)", loc="left")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.text(0.01, -0.04, "Source: districts_synthetic.csv (invented numbers, CC0). Rates weighted by population.", fontsize=8)
plt.tight_layout()
plt.show()
```

The highlighted bar, the national reference line and direct labels let a reader get the message in seconds: province 6
(94 per 1,000) is highest, province 2 (56) lowest, national 81.

### Activity (20 min) — PRIMM
1. Rewrite five topic titles from earlier units as action titles.
2. **Predict** what the highlighted chart will look like; run it.
3. **Modify:** highlight the lowest province instead and change the title to match.
4. **Make:** redraw a cluttered chart from an earlier project using the checklist; show before and after.

### Common mistakes
* Titles that describe the axes instead of the message.
* Rainbow colours on every bar.
* Missing source, units or "synthetic".

**Check (5 min).**
1. What is an action title?
2. What goes in the caption?
3. Why a zero baseline for bars?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: The one-page memo

**Hook (5 min).** A ward chairperson has three minutes between meetings. You have ten pages of analysis. What do you give
them?

### Explanation
Decision-makers read the first lines and maybe the chart. Put the **bottom line up front** (BLUF).

**Memo structure (≈ 250–400 words, one page):**
1. **Title** = the key finding.
2. **Bottom line** (2–3 sentences): what we found and what we recommend.
3. **Evidence:** 3–4 bullet points with numbers, units and comparisons; one chart.
4. **How sure are we:** sample, uncertainty (intervals), limits.
5. **Recommendation(s):** specific, feasible, with who should act.
6. **Details:** data source, method in one line, contact; full analysis in an appendix.

**Example memo (synthetic data):**

> **Province 6 should be first for migrant-family support services**
>
> **Bottom line:** In our (synthetic) district table, 94 of every 1,000 residents of Province 6 live abroad, the highest
> rate of the seven provinces and above the national 81. We recommend piloting family-support desks for migrant
> households there first.
>
> **Evidence:**
> * Province 6: 94 per 1,000; Province 4: 90; Province 2: 56 (lowest).
> * Within Province 6 the rate varies widely: Hill-02 (107) and Hill-06 (101) exceed 100 per 1,000, while
>   Mountain-16 is at 53.
> * Rates are weighted by population, so large and small districts count fairly.
>
> **How sure are we:** These are invented numbers for practice; real decisions need the 2021 census absent-population
> tables. Absentee counts rely on household reports and may miss whole households that left.
>
> **Recommendation:** Validate with census data; if the pattern holds, start in Province 6 and Province 4.
>
> *Data: districts_synthetic.csv (CC0). Method: absentee ÷ population by province. Contact: …*

**Plain language.** Short sentences, everyday words ("people living abroad" not "absentee population"), numbers rounded
sensibly (94, not 94.0721), one idea per paragraph. Read it aloud: if you run out of breath, the sentence is too long.

**Test with a reader.** Give the memo to someone outside the project for 60 seconds, then ask them to tell you the main
point. If they can't, rewrite the first lines.

### Activity (20 min)
1. Draft a 250-word memo for a finding from your Grade 11 or 12 work, using the structure.
2. Swap with a partner; they summarise it back in one sentence after 60 seconds.
3. Revise the bottom line until their summary matches what you meant.

### Common mistakes
* Starting with the method ("We downloaded… we cleaned…").
* Hiding uncertainty or limits in the appendix.
* Recommendations nobody can act on ("more research is needed" alone).

**Check (5 min).**
1. What goes first?
2. Why say what you don't know?
3. Who is your audience?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Presenting and publishing

**Hook (5 min).** "The trend is 0.28 °C per decade (95% CI 0.18–0.39)." How would you say that to a farmers' group, a
newspaper and a scientist?

### Explanation
**Presenting uncertainty in plain words**

| Technical | Plain language |
|---|---|
| 95% CI 0.18–0.39 °C/decade | "warming by about a quarter of a degree every ten years — very likely between a fifth and two-fifths" |
| p = 0.03 | "a difference this big would be unusual if it were just chance" |
| R² = 0.09 | "these factors explain only a small part of why babies' weights differ" |
| recall 0.74 | "the list finds about three in four of the women who need a visit" |

Use **natural frequencies** ("3 in 4", "94 in every 1,000") rather than percentages of percentages, and ranges rather than
false precision. Show uncertainty visually: error bars, shaded bands, or a few plausible lines.

**A short talk (3 minutes):** one sentence of context → the main finding (action title) → one chart, pointing at the key
part → how sure we are → recommendation → invite questions. Practise with a timer.

**Publishing your work responsibly**
* **Credit and licences:** data sources with licences (CC BY requires attribution; BY-SA requires share-alike; some data
  cannot be republished at all, e.g. DHS); your own text and code under an open licence if you choose (this curriculum
  uses CC BY 4.0 for content and MIT for code).
* **Privacy:** no personal data; aggregate; small-group rule (Grade 8 Unit 8).
* **Reproducibility:** link the notebook or repository (Grade 11 Unit 8).
* **Formats:** a PDF report, a poster, a web page, a Streamlit dashboard (Grade 10 Unit 7). Students who want to build
  full websites can explore web frameworks such as Django or Flask, but they are **not required**: a clear memo and chart
  are what decision-makers use.
* **The student gallery:** with consent, publish an anonymised write-up in `community/student-gallery/` of this
  repository.

### Activity (20 min)
1. Translate four technical statements from your earlier projects into plain language for two audiences.
2. Give a 3-minute talk with one chart and one limit; collect two stars and a wish.
3. Write the credits and licence section for your capstone (Unit 8) publication.

### Common mistakes
* Reading slides aloud; too many charts.
* Dropping uncertainty to sound confident.
* Publishing without licences, credits or privacy checks.

**Check (5 min).**
1. How to show uncertainty plainly?
2. What do you publish with data work?
3. Is Django required?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Message first: action titles; right chart; sorted, highlighted, decluttered, honest scales; captions with units,
  source, date, limits.
* Memos: bottom line up front, evidence with numbers, how sure we are, specific recommendations, details last; plain
  language; test with a reader.
* Uncertainty in plain words: natural frequencies, ranges, visuals.
* Short talks: context → finding → chart → certainty → recommendation → questions.
* Publish with credits, licences, privacy checks and links to reproducible work.

## Practice exercises
1. ★ Rewrite as an action title: "Monthly PM2.5, 2019–2020".
2. ★ What three things should every caption contain?
3. ★ Turn "OR = 1.41 per visit" into plain language.
4. ★★ Draw the province chart sorted from highest to lowest with a vertical bar chart instead. Which is easier to read?
   Why?
5. ★★ A memo starts: "This report presents the methodology and results of an analysis of district-level data…" Rewrite
   the first two sentences in BLUF style.
6. ★★ Make a chart with error bars showing the bootstrap 95% interval of the facility-delivery rate for each belt (Grade
   11 Unit 3). Give it an action title.
7. ★★ Write the credits for a map that uses OSM roads, HDX boundaries and census 2021 data.
8. ★★★ Critique a chart from a Nepali newspaper or government report using the six-point checklist and redraw it.
9. ★★★ Your finding is uncertain (interval includes 0). Write a memo bottom line that is honest but still useful.
10. ★★★ Write two versions of the same finding: for a ward chairperson and for a newspaper headline plus first
    paragraph. Discuss what changed.

## Exercises with real data
**R1. A real migration memo (RD-13).** Using the Census 2021 absent population by province (or district), redo the
lesson chart and memo with real numbers. Compare with the synthetic story — did the conclusion change?
*Offline fallback:* the synthetic table, as in the lessons.

**R2. A climate chart for farmers (RD-07 / RD-06).** Make one chart and a 150-word note for farmers in your district about
temperature or rainfall change, with uncertainty in plain words.

**R3. Fix a published chart (RD-02 / RD-01).** Find a chart about Nepal in the news. Recreate it from OWID or World Bank
data, improve it with the checklist, and write a two-line explanation of the changes.

## Unit project: Story and memo
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Hand in one finished chart (before and after
versions), a one-page BLUF memo for a named decision-maker, a 3-minute talk with feedback notes, and a publication
section with credits, licences and privacy check. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Cole Nussbaumer Knaflic, *Storytelling with Data* (2015).
* Alberto Cairo, *How Charts Lie* (2019).
* Edward Tufte, *The Visual Display of Quantitative Information* (2nd ed., 2001).
* The Economist and Our World in Data chart style guides (search online) — models of action titles and clean charts.
