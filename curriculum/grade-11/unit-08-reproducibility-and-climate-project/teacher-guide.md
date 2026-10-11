# Teacher guide — Grade 11, Unit 8: Reproducibility, Git and the climate project

**Time:** 3 lessons + project (about 5 periods). **Track:** B (project).

| # | Lesson | Time |
|---|---|---|
| 1 | Git basics | 40–45 min |
| 2 | Seeds, environments, notes | 40–45 min |
| 3 | Project: analyse and publish | 40–45 min |
| P | Unit project: Climate or weather? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/climate_project.ipynb`; Git installed (https://git-scm.com).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Practise 'commit messages' on paper by describing each change in one line.

## Common misconceptions
* Saving as final_v2_REAL_final.ipynb is version control.
* Setting a seed makes a result true; it only makes it repeatable.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Git basics**
1. What does git commit record?  
   *Answer:* A snapshot with a message.
2. Why write clear messages?  
   *Answer:* So you know what and why later.
3. Which command shows changes waiting?  
   *Answer:* git status.

**Lesson 2: Seeds, environments, notes**
1. Why set a seed?  
   *Answer:* So random results can be repeated.
2. What else affects reproducibility?  
   *Answer:* Library/Python versions and data versions.
3. Does a seed make a result correct?  
   *Answer:* No: only repeatable.

**Lesson 3: Project: analyse and publish**
1. What proves it is reproducible?  
   *Answer:* Someone else reruns it and gets the same results.
2. What goes in the limits?  
   *Answer:* Synthetic data, one series, short period, weather vs climate.
3. What do you disclose?  
   *Answer:* AI help used, data licence and source.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. Edit the file → `git status` → `git add` → `git commit`.
2. "Fix typo in rainfall chart title"; "Add 95% bootstrap interval for temperature trend"; "Remove raw CSV from repo
   and add data/raw/ to .gitignore" (also note it remains in history; ask the teacher how to purge if sensitive).
3. Creates a random-number generator with seed 42, so the same "random" numbers come out each run.
4. ```
   data/raw/
   .ipynb_checkpoints/
   secrets.txt
   ```
5. No seed; cells run out of order; data file changed (downloaded again); different library versions; hidden state
   from deleted cells still in memory.
6. Put the file in the project (`data/climate.csv`) and use `pd.read_csv("data/climate.csv")` (or `Path(__file__)`-
   based paths in scripts).
7. Seeds 1–5 (1,000 resamples each): 0.18–0.39, 0.19–0.39, 0.18–0.39, 0.17–0.39, 0.18–0.38 °C/decade — the
   conclusion (positive trend, interval excludes 0) is robust.
8. It proves the notebook works from a clean start, with no hidden variables from cells you deleted or ran out of order.
9. Missing code/data, undocumented manual steps, different software versions, errors, selective reporting. Trust: if
   others cannot check a result, policy based on it rests on faith.
10. Check for: question, data source/licence/date, how to run, seed/versions, key results, limits, AI use, licence.

## Real-data exercises: notes
* **R1** `hashlib.sha256(open(path, "rb").read()).hexdigest()`; teach the difference between "same code" and "same data".
* **R2** OWID and WDI revise estimates each year; small differences are normal — record the download date.
* **R3** Supervise any public contribution; follow CONTRIBUTING.md and the code of conduct.
