# Teacher guide — Grade 11, Unit 7: Maps and geospatial thinking

**Time:** 3 lessons + project (about 5 periods). **Track:** B (code, light).

| # | Lesson | Time |
|---|---|---|
| 1 | Coordinates and distance | 40–45 min |
| 2 | Maps that don't mislead | 40–45 min |
| 3 | Open map data and licences | 40–45 min |
| P | Unit project: Where is it worst? | 2 periods |

## Before you start
* Materials: Notebook `notebooks/geo_basics.ipynb`; optional OSM data via Overpass (internet).
* Read `docs/pedagogy/lesson-anatomy.md` and `docs/pedagogy/ai-use-policy.md`.

## If you have no computers / no internet
Use a printed map and string to compare straight-line and road distances.

## Common misconceptions
* Colour maps of counts mislead; use rates.
* Straight-line distance = travel distance in the hills.

## Differentiation
* Support: give a partially filled table / sentence starters; pair with a data-steward role.
* Stretch: ask "what would change your conclusion?" and "who is missing?"

## Answer key (check questions)
**Lesson 1: Coordinates and distance**
1. Latitude measures…  
   *Answer:* North–south position.
2. Straight-line vs road distance in hills?  
   *Answer:* Road is longer.
3. What does haversine compute?  
   *Answer:* Distance along the Earth's surface between two points.

**Lesson 2: Maps that don't mislead**
1. Count or rate for a choropleth?  
   *Answer:* Rate.
2. Why colour-blind-friendly scales?  
   *Answer:* Many people can't tell red from green.
3. What to show for missing data?  
   *Answer:* A distinct colour/pattern and a legend note.

**Lesson 3: Open map data and licences**
1. Credit line for OSM?  
   *Answer:* © OpenStreetMap contributors.
2. Does 'open' mean 'no conditions'?  
   *Answer:* No: check the licence.
3. Why check boundary licences?  
   *Answer:* They may differ from the map data.

## Assessment
Starter quiz each lesson (3 questions, one recalling the previous lesson); unit quiz in `quiz.yml`;
project marked with the rubric in `docs/pedagogy/assessment.md`; 2-minute oral check per group.

## Alignment
Enrichment aligned to NEB Grade 11–12 Computer Science (databases, programming) and Maths/Statistics.

## Answers: practice exercises
1. (27.7, 85.3) = latitude 27.7° N, longitude 85.3° E — Kathmandu. (85.3, 27.7) read as lat/lon is near the North Pole
   region (85.3° N) — a swapped-coordinate bug.
2. ≈ 222 km; ≈ 2 × 98 = 196 km.
3. "© OpenStreetMap contributors" (with a link to openstreetmap.org/copyright where possible).
4. ≈ 832 km straight line; highway ≈ 1,000 km → ratio ≈ 1.2 (the Terai is flat; hill routes have far higher ratios).
5. Nearest synthetic station ≈ 30 km from Kathmandu (PM2.5 82.1); 11 stations within 150 km, mean PM2.5 ≈ 92.5 (all
   synthetic, with an invented west–east gradient).
6. Equal intervals (width 20.75 from 12 to 95): 7, 1, 1, 1 → only 1 district in the top class. Quantiles (breaks ≈ 15,
   17, 31.75): 2–3 districts per class → 3 in the top class (35, 60, 95). Quantiles exaggerate the gap between 16 and 18.
7. The large district's rate (based on 1,200 cases) is far more reliable; the small district's 75 could be 25 or 125
   next year by chance. Show counts, use multi-year rates, or mark low-population districts.
8. Density divides by area: small crowded districts (Kathmandu valley, Terai) stand out; a count map highlights big
   populations; area bias differs. Each answers a different question.
9. Layers: schools and health posts (OSM, ODbL), roads/footpaths (OSM), palika boundary (HDX, check licence); method:
   network travel time or at least straight-line distance; limits: unmapped facilities, seasonal roads, facility opening
   hours/staffing.
10. If the combined database is published (publicly used), it must be offered under ODbL (share-alike) with credit; the
    private data mixed into it would become subject to that.

## Real-data exercises: notes
* **R1** The aftershock zone extends east of the Gorkha epicentre towards Dolakha/Sindhupalchok (the 12 May 7.3 quake);
  most events are within ≈ 50–150 km of Kathmandu.
* **R2** Koshi basin generally has the most potentially dangerous lakes in the ICIMOD 2020 inventory — check the file.
* **R3** Requires internet and geopandas; expect name mismatches after the 2015 restructuring.
