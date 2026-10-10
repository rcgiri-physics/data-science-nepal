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
Optional Computer Science (Grades 9–10): databases/SQL and introductory programming; compulsory ICT/Maths data handling.

## Answers: practice exercises
1. `df[["district", "province", "population"]].head(10)`.
2. `len(df[df["province"] == 2])` → 3; `df.groupby("province").size()[2]` → 3.
3. `df["population"].median()` → 298,351.
4. `df[(df["ecological_belt"] == "Terai") & (df["population"] > 600000)].sort_values("population", ascending=False)`
   → 12 districts from Terai-09 (1,607,726) to Terai-22 (609,934). SQL: `SELECT * FROM districts WHERE
   ecological_belt = 'Terai' AND population > 600000 ORDER BY population DESC;`
5. `df["male_share"] = df["male"] / df["population"]`; highest: Terai-03 (0.515).
6. `df.groupby("ecological_belt")["literacy_pct"].agg(["min", "max"])` → Hill 64.6–83.6, Mountain 62.6–73.7,
   Terai 61.3–78.1.
7. Sum population and households per province, divide: province 7 (4.72) is largest; province 1 smallest (4.33).
8. `df.assign(above=df["literacy_pct"] > df["literacy_pct"].median()).groupby("ecological_belt")["above"].sum()` →
   Hill 32, Mountain 1, Terai 4 (True counts as 1).
9. The first returns a sorted copy that is shown and then lost; the second replaces `df` with the sorted copy.
10. `def top_n(df, column, n): return df.sort_values(column, ascending=False).head(n)[["district", column]]`;
    `top_n(df, "population", 3)` → Terai-09, Terai-17, Terai-15.

Lesson 4 Make: weighted people abroad per 1,000 by province: 6 highest (94.1), then 4 (89.7); province 2 lowest
(56.2).

## Real-data exercises: notes
* **R1** Column names in the ODN file must be checked first (`df.columns`); some files have spaces or units in
  names — rename with `df.columns = [...]` or `df.rename(columns={...})`.
* **R2** Typical columns: `SN, Commodity, Date, Unit, Minimum, Maximum, Average`; convert `Date` with
  `pd.to_datetime` and use `df["Date"].dt.year`. Expect a few seconds to load.
* **R3** The "South Asia" aggregate is population-weighted (dominated by India), while the mean of 8 countries
  weights each equally.
