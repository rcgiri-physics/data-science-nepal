# Grade 12 · Unit 8: Capstone with a client

> Track: B/A (project) · Tools: any (Python, spreadsheet, Streamlit); Git · Lessons: 3
> Datasets: `health-synthetic`, `census-districts`, `kathmandu-air-quality`, `climate-monthly`

**Big idea.** Real data science serves someone: a client with a question, a data agreement, responsible handling, and a public write-up.

**What you will be able to do**

* I can scope a real question with a client and write a data agreement.
* I can deliver an analysis or model compared with the client's current practice, audited across groups, documented in
  a model card.
* I can hand over usable work and publish an anonymised write-up with consent.

**Words to know:** client, stakeholder, scope, deliverable, data agreement, consent, anonymisation, current practice, model card, handover, maintenance. Full list: `curriculum/framework/glossary.md`.

**Kit:** `../capstone-kit/` — client brief, data-agreement template, model-card template, rubric.
**Notebook:** `notebooks/capstone_template.ipynb`.

### Before you start
Everything from Grades 8–12 comes together here. The capstone runs over several weeks (the three lessons below are the
milestones; most work happens in between). Groups of three with rotating roles: **client lead** (communication, brief,
handover), **data steward** (agreement, cleaning, privacy, documentation) and **analyst** (analysis, model, audit).

---

## Lesson 1: Scope and agree

**Hook (5 min).** A health post in-charge says: "Help us decide who to visit first." What questions do you ask back
before touching any data? Write at least five.

### Explanation
**Finding a client.** Good capstone clients are local and have a decision to make: a ward office (which tole needs a
tap stand first?), a health post (visit priorities), your school (attendance patterns, library use), a cooperative
(which crops sell best at which season?), an NGO, a community forest user group, a local FM station. Your teacher
approves every client and project.

**The scoping conversation** (use `client-brief.md`):

| Ask | Why |
|---|---|
| What **decision** will this help? Who makes it? | no decision → no project |
| What do you do **now**? How well does it work? | the "current practice" is your real baseline |
| What does **success** look like? How will we know? | agree measures before analysing |
| What **data** exist? Who owns them? Can we use them? | ownership, consent, licence |
| Who is **affected**, and who might be missed or harmed? | fairness from the start |
| What will you **receive** (deliverables), by when? | avoid disappointment |
| Who will **maintain** it after we leave? | work that nobody can update dies |

**Scope it small.** "Improve health in our ward" is a mission, not a project. "Rank households for the next round of
antenatal home visits using last year's anonymised visit records" is a project. A finished small project beats an
unfinished big one.

**The data agreement** (use `data-agreement-template.md`) — signed by the client, your teacher, and you:
* **Purpose:** exactly what the data are for (and not for).
* **Data:** which fields, which period; **only what is needed** (data minimisation, Grade 8).
* **Consent:** how the people in the data agreed (or why aggregated/anonymised data need no individual consent);
  guardian consent where students appear.
* **Storage and access:** where data are kept (school computer, password, no personal phones or cloud drives unless
  agreed), who can see them.
* **Sharing and publishing:** what may be shown publicly (usually only aggregated, anonymised results), with whose
  approval.
* **Deletion:** when and how raw data are deleted after the project.
* **Licence of outputs:** who owns the analysis; open licence for the write-up if agreed.

If the client cannot share personal data safely, use **aggregated** data, **synthetic** data shaped like theirs (as this
curriculum does), or public data — and say so. A signed school agreement is not legal advice; for sensitive data, ask the
school leadership about Nepal's privacy law (Individual Privacy Act, 2075) and local rules.

### Activity (20 min)
1. Role-play: one group plays the client (the teacher provides a client card, e.g. the health post), another the team.
   Run the scoping conversation; the team fills in the client brief.
2. Draft the data agreement for the scenario. Swap with another team: can they find a privacy gap?
3. Write the project's one-sentence statement: decision, data, deliverable, deadline.

### Common mistakes
* Starting with "we want to use machine learning" instead of the client's decision.
* Accepting personal data "informally" (screenshots, WhatsApp).
* Promising more than can be delivered in the time.

**Check (5 min).**
1. What does a data agreement cover?
2. Why define success first?
3. May you share a client's data publicly?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Build and audit

**Hook (5 min).** Your model has 62% precision in the top 120. Is that good? Compared with what the health post does
today?

### Explanation
**Compare with current practice**, not just a statistical baseline. If health workers currently visit women with fewer
than four antenatal visits, evaluate that rule exactly as you evaluate your model, on the same test data:

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split

h = pd.read_csv("health_synthetic.csv")                          # stand-in for the client's anonymised records
h["home"] = 1 - h["institutional_delivery"]
train, test = train_test_split(h, test_size=0.3, random_state=7, stratify=h["home"])
cols = ["antenatal_visits", "wealth_quintile"]

current = (test["antenatal_visits"] < 4).astype(int)              # the health post's current rule
model = LogisticRegression().fit(train[cols], train["home"])
p = model.predict_proba(test[cols])[:, 1]
k = int(current.sum())                                            # same number of visits as the current rule
model_pick = np.zeros(len(test), dtype=int)
model_pick[np.argsort(-p)[:k]] = 1

for name, pick in [("current rule", current), ("model, same capacity", model_pick)]:
    print(f"{name:22s} visits {pick.sum():3d}  precision {precision_score(test['home'], pick):.3f}"
          f"  recall {recall_score(test['home'], pick):.3f}")
```

Result (synthetic): the current rule flags 301 women with precision 0.618 and recall 0.741; the model, given the same
301 visits, scores 0.611 and 0.733 — **no better**. Comparing at the **same capacity** (same number of visits) is fair. If the model is no better than the simple rule the
health workers already understand, recommend the rule — that is a successful, honest capstone result.

**Audit across groups** (Unit 5): sizes, base rates, selection rates, recall and precision by belt, wealth, age group or
whatever groups the client cares about; with intervals for small groups.

**The model card** (use `model-card-template.md`) documents the model for anyone who uses it:
* **Purpose** and intended use (and uses that are **out of scope**);
* **Data:** source, period, size, who is missing, preprocessing;
* **Model:** type, features, threshold or ranking rule;
* **Performance:** vs baseline and current practice, overall and by group, with uncertainty;
* **Limits and risks:** what could go wrong, for whom;
* **Maintenance:** when to re-audit, who owns it, how to report problems.

### Activity (20 min) — PRIMM
1. **Predict** whether the model beats the current rule at the same capacity; run the comparison.
2. Run the group audit by belt and wealth (reuse Unit 5's `audit` function).
3. Fill in the model card.
4. Decide, as a team, what you will recommend: the model, the current rule, a combination (e.g. the rule plus the
   model's next 20 highest-risk women), or something else.

### Common mistakes
* Comparing a model at one capacity with a rule at another.
* Skipping the audit "because the client didn't ask".
* A model card that lists only good news.

**Check (5 min).**
1. What goes in a model card?
2. What is the client's 'current way'?
3. Why audit before handover?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Hand over and publish

**Hook (5 min).** Six months after you leave school, the health post's computer is replaced. Will your work still be
used? What would make that possible?

### Explanation
**The client presentation** (10 minutes + questions), in plain language (Unit 7): the decision and question; what you
found (one or two charts); how it compares with what they do now; how sure you are; your recommendation; what they
receive and how to use it; limits and when to stop trusting it.

**The handover package**
* the **deliverable** in a form the client can use (a printed ranked list template and the rule, a spreadsheet with
  formulas, a simple dashboard, a one-page guide) — usually **simpler than your notebook**;
* a **README** for whoever maintains it: how to update with new data, step by step, with screenshots if needed;
* the **model card** and **audit memo**;
* the notebook/repository for technical readers;
* confirmation that raw personal data have been **deleted** as agreed.

**Public write-up (with consent).** A 2–3 page anonymised summary: question, approach, findings, what the client did with
it, lessons learned. Before publishing check:
* no names, phone numbers, exact addresses or small groups (< 5) that identify people;
* the client and teacher approved the text;
* all data sources credited; licences respected;
* AI use disclosed.
With approval, add it to `community/student-gallery/` in this repository so future students learn from it.

**Reflection.** Every capstone ends with an honest reflection: what worked, what didn't, what you would do differently,
and what you learned about data, people and yourself. Employers and universities value this as much as the technical
result.

### Activity (20 min) — PRIMM
1. Rehearse the client presentation; a classmate plays the client and asks hard questions ("What if it's wrong?").
2. Assemble the handover package with the checklist.
3. Write the public summary and run the privacy checklist on it.
4. Write a one-page personal reflection.

### Common mistakes
* Handing over only a notebook that the client cannot run.
* Publishing before the client approves.
* No plan for who updates the work.

**Check (5 min).**
1. What must be anonymised before publishing?
2. What goes in the README?
3. Whose consent is required?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Start with the client's decision, current practice, success measures, data ownership and affected people; scope small.
* A signed data agreement covers purpose, minimum data, consent, storage, sharing, deletion and output licence.
* Evaluate against current practice at the same capacity; audit groups; document in a model card; recommend the simplest
  thing that works.
* Hand over something usable with a maintenance README; publish an anonymised, approved write-up; reflect honestly.

## Practice exercises
1. ★ Turn "help our school improve results" into a scoped capstone question with a decision, data and deliverable.
2. ★ List five sections of a data agreement.
3. ★ Why compare a model and a rule at the same capacity?
4. ★★ Run the Lesson 2 comparison with `random_state` 1, 2, 3. Does the conclusion change? What do you tell the client?
5. ★★ Write the "out of scope uses" part of a model card for the visit-ranking model (at least three).
6. ★★ A client sends a WhatsApp photo of a register with names and phone numbers "to save time". What do you do?
7. ★★ Design the handover deliverable for a health post with one shared computer and patchy electricity.
8. ★★★ Your model clearly beats the current rule overall but is worse for Mountain-belt women. Draft the recommendation.
9. ★★★ A client wants you to publish a map of households that did not pay a community fee. Respond, using the data
   agreement and ethics from Grade 8 Unit 8.
10. ★★★ Write the maintenance plan: when to re-audit, which signals mean "stop using it", who decides.

## Exercises with real data
**R1. A public-data capstone (any RD).** If no client can share data, choose a public-interest question for a real
organisation (e.g. your municipality, a local school, a youth club) using open data: air quality (RD-12), weather and
climate (RD-06/07), census (RD-13), OpenStreetMap facilities (RD-16), market prices (RD-08). Run the full capstone with
the organisation as "client" for scoping and feedback.

**R2. Learn from others (RD-20).** Read two write-ups in `community/student-gallery/` (or published data-for-good
projects in Nepal, e.g. Kathmandu Living Labs, Open Knowledge Nepal, Code for Nepal). For each: client, decision, data,
deliverable, what you would improve.

**R3. Practise on synthetic data.** Use the synthetic health table as a stand-in for a health post's records and complete
every capstone document (brief, agreement, model card, audit memo, handover README, public summary).

## Unit project: Community capstone
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Hand in: client brief, signed data agreement,
repository/folder with notebook and README, comparison with current practice, group audit, model card, handover package,
5-minute client presentation, anonymised public summary (with consent) and personal reflection. This is Grade 12's
flagship project, marked with `capstone-kit/rubric.md`. Full brief: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Margaret Mitchell et al., "Model Cards for Model Reporting" (2019) — the paper behind model cards.
* DataKind and Data for Good projects: examples of pro bono data science with clients.
* Continue with the "After Grade 12" part of this book: how to keep learning and where this can lead.

---

### End of Grade 12: what you can now do
- [ ] run a full machine-learning workflow with honest validation and testing;
- [ ] choose and explain regression and classification models;
- [ ] evaluate with confusion matrices, precision and recall, and choose thresholds with stakeholders;
- [ ] control overfitting with validation and simplicity;
- [ ] audit models for fairness and write an audit memo;
- [ ] engineer and encode features without leakage;
- [ ] communicate with action titles, memos and plain-language uncertainty;
- [ ] serve a real client responsibly, from scoping to handover.
