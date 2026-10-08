# Grade 11 · Unit 8: Reproducibility, Git and the climate project

> Track: B (project) · Tools: Python, Git, notebooks · Lessons: 3
> Datasets: `climate-monthly`

**Big idea.** Others (and your future self) should be able to rerun your work and get the same answer: seeds, environments, version control and clear notes.

**What you will be able to do**

* I can use Git add/commit/status.
* I can fix random seeds and record versions.
* I can package an analysis so another student can rerun it.

**Words to know:** reproducible, seed, version control, commit, environment (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/climate_project.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Git basics

**Hook (5 min).** You changed your notebook and now it breaks. How do you go back?

**Concept (≤ 5 min).** Version control records snapshots: git add, git commit -m 'what changed', git status, git log. Commit often with clear messages.

**Activity (20 min).** Make a repo for the climate project; commit three times; view the log.

**Check (5 min).**
1. What does git commit record?
2. Why write clear messages?
3. Which command shows changes waiting?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Seeds, environments, notes

**Hook (5 min).** I ran it on Monday and got a different answer on Tuesday. Why?

**Concept (≤ 5 min).** Randomness (bootstrap) needs a fixed seed; library versions can change results; record both. A README says how to run the work.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Add seed and environment print to the notebook; write a 5-line README.

**Check (5 min).**
1. Why set a seed?
2. What else affects reproducibility?
3. Does a seed make a result correct?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Project: analyse and publish

**Hook (5 min).** Can a classmate rerun your work from your folder alone?

**Concept (≤ 5 min).** Finish the analysis, state the trend with an interval and limits, push/share the folder, and have a peer rerun it.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Complete the notebook; peer rerun; fix what broke.

**Check (5 min).**
1. What proves it is reproducible?
2. What goes in the limits?
3. What do you disclose?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Climate or weather?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
