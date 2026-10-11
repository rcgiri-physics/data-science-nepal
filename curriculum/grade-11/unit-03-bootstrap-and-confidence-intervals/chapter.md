# Grade 11 · Unit 3: Uncertainty: bootstrap and confidence intervals

> Track: B (code) · Tools: Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** A sample gives one estimate; resampling shows how much it could vary. A confidence interval is a range that reflects that uncertainty.

**What you will be able to do**

* I can explain sampling variation and how it depends on sample size.
* I can build a bootstrap confidence interval for a mean, a median or a proportion.
* I can interpret an interval correctly — and say what it does not tell us.

**Words to know:** population (समष्टि), sample (नमुना), parameter, statistic, estimate, sampling variation, sampling distribution, standard error, bootstrap, resample, confidence interval (विश्वास अन्तराल), margin of error. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/bootstrap.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

### Before you start
Grade 8 Unit 2 (random samples, bias), Grade 10 Unit 2 (standard deviation). The synthetic health table has 1,500
records; in this unit we **pretend those 1,500 are the whole population** so that we can draw samples from it and see
the truth we are trying to estimate. (In real life you never see the population — that is the whole point.)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = pd.read_csv("health_synthetic.csv")
print(round(h["birth_weight_kg"].mean(), 3))      # 2.886 kg: the "population" mean we pretend not to know
```

---

## Lesson 1: Sampling variation

**Hook (5 min).** Two schools each survey 100 random students about sleep. Will they get the same mean? Should they?
If not, which one is "wrong"?

### Explanation
* A **parameter** is a number describing the population (the true mean birth weight of all 1,500 babies, 2.886 kg).
* A **statistic** is the same kind of number computed from a sample (the mean of the 100 babies we happened to pick).
  We use the statistic as an **estimate** of the parameter.

Different random samples give different estimates. This is **sampling variation** — not a mistake, just chance in who
ends up in the sample. Ten samples of 20 babies:

```python
means = [h["birth_weight_kg"].sample(20, random_state=i).mean() for i in range(10)]
print(np.round(means, 2))      # [2.8  2.82 2.86 2.94 2.78 2.94 2.94 2.94 2.86 2.75]
```

None equals 2.886 exactly, and they spread from 2.75 to 2.94.

If we drew thousands of samples and plotted all their means, we would get the **sampling distribution** of the mean.
Two facts about it (you can check them by simulation):
1. It is centred on the true parameter (if sampling is random) — the estimate is not systematically off.
2. Its spread, called the **standard error** (SE), **shrinks as the sample grows**, roughly as 1 ÷ √n:

> SE of the mean ≈ SD of the data ÷ √n

Quadrupling the sample size halves the standard error. Going from 100 to 400 people helps a lot; from 10,000 to 40,000
helps much less in absolute terms.

**Sampling variation is not bias.** Random samples wobble around the truth. A biased sample (Grade 8: asking only
the front row) is off in one direction, and a bigger biased sample is just more confidently wrong.

### Activity (20 min)
1. **Unplugged:** the teacher puts 100 slips with birth weights (printed from the table) in a bag. Each group draws 20
   slips, computes the mean, returns the slips. Plot every group's mean on a class dot plot.
2. Run the code: 1,000 samples of size 20 and 1,000 of size 80; draw both histograms of the means on one axis
   (`sharex`). What happens to the spread?
3. Compute SD ÷ √n for n = 20 and 80 and compare with the SD of your simulated means.

### Common mistakes
* Thinking the sample mean "should" equal the population mean.
* Confusing the SD of the data (how much babies differ) with the standard error (how much sample means differ).
* Believing large samples fix bias.

**Check (5 min).**
1. Will two samples give the same mean?
2. Bigger sample → ?
3. What causes the difference?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: The bootstrap

**Hook (5 min).** In real life we have **one** sample and no population to draw from again. How could we possibly
know how much our estimate would wobble?

### Explanation
The **bootstrap** (Bradley Efron, 1979) uses the one sample as a stand-in for the population:

1. Take the sample of size *n*.
2. Draw a **resample** of size *n* from it **with replacement** (each value is put back after being drawn, so some appear
   twice or more, others not at all).
3. Compute the statistic (mean, median, proportion…) on the resample.
4. Repeat steps 2–3 thousands of times.
5. The spread of these bootstrap statistics estimates the sampling variation. The **middle 95%** (2.5th to 97.5th
   percentile) is a **95% bootstrap confidence interval** (the "percentile interval").

```python
def bootstrap(values, stat=np.mean, n_boot=5000, seed=0):
    """Return n_boot bootstrap values of stat computed on resamples of values."""
    rng = np.random.default_rng(seed)
    values = np.asarray(values)
    return np.array([stat(rng.choice(values, size=len(values), replace=True)) for _ in range(n_boot)])

sample = h.sample(100, random_state=1)                # our one sample of 100 babies
boot_means = bootstrap(sample["birth_weight_kg"])
low, high = np.percentile(boot_means, [2.5, 97.5])
print(f"sample mean {sample['birth_weight_kg'].mean():.2f} kg, 95% CI {low:.2f} to {high:.2f} kg")
# sample mean 2.91 kg, 95% CI 2.83 to 2.99 kg

plt.hist(boot_means, bins=40)
plt.axvline(low, color="black")
plt.axvline(high, color="black")
plt.xlabel("Bootstrap mean birth weight (kg)")
plt.title("5,000 bootstrap means from one sample of 100")
plt.show()
```

The true mean (2.886) is inside the interval — but we only know that because this is a teaching set-up.

**Why it works (intuition):** if the sample is random and not tiny, it looks roughly like the population, so drawing
from the sample imitates drawing from the population.

**It works for almost any statistic:**

```python
boot_median = bootstrap(sample["birth_weight_kg"], stat=np.median)
boot_prop = bootstrap(sample["institutional_delivery"])     # mean of 0/1 values = proportion
print(np.percentile(boot_median, [2.5, 97.5]).round(2))    # median: about 2.75 to 2.93 kg
print(np.percentile(boot_prop, [2.5, 97.5]).round(2))      # proportion: 0.32 to 0.52
```

The proportion of facility deliveries in the sample is 0.42, with a 95% interval from 0.32 to 0.52 — wide, because 100
is not many people for a proportion.

**What the bootstrap cannot do:** it cannot create information that is not in the sample. It does not fix bias,
very small samples (n < 15–20) or samples that miss whole groups.

### Activity (20 min) — PRIMM
1. **Predict** whether the true mean (2.886) will be inside your interval; run the code.
2. **Investigate:** change `random_state` to draw a different sample of 100. Does the interval move? Does it still
   contain 2.886?
3. **Modify:** compute an interval for the share of babies under 2.5 kg (low birth weight): use
   `(sample["birth_weight_kg"] < 2.5).astype(int)`.
4. **Make:** a bootstrap interval for the **difference** in mean birth weight between facility and home deliveries
   (resample each group separately).

### Common mistakes
* Resampling **without** replacement (you just get the same sample shuffled).
* Resampling a different size from the original sample.
* Too few bootstrap repetitions (use at least 1,000; 5,000 is comfortable).

**Check (5 min).**
1. 'With replacement' means…
2. What do we compute each time?
3. Middle 95% gives…

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Interpreting intervals

**Hook (5 min).** A pre-election poll says: "Party A: 55%, margin of error ± 4 points". What does ± 4 mean? Is Party A
sure to win? Would a poll of 10,000 people make it certain?

### Explanation
**What "95% confidence" means.** The method that produced the interval captures the true parameter in about 95% of
samples. We can check this in our teaching set-up: drawing 200 different samples of 100 and building a bootstrap
interval from each, 189 of the 200 intervals (94.5%) contained the true mean 2.886. For any one interval we don't know
whether it is one of the lucky 95% or the unlucky 5%.

**Width depends on sample size:**

| n | Sample mean (kg) | 95% bootstrap CI (kg) | Width |
|---|---|---|---|
| 25 | 2.89 | 2.71 – 3.07 | 0.35 |
| 100 | 2.96 | 2.88 – 3.04 | 0.15 |
| 400 | 2.90 | 2.86 – 2.95 | 0.08 |

Each fourfold increase in *n* roughly halves the width (the 1 ÷ √n rule). The **margin of error** is half the width
("± 0.04 kg" for n = 400).

**Correct and incorrect interpretations** (for "mean birth weight 2.91 kg, 95% CI 2.83 to 2.99 kg"):

| ✔ Correct | ✘ Incorrect |
|---|---|
| "We are reasonably confident the population mean is between 2.83 and 2.99 kg." | "95% of babies weigh between 2.83 and 2.99 kg." (The interval is about the **mean**, not individual babies — most babies are outside it!) |
| "Values of the population mean below 2.8 kg are not supported by this sample." | "There is a 95% chance the sample mean is in the interval." (The sample mean is always in it.) |
| "With a larger sample the interval would be narrower." | "The interval proves the true mean is 2.91." |
| "The interval reflects random sampling error only." | "A narrow interval means the survey was unbiased." |

**What an interval leaves out:** non-response, biased sampling, measurement error (scales that read 0.1 kg heavy), and
whether the question was the right one. A poll with a tiny margin of error can still be badly wrong if its sample is
not representative. Report the interval **and** how the data were collected.

**The formula shortcut.** For means with reasonable sample sizes, a 95% interval is about estimate ± 2 × SE, with SE ≈
SD ÷ √n. For n = 100: SD ≈ 0.42, SE ≈ 0.042, interval ≈ 2.91 ± 0.08 — close to the bootstrap answer. Grade 12 and
university courses derive such formulas; the bootstrap shows the same idea by simulation.

### Activity (20 min) — PRIMM
1. Compute bootstrap intervals for n = 25, 100 and 400 (use `h.sample(n, random_state=2)`); fill in a table like the one
   above.
2. **Coverage experiment:** draw 100 samples of size 100, build an interval for each, count how many contain 2.886.
   Plot the intervals as horizontal lines (`plt.hlines`) with a vertical line at 2.886.
3. Write two correct and two incorrect interpretations of your n = 100 interval.

### Common mistakes
* Reading a CI as the range of individual values.
* Forgetting that "95%" refers to the method, not to one interval.
* Reporting an estimate with no interval, or an interval with no description of the sampling.

**Check (5 min).**
1. Which is narrower, n=25 or n=400?
2. Does a narrow interval fix a biased sample?
3. Is a 95% interval where 95% of the data lie?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Parameter (population) vs statistic (sample). Random samples vary: **sampling variation**; its size is the
  **standard error**, about SD ÷ √n.
* Bootstrap: resample *n* values with replacement, compute the statistic, repeat thousands of times; the middle 95% is
  a 95% CI. Works for means, medians, proportions, differences.
* 95% confidence = the method captures the truth about 95% of the time.
* Intervals narrow as *n* grows (÷ 2 for ×4 data) but say nothing about bias or individuals.
* Always report the estimate, the interval, and how the data were collected.

## Practice exercises
1. ★ Identify parameter and statistic: "Of 400 randomly chosen voters in Pokhara, 52% support the new bus park."
2. ★ The SD of heights is 8 cm. Estimate the standard error of the mean for n = 16 and n = 64.
3. ★ Why do we resample **with** replacement?
4. ★★ A poll of 1,000 people gives 48% ± 3 points. Write a correct one-sentence interpretation. Can you say the
   candidate is losing?
5. ★★ Bootstrap a 95% CI for the mean `mother_age` from a sample of 50 (`random_state=3`). Then for 200. Compare
   widths.
6. ★★ Bootstrap a 90% interval (5th–95th percentiles) for the same sample. Is it wider or narrower than the 95%
   interval? Why?
7. ★★ Compute bootstrap intervals for the proportion of facility deliveries in each ecological belt from the full table
   treated as a sample. Which belt's interval is widest, and why?
8. ★★★ A survey reports "average monthly income Rs 32,000 (95% CI 30,500–33,500)" from 5,000 households contacted by
   mobile phone. Give two reasons the true average could be outside the interval.
9. ★★★ Explain why the bootstrap fails for n = 5. Try it: what do the bootstrap means look like?
10. ★★★ Using the coverage experiment, compare 95% intervals from samples of n = 10 and n = 100. Do both capture the
    truth about 95% of the time? What does this suggest?

## Exercises with real data
**R1. How sure is the rain? (RD-06 / RD-07).** Take 30 years of July rainfall totals for your town (Open-Meteo daily
data summed by year, or NASA POWER). Bootstrap a 95% CI for the mean July rainfall and for the median. Write an
interpretation that a farmer could use, with a warning about what the interval does not cover (e.g. climate trends).
*Offline fallback:* July values from `climate_monthly_synthetic.csv` (30 values).

**R2. Penguin mass (RD-17).** Bootstrap 95% intervals for the mean body mass of each penguin species. Do the
intervals overlap? What would overlapping or separate intervals suggest about the difference?

**R3. Read a real survey (RD-13).** Find a Nepal survey report (e.g. Nepal Living Standards Survey or a labour force
survey summary from NSO) that reports a margin of error or confidence interval. Write: what was estimated, the
interval, the sample size, and one source of error the interval does not include.

## Unit project: How sure are we?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose a question about the health table (or a
real dataset), take a random sample, estimate a mean or proportion, bootstrap a 95% CI, show the bootstrap histogram,
run a coverage check (synthetic data only), and write correct and incorrect interpretations plus the limits. Full brief
and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* OpenIntro Statistics (free textbook, <https://www.openintro.org/book/os/>), chapters on foundations for inference.
* Seeing Theory, "Frequentist inference" (<https://seeing-theory.brown.edu>).
* David Spiegelhalter, *The Art of Statistics*, chapter 7 ("How sure can we be about what is going on?").
