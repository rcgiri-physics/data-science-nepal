# Roadmap and status (v0.1.0, 2026-10-07)

Legend: ✅ done and checked in this repo · 🟡 drafted, needs human review · ⏳ needs people/time outside the repo.

## What the automated gates verify today
`python tools/validate_dataset_cards.py` (5 cards) · `python tools/check_units.py` (40 units, 123 lessons) ·
`python tools/check_notebooks.py` (28 notebooks execute top-to-bottom offline, with assertions) · `python tools/build_site.py` (MkDocs builds) ·
`python tools/build_offline_bundle.py` (school bundle zip).

## Phase 0 — Verification & decisions
- ✅ Decisions logged with the plan's recommended options (`docs/decisions.md`).
- ✅ Dataset licences checked from publisher-page snippets (`docs/alignment/dataset-licence-register.md`); DHS confirmed non-redistributable.
- ⏳ Read the CDC/NEB syllabus PDFs and GAISE II in full; add page references (the fetch tool could not open them).
- ⏳ Re-open each dataset's primary page and paste the licence text into its card (several portals returned 403/404 to automated fetches).
- ⏳ Measure JupyterLite first-load time on a slow link.

## Phase 1 — Skeleton + vertical slice
- ✅ Repo structure, licences, CITATION, CONTRIBUTING, governance, templates, CI workflows.
- ✅ Tools: dataset-card validator, unit checker, notebook runner, fetch script, offline bundle, site builder.
- ✅ 5 dataset cards + deterministic **synthetic** practice tables (real data fetched from publishers, not re-hosted).
- ✅ Complete flagship units: **G8 U1** (chapter EN + NE draft, teacher guide, 2 worksheets, quiz, project) and **G9 U3** (chapter EN + NE draft, teacher guide, runnable SQL notebook, quiz, project).
- ⏳ Create the GitHub repo, turn on Pages, and confirm the JupyterLite build runs in CI (workflow written, not yet run).

## Phase 2 — Grades 8–10
- ✅ 24 unit packs (8 per grade) written: chapter, teacher guide, project, quiz, dataset list; 12 runnable notebooks for G9–G10.
- 🟡 Streamlit starter app written and syntax-checked, **not run** (Streamlit not installed here).
- 🟡 Lesson count is 24/27/24 for G8/G9/G10 (plan targeted ~24/28/30): add lessons as pilots show gaps.
- ⏳ Sketchnotes, printable PDFs, assessment banks beyond the per-unit quiz, Nepali for the other 38 units.

## Phase 3 — Grades 11–12 + Beyond 12
- ✅ 16 unit packs with 16 runnable notebooks, capstone kit (brief, data agreement, model card, rubric), Beyond-12 chapter.
- ⏳ A capstone completed by a real pilot team as the worked example.
- ⏳ Verify and add larger real datasets (DHM rainfall, earthquake damage, OSM) one by one with licence cards.

## Phase 4 — Pilot, feedback, offline bundle
- ✅ `tools/build_offline_bundle.py`; pilot protocol, instruments and report template (`pilots/`); one-day teacher training outline.
- ⏳ Run pilots in 3–5 schools; record the training; teacher review of Nepali.

## Phase 5 — CDC package & community launch
- ✅ Drafts: policy brief, competency-map skeleton, blog post, teacher guide (`docs/for-cdc/`, `docs/for-teachers/`).
- ⏳ Fill the competency map with syllabus page references; pilot results; freeze `v1.0` "CDC submission edition"; contact the AI & ICT committee; publish the blog post; open `good-first-issue`s.
- Tag **`v0.1.0`** marks this draft only. `v1.0` must wait for pilot evidence.

## Open roles
Teacher co-maintainer · statistician / university partner · Nepali-language editor · pilot schools · repo owner for GitHub org/Pages.

## Questions still for the owner
Owner to review decisions D11–D16 in `docs/decisions.md`; supply the GitHub account/org to replace `REPLACE-ME` (`CITATION.cff`, one dataset card), and name the pilot schools.
