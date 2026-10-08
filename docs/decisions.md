# Decisions log (Phase 0)

Date: 2026-10-07. Decisions on PLAN.md §12 open questions were made by taking the plan's
**recommended option**; the owner can reverse any of them by opening an issue.

| # | Question | Decision | Reason |
|---|---|---|---|
| D1 | Content licence | **CC BY 4.0** (code MIT) | Matches "reuse by crediting me"; lets CDC embed in textbooks. BY-SA would complicate government publishing. |
| D2 | Writing language | **English draft + Nepali by teacher-editor**, released together per unit | Fast drafting, quality Nepali. Units without reviewed Nepali are labelled `ne: draft/pending`. |
| D3 | Web framework | **Streamlit** for Gr 10–12 dashboards; **Django optional** stretch in Gr 12 | Light on school PCs; stays on data work. |
| D4 | Database | **SQLite** Gr 9–11; MySQL/PostgreSQL as concepts in Gr 11–12 | Zero install, runs in browser, same SQL. |
| D5 | Project / repo name | **डेटा विज्ञान / Data Science Nepal**; repo `data-science-nepal` | Plan's working title. Owner to pick the GitHub account/org (open). |
| D6 | Site tooling | **MkDocs Material + JupyterLite + GitHub Pages + GitHub Actions** | Markdown-first, easy for teachers to PR. |
| D7 | Health data (DHS) | **Do not ship DHS.** Use a **clearly-labelled synthetic** DHS-like teaching dataset; teachers may register with DHS themselves | DHS terms forbid redistribution "directly or within any tool/dashboard". |
| D8 | Offline-first | **JupyterLite primary**, Colab badge secondary, USB bundle script | Weak connectivity in many schools. |
| D9 | Real vs synthetic data in repo | Real data is **fetched by script from the original source** (never silently re-hosted); the repo ships only small *synthetic* practice tables, always labelled `SYNTHETIC` | Licence safety and honesty: no invented numbers presented as real. |
| D10 | Data licence handling | Datasets keep their own licence in their card; share-alike data (CC BY-SA, ODbL) stays in `datasets/` and is not mixed into CC BY content | Keeps CC BY content clean. |

## Verified in this pass (2026-10-07, via web search of publisher-page snippets)
See [alignment/dataset-licence-register.md](alignment/dataset-licence-register.md).

## Not verifiable here (needs a person) — carried to ROADMAP
* Reading the CDC / NEB syllabus PDFs end-to-end (the Grade 9 CS PDF exceeded the fetch size limit).
* GAISE II full text (publisher site returned HTTP 402) — the mapping uses the public four-step
  process and level structure; add page references after reading the PDF.
* Pilot schools, teacher PD sessions, Nepali editorial review, CDC submission.
* Measuring JupyterLite first-load time on a 2 Mbps link.

## Owner delegated all remaining decisions (2026-10-08) — to be reviewed by the owner
| # | Question | Decision | Reason |
|---|---|---|---|
| D11 | Branding | Project name only ("Data Science Nepal / डेटा विज्ञान"); the maintainer's blog is linked, not used as the brand | Neutral name suits CDC and partners |
| D12 | Hosting account | GitHub account `rcgiri-physics`, repo `data-science-nepal` (URLs filled in locally). **Not created or pushed**: publishing waits for the owner's go-ahead | Account read from the logged-in `gh` session; publishing is outward-facing |
| D13 | Pilot schools | Start with 3 convenience schools the maintainer can reach (1 urban private, 1 urban public, 1 rural public), first units G8 U1 and G9 U3 | Smallest pilot that tests both tracks |
| D14 | Co-maintainer recruitment | Ask CoSoG Nepal for a teacher, a Kathmandu University statistician, and a Nepali-language editor | Matches GOVERNANCE.md roles |
| D15 | Release policy | `v0.x` until pilot evidence exists; `v1.0` only afterwards | Avoids claiming unproven impact to CDC |
| D16 | Lesson count | Keep 123 lessons in v0.1; add lessons only where pilots show gaps | Quality over quantity |
