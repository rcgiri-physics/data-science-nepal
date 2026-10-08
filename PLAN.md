# Data Science for Nepal's Schools (Grades 8–12): Curriculum + Open Repo Plan

> Working title: **डेटा विज्ञान / Data Science Nepal** (open curriculum, GitHub-hosted)
> Author/maintainer: Ram Chandra Giri (rcgiri.physics@gmail.com) — all reuse requires attribution
> Plan written: 2026-10-07. Status key: ✅ verified in research · ⚠️ must verify before building · ❌ problem found

---

## 0. Read this first: 7 findings that change the plan

| # | Finding | Consequence |
|---|---------|-------------|
| 1 | ❌ **DHS (health survey) microdata cannot be redistributed** — not in a repo, not inside a dashboard; registration is required and use is limited to the registered purpose. ([DHS terms](https://dhsprogram.com/data/terms-of-use.cfm)) | The original idea "Six notebooks incl. health (DHS)" cannot ship DHS files. Use *published aggregate tables* (to verify), other open health data, or a synthetic teaching dataset modelled on DHS. See §5. |
| 2 | ✅ **CDC's school-curriculum revision (Grades 1–12) is live right now.** Task force formed Apr 2026; provincial consultations were scheduled to end 16 Sep 2026; one of 12 thematic committees is "AI and ICT"; drafting follows. ([Kathmandu Post](https://kathmandupost.com/national/2026/09/14/nepal-begins-overhaul-of-school-curriculum-with-ai-and-indigenous-knowledge-in-focus)) | There's a time window. A *policy brief + ready-to-adopt unit pack* should reach the AI/ICT committee early in drafting, not after. |
| 3 | ⚠️ **Computer Science is an *optional* subject in Grades 9–10**, and Grade 10 already has Python + DBMS + "AI & contemporary technologies"; Grade 9 mentions SQL. (CDC Secondary Optional CS Curriculum 2080; sources in §11) | Your assumption "Python starts in 9" may be off by a grade (Python in 10; SQL in 9). Verify against the actual syllabus PDFs. Also: most students never take the optional CS course, so the curriculum needs a **no-code track delivered inside compulsory Maths/Science/Social** *and* a coding track for CS/clubs. |
| 4 | ✅ Grade 8 Maths has Statistics (pie chart, mean, median, mode) but research notes textbook stats is calculation-heavy; question-formation, data collection and interpretation are rarely taught. ([Springer](https://link.springer.com/chapter/10.1007/978-981-97-8426-4_24)) | Our Grade 8 unit adds exactly what's missing (ask → collect → analyse → interpret) — a strong, easy-to-justify pitch to CDC. |
| 5 | ✅ NEB Grade 11–12 CS covers DBMS, web, C, OOP, trends — no Python/data analysis. | Our G11–12 content is *enrichment/bridge*, aligned to (not replacing) NEB CS; map each unit to NEB units so schools can justify time. |
| 6 | ✅ Nothing found that is a Nepal-specific, open, Grade 8–12 data-science curriculum on national datasets. Nepal activity is university/adult level (Omdena–NIC, NAAMII, CS50x Nepal, Samsung Innovation Campus, Code for Nepal fellowships) or CS clubs (CoSoG Nepal). | The niche is real and open. **Partner, don't compete**: CoSoG (school CS clubs), Open Knowledge Nepal (data), NAAMII/NIC (teacher PD). |
| 7 | ⚠️ Colab needs a Google account + internet; many Nepali schools have weak connectivity. JupyterLite (Python in the browser, no server) can be fully self-hosted/offline, but pandas needs >70 MiB first load. ([JupyterLite](https://jupyterlite.readthedocs.io/en/latest/howto/configure/advanced/offline.html)) | **Offline-first** delivery: JupyterLite as the primary runtime, Colab badge as secondary, downloadable "school USB bundle". |

---

## 1. Vision, audience, and scope

**Goal.** A free, openly licensed, bilingual (Nepali + English), spiral curriculum in data science for Grades 8–12, built on real Nepali data, with teacher-ready materials, designed so CDC can adopt or adapt it.

**Two audiences, one repo**
1. **Students** (13–18): book-like chapters, notebooks, projects.
2. **Teachers / CDC reviewers**: facilitation guides, alignment maps, assessment rubrics, pilot evidence.

**Two delivery tracks**
- **Track A "No-code / low-tech"** (paper, calculator, spreadsheet/CODAP): usable in compulsory Maths, Science, Social Studies, Health. Reaches every student.
- **Track B "Code"** (Python, SQL): for optional CS, ICT clubs, and Grades 11–12.

**Non-goals (v1):** a deep-learning course; a replacement for NEB CS; anything requiring paid software or accounts.

**End-of-12 outcome (your requirement).** A final "Beyond Grade 12" chapter shows how this connects to higher education (BSc CSIT, BIT, BE Computer/Software, Statistics, Economics, Public Health, Environmental Science, abroad pathways), careers, and free next steps — explicitly framed as *a taste, not a full course*.

---

## 2. Research: what exists elsewhere (and what to borrow)

| Source | What it is | Borrow | Licence / caution |
|---|---|---|---|
| [GAISE II (ASA/NCTM)](https://nctm.org/Standards-and-Positions/GAISE-II) | Pre-K–12 statistics & data-science framework; Levels A/B/C; the 4-step investigative cycle | **Backbone of our scope & sequence**: map G8→B, G9–10→B/C, G11–12→C | Free to download; cite, don't copy text |
| [Bootstrap:Data Science](https://bootstrapworld.org/materials/data-science) | Gr 5–12 data literacy + Gr 9–12 data science; stats + programming + civic responsibility; mix-and-match modules | The "meaningful domains + civic responsibility" idea; modular units that stretch from 1 week to a year | CC 4.0 but **restricts PD use** → read terms, don't copy |
| [Introduction to Data Science (IDS), UCLA/LAUSD](https://www.lausd.org/Page/6764) | High-school course, R/RStudio, students collect data via phones ("participatory sensing") | **Student-generated data** as a core strand; fusing maths + computing | Check licence before reusing anything |
| [CBSE AI Class 9/10](https://vedantu.com/syllabus/cbse-class-9-artificial-intelligene-syllabus) | India: AI project cycle, data literacy, maths for AI (stats/prob), intro Python, gen-AI | Regional comparator; shows what neighbours' CDC-equivalent already expects | Syllabus only |
| [Australia Digital Technologies 9–10 "Data science skills"](https://www.digitaltechnologieshub.edu.au/search/years-9-10-data-science-skills/) | Data as a process: acquire (surveys, sensors, repositories) → store → analyse → visualise | Data-lifecycle framing for G9–10 | Reference only |
| [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | 20 lessons/10 weeks; per-lesson quiz, assignment, sketchnote; 50+ translations; quiz app | **Repo template**: lesson anatomy, pre/post quizzes, sketchnotes, translations folder | MIT — reusable with notice; adult-beginner level, US-neutral data |
| [CODAP (Concord Consortium)](https://codap.concord.org/about/) | Free open-source drag-and-drop data tool, Gr 6–college, runs in browser | **Grade 8 tool** (no code, no install) | Free, open |
| [Edinburgh/Education Scotland Python & RStudio school resources](https://open.ed.ac.uk/python-and-rstudio-school-resources/) | CC BY 4.0 Jupyter notebooks for schools | Notebook style for school age | CC BY 4.0 |
| Callysto (Canada), Girls Who Code curriculum-notebooks | CC-licensed Jupyter notebooks for K-12 | Fill-in-the-blank notebook scaffolding | Verify each |
| [CS50x Nepal / CS50 AI](https://cs50xnepal.ioepc.edu.np/), Omdena–NIC, NAAMII | Nepal university/adult programmes | Teacher-PD partners; pathway targets for Grade 12 chapter | — |

**To do in Phase 0:** spend one pass reading GAISE II Level B/C tables and the Bootstrap + IDS unit lists *in full*, and the CDC syllabus PDFs (Gr 8 Maths, Gr 9/10 CS, NEB 11/12 CS). Record gaps in `docs/alignment/`.

---

## 3. Pedagogy ("latest", and suited to Gen Z / Gen Alpha in Nepal)

Principle: **real question → real Nepali data → small win fast → reflect → make something public.**

| Practice | How it shows up in every unit |
|---|---|
| **Statistical investigation cycle (PPDAC / GAISE)**: Problem → Plan → Data → Analysis → Conclusion | Every unit and every project uses these five headings. Same skeleton from Gr 8 to 12 = spiral. |
| **Project/inquiry-based learning**, anchored in community | Each unit ends in a mini-project with a *local* question (my ward, my district, my school). |
| **PRIMM for coding** (Predict–Run–Investigate–Modify–Make) + Use-Modify-Create | Every notebook: predict the output → run → explain → tweak → build own. No blank-page coding for beginners. |
| **Worked examples + faded scaffolding** (fill-in-the-blank → partial → blank) | Notebook cells get progressively less scaffolding across the year. |
| **Retrieval practice / spaced quizzes** | 3-question starter quiz recalling last lesson's idea; unit-end low-stakes quiz (offline-printable too). |
| **Formative assessment & rubrics** (fits NCF 2076 competency-based, continuous assessment) | Each unit has I-can statements, a 4-level rubric, and a teacher observation checklist. |
| **Collaborative learning** (pair programming, jigsaw, gallery walk) | Roles card: driver/navigator, data steward, storyteller. |
| **Culturally and locally relevant** | Rainfall in Terai vs Hill vs Himalaya, remittance, migration, monsoon, air quality in Kathmandu, earthquake rebuilding, school enrolment by gender. Nepali-language variable names in glossary. |
| **Universal Design for Learning** | Printable versions, text + visual + audio explanations, mobile-friendly pages. |
| **Micro-content for short attention spans** | Lesson = ≤ 5-minute concept + 20-min activity + 10-min reflection. Optional ≤ 4 min Nepali video per concept. Sketchnote per lesson. |
| **Responsible AI use policy** | Students may use AI assistants as *tutors* ("explain, don't answer"); a documented prompt card; disclose use; assessment requires explaining their own code/interpretation orally. A unit on AI literacy and hallucination at Gr 10+. |
| **Data ethics & privacy from Gr 8** | Consent for survey data, anonymising, bias, "who is missing from this dataset?", caste/ethnicity/gender data handled sensitively. |
| **Teacher-first design** | 40/45-minute period plans, "if no computers", "if no internet", common misconceptions, answer keys. |

---

## 4. Scope & sequence (spiral, GAISE-aligned)

**Spiral idea:** the same five-step cycle, same recurring "anchor datasets", bigger data and sharper tools each year.

| Gr | Theme | Data size & type | Tools | Stats/CS ideas | Flagship project |
|----|-------|------------------|-------|----------------|------------------|
| **8** | *Data detectives* — statistical thinking, no coding | Own class data (≤ 40 rows) + one small district table (≤ 77 rows) | Paper, calculator, Calc/Sheets, **CODAP** | Question types; variables; collecting & sampling basics; tables; bar/pie/line/dot plots; mean/median/mode/range; spotting misleading graphs | "Our class, our school": a class survey + one census table → a one-page poster with a claim and evidence |
| **9** | *Data wranglers* — tidy data & first code | Census 2021 by district/province (77 rows × ~20 cols); school flash-report tables (hundreds of rows) | Spreadsheets → **SQL (SQLite)** → intro Python/pandas in browser | Rows/columns/types; cleaning; filter/sort/group; joins; percentage & rate; histograms, box plots; correlation (visual) | "Which districts are changing?" census-to-poster + simple SQL report |
| **10** | *Data analysts* — Python & analysis | Air quality Kathmandu (thousands of rows), climate monthly series, school/district panels | **Python (pandas, matplotlib)**, SQL | Distributions, outliers, scatterplots, correlation vs causation, line of best fit, time series basics, *intro to prediction* (what ML is); AI & ethics; build a small **Streamlit/Flask** dashboard | "Air in my city": analyse a year of PM2.5, publish a mini dashboard |
| **11** | *Data scientists I* — inference, time & space | 10⁴–10⁶ rows: daily rainfall/temperature (DHM/CCKP), air quality, earthquake damage survey, OSM features | pandas, SQL (SQLite/PostgreSQL), GeoPandas/folium, seaborn | Sampling variation, bootstrap, confidence intervals (intuitive), hypothesis test (permutation), linear regression, time series, maps | "Climate or weather?": detect a trend in Nepal climate data, with uncertainty |
| **12** | *Data scientists II* — modelling & communicating | Largest dataset the student picks (health, migration, education, hazards) + their own | scikit-learn, pandas, Streamlit (**Django optional capstone**), Git/GitHub | Supervised ML (regression/classification), train/test split, overfitting, evaluation metrics, bias/fairness, reproducibility, data storytelling | **Capstone** with a community "client" (ward office, health post, school, NGO) + public write-up |
| **Beyond 12** | *Where this goes next* | — | — | Pathways, careers, free resources, ethics of AI | One-page personal roadmap |

**On your Django idea.** Django is a full web framework — heavy for school PCs and a big detour from data work. Recommend **Streamlit** (or Flask) for Gr 10–12 dashboards; keep **Django as an optional stretch** in Gr 12 for students who already know HTML/web from NEB CS.

**On MySQL.** Use **SQLite** (zero install, works in browser, file-based) for Gr 9–11 and introduce MySQL/PostgreSQL *concepts* in Gr 11–12; the SQL students write is the same. This also matches NEB DBMS content.

### Unit outline (draft; ~6–8 units per grade, 3–5 lessons each)

**Grade 8 (no-code, ~24 lessons)**
1. What is data? (types, sources, who collects Nepal's data — NSO, DHM, Ministry of Education) 
2. Asking good questions (survey vs measurement, bias, fair sampling)
3. Collecting & recording (class survey; consent; tally → table)
4. Showing data (bar/pie/line/dot plots in CODAP; misleading graphs)
5. Summarising data (mean/median/mode/range; which to use when)
6. Comparing groups (two ward/district tables; rates not counts)
7. Telling the story (claim–evidence–reasoning poster)
8. Data and people (privacy, fairness, "who is missing?")

**Grade 9 (~28 lessons)**: tidy data & spreadsheets · cleaning (missing, duplicates, units, Nepali/English names, BS/AD dates) · SQL basics (SELECT/WHERE/ORDER/GROUP BY/JOIN) · first Python in browser (variables, lists, loops *only as needed*) · pandas read/filter/groupby · charts · percent vs rate vs per-capita · mini-project

**Grade 10 (~30 lessons)**: pandas deep-dive · distributions & outliers · relationships (scatter, correlation) · line of best fit by hand then code · time series basics · "what is a model/what is ML" with a tiny k-NN or decision-tree *unplugged then coded* · AI literacy & ethics · dashboard with Streamlit/Flask · project

**Grade 11 (~30 lessons)**: bigger data & performance basics · SQL window functions-lite · uncertainty (bootstrap, CI, permutation test) · regression with interpretation · time series & seasonality · geospatial (district maps, OSM) · reproducibility (notebooks, Git) · project

**Grade 12 (~30 lessons)**: ML workflow (train/test/validation) · regression & classification · evaluation metrics · overfitting · fairness/bias audit · feature engineering · communicating (dashboards, data stories, policy memos) · capstone w/ client · "Beyond 12" chapter

---

## 5. Dataset catalogue (open-data-first)

Every dataset gets a **Dataset Card** (`datasets/<name>/DATASET_CARD.md`): source URL, publisher, licence, date accessed, columns & units, known problems, cleaning notes, ethical flags, which grade uses it, checksum. **Rule: never commit a dataset without a verified licence in its card.**

| Dataset | Grades | Source | Status / licence |
|---|---|---|---|
| Census 2021 results (district, province, municipality tables) | 8–12 | [NSO census portal](https://censusnepal.cbs.gov.np/results), [Open Data Nepal](https://opendatanepal.com/dataset/preliminary-data-of-national-population-and-housing-census-2021) | ✅ exists; preliminary data on ODN is CC BY-SA; ⚠️ confirm final-results terms. Full **microdata is restricted** ([NSO microdata](https://microdata.nsonepal.gov.np)) — don't use |
| NSO National Data Portal indicators (CSV/GeoJSON/API) | 9–12 | NSO | ✅ formats; ⚠️ licence |
| Open Data Nepal catalogue (630 datasets, 24 categories, CKAN) | all | [opendatanepal.com](https://opendatanepal.com) | ✅ "use/reuse/redistribute" per site; ⚠️ per-dataset licence (many CC BY) |
| School education (secondary schools per district 2003–2015, enrolment, flash reports) | 8–11 | ODN, Dept of Education / CEHRD flash reports | ✅ example CC BY; ⚠️ newer flash reports licence |
| Air quality Kathmandu 2015–2021 (PM2.5, PM10, O₃, NO₂, CO…) | 9–11 | [ODN](https://opendatanepal.com/ne/dataset/air-quality-data-in-kathmandu), pollution.gov.np | ✅ exists; ⚠️ licence & live-data scraping terms |
| Climate: historical + projections | 10–12 | [World Bank Climate Knowledge Portal](https://climateknowledgeportal.worldbank.org), [Open Knowledge Nepal climate portal](https://climate.opendatanepal.com/) | ✅ exist; ⚠️ confirm CC BY 4.0 for CCKP downloads |
| Hydrology/meteorology stations (DHM) | 10–12 | [ODN](https://opendatanepal.com/dataset/hydrological-station-of-nepal-with-latitude-and-longitude/resource/1ea49ba3-a9e7-4b27-844a-4c3763bcd899) | ✅ exists; ⚠️ licence. Daily rainfall series: find open source |
| 2015 earthquake housing damage / Open Cities educational facilities | 11–12 | ODN, NRA/NPC, Kathmandu Living Labs | ⚠️ locate and verify |
| Health: DHS 2022 | 11–12 | [DHS Program](https://dhsprogram.com) | ❌ **no redistribution.** Options: (a) link to registration steps for teachers; (b) use *aggregate* published indicator tables if their terms allow; (c) generate a **synthetic dataset** with DHS-like structure for practice; (d) HMIS/DoHS public tables |
| Living standards (NLSS), Labour Force Survey, economic census | 11–12 | NSO | ⚠️ microdata access restricted; use published tables |
| Maps / roads / facilities | 11–12 | OpenStreetMap Nepal (ODbL), HOT | ✅ open; ODbL needs attribution & share-alike for DB |
| Humanitarian Data Exchange, ICIMOD RDS, WorldPop, Our World in Data (Nepal slices) | 10–12 | public portals | ⚠️ per-dataset licence |
| **Student-generated data** (class surveys, school weather station, school canteen, travel-to-school) | 8–12 | the students | ✅ you control the licence (CC0). Build a **contribute-your-data** template with consent + anonymisation checklist |

**MVP: six flagship notebooks** (your original idea, adjusted): ① Gr 8 class survey + census table (CODAP & Sheets) · ② Gr 9 census-by-district with SQL · ③ Gr 10 Kathmandu air quality in Python · ④ Gr 10/11 climate trend · ⑤ Gr 11 health indicators (aggregate/synthetic, see above) · ⑥ Gr 12 capstone template. These form the first public release and the demo for CDC.

---

## 6. Repository design

**Principles:** book-like, modular (a unit = a chapter), contributor-friendly, offline-capable, bilingual, no giant files.

```
data-science-nepal/
├── README.md                    # What, who for, how to start, how to cite/attribute, links to blog
├── LICENSE-CONTENT.md           # CC BY 4.0 (text) – see §8
├── LICENSE-CODE                 # MIT (code)
├── ATTRIBUTION.md               # "How to credit me" with copy-paste citation + CITATION.cff
├── CITATION.cff
├── CONTRIBUTING.md  CODE_OF_CONDUCT.md  GOVERNANCE.md  ROADMAP.md
├── docs/                        # Website source (MkDocs Material)
│   ├── index.md   about.md   how-to-use.md
│   ├── for-teachers/            # facilitation guide, classroom management, no-computer plans
│   ├── for-cdc/                 # curriculum framework, alignment matrices, policy brief, pilot evidence
│   ├── pedagogy/                # PPDAC, PRIMM, AI-use policy, assessment
│   └── beyond-grade-12/         # pathways & careers chapter
├── curriculum/
│   ├── framework/               # competencies by grade (I-can), scope & sequence, GAISE mapping
│   ├── grade-08/
│   │   ├── README.md            # grade overview: outcomes, units, time, tools
│   │   ├── unit-01-what-is-data/
│   │   │   ├── chapter.md              # student-facing "book chapter" (en)
│   │   │   ├── chapter.ne.md           # Nepali version
│   │   │   ├── teacher-guide.md        # lesson plans, timing, misconceptions, answer key
│   │   │   ├── worksheets/             # printable PDFs + source
│   │   │   ├── notebooks/              # .ipynb (grade ≥ 9)
│   │   │   ├── project.md              # PPDAC project brief + rubric
│   │   │   ├── quiz.yml                # pre/post questions (machine-readable)
│   │   │   ├── sketchnote.png
│   │   │   └── datasets.yml            # which dataset cards it uses
│   │   └── …
│   ├── grade-09/ … grade-12/
├── datasets/
│   ├── README.md   catalog.yml
│   └── <dataset-name>/ {DATASET_CARD.md, raw/, clean/, scripts/}   # small files only; big ones fetched by script
├── tools/
│   ├── fetch_data.py            # reproducible download + checksum from original source
│   ├── validate_dataset_cards.py   # CI: card exists, licence field set
│   ├── check_notebooks.py       # CI: execute notebooks, fail on error
│   └── build_offline_bundle.py  # makes USB/zip: JupyterLite + datasets + PDFs
├── jupyterlite/                 # config for in-browser Python (no install)
├── community/
│   ├── dataset-requests/        # "I have a dataset / a problem" issue templates
│   ├── student-gallery/         # accepted projects, with consent
│   └── translations/
├── pilots/                      # school pilot logs, feedback, anonymised results
├── .github/
│   ├── ISSUE_TEMPLATE/ {new-dataset, new-lesson, bug, translation, teacher-feedback}
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/ {build-site.yml, test-notebooks.yml, lint-links.yml, dataset-cards.yml}
└── pyproject.toml  environment.yml  requirements.txt
```

**"Chapter in a book" feel:** the website renders each unit as a numbered chapter (G8 Ch1 … ) with sidebar navigation, "Open in JupyterLite" and "Open in Colab" buttons per notebook, printable PDF, and a Nepali toggle.

**Tooling decision (default; revisit in Phase 0):** MkDocs Material (Markdown-first, easy for teachers to PR) + JupyterLite for runnable notebooks + GitHub Pages hosting + GitHub Actions CI. Alternative: Jupyter Book if notebooks should be the primary source.

**Lesson anatomy (every lesson):** Hook (local question, 5 min) → Concept (≤ 5 min) → Activity (20 min, PRIMM) → Check for understanding (3 Qs) → Reflect (2 min) → Extension. Includes: "Teacher: if no computers/internet…", glossary (EN/NE), sources.

**Quality gates in CI:** every notebook executes top-to-bottom offline-capable; every dataset has a card with licence; link checker; reading-level/jargon lint (optional); Nepali text present for released units.

---

## 7. Community and contribution model (your "others can add datasets/problems" idea)

- **Contribution types**: (1) new dataset + card, (2) new problem/project for an existing unit, (3) translation, (4) bug/fact fix, (5) teacher feedback/pilot report, (6) student-gallery entries.
- **Issue templates** make a non-programmer teacher able to say: "I have this dataset, grade X, topic Y."
- **Review**: 1 maintainer + 1 subject reviewer (teacher or statistician) per PR; labels `grade-8`…`grade-12`, `dataset`, `translation`, `needs-teacher-review`.
- **Credit**: `CONTRIBUTORS.md` + all-contributors bot; units list authors.
- **Governance**: you as lead maintainer; add 2–3 co-maintainers (a school teacher, a statistician/university partner, a Nepali-language editor) by v0.3. Draft `GOVERNANCE.md` early since CDC will want to know who maintains it.
- **Stability for CDC**: tagged releases (`v0.1`, `v1.0`) and a frozen "CDC submission edition" so government can cite a fixed version.

---

## 8. Licensing and attribution (how "just mention me" actually works)

- **Content (text, lesson plans, worksheets, images): CC BY 4.0.** Anyone can reuse/adapt — *including the government* — **provided they credit you**. That's the legal mechanism for "use my content by mentioning me." Alternative: **CC BY-SA 4.0** (adaptations must stay open; may be harder for CDC to publish inside a copyrighted textbook). **CC BY-NC** would block commercial coaching centres but also breaks "open" and many school/NGO uses — not recommended.
- **Code: MIT.** Ship `CITATION.cff` + an ATTRIBUTION page with copy-paste credit line and a link to your blog.
- **Data keeps its original licence**; Dataset Cards carry it. Respect share-alike (CC BY-SA, ODbL) where it applies. Don't mix restricted data (DHS, microdata) into the repo.
- **Third-party content:** log anything borrowed (Microsoft DS4B is MIT; Bootstrap is CC 4.0 *with PD restrictions*) in `THIRD_PARTY.md`.
- **Student work:** only publish with guardian/teacher consent; anonymise.

---

## 9. Evidence, pilots, and the pathway to CDC

1. **Pilot** (Phase 4): 3–5 schools — mix of urban/rural, private/public, with/without reliable internet. Collect: pre/post concept check, teacher time-logs, student enjoyment, issues.
2. **CDC pack** (`docs/for-cdc/`): (a) 2-page policy brief — "Data literacy and AI readiness for NCF revision"; (b) **competency map** to NCF 2076 and the Gr 8 Maths / Gr 9–10 CS / NEB 11–12 CS units; (c) pilot results; (d) sample unit ready to drop into a textbook; (e) teacher training outline; (f) cost note ("zero licence cost, offline possible").
3. **Channels**: CDC AI & ICT thematic committee; CEHRD teacher training; Kathmandu University (task-force chair is a KU professor); NAAMII, NIC, Open Knowledge Nepal, CoSoG, Code for Nepal.
4. Submit **early** (during drafting), as an offer to the working committee, not a finished product.

---

## 10. Phased execution plan (for Opus or any agent)

Each phase has deliverables and acceptance criteria. Execute in order; commit after each.

### Phase 0 — Verification & decisions (do first)
- [ ] Download and read: CDC Gr 8 Maths (stats chapter), Gr 9 & 10 CS (`Secondary Level Optional Computer Science Curriculum 2080`), NEB 11/12 CS; produce `docs/alignment/current-syllabus-notes.md` (what's already covered, where Python/SQL/AI are).
- [ ] Read GAISE II Level B/C in full → `curriculum/framework/gaise-mapping.md`.
- [ ] Verify licences for every dataset in §5 (open each portal, record licence text + URL + date); resolve all ⚠️.
- [ ] Decide DHS strategy (§5) and health notebook data source.
- [ ] Confirm toolchain: MkDocs Material + JupyterLite builds, pandas runs in browser; measure first-load size on a 2 Mbps connection.
- [ ] Copy §12 decisions D1–D12 into `docs/decisions.md` and adjust any the Phase 0 checks overturn (esp. D4, D6).
- **Done when:** `docs/decisions.md` exists; no ⚠️ remain on MVP datasets.

### Phase 1 — Skeleton + vertical slice
- [ ] Create repo structure (§6), licence files, CITATION.cff, CONTRIBUTING, templates, CI workflows.
- [ ] Dataset Card template + 3 MVP datasets with scripts (census districts, Kathmandu air quality, climate monthly).
- [ ] Build **one complete unit per band** end-to-end as the template: **G8 Unit 1** (no-code) and **G9 Unit 3** (SQL on census) including chapter (EN+NE), teacher guide, worksheet, notebook, quiz, rubric.
- [ ] Site live on GitHub Pages with JupyterLite working.
- **Done when:** a teacher can open the site on a phone, do G8-U1 on paper, and run the G9 notebook in-browser with no install; CI green.

### Phase 2 — Grades 8–10 complete
- [ ] All units per §4; the six flagship notebooks (§5 MVP); sketchnotes; printable PDFs; glossary EN/NE.
- [ ] Teacher guides for every lesson; assessment banks.
- **Done when:** a teacher can run a full year with only this repo; all notebooks pass CI offline.

### Phase 3 — Grades 11–12 + Beyond 12
- [ ] Larger datasets (script-fetched), geospatial unit, inference unit, ML unit, fairness unit, capstone kit (client brief, data agreement template, rubric).
- [ ] `beyond-grade-12/`: pathways (Nepal universities & degree programmes, scholarships, free online courses), careers, ethics, "how data science is taught in colleges" overview.
- **Done when:** capstone completed once by a pilot student/team as a worked example.

### Phase 4 — Pilot, feedback, offline bundle
- [ ] `build_offline_bundle.py` → zip/USB package with JupyterLite, datasets, PDFs.
- [ ] Pilot in 3–5 schools; teacher training session (record it); log in `pilots/`; fix issues.
- [ ] Nepali translation review by a teacher.

### Phase 5 — CDC package & community launch
- [ ] Policy brief, competency map, pilot report, tagged `v1.0` "CDC submission edition".
- [ ] Blog post (your Blogspot) linking to the repo + attribution guidance; announce to partners; open `good-first-issue`s.

**Parallelisation tip for agents:** Phase 2 units are independent per grade once the Phase 1 templates exist — one agent per grade, each reading `docs/pedagogy/` and the unit template first.

---

## 11. Sources consulted (for your blog's reference list)

- Nepal curriculum revision: [Kathmandu Post, 14 Sep 2026](https://kathmandupost.com/national/2026/09/14/nepal-begins-overhaul-of-school-curriculum-with-ai-and-indigenous-knowledge-in-focus); [Republica](https://myrepublica.nagariknetwork.com/news/nepal-moves-to-reshape-school-curriculum-for-life-jobs-74-44.html); [Himalayan Times](https://thehimalayantimes.com/nepal/govt-to-introduce-revised-school-curriculum-next-session)
- Current syllabus: [CS Grade 9 (Govt of Nepal PDF)](https://giwmscdnone.gov.np/media/pdf_upload/Computer%20Science%20Grade%209_r12pxcl.pdf); [Gr 8 Maths textbook analysis](https://link.springer.com/chapter/10.1007/978-981-97-8426-4_24); [Gr 8 Maths textbook PDF](https://nepalikitab.org/wp-content/uploads/books/school/0008_MathematicsEnglishTranslationClass8.pdf); [NEB 11/12 CS](https://readersnepal.com/posts/neb-class-11-and-12-computer-science-new-curriculum-and-syllabus)
- Data: [Census 2021 portal](https://censusnepal.cbs.gov.np/results); [Open Data Nepal](https://opendatanepal.com); [NSO microdata](https://microdata.nsonepal.gov.np); [World Bank CCKP](https://climateknowledgeportal.worldbank.org); [DHS 2022 on WB microdata](https://microdata.worldbank.org/catalog/5910/); [DHS terms](https://dhsprogram.com/data/terms-of-use.cfm)
- International programmes: [GAISE II](https://nctm.org/Standards-and-Positions/GAISE-II); [Bootstrap:DS](https://bootstrapworld.org/materials/data-science); [IDS/LAUSD](https://www.lausd.org/Page/6764); [CBSE AI](https://vedantu.com/syllabus/cbse-class-9-artificial-intelligene-syllabus); [Australia DT 9–10](https://www.digitaltechnologieshub.edu.au/search/years-9-10-data-science-skills/); [Microsoft DS4B](https://github.com/microsoft/Data-Science-For-Beginners); [CODAP](https://codap.concord.org/about/); [Edinburgh school resources](https://open.ed.ac.uk/python-and-rstudio-school-resources/)
- Tech: [JupyterLite offline](https://jupyterlite.readthedocs.io/en/latest/howto/configure/advanced/offline.html)
- Nepal ecosystem: [CS50x Nepal](https://cs50xnepal.ioepc.edu.np/); [Omdena–NIC](https://www.omdena.com/omdena-capacity-building-program-with-nic-nepal); [CoSoG Nepal](https://github.com/COSOGNepal); [NAAMII–King's College](https://thehimalayantimes.com/kathmandu/kings-college-partners-with-naamii-for-ai-education)

> Note: search results are secondary summaries. Items marked ⚠️ were not confirmed at the primary source and must be checked in Phase 0 before anything is built on them.

---

## 12. Decisions (made by Claude on the owner's instruction "you decide everything" — owner to review and change)

| # | Decision | Reason | Easy to change? |
|---|----------|--------|-----------------|
| D1 | **Content licence: CC BY 4.0**; code MIT; data keeps its own licence | Attribution is legally required (your "mention me"), and CDC/NGOs can adopt without share-alike friction | Yes before v0.1; hard after others reuse it |
| D2 | **English draft first, Nepali translation by a teacher-editor, released together per unit** (a unit isn't "released" without `.ne.md`) | Faster to write and review technical content; Nepali is mandatory for CDC adoption | Yes |
| D3 | **Dashboards: Streamlit** (Flask as alternative); **Django = optional Grade 12 stretch only** | Lightweight, data-focused, runs on modest PCs | Yes |
| D4 | **Python timing:** a short "first Python" taste in Grade 9 (after SQL), main Python in Grade 10 | Matches CDC syllabus as found (SQL in 9, Python in 10); verify in Phase 0 and shift if wrong | Yes, after Phase 0 check |
| D5 | **Database: SQLite** for Grades 9–11; MySQL/PostgreSQL taught as concepts in 11–12 | No install, runs in browser, same SQL | Yes |
| D6 | **Health data:** use aggregate published indicator tables if terms allow, otherwise a clearly labelled **synthetic dataset** with DHS-like structure; link teachers to DHS registration for real microdata | DHS bans redistribution | Yes |
| D7 | **Stack:** MkDocs Material + JupyterLite + GitHub Pages + GitHub Actions; Colab buttons as secondary | Contributor-friendly, offline-capable, free | Yes |
| D8 | **Name:** repo `data-science-nepal`, site title "Data Science Nepal (डेटा विज्ञान नेपाल)"; hosted first under the owner's personal GitHub account, move to an org once there are 2+ maintainers | Simple, searchable; avoids org overhead at start | Yes |
| D9 | **Attribution line** (in README/ATTRIBUTION.md/CITATION.cff): "Data Science Nepal curriculum by Ram Chandra Giri and contributors, CC BY 4.0, <blog URL>" | Satisfies "mention me" | Yes |
| D10 | **Pilot schools:** none assumed. Recruit 3–5 via CoSoG Nepal, Code for Nepal, personal contacts; mix of urban/rural and internet/no-internet | — | Owner may already have schools |
| D11 | **Co-maintainers:** aim for one teacher, one statistician/university contact, one Nepali-language editor by v0.3 | Review quality and CDC credibility | Owner decides who |
| D12 | **Scope guard:** v0.1 = Grade 8 Unit 1 + Grade 9 Unit 3 + 3 datasets + working site; no new units before the vertical slice passes review | Prevents building much content on unverified assumptions | Yes |

> Remaining items only the owner can supply: real pilot schools, blog URL, GitHub username, and any contacts at CDC/CEHRD.
