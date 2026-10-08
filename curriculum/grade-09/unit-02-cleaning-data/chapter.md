# Grade 9 · Unit 2: Cleaning data

> Track: A/B (spreadsheet + notes) · Tools: spreadsheet, cleaning log · Lessons: 4 · Version: 0.1 draft (English)
> Datasets: `kathmandu-air-quality`

**Big idea.** Real data are messy. Cleaning is detective work, and every change must be written down so others can check it.

**What you will be able to do**

* I can find missing values and error codes.
* I can fix duplicates, inconsistent names and units.
* I can convert between BS and AD years and keep a cleaning log.

**Words to know:** missing value, error code, duplicate, inconsistent, cleaning log (Nepali glossary: `curriculum/framework/glossary.md`).

---

## Lesson 1: Missing values and error codes

**Hook (5 min).** A pollution sensor reports -999 µg/m³. What does that mean?

**Concept (≤ 5 min).** Blank cells are *missing*. Codes like -999 are *error flags*, not real values; they would wreck an average. Replace them with a blank and note it.

**Activity (20 min).** Find blanks and -999 in the air table; compute the mean with and without removing -999; log each step.

**Check (5 min).**
1. Why is -999 not a real PM2.5 reading?
2. What happens to the mean if we leave -999 in?
3. What goes in a cleaning log?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Duplicates and inconsistent names

**Hook (5 min).** 'Chitwan', 'Chitawan', 'CHITWAN' and 'चितवन' appear in one column. How many districts is that?

**Concept (≤ 5 min).** Same thing spelled differently splits groups. Standardise names with a lookup table (one agreed spelling plus the Nepali form).

**Activity (20 min).** Given a messy list of 20 district-name entries, build a lookup table and count districts before/after cleaning.

**Check (5 min).**
1. Why do inconsistent spellings matter for GROUP BY?
2. What is a lookup table?
3. How can you spot duplicates in a spreadsheet?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Units and types

**Hook (5 min).** A column has both '2 hrs' and '45 min'. Can we average it?

**Concept (≤ 5 min).** Convert to one unit (minutes) and one type (number). Strip words, fix decimal commas, and record the conversion.

**Activity (20 min).** Clean a column of mixed time entries; convert ‘2 hrs’ to 120; document the rule.

**Check (5 min).**
1. 2.5 hours in minutes?
2. Why put the unit in the header?
3. What is wrong with '1,50' in some systems?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: BS and AD dates, and the cleaning log

**Hook (5 min).** Is 2080 Baisakh before or after April 2023?

**Concept (≤ 5 min).** Nepal uses Bikram Sambat (BS), about 56–57 years ahead of AD (BS 2080 Baisakh 1 is 14 April 2023). Mixing the two breaks time analysis. Store dates in one calendar (ideally ISO AD: YYYY-MM-DD) and keep the original in another column. Always finish with a cleaning log.

**Activity (20 min).** Convert 6 BS dates to approximate AD years; write a one-page cleaning log for the air table (issues, fixes, counts, who).

**Check (5 min).**
1. Roughly, BS year minus 57 gives…
2. Why store ISO dates?
3. Why keep the original column?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Clean it and log it

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
