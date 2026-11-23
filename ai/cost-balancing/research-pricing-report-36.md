# Overhaul and upgrade costs, British rail vehicles, 1830-2026

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 23 November 2026.

## 1. Method

- Nine Exa searches, one per turn, each naming the subject, the constraint, the date window and a
  source preference. Every figure below was read on the fetched page or the extracted PDF, not from
  a search highlight alone.
- PDFs were downloaded to `ai/temp/pdfs/` and text-extracted with `pypdf`. Two PDFs (`BR-1956-OCR`,
  the docslib book appendix) yielded no text layer and were abandoned.
- **No Simutrans `.dat` value, runningcost, fixed_cost, overhaul or upgrade figure was read, and no
  pakset price enters any ratio here.** Every ratio is between two historical figures.
- Nothing was converted: money is nominal of the year stated, distances as printed (miles unless
  the source says km), time as printed (days, weeks, months, years).
- Tags: **MEASURED** = an account, record card or contract figure; **STATED** = an engineer's or
  historian's statement; **COMPUTED** = my division of two stated figures, said so in the row;
  **ESTIMATE** = my judgement, used only in section 6.
- Deliberately not re-found: Hill 1892 (£253 per engine-year, ~12 per cent of purchase price a
  year), BR Class 52, Aldenham bus overhaul, Hill's £18-45 carriage figure.

## 2. What the evidence supports, in one page

| Class | Best interval | Best cost | Confidence |
|---|---|---|---|
| Steam locomotive, general repair | 104,000-196,000 miles (BR Pacifics 1951-60); 165,000 miles (Royal Scot, 1941); ~74,000-84,000 miles (GWR 28xx boiler exchanges) | £450-£700 heavy general, GWR 28xx, 1930s | MEASURED, strong |
| Steam locomotive, heavy general with boiler exchange | 20-41 months (BR Pacifics) | boiler is 19-27 per cent of locomotive capital; boiler overhaul £150-£700 | MEASURED, strong |
| Steam locomotive, works downtime | 31-53 days (BR Pacifics); 18-21 days (L&YR 1920, classes A/B) | — | MEASURED, strong |
| Diesel/electric locomotive | three overhauls at 2.75, 5.5 and 11 years (BR, 1996) | no per-overhaul money found | STATED, strong on interval, nil on cost |
| Carriage | full vehicle overhaul about every 2 years (BR InterCity, 1996); Midland 1860s overhaul at 25-28 per cent of capital | £62 per carriage (1860s); £100,840-£325,000 per coach (2012-15 refurbishment) | MEASURED, moderate |
| Wagon | works visit about every 9 months (Midland, 1860s-80s) | none found | STATED, weak |
| Multiple unit | C4/C6 cycle; modern refresh 6 days-12 weeks in works | £100,000-£500,000 per vehicle (refresh to re-tractioning) | MEASURED, strong for 2012-25 |

## 3. Overhaul intervals

### 3.1 Steam locomotives

**BR Pacifics, 1951-1960 (MEASURED).** Landau's transcription of the National Railway Museum's
ten-year Class 8 boiler record gives miles and months per general repair and days on works. At a
general repair the boiler was lifted and exchanged for a repaired or new one.

| Class | Miles per general repair | Months per general repair | Days on works |
|---|---|---|---|
| Princess Royal | 169,808 | 32.0 | 45 |
| Duchess | 195,993 | 32.7 | 39 |
| A1 | 122,789 | 20.9 | 31 |
| A4 | 107,257 | 19.6 | 35 |
| Merchant Navy | 195,934 | 40.9 | 53 |
| King | 104,261 | 24.6 | 40 |

The spread is 104,000-196,000 miles and 20-41 months: a factor of two between the most and least
intensively worked classes, on the same maintenance philosophy. The LMS pair and the Southern
Pacific sit at the top, the LNER and GWR Pacifics at the bottom.

**GWR 28xx No. 2874, 1918-1963 (MEASURED).** The engine record card (The National Archives, Kew),
as published by the 2874 Trust, gives every boiler exchange with the locomotive mileage at the time.
Fifteen exchanges over 1,258,517 miles, 44.5 years:

- mean interval between exchanges **83,901 miles (COMPUTED)**;
- mean annual mileage **28,310 miles (COMPUTED)**;
- shortest interval 38,349 miles (1952-54), longest 109,463 miles (1933-36).

This is a heavy-freight 2-8-0 on medium-mileage work, so it sits below the Pacific figures, as it
should.

**Royal Scot, 1941 (MEASURED, component scope).** In the discussion of an IMechE paper an engineer
records that on the three-cylinder Royal Scot the valve gear needed "service repairs averaging
65,000 miles" and "general repairs, every 165,000 miles". The valve gear alone cost £20 at a
service repair and £33 at a general repair, departmental cost including material. Two interval
figures and two component costs, not a whole-locomotive overhaul cost.

**Midland Railway, 1849 (MEASURED, component lives).** Kirtley's report of July 1849, quoted by
Summerson, gives the working lives used for depreciation: boiler tubes 75,000 miles, fireboxes
150,000 miles, boilers 300,000 miles, "working out at ¾d per mile depreciation". In the same report,
120 engines on hand, 58 wanting repairs.

**Pre-grouping practice.** The Derby works description of 1893 (Jones) says "an engine will run
eighteen months or two years with slight repairs. A boiler, which is the most costly item, lasts on
an average fifteen years". That gives the light-repair cycle in time (18-24 months) and the boiler
life (15 years) for the 1890s.

**BR's own view of the interval, 1953 (STATED).** Bond's paper and the discussion of it are the
authority for the classified repair system: light intermediate, intermediate, general and heavy
general. Cook's contribution says he was "rather perturbed to see that so many engines of certain
main line classes required general or intermediate repair at considerably less than 40,000 miles" —
so 40,000 miles is a floor for a main-line intermediate, not a target. Bond's own class averages,
quoted through SteamIndex, run from 55,616 to 93,363 miles between repairs.

### 3.2 Diesel and electric locomotives

**BR, 1996 (STATED, ministerial answer).** Hansard, 11 March 1996, vol. 273: "Locomotive overhaul is
also based on hours in traffic, but the regime consists of three types of overhaul occurring
approximately at two and three-quarter, five and a half and 11-year intervals respectively." The
same answer gives the coaching stock cycle: "progressively larger examinations at one, three, six
and 12-monthly intervals. The full vehicle overhaul is mileage based, but occurs approximately every
two years."

This is the cleanest single statement of the BR classified overhaul cycle for both traction and
coaches, and it is a government answer drawing on BR's vehicle maintenance and overhaul
instructions.

**Class 47 examinations (MEASURED, 1970s).** Calder, of Brush, gives the Class 47 inspection
intervals as 55, 275, 825, 2,500 and 5,000 engine hours. The 5,000-hour examination is the top of
the depot ladder, below works overhaul.

**Engine life between overhauls (MEASURED, 1998).** Railway Gazette International, May 1998, on the
Class 57: the GM 645 engine "has an average service life of 25 to 30,000h between overhauls,
compared with 10 to 12,000h for the 30-year old Sulzers". That is the single best measured statement
of why re-engining paid: the overhaul interval more than doubles.

### 3.3 Carriages and wagons

- **Carriages, BR 1996:** full overhaul about every 2 years (above).
- **Carriages, Midland 1860s:** 50 composite carriages "accepted for repairing, repainting and
  retrimming" at £62 each, recorded by Lacy and Dow. The interval is not stated; the ratio is.
- **Wagons, Midland 1860s-80s (STATED, secondary):** the Carriage and Wagon Committee's six-monthly
  repair returns imply "the average time between works visits was around nine months". Wagons were
  not called in on a schedule but on examination, with General and Intermediate Repair dates carried
  on cast plates.
- **Wagons, BR 1947 (MEASURED):** 182,082 railway-owned and requisitioned wagons under or awaiting
  repair on 22 November 1947, "about half required major repairs". Fleet ~1.18m. That is a stock
  measure, not an interval, but it shows roughly 15 per cent of the fleet in repair at any time.

### 3.4 Multiple units

No pre-1994 classified-repair statement was found. The modern evidence is programme-based:

- Class 455: C6 overhaul plus re-tractioning, "installation will take only six days"; the
  re-tractioning raises the maintenance interval from 16,000 km to about 24,000 km.
- Class 458: "taking two weeks to complete each set".
- Class 185: mid-life refresh, the trade press headline is "How to Refit a Train in 9 Days".
- Class 313: C6 overhaul of 19 units at Wolverton, 2017 (no price, no duration given).

## 4. Overhaul cost in money

### 4.1 Steam

| Year | Class | Item | Cost | Scope | Source | Tag |
|---|---|---|---|---|---|---|
| 1849 | Midland, 120 engines | general repairs, six months to June 1849 | £19,306 | fleet | Kirtley report via Summerson | MEASURED |
| 1849 | Midland | new tubes, fireboxes and boilers, same half-year | £2,490 | fleet | as above | MEASURED |
| 1849 | Midland | per engine actually repaired (19,306/58) | £333 | individual | COMPUTED | COMPUTED |
| 1930s | GWR 28xx | heavy general | £450-£700 | individual | 2874 Trust, engine record card | MEASURED |
| 1930s | GWR 28xx | boiler overhaul | £150-£700 | individual | as above | MEASURED |
| 1920s | GWR standard No. 1 boiler | new boiler | £971 | individual | as above | MEASURED |
| 1953 | BR1 (Britannia) boiler | new boiler | £6,193 | individual | Landau, from Cook | MEASURED |
| 1941 | Royal Scot | valve gear at service repair / general repair | £20 / £33 | component | IMechE discussion | MEASURED |

The Midland 1849 division is the only pre-1900 per-engine overhaul money found. It must be read with
care: 58 of 120 engines wanted repairs, the figure is a half-year, and it includes everything from
light to heavy. £333 per engine repaired in 1849 is roughly 12-15 per cent of a locomotive's cost at
the time, which agrees with Hill's 1892 finding that repairs ran at about 12 per cent of purchase
price a year.

The GWR pair is the strongest single figure in the whole pass: a named class, a named works, a
stated scope ("heavy general"), and a range that brackets the difference between a straightforward
heavy general and one with a firebox renewal.

### 4.2 Diesel, electric and modern traction

No measured per-overhaul money figure for a BR diesel or electric locomotive was found. The
published numbers are all per-mile or per-year maintenance costs (Calder's Class 47 at $69,100 a
year in freight and $135,500 in passenger service; Bradley's Southern Region 2.87d-5.06d per mile
for 1954-55), which cannot be turned into an overhaul price without an assumption about how much of
the annual cost is the overhaul. They are recorded here as context only.

What does exist is the cost of the *rebuild*, which is a different and larger event (section 5).

### 4.3 Carriages, wagons, multiple units

| Year | Item | Cost | Basis | Source | Tag |
|---|---|---|---|---|---|
| 1860s | Midland composite carriage, repair/repaint/retrim | £62 | individual | Lacy & Dow, Midland Railway Carriages I p.31 | MEASURED |
| 2012 | Chiltern Mk3 rebuild incl. plug doors and corrosion | £6.5m / 20 coaches = £325,000 | individual | Rail Magazine, 13 June 2012 | MEASURED |
| 2015 | Greater Anglia Mk3 refresh | £12m / 119 coaches = £100,840 | individual | Rail Magazine, 2 Feb 2015 | MEASURED |
| 2013 | Class 158 full refurbishment | £9.5m / 24 two-car units = £197,917 per vehicle | individual | LNWR press release, 27 Feb 2013 | MEASURED |
| 2025 | EMR Class 158 interior refresh | £5.2m / 26 two-car units = £100,000 per vehicle | individual | Modern Railways, 24 July 2025 | MEASURED |
| 2024 | Class 458 refurbishment | £25m / 28 four-car units = £223,214 per vehicle | individual | Alstom press release, 17 Dec 2024 | MEASURED |
| 2017 | Class 185 mid-life refresh | "just over £600,000 per unit" (3 cars) | individual | Rail Engineer, 4 April 2018 | STATED |
| 1995 | BRML heavy maintenance turnover per vehicle | £180m / 13,500 vehicles = £13,333 per vehicle-year | fleet | DoT press release, 5 June 1995 | COMPUTED |

The 1995 BRML figure is the only BR-era heavy-maintenance money found, and it is a depot turnover
divided by a throughput of vehicles, not an overhaul price. It is useful only as an order of
magnitude: heavy maintenance of a BR vehicle cost about £13,000 a vehicle-year in 1994/95.

## 5. How the cost rises with successive overhauls

The direct evidence is thin, and where it exists it is a range rather than a series.

1. **GWR 28xx, 1930s (MEASURED).** Heavy general £450-£700 and boiler overhaul £150-£700. The top of
   each range is 1.6 and 4.7 times the bottom. The trust's own reading is that the high figures are
   the ones with firebox or boiler renewal. That is the mechanism by which a late overhaul costs
   more: not the labour, but the decision to renew rather than repair the boiler.
2. **Boiler renewal is the step change (MEASURED).** A new GWR standard No. 1 boiler cost £971
   against a £4,992 locomotive (19.5 per cent, COMPUTED); a King boiler cost £1,687 of a £6,172
   locomotive (27.3 per cent, COMPUTED); a Britannia boiler cost £6,193 in 1953. A general repair at
   which the boiler is condemned therefore costs several times a general repair at which it is not.
3. **Cook's mechanism (STATED, 1955).** "In carrying out a heavy repair, the dismantling and erecting
   costs are fairly constant whatever the mileage and a higher mileage enables these to be spread."
   This is the opposite pressure: the fixed part of the overhaul is a declining share of cost per
   mile as mileage between overhauls rises. It does not say the overhaul gets cheaper with age.
4. **LMS individual costing (STATED, 1946).** Cox explains why costs must be averaged over years:
   "it is only thus that the effect of major items such as tyre and cylinder renewals and heavy
   firebox repairs and renewals can be included and so bring repair costs up to a steady level".
   That is a direct statement that the repair bill is lumpy and rises when renewals fall due.
5. **BR Pacific boiler renewals (MEASURED).** The ten-year record shows new boilers fitted at general
   repairs: 34 for the Kings between 1951 and 1959, 25 for the A4s, 9 for the A1s, 1 for the
   Duchesses, none for the Princess Royals or Merchant Navies. Swindon was renewing boilers on a
   25-year-old class; the LMS was not renewing at all. Same nominal overhaul, very different cost.
6. **Fenchurch (STATED, Railway Magazine 1941).** Actuarial life 30 years, written down to about £65
   from £500 by 1898 (13 per cent). A vehicle's book value, and therefore the capital it is worth
   spending an overhaul on, collapses well before its physical life ends.

**Conclusion.** There is no measured series of first, second and third overhaul costs for any
British rail vehicle. What the evidence supports is a *step*, not a ramp: overhauls are cheap while
components are repaired and expensive when the boiler, firebox or engine is renewed, and the
probability of renewal rises with age. The pakset's `overhauls_before_max_cost` should therefore be
small — two or three — and the max cost should represent a renewal overhaul, not a 1.2 multiple of
the first.

## 6. Upgrade and rebuild costs

These are the figures that size `upgrade_price`: the net cost of putting an old vehicle back into
service as this type.

| Year | Item | Cost | Per unit | Source | Tag |
|---|---|---|---|---|---|
| 1998 | Class 47 to Class 57, purchase of donor plus rebuild | £500,000 each | £500,000 | Railway Gazette International, 1 May 1998 | MEASURED |
| 1998 | Class 57 conversion, "reportedly" | £300,000 | £300,000 | Rail Magazine, cited by Wikipedia | STATED |
| 2003 | MML HST refurbishment, 36 power cars + 127 coaches | £18.7m | — | Railway Gazette International, 1 April 2003 | MEASURED |
| 2009 | NXEC HST re-engining and refurbishment, 30 power cars | £27m | £900,000 (COMPUTED) | Rail Technology Magazine, 20 March 2009 | MEASURED |
| 2016 | VTEC re-engine of all HST power cars | £16m | — | Rail Magazine, 16 March 2016 | MEASURED |
| 2015 | Class 321 Renatus, 30 four-car units | £60m | £2.0m per unit, £500,000 per vehicle (COMPUTED) | Eversholt Rail, 1 Aug 2015 | MEASURED |
| 2015 | Class 321 re-tractioning demonstrator, one unit | £5.5m | £5.5m | Eversholt Rail; IRJ, 2 Nov 2015 | MEASURED |
| 2013 | Class 455 re-tractioning, 91 four-car units | £40m | £439,560 per unit, £109,890 per vehicle (COMPUTED) | IRJ, 9 Dec 2013 | MEASURED |
| 2012 | Chiltern Mk3 rebuild with sliding plug doors, 20 coaches | £6.5m | £325,000 per coach | Rail Magazine, 13 June 2012 | MEASURED |

Three points for `upgrade_price`:

- **The Class 57 is the exact analogue of the field.** A 30-year-old locomotive bought and rebuilt
  for £500,000 against a new Class 66. The trade press put the rebuild at "about one-third that of
  a new-build locomotive". So an upgrade is roughly 30-35 per cent of a new vehicle, and that is the
  highest defensible figure for a heavy rebuild.
- **Re-engining alone is cheaper than rebuilding.** HST power cars at £900,000 each in 2009 included
  refurbishment and a bogie overhaul; the 2016 VTEC re-engine was £16m for a fleet, so perhaps half
  that per power car. Against a new power car this is a small fraction.
- **Refurbishment is much cheaper than either.** £100,000-£325,000 per coach, and £110,000 per
  vehicle for EMU re-tractioning, against new-build prices an order higher.

**Boiler renewal as the steam equivalent (MEASURED).** GWR boilers were 19.5-27.3 per cent of
locomotive capital (COMPUTED from the 2874 and King records); a Britannia boiler cost £6,193 in 1953.
A reboilering is therefore the steam `upgrade_price`, and it is cheaper than a diesel rebuild as a
share of capital.

## 7. Recommendations for the pakset fields

The shares are of the historical purchase price of the vehicle, which is the only scale-free way to
transfer these figures. They are **ESTIMATE** where marked: the interval and the money are measured,
the share is my reading of them.

### Steam locomotives, 1830-1960

| Field | 1830-1900 | 1900-1960 |
|---|---|---|
| `max_distance_between_overhauls` | 60,000 miles (97,000 km) | 80,000 miles (129,000 km); 100,000 (161,000 km) for express tender engines |
| `initial_overhaul_cost` | 4-5 per cent of purchase price | 5 per cent |
| `max_overhaul_cost` | 12-15 per cent | 15 per cent |
| `overhauls_before_max_cost` | 3 | 3 |
| `overhaul_month_tenths` | 6-7 (18-21 days, L&YR 1920) | 12-14 (31-45 days, BR Table 4) |
| `upgrade_price` (reboilering) | 15-20 per cent | 20-27 per cent |

The 5 per cent first overhaul sits below the GWR heavy general (9.0-14.0 per cent of the 1918 build
cost, COMPUTED) because a "general repair" in the BR sense is a lighter event than a "heavy
general", and because a first overhaul on a two-year-old engine renews little. The 15 per cent max
is the GWR heavy general upper bound. It should not exceed that: a locomotive whose overhaul cost
20 per cent of its price would never have been overhauled, it would have been scrapped, which is
what happened to the 30-year-old engines in the 1960s.

### Diesel and electric locomotives, 1955-2026

| Field | Value |
|---|---|
| `max_distance_between_overhauls` | 160,000-200,000 miles (258,000-322,000 km), i.e. the 2.75-year cycle at 55,000-70,000 miles a year |
| `initial_overhaul_cost` | 6-8 per cent of purchase price (ESTIMATE) |
| `max_overhaul_cost` | 18-22 per cent (ESTIMATE) |
| `overhauls_before_max_cost` | 3 |
| `overhaul_month_tenths` | 10-12 (a works overhaul of a diesel is shorter than a steam general repair) |
| `upgrade_price` | 30-35 per cent (Class 57), falling to 10-15 per cent for a re-engine only |

The interval is the measured 2.75-year cycle. The cost shares are estimates because no measured
per-overhaul money exists for a BR diesel; they are set so that the engine overhaul (the dominant
item, at 10,000-30,000 hours between overhauls) can be paid for.

### Carriages, 1830-2026

| Field | 1830-1922 | 1923-1994 | 1994-2026 |
|---|---|---|---|
| `max_distance_between_overhauls` | 4 years at contemporary mileage | 2-3 years | 2 years |
| `initial_overhaul_cost` | 8 per cent | 8 per cent | 5 per cent |
| `max_overhaul_cost` | 25 per cent | 25 per cent | 25-30 per cent |
| `overhauls_before_max_cost` | 2 | 3 | 3 |
| `overhaul_month_tenths` | 5 | 5 | 3-5 (6 days to 2 weeks in works) |

The 25 per cent max is the Midland 1860s figure (24.8-27.6 per cent of capital, COMPUTED) and it is
also the share that a modern heavyweight refurbishment reaches: £325,000 a coach for the Chiltern
rebuild is the top of the modern range. The low first overhaul reflects that a new carriage needs
painting and trimming, not structural work.

### Wagons, 1830-2026

| Field | Value |
|---|---|
| `max_distance_between_overhauls` | 3 years (the Midland's nine-month works visit was an examination, not an overhaul) |
| `initial_overhaul_cost` | 8 per cent (ESTIMATE) |
| `max_overhaul_cost` | 20 per cent (ESTIMATE) |
| `overhauls_before_max_cost` | 2 |
| `overhaul_month_tenths` | 2-3 |

This is the weakest class in the pass. No measured wagon overhaul price was found in any era. The
20 per cent max is chosen from the BR practice of condemning a wagon when the repair estimate
exceeded a monetary limit — the limit itself is the effective overhaul ceiling.

### Multiple units, 1950-2026

| Field | Value |
|---|---|
| `max_distance_between_overhauls` | 2 years (BR 1996 coach cycle applies to MU cars) |
| `initial_overhaul_cost` | 4 per cent |
| `max_overhaul_cost` | 20 per cent |
| `overhauls_before_max_cost` | 3 |
| `overhaul_month_tenths` | 2-3 |
| `upgrade_price` | 8-12 per cent for a refresh, 20-25 per cent for re-tractioning |

A re-tractioning at £109,890 a vehicle (Class 455) is the strongest modern datum; against a
new-build EMU vehicle it is well under a quarter.

## 8. Dead ends and cautions

- **No measured per-overhaul price for a BR diesel or electric locomotive.** Searched for it
  directly and through the IMechE and Modern Railways literature. What exists is per-mile and
  per-year maintenance cost, which cannot be decomposed into overhauls.
- **No measured wagon overhaul price, 1830-2026.** The HMRS holds "Wagons - annual average repair
  costs 1972-81" but it is archive-only and not digitised.
- **`British Railways: A business history` appendix tables A.6, A.7 and A.19** (locomotive repair
  expenditure 1928-47, carriage and wagon repair expenditure, and "Maintenance costs per unit, 1981")
  are exactly the tables wanted, but the only accessible copy (docslib) returns an HTML wrapper
  instead of the PDF. Worth a library request.
- **Bond 1953, "Organisation and Control of Locomotive Repairs on British Railways"**, J. Instn Loco.
  Engrs 43, is behind the SAGE paywall. Its class-by-class mileage figures are quoted second-hand on
  SteamIndex (55,616 to 93,363 miles between repairs) and are used here only as a range.
- **The `BR-1956-OCR` and `BR-1958` "Facts and Figures" booklets** have no text layer; they would
  give 1950s repair totals but not per-overhaul prices.
- **Heritage railway overhaul costs** (for example the £250,000 quoted for Fenchurch's 2020-22
  overhaul) are excluded: they are one-off volunteer-sector costs with no production engineering
  behind them and would overstate a working railway's overhaul by an order of magnitude.
- **A forum figure of £125,000 per Mk3 coach for PRM work and sliding doors (2018)** was seen but is
  a poster's assertion, not a contract value, and is not used.
- **The Class 57 figures disagree.** Railway Gazette says £500,000 each including the purchase of
  the donor locomotive; Rail Magazine says £300,000 for the conversion. Both are recorded; the
  £500,000 figure is the one that matches "net cost of replacing an old vehicle with this type" and
  should be preferred for `upgrade_price`.
- **Do not read the GWR £450-£700 as a price level for the 1930s generally.** It is one class, one
  works, and the range spans a firebox renewal. The ratio to the 1918 build cost is the transferable
  quantity, not the pound figure.
