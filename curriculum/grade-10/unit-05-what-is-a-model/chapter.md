# Grade 10 · Unit 5: What is a model? (and a first look at machine learning)

> Track: A then B · Tools: paper cards, Python, numpy · Lessons: 3
> Datasets: `health-synthetic`

**Big idea.** A model is a simplified rule that predicts. We build one by finding patterns in examples and test it on examples it has not seen.

**What you will be able to do**

* I can explain what a model, training data and test data are.
* I can predict with k-nearest neighbours by hand.
* I can compare a model with a simple baseline.

**Words to know:** model, training data, test data, prediction, baseline, accuracy, k-NN (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/knn_intro.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Unplugged: models from cards

**Hook (5 min).** I show you 20 cards of past cases and a new card. How do you guess its label?

**Concept (≤ 5 min).** A model turns examples into a rule for new cases. We *train* on past examples and *test* on new ones we kept hidden.

**Activity (20 min).** Sort 30 training cards on a grid; classify 8 test cards with the 'nearest 3 neighbours vote' rule; count correct.

**Check (5 min).**
1. What is training data?
2. Why keep test data hidden?
3. Which cards are 'nearest'?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Code: k-NN and a baseline

**Hook (5 min).** Is 70% accuracy good?

**Concept (≤ 5 min).** Compare to a baseline (always guess the majority). A model is only useful if it beats a sensible baseline on test data.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Run the notebook: baseline accuracy, then k-NN accuracy; try k=1,5,15,25.

**Check (5 min).**
1. What is a baseline?
2. Why test on unseen data?
3. k = 1 problem?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Limits and misuse

**Hook (5 min).** A clinic uses the model to decide who gets a follow-up visit. What could go wrong?

**Concept (≤ 5 min).** Models learn patterns in the past, including unfairness. Check who is under-represented, what is predicted, who decides, and what happens when it is wrong.

**Activity (20 min).** Discuss three scenarios using the five questions card; write when you would *not* use the model.

**Check (5 min).**
1. Can a model be unfair?
2. Name a high-stakes use needing caution.
3. Who should decide?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Model vs baseline

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
