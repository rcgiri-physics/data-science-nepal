# Roadmap and status

Legend: ✅ done in repo · 🟡 drafted, needs human review · ⏳ needs people/time outside the repo.

## Phase 0 — Verification & decisions
- ✅ Decisions logged (`docs/decisions.md`), recommended options chosen.
- ✅ Dataset licences checked from publisher-page snippets (`docs/alignment/dataset-licence-register.md`).
- ⏳ Read CDC/NEB syllabus PDFs and GAISE II fully; add page references.
- ⏳ Measure JupyterLite first-load on a slow link.

## Phase 1 — Skeleton + vertical slice
- ✅ Repo structure, licences, CITATION, CONTRIBUTING, templates, CI workflows.
- ✅ Tools: dataset-card validator, notebook checker, fetch script, offline bundle builder.
- ✅ Dataset cards for 3 MVP datasets + synthetic practice tables.
- ✅ Complete units: **G8 Unit 1** and **G9 Unit 3** (chapter EN + NE, teacher guide, worksheet, notebook, quiz, project, rubric).
- ⏳ Turn on GitHub Pages (needs repo owner) and confirm JupyterLite build in CI.

## Phase 2 — Grades 8–10
- ✅ All 24 unit packs written (chapter, teacher guide, project, quiz, datasets list).
- 🟡 Flagship notebooks for G9–G10 (runnable, on synthetic data; swap to real data after `fetch_data.py`).
- ⏳ Sketchnotes, printable PDFs, Nepali translation of units other than the two flagship ones.

## Phase 3 — Grades 11–12 + Beyond 12
- ✅ All 16 unit packs, capstone kit, Beyond-12 chapter.
- ⏳ A real capstone completed by a pilot student as worked example.

## Phase 4 — Pilot, feedback, offline bundle
- ✅ `tools/build_offline_bundle.py`, pilot protocol and forms in `pilots/`.
- ⏳ Pilot in 3–5 schools; teacher training; Nepali review by a teacher.

## Phase 5 — CDC package & community launch
- ✅ Drafts: policy brief, competency map skeleton, blog post draft (`docs/for-cdc/`).
- ⏳ Pilot results, `v1.0` "CDC submission edition", submission to the AI & ICT committee, announcements.

## Open roles
Teacher co-maintainer · statistician / university partner · Nepali-language editor · pilot schools.
