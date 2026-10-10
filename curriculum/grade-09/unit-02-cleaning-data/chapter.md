# Grade 9 · Unit 2: Cleaning data

> Track: A/B (spreadsheet + notes) · Tools: spreadsheet, cleaning log · Lessons: 4
> Datasets: `kathmandu-air-quality`

**Big idea.** Real data are messy. Cleaning is detective work, and every change must be written down so others can check it.

**What you will be able to do**

* I can find and handle missing values and error codes.
* I can standardise inconsistent names and remove duplicates.
* I can convert units, types and BS/AD dates.
* I can keep a cleaning log that someone else could follow.

**Words to know:** missing value (हराएको मान), error code, duplicate, lookup table, data type, ISO date, Bikram Sambat (BS), cleaning log. Full list: `curriculum/framework/glossary.md`.

### Before you start
From Unit 1: tidy tables, formulas, sort and filter. From Grade 8 Unit 5: the mean is pulled by extreme values.
Open `datasets/kathmandu-air-quality/clean/air_daily_synthetic.csv` (731 days of **synthetic** PM2.5 and PM10 for
2019–2020, made deliberately messy).

> **Why PM2.5?** PM2.5 means particles smaller than 2.5 micrometres, about 30 times thinner than a hair. They go
> deep into the lungs. It is measured in micrograms per cubic metre (µg/m³). Kathmandu's winter air often has
> several times the World Health Organization's guideline value.

---

## Lesson 1: Missing values and error codes

**Hook (5 min).** A pollution sensor reports PM2.5 = −999 µg/m³ on 18 March 2019. What does that mean? Can air have
negative pollution?

### Explanation
Data scientists often say that 60–80% of their time goes into cleaning. Cleaning is not "making the data look nice";
it is finding out **what the data really say** and fixing only what is clearly wrong, while keeping a record.

**Missing values** are cells with no value. They happen when a sensor is switched off, a form question is skipped, or
a page of a register is lost. In a CSV they appear as empty cells; other datasets use `NA`, `N/A`, `-`, `.` or `null`.

**Error codes** (also called sentinel values) are fake numbers that mean "no valid reading": `-999`, `-99`, `9999`,
`0` in some sensors. They are dangerous because they **look like numbers**, so formulas use them.

**Worked example.** The synthetic air table has 731 days. Investigating `pm25`:

| Check | Formula | Result |
|---|---|---|
| Number of rows | `=COUNTA(A2:A732)` | 731 |
| Blank pm25 cells | `=COUNTBLANK(B2:B732)` | 25 |
| Error codes | `=COUNTIF(B2:B732,-999)` | 4 (2019-03-18, 2019-03-28, 2020-06-11, 2020-09-13) |
| Mean with −999 left in | `=AVERAGE(B2:B732)` | 46.8 µg/m³ |
| Mean after −999 → blank | `=AVERAGE(...)` again | **52.8** µg/m³ |

Four bad values out of 706 dragged the mean down by 6 µg/m³, more than 10%. (`AVERAGE` already ignores the 25
blanks.)

**What to do with missing values: three options**
1. **Leave them missing** and say how many there are. Usually the best first choice.
2. **Remove the rows** — only if the row is useless without that value, and say how many you removed.
3. **Fill them** (impute), e.g. with the previous day's value — only with a stated reason, and never silently. Grade
   10 discusses this.

**Look at *where* values are missing.** If all 25 missing days were in winter, the yearly average without them would
be too low, because winter is the most polluted season. Missingness itself can be a pattern.

**Never fix the original file.** Keep the raw data untouched; clean a **copy**, and record each step in a **cleaning
log**:

| # | Problem found | Rows affected | What I did | Why |
|---|---|---|---|---|
| 1 | `pm25` = −999 | 4 | replaced with blank | sensor error code; negative concentration impossible |
| 2 | `pm25` blank | 25 | left blank; reported | no valid reading; filling would invent data |

### Activity (20 min)
1. Make a copy of the air table (new sheet or new file). Keep the original unchanged.
2. Use `COUNTBLANK` and `COUNTIF(…,-999)` to count blanks and error codes in both `pm25` and `pm10`.
3. Compute the mean `pm25` with the codes left in; then use Find & Replace (whole-cell match) to replace `-999` with
   nothing and compute again.
4. Filter blanks: in which months are the missing days? Is there a pattern?
5. Start your cleaning log with steps 1 and 2.

### Common mistakes
* Replacing −999 with 0. Zero is a (very clean) real value; it still pulls the mean down.
* Deleting every row that has any problem, losing good data in other columns.
* Fixing values "by eye" without writing it down.

**Check (5 min).**
1. Why is -999 not a real PM2.5 reading?
2. What happens to the mean if we leave -999 in?
3. What goes in a cleaning log?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Duplicates and inconsistent names

**Hook (5 min).** One column contains `Chitwan`, `Chitawan`, `CHITWAN`, ` Chitwan` (with a space) and `चितवन`. How
many districts is that? How many will a pivot table think it is?

### Explanation
Computers compare text **exactly**. To a pivot table or SQL `GROUP BY`, `Chitwan` and `Chitawan` are different
districts, so totals are split and counts are wrong. Common causes in Nepal:

* **Romanisation:** Nepali names written in Roman letters several ways (Chitwan/Chitawan, Kavre/Kavrepalanchok,
  Sindhupalchok/Sindhupalchowk, Dhanusha/Dhanusa).
* **Case and spaces:** `CHITWAN`, `chitwan`, `Chitwan ` (trailing space, invisible!).
* **Two scripts:** Devanagari and Roman in the same column.
* **Old and new names:** places renamed after 2015 (e.g. provinces: "Province 1" became Koshi Province in 2023).

**Fix with a lookup table.** Make a small separate table: every spelling found → one **standard** name (and the
Nepali form). Then add a column that looks up the standard name.

| raw_name | standard_name | name_ne |
|---|---|---|
| Chitwan | Chitwan | चितवन |
| Chitawan | Chitwan | चितवन |
| CHITWAN | Chitwan | चितवन |
| चितवन | Chitwan | चितवन |

Spreadsheet tools: `=TRIM(A2)` removes extra spaces; `=PROPER(A2)` makes "Title Case"; `=VLOOKUP(A2, lookup!A:B, 2,
FALSE)` (or `XLOOKUP`) finds the standard name; `#N/A` means a spelling is not in your lookup yet: add it.

**Better still, use codes.** Official tables give every district a number (a **key**). Joining or grouping on a key
avoids spelling problems entirely; Unit 3 relies on this.

**Duplicates** are the same record entered twice (a form submitted twice; a day copied twice). Find them by sorting
(identical rows end up together), with conditional formatting → "duplicate values", or with Data → More Filters →
"no duplications" (Calc) / Remove duplicates (Sheets/Excel) **on a copy**. In the air table each date should appear
once; `=COUNTIF(A:A,A2)>1` flags repeated dates.

### Activity (20 min)
1. Your teacher gives (or you write) a list of 20 entries with district names in mixed spellings, cases, spaces and
   scripts.
2. Count the "districts" with a pivot table before cleaning.
3. Build a lookup table and a `standard_name` column using `TRIM` and `VLOOKUP`.
4. Count again. How many real districts? Add the steps to your cleaning log.
5. In the air table, check that no date is duplicated.

### Common mistakes
* Not seeing trailing spaces: use `=LEN(A2)` to reveal them.
* Fixing names by hand one by one (slow, error-prone, not reusable). A lookup table can be reused next year.
* Removing "duplicates" that are actually two different people with the same name.

**Check (5 min).**
1. Why do inconsistent spellings matter for GROUP BY?
2. What is a lookup table?
3. How can you spot duplicates in a spreadsheet?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Units and types

**Hook (5 min).** A column of travel times contains `2 hrs`, `45 min`, `1.5`, `30` and `half hour`. Can we average
it? What does `1.5` mean?

### Explanation
Every column should have **one unit** and **one type**. Mixed columns arrive whenever people type freely. Cleaning
them has three steps:

1. **Decide the unit** (minutes) and write it in the header (`travel_minutes`).
2. **Convert each value** with a written rule:
   * `2 hrs` → 2 × 60 = 120
   * `45 min` → 45
   * `half hour` → 30
   * `1.5` → ambiguous! Hours (90) or minutes (1.5)? Check with the person, or mark missing. Never guess silently.
3. **Make the type numeric**, then check with `=ISNUMBER(B2)` or by sorting (text sorts separately from numbers).

**Common unit conversions in Nepali data**

| From | To | Rule |
|---|---|---|
| hours | minutes | × 60 |
| kg | g | × 1,000 |
| ropani (hill land) | m² | × 508.72 |
| bigha (Terai land) | m² | × 6,772.63 |
| lakh | number | × 100,000 |
| crore | number | × 10,000,000 |
| mm/day (rain rate) | mm per month | × days in that month |

**Number formats.** `1,50,000` (Nepali/Indian grouping) is 150,000; `1,500.5` uses a decimal point; some European
software writes `1.500,5`. If a file comes from another system, check how commas and dots are used before converting.
**Leading zeros** in codes (`007`) disappear if the column is treated as a number; keep codes as text.

### Activity (20 min)
1. Clean this column into minutes, writing a rule for each: `2 hrs`, `45 min`, `1.5`, `30`, `half hour`, `1 hr 20
   min`, `90 mins`, `20-25`, `?`, `0`.
2. Decide how to treat the ambiguous ones (`1.5`, `20-25`, `?`) and justify your choice in the log.
3. Convert these land areas to m²: 4 ropani; 2 bigha; 0.5 ropani.
4. Convert: Rs 3.5 lakh, Rs 12 crore, 1,50,000.

### Common mistakes
* Assuming a bare number has the unit you expect.
* Converting text to numbers by deleting characters until "it works".
* Losing leading zeros from codes.

**Check (5 min).**
1. 2.5 hours in minutes?
2. Why put the unit in the header?
3. What is wrong with '1,50' in some systems?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 4: BS and AD dates, and the cleaning log

**Hook (5 min).** Is 2080 Baisakh 1 before or after 1 April 2023? A dataset has some dates in BS and some in AD.
What could go wrong if you sort it?

### Explanation
Nepal officially uses the **Bikram Sambat (BS)** calendar. Government reports, school records and many datasets use
BS dates; international data (and most software) use the Gregorian **AD** calendar.

* The BS year starts in **mid-April** (Baisakh 1). BS 2080 Baisakh 1 = **14 April 2023**.
* From Baisakh 1 to the end of the AD year (mid-April to 31 December): **AD year = BS year − 57**.
* From 1 January to the end of Chaitra (January to mid-April): **AD year = BS year − 56**.
* BS months do not line up with AD months, and their lengths (29–32 days) change from year to year, so exact
  conversion needs a **conversion table** or a tool (the Nepali calendar on your phone, or the official calendar).
  Never convert exact days with a formula like "subtract 57 years".

**Fiscal year.** Nepal's fiscal year runs from Shrawan 1 (mid-July) to Asar end (mid-July next year), written like
**2080/81**. Many government tables (budget, trade, tourism) use fiscal years, not calendar years.

**Store dates as ISO.** The international standard **ISO 8601** writes dates as `YYYY-MM-DD` (2023-04-14). They sort
correctly as text and nobody confuses day and month (is `04/05/2023` 4 May or 5 April?). Keep the **original** date in
its own column (`date_bs`) next to the converted one (`date_ad`) so anyone can check the conversion.

**The cleaning log.** By the end of a cleaning job your log should let a classmate repeat every step and get the same
table. A good log has:
* source file name and date downloaded;
* each problem, how many rows, what you did, why;
* final row count and what remains unresolved;
* your name and the date.

### Activity (20 min)
1. Convert these BS dates to approximate AD year and season: 2078 Shrawan 15; 2079 Poush 10; 2080 Magh 5; 2072
   Baisakh 12 (the Gorkha earthquake); 2081 Asar 30; 2081 Chaitra 1.
2. For two of them, find the exact AD date using a Nepali calendar app or printed calendar.
3. Finish the one-page cleaning log for the air table: problems, counts, fixes, final counts, unresolved issues.
4. Swap logs with a partner. Could they repeat your work from your log alone?

### Common mistakes
* Subtracting 57 for every date, including January to mid-April (should be 56).
* Mixing BS and AD in one column.
* Writing dates as `04/05/23`.

**Check (5 min).**
1. Roughly, BS year minus 57 gives…
2. Why store ISO dates?
3. Why keep the original column?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Keep raw data untouched; clean a copy; **log every step**.
* Blanks are missing; codes like −999 are **errors that look like numbers**; replace them with blank, never 0.
* Look at where values are missing: missingness can have a pattern.
* Standardise names with **TRIM**, **PROPER** and a **lookup table**; better, use codes as keys. Remove duplicates
  carefully.
* One unit and one numeric type per column; write conversion rules; ask about ambiguous values.
* BS → AD: −57 from mid-April to December, −56 from January to mid-April; exact dates need a table. Store ISO
  `YYYY-MM-DD`; keep the original column.

## Practice exercises
1. ★ A column of ages has values 14, 15, 0, 13, 999, 14, (blank). Which values are suspicious and why?
2. ★ Write the ISO form of: 5 March 2024; 25 April 2015; 1 January 2000.
3. ★ Convert to minutes: 3 hours; 1 hr 45 min; 0.25 hours.
4. ★★ The mean of 10 PM2.5 readings is 60. Then you find that one value was −999 and should be missing. What is the
   correct mean of the other 9? (Hint: total = mean × count.)
5. ★★ Give three spellings of "Kavrepalanchok" you might find in data, and write the lookup rows.
6. ★★ Convert: 2081 Kartik 15 to the AD year; 2080 Falgun 10 to the AD year; 2082 Baisakh 1 to the AD date (use a
   calendar).
7. ★★ A school file stores student codes 001–120 as numbers. What goes wrong? How do you fix it?
8. ★★★ All 25 missing PM2.5 days in a real dataset are in December and January. The yearly mean without them is
   48 µg/m³. Is the true yearly mean likely higher or lower? Why?
9. ★★★ A survey column has `1.5` for travel time. Give two ways to deal with it and the risk of each.
10. ★★★ Write a 6-line cleaning log for this mini-table (columns: `date, district, rain`): `2080-04-01, chitwan, 12mm`
    · `2080-04-01, Chitawan, 12` · `2023-07-18, Chitwan, -99` · `2080-04-03, Chitwan, 8`.

## Exercises with real data
**R1. Clean NASA POWER (RD-07).** Download monthly temperature and rain for your town from NASA POWER (link pattern
in `docs/datasets/free-datasets.md`) and open it in a spreadsheet. Clean it: (a) remove the header block
(`-BEGIN HEADER-` … `-END HEADER-`) and note what it said; (b) find and blank any `-999`; (c) `PRECTOTCORR` is in
**mm per day**: add a row converting each month to mm per month (× days in the month); (d) write the log.
*Offline fallback:* clean the synthetic air table (Lessons 1–4).

**R2. Real air data (RD-12).** Download the Kathmandu air-quality CSV from Open Data Nepal (≈8 MB, open in a
spreadsheet). How many rows? How are missing values marked? Are there impossible values (negative, extremely high)?
Are there several stations or pollutants in one column (untidy)? Write a log of problems found (you do not need to
fix them all).

**R3. Names across datasets (RD-11 / RD-09).** Compare the district or station names in two Open Data Nepal tables
(e.g. census preliminary and rainfall by station). List names that are spelled differently, and build a lookup table
for them.

## Unit project: Clean it and log it
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Clean the synthetic air table (or a real
table from R1/R2) and hand in: the cleaned file, a one-page cleaning log, before/after means of PM2.5, and three
sentences on how cleaning changed the answer. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* OpenRefine (<https://openrefine.org>, free, offline): a powerful tool for cleaning messy text columns ("clustering"
  finds Chitwan/Chitawan automatically).
* Hamro Patro and other Nepali calendar apps, or the official calendar from the Nepal Panchanga Nirnayak Bikas
  Samiti, for exact BS ↔ AD conversion.
