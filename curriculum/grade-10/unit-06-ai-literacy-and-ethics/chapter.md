# Grade 10 · Unit 6: AI literacy and ethics

> Track: A (no-code) · Tools: discussion, case cards · Lessons: 3
> Datasets: none

**Big idea.** AI systems are built from data and choices. Understanding where they fail helps us use them wisely and fairly.

**What you will be able to do**

* I can explain in simple terms how machine-learning and generative AI systems learn from data.
* I can recognise hallucination and bias, and check AI output against sources.
* I can use AI tools responsibly: as a tutor, with disclosure, protecting privacy.

**Words to know:** artificial intelligence (कृत्रिम बुद्धिमत्ता), machine learning, training data, generative AI, large language model, token, hallucination, bias, deepfake, disclosure. Full list: `curriculum/framework/glossary.md`.

### Before you start
Unit 5 built a tiny model: features in, prediction out, trained on examples, tested on new ones. Modern AI tools —
chatbots, image generators, translation apps, phone keyboards — are the same idea at enormous scale. No computer is
needed for this unit.

---

## Lesson 1: How AI learns

**Hook (5 min).** Type "I am going to" on a phone keyboard. It suggests the next word. How does it guess? Would its
guesses be different for a student in Biratnagar and a student in Jumla?

### Explanation
**Artificial intelligence (AI)** is a broad name for computer systems that do tasks we associate with human
intelligence: recognising faces, translating, answering questions. Most modern AI is **machine learning (ML)**: instead
of a programmer writing every rule, the system **learns patterns from examples** (training data), as your k-NN model
did in Unit 5.

| System | Learns from | Predicts |
|---|---|---|
| Spam filter | emails labelled spam / not spam | is this new email spam? |
| Phone keyboard | huge amounts of typed text | the next word |
| Photo face unlock | many photos of your face | is this you? |
| Translation app | millions of sentence pairs in two languages | the translation |
| Chatbot (large language model) | very large collections of text from books, websites, code | the next piece of text |

**How a chatbot writes.** A **large language model** (LLM) breaks text into small pieces called **tokens** (words or
parts of words). During training it reads billions of sentences and learns, for any text so far, how likely each
possible next token is. When you ask a question it repeatedly picks a likely next token, adds it, and continues. Extra
training with human feedback teaches it to follow instructions and be helpful. The result can be remarkably fluent and
often correct — but it is **predicting likely text**, not looking facts up in a reliable database, unless the tool is
specifically connected to search or documents.

**What follows from "learning from examples":**
* **Quality in, quality out.** Biased or wrong examples produce biased or wrong outputs.
* **Coverage matters.** Languages, places and people that are rare in the training data are handled worse. Nepali,
  and even more Maithili, Tamang, Tharu or Newar (Nepal Bhasa), are "low-resource" languages compared with English,
  so AI tools are often weaker in them.
* **It does not understand like a person.** It has no experience of the world; it can be confidently wrong.
* **It reflects a time.** Training data stop at a date; the model may not know recent events.

### Activity (20 min)
1. **Predict the next word, unplugged.** The teacher reads a short class story one word at a time and stops. Everyone
   writes the next word. Tally the guesses: the most common one is the "model's prediction".
2. Repeat after reading the class five more stories of the same style. Do guesses become more alike? That is
   "training".
3. Discuss: what if all five stories were about boys? About Kathmandu? How would predictions change for a story
   about a girl in Dolpa?

### Common mistakes
* "AI knows the answer" — it generates likely text.
* "AI is a magic brain" — it is statistics on examples, built by people who made many choices.
* "AI is useless" — it is very useful for many tasks when checked.

**Check (5 min).**
1. What does an AI learn from?
2. Does it understand like a person?
3. What happens with bad data?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Hallucination and bias

**Hook (5 min).** A student asks a chatbot for the population of their district and a source. It gives a precise
number and cites a report — but the report doesn't exist. Why would a system do that?

### Explanation
**Hallucination** is when an AI produces confident output that is false or invented: a wrong number, a fake quotation,
a non-existent book or legal case, a made-up reference. It happens because the model generates *plausible* text; a
realistic-looking citation is plausible even when no such document exists. Hallucinations are more likely for:
* specific numbers, dates, names and references;
* local or rare topics (a small Nepali district, a recent event);
* questions phrased so the "expected" answer is a confident one.

**How to check AI output (the verification habit)**
1. **Go to the primary source:** NSO for census numbers, DHM for weather, the dataset card for our data.
2. **Check that references exist** and say what is claimed.
3. **Recompute** numbers yourself where possible.
4. **Ask for uncertainty:** "How sure are you? What would you need to check?"
5. **Be extra careful** with health, legal and money advice.

**Bias** in AI means systematic differences in how well, or how fairly, a system works for different groups:
* **Data bias:** a face-recognition system trained mostly on light-skinned faces makes more errors on darker faces —
  documented in a well-known 2018 study of commercial systems (Buolamwini and Gebru, "Gender Shades").
* **Language bias:** translations that turn a neutral sentence into a gendered stereotype (e.g. "the doctor … he",
  "the nurse … she").
* **Representation bias:** image generators asked for "a doctor" or "a CEO" mostly showing one gender or ethnicity.
* **Historical bias:** a hiring model trained on past (unfair) decisions repeating them.

**Deepfakes** are AI-generated images, audio or video that imitate real people. They can spread misinformation in
elections or be used to harass. Check: who posted it first? Do trusted news sources report it? Are there visual or
audio glitches? When unsure, do not share.

### Activity (20 min)
1. Your teacher gives five "facts" about Nepal produced by an AI tool (some true, some invented: e.g. a district's
   population, a river's length, a law's year, a quotation, a statistic with a source).
2. In pairs, verify each using an official site, a dataset card, a textbook or an atlas. Mark ✔ true, ✘ false,
   ? cannot verify. Write where you checked.
3. Discuss: which kinds of claims were wrong most often? What would have happened if you had copied them into a
   report?

### Common mistakes
* Trusting a reference because it "looks real".
* Thinking bias means the system "wants" to be unfair — it reflects data and design choices.
* Sharing a surprising video before checking.

**Check (5 min).**
1. What is hallucination?
2. How do you check?
3. Give a source of bias.

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Responsible use

**Hook (5 min).** Should a student use AI for homework? Give one way it could help you learn and one way it could stop
you learning.

### Explanation
AI tools can be excellent **tutors**: explaining a concept in different ways, giving practice questions, finding a
bug in your code, suggesting how to structure an essay. They can also **replace your thinking**, which defeats the
purpose of school: the goal of homework is not the answer, it is the skill you build while finding it.

This curriculum's **AI-use policy** (`docs/pedagogy/ai-use-policy.md`) has three rules:
1. **Explain, don't answer.** Ask the tool to explain, give hints or check your work, not to do the work for you.
   "Why is my GROUP BY giving an error?" is good; "Write my project conclusion" is not.
2. **Disclose.** Write one line in every piece of work: what tool you used and for what ("Used a chatbot to explain
   rolling means; all code and text are mine").
3. **Be ready for an oral check.** You must be able to explain everything you hand in.

**Privacy.** Anything typed into an online AI tool may be stored and may be used to improve the system. **Never paste**
personal data about real people (names with marks, health information, phone numbers, citizenship numbers), passwords
or private documents. Use synthetic or anonymised data, as this book does.

**Other things responsible users consider**
* **Copyright and credit:** credit sources the AI drew on when you can identify them; don't present AI-generated
  images or text as your own creative work where originality is required.
* **High-stakes decisions:** health, legal, financial, exam or hiring decisions need accountable humans and real
  experts; AI can support, not decide.
* **Environment:** training and running large models uses a lot of electricity and water for data centres; use them
  when they help, not for everything.
* **Jobs and skills:** tasks change; the people who benefit most are those who understand both the subject and the
  tool's limits.

### Activity (20 min)
1. In groups, sort 10 example uses into "helps learning", "replaces learning" and "unsafe" (e.g. "ask for practice
   questions on percent change"; "paste the whole assignment and submit the answer"; "upload the class marks list to
   get a summary"; "ask why code throws a KeyError"; "ask for three ideas for a project question").
2. Write your class **AI charter**: 6 rules, each with a reason. Start from the AI-use policy and add rules your class
   cares about.
3. Practise a disclosure line for your Unit 3 project.

### Common mistakes
* Hiding AI use (it is usually detectable, and dishonest).
* Pasting private data "just this once".
* Using AI for everything, including what you need to practise.

**Check (5 min).**
1. What does 'explain, don't answer' mean?
2. What must you never paste into a tool?
3. Why an oral check?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Most AI is machine learning: patterns learned from examples. LLMs predict the next token, very fluently.
* Training data shape everything: quality, coverage (low-resource languages), bias, and a cut-off date.
* Hallucinations are confident fabrications; verify with primary sources, check references, recompute numbers.
* Bias = systematic differences in performance or fairness between groups; deepfakes imitate real people.
* Use AI as a tutor: explain-don't-answer, disclose, be ready for an oral check; protect privacy; humans stay
  accountable.

## Practice exercises
1. ★ Give two everyday examples of machine learning in Nepal (apps, phones, banks, social media).
2. ★ In one sentence each, explain *training data*, *token* and *hallucination*.
3. ★ Write a disclosure line for an essay where you used AI to check grammar only.
4. ★★ Why might a translation app work better for English–Nepali than for Tamang–Nepali?
5. ★★ A chatbot says "Nepal has 78 districts" (it has 77 since 2015). Explain how this kind of error could arise from
   training data.
6. ★★ Rewrite each request so it follows "explain, don't answer": (a) "Solve question 5"; (b) "Write a poem for my
   Nepali homework"; (c) "Give me the code for my project".
7. ★★ List three checks you would do before sharing a shocking video of a politician.
8. ★★★ A school wants to use an AI tool to mark essays. List two benefits and three risks, and propose a fair way to
   use it.
9. ★★★ Explain why an AI image generator might draw "a farmer in Nepal" in a stereotyped way. Who could be harmed?
10. ★★★ Your friend says "AI will do all data analysis, so we don't need to learn statistics." Write a reply using what
    you learned in Units 2–5.

## Exercises with real data
**R1. Fact-check an AI (RD-13 / RD-01).** Ask an AI tool (with your teacher's supervision, no personal data) five
factual questions about Nepal: the 2021 census population, your province's population, life expectancy, the share of
remittances in GDP, the length of the Koshi river. Verify every answer against an official source (NSO census portal,
World Bank, a government or ICIMOD page). Score the tool and describe the errors.
*No internet?* Teacher-prepared printed AI answers and printed official tables.

**R2. Language coverage (RD-20).** Ask an AI translation tool to translate the same three sentences into English from
Nepali and from another language spoken in your area. Ask a fluent speaker to rate each translation 1–5. Record and
discuss the results.

**R3. Audit a dataset for coverage (RD-11).** Look at a dataset you have used this year (census, air quality,
rainfall stations). Who or what is under-represented? If an AI were trained on it, which places or people would it
serve worst?

## Unit project: AI charter and audit
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Produce (1) a class AI charter with 6 rules and
reasons, and (2) a short audit of one AI tool: five verified facts (R1), one bias test (R2 or a stereotype test), and a
recommendation for how your school should and should not use it. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Elements of AI (<https://www.elementsofai.com>): free, non-technical course (available in many languages).
* Day of AI / MIT RAISE free curriculum materials for students.
* Read `docs/pedagogy/ai-use-policy.md`, the policy this book uses.
