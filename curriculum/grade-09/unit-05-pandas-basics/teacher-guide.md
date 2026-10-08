# Teacher guide — Grade 9, Unit 5: Tables in pandas

**Time:** 4 lessons + project (about 6 periods). **Track:** B (code: pandas).

| # | Lesson | Time |
|---|---|---|
| 1 | Load and inspect | 40–45 min |
| 2 | Select and filter | 40–45 min |
| 3 | Sort and new columns | 40–45 min |
| 4 | Group and summarise | 40–45 min |
| P | Unit project: Same question, SQL and pandas | 2 periods |

## Before you start
* Materials: Notebook `notebooks/pandas_basics.ipynb`.
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
No computers? Do the unplugged version: print the 10-row extract of the table and carry out each SQL idea by hand (cross out rows for WHERE, sort strips for ORDER BY, make piles for GROUP BY, match ID cards for JOIN). Track B coding cannot be replaced fully; plan it for a lab day.

## Common misconceptions
* df[df.belt == 'Hill'] needs ==, not =.
* Methods usually return a new table; they don't change the original unless you assign.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Load and inspect**
1. Which method shows the first rows?  
   *Answer:* .head()
2. What does .shape return?  
   *Answer:* (rows, columns).
3. Why check dtypes?  
   *Answer:* Numbers stored as text can't be averaged.

**Lesson 2: Select and filter**
1. df[df['ecological_belt']=='Hill'] does what?  
   *Answer:* Keeps only the Hill rows.
2. Combine two conditions with…  
   *Answer:* & (with parentheses around each).
3. SQL twin of a filter?  
   *Answer:* WHERE.

**Lesson 3: Sort and new columns**
1. df['rate'] = 1000*df.a/df.b creates…  
   *Answer:* A new column with a rate per 1,000.
2. Why rank by rate not count?  
   *Answer:* Counts follow population size.
3. ascending=False means…  
   *Answer:* Largest first.

**Lesson 4: Group and summarise**
1. groupby('belt').size() returns…  
   *Answer:* The number of rows in each belt.
2. How can you check a grouped result?  
   *Answer:* Counts add up to the total rows.
3. SQL twin?  
   *Answer:* GROUP BY with aggregates.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming (⚠️ confirm exact grade and unit in the CDC syllabus PDF); compulsory ICT/Maths data handling.
