# Deep research, second pass: the non-rail gaps

**Date**: 2026-11-22
**Scope**: nominal British (and British-operated) prices for ships, aircraft, road vehicles,
stations and non-rail maintenance, for the pak128.Britain-Ex cost-balancing project. Research
record only. No file under `New/` has been changed and no `.dat`, `.tab` or config value has been
touched.

**Outputs**

| File | Contents |
|---|---|
| `ai/temp/research-pricing-rows-2.csv` | 129 rows, same schema as `individual-price-rows.csv` |
| `ai/temp/research-pricing-report-2.md` | this report |
| `ai/temp/shipbuilding-contracts-evidence.md` | draft evidence doc: the Fairplay standard-ship series and the Caledon order book |
| `ai/temp/aircraft-purchase-prices-evidence.md` | draft evidence doc: what Flight and Hansard will and will not give for aircraft prices |
| `ai/temp/build_research_rows_2.py` | generator for the CSV, so every row can be regenerated or audited |

---

## 1. What was searched

Eight searches, one per turn as the rules require, plus direct fetches.

1. New cargo-steamer contract prices per gross ton, 1900-1939 (shipbuilding price series).
2. Caledon Shipbuilding order book, yard number, tonnage and contract cost.
3. Hansard aircraft costs, Britannia / Vanguard / Comet / VC10, 1955-1965.
4. Hansard and operator sources for the cost of a new bus, 1950s-1970s.
5. Commercial Motor operator purchase contracts, 1949-1960.
6. Victorian and Edwardian contract prices for station buildings, goods sheds and signal cabins.
7. Cost of rebuilding a British station in the 1930s; signal box contract prices.
8. Commercial Motor operating-cost tables, bus and lorry maintenance per mile.

**Direct fetches**: NBER/FRED ship price series; FRED table page; *Teknisk Ugeblad* 1931 (for the
Fairplay specification); Hansard pages found by search; six *Flight* issues downloaded from the
Internet Archive as OCR text and searched locally; Friends of Dundee City Archives Caledon PDFs
(23 files, text extracted with pypdf); Commercial Motor article pages.

**New technical routes established in this pass** (worth recording so the next pass does not
rediscover them):

- *Flight* is available in full on the Internet Archive as `sim_flight-international_*`, with a
  public `_djvu.txt` OCR layer. Any issue can be downloaded and searched locally.
- Commercial Motor article pages are directly fetchable **if the URL is known**, but the
  `/search` endpoint sits behind an AWS WAF JavaScript challenge (HTTP 202) and cannot be reached
  by fetch or by script. Exa does index the article pages, so a search returns both the URL and
  the article text; fetch the URL to confirm.
- Archive.org full-text search across a collection is not exposed through a usable public
  endpoint; the practical method is advancedsearch to find item IDs, then download `_djvu.txt`.

---

## 2. Findings by domain and era

### 2.1 Ships and boats — the gap closes

**The single most useful acquisition is a continuous price series on a fixed specification.**
*Fairplay* published a quarterly price for a new, ready **7,500-ton deadweight standard cargo
steamer** from 1898; the series survives as NBER Macrohistory 02140 and is republished by FRED.
33 annual rows (fourth-quarter values) are in the CSV, 1898-1930, with the per-deadweight-ton
figure computed. Board of Trade answers in Hansard extend the same series by statement to 1938
(about £9/ton 1926-35, £14 8s early 1938, £12 13s 4d December 1938) and to 1941 (16 per cent above
April 1939).

Levels: £6.51/dwt in 1898, £5.20 in 1904, £8.00 in 1914, £31.00 at the 1919 peak, £8.00 in 1923,
£6.51 in 1930, £12.67 in December 1938. A complete ship therefore runs from about £39,000 (1904)
to £232,500 (1919) on one specification. This is exactly the kind of ladder the coverage doc said
did not exist.

**Second acquisition: 69 Caledon contract prices, 1899-1950**, from the yard's order book as
transcribed by Friends of Dundee City Archives. These cover types the standard ship does not:
paddle ferries (£9,450 in 1909), a steam tug (£22,256 in 1936), a lighthouse tender (£94,546 in
1939), a light vessel (£36,000 in 1939), a motor tanker (£85,000 in 1914), war-standard cargo
ships (£199,000 in 1942-43), postwar motor cargo liners (£131,000-£557,600 in 1946-50) and a
632-passenger twin-screw motor vessel (£348,800 in 1950).

**Tonnage is the weak point, and it is now clear why.** The Caledon transcription prints gross
tonnage for only three of the 69 priced hulls (Dago 1,654 gt at £35,000 in 1902; Ortolan 1,717 gt
at £43,000 in 1902; Wologda 2,508 gt at £50,000 in 1903). Those three give £21.2, £25.0 and £19.9
per gross ton — well above the £6.4/dwt Fairplay rate for 1902, as the gross/deadweight difference
and better specifications imply. The lesson is that a per-ton ladder must be built on the Fairplay
series, not on yard lists, unless Lloyd's Register tonnage is looked up hull by hull.

### 2.2 Aircraft — six rows, and an honest verdict

Six rows were added: a 1949 DHC-2 Beaver at about £5,500; a 1955 Cessna 310 at $49,950 (£17,900 as
the source's own conversion); the 1956 government purchase of two Comet 2s and a shell for
£560,000 (second-hand, with overhaul); the 1957 BOAC order of 35 VC10s for about £68m including
initial spares, which divides to about £1.94m each; the 1958 Rotodyne quoted at £375,000; and a
1960 Argosy at "around £485,000".

**The gap is not closed.** *Flight* does not print price tables: six issues (1937, 1949, 1955,
1958 Farnborough, 1960) produced five price statements in total, all incidental. Wikipedia has
removed the `unit cost` field from aircraft articles, so the infobox route is dead. Hansard gives
order totals and quantities, from which unit prices can be divided, but also drowns them in
development and cancellation costs that are not prices.

### 2.3 Buses, coaches and lorries, 1948-1982

Eleven capital rows from Commercial Motor, all 1965-1976, in the form the pakset needs — chassis
and body separately, with seating:

- 1965 Brighton, 14 complete 30 ft double-deckers, 69/70 seats, **£6,300 each** estimated.
- 1965 Bournemouth, Atlantean chassis **£3,031**; Walsall, Fleetline chassis **£3,101** and
  Northern Counties bodies **£3,697**; Liverpool, Atlantean chassis **£3,104.50** and MCW bodies
  **£4,445**; Coventry, Fleetline chassis **£3,339.45** and East Lancashire bodies **£3,936**.
- 1969 London Transport, 117 Fleetlines with 89-seat Park House bodies, "over £1m" — at least
  **£8,547** each.
- 1976 London Transport, 660 buses "worth £20m" — about **£30,303** average across two classes,
  a weak figure.

So a complete 1965 double-decker is about £6,800-£7,550 (chassis plus body), against £1,885 for
the 1954 Whitson 44-seater and about £7,000 for the 1959 Atlantean already in the file. That
brackets the 1954-1965 movement reasonably. **Nothing was obtained for 1948-1953 or 1977-1982.**

Five maintenance rows came from the *Commercial Motor Tables of Operating Costs*, which define
the scope precisely (washing, servicing, repairs and preparation for statutory testing; fuel,
tyres, depreciation and standing costs excluded): a 41-seat oil-engined coach at 4.34d a mile in
1969 and 4.77d in 1970; a 7-ton lorry at 4.04d and 4.45d; a 14-ton six-wheel rigid at 5.29d in
1970. These are standard-cost tables, not operator accounts, but they are the only per-mile road
maintenance series for the 1960s-70s that could be reached.

### 2.4 Bridges, tunnels, signals and other infrastructure — almost nothing

**This gap is essentially unfilled and should be treated as a failed pass.** Three station rows
were added (Manchester Central 1875 contract £124,778, secondary source and marked unverified;
Coventry reconstruction 1938 about £100,000 from a contemporaneous newspaper report; Manchester
London Road rebuild 1958-66 £1.75m, encyclopaedia figure). Nothing was obtained for signal boxes,
goods sheds, docks, piers, bridges or tunnels.

Two things were learned that shape the next attempt. First, the itemised Victorian sources that
would answer the question exist but are not digitised: J. W. Grover, *Examples of station buildings
and their cost, as executed on several railways* (1871), which is exactly a station-building cost
book, is recorded in library catalogues with no online copy. Second, the archival finding aids are
online but the documents are not: the LNWR Society's infrastructure list and the National Records
of Scotland catalogues (GD324, RHP122388 for Dundee West goods shed 1883) locate contract drawings
and bills of quantities without giving sums.

### 2.5 Non-rail maintenance

Only the five road-vehicle rows above. No ship repair per voyage, no aircraft engineering per
hour, and no bus or tram maintenance per vehicle-year was obtained in this pass. The existing
files (`ship-maintenance.md`, `aircraft-maintenance.md`) remain the best evidence for those
classes.

---

## 3. Coverage before and after

| Domain | Rows before | Rows added | Rows after | Assessment |
|---|---|---|---|---|
| ship | 93 | 104 | 197 | **Poor → Fair/Good** for capital: a 40-year per-ton series plus 69 dated contract prices by type. Still no tonnage on most individual hulls. |
| boat (inland) | 31 | 0 | 31 | unchanged, Poor |
| aircraft | 41 | 6 | 47 | **Poor, unchanged in substance.** Six prices, three of them firm new-build. |
| road-vehicle | 174 | 16 | 190 | capital 1948-1976 now has ten anchors; maintenance 1969-70 has five. 1948-53 and 1977-82 still empty. |
| bridge | 45 | 0 | 45 | unchanged |
| tunnel | 24 | 0 | 24 | unchanged |
| signal | 20 | 0 | 20 | unchanged |
| signalbox | 8 | 0 | 8 | **unchanged — the weakest infrastructure class** |
| station | 36 | 3 | 39 | marginal: three named projects, one of them verified |
| dock / pier | 4 / 4 | 0 | 4 / 4 | unchanged, Poor |
| canal / way | 26 / 54 | 0 | 26 / 54 | unchanged |

---

## 4. The most valuable new data points

1. **Fairplay 7,500 dwt standard cargo steamer, 33 annual prices 1898-1930** with the per-ton
   figure — the ship capital ladder the evidence base lacked.
2. **Fairplay series extended by Hansard to December 1938** (12s 13s 4d a ton) and by statement to
   1941 (16 per cent above April 1939).
3. **Caledon 1950 twin-screw passenger motor vessel, £348,800 for 632 passengers** — a postwar
   ferry price with a capacity figure attached.
4. **Caledon 1914 twin-screw motor tanker, £85,000** — the only pre-1918 tanker price found.
5. **Caledon 1936 twin-screw steam tug, £22,256** — the only tug price in the file.
6. **Caledon 1909 paddle ferry, £9,450** — the cheap end of the passenger-ship range.
7. **Three gross-tonnage-bearing contract prices (1902-03) at £19.9-£25.0 per gross ton** — the
   bridge between the deadweight series and gross-ton ship objects.
8. **1965 bus chassis and body prices, four operators** — the chassis/body split that the pakset
   bus objects need, with seating and length.
9. **1969 London Transport Fleetline at not less than £8,547** — the 1960s complete-bus anchor.
10. **CM Tables maintenance at 4.04-5.29d a mile, 1969-70**, with the scope defined in the source.
11. **1957 BOAC VC10 order at about £1.94m each including spares** — the first British jet
    airliner contract price in the file.
12. **1958 Rotodyne at £375,000** and **1960 Argosy at about £485,000** — two firm manufacturer
    quotations for British types.
13. **Coventry station reconstruction 1938, about £100,000** — a dated, verified station capital
    figure in the 1850-1950 gap.

---

## 5. Dead ends and blocked sources

| Source | Result | Note for the next pass |
|---|---|---|
| `clydebuiltships.co.uk` | Domain no longer serves the Clydebuilt database; it returns an unrelated commercial site | Do not retry. The Caledon PDFs at fdca.org.uk are the substitute. |
| Commercial Motor `/search` | AWS WAF challenge, HTTP 202, needs JavaScript | Article pages are fetchable by URL; use Exa to find URLs. The in-app browser was unavailable in this session (`browser.disconnected`), so the search page could not be driven. |
| `vlex.co.uk` copy of Maywald, "The construction costs and the value of the British merchant fleet, 1850-1938" | First page only; paywall | This is the one paper that would give a registered-ton construction-cost series back to 1850. Worth a library request. |
| HathiTrust | Still HTTP 403 | As recorded in the first pass. |
| Wikipedia aircraft `unit cost` fields | Removed from articles | Do not retry the infobox route. |
| `hansard-api.parliament.uk` free-text search | Returns whole speeches in very large JSON, ranked by modern relevance | Use Exa to find the page, then fetch it. |
| Board of Trade *Railway Returns* | OCR tables unusable (first pass) | Unchanged; needs a clean PDF or a printed copy. |
| Grover 1871, *Examples of station buildings and their cost* | Not digitised | Library request; this is the single best station-building source identified. |
| LNWR Society and National Records of Scotland catalogues | Finding aids only, no sums | Useful to locate documents (GD324, RHP122388), not to price anything. |
| *The Engineer* on the Internet Archive | Present as `sim_engineer_*` microfilm, but only the index volumes were located | A promising route for 1870-1910 contract sums; not pursued in this pass. |
| Archive.org full-text search API | No usable public endpoint for collection-wide search | Download `_djvu.txt` per item and grep locally. |

---

## 6. Proposed knowledge-base updates (for review; nothing has been edited)

1. **`New/ai/vehicle-cost/published-capital.md`** — add a ship section with the Fairplay series
   (33 rows), the Hansard continuations, and the Caledon table (69 rows), marked "published price
   series" and "yard order book" respectively.
2. **`New/ai/vehicle-cost-evidence.md`** — Ships: change "three purchase points ... do not fit a
   ladder" to record the 1898-1938 per-deadweight-ton ladder and the 69 contract prices. Say
   plainly that the series is deadweight tons and cannot be applied to gross-ton figures.
3. **`New/ai/cost-data-coverage.md`** — Ships: Poor → **Fair/Good (capital)**, with the tonnage
   caveat. Aircraft: leave at Poor, but replace "one forum and eight published purchase figures"
   with the current count and add that Flight carries no price tables. Road vehicles: record the
   1948-1976 capital anchors and the 1969-70 maintenance series, and keep the 1948-53 and 1977-82
   gaps. Stations: note the three added projects. Signal boxes, docks and piers: record that this
   pass found nothing and name the archival routes.
4. **New doc `New/ai/vehicle-cost/ship-capital.md`** — the ship capital evidence proper, split out
   of `published-capital.md` if that file exceeds its size limit. Draft text is in
   `ai/temp/shipbuilding-contracts-evidence.md`.
5. **New doc `New/ai/vehicle-cost/aircraft-capital.md`** — six rows plus the explicit warning that
   the class is still not calibratable. Draft in `ai/temp/aircraft-purchase-prices-evidence.md`.
6. **`New/ai/calibration-sources.md`** — register two datasets: "Fairplay standard-ship series,
   1898-1938, nominal sterling per deadweight ton" and "Caledon order book contract prices,
   1899-1950, nominal sterling per vessel".
7. **`New/ai/vehicle-cost/road-maintenance-1959-2016.md`** — add the five CM Tables rows for
   1969-70 with the table's own scope definition.
8. **`New/ai/vehicle-cost/published-maintenance.md`** — no change; the CM Tables rows belong with
   the road maintenance doc.

---

## 7. What remains unmeasured

- **Ship tonnage for individual hulls.** The per-ton ladder rests on one standard ship. 66 of the
  69 Caledon hulls have no tonnage in the transcription; Lloyd's Register would settle it.
- **Ship prices before 1898.** The Fairplay series starts there; the 1850-1897 range still rests on
  three isolated vessels.
- **Aircraft new-build prices 1930-1975 as a series.** Six rows is not a ladder. The next routes
  are BOAC and BEA annual reports (aircraft capitalised in the year, with fleet counts) and
  Ministry of Aviation contract announcements.
- **Bus and lorry prices 1948-1953 and 1977-1982**, and any bus maintenance per vehicle-year from
  operator accounts rather than standard-cost tables.
- **Signal boxes**: no price at all was added; the class still rests on the 1912 post prices and
  the 1873-84 interlocking figures already in the file.
- **Goods sheds after 1840, docks, piers, and station buildings 1850-1950 as a series.** Three
  station projects is not a series.
- **Non-rail maintenance per vehicle-year** for buses, trams, ships and aircraft, from operator
  accounts with the scope stated.
