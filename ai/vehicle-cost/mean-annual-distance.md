---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Mean annual distance

**Covers**: the class and era mean annual distance table, `MEAN_ANNUAL_KM` in
[evidence_data.py](../cost-balancing/evidence_data.py), and the workbook rows that use it.
Read this before changing an overhaul interval in kilometres, a fixed/per-km split, or any
row whose note states a mean annual distance.

## What the table is

The **mean annual distance** is the distance one vehicle of a class covers in a year. The
**reference duty** is the mean annual distance at which the annual total is split into the two
engine fields. "1900 money" is the general-index deflated value with 1900 = 100; the grade labels
MEASURED, DERIVED, ESTIMATE and UNAVAILABLE follow [claim-tags](../claim-tags.md). The
engine's overhaul trigger is a distance, so an overhaul interval measured or composed in years
becomes:

```
interval_km = interval_years x mean_annual_km
```

The same figure is the reference duty at which the continuous maintenance charge is split
between the fixed and per-kilometre fields:

```
per_km = (1 - fixed_share) x continuous_charge / mean_annual_km
```

At the reference duty the fixed and per-kilometre charges add to the continuous charge. A
measured row duty overrides the class/era value; the table is the reference for rows without
one.

## The table

All values are kilometres a vehicle-year in 1900 money where the cost is in 1900 money; the
distance itself is not deflated. The grade describes the distance evidence, not the cost.

| Class | Era | km a vehicle-year | Grade | Basis |
|---|---|---|---|---|
| Rail carriages | 1830-1889 | 35,000 | DERIVED | Pass 47 band: 210,000 km at six years. The measured 1892 range is 29,000-41,000 km ([report 44](../cost-balancing/research-pricing-report-44.md) section 4.3). |
| Rail carriages | 1890-1922 | 36,000 | DERIVED | Pass 47 band: 180,000 km at five years; inside the measured 1892 range. |
| Rail carriages | 1923-1947 | 55,000 | ESTIMATE | Pass 47 band: 165,000 km at three years. The measured 1961 range is 66,000-110,000 km; the 1920 and 1948 levels are not closed. |
| Rail carriages | 1948-1974 | 88,000 | DERIVED | Pass 47 band: 176,000 km at two years; inside the measured 1961 range. |
| Rail carriages | 1975-1999 | 120,000 | ESTIMATE | Pass 47 band: 240,000 km at two years. The 1983 Sprinter specification is 113,000 km a year; the 2026 long-distance estimate is 241,000. |
| Rail carriages | 2000-2026 | 113,000 | DERIVED | Pass 47 band: 294,000 km at 2.6 years; the 1983 measured value. |
| Rail wagons | 1900-2026 | 40,000 | ESTIMATE | Pass 46 reference duty; no measured annual wagon distance was found. The six-year overhaul at this duty is 240,000 km. [Report 52](../cost-balancing/research-pricing-report-52.md) confirms the 1972-81 repair-cost data are archive-only. |
| Rail locomotives | 1900-1947 | 40,000 | DERIVED | 1892 measured duty of 20,164 train-miles an engine (32,450 km); 1.25 engine-km per train-mile gives 40,560 km ([report 46](../cost-balancing/research-pricing-report-46.md) section 6). |
| Rail locomotives | 1948-1960 | 65,000 | ESTIMATE | Steam mixed-traffic central value. The 1950s express classes measured 155,600-168,000 km a year, the upper end of the range. |
| Rail locomotives | 1961-1989 | 113,000 | MEASURED | Class 47 on passenger duty, 1977 ([report 46](../cost-balancing/research-pricing-report-46.md)). |
| Rail locomotives | 1990-2026 | 150,000 | ESTIMATE | Central modern main-line duty. The long-distance bound in report 46 is 150,000 miles (241,000 km). |
| Multiple units | before 1960 | 100,000 | ESTIMATE | First-generation band in pass 42. No measured British annual distance for first-generation stock was found. |
| Multiple units | 1960-1999 | 120,000 | MEASURED (tube and metro); ESTIMATE (mainline) | Tube and metro stock ran about 120,000 km a car-year; the same value is the central mainline estimate. |
| Multiple units | 2000-2026 | 161,000 | DERIVED | 100,000 miles a car-year, the reference duty in [report 45](../cost-balancing/research-pricing-report-45.md) section 5 (160,934 km, rounded to 161,000). |
| Multiple units, tube and metro | all eras | 120,000 | MEASURED | London Underground, Docklands Light Railway and Tyne & Wear Metro stock; the measured duty is about 120,000 km a car-year. |
| Trams | 1900-1989 | 48,000 | DERIVED | [Report 47](../cost-balancing/research-pricing-report-47.md) reference duty: the measured 1930-31 municipal average of 46,200 km rounded to 48,000. [Report 49](../cost-balancing/research-pricing-report-49.md) uses the same duty for the repairs-only 1950-90 rung. |
| Trams | 1990-2026 | 90,000 | MEASURED | Nottingham Express Transit Citadis forecast annual mileage, the reference duty of the 2011 availability contract ([report 47](../cost-balancing/research-pricing-report-47.md)). |
| Buses and coaches | 1900-2026 | 55,000 | DERIVED | 220,000 km at the four-year overhaul in the class profile. The maintenance split reference is 40,000 km; the two figures are separate and both are stated where used. |
| Lorries | 1900-2026 | 40,000 | ESTIMATE | The workbook's split reference. The overhaul event distances are 80,000, 160,000 and 400,000 km; those are event intervals, not annual distances. |
| Vans | 1900-2026 | 40,000 (25,000 for short-duty vans) | ESTIMATE | The workbook's split references. |
| Cars and taxis | 1900-2026 | 40,000 | ESTIMATE | The workbook's split reference. |
| Ships | 1900-2026 | 115,000 | ESTIMATE | 575,000 km at the five-year special survey. The five-year survey is measured; the annual distance is an assumption. |
| Aircraft | 1900-2026 | 4,200,000 km per C-check | ESTIMATE | C-check every 4,000-6,000 flight hours at cruise. The table gives the event distance; annual utilisation varies by route and is not stated. |
| Maglev | 1900-2026 | 300,000 | ESTIMATE | Pass 50's assumed annual distance a vehicle. |

## Where the table is applied

- **Multiple units**: `wb_fv_pass59.py` applies 100,000 / 120,000 / 161,000 km to 707 rows.
  Tube, LUL, Underground, DLR, Docklands and Tyne & Wear stock take 120,000 km in every era.
- **Carriages**: `wb_fv_pass60.py` applies the six carriage bands to 758 standard-gauge rows.
  Passenger-rated wagons, multiple-unit stock, tube stock and the narrow gauge keep their own
  class rules.
- **Trams**: `wb_fv_pass58.py` and `wb_fv_pass61.py` apply 48,000 km to the historic rows and
  90,000 km to the modern rows. The six tram-sheet horses are on the animal rule from
  `wb_fv_pass57.py`.
- **Check**: `wb_distance_check.py` reports rows whose stated mean annual distance differs
  from the table by more than 10 per cent. The 1,524 rows with a stated mean (707 multiple
  units, 758 carriages, 59 trams) currently report no such deviation.

## Open questions

- **Carriage 1920 and 1950 levels.** [Report 51](../cost-balancing/research-pricing-report-51.md)
  gives 39 GBP a carriage-year in 1900 money for 1920 (band 28-55) and 121 for 1950; pass 62
  applied them. The table's distance values are independent of that question.
- **Locomotive 1914-1948 and after 1977.** [Report 50](../cost-balancing/research-pricing-report-50.md)
  supplied the measured levels; pass 63 applied the Class 92 override (a mixed-traffic class on
  the Caledonian Sleeper). The table's 65,000 and 150,000 km values remain estimates.
- **Road annual distances.** The 40,000 km figure is a split reference, not a measured fleet
  duty. A measured bus, lorry or van annual distance would replace the class assumptions.
- **Trams 1950-90.** The 150 GBP a car-year rung is a repairs-only estimate constrained by the
  measured Sheffield 1949-50 figure; no municipal repairs figure after 1950 was found
  ([report 49](../cost-balancing/research-pricing-report-49.md)).
- **Ship annual distance.** 115,000 km is an assumption derived from the five-year survey; a
  measured sea-days figure would replace it.
- **Aircraft annual utilisation.** The table gives the C-check distance, not a vehicle-year;
  a route mix or annual-hours figure would be needed for a per-year split.
