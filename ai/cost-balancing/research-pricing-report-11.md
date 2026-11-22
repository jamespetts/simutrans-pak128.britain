---
status: draft
verified: none
---
# Research pass 11: British airport buildings and pavements

**Covers**: measured British costs for airport terminal buildings, control towers, hangars,
runways, taxiways, aprons and airfield lighting, from 1928 to 2026, for pricing six terminal
objects and the airfield objects in the pakset.

Rows are in `ai/temp/research-pricing-rows-11.csv` (90 rows). Nothing under `New/` was modified.
No git command was run. Nominal money throughout: every figure is in pounds at the year stated,
with no deflation, escalation or conversion. No figure was fitted to the pakset, and no `.dat`
price was used as evidence.

The central problem is the one the brief names: the pakset records no footprint, so a per-m2 rate
is only useful if a per-object figure can also be given. This pass therefore collects both, and
separates them where a source gives only one.

---

## 1. Evidence grades

| Grade | Meaning | Examples |
|---|---|---|
| A | Contemporaneous official statement, or a peer-reviewed/Historic England account quoting one, with the building named | Birmingham 1939 total; Hansard 1938 hangars; Hansard 1958 airport totals; VOA 2026 cost guide |
| B | Airport, contractor or trade-press statement of a completed project, cost and area from the same source | Heathrow T4; Gatwick North; Stansted; Manchester and Birmingham towers; Luton 1968 hangar |
| C | Cost and area from different sources, or a secondary compilation | Manchester T2; Gatwick 1958; Grangemouth |
| D | Derived by arithmetic from A-C, or read from a publisher's search extract rather than the full text | All `[COMPUTED]` rows; ICE 1933/1950/1960 unit rates |

Grade D rows are usable but must carry their derivation in the note. The report marks every
per-m2 figure that is computed rather than stated.

---

## 2. Terminal buildings

### 2.1 Measured cost and area pairs

Only five British terminals produced both a construction cost and a floor area from the same
project:

| Terminal | Year | Cost | Area | GBP/m2 | Grade |
|---|---|---|---|---|---|
| Heathrow Terminal 4 | 1986 | £200m | 105,481 m2 | **1,896** | B |
| Gatwick North Terminal | 1988 | £200m | 98,000 m2 | **2,041** | B/C |
| Stansted terminal (concourse) | 1991 | £100m | 32,000 m2 | **3,125** | B |
| Stansted, counting the undercroft | 1991 | £100m | about 64,000 m2 | **1,563** | D |
| Manchester Terminal 2 (phase 1) | 1990-93 | £265m | 52,000 m2 | **5,096** | C |
| Manchester T2, two-thirds area | 1990-93 | £265m | about 35,000 m2 | **7,570** | D |
| Heathrow Terminal 5 (programme) | 2008 | £4.3bn | 353,020 m2 | **12,181** | B/D |

The 1986-91 cluster is tight: £1,900-2,050/m2 at Heathrow and Gatwick, £3,125/m2 at Stansted
for the concourse alone. That is a real 1980s-90s range, not a spread of error.

Two results need care:

- **Stansted.** The £100m John Laing contract bought a single-level concourse of about
  32,000 m2 over a full-depth undercroft of the same plan area (Waters, 1989). If the undercroft
  is counted as floor area, the rate is about £1,560/m2. The £1,600/m2 already in the knowledge
  base is consistent with this gross-area figure, not with the concourse figure. Both are
  correct for different definitions; the knowledge base entry should say which is meant.
- **Manchester T2.** The £265m phase 1 built two thirds of the terminal (Construction News,
  1990); the 52,000 m2 is the terminal at opening. The two do not match cleanly, which is why the
  per-m2 is given as a range and graded C.
- **Heathrow T5.** £4.3bn is the whole programme: main terminal, two satellites, track transit,
  tunnels, car parks and rail links. Dividing by the 353,020 m2 terminal area gives an upper
  bound. The true building rate is lower, but no published split was found.

### 2.2 The per-m2 series

| Era | GBP/m2 | Basis | Confidence |
|---|---|---|---|
| 1930s | 25-40 | Derived: Birmingham frame contract and the 1930s building-cost level (section 2.4) | Low |
| 1958-62 | 90-250 | Derived: Manchester T1 £2.7m and Gatwick terminal share of £7.8m, over estimated areas | Low |
| 1986-91 | 1,900-3,125 | Measured: T4, Gatwick North, Stansted | High |
| 1990-93 | 5,100-7,600 | Manchester T2, area/cost mismatch | Low |
| 2008 | 12,200 | T5 whole programme | Medium (scope) |

The series rises faster than general construction inflation. That is expected: the 1980s and
later terminals carry air conditioning, baggage systems, security, retail and IT that the 1930s
building did not. A constant-quality comparison would flatten the curve; the pakset is pricing
the building as built, so the steeper curve is the right one.

### 2.3 Per-object series

This is the series the pakset actually needs, because the objects have fixed footprints.

| Year | Object | Cost | Scope | Confidence |
|---|---|---|---|---|
| 1929 | Manchester Barton | £40,800 | levelling, hangar 150x75x30 ft, workshop, offices, road | Medium |
| 1930s | Worcester | £14,000 | whole municipal scheme | Medium |
| 1930s | **average municipal scheme** | **£93,000** | whole scheme, 1929-39 | **High** |
| 1937 | Liverpool Speke | £435,500 | terminal, tower, two hangars, apron, grass field | High |
| 1938 | Manchester Ringway | £179,295 | borrowing power, not final account | Medium |
| 1939 | Birmingham Elmdon | £360,000 | whole airport including all buildings | High |
| 1939 | Grangemouth | £160,000 | terminal and two large hangars | Low |
| 1946 | Manchester Ringway terminal | £23,500 | terminal building only, Ministry-built | Medium |
| 1955 | Heathrow central area | £21m | T2, Queens Building and road tunnel | High (scope) |
| 1958 | Gatwick | £7.8m | terminal, runway, taxiways, aprons, station, roads | High |
| 1961 | Heathrow T3 | £3m | terminal building | Low |
| 1962 | Manchester T1 | £2.7m | terminal building | High |
| 1986 | Heathrow T4 | £200m | terminal, baggage, links, apron works | High |
| 1988 | Gatwick North | £200m | terminal | High |
| 1991 | Stansted | £100m terminal, £400m airport | terminal contract; whole airport | High |
| 1990-93 | Manchester T2 | £265m | phase 1, two thirds of terminal | Medium |
| 2008 | Heathrow T5 | £4.3bn | whole programme | Medium |

### 2.4 The 1930s municipal package

This is the relevant object for the early terminals, and the evidence is better than expected.
Brodie's Historic England study gives the range and the average directly:

- Worcester £14,000 at the bottom.
- Liverpool £435,500 at the top.
- **Average £93,000** across interwar municipal schemes.
- Birmingham about £360,000, one of the most expensive.

Barton is the cheapest fully itemised package: £30,000 for levelling and cindering 124 acres,
a 150 x 75 x 30 ft hangar, workshop, petrol tank and pump, offices and entrance road, plus
£10,800 supplementary, so about £40,800. It had no purpose-built terminal at first: the
farmhouse was converted.

The terminal alone is much less than the package. At Birmingham the three itemised terminal
contracts are £13,300 for the reinforced concrete frame, £2,690 for panel heating and £1,726 for
metal windows and doors. Those are components, not the whole building, and no total building
cost was found. A terminal of 2,000-3,000 m2 at £25-40/m2 gives £50,000-£120,000, which is
consistent with the £93,000 average package once the hangar and ground works are taken out. That
derivation is grade D and should be presented as an estimate, not a measurement.

### 2.5 What the terminal share looks like

Where a scheme is itemised, buildings are roughly half to two thirds of the total and the
terminal is the largest single building:

- Liverpool: £435,500 for terminal, tower, two hangars of about 8,000 m2 each, apron and field.
  At 1930s hangar rates the two hangars alone are a large share; the terminal cannot have been
  more than about a quarter of the total.
- Birmingham: £360,000 including 730 acres of land, drainage and ground works; the terminal
  frame contract is under 4 per cent of the total, so the building as a whole is perhaps
  10-20 per cent.

This matters for pricing: a 1930s "terminal" object priced at the full package cost would
overstate it by a factor of three to six. The package figure belongs to a combined
terminal-plus-hangar-plus-apron object, if the pakset has one.

---

## 3. Control towers

| Tower | Year | Height | Cost | GBP per metre | Confidence |
|---|---|---|---|---|---|
| Birmingham Elmdon | 1939 | 24 m (79 ft) | included in £360,000 | — | Medium |
| Croydon | 1928 | 15.2 m (50 ft) | included in £267,000 | — | High |
| Luton | n.d. | 48 m | £2.3m | 48,000 | Low (KB only) |
| Edinburgh | 2005 | 57 m | £10m | 175,000 | High |
| Birmingham | 2012 | 34 m | £10m | 294,000 | High |
| Manchester | 2013 | 60 m | £16m | 267,000 | High |
| Heathrow | n.d. | 87 m | £50m | 575,000 | Low (KB only) |
| VOA cab benchmark | 2026 | cab only, 65 m2 | £911,000 | — | High (rate) |

The three verified modern towers give £175,000-£294,000 per metre of height, mean about
£245,000/m. Manchester is the best-documented: £16m project cost, of which £7m was the
Morgan Sindall construction contract for the 60 m shell and cab. The rest is radar, navigation,
communications, fit-out and offices at the base.

The two inherited figures do not fit that line. Luton at £48,000/m is far below it and Heathrow
at £575,000/m far above. Both are plausible for their scope (Luton a simple 1980s tower,
Heathrow an integrated 87 m building with a large equipment base), but neither has a year or a
source URL in the knowledge base. They should be either sourced or dropped.

For a 1930s tower, the only evidence is that it was inside the terminal contract. A 15-24 m
tower with a cab is a small fraction of a £93,000 package. The 2012 replacement of the 24 m
Birmingham tower cost £10m, about a hundred times the average whole 1930s airport.

---

## 4. Hangars

| Hangar | Year | Cost | Area | GBP/m2 | Confidence |
|---|---|---|---|---|---|
| RAF standard new hangar | 1938 | £20,000-30,000 each | not stated | — | High |
| Croydon large hangar (not built) | 1938 | £120,000 | not stated | — | High |
| Liverpool Hangar 1 | 1937 | in £435,500 scheme | 8,016 m2 | — | Area only |
| Barton main hangar | 1929 | in £40,800 scheme | 1,045 m2 | — | Area only |
| Luton, Britannia Airways | 1968 | £621,000 | 7,024 m2 | **88** | High |
| Cardiff, BA maintenance | 1994 | £74m project | 22,000 m2 + 6,000 mezz | 2,643 (upper bound) | Medium |
| Brize Norton, A400M | 2015 | £42m phase | 24,000 m2 | **1,750** | High |
| Humberside training | n.d. | £5m turnkey | 4,270 m2 | 1,171 (upper bound) | Low |
| Farnborough Domus III | 2022 | £55m | 16,258 m2 | **3,383** | High |
| VOA basic hangar | 2026 | — | 500-1,000 m2 | **582** | High (rate) |
| VOA agricultural hangar | 2026 | — | — | 250-350 | High (rate) |

Two distinct markets appear. The VOA rates (£250-582/m2) are replacement-cost benchmarks for
simple uninsulated sheds; recent actual projects run £1,750-3,383/m2 because they include
offices, mezzanines, cranes, specialist doors and services. The Luton 1968 hangar at £88/m2 is
the ancestor of the first group, not the second.

The 1938 Hansard exchange is the best early evidence: a back-bencher complains that the new
large hangars cost "between £20,000 and £30,000 each", and the Air Minister replies about height
and aircraft size without disputing the range. At a typical expansion-period hangar of about
2,000-2,700 m2 that is roughly £10-15/m2, which is consistent with 1930s building costs and with
the £88/m2 at Luton thirty years later.

The Liverpool Hangar 1 at 8,016 m2 is the largest 1930s civil hangar found. Its size explains
why the Liverpool package cost £435,500: two of those plus the terminal and apron is a large
civil engineering bill for 1937.

---

## 5. Pavements, aprons and taxiways

### 5.1 Cost per m2 by era

| Year | Specification | GBP/m2 | Basis | Confidence |
|---|---|---|---|---|
| 1933 | bituminous soil | 0.14 | 2s 4d/sq yd | Low (extract) |
| 1933 | stone base plus 3 in bituminous soil | 0.24 | 4s/sq yd | Low (extract) |
| 1933 | whole-area surfacing, material not named | 0.48 | 8s/sq yd | Low (extract) |
| 1945 | wartime average, all hard surfacing | 1.37 | £200m / 175m sq yd | Medium (derived) |
| 1950 | concrete only, 10 in slab plus sub-base and joints | 0.90 | 15s/sq yd | Low (extract) |
| 1960 | Gatwick runway and apron, including earthworks | 4.60 | 77s/sq yd | Medium (extract) |
| 2026 | concrete, PCN 10 | 69 | VOA Table A | High |
| 2026 | concrete, PCN 93 | 189 | VOA Table A | High |
| 2026 | grass | 1-2 | VOA | High |

The 1960 Gatwick figure is the most useful historical unit rate because its build-up is stated:
earthworks and subgrade 37.7 per cent, concrete slab and lean-mix base 48 per cent, joints
14.3 per cent, with drainage, ducts and associated works excluded. At 2026 prices the same
£4.60/m2 is about £90/m2 after general inflation, which lands inside the VOA's £69-189/m2 band.
That is a strong consistency check across 66 years.

The 1945 wartime average of £1.37/m2 is an all-in figure across 175 million square yards and
444 stations. It should be used only as an order-of-magnitude check, not as a design rate.

### 5.2 Widths

Runway widths, measured:

| Year | Width | Source |
|---|---|---|
| 1929 | 30.5 m (100 ft) | Air Ministry licence condition at Barton |
| 1939 | 45.7 m (50 yd) | RAF maximum runway, 1,000 x 50 yd |
| 1941 | 91.4 m (100 yd) | Prestwick main runway as demanded and built |
| 1945 | 91.4 m (100 yd) | Selected heavy-bomber airfields, 3,000 x 100 yd |
| 1958 | 45.7 m (150 ft) plus 75 ft shoulders each side | Gatwick |
| 2022 | 45 m | ICAO code 3/4 |

Taxiway widths, modern: 23 m for code D/E, 25 m for F, 15 m for C, 10.5 m for B, 7.5 m for A
(ICAO Doc 9157 Part 2, Table 1-1). The wartime 100 yd runway is twice the modern standard; the
1950s Gatwick runway is exactly the modern 45 m with wide shoulders.

For a per-tile figure, the runway pavement area is length x width, and the modern default should
be 45 m. A wartime or 1940s object at 91 m is a different, much larger object.

### 5.3 Aprons

No source separated apron cost from runway or taxiway cost. The VOA rate explicitly covers
"runways, taxiways and aprons" as one class, and every project figure found (Stansted £400m,
Heathrow £11m, Cardiff £74m) bundles the apron with other works. The defensible position is that
an apron costs the same per m2 as the pavement it is made of, at the same PCN, and that the
difference between an apron and a runway is area, not rate.

What is missing is a measured apron area per aircraft stand. ICAO gives clearances (7.5 m for
code D/E/F stands) but not a standard stand area. This is a gap for the pakset's apron objects.

---

## 6. Lighting and navigation aids

Only four priced British systems were found:

| System | Year | Cost | Note |
|---|---|---|---|
| Contact lighting, Heston (not installed) | 1938 | about £10,000 | The amount struck from the estimate |
| FIDO fog dispersal, London Airport, runway only | 1953 | £130,000 | Full approach £227,000 |
| Surveillance radar, Edinburgh Turnhouse | 1968 | £150,000 capital, £30,000/year | About two years to install |
| Apron lighting, Gatwick (postponed) | 1968 | £160,000 saving | Single airport, single system |

These are system-level prices, not per-light or per-metre rates. They are enough to price a
"lighting" or "navaid" object as a lump sum, but not to scale it by runway length. The 1938
contact-lighting figure is the only pre-war one and is crude.

---

## 7. Proposed rate table

The table below is the recommendation for the six terminal objects and the airfield objects. It
gives a per-object figure first, because that is what the pakset can use, and a per-m2 figure
second, for checking and for sizing any new object. All figures are nominal pounds at the stated
year. Conversion to pakset money is out of scope and must follow the pakset's own conversion
chain; no figure here was chosen to match a pakset price.

### 7.1 Terminals

| Object | Per object | Per m2 | Confidence | Note |
|---|---|---|---|---|
| 1930s small municipal terminal | £30,000-£60,000 | £25-40 | Low | Part of a £93,000 average package; terminal alone is much less than the package |
| 1930s major municipal terminal | £100,000-£150,000 | £30-45 | Low | Liverpool and Birmingham class; the £360,000-£435,000 figures are whole airports |
| 1950s terminal | £2m-£4m | £90-150 | Low | Gatwick share; Heathrow T2 area known but cost bundled |
| 1960s terminal | £2.7m-£5m | £90-150 | Medium | Manchester T1 £2.7m is the anchor |
| 1980s terminal | £200m | £1,900-2,050 | High | T4 and Gatwick North agree |
| 1990s terminal | £100m-£265m | £3,100-5,100 | Medium | Stansted and Manchester T2 |
| 2000s terminal | £4.3bn | £12,200 | Medium | T5 programme, upper bound |

For a pakset with six terminal objects, the cleanest set is: 1930s small, 1930s major, 1950s,
1960s, 1980s, 1990s/2000s. The 1980s figure is the strongest single point; the 1930s and 1950s
figures are weaker and should be presented as ranges.

### 7.2 Towers

| Object | Per object | Per metre | Confidence |
|---|---|---|---|
| 1930s tower, 15-24 m, integrated with terminal | £10,000-£30,000 | — | Low |
| 1960s-70s tower, 40-60 m | £2m-£5m | £50,000-£100,000 | Low |
| 2000s-2010s tower, 34-60 m | £10m-£16m | £175,000-£294,000 | High |
| Very large tower, 87 m, with equipment base | £50m | £575,000 | Low |

The modern per-metre range is the useful one: about £245,000/m of height, plus a base building
and systems. A cab alone is about £911,000 at 2026 replacement cost.

### 7.3 Hangars

| Object | Per m2 | Per hangar | Confidence |
|---|---|---|---|
| 1930s steel hangar | £10-15 | £20,000-30,000 | Medium |
| 1960s hangar | £88 | £621,000 for 7,024 m2 | High |
| Modern basic hangar | £582 | — | High (2026 rate) |
| Modern equipped hangar | £1,750-3,383 | £42m-55m for 16,000-24,000 m2 | High |

### 7.4 Pavement

| Object | Per m2 | Confidence |
|---|---|---|
| Grass runway | £1-2 (2026) | High |
| Concrete runway, low strength (PCN 10) | £69 (2026) | High |
| Concrete runway, high strength (PCN 93) | £189 (2026) | High |
| Historical concrete, 1960 | £4.60 | Medium |
| Historical concrete, 1950, pavement only | £0.90 | Low |

Runway width for area: 45 m modern, 45.7 m 1950s, 91.4 m wartime heavy bomber, 30.5 m 1930s
minimum. Taxiway: 23 m modern code D/E.

---

## 8. Dead ends

Recorded so they are not searched again:

1. **Heathrow Terminal 1 cost.** The area (74,601 m2) is official; the 1968 construction cost is
   not in Heathrow's history pages, the CAA appendix, the 1968 Nature note, or Hansard. The
   Nature note gives a £10m pier plan, not the terminal.
2. **All pre-1968 Heathrow terminal costs.** T2's cost is only available as a £21m bundle for
   the central terminal area including the road tunnel. T3's £3m has no 1961 area.
3. **Croydon terminal floor area and cost split.** The £267,000 is quoted for the building by
   one source and for the building plus hotel and hangars by another. No area.
4. **Liverpool Speke terminal cost and floor area.** The listing gives plan form (8-bay and
   10-bay ranges, 2-3 storeys) but no dimensions or cost.
5. **Birmingham Elmdon terminal floor area and total building cost.** Component contracts only.
6. **Prestwick 1930s terminal cost.** Prestwick used the Orangefield Hotel as its terminal; no
   purpose-built 1930s terminal cost exists. The 1941 runway costs are known by dimension, not
   by contract sum.
7. **Renfrew.** Hansard (1953) records that a new passenger building and control tower were being
   built, but gives no sum.
8. **Luton 1938 and 1985 terminals, Liverpool 1986 terminal, Birmingham 1984 terminal.** No cost
   and area pair found in the time available.
9. **Manchester T1 floor area.** The £2.7m is firm; the area is not published in the sources
   found.
10. **Apron cost per m2 as a separate item, and apron area per stand.** No measured separation.
11. **Per-metre lighting costs.** Only system-level prices exist.
12. **Luton and Heathrow tower years and sources.** The knowledge base gives heights and costs
    without a year or citation; they could not be verified in this pass.

Retrieval notes: the Historic England report *Nine Thousand Miles of Concrete* is behind
Cloudflare and could not be downloaded; its figures were read from the Exa extract of the page
and are cited to the report. The ICE 1933, 1950 and 1960 unit rates were read from the
publishers' search extracts, not the full PDFs, and are graded accordingly.

---

## 9. Sources

Primary and official: Hansard 20 July 1938 (hangars, Croydon hangar, Heston lighting, East
Bridgford); Hansard 17 June 1953 (FIDO); Hansard 12 November 1958 (Gatwick and Heathrow totals);
Hansard 7 February 1968 (Turnhouse radar; Gatwick apron lighting); Hansard 17 December 1971
(Heathrow runway and apron spend); Valuation Office Agency, *Rating Manual* section 6 part 3,
airports practice note 2026; ICAO Annex 14 Volume I (2022) and Doc 9157 Part 2 (2020).

Institutional and academic: Brodie, *Birmingham Airport's 1939 Terminal and Interwar Air Travel
in England* (Historic England, 2020); Francis, Flagg and Crisp, *Nine Thousand Miles of
Concrete* (Historic England, 2016); Historic England list entries 1188970, 1217911 and 1359838;
ICE *Proceedings* 1933, 1950 and 1960; Waters, *Stansted Terminal Building and Early Atrium
Studies* (1989); Luke, *Aircraft Maintenance Hangar, Cardiff* (1994).

Airport and contractor: Heathrow media centre (T2 2009, T4 2016); Heathrow *Terminals and
Airfield*; CAA CAP 1133 Appendix C; Gatwick Airport history; RPS, *The Historical Development of
Gatwick Airport* (2024); Manchester Airport history; Construction News (1990, 2012); Construction
Co.uk (2011, 2012); BBC News (2011, 2012); Stansted media centre (2021); Air Navigation Solutions
(2019); New Steel Construction (Luton hangar, 1970); DIO (Brize Norton, 2015); Farnborough
Airport (2022); Houlton (Humberside); Brumhead, *Barton* (Manchester Geographies 5); Capper,
*Prestwick 1935-75* (RAeS, 2019).

Secondary and compilation: Wikipedia terminal areas and dates, used only where corroborated by
an airport or CAA figure; Simple Flying (T3 £3m), graded low; Aviation Trails (Grangemouth),
graded low.
