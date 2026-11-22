# Deep research: additional British vehicle and infrastructure cost data

**Date**: 2026-11-22
**Scope**: nominal British (UK and Ireland) vehicle and infrastructure costs, c.1750-2000, for the
pak128.Britain-Ex cost-balancing project. This is a research record only. No `.dat` file, config
file or knowledge-base document has been changed.

**Outputs**

| File | Contents |
|---|---|
| `ai/temp/research-pricing-rows.csv` | 80 rows, same schema as `individual-price-rows.csv` |
| `ai/temp/research-pricing-report.md` | this report |
| `ai/temp/whishaw-1842-railway-costs.md` | draft evidence doc for the Whishaw 1842 source family |
| `ai/temp/build_research_rows.py` | generator for the CSV, so rows can be regenerated or audited |

---

## 1. What was searched

One search per turn, as the workspace rules require, plus direct fetches of known full-text
repositories.

**Searches**

1. Board of Trade *Railway Returns*: maintenance of rolling stock per train mile and per vehicle,
   1900-1925.
2. Tramcar purchase prices 1905-1925 from municipal tramway accounts.
3. Locomotive repair cost per engine mile, LMS/LNER 1920s-1930s.
4. *Commercial Motor* complete double-decker prices 1948-1962.
5. *Flight* / contemporary British airliner list prices 1930s.

**Direct sources fetched and read**

- Whishaw, *The Railways of Great Britain and Ireland* (1842), complete Wikisource transcription:
  760 page transcriptions pulled through the MediaWiki `action=raw` endpoint and searched locally.
  This is the single largest addition and is written up separately.
- Lardner, *Railway Economy* (1850), archive.org OCR. Read and **rejected** for cost calibration:
  its per-vehicle-mile figures are the author's own allocation model ("charge per mile on each
  vehicle"), not measured accounts. Do not cite it as evidence.
- Board of Trade *Railway Returns for 1907* (archive.org `op1255486-1001`) and the 1908 volume
  (`railwayreturns00britgoog`). Read; the per-company expenditure tables are unusable in OCR (see
  §4).
- *Blackpool Trams* (LTH Library PDF, 140 pp). Read; yields the only complete British tram
  component-price ladder found, 1947-1983.
- East London Railway Joint Committee, *Financial Accounts and Statistical Returns 1936* (PDF).
  Read; maintenance total only, no vehicle counts (see §4).

All dates are the year the source states. Where Whishaw describes a railway without giving a year,
the row is dated 1839, his main tour year; his observations run 1839-1841 and the book was published
in 1842. Currency is sterling unless stated; no conversion, deflation or currency translation has
been applied anywhere in the CSV.

---

## 2. What was found, by domain and era

### 2.1 Locomotives

**Pre-1850: the largest single gain.** Whishaw gives a dated ladder of fifteen locomotive prices
1833-1840 (fourteen new-build, one second-hand), nearly all with cylinder dimensions, wheel
arrangement and weight, and with the tender treatment stated:

| Year | Railway / engine | Price | Tender |
|---|---|---|---|
| 1833 | Dundee & Newtyle, Stirling engines | £700 | excluded (£30 extra) |
| 1836 | Dundee & Newtyle, *John Bull* | £1,137 | included |
| 1839 | Clarence Railway, six-coupled coal engine | £900 | included (£40 of it) |
| 1839 | Neath Abbey *Camel* / *Elephant* | £725 / £800 | included |
| 1839 | Ardrossan & Johnstone, Bury type | £1,150 | included |
| 1839 | Dublin & Kingstown (original) | £1,000 | not stated |
| 1839 | Liverpool & Manchester | £1,850-£2,150 | not stated |
| 1839 | Newcastle & Carlisle 4-wheel / 6-wheel | £1,000 / £1,700 | included |
| 1839 | Ulster Railway | £1,500 + £260 tender | separate |
| 1839 | Paisley & Renfrew | £1,100 | carried on engine |
| 1839 | Eastern Counties | £1,300 | excluded |
| 1839 | Clarence, *Victoria* | £750 | not stated |

The price per ton of engine weight works out at £72.50 and £66.67 for the two Bodmin & Wadebridge
engines (Neath Abbey Iron Co. build, 10 t and 12 t) and £143.75 for the Ardrossan 8-tonner, against
the £32-£78 steam-era range already in `vehicle-cost-evidence.md`. That is a usable cross-check:
early engines were more expensive per ton than mature ones.

**1900-1950: the gap is partly closed.** Reeves's LMS 1933-35 operating-cost study gives absolute
repair cost per engine mile by class, which the knowledge base explicitly lacked:

- 3.18d per engine mile, annual mileage 23,270 (general freight tender engine);
- 4.11d per engine mile, annual mileage 22,818 (7F 0-8-0);
- 2.91d per engine mile, annual mileage 27,590 (Hughes/Fowler class);
- 2.88d and 3.41d per engine mile at 38,022 and 34,654 miles (Lentz-gear variants).

These sit between Hill's 1892 average of 2.51d per *train*-mile and the 1954 BR boiler-only figures
of 0.80-1.53d per mile, and they are per *engine*-mile, which is the denominator Hill warns is not
interchangeable with train-mile.

### 2.2 Carriages and wagons

Eighteen carriage prices 1839-1840 from Whishaw, £50-£480, with seating and often weight:

- first class 18 seats: £358 (D&K), £400 (Bolton & Leigh; GPA), £420 (York & North Midland,
  3 t 14 cwt), £440 (Hull & Selby), £480 (Manchester & Bolton, 76 cwt);
- second class 30-40 seats: £120 (GPA), £142 (Clarence), £195 (Hull & Selby), £318 6s (D&K);
- horse-drawn 24-seat: £50 (Arbroath & Forfar);
- luggage trucks: £40-£50.

Ten wagon prices 1839-1840, £13-£115, with the wheel treatment stated in most cases. The
cleanest are the L&BR truck at about £65 including wrought-iron wheels (£20-£29 a set when bought
separately), the Ulster wagon at £115 including a £55 set of Losh wheels, and the Bodmin &
Wadebridge pair at £13 (ore, 30 cwt) and £30 (coal, 2 t).

**Maintenance**: Hill's 1892 wagon column, recorded in the knowledge base as unreadable, is legible
in the discussion text. Company values run from about £2 12s to £5 12s per wagon per annum, mean
about £4. This is the first per-wagon-year maintenance figure in the evidence base and it pairs with
the new 1839 carriage figure below.

### 2.3 Maintenance, all classes

Twelve maintenance rows were added. The most important are:

- **Dublin & Kingstown, 1839**: £2,947 17s 8d for 59 carriages in one year = **£49.97 per
  carriage-year**. That is higher than Hill's 1892 range of £18-£45, which is plausible for a
  railway with new, heavily used stock and no renewal account.
- **Northumberland coal wagons, 1840**: **£4 per wagon per annum** to keep in repair.
- **Clarence Railway *Victoria*, 1840**: **£500 of repairs in about fifteen months on an engine
  that cost £750**. An extreme case, but it shows how far early engine repair could exceed
  expectation.
- **Rail way maintenance per mile, 1839-40**: £59 (Edinburgh & Dalkeith, horse/rope), £185 (Dublin
  & Kingstown), £214 (Manchester & Bolton), £130 14s (Liverpool & Manchester, three-year average),
  £48 (North Union).

### 2.4 Trams

The knowledge base recorded "no car purchase ladder". There is now a thirteen-row ladder:

| Date | Item | Price |
|---|---|---|
| 1902 | Wallasey, 20 cars, ER&TCW tender | £11,800 = £590 each (no air brakes); £12,700 = £635 with |
| 1905-06 | Accrington, Brush saloon car | £695 each |
| 1914 | Northampton, Brush car body/truck | £460, plus Dick, Kerr electrical equipment £289 14s 6d |
| 1947 | Blackpool, reconditioning package | bogies £2,748/pair + Vambac £2,300/set = £5,048 |
| 1950 | Blackpool Coronation | body £4,902 + electrical £2,503 + bogies £5,765 = **£13,170 each**, 21 t |
| 1983 | Blackpool Centenary | body £59,000 + electrical £27,000 = £138,000 |

The 1950 row is the best tram data point in the file: complete component split, stated weight, and
a batch total (£329,250 for 25) from which the per-car figure is the source's own division.

### 2.5 Road vehicles

Only two rows, because the existing `individual-price-rows.csv` already holds 174 road-vehicle
rows. Both fill the 1948-1960 complete-vehicle gap:

- 1954 Whitson "Economist" 44-seat bus on Sentinel chassis, **£1,885 complete**, unladen 6 t 18 cwt;
- c.1959 Leyland Atlantean, **about £7,000 complete**, against a front-engined double-decker
  implied at about £5,000 (the source says the Atlantean cost 40% more).

### 2.6 Stations and depots

Whishaw's London & Birmingham account is the only pre-1850 depot cost found anywhere:

- Euston station **£81,532**;
- Camden depot **£114,385**;
- Wolverton depot **£109,454**;
- all intermediate stations London-Wolverton together **£25,386**;
- against a revised estimate of £70,000 for stations and depots, actual spend "upwards of
  £360,000".

Also: Liverpool passenger station £120,000 (1839); London & Croydon terminus £21,000; London &
Greenwich station of 25,000 sq ft at £27,861 10s (£1.11/sq ft); North Midland station £14,000 with a
**goods depot at £7,000**, which is the "goods shed priced apart" the coverage doc records as missing.

### 2.7 Aircraft

Only two rows, both **second-hand** 1935 purchases (DH.84 Dragon £2,200; DH.83 Fox Moth £650).
They are recorded because they are dated and sourced, but they must not be used as new-aircraft
prices. The aircraft gap is not closed.

---

## 3. The ten to twenty most valuable new data points

1. **L&BR Euston £81,532 / Camden £114,385 / Wolverton £109,454 (1839)** — the only pre-1850
   station-and-depot itemisation with works separated.
2. **North Midland goods depot £7,000 against station £14,000 (1840)** — goods shed priced apart.
3. **Dublin & Kingstown carriage repairs, £49.97 per carriage-year (1839)** — earliest measured
   per-vehicle-year carriage maintenance.
4. **Northumberland wagon repair, £4 per wagon-year (1840)** — earliest wagon maintenance figure.
5. **Hill 1892 wagon maintenance, £2 12s-£5 12s, mean £4 per wagon-year** — closes a gap the
   knowledge base records as unreadable.
6. **LMS 1933-35 locomotive repair, 2.88-4.11d per engine-mile with annual mileage** — the missing
   1900-1950 locomotive maintenance anchor.
7. **Whishaw locomotive ladder 1833-1840, £700-£2,150 with weights and tender treatment** — the
   first pre-1850 locomotive price surface.
8. **Whishaw carriage ladder 1839-1840, £120-£480 by class and seating** — pre-1850 carriage
   surface.
9. **L&BR wagon £65 including wheels; wheel sets £20 and £29 (1840)** — the wheel-in-or-out
   question answered explicitly for one works.
10. **Blackpool Coronation £13,170 each (1950), body £4,902 + electrical £2,503 + bogies £5,765,
    21 tons** — complete tram component ladder.
11. **Wallasey 20 cars for £11,800 (1902)** — first Edwardian tram tender price.
12. **Northampton £460 car + £289 14s 6d electrical equipment (1914)** — the car/equipment split
    that pakset tram objects need.
13. **Blackpool Centenary £138,000 (1983)** — modern tram capital anchor.
14. **Whitson 44-seat complete bus £1,885 (1954)** — cheap end of the 1950s bus market.
15. **Atlantean about £7,000 complete (c.1959)** — with the implied £5,000 conventional
    double-decker.
16. **Rail way maintenance per mile, £48-£214 (1839-40)** — five companies, same source.
17. **Clarence *Victoria*: £500 of repairs in 15 months on a £750 engine** — the upper bound of
    early locomotive repair.
18. **Whishaw's L&BR station total: £360,000 actual against a £70,000 estimate** — the scale of
    station cost overrun at the start of the railway age.

---

## 4. Sources tried that produced nothing (do not retry by the same route)

| Source | Result | Why |
|---|---|---|
| HathiTrust full text (`babel.hathitrust.org`) | HTTP 403 | Blocked to this client. The *Railway Returns* and the 1919 "Railway Reorganisation" (1913 cost analysis) are both there and both would be valuable: obtain through a library or a different machine. |
| Board of Trade *Railway Returns* 1907, archive.org OCR | Table headers and figures cannot be aligned | The volume prints "Repairs and Renewals of Rolling Stock" per train mile by company (Abstract No. 21) and national rolling-stock counts, but the OCR interleaves column headers with numbers. A clean PDF or a printed copy is needed. The 1908 Google-digitised volume is the same. |
| ICE Virtual Library / Emerald | HTTP 403 | Hill 1909, "On the serviceable life and average annual cost of locomotives in Great Britain", *Min. Proc. ICE* 175 — the single best 1909 per-engine-year anchor. Paywalled. |
| Historic Hansard search endpoint | No usable API | `api.parliament.uk/historic-hansard/search` returns an interstitial, not results. Use known volume/page URLs instead. |
| Wikisource MediaWiki API, 50 titles per request | HTTP 429 after the first request | Rate-limited. Use `w/index.php?...&action=raw` one page at a time with a delay; that worked for all 760 pages. |
| East London Railway Joint Committee accounts 1936 (PDF) | Rolling-stock statistical page did not OCR | Gives "Maintenance of Rolling Stock £4,943" for 1936 but no vehicle count, so no per-vehicle figure. |
| SteamIndex class pages (`stanierlo.htm`, `black5.htm`, etc.) | HTTP 404 | Only `fowlerlo.htm` and `hughloco.htm` resolve; both were used. |
| *Flight* archive | No direct route found | Only second-hand aircraft prices surfaced. The FlightGlobal PDF archive is reachable only through the Wayback Machine with exact page URLs. |
| Lardner, *Railway Economy* (1850) | Read and rejected | Its per-vehicle-mile costs are an allocation model, not accounts. Recorded here so nobody re-mines it. |

---

## 5. Coverage after this work

| Class | Before | After | What is still missing |
|---|---|---|---|
| Locomotives, capital | Good | Good (pre-1850 now Fair) | Industrial and narrow-gauge pre-1900; electric locomotives 1900-1950 |
| Locomotives, maintenance | Fair | **Fair/Good** | 1900-1933 and 1935-1953; only LMS 1933-35 has absolute pence/mile |
| Carriages, capital | Good | Good (pre-1850 now Fair) | 1850-1890 |
| Carriages, maintenance | Fair | **Fair/Good** | per-mile figures 1900-1950 |
| Wagons, capital | Good | Good | — |
| Wagons, maintenance | **None** | **Poor/Fair** | any 20th-century per-wagon-year figure |
| Trams, capital | **None** | **Fair** | 1918-1947; single-deck vs double-deck split |
| Trams, maintenance | Fair | Fair | after 1931 |
| Road vehicles | Good | Good | 1948-1960 now has two complete-vehicle anchors |
| Aircraft | Poor | **Poor** | new purchase prices with specification — unchanged |
| Stations | Good | Good | 1850-1950 ordinary stations |
| Depots | Fair | **Fair/Good** | post-1850 engine sheds |
| Goods sheds | **None** | **Poor** | one 1840 figure only |

---

## 6. Proposed knowledge-base updates (for the user to review; nothing has been edited)

1. **New doc `New/ai/vehicle-cost/whishaw-1842.md`** — the source family, the method of reading it,
   the full table of 50-odd prices and the caveats. Draft is at
   `ai/temp/whishaw-1842-railway-costs.md`.
2. **`vehicle-cost-evidence.md`** — add a "Before 1850" subsection under each of Locomotives,
   Carriages and Wagons; change the "thirteen dated purchase prices 1831-1960" count; note the new
   per-ton cross-check (£72-£144 per ton for early engines).
3. **`vehicle-cost/published-capital.md`** — add the Whishaw block (about 45 rows) as a new table,
   marked "contemporaneous survey, second-hand report".
4. **`vehicle-cost/published-maintenance.md`** — add: LMS 1933-35 per engine mile (new §1a); Hill's
   wagon per-vehicle-year (fills the stated gap in "Gaps"); D&K 1839 carriage per-vehicle-year;
   Northumberland 1840 wagon repair; Clarence *Victoria* repair case; and the 1839-40 way
   maintenance per mile.
5. **`cost-data-coverage.md`** — upgrade: wagons maintenance None → Poor/Fair; trams capital "no
   car purchase ladder" → Fair with a ladder; locomotives maintenance Fair → Fair/Good; depots and
   goods sheds to note the 1839-40 figures. Update the "thirteen dated purchase prices" sentence.
6. **`infrastructure-cost-evidence.md`** — add the 1839-40 station/depot itemisation and the
   per-mile way maintenance figures.
7. **`vehicle-cost/tram-maintenance.md`** (or a new `tram-capital.md`) — the 1902-1983 capital
   ladder, with the component split.
8. **`calibration-sources.md`** — register Whishaw 1842 as a dataset ("contemporaneous railway
   survey, 1830-1841, nominal sterling") and note that it is the pre-1850 backbone.
9. **`prices-forum-fragments.md`** — no change needed; the new station figures are measured, not
   forum.

---

## 7. What remains unmeasured

- **Per-locomotive-year repair cost, 1900-1950**, as opposed to per engine mile.
- **Per-carriage-mile** and **per-wagon-year** maintenance for any year after 1892.
- **Bus maintenance 1959-1982** (the capital side now has two anchors; the maintenance side is
  untouched here).
- **Tram maintenance after 1931** and any car-only (excluding track) figure.
- **Ship new-build prices with tonnage**, so that a per-gross-ton ladder can be built. The Caledon
  contract prices already in `published-capital.md` have no tonnage attached.
- **Aircraft new purchase prices with specification.** This is still the largest single hole and
  the coverage doc's "do not calibrate from this evidence" stands.
- **Station buildings 1850-1950** and **goods sheds after 1840**.
- **Pre-1830 carriages and wagons** — Whishaw starts in 1830 and the earlier canal-era stock is not
  covered.
- **Private-owner wagons and wagon repair firms** (Wagon Repairs Ltd from 1919), which is the most
  likely route to a 20th-century per-wagon-year figure.
