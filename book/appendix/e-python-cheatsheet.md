# Appendix E — Python, pandas, matplotlib and scikit-learn cheat sheet

## Python basics
```text
x = 14                      # variable (int); 8.2 float; "Sita" str; True bool
minutes = [53, 27, 40]      # list; minutes[0] = 53; minutes[-1] = 40; len(minutes) = 3
minutes.append(19)          # add to list
for m in minutes:           # loop (indent the body 4 spaces)
    if m > 30:              # condition: == != < > <= >=, and/or/not
        print(m)
def my_mean(values):        # function
    return sum(values) / len(values)
assert my_mean([2, 4, 6]) == 4   # test
```

## pandas: load and inspect
```text
import pandas as pd
df = pd.read_csv("file.csv", parse_dates=["date"], na_values=[-999], usecols=[...])
df.shape  df.columns  df.dtypes  df.head()  df.tail()  df.sample(5)
df.isna().sum()  df.describe()  df["col"].value_counts()  df["col"].unique()
```

## Select, filter, sort, new columns
```text
df["col"]                                 # one column (Series)
df[["a", "b"]]                            # several columns
df[df["belt"] == "Hill"]                  # filter
df[(df["belt"] == "Hill") & (df["lit"] > 80)]   # & | ~ with brackets
df[df["province"].isin([1, 3])]
df.query("belt == 'Terai' and province == 2")
df.sort_values("population", ascending=False).head(5)
df["rate"] = 1000 * df["abroad"] / df["population"]
df["flag"] = (df["visits"] >= 4).astype(int)
df["band"] = pd.cut(df["age"], [0, 19, 34, 99])
df = df.rename(columns={"old": "new"})
```

## Group, merge, reshape
```text
df.groupby("belt").size()
df.groupby("belt")["lit"].mean()
df.groupby("belt").agg(n=("district", "count"), pop=("population", "sum"))
g = df.groupby("belt")[["part", "whole"]].sum(); g["rate"] = g["part"] / g["whole"]   # weighted rate
df.groupby("month")["pm25"].transform("median")      # group value on every row
m = df.merge(other, on="district_id", how="left")    # join
long = wide.melt(id_vars=["YEAR"], var_name="month", value_name="value")   # wide → long
pd.get_dummies(df["belt"], drop_first=True)          # one-hot
```

## Missing values, dates, time series
```text
df["x"] = df["x"].replace(-999, float("nan"))
df.dropna(subset=["x"])   df["x"].fillna(0)   df["x"].interpolate()   df["x"].ffill()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df["date"].dt.year / .dt.month / .dt.day_name()
s = df.set_index("date")["pm25"]
s.resample("MS").mean()   s.rolling(7, min_periods=4).mean()   s.shift(1)   s.autocorr(1)
```

## Statistics and simulation (numpy)
```text
import numpy as np
rng = np.random.default_rng(2026)                     # seeded generator
rng.choice(values, size=len(values), replace=True)    # bootstrap resample
rng.shuffle(pooled)                                   # permutation
np.percentile(boot, [2.5, 97.5])                      # 95% interval
np.polyfit(x, y, 1)                                   # slope, intercept (slope first!)
df["a"].corr(df["b"])                                 # r
df["x"].quantile([0.25, 0.75])                        # Q1, Q3
```

## matplotlib
```text
import matplotlib.pyplot as plt
plt.bar(categories, values)   plt.barh(...)   plt.hist(x, bins=10)   plt.boxplot(groups)
plt.scatter(x, y, s=8, alpha=0.5)   plt.plot(x, y, label="...")
plt.title("Action title (synthetic data)")  plt.xlabel("units")  plt.ylabel("units")  plt.legend()
fig, axes = plt.subplots(1, 3, figsize=(12, 3))  # axes[0].set_title(...)
plt.axhline(40)  plt.ylim(0, 100)  plt.tight_layout()  plt.show()
```

## scikit-learn
```text
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, mean_absolute_error, precision_recall_curve)

X_tmp, X_test, y_tmp, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression()).fit(X_train, y_train)
model.score(X_val, y_val)                      # accuracy (classifier) / R² (regressor)
p = model.predict_proba(X_val)[:, 1]           # probabilities
pred = (p >= 0.5).astype(int)                  # threshold is a decision
tn, fp, fn, tp = confusion_matrix(y_val, pred).ravel()
cross_val_score(model, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=0))
```

## Workflow reminders
Seed randomness · split before preprocessing · pipeline everything · baseline first · choose on validation · test once
· audit by group · restart and run all before sharing.
