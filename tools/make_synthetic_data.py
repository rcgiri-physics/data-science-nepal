"""Generate the small SYNTHETIC practice tables shipped with the repo (CC0).

All numbers are INVENTED by a seeded random generator. They imitate the *structure* of real Nepali
datasets so lessons can run offline and with zero licence risk. District names are deliberately
fictional ("Hill-07") so nobody mistakes these numbers for real statistics. After running
tools/fetch_data.py for the real dataset, students can re-run the same notebook on real data.

Usage: python tools/make_synthetic_data.py   (deterministic; re-running gives identical files)
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DS = ROOT / "datasets"


def out(name: str) -> Path:
    p = DS / name / "clean"
    p.mkdir(parents=True, exist_ok=True)
    (DS / name / "raw").mkdir(exist_ok=True)
    (DS / name / "raw" / ".gitkeep").touch()
    return p


def census() -> None:
    rng = np.random.default_rng(2026)
    belts = ["Mountain"] * 16 + ["Hill"] * 39 + ["Terai"] * 22  # 77 districts, like real Nepal's count
    rng.shuffle(belts)
    prov_by_belt = {"Mountain": [1, 4, 6, 7], "Hill": [1, 3, 4, 5, 6, 7], "Terai": [1, 2, 3, 5, 7]}
    counters = {"Mountain": 0, "Hill": 0, "Terai": 0}
    rows = []
    for i, belt in enumerate(belts, start=1):
        counters[belt] += 1
        base = {"Mountain": 60_000, "Hill": 280_000, "Terai": 600_000}[belt]
        pop = int(rng.lognormal(np.log(base), 0.45))
        hh = int(pop / rng.uniform(4.0, 5.2))
        lo, hi = {"Mountain": (1500, 6000), "Hill": (600, 2500), "Terai": (800, 2500)}[belt]
        area = float(rng.uniform(lo, hi))
        female_share = {"Mountain": 0.53, "Hill": 0.54, "Terai": 0.51}[belt] + rng.normal(0, 0.01)
        female = int(pop * female_share)
        lit = {"Mountain": 66, "Hill": 77, "Terai": 70}[belt] + rng.normal(0, 4)
        absentee = int(pop * {"Mountain": 0.06, "Hill": 0.09, "Terai": 0.08}[belt] * rng.uniform(0.6, 1.4))
        rows.append(dict(
            district_id=i, district=f"{belt}-{counters[belt]:02d}", ecological_belt=belt,
            province=int(rng.choice(prov_by_belt[belt])), population=pop, households=hh,
            area_km2=round(area, 1), male=pop - female, female=female,
            literacy_pct=round(float(np.clip(lit, 40, 95)), 1), absentee_population=absentee))
    d = pd.DataFrame(rows)
    d.to_csv(out("census-districts") / "districts_synthetic.csv", index=False)

    schools = []
    for r in d.itertuples():
        n = max(5, int(r.population / rng.uniform(900, 1700)))
        enrol = int(r.population * rng.uniform(0.17, 0.23))
        girls = int(enrol * rng.uniform(0.46, 0.53))
        schools.append(dict(district_id=r.district_id, n_secondary_schools=n,
                            enrolment_girls=girls, enrolment_boys=enrol - girls))
    pd.DataFrame(schools).to_csv(out("census-districts") / "schools_synthetic.csv", index=False)


def air() -> None:
    rng = np.random.default_rng(7)
    days = pd.date_range("2019-01-01", "2020-12-31", freq="D")
    doy = days.dayofyear.to_numpy()
    season = 55 + 45 * np.cos((doy - 15) * 2 * np.pi / 365)  # high in winter, low in monsoon
    pm25 = np.clip(season + rng.normal(0, 14, len(days)), 5, None)
    weekend = np.asarray(days.dayofweek >= 5)
    pm25 = pm25 * np.where(weekend, 0.93, 1.0)
    df = pd.DataFrame({"date": days.strftime("%Y-%m-%d"), "pm25": pm25.round(1)})
    df["pm10"] = (df.pm25 * rng.uniform(1.4, 1.9, len(df))).round(1)
    # realistic messiness for the cleaning lesson
    miss = rng.choice(len(df), 25, replace=False)
    df.loc[miss, "pm25"] = np.nan
    bad = rng.choice(len(df), 4, replace=False)
    df.loc[bad, "pm25"] = -999  # sensor error code
    df.to_csv(out("kathmandu-air-quality") / "air_daily_synthetic.csv", index=False)


def climate() -> None:
    rng = np.random.default_rng(11)
    rows = []
    for year in range(1991, 2021):
        for m in range(1, 13):
            t = 18 + 8 * np.sin((m - 4) * np.pi / 6) + 0.03 * (year - 1991) + rng.normal(0, 0.8)
            monsoon = {6: 280, 7: 480, 8: 430, 9: 250}.get(m, 25)
            rain = max(0.0, rng.gamma(4, monsoon / 4))
            rows.append(dict(year=year, month=m, mean_temp_c=round(float(t), 2), rain_mm=round(float(rain), 1)))
    pd.DataFrame(rows).to_csv(out("climate-monthly") / "climate_monthly_synthetic.csv", index=False)


def health() -> None:
    rng = np.random.default_rng(5)
    n = 1500
    belt = rng.choice(["Mountain", "Hill", "Terai"], n, p=[0.1, 0.45, 0.45])
    wealth = rng.integers(1, 6, n)
    age = rng.integers(16, 43, n)
    base = np.select([belt == "Mountain", belt == "Hill"], [-0.6, 0.0], 0.1)
    z = -0.2 + base + 0.45 * (wealth - 3) + rng.normal(0, 0.8, n)
    anc = np.clip(np.round(3.2 + 0.8 * z + rng.normal(0, 0.9, n)), 0, 8).astype(int)
    inst = (rng.random(n) < 1 / (1 + np.exp(-(0.5 * z + 0.15 * anc - 0.5)))).astype(int)
    bw = np.clip(2.75 + 0.07 * (wealth - 3) + 0.04 * anc + rng.normal(0, 0.4, n), 1.2, 4.5).round(2)
    pd.DataFrame(dict(record_id=np.arange(1, n + 1), ecological_belt=belt, mother_age=age,
                      wealth_quintile=wealth, antenatal_visits=anc, institutional_delivery=inst,
                      birth_weight_kg=bw)).to_csv(out("health-synthetic") / "health_synthetic.csv", index=False)


def survey() -> None:
    rng = np.random.default_rng(8)
    n = 36
    mode = rng.choice(["walk", "bus", "bicycle", "motorbike"], n, p=[0.55, 0.2, 0.15, 0.1])
    minutes = np.where(mode == "walk", rng.integers(5, 55, n),
                       np.where(mode == "bicycle", rng.integers(5, 35, n), rng.integers(8, 45, n)))
    pd.DataFrame(dict(student_code=[f"S{i:02d}" for i in range(1, n + 1)],
                      travel_mode=mode, travel_minutes=minutes,
                      siblings=rng.integers(0, 6, n), sleep_hours=np.round(rng.normal(8, 1, n), 1),
                      height_cm=rng.integers(138, 172, n),
                      favourite_subject=rng.choice(["Maths", "Science", "English", "Nepali", "Social"], n)
                      )).to_csv(out("class-survey-synthetic") / "class_survey_synthetic.csv", index=False)


if __name__ == "__main__":
    for fn in (census, air, climate, health, survey):
        fn()
    print("synthetic tables written under datasets/*/clean/")
