# Free real datasets for exercises

Every chapter in this book ends with **Exercises with real data**. Those exercises use the datasets below. Each has
a code (**RD-01** … **RD-20**) so a chapter can say "use RD-05" and you can find it here.

**Rules that apply to all of them**

1. **Download from the publisher, not from a copy.** Links below go to the original source. The repository does
   not re-host real data (decision D7); `tools/fetch_data.py` downloads some of them reproducibly.
2. **Read the licence and credit the source** in anything you hand in or publish: name, publisher, link, year
   downloaded. "CC BY" means you may reuse with credit; "BY-SA" means anything you build from it must use the same
   licence; "NC" means no commercial use.
3. **No internet?** Every exercise names an **offline fallback**: a synthetic table shipped in `datasets/` with the
   same shape. Teachers can also download a file once and copy it to the school computers or a USB stick.
4. **Data change.** Publishers revise numbers. Write down the date you downloaded, and expect your answers to
   differ a little from a classmate who downloaded on another day. That is normal and worth discussing.

Licence status was checked on 2026-10-11 from the publishers' own pages where they were reachable. Check again
before you publish anything. Status: ✅ open licence confirmed · ⚠️ use in class, check terms before publishing ·
🚫 look, don't redistribute.

---

## Quick table

| Code | Dataset | Publisher | Licence | Access | Best for (grade · unit) |
|---|---|---|---|---|---|
| RD-01 | World Development Indicators (Nepal and neighbours) | World Bank | CC BY 4.0 ✅ | API / CSV | 9·7, 10·3, 10·4, 11·5, 12·2 |
| RD-02 | Our World in Data charts | Our World in Data | CC BY 4.0 ✅ | CSV per chart | 8·4, 8·7, 9·6, 10·3, 10·4 |
| RD-03 | Gapminder indicators | Gapminder Foundation | CC BY 4.0 ✅ | CSV | 8·7, 10·3, 12·7 |
| RD-04 | World Population Prospects | UN DESA Population Division | CC BY 3.0 IGO ✅ | CSV / data portal | 9·6, 9·7, 11·5 |
| RD-05 | Earthquake catalogue (Nepal region) | US Geological Survey | Public domain (US Gov) ✅ | API CSV | 8·4, 10·2, 10·4, 11·1, 11·7 |
| RD-06 | Historical daily weather for any town | Open-Meteo | CC BY 4.0 (free API: non-commercial) ✅ | API CSV | 8·6, 10·4, 11·3, 11·6 |
| RD-07 | Monthly temperature and rainfall (satellite/model) | NASA POWER | Free, cite NASA POWER ✅ | API CSV | 9·2, 10·1, 11·6, 11·8 |
| RD-08 | Kalimati vegetable and fruit prices 2013–2021 | Open Data Nepal (from Kalimati Market board) | CC BY (per listing) ⚠️ | Manual CSV (≈9 MB) | 9·5, 10·1, 10·4, 11·1, 11·6 |
| RD-09 | Annual rainfall by station 2004–2015 | Open Data Nepal (from CBS Statistical Year Book) | CC BY (per listing) ⚠️ | Manual CSV | 8·5, 9·1, 10·2 |
| RD-10 | Tourist arrivals by mode of transport 2001–2014 | Open Data Nepal (from Ministry of Culture, Tourism and Civil Aviation) | CC BY (per listing) ⚠️ | Manual CSV | 8·4, 9·7, 10·4 |
| RD-11 | Census 2021 preliminary results by district | Open Data Nepal (from NSO) | CC BY-SA ⚠️ | Manual CSV | 8·1, 9·3, 9·7, 11·2 |
| RD-12 | Air quality, Kathmandu 2015–2021 | Open Data Nepal (upstream OpenAQ) | CC BY-SA ⚠️ | Manual CSV (≈8 MB) | 9·2, 10·2, 10·8 |
| RD-13 | Census 2021 final results (tables) | National Statistics Office | Government publication ⚠️ | Portal tables | 9·7, 11·5, 12·7 |
| RD-14 | Glacial lakes of Nepal (inventories, potentially dangerous lakes) | ICIMOD Regional Database System | CC BY 4.0 ✅ | Download after free sign-in | 8·4, 10·2, 11·7 |
| RD-15 | Administrative boundaries (province, district, palika) | OCHA / HDX, from Survey Department | Check HDX page ⚠️ | GeoJSON / shapefile | 11·7 |
| RD-16 | OpenStreetMap features (schools, health posts, roads) | OpenStreetMap contributors | ODbL ✅ (share-alike) | HOT export / Overpass | 11·7, 12·8 |
| RD-17 | Palmer penguins | Allison Horst et al. | CC0 ✅ | CSV | 10·5, 12·1–12·4 |
| RD-18 | Global Health Observatory indicators | World Health Organization | CC BY-NC-SA 3.0 IGO ⚠️ | CSV / API | 12·5 (class use only) |
| RD-19 | Himalayan Database (expeditions) | The Himalayan Database | Personal licence; publishing needs permission 🚫 | Desktop program | 11·1 (explore only) |
| RD-20 | Your own class or school data | You | You decide (with consent) ✅ | Survey / records | every grade |

---

## Details and how to download

### RD-01 · World Development Indicators (World Bank) ✅
* **What:** about 1,400 yearly indicators for every country since 1960: population, GDP per person, school
  enrolment, electricity access, remittances, forest area, life expectancy.
* **Link:** <https://data.worldbank.org/country/nepal> (pick an indicator, then *Download → CSV*).
* **API pattern (one indicator, JSON):**
  `https://api.worldbank.org/v2/country/NPL;IND;BGD;LKA;PAK;BTN/indicator/SP.POP.TOTL?format=json&per_page=500`
* **Useful codes:** `SP.POP.TOTL` population · `NY.GDP.PCAP.CD` GDP per person (US$) ·
  `BX.TRF.PWKR.DT.GD.ZS` remittances (% of GDP) · `EG.ELC.ACCS.ZS` access to electricity (%) ·
  `SE.PRM.ENRR` primary enrolment (gross %) · `SP.DYN.LE00.IN` life expectancy · `SP.URB.TOTL.IN.ZS` urban
  population (%) · `IT.NET.USER.ZS` internet users (%) · `AG.LND.FRST.ZS` forest area (%).
* **Licence:** CC BY 4.0. Credit: "World Bank, World Development Indicators (downloaded DD-MM-YYYY)".
* **Offline fallback:** `datasets/census-districts/clean/districts_synthetic.csv` for per-capita work.

### RD-02 · Our World in Data ✅
* **What:** clean, documented long-run series (child mortality, life expectancy, CO₂, population, internet use).
* **Link:** any chart page, for example <https://ourworldindata.org/grapher/child-mortality>; use the
  *Download* tab, or this CSV pattern (works for most line charts):
  `https://ourworldindata.org/grapher/child-mortality.csv?country=NPL~IND~BGD~LKA&csvType=filtered&useColumnShortNames=true`
* **Charts that work well for Nepal:** `child-mortality`, `life-expectancy`, `co-emissions-per-capita`,
  `population` (note: it starts at year −10000, a nice cleaning surprise), `share-of-individuals-using-the-internet`,
  `mobile-cellular-subscriptions-per-100-people`, `share-of-population-urban`, `gdp-per-capita-worldbank`.
  Some charts ignore the country filter and return every country; then filter for `Nepal` yourself.
* **Licence:** CC BY 4.0 for OWID's own work; the chart page names the underlying source. Credit both.
* **Offline fallback:** `datasets/climate-monthly/clean/climate_monthly_synthetic.csv` for time-series practice.

### RD-03 · Gapminder ✅
* **What:** income, life expectancy, population, babies per woman for every country, 1800 to today. Famous for
  the "bubble chart" by Hans Rosling.
* **Link:** <https://www.gapminder.org/data/> (choose an indicator → *Download CSV*); tool: <https://www.gapminder.org/tools/>.
* **Licence:** CC BY 4.0. Credit: "Free data from Gapminder.org".
* **Offline fallback:** draw the bubble chart by hand from five countries' values copied from the teacher's sheet.

### RD-04 · UN World Population Prospects ✅
* **What:** population by age and sex, births, deaths, projections to 2100 for every country.
* **Link:** <https://population.un.org/wpp/> (*Download Center* → CSV). The files are large; the teacher can save
  just Nepal's rows. OWID's `population` chart (RD-02) is built from the same source and is smaller.
* **Licence:** CC BY 3.0 IGO. Credit: "UN DESA, Population Division, World Population Prospects (year of edition)".
* **Offline fallback:** `districts_synthetic.csv` (`male`, `female`, `population`).

### RD-05 · USGS earthquake catalogue ✅
* **What:** every recorded earthquake with time, latitude, longitude, depth and magnitude. The 25 April 2015
  Gorkha earthquake (magnitude 7.8) and its aftershocks are in it.
* **Link (CSV, Nepal box, April–December 2015, magnitude ≥ 4):**
  `https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2015-04-01&endtime=2015-12-31&minlatitude=26&maxlatitude=31&minlongitude=80&maxlongitude=89&minmagnitude=4`
  (about 300 rows). Change the dates and magnitude to get more or fewer rows. Search page:
  <https://earthquake.usgs.gov/earthquakes/search/>.
* **Licence:** US Government work, public domain. Credit "U.S. Geological Survey" anyway.
* **Care:** these events killed nearly 9,000 people. Some students lost family or homes. Teach it with respect and
  give students the choice of another dataset.
* **Offline fallback:** `air_daily_synthetic.csv` for dates and distributions.

### RD-06 · Open-Meteo historical weather ✅
* **What:** daily or hourly temperature, rain, wind for any latitude/longitude since 1940 (reanalysis, ~10 km grid).
* **Link (Kathmandu, 2023, daily max temperature and rain):**
  `https://archive-api.open-meteo.com/v1/archive?latitude=27.70&longitude=85.32&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia/Kathmandu&format=csv`
  Change latitude/longitude for other towns, e.g. Biratnagar 26.45, 87.27 · Pokhara 28.21, 83.99 ·
  Nepalgunj 28.05, 81.62 · Jumla 29.27, 82.18 · Dhangadhi 28.70, 80.59.
  The first two lines of the CSV are location metadata; the data table starts after a blank line
  (in pandas: `pd.read_csv(url, skiprows=3)`).
* **Licence:** data CC BY 4.0 ("Weather data by Open-Meteo.com"); the free API is for non-commercial use, which
  covers school work.
* **Care:** model data, not a weather station; it smooths mountains. Good for patterns, not for record values.
* **Offline fallback:** `climate_monthly_synthetic.csv`.

### RD-07 · NASA POWER ✅
* **What:** monthly temperature, rainfall, solar energy for any point, from satellites and models, since 1981.
* **Link (Kathmandu, monthly 2015–2023):**
  `https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2M,PRECTOTCORR&community=AG&longitude=85.32&latitude=27.70&start=2015&end=2023&format=CSV`
* **Why it is great for teaching:** the file has a text header block (`-BEGIN HEADER-` … `-END HEADER-`), months as
  columns (`JAN` … `DEC`, `ANN`), rain in **mm per day** not per month, and `-999` for missing values. Students
  must clean and reshape it: exactly the Grade 9–10 skills.
* **Licence:** free and open; NASA asks users to cite "NASA Langley Research Center (LaRC) POWER Project".
* **Offline fallback:** `climate_monthly_synthetic.csv`.

### RD-08 · Kalimati vegetable prices ⚠️
* **What:** daily minimum, maximum and average price of about 100 vegetables and fruits at Kalimati wholesale
  market, Kathmandu, June 2013 – May 2021. Columns: commodity, date, unit, minimum, maximum, average.
* **Link:** <https://opendatanepal.com/dataset/kalimati-tarkari-dataset> (manual download, ≈9 MB CSV). Current
  prices are published daily at <https://kalimatimarket.gov.np>.
* **Licence:** listed as Creative Commons Attribution on Open Data Nepal. Credit Open Data Nepal and the Kalimati
  Fruits and Vegetable Market Development Board.
* **Ideas:** tomato price by month (seasonality), festival-time spikes (Dashain/Tihar), which vegetable is most
  volatile, inflation of a "dal-bhat-tarkari basket".
* **Offline fallback:** `climate_monthly_synthetic.csv` (same date-handling skills).

### RD-09 · Annual rainfall by station ⚠️
* **What:** total rainfall (mm) per year at weather stations across Nepal, 2004–2015, from the CBS Statistical
  Year Book. Years are in columns (wide format), so it is ideal for "tidy data" practice.
* **Link:** <https://opendatanepal.com/dataset/annual-rainfall-in-mm-by-stations-from-2004-to-2015>; a 2019
  version ("Annual Rainfall by Station") and "Average Rainfall by Altitude" (CC BY-SA) are also on Open Data Nepal.
* **Licence:** Creative Commons Attribution per listing. Credit CBS/NSO and Open Data Nepal.
* **Offline fallback:** `climate_monthly_synthetic.csv`.

### RD-10 · Tourist arrivals ⚠️
* **What:** tourists arriving by air and by land each year, and foreign-exchange earnings, 2001–2014. Small (one
  row per year) and perfect for a first line graph. Newer figures are in the Ministry's yearly *Nepal Tourism
  Statistics* report (PDF).
* **Link:** <https://opendatanepal.com/dataset/total-annual-tourist-arrivals-by-mode-of-transportation-and-gross-earnings-2001-to-2014>
* **Licence:** Creative Commons Attribution per listing.
* **Offline fallback:** copy the 14 rows onto the blackboard; it is small enough.

### RD-11 · Census 2021 preliminary results ⚠️
* Already described in `datasets/census-districts/DATASET_CARD.md`. Population, households, male/female by district.
* **Licence:** CC BY-SA. Keep share-alike results separate from CC BY text (decision D8).
* **Offline fallback:** `districts_synthetic.csv` (same columns, invented numbers).

### RD-12 · Kathmandu air quality ⚠️
* Already described in `datasets/kathmandu-air-quality/DATASET_CARD.md`. Daily PM2.5, PM10 and other pollutants
  2015–2021 from the US Diplomatic Post and other stations via OpenAQ.
* **Licence:** CC BY-SA per Open Data Nepal; OpenAQ asks you to credit the original data provider too.
* **Offline fallback:** `air_daily_synthetic.csv`.

### RD-13 · Census 2021 final results ⚠️
* **What:** official tables: population by age, sex, caste/ethnicity, language, religion, literacy, disability,
  housing, migration, at national, provincial, district and municipal level.
* **Link:** <https://censusnepal.cbs.gov.np/results> (National Statistics Office). Many tables can be viewed and
  downloaded; reports are PDFs. Microdata is restricted; do not request it for school work.
* **Licence:** government publication. Use and cite freely in class; check terms before republishing whole tables.
* **Offline fallback:** `districts_synthetic.csv`.

### RD-14 · ICIMOD glacial lakes ✅
* **What:** inventories of glacial lakes (area, elevation, basin, type) and a ranked list of potentially dangerous
  lakes in the Koshi, Gandaki and Karnali basins.
* **Link:** <https://rds.icimod.org> → search "glacial lakes". Examples: DOI 10.26066/RDS.1971946 (glacial lakes
  2020) and 10.26066/RDS.1971950 (potentially dangerous lakes). Free sign-in is needed to download.
* **Licence:** CC BY 4.0 (per record). Credit "ICIMOD (2020) …" with the DOI.
* **Offline fallback:** teacher prints a 20-row extract.

### RD-15 · Administrative boundaries (HDX) ⚠️
* **What:** outlines of the 7 provinces, 77 districts and local levels, for drawing maps. Nepal has 753 local
  levels, but the HDX file lists 775 admin-3 units: finding out why is itself a good data-checking exercise.
* **Link:** <https://data.humdata.org/dataset/cod-ab-npl>. Read the licence field on the page before use.
* **Offline fallback:** a printed outline map and coloured pencils (choropleth by hand).

### RD-16 · OpenStreetMap ✅ (share-alike)
* **What:** schools, health posts, roads, rivers, mapped by volunteers (many in Nepal by Kathmandu Living Labs
  and HOT after 2015).
* **Link:** <https://export.hotosm.org> (choose an area and a feature type) or <https://overpass-turbo.eu>.
* **Licence:** ODbL. Credit "© OpenStreetMap contributors". Anything you build from it must stay ODbL.
* **Care:** OSM is only as complete as volunteers made it; missing schools may be "unmapped", not "absent".

### RD-17 · Palmer penguins ✅
* **What:** 344 penguins, 3 species, bill and flipper measurements. Not Nepali, but the cleanest small dataset for
  first classification models.
* **Link:** `https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv`
* **Licence:** CC0.
* **Offline fallback:** `health_synthetic.csv` (binary target `institutional_delivery`).

### RD-18 · WHO Global Health Observatory ⚠️
* **What:** health indicators by country: immunisation, stunting, tuberculosis, road deaths.
* **Link:** <https://www.who.int/data/gho>.
* **Licence:** CC BY-NC-SA 3.0 IGO: fine for class work; non-commercial; share-alike. Do not paste into CC BY
  material.

### RD-19 · Himalayan Database 🚫
* **What:** every expedition to Nepal's high peaks since 1905 (Elizabeth Hawley's records): peak, year, season,
  members, success, deaths.
* **Link:** <https://www.himalayandatabase.com> (free desktop program).
* **Licence:** single-user licence; publishing extracts or analyses needs written permission. Use it to **explore
  and ask questions** in class; do not upload tables or results publicly without permission.

### RD-20 · Your own data ✅
* Class surveys, school attendance (anonymised, with the head teacher's permission), a weather diary, a traffic
  count at the school gate, prices at the local shop. Use the consent form in
  `community/student-data-consent.md`. Small, real and yours: often the best dataset of all.

---

## Datasets we looked at and do not recommend

| Dataset | Why not |
|---|---|
| DrivenData "Richter's Predictor" (2015 earthquake buildings) | Competition rules allow use only for the competition; no redistribution |
| DHS microdata | Registration required; no redistribution "directly or within any tool/dashboard" (decision D6) |
| Census 2021 microdata | Restricted access |
| Commercial mirrors of NRB/CPI data (CEIC etc.) | Paywalled; use Nepal Rastra Bank publications at <https://www.nrb.org.np> instead |
| 2015 earthquake housing survey portal (eq2015.npc.gov.np) | Valuable, but no licence statement found; explore online only |
