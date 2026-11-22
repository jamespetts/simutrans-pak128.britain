---
status: draft
verified: none
---

# Research report 17: maglev guideway construction and maintenance cost, overseas systems

**Covers**: guideway-only construction cost per route-km and per track-km for the Shanghai
Transrapid, the Incheon Airport Maglev, Linimo, the Chuo Shinkansen, the Changsha Maglev Express
and Beijing S1, plus the German Transrapid cost estimates and the Emsland test facility; what each
figure includes; a labour-cost adjustment to United Kingdom levels; and maglev maintenance per
km-year.

All figures are nominal money of the year and currency stated. No deflation and no inflation to a
common price level has been applied anywhere. No Simutrans `.dat` price was used as evidence and no
figure was fitted to the pakset. Nothing under `New/` was modified and no git command was run.

Evidence base: 52 rows in `research-pricing-rows-17.csv`. Domains: 42 construction, 4 maintenance,
1 operating, 5 labour index. Every row carries its scope; the scope column is the authoritative
statement of what each number includes.

---

## 1. The answer in one page

1. **Only one system publishes something close to a guideway-only figure as built: Linimo.** The
   Aichi prefectural government splits the JPY 99.7bn cost into JPY 64.1bn of public
   infrastructure (piers, girders and the civil structures of nine stations, over 9.15 km of double
   track) and JPY 35.6bn of infrastructure-external works (vehicles, electrical installations,
   depot, station equipment). That is **JPY 3.50bn per track-km, about GBP 17.5m at the 2005
   rate**, and it includes nine stations in 9.15 km plus 1.4 km of tunnel, so it is an upper bound
   for open elevated guideway.

2. **No system publishes a guideway-only figure for a high-speed maglev.** The Shanghai final
   account is documented to the last million (RMB 9,943m for 29.873 km double track, including
   vehicles, substations, auxiliary facilities and interest), and the two German contracts are
   documented (DM 1,293m for equipment and services, DM 100m for guideway technology). The civil
   residual is therefore recoverable at RMB 4,664m, but the guideway's share of that residual is
   not published. **A guideway-only figure of RMB 51-62m per track-km is an inference, not a
   measurement.**

3. **The best-evidenced guideway-only pair is German and is an estimate, not an outturn.** The
   independent Hamburg-Berlin cost calculation puts the Transrapid guideway at **DM 21.0m per
   route-km at grade and DM 26.5m per route-km elevated (1993), double track, guideway structure
   and piers only**, excluding the stator support rail, switches, land, project management,
   stations, power and vehicles. The same document records an official estimate of DM 15.0m per
   route-km, so the estimate is 1.9 times the official figure and the truth is unknown, because the
   line was never built.

4. **At grade is about 80 per cent of elevated, not the one third that urban rail practice would
   imply.** Two independent sources agree: the 1993 German estimate gives 79 per cent (DM 21.0
   against 26.5) and the 2007 Munich planning estimate gives 82 per cent (EUR 20.20 against 24.70
   per route-km). The reason is that a maglev "at grade" guideway is a low bridge structure, not
   ballasted track on a formation; the beam is the cost and the piers are a small increment. **A
   pakset that prices an at-grade maglev way at a fraction of a viaduct would be wrong.**

5. **The labour adjustment is defensible in direction and rough size, and it is large for China.**
   Turner & Townsend put the UK average construction wage at USD 50 an hour and Shanghai structural
   trades at USD 7 an hour (2024). With guideway civil works at an assumed 25 per cent labour, the
   uplift from Shanghai costs to UK costs is **2.54 times** (range 1.92 to 3.15 for a 15 to 35 per
   cent labour share). For Japan the uplift is 1.18 times, for Korea 1.21 and for Germany 0.96.
   Without the adjustment, Chinese figures understate a UK guideway by a factor of about 2.5.

6. **Recommended United Kingdom guideway rate: GBP 8-12m per track-km elevated and GBP 6.5-9.5m
   per track-km at grade, central values GBP 10m and GBP 8m, in the money of the year of the
   reference project.** Three independent derivations land between GBP 8.1m and GBP 10.9m per
   track-km elevated after adjustment (Munich 2007, Shanghai 2004, China 2022); the as-built Linimo
   infrastructure part at GBP 20.6m is the upper bound and the 1993 Hamburg-Berlin estimate at GBP
   5.1m is the lower bound. The nominal sterling cost of a Chinese guideway barely moved between
   2004 and 2023, so the range is not sensitive to which year is chosen.

7. **Maintenance per km-year is not measured anywhere.** The only quantitative split between
   guideway and systems is a 1992 Volpe model, and it says the systems cost about 5.8 times the
   guideway structure to maintain in materials (USD 15,500 against USD 2,650 per single guideway
   mile-year). The only published per-track-km-year maglev maintenance figure is an estimate for an
   unbuilt Saudi line, EUR 12,300 at 2009 prices. Linimo's whole-line operating expense is JPY
   137.8m per route-km-year (2023), but that is operations, stations and traction power, not
   guideway maintenance.

---

## 2. What each system actually published

### 2.1 Shanghai Transrapid (China, 2001-2004)

The financial record is unusually complete for the total and unusually incomplete for the guideway.

| Item | Amount | What it covers |
|---|---|---|
| Approved budget estimate | RMB 10,029.9m | whole project |
| Final account, April 2004 | RMB 9,943m | track, vehicles, substations, auxiliary facilities, interest during construction |
| NDRC stated actual unit cost | RMB 310m per route-km | implies about RMB 9,260m, probably excluding interest |
| German equipment and services contract, Jan 2001 | DM 1,293m | vehicles, operation control, propulsion and power supply, stator packs and winding cables, switch steel bending girders |
| German guideway technology contract, Jan 2001 | DM 100m | concrete composite girder system |

The line is 29.873 km of double track, so the whole system cost RMB 333m per route-km, or **RMB
166m per track-km**, in 2004. Routes to a guideway figure:

- The two German contracts convert to about RMB 5,280m at the 2001 average of DM 3.79 per RMB,
  leaving **RMB 4,664m** of Chinese-side cost. That residual contains the guideway girders, piers,
  the 20,000 piles of 40-60 m driven in soft ground, two stations, the maintenance base, the girder
  factory, land, installation of the German equipment, design and management.
- Taking the guideway as 65 to 80 per cent of that residual gives **RMB 51-62m per track-km**, or
  GBP 3.4-4.1m at the 2004 rate of RMB 15.17 per GBP.
- The Siemens 2001 comparison chart puts the Shanghai fixed installation at **EUR 42.2m per
  double-track km with vehicles excluded**, which is EUR 21.1m per track-km, consistent with a
  fixed installation of about EUR 1.2bn. The chart's row-to-system mapping was read from a text
  extraction and is uncertain, so this row is marked indicative.

**Dead end**: no Chinese source found gives the guideway girder or civil works as a separate line
item. Searches in Chinese for the 工程决算 breakdown, for 轨道梁 unit prices and for 土建 versus
设备 shares returned the total, the two contracts and the girder count (about 2,550 girders), but no
civil subtotal.

### 2.2 Linimo / Tobu Kyuryo Line (Japan, 2002-2005)

The Aichi prefectural government publishes the split that every other operator withholds:

| Item | Amount (actual) | Amount (initial plan) |
|---|---|---|
| Infrastructure: piers, girders, station civil structures, built by the prefecture and Nagoya city | JPY 64.1bn | JPY 67.0bn |
| Infrastructure-external: vehicles, electrical installations, management building, station equipment, depot, built and operated by Aichi Rapid Transit | JPY 35.6bn | JPY 40.5bn |
| Total | JPY 99.7bn | JPY 107.5bn |

9.15 construction km, double track, elevated with 1.4 km underground, nine stations. The
infrastructure part is **JPY 7.00bn per route-km and JPY 3.50bn per track-km**. The railway's own
chronology records that vehicle cost, power line cost, the management building and station
equipment are all classed as infrastructure-external, which implies that station civil structures
sit inside the public infrastructure part. Nine stations in 9.15 km and a 1.4 km cut-and-cover
section make this an upper bound for open elevated guideway, not a central estimate.

This is the single most useful as-built row in the set, because the boundary between public
infrastructure and operator infrastructure is stated by the funder rather than inferred.

### 2.3 Incheon Airport Maglev (Korea, 2010-2016)

KRW 414.9bn for 6.113 km of double track, six stations, a depot and four two-car trains. That is
**KRW 67.9bn per route-km and KRW 33.9bn per track-km**, about USD 28m per track-km at the 2016
rate. The funding shares are documented (government 69 per cent, airport 25 per cent, city 6 per
cent) and a further KRW 100bn of research spending is sometimes added. Construction ran from 2010 to
2012 and test running from 2012 to 2014; the source does not say which phases the KRW 414.9bn
covers.

**Dead end**: no Korean source found gives a breakdown by 공종 (civil, track, station, electrical,
signalling, vehicle). With six stations in 6.1 km, this line is station-dominated and its per-km
figure cannot be used as a guideway rate.

### 2.4 Chuo Shinkansen (Japan, 2014 onwards)

The construction implementation plan gives a clean split for the 285.6 km Shinagawa-Nagoya section:

| Item | Amount (2014) | Per route-km |
|---|---|---|
| Civil structures (tunnels, viaducts, bridges, formation, land) | JPY 4,015.8bn | JPY 14.06bn |
| Electrical facilities | JPY 837.8bn | JPY 2.93bn |
| Total including rolling stock | JPY 5,523.6bn | JPY 19.34bn |
| Revised total, 2023 | JPY 7,048.2bn | JPY 24.68bn |

The structure lengths are 246.6 km tunnel (86 per cent), 23.6 km viaduct, 11.3 km bridge and 4.1 km
formation. **The civil cost of JPY 14.06bn per route-km is not a guideway rate**; it is a tunnel
rate with a small viaduct tail. It is useful only as a hard upper bound and as proof that a
high-speed maglev alignment in difficult terrain is a tunnelling project, not a guideway project.

### 2.5 Changsha Maglev Express and the Chinese component rates (China, 2014-2016 and 2022)

The Changsha line is the most transparent Chinese scheme:

- 18.55 km, three stations, one depot, of which 1.13 km at grade and 17.42 km elevated.
- Total investment RMB 4,290m (Xinhua, 2016); the EPC contractor records RMB 4,600m total and a
  RMB 2,770m EPC contract price covering design, procurement, construction and commissioning.
- Whole system: **RMB 231m per route-km, RMB 116m per track-km**, GBP 12.8m per track-km at the
  2016 rate.

More useful than the whole-scheme figure are the unit rates published in a 2022 Changsha S1 mode
comparison, which are component-level and directly usable:

| Component | RMB per double-track km | RMB per track-km |
|---|---|---|
| Elevated viaduct, superstructure and piers, side-by-side single-track U-beams | 54m | 27m |
| Track panel (F-rail, reaction plate, sleepers, fastenings) | 22m | 11m |
| **Elevated guideway including track** | **76m** | **38m** |
| Shield tunnel, 6.2 m internal diameter | 166m | 83m |
| Elevated station | RMB 8,500 per m2 of floor area | |
| Underground station | RMB 13,800 per m2 of floor area | |

At the 2023 rate of RMB 8.81 per GBP, RMB 38m per track-km is **GBP 4.3m per track-km**. These
rates are for a 100-120 km/h medium-low-speed maglev; a 430 km/h Transrapid girder is a heavier and
more precisely machined structure (165 t, 25 m span, 2.2 m deep, milled steel flanges) and costs
more.

### 2.6 Beijing S1 (China, 2015)

RMB 8,900m for 10.21 km, eight stations and one depot, from the cost consultant that audited the
initial-design budget. That is RMB 872m per route-km, 3.8 times the Changsha rate. With eight
stations in 10.2 km the line is station-dominated; the figure is recorded for completeness and is
not usable as a guideway rate.

### 2.7 German Transrapid estimates and the Emsland test facility

The Hamburg-Berlin cost calculation (1993 price level) is the only source that separates the
guideway from everything else and separates at grade from elevated:

| Item | Rate | Note |
|---|---|---|
| Guideway at grade, the beam on a prepared formation 0.1-2 m high, including foundations | DM 21.0m per route-km | justified as the cost of a double-track railway bridge superstructure without track or piers |
| Piers and columns (Aufständerung), on 140 km of the 294 km route | DM 5.5m per route-km | so elevated is DM 26.5m per route-km |
| Stator support rail | DM 2.1m per route-km | a system component, not civil works |
| Switches | DM 109m total | |
| Land | DM 365m total | |
| Project management | DM 245m total | |
| Official estimate for guideway and special structures | DM 15.0m per route-km | the independent re-estimate is DM 29.0m, 1.9 times higher |

The manufacturer's own figure, quoted second-hand, is EUR 17m per km of double guideway (scope
otherwise unstated).

The Emsland test facility adds one figure of limited use: DM 422m was budgeted for the first 12 km
section, of which about DM 60m was for a vehicle. That is DM 30.2m per km if the basis really is
12 km, or DM 17.7m if the basis is the 20.5 km first construction phase. The facility is single
track, has switches and a test centre, and has no stations, so it is not a commercial rate. Federal
spending on the facility from 1970 to 2008 was about EUR 800m, more than half of it construction,
but no construction-only split is published.

---

## 3. Guideway-only figures, and how far each is an inference

| System | Year | Figure as published | Guideway only? | Basis |
|---|---|---|---|---|
| Linimo infrastructure part | 2005 | JPY 3.50bn per track-km | Nearly: piers, girders, station civil structures | As-built, published split |
| Shanghai, derived | 2004 | RMB 55m per track-km (51-62) | Yes, by inference | Residual after German contracts, 65-80 per cent attributed to guideway |
| Hamburg-Berlin at grade | 1993 | DM 10.5m per track-km | Yes | Engineering estimate |
| Hamburg-Berlin elevated | 1993 | DM 13.25m per track-km | Yes | Engineering estimate |
| Chinese elevated viaduct plus track | 2022 | RMB 38m per track-km | Yes | Published component unit rates |
| Chinese elevated viaduct only | 2022 | RMB 27m per track-km | Yes, structure only | Published unit rate |
| Munich at grade | 2007 | EUR 10.1m per track-km | No: fixed infrastructure | Planning estimate, scope inherited |
| Munich elevated | 2007 | EUR 12.35m per track-km | No: fixed infrastructure | Planning estimate, scope inherited |
| Incheon | 2012 | KRW 33.9bn per track-km | No: whole system | As-built |
| Changsha | 2016 | RMB 116m per track-km | No: whole system | As-built |
| Beijing S1 | 2015 | RMB 436m per track-km | No: whole scheme | Budget estimate |
| Chuo Shinkansen civil | 2014 | JPY 7.03bn per track-km | No: civil works, 86 per cent tunnel | Approved plan |

The pattern is that the two figures which are genuinely guideway-only (German 1993, Chinese 2022)
are both estimates or unit rates rather than outturns, and the two figures which are outturns
(Linimo, Shanghai derived) both contain station civil works.

---

## 4. At grade against elevated

Two independent sources give the ratio:

- German 1993 estimate: DM 21.0 at grade against DM 26.5 elevated per route-km, a ratio of 0.79.
- Munich 2007: EUR 20.20 against EUR 24.70 per route-km, a ratio of 0.82.

The Chinese rule of thumb for urban rail, that at grade, elevated and underground costs run
1:3:6, does **not** apply to maglev. That rule assumes at-grade means a formation with ballasted
track. A maglev at grade still needs a precise concrete or steel beam, and in poor ground it still
needs piling: the Shanghai line is carried on about 20,000 piles of 40-60 m over its whole length,
at grade sections included.

**Recommendation for the pakset: price an at-grade maglev way at 0.78-0.82 of the elevated rate,
not below it.** The saving from omitting piers is about one fifth of the guideway cost.

---

## 5. Labour adjustment

### 5.1 Method

For each system, cost in the source country is split into a labour part and a material and plant
part, the labour part is repriced at the United Kingdom rate, and the material and plant part is
left unchanged:

    adjusted = cost x [(1 - L) + L x (w_UK / w_source)]

where L is the labour share of the works and w is the construction wage per hour, employer cost.

### 5.2 Index used

Turner & Townsend, *International Construction Market Survey 2024*, which reports employer cost
per hour including travel, pension, health insurance and other on-costs, on a consistent basis
across markets. The relevant entries:

| Market | Structural trades, USD per hour |
|---|---|
| United Kingdom, average | 50 (2023: 45) |
| London | 56.8 (2025 edition) |
| Shanghai | 7 |
| Tokyo | 29 |
| Seoul | 27 |
| Munich | 60 |

The survey also gives whole-market averages, including Asia at USD 13 an hour and the United
Kingdom at USD 50; the 2021 edition of the same survey put continental Europe at USD 53.7 and the
United Kingdom at USD 45.4, but the two editions are not directly comparable because the 2024
figures are converted at different exchange rates.

### 5.3 Size of the adjustment

At a 25 per cent labour share:

| Source | Wage ratio to the UK | Adjustment factor |
|---|---|---|
| China | 7.14 | 2.54 |
| Japan | 1.72 | 1.18 |
| Korea | 1.85 | 1.21 |
| Germany | 0.83 | 0.96 |

Sensitivity to the labour share, for China: 15 per cent gives 1.92, 25 per cent gives 2.54, 35 per
cent gives 3.15.

Applied to the guideway figures:

| System | Nominal | Adjusted to UK |
|---|---|---|
| Shanghai derived, 2004 | GBP 3.6m per track-km | GBP 9.2m per track-km |
| Chinese elevated viaduct plus track, 2022 | GBP 4.3m per track-km | GBP 10.9m per track-km |
| Linimo infrastructure, 2005 | GBP 17.5m per track-km | GBP 20.6m per track-km |
| Munich elevated, 2007 | GBP 8.45m per track-km | GBP 8.1m per track-km |
| Hamburg-Berlin elevated, 1993 | GBP 5.34m per track-km | GBP 5.1m per track-km |

### 5.4 Limits of the method

1. **The labour share is not measured.** No source found states the labour content of a maglev
   guideway. The 25 per cent assumption rests on the material intensity of precast concrete and
   steel structures, and the sensitivity band above is the honest expression of that.
2. **Wage per hour is not unit labour cost.** A Shanghai crew uses more hours per tonne of girder
   than a British crew, so the true labour cost ratio per km is smaller than the wage ratio. The
   output-based composite rates in the same survey show this: excavation in Shanghai is USD 10 per
   m3 against USD 65 in Munich, a gap of 6.5 to 1, while the hourly structural-trade gap between
   Shanghai and Munich is 8.6 to 1. The productivity offset is therefore real but modest for civil
   work, and it does not overturn the direction of the adjustment.
3. **Materials are held at source prices.** Chinese cement and reinforcement are cheaper than
   British, so the adjustment understates the Chinese-to-UK gap on materials and therefore
   understates the total. The direction is known, the size is not.
4. **The wage ratio used is the 2024 one, applied to projects built in 2004-2016.** Chinese
   construction wages rose much faster than British ones over that period, so the historical ratios
   were larger and the 2004 Shanghai adjustment in particular is understated.
5. **No adjustment is made for the exchange rate at the time of construction.** The Shanghai figure
   is converted at the 2004 average; a 2001 conversion would give a different answer because the
   euro and the dollar moved against the renminbi.

Despite those limits the adjustment is defensible: the direction is certain, the order of magnitude
(about 2.5 times for China, about 1.2 for Japan and Korea, about 1.0 for Germany) is stable across
the plausible labour-share range, and the conclusion that Chinese guideway costs cannot be
transferred to a British pakset without a large uplift is robust.

---

## 6. Recommended rate

**Elevated guideway, United Kingdom equivalent: GBP 8-12m per track-km, central GBP 10m.**
**At grade: GBP 6.5-9.5m per track-km, central GBP 8m**, derived as 0.8 of the elevated figure.

Basis, three independent routes to the band, with an as-built upper bound and a planning lower
bound:

| Route | Elevated, UK adjusted |
|---|---|
| Shanghai, derived guideway, adjusted | GBP 9.2m per track-km (2004 money) |
| Chinese component rates, adjusted | GBP 10.9m per track-km (2023 money) |
| Munich planning estimate, adjusted for German wages | GBP 8.1m per track-km (2007 money) |
| Linimo infrastructure part, adjusted | GBP 20.6m per track-km (2005 money), upper bound because of nine stations and 1.4 km of tunnel |
| Hamburg-Berlin guideway, adjusted | GBP 5.1m per track-km (1993 money), lower bound because it is an estimate for a line that was never built |

The band is deliberately wide because the labour share is assumed. It should be read as a range
whose central value is GBP 10m, not as a precise figure.

Two observations support the central value:

- **Nominal sterling cost barely moved between 2004 and 2023.** The Shanghai guideway was GBP 3.6m
  per track-km in 2004 and the Chinese component build-up is GBP 4.3m per track-km in 2023. Chinese
  construction costs in renminbi rose substantially over that period, but the renminbi also
  appreciated against sterling (RMB 15.17 to the pound in 2004 against RMB 8.81 in 2023) and the
  Chinese-to-UK wage ratio narrowed, so the adjusted figures converge. Part of the convergence is
  offsetting product difference rather than pure price movement, because the 2023 rate is for a
  100-120 km/h U-beam and the 2004 rate is for a 430 km/h Transrapid girder, so the comparison is
  indicative rather than exact.
- **The British elevated-structure cross-check is consistent.** The DLR City Airport viaduct is
  recorded at GBP 19-24m per km in 2005. If that is per route-km of double-track viaduct, it is GBP
  9.5-12m per track-km, which brackets the recommendation.

For a high-speed (400-500 km/h) guideway rather than a 100-120 km/h urban one, the upper half of
the range should be used: the girder is heavier, the tolerances are millimetre-scale, and the
Shanghai girder needed a purpose-built casting yard with a 100 x 200 m hall.

---

## 7. Maintenance

No operator publishes a guideway maintenance cost per km-year, and none publishes a split between
guideway and systems. What exists is three different things:

**A parametric model (Volpe, 1992).** The Federal Railroad Administration's maglev cost model gives,
per single guideway mile-year:

| Item | Quantity | Basis |
|---|---|---|
| Guideway structure, material | USD 2,650 | 0.0625 per cent a year of USD 4.25m per single guideway mile |
| Systemwide electrical, material | USD 15,500 | 0.536 per cent a year of USD 2.9m per single guideway mile |
| Guideway inspection labour | 200 hours | plus 8 per cent for foremen |
| Switches, material | USD 9,500 each | 0.5 per cent a year |

Converting: about USD 1,646 per track-km-year of guideway material and about 124 labour hours per
track-km-year, which at the report's own rate is about USD 2,240, so **about USD 3,900 per
track-km-year for the guideway structure in 1992 money**, and **about USD 9,630 per track-km-year
for the electrical systems in materials alone**. The model therefore says the electrical systems
cost about 5.8 times the guideway structure to maintain, which is the opposite of the usual
assumption that the guideway dominates.

**One literature estimate (Almujibah and Preston, 2018).** EUR 12,300 per track-km-year at 2009
prices for regular maintenance of the whole line, for a proposed Riyadh-Dammam maglev. This is an
estimate, not a measurement. Adding the model's four components (guideway material USD 1,646 and
labour USD 2,238, electrical material USD 9,632 and labour USD 3,355) gives about **USD 16,900 per
track-km-year in 1992 money**, which at 2009 prices is about EUR 19,000, or roughly 1.5 times the
Almujibah figure. The two are the same order of magnitude. The model is the higher of the two,
which is the expected direction for a parametric model that assumes a full maintenance organisation.

**One operator's accounts (Linimo, FY2023).** Transport operating expenses of JPY 1,226m, or JPY
137.8m per route-km-year and about JPY 68.9m per track-km-year (about GBP 390,000 at the 2023 rate
of JPY 174.7 to the pound). This covers staff, traction power, station operation, maintenance and
renewals charged to revenue, and excludes depreciation. It is an order of magnitude above the model
because it is an operating account, not an infrastructure maintenance account, and it is not split.

**Conclusion for the pakset**: use a guideway maintenance rate of roughly 1-2 per cent of guideway
capital a year, with the electrical and signalling systems at about five times the guideway rate.
That is a modelled relationship, not a measured one, and it should be tagged as such.

---

## 8. Consistency checks

1. **Guideway as a share of whole system.** Guideway at GBP 10m per track-km against whole-system
   figures of GBP 11.0m (Shanghai), 12.8m (Changsha), 21.6m (Incheon) and 40.3m (Chuo) per
   track-km gives a guideway share of 90, 78, 46 and 25 per cent. Shanghai and Changsha were cheap,
   lightly stationed lines where the guideway does dominate; Incheon and Chuo were not. The
   ordering is plausible.
2. **Two at-grade-to-elevated ratios, two countries, fourteen years apart, agree to three
   percentage points** (0.79 and 0.82). That is the strongest structural finding in the set.
3. **The German official estimate is half the independent estimate.** Any rate taken from German
   planning documents carries a factor-of-two uncertainty that no labour adjustment can remove.
4. **The Chinese component rates are coherent.** Viaduct 27 plus track 11 equals 38 per track-km
   for the elevated section. The Changsha line is 94 per cent elevated, so the guideway accounts for
   about RMB 38m of its RMB 116m whole-system cost per track-km; the remaining RMB 78m is stations,
   depot, systems, vehicles and land. That is the right shape for a three-station urban line.

---

## 9. Dead ends

1. **No guideway-only as-built cost for any high-speed maglev.** Shanghai's civil works are not
   published as a line item; the Chinese cost paper on maglev girder erection (Guo Sanwei,
   Railway Engineering Technology and Economy 36(5), 2021) is behind a paywall and only its
   abstract is available, and the abstract contains no figures.
2. **No Incheon breakdown by work package.** Korean-language searches returned the funding shares
   and the programme budget but no 공종 split.
3. **No Chuo Shinkansen viaduct unit cost.** JR Central publishes civil and electrical totals and
   structure lengths, not rates by structure type.
4. **No Chengdu maglev line with published costs.** Chengdu has a short test facility associated
   with Southwest Jiaotong University; no commercial line and no cost figure was found. Recorded as
   a dead end rather than a nil.
5. **No Shanghai girder unit price.** The girder count (about 2,550) and the casting yard are
   documented; the price per girder is not.
6. **No official Emsland construction cost per km.** Only the DM 422m first-section budget, whose
   length basis is ambiguous, and the EUR 800m total federal spend which mixes construction with
   38 years of operation.
7. **No measured maglev maintenance series.** No operator publishes guideway maintenance per km and
   none publishes a guideway-versus-systems split. The Volpe model is 34 years old.
8. **No measured labour share of guideway construction.** This is the largest single assumption in
   the report.
9. **The Munich figures were not independently verified in this pass.** They are carried as
   inherited from the requesting session and their scope, in particular whether stations and
   operation control are inside, is unconfirmed.
10. **The Siemens 2001 comparison chart was read from a text extraction.** The row-to-system mapping
    is uncertain and the Shanghai 42.2 and Hamburg-Berlin 33.1 figures should be treated as
    indicative only.

---

## 10. Confidence

| Finding | Confidence | Why |
|---|---|---|
| Shanghai total cost and its composition | High | Final account, two independent official statements, contract values |
| Shanghai guideway-only figure | Low | An inference from a residual, 65-80 per cent assumption |
| Linimo infrastructure split | High | Published by the funder, with the boundary stated |
| Linimo as a guideway rate | Medium | Includes nine stations and 1.4 km of tunnel |
| Chuo civil cost | High | Approved plan |
| Chuo as a guideway rate | Very low | 86 per cent tunnel; upper bound only |
| Incheon, Changsha, Beijing totals | High | Official or audited |
| Their use as guideway rates | None | Whole system |
| German 1993 guideway pair | Medium | Careful engineering estimate, but 1.9 times the official figure and never built |
| At grade = 0.8 of elevated | High | Two independent sources |
| Wage ratios | High | Published, consistent methodology |
| Labour share of 25 per cent | Low | Assumption, no measured source |
| Recommended GBP 8-12m per track-km | Medium | Three independent routes converge, but each carries its own assumption |
| Maintenance per km-year | Low | Modelled, not measured |

---

## 11. Sources

Primary and official:

- Wu Xiangming, *Achievements of Shanghai Maglev Demonstration Operation Line and the Maglev
  Development Strategy*, Maglev 2004.
- Xinhua via gov.cn, 26 April 2006, archived, for the NDRC unit cost and the 29.873 km length.
- SMTDC official chronology, for the two German contracts and their values.
- Eberhard Grossert, *Transrapid Shanghai: Construction of the First Commercial Operational Line*,
  Promet 15 (2003) 117-125, for the girder, piling and alignment detail.
- Aichi Prefecture, Tobu Kyuryo Line (Linimo) project page, for the infrastructure split.
- Aichi Rapid Transit, 25th business report, for transport operating expenses.
- Ministry of Land, Infrastructure, Transport and Tourism (Japan), approval of the Chuo Shinkansen
  construction implementation plan part 1, 17 October 2014.
- JR Central, construction implementation plan part 3, December 2023.
- International Railway Journal, 3 February 2016, for the Incheon total.
- Xinhua via People's Daily, 6 May 2016, and the CRFSDI EPC case study, for Changsha.
- Beijing Municipal Engineering Consulting Corp project page, for Beijing S1.
- Chen Yang, *Changsha S1 system comparison study*, for the Chinese component unit rates.
- Verkehrsconsult Dresden, *Wirtschaftlichkeit des Transrapid-Vorhabens Hamburg-Berlin*, for the
  German guideway cost breakdown.

Secondary:

- Volpe National Transportation Systems Center, *Maglev Cost Estimation: Annual O&M Cost Elements*,
  March 1992.
- Almujibah and Preston, *The total social costs of constructing and operating a maglev line*,
  Transportation Systems and Technology 4(3) Suppl. 1 (2018).
- Turner & Townsend, *International Construction Market Survey 2024* and *Global construction
  market intelligence 2025*.
- *Survey of foreign maglev systems*, 1992 (doi:10.2172/10134413), for the USD 15-25m per km of
  double track general estimate.

---

## Appendix: conversion rates used in this report

The CSV rows carry no conversion: every price is in the currency of its own source. The rates below
are approximate annual averages, used only to compare the rows in this report, and are not evidence
in themselves.

| Year | Rate used | Currency per GBP |
|---|---|---|
| 1993 | DM 2.483 | DEM |
| 2001 | DM 3.15 | DEM |
| 2004 | RMB 15.17 | CNY |
| 2005 | JPY 200.6 | JPY |
| 2007 | EUR 0.6843 | EUR |
| 2012 | KRW 1,573 | KRW |
| 2014 | JPY 174.5 | JPY |
| 2016 | RMB 9.01 | CNY |
| 2023 | RMB 8.81 | CNY |
| 2023 | JPY 174.7 | JPY |

A conversion made at a different point in a multi-year project, or at a different point in the
exchange-rate cycle, changes any of the sterling comparisons above by up to 30 per cent. The
renminbi moved from about RMB 11.9 to the pound in 2001 to RMB 15.2 in 2004, so the choice between
those two dates alone moves every Shanghai sterling figure by 27 per cent. The two German contracts
have been converted into renminbi at the 2001 cross-rate (DM 3.79 to the renminbi) so that they can
be subtracted from a renminbi account, which is an approximation to the rates at which they were
actually booked.
