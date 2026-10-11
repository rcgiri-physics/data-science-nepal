# 2. The foundation ladder: how ideas build from Grade 8 to Grade 12

Teachers in one grade often do not see what came before or what comes next. This chapter is the map. Use it to
connect your lessons to what students already know ("remember the human median in Grade 8?") and to what they will need.

## Strand 1: Statistical thinking

| Idea | Gr 8 | Gr 9 | Gr 10 | Gr 11 | Gr 12 |
|---|---|---|---|---|---|
| Variability | answers differ; statistical questions (U2) | variation between districts | distributions, SD, IQR (U2) | sampling variation (U3) | noise vs signal, overfitting (U4) |
| Centre and spread | mean, median, mode, range (U5) | quartiles, box plots (U6) | mean/SD vs median/IQR; z-scores (U2) | standard error (U3) | error metrics MAE/RMSE (U2) |
| Comparing groups | rates, medians, dot plots (U6) | weighted rates (U7) | box plots by group; within-group context (U2) | permutation tests, effect sizes (U4) | group audits (U5) |
| Sampling and bias | random vs convenience samples (U2) | who is missing in tables | representation in training data (U5) | bootstrap; intervals don't fix bias (U3) | representation and label bias (U5) |
| Relationships | — | scatter plots, *r* (U6) | least squares, residuals, confounding (U3) | multiple regression, "holding fixed" (U5) | classification, odds (U2) |
| Cause and chance | claims vs evidence (U7) | correlation ≠ cause (U6) | confounders, experiments (U3) | p-values, randomisation (U4) | current practice comparisons (U8) |
| Time | line graphs (U4) | — | trend, season, anomalies (U4) | seasonal indices, trend intervals (U6) | time-based splits (U1) |

## Strand 2: Data handling

| Idea | Gr 8 | Gr 9 | Gr 10 | Gr 11 | Gr 12 |
|---|---|---|---|---|---|
| Tidy tables | one row per case (U1, U3) | spreadsheets, types (U1) | DataFrames, dtypes (U1) | memory and types (U1) | feature tables (U6) |
| Cleaning | units, missing as NA (U3) | codes, names, BS/AD, logs (U2) | NaN, imputation, robustness (U1) | joins and NULLs (U2) | leakage (U1, U6) |
| Databases | — | SQL SELECT…JOIN (U3) | — | windows, CTEs, indexes (U1–2) | — |
| Documentation | source questions (U1) | cleaning log | data-quality report (U8) | README, Git, seeds (U8) | model cards, data agreements (U8) |

## Strand 3: Tools

| | Gr 8 | Gr 9 | Gr 10 | Gr 11 | Gr 12 |
|---|---|---|---|---|---|
| Unplugged / paper | everything | SQL cards | k-NN cards | shuffle slips | task cards, role plays |
| Spreadsheet / CODAP | optional | core (U1–2, U7) | — | — | — |
| SQL | — | core (U3) | — | advanced (U2) | — |
| Python | — | first steps, pandas (U4–6) | pandas, matplotlib, Streamlit | numpy, simulation, Git | scikit-learn |

## Strand 4: Modelling

Grade 8 "a summary is a tiny model of a list" → Grade 9 rates as fair models of size → Grade 10 line of best fit and
k-NN against a baseline → Grade 11 regression with uncertainty, seasonal models → Grade 12 the ML workflow, metrics,
overfitting, fairness and features.

**The constant message:** compare with a baseline, test on unseen data, prefer simple and explainable, judge by the
decision the model supports.

## Strand 5: Communication and ethics

| Gr 8 | Gr 9 | Gr 10 | Gr 11 | Gr 12 |
|---|---|---|---|---|
| CER posters; consent; privacy; who is missing; data charter | plan cards; SQL report; honest charts | AI literacy; dashboards; health limits cited | licences; maps that don't mislead; reproducibility | memos, plain-language uncertainty, fairness audits, client data agreements |

## The minimum foundation

If time is short, these are the ideas **every** student should leave school with, and where they are taught:

1. A good question is about a group and expects variation (G8 U2).
2. How data were collected decides what they can tell us; ask who is missing (G8 U1–3, U8).
3. Look at the whole distribution, not just an average (G8 U4–5; G10 U2).
4. Compare with rates, not counts (G8 U6; G9 U7).
5. Patterns can be chance: bigger samples help, bias does not shrink (G8 U2; G11 U3–4).
6. Correlation is not causation; look for confounders (G9 U6; G10 U3).
7. Clean data carefully and record what you did (G9 U2).
8. A model must beat a baseline on unseen data, and its mistakes fall on people (G10 U5; G12 U3, U5).
9. Say what you found, how sure you are, and what you cannot say (G8 U7; G12 U7).
10. Respect consent, privacy and fairness (G8 U3, U8; G10 U6; G12 U5, U8).
