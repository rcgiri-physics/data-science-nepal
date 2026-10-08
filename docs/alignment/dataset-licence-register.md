# Dataset licence register

Status key: ✅ confirmed · ⚠️ partly confirmed, re-check at primary page · ❌ cannot be redistributed.
"Evidence" = what was read on 2026-10-07 (search-result snippets of publisher pages; direct page
fetches of some portals returned 403/404). **A maintainer must re-open the primary page and paste
the licence text into the dataset card before the first real-data release.**

| Dataset | Licence found | Status | Evidence / caveat | Repo handling |
|---|---|---|---|---|
| Census 2021 preliminary data (Open Data Nepal) | CC BY-SA (dataset listing); copyright NSO Nepal 2021 | ⚠️ | ODN site footer says platform content is CC BY 4.0 but the dataset listing says BY-SA → treat as **BY-SA**. Final-results terms on censusnepal.cbs.gov.np not read | Script-fetch; card says BY-SA; not mixed into CC BY text |
| Census 2021 microdata (NSO) | Restricted access | ❌ | microdata.nsonepal.gov.np | Do not use |
| Air Quality Kathmandu 2015–Mar 2021 (ODN) | CC BY-SA; author Hel Nershing Thapa; upstream OpenAQ; CSV ≈ 8.3 MiB | ⚠️ | ODN listing; check OpenAQ upstream licence | Script-fetch; BY-SA card |
| World Bank CCKP climate data | CC BY 4.0 (World Bank datasets default) | ✅ | World Bank data-catalog entries for CCKP list CC BY 4.0 | Script-fetch; attribute World Bank |
| DHS 2022 microdata | Registration required; no redistribution "directly or within any tool/dashboard"; use limited to registered purpose; non-commercial | ❌ | dhsprogram.com terms of use | Never ship. Use synthetic teaching table |
| DHM station list / rainfall (ODN) | Not confirmed | ⚠️ | Not opened | Phase-3 verify; do not ship until confirmed |
| Earthquake 2015 housing / Open Cities | Not confirmed | ⚠️ | Not opened | Phase-3 verify |
| OpenStreetMap | ODbL | ✅ | osm.org/copyright (well known) | Fetch by bounding box; credit "© OpenStreetMap contributors" |
| School flash reports / education tables | Not confirmed | ⚠️ | Not opened | Verify before use |
| NLSS, LFS, economic census | Microdata restricted; tables unverified | ⚠️ | — | Published tables only, after check |
| Student-generated data | CC0 (our template) | ✅ | Consent form in `community/` | Allowed with consent form |
| **Synthetic teaching tables written for this repo** | CC0 | ✅ | `datasets/*/scripts/make_synthetic.py` | Shipped; labelled SYNTHETIC |
