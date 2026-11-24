---
status: draft
verified: New ex-15 @ 687347620 (working tree), 2026-11-24
---
# Base maintenance costs

**Covers**: what a vehicle should cost to maintain, in the engine's two fields, expressed in 1900
terms so that the values can be entered in a `.dat` file and scaled by the index.

Evidence: [published-maintenance](../vehicle-cost/published-maintenance.md). Method:
[vehicle-cost-method](../vehicle-cost-method.md). Engine mechanics:
[vehicle-cost-model](../vehicle-cost-model.md). Decomposition into `fixed_cost`, `runningcost`,
overhaul and upgrade components: [maintenance-decomposition](maintenance-decomposition.md).
Parent: [vehicle-cost-evidence](../vehicle-cost-evidence.md).

No `.dat` value has been changed. This doc supplies the level; the synthesis across all domains
decides when it is used. `[USER-DIRECTION:2026-11-16]`

Coverage is uneven: steam locomotives, carriages, buses, lorries and aircraft are measured, trams,
horses and inland boats are not measured at all. Read the coverage table before using any class's
figure, and do not extend a class's value to another class on the strength of this doc alone.

## Conversion

Two conversions, both already established:

- **Per-kilometre costs are on the revenue timescale.** One Simucredit is £0.005208 in 1900, and
  the fare calibration fixes it exactly: 50 Simucents (0.50 Simucredits) per kilometre is 1d per mile, so
  1 Simucredit is 1.243 old pence. The `.dat` field is in Simucents (hundredths of a Simucredit), so a cost of
  *d* pence per kilometre in 1900 becomes `runningcost = d × 80.4`.
  `[CODE New ex-15 @ 8d0603d81]`
- **Monthly charges are on the capital timescale**, which is the revenue rate multiplied by the
  workbook's time compression of 76.09. The per-vehicle-year figures below are converted on the
  revenue rate, so if `fixed_cost` belongs on the capital rate they should be 76 times larger.
  Which timescale a monthly charge belongs on depends on kilometres travelled per game month,
  which is not yet known; see [balance-synthesis](../balance-synthesis.md) §8. Treat the
  `fixed_cost` column below as a lower bound until that is settled.
- **Nominal figures are brought to 1900 by dividing by the `general` index** for the year of the
  figure, then converted as above. Pence per mile becomes pence per kilometre by multiplying by
  0.6214.

### What these figures exclude, and what must be added back

Fuel is excluded from every figure in this doc. The engine charges it separately from
`config/fuel.tab` by fuel and engine type, so it must not appear in `runningcost` or `fixed_cost`.
Crew is likewise excluded and charged from `config/staff.tab`.

Tyres and lubricants are excluded from most of the measured figures but are charged from neither
of those files. The engine has no separate field for them, so they belong in `runningcost`.
Commercial Motor itemises them separately, which is why the road figures below can be adjusted
and the rail figures cannot. The per-kilometre table is therefore a floor: it is the repair cost,
not the whole non-fuel per-kilometre cost.

Damage to the way is a separate matter and must not be added here. The engine charges way wear on
the way itself, through the way's wear capacity and renewal, and the pakset's own wear workbooks
(`New/Wear calculations.ods` and `New/road-vehicle-wear-calcs.ods`) compute a vehicle's
contribution to that damage from axle load and gross weight. That cost sits in the infrastructure
domain and is already covered there.

## Per-kilometre maintenance

Measured figures, converted to 1900 pence per kilometre and to the `.dat` field:

| Year | Vehicle | As stated | 1900 d/km | `runningcost` |
|---|---|---|---|---|
| 1892 | Locomotive, 19-company average | 2.51d per train-mile | 1.61 | 129 |
| 1892 | Locomotive, North Eastern | 4.40d per train-mile | 2.82 | 227 |
| 1892 | Locomotive, Lancashire & Yorkshire | 3.38d per train-mile | 2.17 | 174 |
| 1892 | Locomotive, Great Southern & Western | 2.86d per train-mile | 1.83 | 147 |
| 1892 | Locomotive, London & South-Western | 2.04d per train-mile | 1.31 | 105 |
| 1892 | Locomotive, North British | 1.47d per train-mile | 0.94 | 76 |
| 1954 | Locomotive, boiler work only, 41 class-years | 1.36d per mile | 0.19 | 15 |
| 1928 | Trolleybus, Keighley | 2.37d per vehicle-mile | 0.75 | 60 |
| 1948 | Bus, 26-seat | 2.50d per mile | 0.46 | 37 |
| 1948 | Coach, 26-seat | 1.50d per mile | 0.28 | 22 |
| 1955 | Bus, municipal average | 2.82d per vehicle-mile | 0.37 | 30 |
| 1955 | Bus, London Transport | 4.36d per vehicle-mile | 0.58 | 47 |
| 1958 | Lorry, 5-ton petrol | 1.95d per mile | 0.23 | 19 |
| 1958 | Lorry, eight-wheel oil | 2.47d per mile | 0.29 | 23 |
| 1953 | Lorry, 6-ton oil | 1.89d per mile | 0.27 | 21 |
| 1955 | Lorry, 7-ton oil | 1.80d per mile | 0.24 | 19 |

Reading:

- Steam locomotive repair cost varies by a factor of three between companies of the same period
  on the same accounting basis. The North Eastern figure is distorted: the company built engines
  to revenue and transferred them to capital, which the author states. The North British figure
  the author could not explain. Neither should anchor the series; the mid-range English companies
  are the better guide.
- Boiler work is a small part of a locomotive's repair bill: the 1954 boiler-only average is
  about 12 per cent of the 1892 all-in average, across very different eras.
- Road vehicle maintenance does not vary much by class: buses 30 to 47, lorries 19 to 31.

### Tyres and lubricants

Where the source itemises them, they can be added:

| Year | Vehicle | Maintenance | Lubricants | Tyres | Total | 1900 d/km | `runningcost` |
|---|---|---|---|---|---|---|---|
| 1948 | Bus, 26-seat | 2.50d | | 0.72d | 3.22d | 0.59 | 48 |
| 1948 | Coach, 26-seat | 1.50d | | 1.00d | 2.50d | 0.46 | 37 |
| 1955 | Lorry, 7-ton petrol | 2.00d | 0.25d | 1.75d | 4.00d | 0.53 | 43 |
| 1955 | Lorry, 7-ton oil | 1.80d | 0.25d | 1.75d | 3.80d | 0.50 | 41 |

The true non-fuel per-kilometre cost is therefore 30 to 100 per cent above the repair figure for
road vehicles, with tyres the larger part. No source found separates tyres or lubricants for rail
vehicles, so the rail figures remain repair cost only.

## Per-vehicle-year maintenance

Carriage and wagon accounts are kept per vehicle per year, not per mile. Hill gives carriage
maintenance of £18 to £45 per vehicle per year in 1892, which is £18.6 to £46.7 in 1900 terms:

| Nominal 1892, £ | 1900, £ | 1900, d/year | 1900, d/month | `fixed_cost` |
|---|---|---|---|---|
| 18 | 18.6 | 4,454 | 371 | 29,858 |
| 26 | 27.0 | 6,482 | 540 | 43,460 |
| 31 | 32.3 | 7,744 | 645 | 51,920 |
| 39 | 40.5 | 9,724 | 810 | 65,190 |
| 45 | 46.7 | 11,208 | 934 | 75,142 |

This is the single most useful block for carriages, because it is already in the engine's
per-month unit once divided by twelve. It needs no split: the accounts state the cost per vehicle
per year, which is exactly what `fixed_cost` charges.

### Trams

The Ministry of Transport statutory returns print a combined "General Repairs and Maintenance" per
car-mile for British tramways and light railways, 1913-14 and 1922-23 to 1930-31. The head excludes
power, traffic expenses, rates, compensation, insurance and general expenses, which is the right
scope: the vehicle's own upkeep and nothing else.

| Year | Undertakings | As stated | 1900 d/km | `runningcost` |
|---|---|---|---|---|
| 1913-14 | All, Great Britain | 1.57d per car-mile | 0.91 | 73 |
| 1913-14 | Companies | 1.70d per car-mile | 0.99 | 79 |
| 1922-23 | All, Great Britain | 4.46d per car-mile | 1.28 | 103 |
| 1922-23 | Companies | 5.07d per car-mile | 1.46 | 117 |

A tramcar therefore costs about twice what a bus costs per kilometre in the same money, which is
the expected direction: a heavier vehicle with electrical equipment, and the tram figures are
thirty-five years earlier, when repair labour was cheaper in real terms.

Modern light rail has budget figures but no operator-stated cost per vehicle-km. Sheffield
Supertram's rolling-stock and infrastructure maintenance budgets for 2024/25 and 2025/26 are
separately stated, and the Department for Transport gives vehicle mileage by system, so a
per-vehicle-km figure can be constructed but is not published as one. See
[tram-maintenance](tram-maintenance.md).

## Maintenance as a share of purchase price

### Road vehicles, measured share (2026-11-23)

For motor road vehicles the annual maintenance bill is **12 to 21 per cent of purchase price**,
and four of the ratios have both sides measured in the same accounts or the same article:

| Year | Vehicle | Share a year | Basis |
|---|---|---|---|
| 1932 | Glasgow 51-seat double-decker | 21% | both sides in the same accounts |
| 1934 | Glasgow 51-seat double-decker | 15% | capital includes premises and plant, so the vehicle share is higher |
| 1961 | 31-seat bus | 14% | both sides in the same article |
| 1934 | 1-ton lorry | 12% | both sides in the same article |
| 1933 | 2-ton van | 21% | both sides in the same article |
| 1933 | 12-13 ton steam wagon | 8% | owner's accounts |

The share does **not** taper with vehicle size: the apparent taper in a 1-ton/2-ton lorry pair
is the price ratio doing the work, not the maintenance ratio. The share is therefore useful as
a cross-check, but it is not how the workbooks now charge road maintenance: the per-kilometre
evidence is direct and the share is not (see the field note below).
`[LITERATURE: research pass 31; Commercial Motor accounts quoted there]`

**Field note and the split (2026-11-23).** The section above puts road vehicles in
`runningcost`, because Commercial Motor records maintenance per mile. Maintenance is not
wholly mileage-driven, however: the annual test, periodic safety inspections, washing,
cleaning and body care accrue whether or not the vehicle runs, and so does workshop overhead.
No source measures the split. The workbooks therefore take the measured per-kilometre total
and divide it **75 per cent distance-driven to 25 per cent standing**, the standing part being
an estimate within a defensible band of 15-35 per cent. The per-kilometre charge goes to
`runningcost` and the standing part to `fixed_cost`; the reference annual distance at which
the total is turned into the two charges is 50,000 km for a bus, 40,000 km for a lorry and
25,000 km for a van. Every row records the split, the reference distance and the implied share
of capital, so a later reader can see what was measured and what was assumed.
`[CODE ai/temp/evidence_data.py; research pass 31]`

**The two routes disagree, and the per-kilometre one is used.** The capital-share route and
the per-kilometre route do not reconcile for every vehicle. A 1961 31-seat bus at £2,900 with
a £407 a year maintenance bill is 14 per cent of capital; a 1955 municipal bus at 2.82d a mile
over 48,000 km is about £75 a year, which is 7-9 per cent of a £850-1,200 bus. The spread of
the measured evidence is therefore **7-21 per cent**, not the 12-21 per cent of the ratio table
above, and the ratio is sensitive to the annual mileage assumption. The per-kilometre figures
are direct measurements of the quantity being charged, so they carry the workbooks, and the
implied share is printed on every row as the cross-check.
`[LITERATURE: research pass 31; Commercial Motor 1961 cost tables]`

**Towed trailers carry a distance charge too.** A semi-trailer has no engine but it wears on
tyres, brakes, suspension, body and coupling, and the only measured split found — the FTA 2016
table — puts the trailer at 5.72p a mile against the tractor's 10.41p, so a trailer carries
about 35 per cent of the combination's maintenance and about 30 per cent of its capital. The
workbooks price motor-era trailers that way and keep the same 75/25 distance-to-standing split.
Horse-drawn carts and horse-drawn trailers stay on the cart ladder, because they have no
mileage evidence of their own; the horse itself is a separate object and its keep is entirely
time-based, which is correct.
`[LITERATURE: FTA Managers' Guide to Distribution Costs, October 2016]`

### The dimensionless result

The dimensionless result, which is independent of the currency conversion and of mileage:

| Vehicle | Annual maintenance as a share of purchase price | Basis |
|---|---|---|
| General cargo steamer, mid-life | 5 per cent | Martin 1924, surveyor's working figure |
| Steam locomotive, mid-life | about 12 per cent | Hill's £253 per engine-year against a locomotive of about £2,000 |
| Bus, 1955 | about 11 per cent | 0.37d/km at about 60,000 km a year against a bus of about £850 in 1900 terms |
| Lorry, 1958 | about 11 per cent | 0.23d/km at about 40,000 km a year against a lorry of about £340 in 1900 terms |
| Steam locomotive, end of life | 25 to 33 per cent | Webb, United States practice, at scrapping |
| Locomotive renewals | 3.6 per cent a year | Hill, seven companies, implying a 28-year life |

So a mid-life vehicle costs about a tenth of its purchase price a year to keep in repair, a ship
about a twentieth, and a worn-out locomotive a quarter to a third. That is the envelope within
which any class's two fields must sum, and it is the natural cross-check on the per-kilometre and
per-vehicle figures above. The bus and lorry rows are repair cost only; with tyres and lubricants
they rise by roughly a fifth to a third.

## Which field a class belongs in

The accounts themselves indicate the mapping, because they chose how to record the cost:

- **Locomotives, railcars and multiple units: `runningcost`.** Recorded per train-mile or per
  engine-mile. Use the per-kilometre table.
- **Carriages and wagons: `fixed_cost`.** Recorded per vehicle per year. Use the per-vehicle table.
- **Road vehicles: `runningcost`.** Commercial Motor records maintenance per mile, with fuel,
  tyres, licences, insurance and wages as separate heads. Use the per-kilometre table and add
  tyres and lubricants from the same tables: they are not charged anywhere else.
- **Ships: `fixed_cost`, with a running element.** The class-survey docking and the annual repair
  reserve are time-based; voyage repairs are not.
- **Aircraft: `runningcost`.** Recorded per block-hour or per flight-hour.

## The split problem

No source found separates standing maintenance from distance-based maintenance. Hill gives the
same locomotive cost both per train-mile and per engine-year, and the two are consistent with each
other at about 23,000 miles a year and no standing element at all. The railway accounts therefore
treat locomotive repair as wholly mileage-driven.

That is a statement about accounting practice, not about physics: an engine standing in a shed
still needs inspection, cleaning and protection from deterioration. The engine models that through
`fixed_cost`, and the historical record cannot size it.

Three ways to proceed, in order of preference:

1. **Leave the measured field only.** Put the measured cost in the field the accounts used, and
   set the other field to a small standing allowance that is stated as an assumption rather than
   as evidence. This is honest and keeps the measured part measured.
2. **Allocate by the overhaul cycle.** Overhauls are distance-based in the engine, so the fixed
   field should hold only the time-based remainder: inspection, cleaning, certification.
3. **Allocate by a fixed proportion** of the total, stated as an assumption. This is the weakest
   option and should be used only if the first two cannot be made to work.

## What this implies for the current `.dat` values

A comparison against the files as they stand, offered as a diagnostic and not as a correction:

- `runningcost` is in the right order of magnitude. The Leyland Atlantean's 57 sits just above
  the measured bus range of 30 to 48 once tyres are added; the LNER A3's 393 is about three times
  the 1892 all-company average of 129, which is plausible for a large express engine.
- `fixed_cost` on carriages is two orders of magnitude too small. A BR Mk1 TSO carries 694; the
  1892 carriage evidence implies 30,000 to 75,000. The GNR six-wheel third at 374 is further out
  still.
- The two errors are in opposite directions within the same file set, which is consistent with the
  finding that the present values came from more than one calibration run.

### Later anchors, added 2026-11-17

Road vehicles, converted from the Commercial Motor tables and later sources. The 1983 and 2016
sources are printed in decimal pence; the 1900 basis is old pence, so every post-1971
pence-per-mile figure carries an additional factor of 2.4 (one decimal penny is 2.4 old pence).
The rows below include it.

| Year | Vehicle | As stated | `runningcost` |
|---|---|---|---|
| 1963 | 7-ton oil goods | 2.71d per mile | 23 |
| 1966 | 7-ton goods | 2.85d per mile | 22 |
| 1966 | 10-ton articulated | 3.13d per mile | 24 |
| 1968 | 16-ton rigid eight-wheeler | 5.06d per mile | 36 |
| 1970 | 16-ton four-wheeler | 4.66d per mile | 29 |
| 1983 | Merseyside buses, repairs and maintenance | 53.7p per mile (decimal) | 177 |
| 2016 | 32-ton rigid tipper | 21.37p per mile (decimal) | 23 |
| 2016 | 44-ton artic tractor unit | 10.41p per mile (decimal) | 11 |

The 2016 values are per unit, not per combination: the trailer adds 5.72p per mile, so the
articulated combination is about 16.1p per mile, or `runningcost` 17. Maintenance per mile is
therefore roughly flat in real terms between 1968 (36) and 2016 (17-23), not a fivefold fall;
the earlier figures in this table that omitted the 2.4 factor made the post-1971 rows look like
a real-terms collapse. [LITERATURE: *Commercial Motor*, 21 Jan 1984; FTA *Managers' Guide to
Distribution Costs*, Oct 2016; unit conversion in research pass 15]

Modern rail traction, total maintenance per vehicle-mile at 2013 prices: £0.80 for diesel multiple
units, giving `runningcost` 89, and £0.44 for electric, giving 49. London Underground's per-car-year
figures for 2009/10 and the Class 66 and 47 rebuild costs are in
[modern-traction-multiple-units](modern-traction-multiple-units.md) and
[modern-traction-locomotives-and-wagons](modern-traction-locomotives-and-wagons.md).

Horses, from the itemised London accounts of 1876-1897, excluding the horsekeeper's wages:

| Annual keep, nominal | Range across accounts | 1900 £/month | `fixed_cost` |
|---|---|---|---|
| about £45 | £28 to £60 | 3.9 | 74,700 |
| low | £28 6s (LGOC, 1893) | 2.4 | 46,500 |
| high | £59 13s 6d (London coal wharf, 1830) | 5.2 | 99,600 |

A horse costs about as much to keep each year as a carriage costs to maintain, and more than the
horse itself cost to buy. That is the correct shape for the engine: a low `cost` and a high
`fixed_cost`, because a horse is a current cost rather than a long-lived asset.

## Coverage by class

What the evidence supports, and what it does not.

| Class | Coverage | Best figures | Gap |
|---|---|---|---|
| Steam locomotives | Strong | 19-company per-mile range 1892; GWR and SER per-engine-year; pre-1890 now measured (Price Williams 1870, 12 companies; McDonnell 1877, 6 companies) | No per-mile figure for 1900-1950 |
| Diesel and electric locomotives | Good | TRB classes 37, 47, 55, 87; Class 66 and 47 rebuild costs and intervals; Beeching 1961 and Serpell per-train-mile and per-passenger-mile chains | No money per overhaul (Kew: COAL 101/164, AN 88/108, AN 112 charge schedules) |
| Multiple units | Good | RDG £0.80 diesel and £0.44 electric per vehicle-mile; London Underground per car-year; Civity per train-km | No scheduled/unscheduled money split |
| Carriages | Strong | Per vehicle-year, 19 companies, 1892 (£18 6s.-£52 14s., average £33 6s.; Hill 1895 Table II, company attribution recovered 2026-11-24) | No post-1906 figure except whole-company totals |
| Wagons | Strong (1892), fair after | Hill 1895 Table III: 19 companies, average £4 4s. per wagon-year repairs + renewals; 1929 private-owner repair contract £5; Metropolitan whole-account totals 1893-1906 | Solved for 1887-92 (2026-11-24); no 20th-century figure (post-1911 MoT returns, library route) and no overhaul price in any era |
| Buses | Strong | 1914 LGOC, 1925 Edinburgh, 1931-34 Glasgow, 1955 six undertakings; annual bill 12-21 per cent of purchase price | No measured pre-1914 figure; no municipal omnibus returns exist |
| Coaches | Fair | 1948, 1964, 1969 and 1970 costings | No undertaking data |
| Lorries | Strong | 1934-1970 size pairs and the 2016 FTA tables, with tyres and lubricants itemised | Gap 1975-2015; the trade tables are page images |
| Vans | Fair | 1934 1-ton and 1933 2-ton, both with the purchase price | No pre-1930 figure |
| Trolleybuses | Weak | 1928 Keighley only | No other undertaking |
| Horse stage coaches | Fair | 1760s Hanforth accounts: GBP 70 a coach-year and about 70 per cent of capital | No 1800-1840 repair account; the 1820 private-carriage bill is the nearest |
| Trams, old | Good | Ministry of Transport returns 1913-14 and 1922-23 to 1930-31, per car-mile on a combined repairs and maintenance head | No car-only figure; no pre-1913 figure |
| Trams, light rail | Fair | Sheffield Supertram budgets 2024/25 and 2025/26; DfT vehicle mileage by system; DLR CoMET unit costs | No operator-stated cost per vehicle-km |
| Ships | Good | 50 figures 1849-2026, dry-docking and survey costs; no per-voyage figure exists in any source found | No British liner-company repair figure: the accounts print working expenses as one line |
| Inland boats | Weak | Repair jobs from canal company records, 1877-1928; modern narrowboats | No figure for a boat in the carrying trade |
| Horses | Good for 1876-1897 London | Itemised feed, farriery, veterinary and stabling; annual keep £28 to £60 | Pre-1830 rests on one coach account; no railway or canal horse account |
| Aircraft | Fair | British operator engineering cost per flying hour for 1969/70 and 1972/73; IATA 2024 benchmark | No British per-hour figure outside 1969-1973 |

The coverage is now sufficient to set a base level for every class the pakset runs except one:
**wagons**, where no per-wagon-year figure exists, and **inland boats in the carrying trade**,
where only individual repair jobs are recorded. The weakest remaining point is the pre-1830 horse
fleet, which rests on one coach account.

## What would fill the gaps

Candidate sources, none yet tried:

- **Trams, old**: municipal tramway annual accounts, which are structured like the bus accounts
  that worked well for 1955, with repairs and maintenance per car-mile; the tramway trade press;
  London County Council and Manchester Corporation tramways reports.
- **Trams, light rail**: modern light rail operators publish maintenance cost per vehicle-km in
  their annual reports and in the ORR's light rail statistics.
- **Horses**: feed, farriery, veterinary and stabling are separable heads in coaching and omnibus
  accounts. The London General Omnibus Company and the coaching inn records are the likely route;
  agricultural cost surveys also price horse keep.
- **Wagons**: solved — Hill 1895 Appendix II Table III gives the per-wagon-year figure for 1887-92
  (19 companies, average £4 4s., repairs + renewals). The 20th century needs the post-1911
  Ministry of Transport returns (library route); overhaul prices survive only in undigitised
  repair invoices.
- **Diesel and electric multiple units**: BR depot cost data of the kind the TRB report used, or
  the modern train-operating companies' published cost per vehicle-mile.
- **Inland boats**: canal carrier accounts; the narrowboat operating literature is thin and mostly
  qualitative.
- **Aircraft**: CAA and IATA cost statistics for British operators, which would replace the United
  States system averages.
- **Post-1958 road vehicles**: later Commercial Motor tables, which continue the same structure and
  would extend the series to the present.

## Open questions

- What standing allowance should a locomotive carry, given that no source measures one?
- How is the Hill per-vehicle-year maintenance figure (repairs **and renewals** combined) to be
  split into `fixed_cost` and `runningcost`? The 2026-11-24 regression across Hill's 19 companies
  does not identify it (r² 0.04 in cost space; see
  [research-pricing-report-39](../cost-balancing/research-pricing-report-39.md) §1). Routes: the
  GER half-yearly series within-company; an engineering fixed/distance decomposition; modern
  contract structures. The renewals share must also be netted out (renewals are capital in-game),
  against the post-1911 MoT returns' renewals columns.
- Does the engine's wear ramp already represent the distance-based overhaul, so that
  `runningcost` should be the mid-life average rather than the new-vehicle figure?
- Should wagons, which the accounts also record per vehicle-year, use `fixed_cost` like carriages,
  or `runningcost` because their maintenance is dominated by mileage?
- Are the pakset's horse figures to be replaced by evidence, or kept as stated estimates? No
  historical horse keep figure has been found.
