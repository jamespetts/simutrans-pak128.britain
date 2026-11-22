---
status: draft
verified: none
---

# Research report 16: measured British maintenance costs of depots, tunnels, road signs and bridges

**Covers**: annual maintenance of locomotive sheds, bus garages, tram depots and goods
sheds; annual maintenance and renewal of railway and road tunnels, with drainage, lighting
and pumping where stated; annual maintenance of road signs, illuminated signs, vehicle
activated signs and traffic signal sites; annual bridge upkeep per structure and per metre,
as a cross-check on Cudworth 1886.

All figures are nominal money of the year stated. No deflation has been applied anywhere in
this report or in `research-pricing-rows-16.csv`, except where a figure is explicitly
labelled as derived or restated. No Simutrans `.dat` price was used as evidence, and no
figure was fitted to the pakset. Nothing under `New/` was modified and no git command was
run.

Evidence base: 56 rows in `research-pricing-rows-16.csv`. Domains: 19 depot, 9 tunnel,
19 roadsign, 9 bridge. Kinds: 48 maintenance, 8 capital. The capital rows exist only to make
a maintenance rate interpretable (garage construction cost, sign replacement cost, bridge
backlog and intervention cost); they are marked `kind=capital` so they can be filtered out.

---

## 1. The answer in one page

1. **Depots have no measured per-depot maintenance account in the British sources
   consulted.** The two measured system-level figures are the Midland Railway's annual
   "turntables and buildings" charge, GBP 2,086 in 1873 and GBP 3,148 in 1896, with a peak of
   GBP 3,704 in 1878 (0.19 to 0.39 per cent of gross locomotive department expenditure), and
   the British Transport Commission's 1949 bus premises line, GBP 533,105 for the provincial
   and Scottish bus
   undertakings (1.49 per cent of receipts) and GBP 1,269,842 for London Transport road
   services (3.01 per cent of receipts). Neither can be converted to a per-shed or per-garage
   rate without a building count and a capital value that the sources do not give.

2. **The defensible depot rate is therefore a building benchmark, not a depot measurement.**
   Seeley states a rough guide of about 1 per cent of capital a year for buildings generally
   (1976); his light industrial example implies about 1.6 per cent; the Building Maintenance
   Information benchmark is 2.5 per cent of capital a year averaged across many building
   types (2003-04). For a brick or steel shed with pits, cranes and heating, **1.0 to 2.0 per
   cent of capital a year, central 1.5 per cent**, is the recommendation. Confidence:
   medium-low.

3. **Tunnels have a strong modern aggregate but no British lining-specific series.**
   Network Rail is responsible for 630 tunnels over 335 km and spent GBP 22m on tunnel
   renewals in 2023-24. That is **GBP 65.67 per metre-year, or GBP 34,921 per tunnel-year**,
   in nominal 2023-24 money. It is renewal rather than routine maintenance, so it is a floor
   for total upkeep, not a complete maintenance figure.

4. **The tunnel rate is about 1 per cent of capital a year.** A double-track bored tunnel cost
   GBP 45-145 a metre in 1900 (knowledge base section 4); 1 per cent gives GBP 0.45-1.45 per
   metre-year in that money. The modern renewal provision is GBP 65.67 per metre-year in
   2023-24 money. The two cannot be compared directly without a deflator, and none is applied
   here, but they are of the same order once the price level change is allowed for. The
   recommendation is **1.0 per cent of capital a year, range 0.5 to 1.5 per cent**, with the
   lower end for a modern deep tunnel. Confidence: medium for the level, low for any
   difference between lining materials.

5. **Road signs are cheap to maintain individually and expensive only when they are lit or
   powered.** Argyll and Bute's 5,013 non-illuminated signs carry GBP 7,912 of annualised
   depreciation, GBP 1.58 a sign-year, and a GBP 52,000 replacement budget, GBP 10.37 a
   sign-year over a 29-year cycle. Wigan's 15,000 signs at GBP 2.1m over a 12-year life imply
   GBP 11.67 a sign-year. Routine cleaning and repair is smaller than either. The
   recommendation for an ordinary plate sign is **GBP 2 to 5 a sign-year in 2024 money,
   central GBP 3**, confidence medium.

6. **Illuminated signs and vehicle activated signs are an order of magnitude dearer.**
   Argyll's illuminated signs carry GBP 23.08 a sign-year of annualised depreciation; the DfT
   puts the energy cost at GBP 8.17 a sign-year and suggests, without validating the figure,
   that lamp cleaning, electrical testing and bulb changing could add at least GBP 100.
   Measured vehicle activated sign costs are GBP 250 a sign-year (Buckinghamshire, 2006) and
   GBP 90 a sign-year for interactive school signs (Lancashire, 2011). The recommendation for
   a lit or powered sign is **GBP 30 to 100 a sign-year**, confidence medium-low.

7. **Traffic signal sites are the best-measured item in this report.** Three independent
   sources agree: Argyll and Bute's revenue budget is GBP 45,000 for 25 sites, GBP 1,800 a
   site-year; the DfT's 2023 renewal unit rates annualised over the 12.5-year half-life give
   GBP 1,599 to 2,393 a site-year; West Sussex's 2020 contract, already recorded in report
   14, was GBP 1,532 to 1,613 a site-year. The recommendation is **GBP 1,500 to 2,400 a
   site-year**, confidence high.

8. **Bridges have no new per-metre British measurement, and Cudworth 1886 still stands as the
   only one.** The modern evidence is per structure: local authority bridge maintenance was
   GBP 367m in 2016-17 and GBP 598m in 2017-18 across about 71,650 bridges, which is GBP 5,122
   and GBP 8,346 per bridge-year; Network Rail's bridge and major structure renewals were
   GBP 277m in 2023-24, about GBP 9,431 per structure-year. These bundle deck renewal,
   waterproofing, bearings and traffic loading, so they are not comparable with Cudworth's
   routine iron viaduct upkeep of GBP 0.25 per metre-year.

---

## 2. Method and evidence grades

The evidence is graded as follows:

1. **Measured account or contract** — an actual account line, contract sum or statutory
   return. Examples: the Midland Railway locomotive department table, the BTC 1949 accounts,
   the Argyll and Bute asset valuation, the West Sussex signal contract.
2. **Published benchmark** — a stated rate from a recognised body, applied to a class rather
   than a named asset. Examples: the BMI 2.5 per cent building rate, Seeley's 1 per cent
   guide, the Constructing Excellence factory rates.
3. **Derived** — arithmetic on a measured figure, with the arithmetic shown in the row. The
   derivation is only as good as its numerator and denominator; the notes say which.
4. **Unverified estimate** — a figure the source itself declines to rely on. Only one row is
   in this class: the DfT's GBP 100 a year for lit-sign maintenance.

The search rule was one query per turn, with the subject, the constraint and the date window
in the query. Every figure was read from a fetched page or a fetched PDF. Three Institution
of Civil Engineers papers that would have supplied lining-specific tunnel maintenance were
paywalled; they are recorded as dead ends in section 7 rather than cited from the search
extract.

---

## 3. Depots

### 3.1 What the railway accounts show

The Midland Railway's locomotive department accounts, as reproduced by Dodgson from Johnson's
1898 Institution of Mechanical Engineers address, carry a line for "turntables and buildings".
It is the only annual railway depot building charge found in a continuous series:

| Year | Charge | Share of gross locomotive expenditure |
|---|---|---|
| 1873 | GBP 2,086 | 0.22 per cent |
| 1878 | GBP 3,704 | 0.39 per cent |
| 1883 | GBP 2,898 | 0.25 per cent |
| 1888 | GBP 2,898 | 0.25 per cent |
| 1893 | GBP 3,111 | 0.20 per cent |
| 1896 | GBP 3,148 | 0.19 per cent |

Two cautions apply. First, the line covers the whole Midland system, not one shed, and the
number and capital value of Midland sheds in 1896 are not in the source. Second, the railway
accounting distinction between revenue and capital put major building renewals in "maintenance
of way and works" or in capital, so the line understates total shed upkeep. It is a floor.

The useful finding is the ratio, not the absolute sum: shed fabric upkeep charged to the
locomotive department was between one-fifth and two-fifths of one per cent of locomotive
department expenditure. Even allowing for a second property account, the shed building was a
small cost next to the locomotives it housed.

### 3.2 What the bus accounts show

The British Transport Commission's 1949 report separates "maintenance of buildings, etc." from
vehicle maintenance and depreciation. The three road undertakings give a useful spread:

| Undertaking | Premises maintenance | Gross receipts | Share |
|---|---|---|---|
| Provincial and Scottish bus undertakings | GBP 533,105 | GBP 35,823,033 | 1.49 per cent |
| London Transport road services | GBP 1,269,842 | GBP 42,206,574 | 3.01 per cent |
| British Road Services | GBP 162,322 | GBP 38,850,939 | 0.42 per cent |

The London figure is twice the provincial figure and seven times the road haulage figure. The
difference is consistent with a larger premises estate in London, which included central
works, bus stations and offices as well as garages, but the source does not separate them.
The haulage figure covers goods depots and warehouses. This is a real spread, not a
statistical artefact, and it is the reason a single national depot percentage should carry a
range.

No British source consulted gives the number of garages behind either figure, so a per-garage
rate cannot be derived. The Commercial Motor reports of municipal accounts give combined
"repairs and maintenance" for vehicles only; they do not separate buildings.

### 3.3 What a depot costs to build

Two measured bus garage costs, with a third combined figure, give the capital base to which a
percentage applies:

| Garage | Year | Cost | Floor area | Cost per m2 |
|---|---|---|---|---|
| Glasgow, Larkfield | 1929 | GBP 33,400 | 6,132 m2 | GBP 5.45 |
| Lincoln | 1928 | GBP 13,987 | 1,625 m2 | GBP 8.61 |
| Lincoln, including land and offices | 1928 | GBP 21,857 | 1,625 m2 plus offices | not comparable |

The Glasgow garage was opened alongside a 128-bus fleet and had four bays; the Lincoln garage
was built for 50 buses. Both are single-storey sheds with pits, a wash plant and a repair
shop, which is the closest building type to a pakset depot.

### 3.4 Building benchmarks

Three independent benchmarks bracket the rate:

1. **Seeley (1976)**: "a rough guide to maintenance costs is that they average about 1 per
   cent per annum of capital costs", with the rate rising as the building ages. His table of
   annual equivalent costs, from Drake, gives light industrial buildings a maintenance share
   of 16 per cent against a construction share of 56 per cent; at a construction annual
   equivalent of about 5.5 per cent of capital, that implies about 1.6 per cent a year. The
   1.6 per cent is derived, not stated.
2. **Building Maintenance Information (2003-04)**: a benchmark of 2.5 per cent of capital a
   year averaged across many sectors. This is the upper bound and it includes services and
   decorations.
3. **Constructing Excellence, from BMI 2002-03**: factories carry GBP 400 per 100 m2 of fabric
   maintenance, GBP 500 of services maintenance and GBP 150 of decorations, GBP 10.50 per m2 a
   year in total. A depot with cranes, pits, heating and lighting sits closer to the factory
   row than to an office.

### 3.5 Recommendation

**Depot maintenance: 1.0 to 2.0 per cent of capital a year, central 1.5 per cent.**

- Use the lower half (1.0 to 1.3 per cent) for an open goods shed or a simple stabling shed
  with no plant.
- Use the upper half (1.5 to 2.0 per cent) for a running shed or bus garage with turntables,
  inspection pits, cranes, heating and washing plant.
- Do not use the Midland Railway's 0.2 to 0.4 per cent as a total rate: it is one account
  line and excludes major repairs.

Confidence: **medium-low**. The rate rests on building benchmarks and two system-level
accounts, not on a measured per-depot series. The largest single gap in this report is the
absence of a depot account that states both the maintenance charge and the capital value of
the same building.

---

## 4. Tunnels

### 4.1 The modern railway aggregate

Network Rail's 2023-24 expenditure breakdown gives tunnel renewals of GBP 22m, within civils
renewals of GBP 436m (underbridges GBP 176m, overbridges GBP 69m, major structures GBP 32m,
tunnels GBP 22m, minor works GBP 97m, other GBP 40m). Network Rail states that it is
responsible for 630 tunnels over 335 km. The arithmetic:

- GBP 22,000,000 / 335,000 m = **GBP 65.67 per metre-year**
- GBP 22,000,000 / 630 = **GBP 34,921 per tunnel-year**

This is a renewal rate. Routine examination, drainage clearing, lighting and small repairs are
charged to structures maintenance and are not separated in the published tables, so the true
total upkeep is higher. The figure is nevertheless the best British tunnel number found, and
its denominator is unusually well defined.

### 4.2 The road tunnel comparison, 1973-74

Hansard for 13 October 1975 gives costs excluding debt charges for the five publicly owned
toll crossings in 1973-74. The three tunnels:

| Tunnel | Length used | Annual cost | Cost per metre-year |
|---|---|---|---|
| Mersey (Queensway) | 3,429 m main tunnel | GBP 1.24m | GBP 362 |
| Tyne | 1,700 m | GBP 0.43m | GBP 253 |
| Dartford | 1,400 m, one bore | GBP 0.43m | GBP 307 |

These are upper bounds, not maintenance: the return covers toll collection, policing,
operation, lighting and ventilation as well as repair. They are useful for two reasons. They
show that a road tunnel's total annual operating cost per metre was several times a railway
tunnel's renewal cost per metre in nominal terms, and the gap widens once the fifty years of
price change are allowed for. That difference is what lighting, ventilation and staffing do.
And they show that GBP 250 to 360 per metre-year in 1973-74 money is the right order for a
fully serviced tunnel, not GBP 5 or GBP 50.

### 4.3 The historic capital anchor and the implied rate

The knowledge base records ordinary double-track bored tunnels at GBP 45-145 a metre in 1900,
cut-and-cover in cities at GBP 120-170, and deep tube per bore at GBP 25-61 in 1890-1900. At
1 per cent of capital a year:

- GBP 45/m gives GBP 0.45/m-year
- GBP 145/m gives GBP 1.45/m-year
- GBP 61/m of tube gives GBP 0.61/m-year

No deflator is applied here. The modern GBP 65.67/m-year and the historic GBP 0.45-1.45/m-year
cannot be compared directly across 123 years. The check is qualitative: the two are of the
same order of magnitude once the twentieth-century price level change is allowed for, and the
modern figure is a renewal provision rather than total upkeep. What the two routes do support
is **about 1 per cent of capital a year for a Victorian tunnel**, with the lower end of the
range for a modern deep tunnel whose capital cost per metre is much higher.

### 4.4 What is not measured: lining material

No British source found in this pass gives tunnel maintenance by lining material. The
qualitative expectation is that cast-iron segmental linings need caulking, bolt tightening and
grouting rather than brick replacement; brick linings need brick and mortar repair and are
vulnerable to scaling and sulphate attack; concrete linings need least routine repair but can
spall. The 1932 Severn Tunnel paper describes cementation of 5,500 feet of brick lining with
8,000 tons of cement, but that was a capital treatment, not an annual rate, and the paper is
paywalled.

**Do not encode a lining differential without a measurement.** The honest position is one rate
for all linings, with a note that the range should be wider for brick and narrower for
concrete if a future source supports it.

### 4.5 Recommendation

**Tunnel maintenance: 1.0 per cent of capital a year, range 0.5 to 1.5 per cent.**

- For a modern-era object, cross-check against GBP 65 per metre-year in 2023-24 money.
- For a wet tunnel with mechanical pumping, add the pumping cost separately; the Severn Tunnel
  is the extreme case and no annual figure was found for it.
- Do not use the road tunnel figures of GBP 250 to 360 per metre-year as maintenance: they are
  total operating costs including toll collection and policing.

Confidence: **medium** for the level, **low** for any material differential.

---

## 5. Road signs and traffic signals

### 5.1 Ordinary non-illuminated signs

Two council asset registers give the replacement provision:

| Authority | Signs | Gross replacement | Annualised depreciation | Per sign-year |
|---|---|---|---|---|
| Argyll and Bute, 2024 | 5,013 | GBP 158,244 | GBP 7,912 | GBP 1.58 |
| Wigan, 2015-22 | 15,000 | GBP 2.1m | 12-year life | GBP 11.67 |

The difference is mostly accounting method: Argyll uses a 29-year renewal cycle derived from
its current GBP 52,000 budget (173 signs a year), while Wigan assumes a 12-year sign life and
values the stock at GBP 140 a sign. Argyll's own budget implies GBP 10.37 a sign-year, close to
Wigan's figure. The range GBP 1.6 to 11.7 a sign-year is therefore a range of provisions, not
a disagreement about physical deterioration.

Routine maintenance is smaller than replacement. Sign faces are cleaned at intervals not
exceeding three years (six on gantries) under Design Manual for Roads and Bridges CM 125, and
most repair is reactive after damage. York's officer assumed GBP 75 a repair in 2009, which is
an assumption rather than a contract price. No source found states a routine maintenance
budget per sign.

**Recommendation: GBP 2 to 5 a sign-year in 2024 money, central GBP 3.** This covers cleaning
on a three-year cycle, inspection and minor repair, and excludes replacement, which is capital.
Confidence: **medium**.

### 5.2 Illuminated signs and vehicle activated signs

| Item | Year | Cost per sign-year | Source |
|---|---|---|---|
| Illuminated sign, annualised depreciation | 2024 | GBP 23.08 | Argyll and Bute |
| Illuminated sign, energy | 2014 | GBP 8.17 | DfT impact assessment |
| Illuminated sign, maintenance including lamp cleaning and testing | 2014 | at least GBP 100 | DfT footnote, explicitly unvalidated |
| Vehicle activated sign, maintenance and inspection | 2006 | GBP 250 | Buckinghamshire, from South Gloucestershire 2003-04 |
| Interactive school warning sign | 2011 | GBP 90 | Lancashire |
| Bedford illuminated sign inspection | 2021 | GBP 2.71 | Bedford, inspection only |

The DfT's GBP 100 is the only figure that attempts to cover lamp cleaning, electrical testing
and bulb changing, and the department declined to use it. The two measured vehicle activated
sign figures, GBP 90 and GBP 250, are the better guide for a powered sign because they come
from actual maintenance arrangements. The spread reflects the equipment: a simple lit plate
needs an annual electrical test and occasional lamp work, while a vehicle activated sign has
electronics, a detector and a battery or solar supply.

**Recommendation: GBP 30 to 100 a sign-year for a lit or powered sign, central GBP 50.**
Confidence: **medium-low**, because the only comprehensive figure is unvalidated.

### 5.3 Traffic signals

The three sources agree closely:

| Source | Year | Cost per site-year | Basis |
|---|---|---|---|
| Argyll and Bute revenue budget | 2024 | GBP 1,800 | GBP 45,000 for 25 sites |
| Argyll and Bute annualised depreciation | 2024 | GBP 1,519 | GBP 37,984 for 25 sites |
| DfT, renewal annualised over 12.5 years | 2024 | GBP 1,599 to 2,393 | GBP 19,986 to 29,919 renewal |
| West Sussex contract (report 14) | 2020 | GBP 1,532 to 1,613 | GBP 380,000-400,000 for 248 sites |

The convergence is strong because the DfT's 12.5-year half-life and Argyll's revenue budget
describe the same activity from different directions. **Recommendation: GBP 1,500 to 2,400 a
site-year.** Confidence: **high**.

Report 14 already carries the West Sussex and TfGM figures and the LED economics; this report
adds the Argyll and DfT 2024 corroboration and does not repeat the LED analysis.

---

## 6. Bridges

### 6.1 Cudworth stands

The knowledge base's Cudworth 1886 figures remain the only British per-metre bridge upkeep
series: Belah iron viaduct GBP 0.25/m-year, Deepdale GBP 0.23, Hownes Gill firebrick GBP 0.05,
against plain line at GBP 0.19. Timber deck renewal at GBP 0.52-0.55/m/year is renewal, not
maintenance. Nothing found in this pass contradicts those figures or adds a per-metre series
for masonry arch bridges.

### 6.2 Modern per-structure figures

| Source | Year | Annual figure | Denominator | Per structure-year |
|---|---|---|---|---|
| Local authority bridge maintenance | 2016-17 | GBP 367m | 71,652 bridges | GBP 5,122 |
| Local authority bridge maintenance | 2017-18 | GBP 598m | 71,652 bridges | GBP 8,346 |
| Network Rail bridge and major structure renewals | 2023-24 | GBP 277m | about 29,370 structures | GBP 9,431 |

The local authority figures cover all structures over 1.5 m span, from culverts to major river
bridges, and cover all work charged to bridge maintenance rather than inspection alone. The
Network Rail figure is renewals only and excludes minor works. Neither is comparable with
Cudworth's routine upkeep of an iron viaduct, which excluded deck renewal.

The RAC Foundation's 2022-23 backlog is GBP 6.8bn across 73,208 bridges, about GBP 92,886 a
bridge. That is a whole-life workbank, not an annual rate, and should not be divided by a life
without knowing the condition distribution.

### 6.3 Recommendation

No new recommendation is made for bridges. If a modern-era bridge object needs a rate, the
defensible statement is **GBP 5,000 to 9,500 per bridge-year in 2016-2024 money for an
ordinary road or railway bridge**, with the caveat that this bundles renewal. For the per-metre
rate by construction material, Cudworth remains the authority.

Confidence: **high** for the modern per-structure figures, **unchanged** for Cudworth.

---

## 7. Dead ends

These were pursued and produced no usable figure. They are recorded so that the next pass does
not repeat them.

1. **Severn Tunnel pumping cost.** The 1932 Institution of Civil Engineers discussion on
   cementation says only that the Big Spring "involved an annual expenditure of many thousand
   pounds on pumping". No sum is given in the paper, the discussion or the correspondence, and
   the full paper is paywalled. The Great Western Railway's accounts were not accessible. This
   is the single most important missing drainage figure.
2. **Watson, "Maintenance of Railway Tunnels", ICE Minutes 140 (1900), pp.180-191.** Paywalled.
   The title and keywords show it covers brickwork defects, repairs and costs, which is exactly
   the lining-specific evidence wanted. No text was obtained.
3. **Robarts, "Tunnel Maintenance", ICE Railway Engineering Division Papers 5(5) (1947),
   pp.3-22.** Paywalled. Keywords show Southern Railway tunnels, records, brick lining, repairs,
   drainage and clearance. This is the most likely source of a per-tunnel or per-mile Southern
   Railway maintenance series. No text was obtained.
4. **No British tunnel maintenance series by lining material** was found in any accessible
   source. The qualitative expectation in section 4.4 is not evidence.
5. **Municipal bus and tram accounts.** The Commercial Motor reports and the Board of Trade
   tramway and trolleybus returns give a combined "repairs and maintenance" figure for vehicles
   and a "miscellaneous" column that may include premises, but none separates depot buildings.
   The 1930-31 trackless trolley return, for example, gives Wolverhampton electrical equipment
   GBP 5,474, vehicles GBP 16,680 and miscellaneous GBP 922, with no statement of what
   "miscellaneous" contains.
6. **No per-depot measured account.** The Midland Railway series and the BTC bus series are
   system-level. No account was found that states the maintenance of a named shed or garage
   alongside its capital value.
7. **National per-sign maintenance rate.** The DfT's 2024 local highways maintenance appraisal
   explicitly excludes signage as a sub-asset because of data gaps. The HMEP Method of
   Measurement for Highway Maintenance Services (published through the Institute of Highway
   Engineers) provides a sign-cleaning item and a unit of measurement, but no rate. There is
   no British equivalent of the per-signal-site contract figure for ordinary signs.
8. **Highways guidance.** Searches returned the HMEP method of measurement and DMRB CM 125, both
   of which prescribe frequencies (three-year cleaning, defect rectification times) but not
   costs.
9. **Nottingham bus garage 1929.** The Commercial Motor article states a cost of slightly over
   GBP 100,000 for a 400 ft by 400 ft garage for 200 buses, but the fetch returned only the
   search extract and the page image, so the figure is not used in the CSV.

---

## 8. What this does not support

1. **It does not support a per-depot figure in pounds.** The percentage recommendation is a
   building rate applied to whatever capital value the pakset gives a depot. It is not a
   measured shed account.
2. **It does not support a lining differential for tunnels.** The 1 per cent rate is common to
   all linings. Any brick-against-concrete or iron-against-brick multiplier would be invented.
3. **It does not support using road tunnel costs as maintenance.** The Mersey, Tyne and
   Dartford figures include toll collection, policing and operation.
4. **It does not support a per-metre modern bridge rate.** The modern figures are per
   structure. Cudworth remains the per-metre authority and is 140 years old.
5. **It does not support treating annualised depreciation as maintenance.** The Argyll and
   Wigan sign figures, and the Network Rail tunnel and bridge figures, are capital consumption
   or renewal. They bound maintenance from above and below but are not the same account.

---

## 9. Recommended rates

| Family | Recommendation | Range | Confidence | Basis |
|---|---|---|---|---|
| Depot | 1.5 per cent of capital a year | 1.0-2.0 per cent | medium-low | Seeley 1 per cent; BMI 2.5 per cent; Midland and BTC accounts |
| Tunnel | 1.0 per cent of capital a year | 0.5-1.5 per cent | medium level, low material | Network Rail GBP 65.67/m-year; historic capital GBP 45-145/m |
| Road sign, unlit | GBP 3 a sign-year | GBP 2-5 | medium | Argyll, Wigan, CM 125 cleaning cycle |
| Road sign, lit or powered | GBP 50 a sign-year | GBP 30-100 | medium-low | Argyll depreciation, DfT energy, VAS contracts |
| Traffic signal site | GBP 1,800 a site-year | GBP 1,500-2,400 | high | Argyll, DfT 2024, West Sussex |
| Bridge | no new rate; Cudworth stands | GBP 5,000-9,500 per structure-year if a modern rate is needed | high for modern, unchanged for Cudworth | RAC Foundation, Network Rail |

---

## 10. Sources

**Measured accounts and contracts**: Midland Railway locomotive department accounts via
Dodgson (2008) and Johnson (1898); British Transport Commission annual report for 1949 via
*Commercial Motor*, 22 September 1950; Argyll and Bute Council Annual Status and Options
Report, January 2024; Wigan Council Highway Asset Management Strategy 2015-2022; Bedford
Borough Council Illuminated Signage Asset Strategy, December 2021; City of York Council
Street Furniture Removal report, 20 October 2009; Buckinghamshire County Council Vehicle
Activated Signs policy, 7 March 2006; Lancashire County Council 20mph Sign Only Scheme report,
4 February 2011; West Sussex traffic signal contract as recorded in report 14.

**Government and regulator**: Department for Transport, Economic Appraisal for Investing in
Local Highways Maintenance, November 2024; Department for Transport, Traffic Signs Review
Impact Assessment, 28 April 2014; Network Rail, Annual expenditure 2023-24; Network Rail,
Capability Assessment Tool for Tunnel Masonry Linings, 2019; Office of Rail and Road, PR23
final determination and cost benchmarking report 2023-24; Hansard, 13 October 1975, cc545-6W;
Design Manual for Roads and Bridges CM 125, Maintenance of traffic signs, revision 1, 2020.

**Benchmarks and research**: Seeley, *Building Maintenance* (Macmillan, 1976); Building
Maintenance Information, Review of Maintenance Costs 2003 and 2004, as quoted by London
Economics, *The Cost of Space* (2005); Constructing Excellence, *Whole Life Costing* fact
sheet, from BMI 2002-03; RAC Foundation bridge maintenance reports for 2017-18, 2021-22 and
2022-23; Dodgson, *TFP Growth Using Perpetual Inventory of Capital: Midland Railway Locomotive
Power in the Late Nineteenth Century* (2008).

**Paywalled and not used as evidence**: Watson, "Maintenance of Railway Tunnels", ICE Minutes
140 (1900); Robarts, "Tunnel Maintenance", ICE Railway Engineering Division Papers 5(5)
(1947); Carpmael, "Cementation in the Severn Tunnel", ICE Minutes 234 (1932).
