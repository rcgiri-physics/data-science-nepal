# Grade 8 · Unit 6: Comparing groups

> Track: A (no-code) · Tools: paper, calculator · Lessons: 3
> Datasets: `census-districts`

**Big idea.** Fair comparisons use rates, not raw counts, and compare like with like.

**What you will be able to do**

* I can compute and compare rates (per 100, per 1,000).
* I can compare two groups with medians and side-by-side dot plots.
* I can tell percentage points from percent change.

**Words to know:** rate (दर), percentage (प्रतिशत), per capita (प्रतिव्यक्ति), percentage point, comparison, fair comparison. Full list: `curriculum/framework/glossary.md`.

### Before you start
From Unit 3: relative frequency (share of the total). From Unit 5: median, range, and describing a distribution.
This unit uses the **synthetic** district table `districts_synthetic.csv`: the district names (Hill-01, Terai-09…) and
numbers are invented so that we can practise freely. Real census numbers appear in the real-data exercises.

---

## Lesson 1: Counts versus rates

**Hook (5 min).** District P has 900 girls in school; district Q has 600. Which district is doing better at getting
girls into school? Vote, then wait for one more fact.

### Explanation
A **count** is how many: 900 girls enrolled. Counts depend on **size**: a big district has big counts of almost
everything — schools, students, accidents, doctors, births. Comparing counts of places with different sizes mostly
tells us which place is bigger.

A **rate** divides the count by the size of the group it comes from:

> rate = count ÷ size of the group (× 100 for percent, × 1,000 for "per 1,000")

Now the missing fact: P has 1,800 girls of school age; Q has 1,000.
* P: 900 ÷ 1,800 = 0.50 = **50%** enrolled.
* Q: 600 ÷ 1,000 = 0.60 = **60%** enrolled.
Q is doing better, even though its count is smaller.

**Choosing "per what?"**
* Percent (per 100) for common things: literacy, enrolment, households with a tap.
* Per 1,000 for rarer things: births, deaths (the *crude birth rate* is births per 1,000 people per year).
* Per 100,000 for very rare things: road deaths, cases of a disease.
* **Per capita** (प्रतिव्यक्ति) means "per person": GDP per capita = total income ÷ population.

To change between them, multiply or divide by 10s: 45 per 1,000 = 4.5 per 100 = **4.5%**.

**The denominator must match the count.** Girls enrolled ÷ *girls of school age*, not ÷ total population. Deaths of
children under 5 ÷ *live births*, not ÷ all people.

**Worked example (synthetic districts).** Six districts and the number of people living abroad ("absentee
population"):

| District | Population | Absentee population | Rank by count | Absentee rate (%) | Rank by rate |
|---|---|---|---|---|---|
| Terai-09 | 1,607,726 | 111,228 | 1 | 6.9 | 4 |
| Terai-15 | 1,116,962 | 56,035 | 2 | 5.0 | 6 |
| Hill-05 | 524,892 | 31,515 | 3 | 6.0 | 5 |
| Hill-03 | 204,455 | 20,930 | 4 | 10.2 | 2 |
| Mountain-08 | 84,505 | 6,830 | 5 | 8.1 | 3 |
| Hill-13 | 51,855 | 5,680 | 6 | 11.0 | 1 |

Rate for Hill-13: 5,680 ÷ 51,855 × 100 ≈ 11.0%. By count Hill-13 is last; by rate it is **first**: more than one person
in nine from Hill-13 lives abroad. A planner deciding where migration matters most for families would use the rate.

### Activity (20 min)
1. Copy the six districts (population and absentee population only).
2. Rank them by the absentee **count**.
3. Compute each **rate** (absentee ÷ population × 100, one decimal place) and rank again.
4. Draw a line from each district's count rank to its rate rank. Which district moved most?
5. Write one sentence a newspaper should *not* write using counts, and the fair version using rates.

### Common mistakes
* Comparing counts of places with different sizes.
* Using the wrong denominator (total population instead of the group the count comes from).
* Forgetting to say "per what" ("the rate is 11" — 11 per 100? per 1,000?).

**Check (5 min).**
1. District P: 900 of 1,800 children enrolled; Q: 600 of 1,000. Which has the higher enrolment rate?
2. Why is a count unfair across districts?
3. Convert 45 per 1,000 to a percent.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Comparing two groups

**Hook (5 min).** Do Hill districts have higher literacy than Mountain districts in our (synthetic) table? How would
you show it convincingly to someone who does not believe you?

### Explanation
To compare two (or more) groups fairly:

1. **Use the same measure** for every group (median literacy for each belt, not the median for one and the mean for
   another).
2. **Show them on the same scale**: two dot plots one above the other on one number line, so the eye compares
   positions directly.
3. **Say how big the difference is**, in units: "11 percentage points higher", not just "higher".
4. **Look at the overlap.** If most values in one group are higher than most in the other, the difference is
   **consistent**. If the dot plots overlap a lot, the difference in medians may not mean much for any single district.
5. **Compare like with like.** Mountain districts are remote and sparsely populated; differences may be about
   distance, not about the people. Say what else differs between the groups.

**Worked example.** The first ten districts of the synthetic table, literacy (%):

| Belt | Districts | Literacy values | Median |
|---|---|---|---|
| Mountain | 3 | 62.6, 66.2, 66.7 | 66.2 |
| Hill | 5 | 73.1, 76.9, 78.8, 78.9, 82.2 | 78.8 |
| Terai | 2 | 69.9, 78.1 | 74.0 |

```
Literacy (%)   60    65    70    75    80    85
Mountain        ●     ● ●
Hill                         ●    ● ●●  ●
Terai                       ●         ●
```

Comparison sentence: "In these ten (synthetic) districts, the median literacy in Hill districts (78.8%) is
12.6 percentage points higher than in Mountain districts (66.2%), and every Hill district is above every Mountain
district, so the difference is consistent. With only 2 Terai districts we cannot say much about the Terai." Notice
the last clause: **small groups give shaky medians.**

### Activity (20 min)
1. Using the full district table (77 rows) or the 10-row extract, split districts by ecological belt.
2. Compute the median literacy of each belt.
3. Draw dot plots for the belts on one number line.
4. Write a comparison sentence that includes: the medians with units, the size of the difference, the overlap, and
   one other thing that differs between the groups.

### Common mistakes
* Comparing only the "best" district of one group with the "worst" of the other.
* Ignoring group size: a median from 2 values is much less reliable than one from 39.
* Concluding that belonging to a group *causes* the difference ("living in the mountains makes people less
  literate"); the cause could be distance to school, poverty, or many other things.

**Check (5 min).**
1. What do you compute for each group before comparing?
2. If belt medians are 66 and 77, what is the difference?
3. Why draw both on the same axis?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Percent change and percentage points

**Hook (5 min).** Literacy in a district rose from 60% to 66%. Headline A: "Literacy up 6%". Headline B: "Literacy
up 10%". Which is right?

### Explanation
Both can be right, because they measure different things:

* **Change in percentage points** (pp) = new % − old % = 66 − 60 = **6 percentage points**.
* **Percent change** (relative change) = (new − old) ÷ old × 100 = (66 − 60) ÷ 60 × 100 = **10%**.

Percent change works for any quantity, not just percentages:
* Price of rice from Rs 80 to Rs 100 per kg: (100 − 80) ÷ 80 × 100 = **25% increase**.
* Tourists from 800,000 to 600,000: (600,000 − 800,000) ÷ 800,000 × 100 = **−25%** (a 25% decrease).

**Watch out:** a 50% fall followed by a 50% rise does *not* get you back. Rs 100 → Rs 50 (−50%) → Rs 75 (+50% of 50).

**Small bases make huge percentages.** Cases of a disease in a village rise from 2 to 6: a "200% increase", but only 4
more people. Always give the counts alongside the percent.

**Which to report?** For things already in percent (literacy, enrolment), say "percentage points" for the difference
and give both the old and new values: "Literacy rose from 60% to 66%, up 6 percentage points." That sentence cannot
mislead anybody.

### Activity (20 min)
1. For each pair, give the change in percentage points and the percent change: 60% → 66%; 80% → 84%; 50% → 45%;
   20% → 30%.
2. Write the most dramatic true headline and the most honest headline for 20% → 30%.
3. A shop raises the price of a notebook from Rs 40 to Rs 50, then has a "20% off" sale. Is the sale price back to
   Rs 40?

### Common mistakes
* Calling a percentage-point change a percent change (or the reverse).
* Dividing by the new value instead of the old value.
* Reporting a big percent from a tiny base without the counts.

**Check (5 min).**
1. 60% to 66%: change in percentage points?
2. Same change as relative percent?
3. Why do headlines sometimes pick the bigger-sounding one?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Counts depend on size; compare places with **rates** (count ÷ group size), choosing per 100, 1,000 or 100,000.
* The denominator must be the group the count comes from.
* Compare groups with the **same summary**, on the **same scale**, saying **how big** the difference is and how much
  the groups **overlap**.
* Small groups give unreliable summaries; differences between groups are not automatically causes.
* **Percentage points** = difference of two percentages; **percent change** = change ÷ old value × 100. Give the old
  and new values.

## Practice exercises
1. ★ A school has 240 girls and 260 boys; 216 girls and 221 boys passed. Compute the pass rate of each. Who did better?
2. ★ Convert: 8 per 1,000 to percent; 2.5% to per 1,000; 0.3 per 100 to per 100,000.
3. ★ Price of petrol rose from Rs 160 to Rs 176 per litre. Percent change?
4. ★★ District X had 150 road deaths and 1,500,000 people; district Y had 40 deaths and 200,000 people. Compute the
   rate per 100,000 for each. Which is more dangerous?
5. ★★ In a village, households with a toilet went from 40% to 70%. Write the change in percentage points and as a
   percent change. Which would you use in a report, and how would you write the sentence?
6. ★★ Two sections' Maths marks (out of 50): A: 22, 25, 31, 33, 34, 38, 40; B: 28, 30, 31, 32, 33, 35, 36. Compare
   them using medians, ranges and dot plots on one axis.
7. ★★ "Kathmandu has the most schools in Nepal, so it has the best access to education." What is wrong with this
   reasoning? What rate would you compute instead?
8. ★★★ A price falls by 20% and then rises by 20%. Is it back where it started? Show with Rs 1,000.
9. ★★★ A report says: "Cases of dengue rose by 300% in our ward." What two questions would you ask before deciding how
   worried to be?
10. ★★★ Using the full synthetic table (77 districts), find the median literacy for each belt. (Answer check:
    Mountain 65.5, Hill 77.5, Terai 70.35.) Why are these different from the 10-district medians in Lesson 2?

## Exercises with real data
**R1. Your district vs Nepal (RD-11 / RD-13).** From the Census 2021 results, find the population and number of
households in your district and in Nepal. Compute the average household size (population ÷ households) for both.
Is your district's household bigger or smaller than Nepal's? Find one other district to compare, and use a rate,
not a count.
*Offline fallback:* compute `population ÷ households` for three synthetic districts of different belts.

**R2. Fair comparison of countries (RD-01).** From the World Bank site, get the population and number of internet
users (% of population, `IT.NET.USER.ZS`) for Nepal, India, Bangladesh and Bhutan for the latest year. Which country
has the most internet users as a **count**? Which has the highest **rate**? Write a fair comparison sentence.

**R3. Then and now (RD-02).** Life expectancy in Nepal was about 54.8 years in 1990 and 69.1 years in 2020 (Our World
in Data, UN WPP estimates). Compute the change in years and the percent change. Find the same values for one
neighbouring country on the OWID life-expectancy chart and compare.

## Unit project: Two places, fair comparison
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose two districts (synthetic, or real
from the census) and one question ("Which has more people abroad?", "Which has more secondary schools for its
population?"). Compute counts *and* rates, show them in a bar chart pair, and write a conclusion that says which
comparison is fair and why. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Our World in Data, "How to read rates and ratios": search the OWID website for "per capita" explainer articles.
* Look up the Nepal Rastra Bank's monthly inflation figure (<https://www.nrb.org.np>) and say it as a percent change
  of what.
