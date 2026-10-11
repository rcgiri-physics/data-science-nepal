# Grade 12 · Unit 4: Overfitting: when a model memorises

> Track: B (code) · Tools: Python, numpy · Lessons: 3
> Datasets: none

**Big idea.** A model that memorises its training data fails on new data. Complexity must be matched to how much data and noise we have.

**What you will be able to do**

* I can recognise underfitting and overfitting from training and test errors.
* I can choose model complexity with a validation set or k-fold cross-validation.
* I can argue when a simpler, explainable model is the better choice.

**Words to know:** underfitting, overfitting, model complexity, degree (of a polynomial), RMSE, generalisation, bias–variance trade-off, cross-validation, fold, regularisation. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/overfitting.ipynb` (generates its own synthetic data; runs offline).

### Before you start
Unit 1 (train/validation/test), Grade 10 Unit 3 (least-squares lines, residuals). We use **synthetic** data with a
known truth so we can see exactly what goes wrong. Imagine a farmer's field trials: rice yield (quintals per hectare)
for different amounts of fertiliser (bags per hectare). Yield rises with fertiliser, then falls when there is too much.
The true curve is yield = 20 + 3x − 0.4x², plus random noise (weather, soil) with SD 2.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(4)

def make_trials(n):
    """n synthetic field trials: fertiliser (bags/ha) and yield (quintals/ha)."""
    x = rng.uniform(0, 10, n)
    y = 20 + 3 * x - 0.4 * x ** 2 + rng.normal(0, 2, n)
    return x, y

x_train, y_train = make_trials(20)      # 20 trials to learn from
x_val, y_val = make_trials(20)          # 20 trials to choose complexity
x_test, y_test = make_trials(200)       # 200 new trials: the "future"

def rmse(pred, actual):
    return np.sqrt(np.mean((pred - actual) ** 2))
```

**RMSE** (root mean squared error, Unit 2) measures the typical miss in quintals per hectare. Because the noise has SD 2,
**no model can do much better than about 2** on new data.

---

## Lesson 1: Underfitting and overfitting

**Hook (5 min).** A student memorises the answers to last year's 50 exam questions word for word and scores 100% in
practice. This year's exam has different questions. What happens? What should the student have learned instead?

### Explanation
A **polynomial** of degree *d* can bend *d* − 1 times: degree 1 is a straight line, degree 2 a parabola, degree 12 a very
wiggly curve. Higher degree = more **complexity** (more parameters to fit).

```python
for degree in (1, 2, 3, 5, 8, 12):
    coef = np.polyfit(x_train, y_train, degree)
    print(f"degree {degree:2d}: train RMSE {rmse(np.polyval(coef, x_train), y_train):6.2f}"
          f"   test RMSE {rmse(np.polyval(coef, x_test), y_test):8.2f}")
```

| Degree | Train RMSE | Test RMSE | Diagnosis |
|---|---|---|---|
| 1 | 3.29 | 3.83 | **underfit**: a straight line cannot bend down |
| 2 | 1.82 | 2.12 | about right (the true shape) |
| 3 | 1.77 | 2.21 | fine |
| 5 | 1.73 | 2.22 | slightly worse on new data |
| 8 | 1.58 | 8.66 | **overfit** |
| 12 | 0.91 | 2,186 | badly overfit: wild swings between and beyond points |

(`np.polyfit` may warn that high degrees are "poorly conditioned" — another sign that 20 points cannot support 13
coefficients.)

The pattern is general:
* **Training error always falls** as complexity grows: a more flexible curve can pass closer to every training point —
  including through the **noise**, which is random and will not repeat.
* **Test error falls, then rises.** Too simple → misses the real pattern (**underfitting**, also called high bias).
  Too complex → learns the noise (**overfitting**, high variance: the curve would change a lot with a different 20
  trials).
* The best model sits in between, near where test error is lowest — and it is not perfect: test error ≈ 2, the size of
  the noise.

```python
xs = np.linspace(0, 10, 200)
plt.scatter(x_train, y_train, color="black", label="training trials")
for degree in (1, 2, 12):
    coef = np.polyfit(x_train, y_train, degree)
    plt.plot(xs, np.polyval(coef, xs), label=f"degree {degree}")
plt.ylim(0, 40)
plt.xlabel("Fertiliser (bags/ha)")
plt.ylabel("Yield (quintals/ha)")
plt.legend()
plt.show()
```

### Activity (20 min) — PRIMM
1. **Predict** which degree has the lowest training error and which the lowest test error; run the table.
2. Draw the three curves. Describe each in one sentence a farmer would understand.
3. **Investigate:** regenerate the training data with a different seed. How much do the degree-2 and degree-12 curves
   change?
4. **Make:** plot train and test RMSE against degree (1 to 10) on one chart: the classic U-shaped test curve.

### Common mistakes
* Judging a model by training error.
* Thinking overfitting only happens with polynomials (trees, k-NN with k = 1 and neural networks overfit too).
* Expecting test error to reach zero.

**Check (5 min).**
1. Training error with more complexity…
2. Test error with too much complexity…
3. What is noise?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Choosing complexity with validation

**Hook (5 min).** In real life we don't have 200 test trials from the future. How do we choose the degree without
peeking at the test set?

### Explanation
**Use validation data** (Unit 1): fit on training, compare on validation, choose, then test once.

```python
val_errors = {}
for degree in range(1, 9):
    coef = np.polyfit(x_train, y_train, degree)
    val_errors[degree] = rmse(np.polyval(coef, x_val), y_val)
best = min(val_errors, key=val_errors.get)
print({d: round(e, 2) for d, e in val_errors.items()})
print("chosen degree:", best)
```

Here the validation set chooses **degree 6** (RMSE 2.25) just ahead of degree 2 (2.32) — even though we know the truth
is a parabola. With only 20 validation trials, the validation errors are themselves noisy, and a different validation
set might choose a different degree. **k-fold cross-validation** uses the data more efficiently:

1. Split the available data (here train + validation, 40 trials) into *k* equal **folds** (e.g. 5 folds of 8).
2. For each fold: fit on the other 4 folds, measure error on this fold.
3. Average the *k* errors (and look at their spread).

Every trial is used for validation exactly once and for training *k* − 1 times.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

X_all = np.concatenate([x_train, x_val]).reshape(-1, 1)   # scikit-learn wants a 2-D table of features
y_all = np.concatenate([y_train, y_val])
folds = KFold(n_splits=5, shuffle=True, random_state=0)
for degree in (1, 2, 3, 5, 8):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    scores = -cross_val_score(model, X_all, y_all, cv=folds, scoring="neg_root_mean_squared_error")
    print(f"degree {degree}: CV RMSE {scores.mean():.2f} ± {scores.std():.2f}")
```

Result: degree 1: 3.31, degree **2: 2.06**, degree 3: 2.12, degree 5: 2.24, degree 8: 2.29. Degree 2 wins, and it is the
true shape. Refit degree 2 on all 40 trials and test once: test RMSE ≈ **2.12**, about the noise level. The fitted curve
puts the best fertiliser amount at about 3.5 bags/ha (true value 3.75).

(scikit-learn's scorers are "higher is better", so errors come back negative; the minus sign flips them.)

### Activity (20 min) — PRIMM
1. **Predict** which degree validation will choose; run the validation loop.
2. Run 5-fold cross-validation. Do the two methods agree?
3. Refit the chosen degree on all 40 trials, test once, and find the best fertiliser amount (where the curve peaks:
   −b ÷ 2a for ax² + bx + c).
4. **Make:** repeat the whole experiment with 200 training trials instead of 20. What happens to the degree-8 test
   error? (More data lets complex models behave.)

### Common mistakes
* Choosing complexity on the test set.
* Ignoring the spread of cross-validation scores (differences smaller than the spread are not meaningful).
* Doing preprocessing outside the pipeline (leakage across folds).

**Check (5 min).**
1. Which data choose complexity?
2. Why not test data?
3. What is cross-validation?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Simple can win

**Hook (5 min).** Your degree-3 model is 0.05 quintals/ha "better" in cross-validation than degree 2 on some seed. A
government agriculture office wants advice for farmers. Which model do you recommend, and why?

### Explanation
**Prefer the simplest model that performs about as well as the best.** A common rule of thumb ("one standard error
rule"): pick the simplest model whose CV error is within one standard deviation of the best. Reasons:

* **Generalisation:** with limited data, simple models are less likely to have learned noise.
* **Stability:** they change less when new data arrive.
* **Explainability:** "yield rises with fertiliser up to about 3.5 bags/ha and falls after that" can be told to farmers
  and checked against agronomy; a degree-8 curve cannot.
* **Accountability:** public offices must justify decisions; simple models can be audited (Unit 5).
* **Robustness outside the data:** complex curves behave wildly beyond the training range (try predicting 11 bags/ha).

**Other ways to control overfitting**
* **More data** (often the best fix).
* **Regularisation:** penalise large coefficients (ridge, lasso regression), so the model prefers smoother fits.
* **Limits on complexity:** maximum tree depth, minimum leaf size, larger *k* in k-NN.
* **Fewer, better features** (Unit 6).
* **Early stopping** in iterative methods such as neural networks.

**Overfitting in the wild.** A model that predicts exam results from 200 variables about 300 students will "find"
patterns that are noise. A stock-market strategy tested on hundreds of rules will find one that worked by luck in the
past. The more you search, the more you must validate on new data.

### Activity (20 min)
1. Compare degree 2 and degree 8 fitted on the 40 trials: plot them between 0 and 12 bags/ha. Which would you trust
   for 11 bags/ha?
2. Apply the one-standard-error rule to your CV results.
3. Write a 150-word recommendation to the agriculture office: the model, the advice, how sure you are, what data would
   improve it.

### Common mistakes
* Treating a tiny CV improvement as decisive.
* Assuming complex = modern = better.
* Extrapolating beyond the data range.

**Check (5 min).**
1. When do simple models shine?
2. Why prefer explainable models in public service?
3. Is overfitting only a polynomial problem?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Training error falls with complexity; test error falls then rises (U-shape). Underfit = too simple; overfit = learns
  noise.
* No model beats the noise level on new data.
* Choose complexity with a validation set or k-fold cross-validation (look at the spread); test once at the end.
* Prefer the simplest model close to the best (one-standard-error rule); simple models generalise, explain and audit
  better.
* Other remedies: more data, regularisation, complexity limits, fewer features, early stopping.

## Practice exercises
1. ★ Train RMSE 0.5, test RMSE 6.0. Underfit or overfit? What about train 4.0, test 4.1 when the noise SD is 1?
2. ★ How many times is each data point used for validation in 5-fold CV? For training?
3. ★ Name two ways to reduce overfitting besides choosing a lower degree.
4. ★★ For k-NN classification on the health table (Unit 1), plot training and validation accuracy for k = 1, 3, 5, 11,
   25, 51, 101. Where is overfitting? Underfitting?
5. ★★ For decision trees on the health table, compare `max_depth` = 1, 2, 3, 5, 10, None with 5-fold CV accuracy.
   Which depth do you choose by the one-standard-error rule?
6. ★★ Repeat Lesson 1 with noise SD 0.5 instead of 2. Which degrees are now acceptable? Why?
7. ★★ Use the degree-2 model to predict yield at 11 bags/ha and the degree-8 model too. Comment.
8. ★★★ Explain the bias–variance trade-off using the two curves from different random training sets.
9. ★★★ A student says: "I tried 1,000 feature combinations and kept the best by test accuracy: 71%!" Explain why 71% is
   optimistic and what they should have done.
10. ★★★ Use ridge regression (`sklearn.linear_model.Ridge(alpha=...)`) with degree-8 polynomial features on the 40
    trials. How does CV RMSE change as `alpha` grows?

## Exercises with real data
**R1. Seasonal temperature curve (RD-06 / RD-07).** Fit polynomials of degree 1–10 to monthly mean temperature against
month number (1–12) for one year of your town's data; validate on another year. Which degree generalises? Why might a
sine-and-cosine (seasonal) model be better than polynomials?
*Offline fallback:* two years of `climate_monthly_synthetic.csv` (train on one, validate on the other).

**R2. Life expectancy vs income (RD-03).** Fit degrees 1–6 for life expectancy against log GDP per capita, choose with
5-fold CV, and check how the curve behaves for the poorest and richest countries.

**R3. Penguins (RD-17).** Compare decision-tree depths for species classification with 5-fold CV; plot train vs CV
accuracy against depth.

## Unit project: Find the sweet spot
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. For one dataset, show train vs validation/CV
error across complexity, choose a model with the one-standard-error rule, test once, and write a recommendation that
explains why a simpler model was (or was not) preferred. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* *An Introduction to Statistical Learning* (free), chapter 2 (bias–variance) and chapter 5 (cross-validation).
* StatQuest videos "Bias and Variance" and "Cross Validation".
* Google Machine Learning Crash Course: "Generalization" and "Regularization".
