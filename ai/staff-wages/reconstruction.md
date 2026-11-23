---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Staff wage reconstruction, 2026-11-23

**Covers**: how the seven `staff.tab` series were rebuilt from the measured rows in
[evidence-1914-1946](evidence-1914-1946.md), [post-1980](post-1980.md) and
[staff-wages](../staff-wages.md), the engine conversion from annual wages to monthly Simucents,
and the status (measured, derived or estimated) of every anchor.

Read with [staff-wages](../staff-wages.md) for the pre-1980 register and the 1901-1968 official
tables, [post-1980](post-1980.md) for the New Earnings Survey 1980 anchor, the ASHE annual
series and the 2026-2050 projection, and [vehicle-cost-model](../vehicle-cost-model.md) for the
engine's monthly scaling.

Review workbook: `New/staff-wages.xlsx` (README, Params, Measured rows, ASHE, Reconstruction,
Old vs new, Comparators, Table 50, NES, Gaps). It is a review aid; the evidence and status in
this document govern.

## 1. The engine basis

`config/staff.tab` holds a monthly salary per person per staff type, in Simucents. The engine:

- interpolates linearly between the listed years and clamps at both ends
  (`karte_t::get_staff_salary`);
- charges the salary per person per month, for the staff a vehicle declares, and passes the
  total through `calc_adjusted_monthly_figure` (`convoi_t::get_salaries`).
  `[CODE simutrans-extended ex-15]`

At `bits_per_month = 22` and `meters_per_tile = 125` the monthly factor is
`2^(22-18) / (1000/125) = 2`. `[CODE New ex-15]`

### The conversion

The series is compiled as **nominal annual wages in old pence** (240 to the pound).

- 1 old penny = £1/240 = 0.4167 new pence.
- 1 new penny = 192 Simucents at the revenue rate (£1 = 100 new pence; 1 Simucent =
  £0.00005208).
- Therefore 1 old penny = 0.4167 × 192 = **80 Simucents**.
- Annual wage W old pence = 80W Simucents a year = 80W/12 = 6⅔W Simucents a month.
- The engine doubles the monthly figure, so the stored value is half: **W × 10/3**.

The 2026-11-23 rebuild corrected a file that held the annual-pence values without this
conversion, so the engine charged 3/10 of the annual figure it stored. The 1907 driver, for
example, was stored as 14,848 and charged as £17.28 a year; the stored annual figure was £61.87,
and the measured driver rate was £104. The file now stores 83,200 and charges £104.
`[CODE New ex-15; arithmetic]`

The 2030-2050 projection is rebuilt on the new 2026 anchor and checked by converting every
stored value back: stored × 3/10 / 240 is the annual pound figure, and stored × 3/10 / 624 the
implied weekly rate. The ×10/3 conversion is applied exactly once. See
[post-1980](post-1980.md) section 4.

## 2. The seven series

All values below are annual old pence, before the ×10/3 conversion. "Measured" means a wage
rate or earnings figure in a cited source; "derived" means a measured figure multiplied by a
measured ratio; "estimated" means an assumption, labelled as such. Post-1980 points are
measured, derived or projected as set out in [post-1980](post-1980.md) section 5; the tables
below carry the pre-1980 evidence and the post-1980 endpoints.

### staff[0] — Train/engine driver

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1710-1850 | 7,409-16,139 | derived | general labourer × 1.5; the 1907 driver/labourer ratio |
| 1851-1891 | 16,139-22,565 | derived | labourer × 1.5 at the Williamson points |
| 1901 | 24,804 | derived | labourer 1901 × 1.5 |
| 1907 | 24,960 | measured | 40s a week; Board of Trade railway enquiry |
| 1914 | 25,272 | measured | 40s 6d a week; Hansard 1962 table |
| 1920 | 60,528 | measured | 97s a week, mid-point of 88-106s; Hansard 1962 |
| 1922 | 50,544 | measured | 81s a week, mid-point of 72-90s; Hansard 1922 |
| 1925 | 50,544 | measured | 81s a week, mid-point of 72-90s; Hansard 1925 |
| 1930 | 50,544 | measured | 81s a week, mid-point of 72-90s; Hansard 1962 |
| 1940 | 56,784 | measured | 91s a week, mid-point of 85-97s; Hansard 1962 |
| 1950 | 81,744 | measured | 131s a week, mid-point of 124-138s; Hansard 1962 |
| 1961 | 149,760 | measured | 240s a week, mid-point of 220-260s; Hansard 1962 |
| 1962 | 157,167 | differential-derived | 1961 driver/BR-average ratio (240/283) × 1962 BR average 297s |
| 1964 | 173,573 | differential-derived | same ratio × 1964 BR average 328s |
| 1966 | 220,142 | differential-derived | same ratio × 1966 BR average 416s |
| 1968 | 231,785 | differential-derived | same ratio × 1968 BR average 438s; 371.4s a week |
| 1980 | 1,437,696 | measured | NES April 1980, £115.20 a week; see [post-1980](post-1980.md) |
| 1982 | 1,893,216 | measured | NES April 1982, £151.70 a week |
| 1985 | 2,392,416 | measured | NES April 1985, £191.70 a week |
| 1988 | 3,101,280 | measured | NES April 1988, £248.50 a week |
| 1995 | 4,828,512 | measured | NES April 1995, £386.90 a week |
| 1999-2026 | 6,133,680-17,729,664 | measured | ASHE median, SOC 882/3514/8231 |
| 2030-2050 | 19,951,181-29,646,359 | projection | 2026 real pay × the general index |

### staff[1] — Fireman

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1710-1850 | 4,099-8,930 | derived | labourer × 0.83 |
| 1851-1891 | 8,930-12,486 | derived | labourer × 0.83 at the Williamson points |
| 1907 | 14,820 | measured | 23s 9d a week |
| 1914-1968 | 0.594 × driver | derived | the 1907 fireman/driver ratio; 1962-1968 use the 1961 ratio × Table 50 |
| 1980-2050 | 0.594 × driver | estimated | held for heritage steam; no fireman grade after 1968 |

The 1907 ratio is not independently verified after 1930. The 1962 passenger-porter series rose
faster than the driver rate, so the 0.594 ratio may understate the fireman in 1950-1968; a
measured fireman rate is an open gap.

### staff[2] — Guards

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1710-1850 | 3,408-7,424 | derived | labourer × 0.69 |
| 1851-1891 | 7,424-10,380 | derived | labourer × 0.69 at the Williamson points |
| 1907 | 17,264 | measured | passenger guard 27s 8d a week |
| 1914-1968 | 0.69 × driver | derived | the 1907 passenger-guard/driver ratio; 1962-1968 use the 1961 ratio × Table 50 |
| 1980 | 1,120,871 | derived | 0.780 × driver, the measured 1999 ASHE guard/driver ratio |
| 1982 | 1,476,008 | derived | 0.780 × driver |
| 1985 | 1,865,199 | derived | 0.780 × driver |
| 1988 | 2,417,851 | derived | 0.780 × driver |
| 1995 | 4,037,280 | measured | NES April 1995, rail inspectors, supervisors and guards, £323.50 a week |
| 1999-2026 | 4,782,000-11,563,128 | measured | ASHE median, SOC 881/6215/6214 |
| 2030-2050 | 13,011,981-19,335,090 | projection | 2026 real pay × the general index |

The goods guard was 28s 2d in 1907, 0.704 of the driver; the passenger guard is used because
the engine has one guard type. The NES 1980 table has no guard row, so the 1980 point is a
ratio of the driver rather than a measured guard figure.

### staff[3] — Carriage attendants

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1750-1850 | 4,940-10,676 | estimated | general labourer; no attendant grade before the dining car |
| 1896 | 15,600 | measured | £195 a year for three dining-car staff, £65 each |
| 1907-2050 | 0.65 × driver | derived | the 1896-1907 attendant/driver ratio |

The post-1930 0.65 ratio is an assumption; no measured attendant rate was found after 1896, and
the ratio gives £48,018 a year in 2026, which is above any catering wage. This is the least
supported line in the file; see [post-1980](post-1980.md) section 6.

### staff[4] — General labourer

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1710-1911 | 4,613-17,770 | measured | Williamson 1982, annual earnings |
| 1946 | 52,416 | measured | platelayer 84s a week |
| 1950 | 66,560 | measured | local authority labourer 106s 8d; Hansard 1962 |
| 1961 | 118,872 | measured | local authority labourer 190s 6d; Hansard 1962 |
| 1968 | 183,979 | differential-derived | 1961 labourer/BR-average ratio (190.5/283) × 438s = 294.8s |
| 1980 | 1,173,120 | measured | NES April 1980, general labourers, £94.00 a week |
| 1982 | 1,411,488 | measured | NES April 1982, general labourers, £113.10 a week |
| 1985 | 1,672,320 | measured | NES April 1985, general labourers, £134.00 a week |
| 1988 | 2,075,424 | measured | NES April 1988, general labourers, £166.30 a week |
| 1990 | 2,569,632 | measured | NES April 1990, other building and civil engineering labourers, £205.90 a week |
| 1992 | 2,917,824 | measured | NES April 1992, other building and civil engineering labourers, £233.80 a week |
| 1995 | 3,122,496 | measured | NES April 1995, other building and civil engineering labourers, £250.20 a week |
| 1999-2026 | 3,376,080-6,642,048 | measured | ASHE median, elementary construction occupations |
| 2030-2050 | 7,474,293-11,106,389 | projection | 2026 real pay × the general index |

The Williamson series is a general labourer, not a railway labourer. The 1907 railway
locomotive, carriage and wagon labourer rate was 20s a week, below the general labourer's
27.7s. The pakset's staff type is a general labourer, so the general series is used. From 1999
the proxy is ASHE elementary construction occupations rather than farm workers, because the
pre-1980 series is a building and general labourer and the NES 1980 anchor is general
labourers; farm workers are a different and lower-paid trade.

### staff[5] — Tram/bus driver

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1750-1850 | 7,410-16,014 | estimated | general labourer × 1.5; horse omnibus driver |
| 1890 | 18,720 | measured | 30s a week, Gladwin |
| 1906 | 19,708 | measured | 31s 7d a week, Board of Trade |
| 1914 | 19,384 | measured | 31s 1d a week; Hansard 1962 |
| 1920 | 46,124 | measured | 73s 11d a week; Hansard 1962 |
| 1925 | 36,920 | measured | 59s 2d a week; Hansard 1925 |
| 1930 | 37,648 | measured | 60s 4d a week; Hansard 1962 |
| 1940 | 45,552 | measured | 73s 0d a week; Hansard 1962 |
| 1950 | 72,436 | measured | 116s 1d a week; Hansard 1962 |
| 1961 | 128,492 | measured | 205s 11d a week; Hansard 1962 |
| 1968 | 198,867 | differential-derived | 1961 road-driver/BR-average ratio (205.9/283) × 438s = 318.7s |
| 1980 | 1,465,152 | measured | NES April 1980, bus and coach drivers, £117.40 a week |
| 1982 | 1,792,128 | measured | NES April 1982, £143.60 a week |
| 1985 | 2,142,816 | measured | NES April 1985, £171.70 a week |
| 1988 | 2,388,672 | measured | NES April 1988, £191.40 a week |
| 1990 | 2,700,672 | measured | NES April 1990, £216.40 a week |
| 1992 | 2,929,056 | measured | NES April 1992, £234.70 a week |
| 1995 | 3,038,880 | measured | NES April 1995, £243.50 a week |
| 1999-2026 | 3,213,840-8,143,080 | measured | ASHE median, SOC 873/8213/8212 |
| 2030-2050 | 9,163,403-13,616,314 | projection | 2026 real pay × the general index |

The 1956 and 1962 London Transport road-staff averages are no longer used: the 1962 table gives
a national rate for 39 large towns, and the London averages are about 50 per cent higher. The
1980 NES figure is close to the driver's, and the two diverge sharply after 1986: by 2026 the
bus driver earns 46 per cent of the train driver, against 102 per cent in 1980.
`[arithmetic]`

### staff[6] — Tram/bus conductor

| Year | Annual old pence | Status | Basis and source |
|---:|---:|---|---|
| 1750-1850 | 4,940-10,676 | estimated | general labourer |
| 1890 | 12,480 | measured | 20s a week, Gladwin |
| 1900 | 17,472 | measured | 28s a week, Leeds |
| 1906 | 18,096 | measured | 29s a week, Board of Trade |
| 1914 | 17,368 | measured | 27s 10d a week; Hansard 1962 |
| 1920 | 44,044 | measured | 70s 7d a week; Hansard 1962 |
| 1925 | 33,966 | derived | 0.92 × bus driver |
| 1930 | 35,620 | measured | 57s 1d a week; Hansard 1962 |
| 1940 | 43,576 | measured | 69s 10d a week; Hansard 1962 |
| 1950 | 70,044 | measured | 112s 3d a week; Hansard 1962 |
| 1961 | 125,268 | measured | 200s 9d a week; Hansard 1962 |
| 1968 | 193,878 | differential-derived | 1961 conductor/BR-average ratio (200.75/283) × 438s = 310.7s |
| 1980 | 1,305,408 | measured | NES April 1980, bus conductors, £104.60 a week |
| 1980-2050 | 0.891 × bus driver | derived | the measured 1980 conductor/driver ratio, held |

No conductor grade survives in ASHE, so the ratio is held to 2050 for heritage vehicles.

## 3. What changed

| Grade | Old file, 1906/1907 | New file, 1907 | Factor | Old 2026 | New 2026 | Factor |
|---|---:|---:|---:|---:|---:|---:|
| Driver | 14,848 | 83,200 | 5.60 | 10,075,443 | 59,098,880 | 5.87 |
| Fireman | 9,267 | 49,400 | 5.33 | 6,716,962 | 35,104,735 | 5.23 |
| Guard | 9,267 | 57,547 | 6.21 | 6,716,962 | 38,543,760 | 5.74 |
| Carriage attendant | 9,267 | 54,080 | 5.84 | 6,716,962 | 38,414,272 | 5.72 |
| General labourer | 9,587 | 57,588 | 6.01 | 6,045,266 | 22,140,160 | 3.66 |
| Tram/bus driver | 14,848 | 65,433 | 4.41 | 10,075,443 | 27,143,600 | 2.69 |
| Tram/bus conductor | 9,267 | 60,095 | 6.49 | 6,716,962 | 24,184,161 | 3.60 |

The 1907 change is the ×10/3 engine conversion (3.33) times the move from an all-grades railway
average to the measured driver rate (1.68), with the grade ratios correcting the rest. The 2026
column is the same conversion applied to the ASHE medians.

The 2026-11-23 post-1980 pass left the 2026 endpoints almost unchanged (driver, fireman,
attendant and bus driver under 0.01 per cent; guard 0.03), because 2019 and 2026 were already
ASHE medians. Two moved: the labourer +2.5 per cent, from the move to elementary construction
occupations, and the conductor +11.4 per cent, from the measured 1980 ratio replacing 0.80. The
1980-1999 bridge was then replaced by the measured NES years 1982, 1985, 1988, 1990, 1992 and
1995; the 1999 endpoints did not move.

At 1980 the driver falls from £7,424 a year to £5,990, the bus driver rises from £5,197 to
£6,105, the labourer from £4,454 to £4,888 and the conductor from £4,157 to £5,439: the previous
values were of unverified provenance and are replaced by the NES survey.

## 4. What is measured, derived and estimated

**Measured:** the 1906 tram rates; the 1907 railway grades; the 1914, 1920, 1922, 1925, 1930,
1940, 1950 and 1961 railway driver rates; the 1914-1961 road driver and conductor rates; the
1946 platelayer and signalman rows; the 1950 and 1961 local authority labourer rates; the
British Rail averages 1962-1968; the NES 1980-1995 means for the grades in
[post-1980](post-1980.md) section 3; the ASHE medians 1999-2026.

**Derived:** the pre-1901 driver, fireman and guard from the general labourer × the 1907
ratios; the fireman, guard and attendant 1914-1968; the 1925 road conductor; the 1962-1968 grade
points; the 1980 guard, fireman, attendant and conductor; the guard 1982-1988; the conductor on.

**Estimated:** the pre-1850 horse omnibus driver; the years between the measured NES dates
(1981, 1983-84, 1986-87, 1989, 1991, 1993-94, 1996-98); the fireman after 1930; the carriage
attendant after 1896; the 2030-2050 projection.

The order of value for further work:

1. Transcribe the remaining NES years from S18 (1981, 1983-84, 1986-87, 1989, 1991, 1993-94,
   1996). 1996 would close the 1995-1999 gap; 1990 and 1992 cannot be closed, having no row.
2. A measured 1968 driver and bus-driver rate. The 1968 points are differential-derived from
   the 1961 rate/BR-average ratio and Table 50.
3. A carriage-attendant rate, or a decision that the type is a catering grade and should use a
   catering ratio instead of 0.65 of the driver.
4. A measured fireman rate for 1930-1968; the 1907 ratio may understate the lower grades after
   the driver/porter differential narrowed.

## 5. Open questions

- Is the revenue timescale the right one for staff? The file uses the revenue rate
  (192 Simucents = 1 new penny). On the capital rate the same stored values would charge
  76 times as much. The engine has one currency; the choice is a pakset convention, not an
  engine property.
- Should the engine's monthly factor apply to staff at all? It does, through
  `calc_adjusted_monthly_figure`; the file is built for that behaviour. If the engine is
  changed to stop doubling staff, every value must be doubled.
- Should the driver be paid the rate or the earnings? The file uses earnings, because that is
  what ASHE measures and what the engine's fixed monthly wage most nearly represents. The
  consequence is that 1967-1998 is a rate series joined to an earnings series at 1980, so the
  1968-1980 segment rises by the rate-to-earnings step as well as by the wage settlement.
- Should the 1980 anchor be full-time male mean earnings while 1999-2026 is an all-employee
  median? The mean/median gap is under 2 per cent for the grades used; the full-time share is
  the larger difference and is not corrected.
- **Do we need an engine change to record staff numbers in buildings as well as in vehicles?**
  This is the open question for signalboxes and ATC. `staff.tab` is charged only through
  `convoi_t::get_salaries`; `building_desc_t`, `simhalt.cc` and `gebaeude.cc` have no staff
  field, so a signalbox or airport cannot declare staff. Signalbox staff are already inside the
  signalbox maintenance (the 1909 evidence is £150 a year to man a small box with two men and
  maintain the signals), and the control-tower/airport maintenance is a building cost. A
  separate signaller or ATC `staff[i]` series would therefore be inert, and could double-count
  if the building maintenance is not split. If the pakset wants separate staff numbers and
  wages for buildings, the engine needs a building staff field and a charge path first; the
  signaller wage series is ready (1907, 1909, 1914-25, 1946, modern ASHE rail operatives), but
  an ATC series would need NATS/CAA data. This is an engine change, not a `staff.tab` change.
- How many hours is a weekly rate? The sources rarely state hours. The 1907 rate is for
  "full ordinary time"; the 1946 rows are for an 8-hour shift; the tram rows are 64-hour
  weeks. The game charges per month regardless of hours, so the weekly rate is treated as a
  full-time week.
