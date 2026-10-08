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
