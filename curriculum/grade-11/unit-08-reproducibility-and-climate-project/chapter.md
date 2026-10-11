# Grade 11 · Unit 8: Reproducibility and a climate project

> Track: B (project) · Tools: Python, Git, notebooks · Lessons: 3
> Datasets: `climate-monthly`

**Big idea.** Others (and your future self) should be able to rerun your work and get the same answer: seeds, environments, version control and clear notes.

**What you will be able to do**

* I can use Git to record, inspect and undo changes to a project.
* I can make an analysis repeatable: fixed seeds, recorded versions, relative paths, a README.
* I can complete and publish a climate analysis that a classmate can rerun from my folder alone.

**Words to know:** reproducible, version control, repository (repo), commit, commit message, diff, seed, environment, dependency, README, relative path. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/climate_project.ipynb` (PPDAC template for the project).

### Before you start
Units 3 and 6 of this grade (bootstrap intervals, seasonal trends) are the analysis tools. You need Git installed (free:
<https://git-scm.com>) or a school computer with Git; in JupyterLite you can still do Lessons 2–3 and use Git on a
school PC for Lesson 1.

---

## Lesson 1: Git basics

**Hook (5 min).** You changed your notebook yesterday and now it breaks. Your folder contains `project.ipynb`,
`project_final.ipynb`, `project_final_v2.ipynb` and `project_REAL_final.ipynb`. Which one worked? What changed?

### Explanation
**Version control** records snapshots of a project, with who changed what, when and why, and lets you go back. **Git**
is the most widely used version-control system; the whole of this curriculum lives in a Git repository.

**The basic cycle**

```bash
git init                         # once: make this folder a repository
git status                       # what has changed since the last snapshot?
git add analysis.ipynb README.md # choose the changes to include (the "staging area")
git commit -m "Add seasonal indices and de-seasonalised plot"
git log --oneline                # list of snapshots, newest first
git diff                         # line-by-line changes not yet committed
```

* A **commit** is a snapshot plus a **message**. Good messages say *what* and *why* in the imperative: "Fix −999
  handling in rain column", not "changes" or "asdf".
* Commit **often**: each small working step.
* `git restore file` throws away uncommitted changes to a file; `git checkout <commit> -- file` brings back an old
  version; `git revert <commit>` undoes a commit by adding a new one.
* **What to commit:** code, notebooks, README, small data you are allowed to share. **What not to commit:** large raw
  data, passwords, personal data, data whose licence forbids redistribution. List them in a `.gitignore` file.

**Sharing.** Services such as GitHub, GitLab or Codeberg host repositories online (`git push` sends commits, `git pull`
fetches others'). Many employers and universities look at a student's public repositories — your projects become a
portfolio (see "After Grade 12").

### Activity (20 min)
1. Create a folder `climate-project`, run `git init`, add the notebook and a one-line README, commit.
2. Make a change (add a plot), check `git status` and `git diff`, commit with a good message.
3. Break something on purpose (delete a cell), then restore it with Git.
4. Look at `git log --oneline`: could someone understand your project's history from the messages?

### Common mistakes
* Committing huge data files or secrets.
* One giant commit at the end ("final").
* Messages that say nothing.

**Check (5 min).**
1. What does git commit record?
2. Why write clear messages?
3. Which command shows changes waiting?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Seeds, environments, notes

**Hook (5 min).** You ran the bootstrap on Monday: CI 0.18–0.39. On Tuesday: 0.17–0.40. Your partner, on another
computer: 0.19–0.38. Who is right?

### Explanation
**Reproducible** means: same data + same code → same results, for anyone. Four common reasons it fails:

1. **Randomness without a seed.** Bootstrap, permutation tests, train/test splits and simulations use random numbers.
   A **seed** fixes the sequence so reruns match:

```python
import numpy as np

rng = np.random.default_rng(2026)      # write the seed once, at the top
print(rng.integers(0, 100, 3))          # the same three numbers every run
```

   A seed makes a result **repeatable**, not **correct**: a result that only appears with one lucky seed is not a
   result. Check that conclusions hold for a few different seeds.

2. **Different software versions.** Functions change behaviour between library versions. Record them:

```python
import sys
import numpy
import pandas
import matplotlib

print("Python", sys.version.split()[0])
print("numpy", numpy.__version__, "| pandas", pandas.__version__, "| matplotlib", matplotlib.__version__)
```

   Projects list their **dependencies** in a file such as `requirements.txt` (e.g. `pandas>=2.0`), so others can
   install the same environment (`pip install -r requirements.txt`). This repository does exactly that.

3. **Paths that only work on your computer.** `C:/Users/Sita/Desktop/data.csv` fails everywhere else. Use **relative
   paths** (`data/climate.csv`, relative to the project folder).

4. **Manual steps.** "Then I deleted some rows in Excel" cannot be repeated. Do every step in code, top to bottom, and
   **restart and run all** before sharing to prove the notebook works from a clean start.

**The README** is the front door of a project. Five to ten lines:

```text
# Is it getting warmer? (Grade 11 climate project)
Question: trend in annual mean temperature, 1991–2020, synthetic table.
Data: datasets/climate-monthly/clean/climate_monthly_synthetic.csv (CC0, synthetic).
How to run: pip install -r requirements.txt; open analysis.ipynb; Restart & Run All (≈ 30 s).
Seed: 2026. Tested with Python 3.12, numpy 2.x, pandas 2.x.
Results: trend +0.28 °C/decade (95% bootstrap CI 0.18 to 0.39).
Limits: synthetic data; one series; no homogenisation; no attribution of cause.
AI use: used a chatbot to explain the block bootstrap; all code mine.
Author, date, licence (CC BY 4.0 for text, MIT for code).
```

### Activity (20 min) — PRIMM
1. **Predict** whether two runs without a seed give the same bootstrap interval; test it; then add a seed.
2. Change the seed to three other values. Does the conclusion (interval excludes 0) hold every time?
3. Add the environment-printing cell and a `requirements.txt` to your project.
4. Write the README.

### Common mistakes
* Seeding only once in one cell, then re-running cells out of order.
* "Works on my computer" paths.
* Treating a seed as proof.

**Check (5 min).**
1. Why set a seed?
2. What else affects reproducibility?
3. Does a seed make a result correct?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Project: analyse and publish

**Hook (5 min).** Swap folders with a classmate. Can they run your whole analysis and get your numbers in five minutes,
without asking you a single question?

### Explanation
**The climate project** brings together Units 3, 6 and 8:

| PPDAC | What to include |
|---|---|
| **Problem** | "Is [place] warming? How fast? How sure are we?" (and the same for rain) |
| **Plan** | methods (seasonal indices, de-seasonalised trend, year-block bootstrap, sensitivity table), seed, versions |
| **Data** | source, licence, date downloaded, cleaning log (synthetic table, or real NASA POWER/Open-Meteo data) |
| **Analysis** | seasonal profile; adjusted series with trend; bootstrap histogram and CI; sensitivity table; rain trend |
| **Conclusion** | claim with interval, weather vs climate, limits (one series, model data, homogenisation, cause) |

**Peer rerun protocol**
1. The reviewer receives only the folder (or repo link).
2. They follow the README exactly: install, open, Restart & Run All.
3. They compare their key numbers with the README's.
4. They note every point where they got stuck.
5. The author fixes the problems and commits ("Fix path to data file reported in peer rerun").

**Publishing.** Push the repository to an online host (if allowed by your school), or export the notebook as HTML/PDF
together with the folder. The real Open-Meteo data is CC BY 4.0 (credit Open-Meteo), NASA POWER asks for a citation;
include them. Do not upload data whose licence forbids it.

### Activity (20 min) — PRIMM
1. Complete the notebook following the PPDAC table.
2. Run the peer rerun protocol with a partner; record problems.
3. Fix, commit and write the final conclusion with limits and the AI-use line.

### Common mistakes
* The notebook only works if cells are run in a special order.
* README results don't match the notebook (updated one, not the other).
* Forgetting licences and credits when publishing.

**Check (5 min).**
1. What proves it is reproducible?
2. What goes in the limits?
3. What do you disclose?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Git: `init`, `status`, `add`, `commit -m`, `log`, `diff`, `restore`; commit small steps with clear messages; never
  commit secrets, personal data or restricted data.
* Reproducibility: seeds (repeatable ≠ correct; try several), recorded versions and `requirements.txt`, relative paths,
  everything in code, Restart & Run All.
* A README states question, data and licence, how to run, seed and versions, results, limits, AI use.
* A peer rerun is the real test of reproducibility.

## Practice exercises
1. ★ Put in order: `git commit`, `git add`, edit the file, `git status`.
2. ★ Write good commit messages for: fixing a typo in a chart title; adding a bootstrap interval; removing a large
   CSV that should not have been committed.
3. ★ What does `rng = np.random.default_rng(42)` do?
4. ★★ Write a `.gitignore` for a project with a `data/raw/` folder of downloaded files, `.ipynb_checkpoints/`
   folders and a `secrets.txt` file.
5. ★★ A notebook gives different results when run twice. List four possible reasons.
6. ★★ Rewrite `pd.read_csv("C:/Users/Ram/Downloads/climate.csv")` so it works for anyone who has the project folder.
7. ★★ Run the year-block bootstrap with seeds 1, 2, 3, 4, 5. Report the five intervals. Is the conclusion robust?
8. ★★★ Why is "restart and run all" a better test than "it ran fine when I wrote it"?
9. ★★★ A study cannot be reproduced by other researchers. Give three possible reasons, and explain why reproducibility
   matters for trust in science and in government statistics.
10. ★★★ Write the README for your Grade 10 "Air in my city" project as if publishing it today.

## Exercises with real data
**R1. Real climate, reproducibly (RD-07 / RD-06).** Write a notebook that **downloads** the data itself (NASA POWER or
Open-Meteo URL in a variable at the top), saves the raw file with the download date in its name, and runs the whole
analysis. Note in the README that rerunning later may give slightly different data (publishers revise), and record the
file's checksum (`hashlib.sha256`) like `tools/fetch_data.py` does.
*Offline fallback:* the synthetic table with a fixed seed.

**R2. Reproduce a published number (RD-01 / RD-02).** Pick one number from an OWID or World Bank chart about Nepal (e.g.
the 2020 child mortality rate). Reproduce it from the downloaded data in a notebook. Did you get exactly the same? If not,
why (revisions, rounding, definitions)?

**R3. Contribute (RD-20).** With your teacher, find a small improvement to this curriculum's repository (a typo, a
broken link, a clearer sentence) and propose it following `CONTRIBUTING.md`.

## Unit project: Climate or weather?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Hand in a Git repository (or folder) with the
notebook, README, requirements, `.gitignore` and a commit history of at least 6 meaningful commits; results that a
classmate reproduced in a documented peer rerun; and a conclusion with an interval and limits. This is Grade 11's
flagship project. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* "The Turing Way" (<https://the-turing-way.netlify.app>): free handbook on reproducible data science.
* Software Carpentry lessons "Version control with Git" (<https://swcarpentry.github.io/git-novice/>), free.
* *Pro Git* by Scott Chacon and Ben Straub (free online at <https://git-scm.com/book>).

---

### End of Grade 11: are you ready for Grade 12?
You are ready if you can:
- [ ] measure and improve performance with types, vectorising and indexes;
- [ ] write SQL window functions and CTEs, and check joins;
- [ ] build and interpret bootstrap confidence intervals;
- [ ] run and honestly interpret permutation tests;
- [ ] fit and interpret multiple regression, with residual checks and coefficient intervals;
- [ ] decompose a seasonal series and give a trend with uncertainty;
- [ ] compute distances and design honest maps with correct licences;
- [ ] keep a project reproducible with Git, seeds, environments and a README.
