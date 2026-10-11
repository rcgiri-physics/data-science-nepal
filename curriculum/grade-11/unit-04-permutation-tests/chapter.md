# Grade 11 · Unit 4: Is it chance? Permutation tests

> Track: B (code) · Tools: Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** To ask if a difference between two groups could be just chance, shuffle the labels many times and see how often chance alone produces such a difference.

**What you will be able to do**

* I can state a null hypothesis and explain what shuffling labels imitates.
* I can run a permutation test and compute a p-value.
* I can interpret a p-value honestly, alongside an effect size and an interval.

**Words to know:** hypothesis, null hypothesis, test statistic, permutation (shuffle), p-value, statistically significant, effect size, false positive, multiple testing, randomised experiment. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/permutation.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Unit 3: sampling variation and intervals. Grade 10 Unit 3: correlation is not causation. Setup:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = pd.read_csv("health_synthetic.csv")
hill = h[h["ecological_belt"] == "Hill"]
mountain = h[h["ecological_belt"] == "Mountain"]
```

---

## Lesson 1: The idea of chance

**Hook (5 min).** Two cricket teams from the same school play; Team A scores 12 runs more than Team B. Is Team A better,
or did they just get lucky today? What would convince you?

### Explanation
In the synthetic health table, 42.1% of Hill births were in a health facility, compared with 32.5% of Mountain births:
a difference of **9.6 percentage points**. Before we try to explain it (distance to facilities? roads? wealth?), we
should ask a humbler question: **could a difference this big appear just by chance**, even if belt made no difference
at all?

The **null hypothesis** (H₀) is the "nothing going on" story: *belt and facility delivery are unrelated; the Hill and
Mountain labels are just names.* If H₀ were true, the labels would be interchangeable: we could shuffle them among the
records and nothing important would change.

**The shuffle idea (unplugged):**
1. Write each record's outcome (1 = facility, 0 = home) on a card: 696 Hill cards and 157 Mountain cards.
2. Shuffle all 853 cards together and deal 696 into a "Hill" pile and 157 into a "Mountain" pile.
3. Compute the difference in the share of 1s between the piles.
4. Repeat many times. These differences show what **chance alone** produces when H₀ is true.
5. Compare the **observed** difference (9.6 points) with the shuffled ones. If shuffles rarely produce a difference this
   large, chance is a poor explanation.

This is a **permutation test** (permutation = rearrangement). It needs no formulas, only the willingness to let the
computer shuffle thousands of times.

### Activity (20 min)
1. **Unplugged, small version:** the teacher prepares 20 cards — Group A outcomes 1,1,1,0,1,1,0,1,1,1 and Group B
   outcomes 0,1,0,0,1,0,0,1,0,0. Compute the observed difference in proportions (A − B).
2. In pairs, shuffle and deal 10–10 five times; record each difference on the board.
3. Pool the class's shuffles in a dot plot. How many are at least as large as the observed difference (in either
   direction)? Is chance a believable explanation?

### Common mistakes
* Thinking the test asks "is H₀ true?" — it asks "how surprising would our data be **if** H₀ were true?"
* Forgetting that shuffling keeps the group sizes the same.

**Check (5 min).**
1. What does shuffling labels imitate?
2. What do we compare to?
3. What is chance variation?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Run a permutation test

**Hook (5 min).** Shuffling cards 5,000 times would take a class a week. A computer does it in a second. What exactly
must we tell it to do?

### Explanation
```python
def permutation_test(a, b, n_shuffles=5000, seed=0):
    """Two-sided permutation test for a difference in means (or proportions, for 0/1 data).
    Returns the observed difference (mean a − mean b), the p-value and all shuffled differences."""
    rng = np.random.default_rng(seed)
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    observed = a.mean() - b.mean()
    pooled = np.concatenate([a, b])
    diffs = np.empty(n_shuffles)
    for i in range(n_shuffles):
        rng.shuffle(pooled)                                   # shuffle all values together
        diffs[i] = pooled[:len(a)].mean() - pooled[len(a):].mean()
    p_value = np.mean(np.abs(diffs) >= abs(observed))         # share at least as extreme
    return observed, p_value, diffs

obs, p, diffs = permutation_test(hill["institutional_delivery"], mountain["institutional_delivery"])
print(f"observed difference {obs:.3f}, p-value {p:.3f}")     # observed difference 0.096, p-value 0.033

plt.hist(diffs, bins=40)
plt.axvline(obs, color="black")
plt.axvline(-obs, color="black", linestyle="--")
plt.xlabel("Difference in facility-delivery share (Hill − Mountain) under shuffling")
plt.show()
```

* The **test statistic** is the difference in means (for 0/1 data, a difference in proportions).
* **Two-sided:** we count shuffles as extreme as the observed in **either** direction (`abs`), because before looking we
  had no reason to expect Hill to be higher rather than lower.
* The **p-value** is the share of shuffles at least as extreme as the observed difference: here about **0.03**. If belt
  made no difference, a gap of 9.6 points or more would turn up in only about 3% of random relabellings.

**Reading the p-value**
* Small p (conventionally < 0.05): the data would be **surprising** if H₀ were true, so chance alone is a weak
  explanation. Researchers call this "statistically significant at the 5% level".
* Large p: the data are **compatible** with chance. That does **not** prove there is no difference — the sample may be
  too small to tell.

A second test on the same groups: mean birth weight, Hill 2.892 kg vs Mountain 2.880 kg (difference 0.012 kg),
p ≈ **0.77** — such a small difference is entirely ordinary under shuffling.

**How many shuffles?** The p-value itself is estimated by simulation; with 5,000 shuffles it is accurate to about ±0.005
around 0.03. Use more (10,000–50,000) when p is close to a decision threshold.

### Activity (20 min) — PRIMM
1. **Predict** whether the Hill–Mountain difference in facility delivery will look like chance; run the test.
2. Run the birth-weight test. Draw both histograms of shuffled differences with the observed line.
3. **Investigate:** change `n_shuffles` to 500 and to 20,000 with different seeds. How much does p wobble?
4. **Make:** test Terai vs Hill for facility delivery, and women under 25 vs 25+ for antenatal visits.

### Common mistakes
* One-sided counting when the question was two-sided (halves the p-value unfairly).
* Shuffling within one group instead of the pooled data.
* Forgetting that p depends on sample size: tiny differences in huge samples can have tiny p.

**Check (5 min).**
1. p-value = ?
2. Why 5,000 shuffles?
3. What does a tiny p-value suggest?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Interpreting results honestly

**Hook (5 min).** A study reports p = 0.03. Tomorrow's headline: "PROVEN: Mountain women avoid health facilities!" List
everything wrong with that headline.

### Explanation
A p-value answers one narrow question: *how surprising are these data under the chance-only story?* It does **not** tell
you:

| A p-value does not tell you… | Instead, report… |
|---|---|
| how **big** or important the difference is | the **effect size**: "9.6 percentage points" |
| how **precise** the estimate is | a **confidence interval** (bootstrap, Unit 3) for the difference |
| **why** the difference exists (cause) | the **design**: randomised experiment, or observational data with possible confounders |
| the probability that H₀ is true | — (that needs other methods and assumptions) |
| whether the data were collected fairly | how the sample was drawn, who is missing |

In our example the groups were **not randomised**. Mountain and Hill women differ in wealth, roads, distance and much
more, so even a real difference says nothing about *what* causes it. Tests on **randomised experiments** (e.g. a
reminder SMS sent to a random half of pregnant women) do support causal conclusions, because randomisation makes
the groups alike on everything else.

**Multiple testing.** If you run 20 tests where nothing is going on, you expect about 1 of them to have p < 0.05 by
chance alone (5% of 20). Testing many variables and reporting only the "significant" one ("p-hacking") creates false
discoveries. Decide your main question in advance, report every test you ran, and treat surprising single results as
ideas to check with new data.

**Statistically significant ≠ important.** With 100,000 records, a 0.3-point difference can have p < 0.001 and matter
to nobody. With 30 records, a 20-point difference can have p = 0.2 and matter a lot (and deserve a bigger study).

**An honest result sentence:**
> "In this synthetic sample, 42% of Hill births and 33% of Mountain births were in a facility (difference 9.6
> percentage points; permutation test p ≈ 0.03). A difference this large would be unusual if belt were unrelated to
> facility delivery. The data are observational and synthetic, so they do not show why the difference exists."

### Activity (20 min)
1. Rewrite three over-claiming headlines honestly (e.g. "p = 0.04: tuition proven to raise marks"; "p = 0.3: the new
   bridge had no effect on attendance"; "Scientists find chocolate makes you smarter (p = 0.049)").
2. Bootstrap a 95% interval for the Hill − Mountain difference (resample each group, compute the difference) and add it
   to the result sentence.
3. **Multiple-testing demonstration:** randomly split the table into two fake groups 100 times and test birth weight
   each time (500 shuffles per test is enough). Nothing real is going on, yet about 5 in 100 tests are expected to give
   p < 0.05 — your count may be anywhere from about 1 to 10. Compare counts across the class and discuss.

### Common mistakes
* "p < 0.05 means it's true / important / causal."
* "p > 0.05 means there is no difference."
* Reporting only the significant results.

**Check (5 min).**
1. Does small p show a large effect?
2. Does large p show no difference?
3. What else to report?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Null hypothesis = chance-only story; shuffling labels simulates it.
* Permutation test: pool, shuffle, split, compute the statistic, repeat; p-value = share of shuffles at least as
  extreme (two-sided: compare absolute values).
* Small p: data surprising under chance. Large p: compatible with chance, not proof of no difference.
* Always report effect size, an interval and the design; randomisation is needed for causal claims.
* Many tests → false alarms; pre-specify and report everything.

## Practice exercises
1. ★ Write the null hypothesis for: "Do girls and boys in our school sleep different amounts?"
2. ★ Out of 2,000 shuffles, 140 gave a difference at least as extreme as observed. What is the p-value?
3. ★ True or false (explain): "p = 0.01 means there is a 1% chance the null hypothesis is true."
4. ★★ Run a permutation test for mean antenatal visits, Mountain vs Terai. Report the difference, p and an honest
   sentence.
5. ★★ Take a random sample of 60 records (`h.sample(60, random_state=4)`) and repeat the Hill–Mountain facility test.
   What happens to p? Why?
6. ★★ Modify `permutation_test` to use the difference in **medians**. Test birth weight, facility vs home deliveries.
7. ★★ Why is a two-sided test the default? When could a one-sided test be justified?
8. ★★★ A school tries a new reading programme in the 3 sections whose teachers volunteered, and compares with 3 other
   sections. The test gives p = 0.01. Why is a causal conclusion still weak? How would you redesign the study?
9. ★★★ A researcher tests 40 different foods against exam marks and finds 2 with p < 0.05. What should they conclude?
10. ★★★ Explain the connection between a permutation test and a bootstrap interval for the same difference. If the
    95% interval for a difference excludes 0, what do you expect the p-value to be roughly?

## Exercises with real data
**R1. Penguins by sex (RD-17).** Test whether male and female Adelie penguins differ in mean body mass. Report the
difference in grams, p and a bootstrap CI. Then test bill depth between two islands for the same species.
*Offline fallback:* Hill vs Terai birth weight in the health table.

**R2. Monsoon then and now (RD-06 / RD-07).** For your town, compare July rainfall totals in 1991–2005 with 2006–2020
using a permutation test. Is the difference larger than chance? Why might years not be "interchangeable" (trends,
autocorrelation)?

**R3. Air quality on holidays (RD-12).** In the real Kathmandu data, compare PM2.5 on public holidays/strike days (choose
dates from news) with comparable ordinary days in the same months. Discuss why matching months matters.

## Unit project: Chance or real?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Pre-register (write down before analysing) one
question comparing two groups. Run the permutation test with a histogram, a bootstrap interval for the difference, and
an honest result sentence that states effect size, p, interval, design and limits. Report any extra tests you ran.
Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* American Statistical Association, "Statement on p-values" (2016) — six principles, short and readable.
* OpenIntro Statistics (free), the randomisation tests sections.
* "Statistics without the agonizing pain" (John Rauser, talk on YouTube) — permutation tests explained in 10 minutes.
