# Teacher guide — Grade 10, Unit 7: Dashboards with Streamlit

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code).

| # | Lesson | Time |
|---|---|---|
| 1 | Design on paper | 40–45 min |
| 2 | Build with Streamlit | 40–45 min |
| 3 | Publish and review | 40–45 min |
| P | Unit project: Mini dashboard | 2 periods |

## Before you start
* Materials: `app/air_dashboard.py` and `requirements-streamlit.txt` in this unit's folder. Install: `pip install streamlit` (internet needed once). Run: `streamlit run app/air_dashboard.py`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Sketch a dashboard on paper: title, one chart, one selector, source note. Peer-test with 'tell me what you see'.

## Common misconceptions
* More charts = better dashboard. One clear message beats ten charts.
* Dashboards can't be wrong because they're interactive.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Design on paper**
1. What is the first design decision?  
   *Answer:* The question the dashboard answers.
2. Why add a source note?  
   *Answer:* So viewers can judge trust.
3. How many main messages?  
   *Answer:* One.

**Lesson 2: Build with Streamlit**
1. How do you run an app?  
   *Answer:* streamlit run file.py
2. What does st.sidebar.selectbox do?  
   *Answer:* Adds a dropdown to the sidebar.
3. What does the script do when you click?  
   *Answer:* Reruns from top with the new value.

**Lesson 3: Publish and review**
1. Name two things to check before sharing.  
   *Answer:* Source and limits; no personal data; licence.
2. Does hosting change the data's licence rules?  
   *Answer:* No: attribute and respect share-alike.
3. Why test on a phone?  
   *Answer:* Many users have only phones.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science Grade 10: Python programming, databases and AI & contemporary technology; compulsory Maths data handling/statistics.

## Answers: practice exercises
1. User: principal; question: "Which classes had the lowest attendance this month?"; decision: whom to follow up;
   10-second view: school attendance % this month and a bar chart by class.
2. `st.metric` shows one big number (with optional change); `st.line_chart` draws a chart from a table/series.
3. So the code can be written top-to-bottom like a normal script; each run uses the widgets' current values — no
   complicated event handling.
4. Title = question; metric: belt or national rate; main chart: horizontal bars of the top 10 districts by rate; widget:
   belt or province selector; note: synthetic data.
5. `belt = st.selectbox("Ecological belt", sorted(df["ecological_belt"].unique()))` and
   `st.metric("Districts in belt", int((df["ecological_belt"] == belt).sum()))`.
6. `st.metric("Mean PM2.5, 2020 (µg/m³)", "52.8")` (plus "synthetic" in the caption).
7. A long default smoothing window that hides peaks; auto-scaled y-axes that exaggerate small changes; a flattering
   default period or place.
8. Do not offer downloads of personal/sensitive data or data whose licence forbids redistribution (e.g. DHS); credit and
   licence must travel with any download.
9. Show only aggregated counts/rates by belt or district with a small-group rule; never individual records, ages with
   locations, or anything identifying.
10. Poster: works offline, one clear message, easy to print; dashboard: users explore their own question, updates with
    new data. (Poster: fixed; dashboard: needs a device and internet.)

## Real-data exercises: notes
* **R1** Check that share-alike is acknowledged and that the app does not re-host the full raw dataset publicly unless
  the maintainers agree (D7/D8).
* **R2–R3** Encourage saving downloaded CSVs locally and loading them with `@st.cache_data`; don't call APIs on every
  rerun (Open-Meteo free tier limits).
