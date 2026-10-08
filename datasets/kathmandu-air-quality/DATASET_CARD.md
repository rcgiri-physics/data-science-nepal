---
name: kathmandu-air-quality
source_url: https://opendatanepal.com/dataset/air-quality-data-in-kathmandu
publisher: Open Data Nepal (author Hel Nershing Thapa; upstream OpenAQ) - REAL; folder
  ships SYNTHETIC look-alike
licence: 'Synthetic table: CC0. Real dataset: CC BY-SA per ODN listing (check OpenAQ
  upstream terms)'
licence_status: synthetic-cc0
date_accessed: '2026-10-07'
grades:
- 9
- 10
- 11
synthetic: true
redistribution_allowed: true
---

# Kathmandu air quality (SYNTHETIC practice table)

**SYNTHETIC: invented daily PM2.5 / PM10** for 2019-2020, shaped like a Kathmandu year (high in winter,
low in monsoon). It is deliberately **messy**: 25 missing PM2.5 values and 4 sensor error codes (`-999`).

## Columns
`date` (YYYY-MM-DD), `pm25` (ug/m3), `pm10` (ug/m3).

## Real data
Real series (Jan 2015 - Mar 2021; PM2.5, PM10, O3, SO2, NO2, CO, BC; CSV about 8.3 MiB) - see `source.yml`.

## Ethics / limits
Single-station air data is not "the city's air". Discuss health guidance thresholds from the WHO/Nepal standard
only after reading the current official values.
