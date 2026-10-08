# Grade 11 · Unit 7: Maps and geospatial thinking

> Track: B (code, light) · Tools: Python, numpy, matplotlib (folium/GeoPandas optional) · Lessons: 3 · Version: 0.1 draft (English)
> Datasets: none

**Big idea.** Where things are matters. Coordinates, distances, regions and map choices (and their licences) all shape the story a map tells.

**What you will be able to do**

* I can use latitude/longitude.
* I can compute great-circle distance.
* I can plan a choropleth honestly and credit OpenStreetMap.

**Words to know:** latitude, longitude, coordinate, haversine, choropleth, ODbL (Nepali glossary: `curriculum/framework/glossary.md`).

**Notebook:** `notebooks/geo_basics.ipynb` (open in JupyterLite, Colab or Jupyter; runs offline on the synthetic table).

---

## Lesson 1: Coordinates and distance

**Hook (5 min).** How far is Kathmandu from Pokhara, as the crow flies?

**Concept (≤ 5 min).** Latitude (north–south) and longitude (east–west) locate points. The haversine formula gives great-circle distance on a sphere.

**Activity (PRIMM: Predict → Run → Investigate → Modify → Make) (20 min).** Compute distances between three city pairs; compare with road distances you know.

**Check (5 min).**
1. Latitude measures…
2. Straight-line vs road distance in hills?
3. What does haversine compute?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Maps that don't mislead

**Hook (5 min).** A map shades the biggest districts darkest by number of cases. Fair?

**Concept (≤ 5 min).** Choropleths should show rates, use clear classes and colour scales, and show missing areas. Bigger regions draw more attention than their populations deserve.

**Activity (20 min).** Critique three maps; redraw the colour classes for one.

**Check (5 min).**
1. Count or rate for a choropleth?
2. Why colour-blind-friendly scales?
3. What to show for missing data?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Open map data and licences

**Hook (5 min).** Where do school map data come from, and who can reuse them?

**Concept (≤ 5 min).** OpenStreetMap (ODbL) is open with credit and share-alike for databases; boundary files have their own licences.

**Activity (20 min).** Plan a map project: data source, licence, credit line, limits.

**Check (5 min).**
1. Credit line for OSM?
2. Does 'open' mean 'no conditions'?
3. Why check boundary licences?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit project: Where is it worst?

Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*
