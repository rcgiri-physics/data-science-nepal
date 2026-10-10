# Grade 10 · Unit 7: Dashboards with Streamlit

> Track: B (code) · Tools: Python, Streamlit · Lessons: 3
> Datasets: `kathmandu-air-quality`

**Big idea.** A dashboard lets others explore your analysis. Good dashboards answer one question clearly and say where the data came from.

**What you will be able to do**

* I can design a dashboard on paper around one question and test it with a user.
* I can build a small Streamlit app with a title, a key number, a chart and a selector.
* I can review and improve a dashboard with a checklist before sharing it.

**Words to know:** dashboard, user, prototype, widget, metric, filter, cache, deploy. Full list: `curriculum/framework/glossary.md`.

**App:** `app/air_dashboard.py` (starter app). Install once with `pip install -r requirements-streamlit.txt`, then run
`streamlit run app/air_dashboard.py` from this unit's folder. The app opens in your web browser.

### Before you start
Units 1–4: cleaning, grouping and plotting the air series; Grade 8 Unit 7: designing for the 10-second reader.
Streamlit needs a computer with Python (it does not run inside JupyterLite). No computer? Lesson 1 is entirely on
paper, and Lessons 2–3 can be done as a demonstration by the teacher.

---

## Lesson 1: Design on paper

**Hook (5 min).** A visitor opens your dashboard and has 10 seconds. What must they understand before they leave?

### Explanation
A **dashboard** is a page that shows a few key numbers and charts, often with controls (**widgets**) the user can
change: choose a year, a city, a smoothing window. Dashboards are everywhere: Nepal's COVID-19 dashboards, school
results portals, air-quality apps showing the AQI near you, election-night results pages.

**Design before code.** Most bad dashboards are bad because nobody decided what they were for. Answer four questions
on paper first:
1. **Who** is the user? (a parent, a school principal, a city official)
2. **What one question** does it answer? ("How polluted was the air this month, and is it getting better?")
3. **What decision** might it support? ("Should outdoor sports be moved indoors this week?")
4. **What must be visible in 10 seconds?** Usually one big number and one chart.

**A good layout**

```
┌───────────────────────────────────────────────┐
│ Title = the question                           │
│ one-line caption: data, place, period         │
├──────────────┬──────────────┬─────────────────┤
│ KEY NUMBER   │ KEY NUMBER   │ (optional)      │
│ mean PM2.5   │ days > limit │ missing days    │
├──────────────┴──────────────┴─────────────────┤
│              MAIN CHART                       │
│   daily values + smoothed line                │
├───────────────────────────────────────────────┤
│ Source · licence · date · limits · contact    │
└───────────────────────────────────────────────┘
Sidebar: year ▼   smoothing window ═══●══
```

**Paper prototyping.** Draw the dashboard on A4, with widgets as boxes. Then test it: show it to a classmate playing
the user, ask them to answer the question, and watch where they get confused. Fixing a pencil sketch takes a minute;
fixing code takes an hour.

### Activity (20 min)
1. Choose a user and a question for the air data (or rainfall, or districts).
2. Sketch the dashboard on A4: title, 1–3 key numbers, one main chart, at most two widgets, a source/limits box.
3. Test with a classmate for 2 minutes: can they answer the question? Note one confusion and fix it.

### Common mistakes
* Starting with "what charts can I make?" instead of "what question does the user have?".
* Ten charts on one page.
* No source, date or units.

**Check (5 min).**
1. What is the first design decision?
2. Why add a source note?
3. How many main messages?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Build with Streamlit

**Hook (5 min).** Your notebook makes great charts, but a principal will never open a notebook. How do you turn your
analysis into a page anyone can use with a click?

### Explanation
**Streamlit** is a Python library that turns a script into a web app. You write ordinary Python; each `st.` command adds
something to the page. Run it with `streamlit run file.py`.

The starter app, explained piece by piece:

```python
# app/air_dashboard.py (shortened) — a Streamlit app, not run by the book's code checker
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Air in my city", layout="centered")
st.title("Air in my city: daily PM2.5")
st.caption("SYNTHETIC practice data - invented numbers. Source and limits are at the bottom.")

@st.cache_data
def load():
    df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    df["pm25"] = df["pm25"].replace(-999, np.nan)   # -999 is a sensor error code
    return df

air = load()
year = st.sidebar.selectbox("Year", sorted(air["date"].dt.year.unique()))
window = st.sidebar.slider("Smoothing window (days)", 1, 30, 7)

view = air[air["date"].dt.year == year].set_index("date")
view = view.assign(smooth=view["pm25"].rolling(window, min_periods=1).mean())

left, right = st.columns(2)
left.metric("Mean PM2.5 (ug/m3)", f"{view['pm25'].mean():.1f}")
right.metric("Missing days", int(view["pm25"].isna().sum()))
st.line_chart(view[["pm25", "smooth"]])
st.markdown("**Source:** synthetic table … **Limits:** one station; missing days; invented numbers.")
```

How it works:
* **The whole script reruns from top to bottom every time the user changes a widget.** That is why it is so simple:
  `year` simply holds whatever the user chose this time.
* `st.sidebar.selectbox` and `st.sidebar.slider` are **widgets**; they return the current value.
* `@st.cache_data` remembers the result of `load()`, so the CSV is read once, not on every rerun.
* `st.metric` shows a big number; `st.columns(2)` places items side by side; `st.line_chart` draws an interactive
  chart; `st.pyplot(fig)` shows a matplotlib figure instead.

**Adding a feature: a month filter and a limit line.** Inside the app:

```python
# add to the app — not run by the book's code checker
months = st.sidebar.multiselect("Months", list(range(1, 13)), default=list(range(1, 13)))
view = view[view.index.month.isin(months)]

limit = st.sidebar.number_input("Daily limit (ug/m3)", value=15)
st.metric("Days above limit", int((view["pm25"] > limit).sum()))
st.caption(f"Limit = {limit} ug/m3. Check the current WHO guideline and Nepal standard before using a value.")
```

When something breaks, Streamlit shows the Python error on the page; read the last line first, as always.

### Activity (20 min) — PRIMM
1. **Predict** what changes when you move the slider; run the starter app and try it.
2. **Modify:** change the title to your question; add a third metric (maximum PM2.5).
3. Add the month filter and the "days above limit" metric.
4. **Make:** add a bar chart of monthly mean PM2.5 for the chosen year (`st.bar_chart(view["pm25"].resample("MS").mean())`).

### Common mistakes
* Running `python air_dashboard.py` instead of `streamlit run air_dashboard.py`.
* Reading the data inside the main script without caching (slow on every click).
* Forgetting that widget values change on each rerun (do not "remember" them in normal variables).

**Check (5 min).**
1. How do you run an app?
2. What does st.sidebar.selectbox do?
3. What does the script do when you click?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Publish and review

**Hook (5 min).** Your dashboard works on your computer. Is it ready for strangers — a parent on a phone, with slow
internet, who has never heard of PM2.5?

### Explanation
Before sharing, review with the **dashboard checklist**:

| ✔ | Check |
|---|---|
| ☐ | The title is the question; the main message is visible in 10 seconds |
| ☐ | Every number has a unit; every chart has labelled axes |
| ☐ | Source, licence, date of data, and "synthetic" (if it is) are stated |
| ☐ | Limits are stated (one station, missing days, model data…) |
| ☐ | No personal or sensitive data; nothing that identifies individuals |
| ☐ | Health or safety thresholds are cited from the current official document |
| ☐ | It works on a phone screen (narrow layout) and loads quickly |
| ☐ | Colours are readable by colour-blind users; text is large enough |
| ☐ | A user test was done and at least one problem fixed |

**Sharing options.** On the school network, run the app on one computer and others open its address. Free hosting
services (for example Streamlit Community Cloud, which deploys an app from a public GitHub repository) let anyone with
the link use it. **Licences still apply** when you publish: credit the data source, respect share-alike terms (the real
Kathmandu air data on Open Data Nepal is CC BY-SA), and never publish restricted data (such as DHS microdata,
decision D6).

**Dashboards can mislead too.** Interactivity does not make a chart honest. A default smoothing window of 30 days hides
dangerous days; a y-axis that rescales with each selection can exaggerate small changes; a default year that happens to
look good is cherry-picking. Choose defaults that tell the truth.

### Activity (20 min)
1. Swap laptops (or screenshots) with a partner and review their dashboard with the checklist.
2. Give two stars and a wish; fix at least three issues in your own app.
3. Test on a phone (or narrow the browser window).
4. Write a 3-line "about this dashboard" note: question, data and licence, limits.

### Common mistakes
* Publishing synthetic data without saying so.
* Copying a health threshold from a random website.
* Forgetting the phone users (most people in Nepal access the internet by phone).

**Check (5 min).**
1. Name two things to check before sharing.
2. Does hosting change the data's licence rules?
3. Why test on a phone?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Design first: user, one question, decision, what is visible in 10 seconds; paper prototype and user test.
* Streamlit: a script → web app; widgets return values; the script reruns on every change; cache data loading.
* `st.title`, `st.caption`, `st.sidebar.selectbox/slider/multiselect`, `st.metric`, `st.columns`, `st.line_chart`,
  `st.bar_chart`, `st.pyplot`.
* Review with the checklist (units, source, licence, limits, privacy, phone, colours) before sharing.
* Licences apply when publishing; defaults should tell the truth.

## Practice exercises
1. ★ List the four design questions and answer them for a dashboard about your school's attendance.
2. ★ What is the difference between `st.metric` and `st.line_chart`?
3. ★ Why does Streamlit rerun the whole script when a widget changes? What is one advantage?
4. ★★ Sketch a dashboard for "Which districts have the most people abroad per 1,000?" using the synthetic district
   table. Which widget would you add?
5. ★★ Write the Streamlit lines for a selectbox of ecological belts and a metric showing the number of districts in the
   chosen belt (assume `df` is the district table).
6. ★★ The app shows "Mean PM2.5: 52.8" with no unit and no year. Rewrite the metric label.
7. ★★ Give two ways a dashboard's default settings could mislead.
8. ★★★ Add a download button so users can save the filtered data:
   `st.download_button("Download CSV", view.to_csv().encode("utf-8"), "pm25.csv")`. When should you **not** offer a
   download?
9. ★★★ Design (on paper) a dashboard for a district health office using the synthetic health table. What must it
   *not* show, and why?
10. ★★★ Compare a static poster with an interactive dashboard: two advantages of each.

## Exercises with real data
**R1. Real air dashboard (RD-12).** Replace `DATA_FILE` with your cleaned real Kathmandu PM2.5 file (from Unit 1, R1).
Update the caption, source line (CC BY-SA, Open Data Nepal, OpenAQ) and limits. Do the checklist.
*Offline fallback:* the synthetic starter app.

**R2. Weather explorer (RD-06).** Build an app where the user chooses a town (from 4–5 towns you downloaded from
Open-Meteo, saved as CSV) and sees monthly rain and temperature. Credit Open-Meteo (CC BY 4.0).

**R3. Country comparer (RD-01 / RD-02).** Build an app with a multiselect of South Asian countries and a line chart of
one World Bank or OWID indicator over time. Add the source and the indicator definition.

## Unit project: Mini dashboard
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Hand in: the paper prototype with user-test
notes, the Streamlit app (one question, 1–3 metrics, one main chart, ≤ 2 widgets, source and limits), the completed
checklist and a 3-line "about" note. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Streamlit documentation and gallery (<https://docs.streamlit.io>, <https://streamlit.io/gallery>).
* Stephen Few, *Information Dashboard Design* (2nd ed., 2013) — the classic book on dashboard design.
