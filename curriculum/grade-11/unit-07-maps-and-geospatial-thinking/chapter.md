# Grade 11 · Unit 7: Maps and geospatial thinking

> Track: B (code, light) · Tools: Python, numpy, matplotlib (folium/GeoPandas optional) · Lessons: 3
> Datasets: none

**Big idea.** Where things are matters. Coordinates, distances, regions and map choices (and their licences) all shape the story a map tells.

**What you will be able to do**

* I can use latitude and longitude, compute great-circle distances, and explain why travel distance differs.
* I can design a choropleth that shows a rate with honest classes, colours and missing-data handling.
* I can find open map data, follow its licence, and plan a map project.

**Words to know:** latitude (अक्षांश), longitude (देशान्तर), coordinate, great-circle distance, haversine, projection, choropleth, classification (classes), point map, OpenStreetMap, ODbL, boundary file. Full list: `curriculum/framework/glossary.md`.

**Notebook:** `notebooks/geo_basics.ipynb` (generates synthetic stations; runs offline).

### Before you start
Grade 8 Unit 4 (graphs that mislead), Grade 9 Unit 7 (rates), Grade 8 Unit 8 (who is missing). Optional tools: `folium`
(interactive web maps) and `geopandas` (boundary files) are not needed for the core lessons, which use only numpy and
matplotlib.

---

## Lesson 1: Coordinates and distance

**Hook (5 min).** How far is Pokhara from Kathmandu "as the crow flies"? And by road? Write your two guesses. Why might
they be so different?

### Explanation
Every point on Earth has two **coordinates**:
* **Latitude** (अक्षांश): degrees north or south of the equator (−90° to +90°). Nepal lies between about 26.3° N and
  30.5° N.
* **Longitude** (देशान्तर): degrees east or west of the Prime Meridian through Greenwich (−180° to +180°). Nepal lies
  between about 80° E and 88.2° E.

Kathmandu is at about (27.717° N, 85.324° E); Pokhara at (28.210° N, 83.986° E). On maps and in data, coordinates are
usually written as decimal degrees, **latitude first** (but many file formats, such as GeoJSON, store **longitude
first** — a classic source of bugs that puts Nepal in the ocean).

**Degrees are not kilometres.** One degree of latitude is about 111 km everywhere. One degree of longitude is 111 km at
the equator but shrinks towards the poles: at Nepal's latitude (28°) it is about 111 × cos 28° ≈ 98 km. So you cannot
use Pythagoras on raw degrees.

**The haversine formula** gives the **great-circle distance** — the shortest distance along the surface of a sphere:

```python
import numpy as np

def haversine_km(lat1, lon1, lat2, lon2, radius_km=6371.0):
    """Great-circle distance in km between points given in decimal degrees."""
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = phi2 - phi1
    dlam = np.radians(lon2 - lon1)
    a = np.sin(dphi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlam / 2) ** 2
    return 2 * radius_km * np.arcsin(np.sqrt(a))

towns = {
    "Kathmandu": (27.7172, 85.3240), "Pokhara": (28.2096, 83.9856), "Biratnagar": (26.4525, 87.2718),
    "Nepalgunj": (28.0500, 81.6167), "Jumla": (29.2742, 82.1838),
}
for a, b in [("Kathmandu", "Pokhara"), ("Kathmandu", "Biratnagar"), ("Nepalgunj", "Jumla")]:
    print(a, "–", b, round(haversine_km(*towns[a], *towns[b])), "km")
```

Results: Kathmandu–Pokhara ≈ **142 km**, Kathmandu–Biratnagar ≈ 239 km, Nepalgunj–Jumla ≈ 147 km. The road from
Kathmandu to Pokhara is about 200 km and takes 6–8 hours; Nepalgunj to Jumla by road is much further than 147 km and
can take a day or more. In the hills, **travel time** — not straight-line distance — decides access to schools,
hospitals and markets. Analysts use road networks (from OpenStreetMap) to compute travel times.

`np.radians` converts degrees to radians, which trigonometric functions need. Because the function uses numpy, it works
on whole columns at once (vectorised, Unit 1).

### Activity (20 min) — PRIMM
1. **Predict** the three distances, then compute them.
2. Look up road distances (a map app or bus timetable) and compute the ratio road ÷ straight line. Which route is most
   "winding"?
3. **Make:** compute the distance from your school (find its coordinates on a map: right-click → coordinates) to the
   nearest district hospital and to the district headquarters.

### Common mistakes
* Swapping latitude and longitude.
* Using Pythagoras on degrees.
* Treating straight-line distance as access in mountainous areas.

**Check (5 min).**
1. Latitude measures…
2. Straight-line vs road distance in hills?
3. What does haversine compute?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 2: Maps that don't mislead

**Hook (5 min).** A national map shades districts by "number of dengue cases", darkest for the most cases. Kathmandu and
large Terai districts are dark; small Mountain districts are pale. What has the map really shown? And why does the
eye notice the big pale Mountain districts so much?

### Explanation
**Kinds of thematic maps**
* **Point map:** a dot for each location (schools, stations, earthquakes). Good for "where".
* **Proportional symbol map:** circles sized by a count (population of each town). Good for counts.
* **Choropleth** (from Greek "area" + "many"): regions coloured by a value. Good for **rates**, bad for counts.

**Rules for an honest choropleth**
1. **Map rates, not counts.** Counts mostly show population size (Grade 8 Unit 6). Map cases per 100,000 people.
2. **Choose classes deliberately.** The same data can look very different with different class breaks:
   * **equal intervals** (0–10, 10–20, …) — easy to read, can put almost every region in one class when data are skewed;
   * **quantiles** (each class has the same number of regions) — always shows contrast, but can exaggerate small
     differences;
   * **meaningful thresholds** (above/below a health standard) — best when such thresholds exist.
   Use 4–6 classes, and state the method in the legend.
3. **Colour:** a **sequential** scale (light → dark) for low → high; a **diverging** scale (blue ← white → red) only
   when there is a meaningful middle (e.g. above/below the national rate). Avoid red–green (about 1 in 12 men are
   colour-blind); use tested palettes such as "viridis".
4. **Show missing data** in a distinct colour or hatching with a legend entry — never the "lowest" colour.
5. **Area bias:** big, empty regions dominate the eye. Nepal's large Mountain districts (Dolpa, Humla, Mugu) have small
   populations; a district map overweights them visually. Consider a **cartogram** or a tile map (each district the same
   size) as a companion.
6. **Small numbers:** rates from small populations jump around (2 cases in 5,000 people = 40 per 100,000). Show the
   counts too, or combine years.
7. Title, legend with units, source, date, and **credit** for the boundaries.

Without boundary files we can still practise the ideas on a point map of synthetic stations:

```python
import matplotlib.pyplot as plt

rng = np.random.default_rng(9)
stations = {"lat": rng.uniform(26.4, 30.4, 40), "lon": rng.uniform(80.1, 88.1, 40)}
pm25 = (30 + 12 * (stations["lon"] - 80) + rng.normal(0, 8, 40)).round(1)     # invented west–east pattern

plt.scatter(stations["lon"], stations["lat"], c=pm25, cmap="viridis", s=40)
plt.colorbar(label="PM2.5 (µg/m³) — SYNTHETIC")
plt.xlabel("Longitude (°E)")
plt.ylabel("Latitude (°N)")
plt.gca().set_aspect(1 / np.cos(np.radians(28)))     # stretch so 1° lon looks as long as it is at 28° N
plt.title("Invented monitoring stations")
plt.show()
```

The `set_aspect` line corrects the shape: without it, Nepal looks squashed or stretched, because 1° of longitude is
shorter than 1° of latitude here.

### Activity (20 min)
1. Critique three maps (teacher's printouts, a newspaper, or OWID's world maps): what is mapped (count or rate)? which
   classes? which colours? how is missing data shown? what is the source?
2. Take the synthetic district table's `absentee_population` and compute both count and rate per 1,000. On a printed
   outline map of districts (or a tile grid), colour the same 10 districts by count and by rate with 4 quantile classes.
   How do the stories differ?
3. Recolour one map with equal-interval classes. Which version would you publish, and why?

### Common mistakes
* Choropleths of counts.
* Too many classes or a rainbow palette.
* Missing data shown as "lowest".

**Check (5 min).**
1. Count or rate for a choropleth?
2. Why colour-blind-friendly scales?
3. What to show for missing data?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

## Lesson 3: Open map data and licences

**Hook (5 min).** Where does the map on your phone come from? Who drew the roads and schools in your village? Could you
use that map in a school report? In a company's app?

### Explanation
**Sources of map data for Nepal**

| Data | Source | Licence | Notes |
|---|---|---|---|
| Roads, buildings, schools, health posts, rivers | OpenStreetMap (RD-16), via HOT Export Tool or Overpass | ODbL (open, share-alike) | mapped by volunteers; much mapping after 2015 by Kathmandu Living Labs and HOT; completeness varies |
| Province, district, palika boundaries | HDX (OCHA COD-AB, from Survey Department) (RD-15) | check the dataset page | boundary versions change (2015 restructuring) |
| Glacial lakes, land cover | ICIMOD RDS (RD-14) | CC BY 4.0 per record | scientific inventories with DOIs |
| Earthquakes | USGS (RD-05) | public domain | points with depth and magnitude |
| Elevation, satellite images | NASA, ESA (Copernicus) | open, with credit | large files |

**ODbL (Open Database Licence)** used by OpenStreetMap means:
* you may use, share and adapt the data, even commercially;
* you must **credit**: "© OpenStreetMap contributors";
* if you publish an adapted **database**, it must also be under ODbL (**share-alike**); a map image made from it can be
  under other terms, but must keep the credit.

"Open" never means "no conditions". Boundary files may have their own licences and official status (disputed borders
are drawn differently by different sources — check that a map used in school follows the official Government of
Nepal map). Combine sources only if their licences are compatible, and list every credit on the map.

**Completeness is a data-quality question.** An empty area in OpenStreetMap may mean "nothing there" or "nobody mapped
it yet". Before concluding "this ward has no health post", check another source or local knowledge (Grade 8 Unit 8:
who is missing?).

**Planning a map project** — a one-page plan:
1. question (e.g. "Which palikas are more than 2 hours' walk from a health post?");
2. data layers with source, date and licence;
3. method (distances or travel times, rates, classes);
4. map design (type, classes, palette, missing data);
5. credits and limits.

### Activity (20 min)
1. Open <https://www.openstreetmap.org> and find your school. Is it mapped? Its name correct? Are nearby health posts
   mapped?
2. Write the full credit lines for a map using OSM roads, HDX district boundaries and ICIMOD glacial lakes.
3. Write a one-page map project plan for a question about your district.
4. (Optional, with internet and permission) Join a mapping task on the HOT Tasking Manager or fix your school's name in
   OSM with your teacher's account.

### Common mistakes
* Thinking "free to download" means "free to use without credit".
* Treating unmapped as absent.
* Mixing boundary versions from before and after 2015.

**Check (5 min).**
1. Credit line for OSM?
2. Does 'open' mean 'no conditions'?
3. Why check boundary licences?

**Reflect (2 min).** What surprised me? Who or what is missing from this data?

---

## Unit summary
* Latitude (N–S) and longitude (E–W) in decimal degrees; watch the order in file formats.
* 1° latitude ≈ 111 km; 1° longitude ≈ 111 × cos(latitude) km; haversine gives great-circle distance. In the hills,
  travel time matters more than distance.
* Choropleths: rates not counts; deliberate classes (equal, quantile, thresholds); sequential or diverging
  colour-blind-safe palettes; missing data distinct; area bias; small-number instability.
* Map data: OSM (ODbL, credit, share-alike), HDX boundaries, ICIMOD, USGS — check licences and official boundaries.
* Unmapped ≠ absent.

## Practice exercises
1. ★ Which of (27.7, 85.3) and (85.3, 27.7) is in Nepal? Where is the other?
2. ★ About how many km is 2° of latitude? 2° of longitude at 28° N?
3. ★ Write the OSM credit line.
4. ★★ Compute the straight-line distance between the eastern and western ends of Nepal (Kakarbhitta ≈ 26.65° N,
   88.15° E; Gaddachauki ≈ 28.96° N, 80.10° E). The East–West (Mahendra) Highway is about 1,000 km. Ratio?
5. ★★ Using the synthetic stations, find the station nearest to Kathmandu and the mean PM2.5 of all stations within
   150 km.
6. ★★ Ten districts have rates per 1,000: 12, 14, 15, 15, 16, 18, 22, 35, 60, 95. Make 4 equal-interval classes and 4
   quantile classes. How many districts fall in the top class each way?
7. ★★ A district with 4,000 people had 3 cases (75 per 100,000); a district with 2 million had 1,200 (60 per 100,000).
   Which rate do you trust more? How could a map show this?
8. ★★★ Explain why a map of Nepal's districts coloured by population density gives a different impression from one
   coloured by population count.
9. ★★★ Design a map to answer "Which schools in our municipality are furthest from a health post?" List layers,
   licences, method and limits.
10. ★★★ An app combines OSM data with its own private data and publishes a new database. What does ODbL require?

## Exercises with real data
**R1. Earthquakes on a map (RD-05).** Plot the 2015 USGS earthquakes as points (longitude, latitude) sized by
magnitude and coloured by date; add Kathmandu as a star. Where are most aftershocks relative to the main shock? Compute
each quake's distance from Kathmandu and make a histogram.
*Offline fallback:* the synthetic stations.

**R2. Glacial lakes (RD-14).** From ICIMOD's glacial lake inventory, plot lakes by longitude and elevation (or on a map
if coordinates are given). Which basin has the most potentially dangerous lakes? Credit ICIMOD with the DOI.

**R3. A real choropleth (RD-15 + RD-13).** With internet and `geopandas` installed, load HDX district boundaries, join
census population and households (check district names with a lookup table and a LEFT JOIN, Unit 2), and map average
household size with 5 quantile classes. Add the credits.

## Unit project: Where is it worst?
Follow **P**roblem · **P**lan · **D**ata · **A**nalysis · **C**onclusion. Choose a "where" question, plan layers and
licences, compute a rate or a distance, and produce one honest map (point or choropleth, printed or digital) with
classes and palette justified, missing data shown, credits complete, and a paragraph on what the map cannot show.
Full brief and rubric: `project.md`.

*If you use an AI assistant, follow the AI-use policy (explain, don't answer; disclose; be ready for an oral check).*

## Going further
* Kathmandu Living Labs (<https://kathmandulivinglabs.org>) and HOT Tasking Manager (<https://tasks.hotosm.org>):
  mapping projects in Nepal.
* Mark Monmonier, *How to Lie with Maps* (3rd ed., 2018).
* ColorBrewer (<https://colorbrewer2.org>): colour schemes designed for maps.
