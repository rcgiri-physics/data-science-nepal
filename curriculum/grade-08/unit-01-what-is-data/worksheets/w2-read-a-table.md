# Worksheet 2 — Read a table (Lesson 3)

**SYNTHETIC class table** — 10 invented students (codes only, no names). Source: `datasets/class-survey-synthetic`.

| student_code | travel_mode | travel_minutes | siblings | sleep_hours | height_cm | favourite_subject |
|---|---|---|---|---|---|---|
| S01 | walk | 53 | 0 | 8.2 | 155 | Social |
| S02 | motorbike | 27 | 5 | 6.7 | 165 | Nepali |
| S03 | walk | 40 | 0 | 7.1 | 160 | Science |
| S04 | bicycle | 23 | 1 | 8.1 | 155 | English |
| S05 | bicycle | 11 | 1 | 8.6 | 145 | Science |
| S06 | walk | 48 | 2 | 6.7 | 170 | Science |
| S07 | walk | 21 | 0 | 8.7 | 150 | Social |
| S08 | walk | 7 | 3 | 6.6 | 165 | Social |
| S09 | walk | 12 | 0 | 7.2 | 146 | Maths |
| S10 | walk | 52 | 5 | 8.9 | 171 | Science |

## Questions
1. What does **one row** represent?
2. How many **variables** (columns) are there? (Does `student_code` count as a variable or an ID?)
3. Write the unit of each numerical column.
4. Circle the row for S06. Underline the column `sleep_hours`.
5. How many students walk? Bicycle? Motorbike? Do the counts add to 10?
6. What question could this table help answer? What question could it **not** answer?
7. Who might be missing from a table like this?

## Answer key (teacher)
1. One student (identified by a code).
2. 7 columns; `student_code` is an ID, so 6 real variables: 4 numerical (travel_minutes, siblings, sleep_hours, height_cm) and 2 categorical (travel_mode, favourite_subject).
3. travel_minutes: minutes; siblings: number of siblings (count); sleep_hours: hours; height_cm: centimetres.
5. walk 7, bicycle 2, motorbike 1 → 10. ✓
6. Possible: "How do students travel to school?" Not: "Why do they choose that way?" or anything about other classes.
7. Students absent that day; other sections or grades; students who did not consent.

**Extension (fast finishers):** mean travel_minutes = 294 ÷ 10 = 29.4; median = 25 (sorted: 7, 11, 12, 21, 23, 27, 40, 48, 52, 53). Why do they differ a little?
