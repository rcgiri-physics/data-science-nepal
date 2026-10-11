# The data-science cycle in one page

Every investigation in this book — from a Grade 8 class survey to a Grade 12 client capstone — follows the same five
steps, called **PPDAC**. The steps are the same; what you do inside each step grows every year.

```
        ┌────────────┐
        │  PROBLEM   │  What do we want to know, and why? Who will use the answer?
        └─────┬──────┘
              ▼
        ┌────────────┐
        │    PLAN    │  What data, from whom, how? What could go wrong? What will we compute?
        └─────┬──────┘
              ▼
        ┌────────────┐
        │    DATA    │  Collect or download; record source and licence; clean and log every step.
        └─────┬──────┘
              ▼
        ┌────────────┐
        │  ANALYSIS  │  Summarise, graph, compare, model — and check how sure we can be.
        └─────┬──────┘
              ▼
        ┌────────────┐
        │ CONCLUSION │  Claim, evidence, reasoning, limits. Communicate. New questions?
        └─────┬──────┘
              └──────────► back to PROBLEM (every good answer raises a new question)
```

## How each step grows from Grade 8 to Grade 12

| Step | Grade 8 | Grade 9 | Grade 10 | Grade 11 | Grade 12 |
|---|---|---|---|---|---|
| **Problem** | statistical vs non-statistical questions | questions about districts and rates | questions about time and relationships | questions about uncertainty and change | a client's decision and success measures |
| **Plan** | survey design, fair samples, consent | plan card, choice of rate | cleaning plan, limit values | pre-registration, seeds, Git | task card, data agreement |
| **Data** | tallies and tidy tables | spreadsheets, cleaning logs, SQL | pandas, dates, missing values | big data, joins, maps, licences | features, encoding, leakage checks |
| **Analysis** | graphs, mean/median, rates | pivots, SQL, pandas, charts | distributions, best-fit lines, models | bootstrap, tests, regression, trends | ML workflow, metrics, audits |
| **Conclusion** | claim–evidence–reasoning poster | poster + SQL report | report or dashboard | reproducible notebook | memo, model card, handover |

## Five questions to ask at every step

1. **Who** collected these data, **why**, and **how**?
2. **Who or what is missing?**
3. Is this difference or pattern **bigger than chance** would produce?
4. Could something else **explain** it (a confounder)?
5. What **can't** we say from this — and who could be **harmed** if we get it wrong?

These five questions appear, in growing depth, in every grade. If you remember nothing else from this book, remember
them.
