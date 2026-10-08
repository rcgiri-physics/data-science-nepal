# Design decisions

| # | Topic | Decision | Reason |
|---|---|---|---|
| D1 | Licences | **CC BY 4.0** for content, **MIT** for code; data keeps its own licence | Reuse with credit; CDC and NGOs can adopt without share-alike friction |
| D2 | Languages | English first, Nepali by a teacher-editor, released together per unit | Technical content is faster to write in English; Nepali is needed for CDC adoption |
| D3 | Dashboards | **Streamlit**; Django only as an optional Grade 12 stretch | Light on school PCs; stays focused on data |
| D4 | Programming order | SQL in Grade 9, a short first-Python taste in Grade 9, main Python in Grade 10 | Matches the optional CS syllabus as reported |
| D5 | Database | **SQLite** in Grades 9–11; MySQL/PostgreSQL as concepts in 11–12 | No install, runs in the browser, same SQL |
| D6 | Health data | No DHS data is shipped. A clearly labelled synthetic table is used instead | DHS terms forbid redistribution "directly or within any tool/dashboard" |
| D7 | Real vs synthetic data | Real data is fetched from the original publisher by script; only small synthetic tables are shipped, labelled `SYNTHETIC` | Licence safety; no invented numbers presented as real |
| D8 | Data licences | Share-alike data (CC BY-SA, ODbL) stays in `datasets/` and is not mixed into CC BY text | Keeps CC BY content clean |
| D9 | Tooling | MkDocs Material + JupyterLite + GitHub Pages + GitHub Actions; Colab as secondary | Contributor-friendly, offline-capable, free |
| D10 | Offline first | JupyterLite primary; school USB bundle (`tools/build_offline_bundle.py`) | Weak connectivity in many schools |
| D11 | Name and branding | "Data Science Nepal / डेटा विज्ञान"; repo `data-science-nepal` | Neutral and searchable |
| D12 | Hosting | GitHub account `rcgiri-physics`; move to an organisation once there are two or more maintainers | Simple start |
| D13 | Release scope | Grade 8 Unit 1 and Grade 9 Unit 3 are the v0.1 release candidate; other units are available for review and are not recommended for classroom pilots until reviewed | Review the vertical slice before scaling |
| D14 | Pilots | 3–5 schools: urban and rural, public and private, with and without internet; first units G8 U1 and G9 U3 | Tests both tracks |
| D15 | Co-maintainers | One teacher, one statistician or university contact, one Nepali-language editor | Review quality and CDC credibility |
| D16 | Releases | `v0.x` until pilot evidence exists; `v1.0` afterwards | Avoids claiming unproven impact |

Dataset licence evidence: [alignment/dataset-licence-register.md](alignment/dataset-licence-register.md).
