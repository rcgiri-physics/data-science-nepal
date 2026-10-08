# For teachers

## Start here (30 minutes)
1. Read `docs/pedagogy/lesson-anatomy.md` (one page).
2. Open `curriculum/grade-XX/README.md` for your grade and pick a unit.
3. Open that unit's `teacher-guide.md`: timing, misconceptions, answer key.
4. Choose your track:
   * **Track A (no-code)** — works with paper, calculator, a spreadsheet or [CODAP](https://codap.concord.org).
   * **Track B (code)** — SQL and Python; needs computers (offline OK).

## If you have no computers
* Grades 8 and most of 9–10: use the printed extracts and worksheets. Every unit's teacher guide has an "if no computers" note.
* Code units: plan a lab day, or use the offline USB bundle on one shared computer with a projector.

## If you have no internet
Build the school bundle on any computer with internet, then copy it by USB:

```bash
python tools/build_offline_bundle.py
```

## Classroom routines
* **Roles** in groups of three: data steward (keeps the table clean), analyst/driver, storyteller. Rotate.
* **Starter quiz**: three questions, one recalling the last lesson.
* **Oral check**: two minutes per group; essential in the AI era.
* **Data rules**: use student codes, never names; ask consent; see Grade 8 Unit 8 and `community/student-data-consent.md`.

## Using AI assistants
See `docs/pedagogy/ai-use-policy.md`: explain, don't answer; disclose; verify; protect people.

## Give feedback
Open a *teacher-feedback* issue or add a note in `pilots/`. Tell us: grade, unit, time taken, what confused students,
what worked, and what you changed.

## Teacher training outline (one day, 6 hours)
| Time | Session |
|---|---|
| 0:00–0:45 | PPDAC and the spiral; do a Grade 8 hook activity as learners |
| 0:45–1:45 | Teach-back of one Track A lesson; misconceptions |
| 1:45–2:45 | Spreadsheet/CODAP data portrait; cleaning log |
| 2:45–3:30 | Lunch |
| 3:30–4:45 | Grade 9 SQL notebook (unplugged first, then run) |
| 4:45–5:30 | Assessment: rubrics, oral checks, AI-use policy |
| 5:30–6:00 | Plan a unit for your school; set up feedback |
