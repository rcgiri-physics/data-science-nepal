# 4. Anatomy of a good data-science lesson

Every lesson in this book follows the same five blocks (`docs/pedagogy/lesson-anatomy.md`). This chapter explains why,
and how to run each block well.

| Block | Time | Purpose |
|---|---|---|
| **Hook** | 5 min | curiosity and a prediction |
| **Concept** | ≤ 5–10 min | one idea, explained clearly with an example |
| **Activity** | 20 min | students *do* data work |
| **Check** | 5 min | retrieval: three short questions |
| **Reflect** | 2 min | "What surprised me? Who is missing from this data?" |

## Hook: start with a question and a prediction

A good hook is **local** ("Is Biratnagar hotter than Jumla — by how much?"), **concrete** (a real number, a photo of a
notice board, a news headline) and asks students to **predict** before they know. Predictions matter: when a student has
committed to a guess, they care about the answer, and a wrong guess is a powerful learning moment ("I thought most of us
walked 10 minutes — the median is 29.5!").

Techniques:
* **Show of fingers** (1–5) or mini-whiteboards for predictions, so every student commits, not only the confident ones.
* **Write the class predictions on the board** and return to them at the end.

## Concept: one idea, briefly

The *Explanation* sections in this book are longer than you need to say aloud: they are written for students to read.
In class, pick the **one** core idea and one worked example. Talk for at most 5–10 minutes. Then let students work.

* Use the board for one clear example (a table of five rows is enough).
* Ask "why?" questions: "Why did the mean go up so much when we added the rich family?"
* Use the **Words to know** with their Nepali equivalents; let students explain terms in their own languages.

## Activity: students do the data work

* **Groups of three with roles** — *data steward* (keeps the table clean and the log), *analyst/driver* (computes or
  types), *storyteller* (writes the sentence and presents). Rotate roles each lesson so everyone does everything.
* **Unplugged first.** Shuffle slips before running a permutation test; sort cards on a grid before k-NN; be the
  "database" holding up cards before writing SQL. Physical activities make abstract ideas concrete and work without
  power.
* **PRIMM for code** (chapter 6): Predict → Run → Investigate → Modify → Make.
* **Circulate and listen.** Ask groups to explain what they are doing; misconceptions show up in explanations, not in
  answers.

## Check: three quick questions

Every lesson has three Check questions, with answers in the teacher guide. Use them as **retrieval practice**, not as a
test:
* students answer **from memory**, on paper or mini-whiteboards;
* one question recalls a **previous** lesson (spacing);
* go over answers immediately; it takes 5 minutes.

Retrieval practice is one of the most robust findings in learning research: remembering something makes it easier to
remember later.

## Reflect: what surprised me? who is missing?

Two minutes, every lesson, the same two questions. Over a year they build two habits: noticing (surprise means a
prediction was wrong — learning happened) and asking about the edges of data. Collect a few answers in a class
"surprise wall" or "missing people list".

## Questioning in data lessons

Good questions to keep asking:
* "How do you know?" / "What in the data shows that?"
* "Compared with what?"
* "Could that happen by chance?"
* "What else could explain it?"
* "Who collected this, and why?"
* "Who is not in this table?"
* "What would change your mind?"

## Managing discussions about sensitive data

Data about caste, ethnicity, religion, disability, income or health can hurt. Guidelines:
* Use **synthetic** data for practice; real sensitive data only in aggregate.
* Describe groups; **never rank people**.
* Agree ground rules (Grade 8 Unit 8's class data charter).
* Allow students to opt out of a dataset that touches their life (for example, the 2015 earthquake), and always offer an
  alternative.
