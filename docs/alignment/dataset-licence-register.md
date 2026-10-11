# Dataset licence register

Status key: ✅ confirmed · ⚠️ partly confirmed, check the publisher's page · ❌ cannot be redistributed.
"Evidence" = what was read on 2026-10-07 (publisher-page summaries; some portals did not allow direct page
access). Check the publisher's page and copy its licence text into the dataset card before redistributing real data.

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

## Exercise datasets (checked 2026-10-11)
Used in chapter exercises only; downloaded by students/teachers from the publisher, never re-hosted here. Full
directory: [`../datasets/free-datasets.md`](../datasets/free-datasets.md).

| Code | Dataset | Licence found | Status | Evidence / caveat |
|---|---|---|---|---|
| RD-01 | World Bank WDI | CC BY 4.0 | ✅ | World Bank open data terms; API tested 2026-10-11 |
| RD-02 | Our World in Data | CC BY 4.0 (own work; underlying source named per chart) | ✅ | Chart CSV endpoints tested |
| RD-03 | Gapminder | CC BY 4.0 | ✅ | gapminder.org/free-material |
| RD-04 | UN World Population Prospects | CC BY 3.0 IGO | ✅ | Licence notice on WPP files and reports |
| RD-05 | USGS earthquake catalogue | US Government public domain | ✅ | FDSN CSV endpoint tested (≈300 events, Nepal box, Apr–Dec 2015) |
| RD-06 | Open-Meteo historical | Data CC BY 4.0; free API non-commercial | ✅ | open-meteo.com/en/licence and /en/terms |
| RD-07 | NASA POWER | Free; citation requested | ✅ | power.larc.nasa.gov/docs/referencing; endpoint tested |
| RD-08 | Kalimati prices 2013–2021 (ODN) | Creative Commons Attribution (listing) | ⚠️ | ODN listing; site footer links BY-SA 4.0 deed — treat as BY-SA if unsure |
| RD-09 | Annual rainfall by station (ODN, CBS) | Creative Commons Attribution (listing) | ⚠️ | Source is CBS Statistical Year Book |
| RD-10 | Tourist arrivals 2001–2014 (ODN) | Creative Commons Attribution (listing) | ⚠️ | Source MoCTCA |
| RD-14 | ICIMOD glacial lakes | CC BY 4.0 | ✅ | RDS metadata records (DOIs in directory) |
| RD-15 | HDX COD-AB Nepal boundaries | Check HDX page | ⚠️ | Public access; licence string not read |
| RD-17 | Palmer penguins | CC0 | ✅ | palmerpenguins package |
| RD-18 | WHO GHO | CC BY-NC-SA 3.0 IGO | ⚠️ | Class use only; never mix into CC BY text |
| RD-19 | Himalayan Database | Single-user licence; publishing needs permission | ❌ | Program guide "Software License and Terms of Use" |
| — | DrivenData Richter's Predictor | Competition-only use; no redistribution | ❌ | Competition rules |
