# Road vehicle and road infrastructure costs: research pass 5

Compiled 2026-11-22. Companion to `research-pricing-rows-5.csv` (193 rows) and
`draft-evidence-bus-station-and-garage-costs.md`, both in `ai/temp/`.

**Scope.** Bus stops, shelters and roadside furniture; bus stations and terminals; bus garages
and depots; road construction and maintenance by era and class; road bridges; level crossings;
car parks; street lighting. Nominal money only. No deflation, no conversion to 1900 prices.

**Method.** Thirteen web searches, one per turn, each with the subject, the constraint and the
date window in the query, followed by page fetches. The Commercial Motor archive was the
single most productive source: its article pages are readable and transcribed, although its
own search page sits behind an AWS WAF JavaScript challenge and cannot be queried directly
(see Dead ends). Article text was fetched and read; where a figure comes only from a search
result's extracted page text rather than a fetched page this is not marked separately, because
the extraction is of the page itself, but OCR damage in the archive transcription is flagged in
the row notes and below.

---

## 1. Bus stops, shelters and roadside furniture

The evidence now forms a usable ladder from 1934 to 2023, with an unusual feature: almost
every point is a *supply-and-erect* price for a named product or a programme average, so the
figures are directly comparable with a bus-stop or shelter object.

| Year | Item | Figure | Source |
|---|---|---|---|
| 1934 | London Transport shelters, 12 standard plus 1 experimental | £1,214 total, £93.38 each | LT Engineering Committee minutes, 19 Mar 1934, via London Bus Museum newsletter 180 |
| 1935 | Warrington cast bus stop flag | 17s 6d each (£0.88) | RTHA Newsletter 14 (1997) |
| 1953 | Unit Concrete precast shelter, 9 ft × 4 ft 6 in | about £60 | Commercial Motor, 11 Sep 1953, p.45 |
| 1958 | North Midlands city shelter, 15 ft, erected | £69 | Commercial Motor, 31 Oct 1958, p.47 |
| 1958 | North Midlands rural shelter, 15 ft, erected | £99 | ibid. |
| 1958 | Glass panels, armoured plate / Georgian wired | £6 13s / £8 10s each | ibid. |
| 1968 | Derbyshire parish shelters | £50-£172 each | Commercial Motor, 12 Jul 1968, p.37 |
| 1968 | Newcastle upon Tyne, 170 shelters | £30,000 = £176.47 each | Commercial Motor, 27 Dec 1968, p.18 |
| 2013 | Hemel Hempstead, shelter supply and install | £9,500 each | Dacorum BC cabinet paper, 30 Apr 2013 |
| 2013 | Hemel Hempstead, flag and pole | £750 each | ibid. |
| 2013 | Hemel Hempstead, electronic passenger information | £1,500 per stop plus £10,000 comms | ibid. |
| 2015 | Cumbria, bus stop improvement | £6,000-8,000 per stop | Cumbria CC, Carlisle study, 2015 |
| 2015 | Havering, Clay Tye Road | £20,000 for 5 stops = £4,000 each | Havering committee, 2 Feb 2016 |

The 1958 product prices are the most useful single find in this group: they decompose into a
per-section rate (£18 or £30) plus a fixed erection charge (£15 or £9), which means the
shelter has a real fixed/variable structure rather than one lump price. Glass is priced per
panel and two panels are needed per 5 ft section, so a 15 ft shelter carries six panels.

**Roadside works.** The Hertfordshire County Council bill for the Hemel Hempstead bus station
rebuild (2013) is the only fully itemised modern highway bill found, and it prices exactly the
items the brief asked for:

- precast bus docking kerb, face raised about 50 mm: £95 per metre;
- carriageway block paving, 60 mm on sand bed with concrete and Type 1 base: £60 per m²;
- anti-slip precast footway at the boarding area: £50 per m²;
- all road markings for new bus stop locations: £2,500 for the whole scheme as one item (about
  £179 a stop if spread over the 14 stops);
- precast gully and grating: £350 each; 150 mm drain connection £70 per metre;
- linear drainage at the raised kerb: £65 per metre;
- 8 m street lighting column, provisional: £2,000 each.

The TfL-funded Havering schemes from 2014-16 give the whole-package cost of bringing a stop
up to accessible standard: £20,000 for five stops, £55,000 for nine locations, and similar.
Those are kerb, footway and 27-37 m clearway only, with no shelter, so they bracket the
"bus cage and kerb" element rather than the furniture.

**What is missing.** No price for a plain pole-and-flag stop before 1935, and none between
1935 and the modern £300-500 range already in the knowledge base. The 1935 Warrington figure
is flag-only because the poles were second-hand gas lamp standards, so it is a lower bound.

---

## 2. Bus stations and terminals

Fifteen rows covering twelve schemes, 1928-1977, spanning municipal, company and combined
interchange schemes.

**The 1928-38 municipal generation is cheap.** Middlesbrough's new station was estimated at
about £4,000 (1929); Grantham's station and car park at nearly £8,000 (1932); Lancaster's at
£13,950 (1937); Leeds cost £15,000 to build on a site costing £29,000 (1938). These were
open-platform stations with shelters, offices and parcels accommodation, not enclosed
buildings, which is why their totals are so low against the post-war interchanges.

**The post-war generation is an order of magnitude dearer.** Preston's 80-gate station with
1,100 car spaces above it cost £1,082,000 (contract 1968, opened 1969); Bradford's 87-stand
interchange with a 200-bus depot and a rail concourse was estimated at £13.8m in 1971 and cost
£16m by 1977. Both are combined schemes, so the only honest per-stand figures are upper
bounds: £13,525 at Preston and £158,632 at Bradford.

**Stand counts and scope are the recurring problem.** Of the twelve schemes recorded, only four
state a stand, gate or platform count (Newcastle 1928, Ribble 1955, Preston 1969, Bradford
1971), and only Ribble's Preston coach station (£10,000 for 11 stands) is a clean single-purpose
scheme. The most valuable rows are therefore the two that give scope in full: Preston (80 gates,
1,100 cars, offices, shops, subways, six acres) and Bradford (87 stands, 200-bus depot, rail
concourse, 8.5 acres, 130 services).

**Revenue cross-check.** Preston let twelve stands to other operators at £370 a year each
including rates (1971), which is the only stand rent found and gives a rough yield on the
capital cost.

---

## 3. Bus garages and depots

Sixteen rows, 1931-1958, all from Commercial Motor's municipal and company news columns. This
is a new source family for the pakset and the strongest single addition in this pass, because
the articles routinely state both the capital cost and the number of vehicles accommodated.

| Year | Depot | Cost | Vehicles | £ per vehicle |
|---|---|---|---|---|
| 1931 | Stockport, Heaton Lane | £125,000 | not stated | - |
| 1938 | LT Alperton | £40,000 | 83 | £482 |
| 1938 | LT Gillingham Street | £100,000 | not stated | - |
| 1938 | LT Edgware | £14,000 | not stated | - |
| 1953 | Potteries Motor Traction, Hanley | under £63,000 | 126 | under £500 |
| 1954 | Coventry, Sandy Lane | £120,000 | 150 | £800 |
| 1958 | Chesterfield, Sheffield Road | £710,274 | 250 | £2,841 |

The Chesterfield figure is the top of the range because it is a complete transport
headquarters: 250-vehicle garage, 133,000 sq ft floor, workshops, dining hall, administration
offices and external works. The Potteries depot is the bottom because the chairman's point was
that it had been built for under £500 a bus including all equipment, in three 228 ft bays of
65 ft span to save steel.

Two other facts are worth recording because they explain the range. First, several of these
depots replaced open-air parking: Coventry's fleet had mostly stood outdoors, and Potteries had
over 100 vehicles in the open. Second, London Transport's 1949 programme shows the scale of
conversion work: seven buildings for about £1.8m, within a £2.8m garage and depot programme and
a £4.6m total scheme that also covered tram-to-bus conversion.

Chelmsford (Eastern National, 1937) is a useful scope case even though no cost survives: 100
vehicles, 67,000 sq ft total, 40,000 sq ft unobstructed garage floor, 550 ft of loading
platforms, offices and a control tower.

---

## 4. Roads: construction

The 1911-1950 hole in the knowledge base is now partly closed, and the 1958-1980 motorway
series is dense.

**1920s-1930s.** The Barnet bypass sections opened in 1928 cost £1,150,000 from north of
Hatfield to Highgate, on a 100 ft formation with a 30 ft carriageway; the North Circular Road
had cost £1,200,000 by 1932, built from 1921 as an unemployment-relief scheme. Neither article
states a length, so no per-mile rate is derived — a deliberate omission rather than a gap in
the source.

The 1938 House of Lords debate is the best single 1930s source. Quoting the County Surveyors'
Association it gives, for the same area near Bristol:

- modernising an existing road to 120 ft dual carriageways with footpaths and cycle tracks:
  **£221,600 a mile**;
- a new road on a new alignment: **£77,600 a mile**;
- a motorway: about **£60,000 a mile**, or below £50,000 in 100-mile contracts.

That ordering — modernisation far dearer than new construction, motorway cheapest — is the
opposite of the intuitive one and is a direct comment on the pakset's upgrade/forge logic.

**1958-1962.** The 1958 Lords debate gives motorway construction at £350,000 a mile with land
at only £3,400 a mile; Lancaster bypass £4m for 11 miles (£364k/mile); London-Yorkshire
motorway £15m for 53 miles (£283k/mile). The 1962 answers give M.1 at £407,000 a mile
including land and M.6 Dunston-Preston at £699,000 including land. The 1961 scheme table is
more useful still because it separates physical construction, land and consulting engineers'
fees for named schemes: Stevenage bypass £251k/mile, Doncaster £369k/mile, Maidstone eastern
£280k/mile, Catterick £281k/mile, Stamford £252k/mile, Grantham £249k/mile, all excluding land.

**1969-1980.** The 1969 table is the only year-by-year contract-let series found: rural dual
two-lane £229k-£1,048k a mile, rural dual three-lane £243k-£1,646k, urban dual three-lane
£905k-£4,300k, all excluding land and elevated sections. The 1978 and 1980 answers give means
at constant prices: rural D3M £2.49m (Aug 1978) rising to £3.33m (June 1980); D2M £1.81m to
£2.63m; dual two-lane all-purpose £1.43m to £2.01m; single two-lane £0.95m. Urban motorways
are stated to be about three times rural.

**What this gives the pakset.** A continuous per-mile series for motorways and trunk roads
1958-1980 with lane counts, plus 1938 points for ordinary roads. The remaining hole is
1900-1928 and 1980-2005 at the "ordinary road" level; the modern motorway end is already
covered by the existing 2005 and 2011 rows.

---

## 5. Roads: maintenance and resurfacing

**Motorways, 1982-1986.** Hansard gives a clean age-related ladder for a three-lane motorway
at 1982 prices: about £6,000 a mile-year under two years old, £10,000 at two to five years,
£15,000 at six to ten, and £40,000-£120,000 over ten years once renewal begins. Two years
later the structural maintenance outturn was £66,059 a mile for all motorways, £82,592 for the
M3, £149,657 for the M1 and £4,511 for the new M25. That spread (a factor of 33 within one
year) is the single most important warning in this domain: a per-mile-year figure is meaningless
without the age and renewal state of the road.

**Modern unit rates, 2023 prices.** The DfT's 2024 evidence review republishes the UKRLG unit
rates, which are directly usable:

- strategic roads: resurfacing £78.53-95.71/m², strengthening £125.15-154.60/m²;
- classified roads: resurfacing £28.22-30.37/m², strengthening £58.90-61.04/m²;
- unclassified roads: resurfacing £15.95-18.10/m², strengthening £28.22-30.37/m²;
- footways and cycleways: surface treatment £10.45/m², resurfacing £30.44/m²,
  reconstruction £51.37/m².

A 7 m carriageway resurfaced at £30/m² is about £210,000 a km, which is a useful cross-check
on the per-mile-year figures.

**National Highways, 2024-25.** The ORR regional dashboards give maintenance and renewal spend
per lane mile: £93,000 (Yorkshire and the North East), £48,000 (North West), £60,000
(Midlands), £67,000 (East), £112,000 (London and the South East), £64,000 (South West), all at
2024-25 prices. Converted, the range is about £29,800-£69,600 per lane-km-year. The network
average is printed only as a chart line and is not recorded as a number.

**Older maintenance.** No per-mile-year figure was found between 1911 and 1982 that was clean
enough to use. The 1906 Institution of Civil Engineers discussion contains 1897-1903 county
maintenance per mile, but the OCR renders pound signs as "2" or "X" throughout ("2 3 2 per
mile", "22,500 per mile"), so the numbers cannot be trusted and are recorded as a dead end.

---

## 6. Road bridges

Three independent modern families, plus one 1958 point:

- **Highways Agency data via EC Harris, Q1 2006**, per m² of deck: overbridge £5,200 (1 span),
  £4,250 (2), £2,700 (3), £2,125 (4+); underbridge £5,050, £3,550, £2,100, £2,050; footbridge
  £4,625; large culvert £2,425; railway overbridge £7,100, £4,250, £3,775, £3,300; pedestrian
  subway £6,150. Inclusive of preliminaries, exclusive of design and VAT.
- **CIPFA replacement unit rates** (via BridgeStation), 2015/16: vehicular single span
  £7,175.47/m², two to three spans £5,146.17, four or more £3,671.96; pedestrian £4,370.63 and
  £2,622.83. The 2024/25 single-span rate is £10,301.82/m².
- **DfT 2024 structure works rates** by condition band: £481-805/m² (very good) rising to
  £3,078-4,362/m² (very poor). These are maintenance and strengthening, not new build, and
  they give the pakset a defensible bridge *maintenance* ladder for the first time.
- **Langstone Bridge, 1958**: structure at about £2 1s a sq ft (about £22/m²), total £312,000
  including approaches, land, lighting and demolition.

The EC Harris and CIPFA families agree on the shape: span count dominates, and a single-span
structure costs roughly two to two and a half times a four-span one per m² of deck.

One caution: the EC Harris figures are a reprint on a document-sharing site of an EC Harris
publication that itself analyses Highways Agency data. They are recorded as SECONDHAND.

---

## 7. Level crossings

Ten rows, 1961-2022, which fill a domain that previously had none.

- 1961: the first automatic half-barrier at Spath cost £5,000-6,000, and saved about £2,000 a
  year in three signalmen's wages.
- 1969: average AHB installation £8,600 before Hixon; a minimum of £13,000 for installations
  with the Hixon modifications.
- 1984: AHB £70,000 to install and £400 a year to operate; manually controlled full barriers
  £120,000 to install and £21,000 a year to operate.
- 2011-15: the AOCL-to-AOCL+B retrofit programme delivered 66 crossings for £13.7m, an average
  of £207,576 each.
- 2022: a miniature stop light overlay for a user-worked crossing costs £120,000-150,000.

The 1984 pair is the most useful: it separates the capital cost of the two common protection
types and shows that the manning cost of a full-barrier crossing is fifty times the operating
cost of an automatic one. That is a direct input to the pakset's crossing objects, which
currently have no cost evidence at all.

---

## 8. Car parks

The 1963 Buchanan report gives £425, £380 and £460 per space for its three schemes (including
land, roads and fees); the 1970 Fire Research Note gives £480 per place for concrete
multi-storey and £342 for steel (1970 prices); Westminster's underground car park was estimated
at £4,450 a space in 1972. Modern ranges are £2,500-4,000 (surface), £14,500-17,000 (above
ground multi-storey) and £20,000-28,000 (underground), with a 2007 London cost model at
£9,000-17,000.

The step from £380-480 in 1963-70 to £9,000-17,000 in 2007 is large but not obviously out of
line with general building inflation over those 37 years; no deflation has been applied here, so
this is a judgement, not a measurement. The value for the pakset is as a city-building or
station-adjacent object, not as a transport way.

---

## 9. Street lighting

Only modern evidence was found: a column and bracket supply-and-install at £598.41 (2016
schedule), £900 per column replacement (2023), £330-335 per LED lantern installed, an average
maintenance cost of £77.40 per light a year and average investment of £70.70 per light a year
(APSE 2018/19). No municipal 1920s-1960s lighting account was found; the Institution of Gas
Engineers' 1931 street illumination committee is mentioned in a Commercial Motor news item but
published no costs there.

---

## 10. Coverage before and after

| Topic | Before this pass | After | Remaining gap |
|---|---|---|---|
| Bus stops and shelters | 1990 range only, plus 5 station-type shelters | 11 points, 1934-2018, supply-and-erect basis | pole-and-flag 1935-1990; bus cage cost separated from clearway |
| Bus stations | none | 12 schemes, 1928-1977, 4 with stand counts | clean single-purpose per-stand rate; 1978-2010 |
| Bus garages and depots | none | 11 schemes, 1931-1958, 4 with vehicle counts | 1960-2026; per m² floor area |
| Road construction < 1950 | turnpike 1806-1880, tarmac 1906-11 | adds 1928, 1933, 1938 (four rates) | 1900-1928; 1945-1958 ordinary roads |
| Road construction 1950-2000 | motorway 2005, 2011 only | about 30 points, 1958-1980, with lane counts | 1980-2005 |
| Road maintenance | 1880, 1900, 2023 resurfacing | 1982-1986 motorway ladder; 2023 unit rates; 2024-25 per lane-mile | 1911-1982; per-lane-km before 2016 |
| Road bridges | forum 2011 yard rates; HS2 2011 | 2006, 2015/16, 2024/25 per m² families; 1958 point | pre-1958 road bridge; bridge by span in 1900 prices |
| Level crossings | none | 1961-2022, six dates | pre-1961; half-barrier vs gates |
| Car parks | none | 1963-2015 | - |
| Street lighting | none | 2016-2023 | pre-2016 |

---

## 11. Dead ends and unverified items

1. **Commercial Motor's own search is unusable directly.** `archive.commercialmotor.com/search`
   returns an AWS WAF JavaScript challenge, not results. Article pages fetch normally. All
   Commercial Motor finds therefore came from Exa searches that happened to surface the
   articles, not from systematic searching of the archive. A browser session could search it
   properly and would probably yield several times as many depot and bus station reports.
2. **OCR damage in the archive.** Pound signs are frequently dropped or misread: Newcastle's
   £15,000 and £12,000 appear as "15,000" and "12,000", and Stockport's £125,000 as "125,000".
   Rows affected are marked UNVERIFIED (OCR).
3. **The 1906 ICE road discussion** is unusable for numbers because the OCR substitutes "2"
   and "X" for "£" throughout. It would be a rich source (county main road maintenance 1897-
   1903, urban and rural comparisons) if a clean copy were obtained.
4. **Langstone Bridge's per-square-foot figure** survives only as "€2 Ibslsq. ft." in the PDF
   text layer. It is read as £2 1s and flagged.
5. **The 1970 Fire Research Note's car park table** is OCR-damaged: site names, dates and
   places are partly garbled. Only the two averages and two named comparisons were used.
6. **Bradford Interchange 1977** is £16m for a combined bus station, rail station, 200-bus
   garage and offices; no component split exists, so no per-stand figure is usable.
7. **Preston 1969** is the same problem in reverse: £1,082,000 covers an 80-gate station and a
   1,100-car multi-storey car park, and the source explicitly says the two have separate city
   treasury accounts but does not give them.
8. **Victoria Coach Station** has no cost in the TfL research guide; the archives listed hold
   refurbishment files from 1989-94 but no figures.
9. **National Highways network-average maintenance per lane mile** is printed as a chart line
   only in the ORR regional summaries, so only the six regional values are recorded.
10. **No turnpike or macadam cost was added.** The existing knowledge base already covers
    1806-1823 and 1880 adequately, and the one new candidate source (the 1906 ICE discussion)
    was unusable.

---

## 12. Most valuable points

1. **The 1958 shelter price list** (£18/section + £15, or £30/section + £9) is the only
   decomposed shelter price found and gives a real fixed/variable structure for a small object.
2. **The 1931-1958 bus depot ladder**, with vehicle counts, converts a class that previously
   had no evidence at all into one with a 6:1 range from Potteries (£500/bus) to Chesterfield
   (£2,841/bus), explained by scope (parking shed against full headquarters).
3. **The 1938 three-way road comparison** (£221,600 modernisation, £77,600 new road, £60,000
   motorway per mile) is a direct statement about the relative cost of upgrading against
   building new, which is exactly the pakset's forge/way distinction.
4. **The 1969 contract-let motorway table** is the only year-by-year per-mile series with lane
   counts found, and its 14 contracts in 1968 alone show a 1.6:1 spread within one year.
5. **The 1984 age ladder for motorway maintenance** (£6,000 to £120,000 a mile-year) explains
   why single maintenance figures for roads are so unstable, and gives the pakset a defensible
   shape for road `maintenance` by era.
6. **The DfT 2024 unit rates** are the cleanest modern set: resurfacing and strengthening per
   m² by road class, footway rates, and bridge works rates by condition band.

---

## 13. Proposed knowledge-base updates

All are proposals for the owner to review; nothing under `New/` has been changed.

1. **`New/ai/infrastructure-cost-evidence.md` §3 (Roads)** — add the 1928, 1933 and 1938
   construction points, the 1958-1980 motorway series, the 1982-1986 motorway maintenance
   ladder and the 2023/2024 unit rates. The present section has one line for motorways and
   nothing between 1911 and 2005.
2. **A new child doc `New/ai/infrastructure/road-bridges.md`** (a new topic folder, following the
   `vehicle-cost/` pattern; or a subsection of §4) — the three per-m²-deck families (2006,
   2015/16, 2024/25) with span-count bands, plus the 1958 Langstone point and the DfT
   condition-band maintenance rates.
3. **`New/ai/cost-data-coverage.md` "Road ways"** — the rating should stay Good, but the entry
   should record that the 1911-1950 gap is now narrowed and that pre-1900 and post-2005 remain
   weak. "Crossings (level)" should move from None to Fair on the strength of the 1961-2022
   ladder. "Depots" should be split: rail depots stay Fair/Poor, road depots become Fair with
   11 named schemes.
4. **`New/ai/infrastructure-cost-evidence.md` §6** — add the bus stop and shelter ladder and
   the Hemel Hempstead roadside-works rates beside the existing 1990 bus-stop range.
5. **`New/ai/prices-forum-fragments.md`** — no change; the new material does not come from the
   forum thread and should not be attributed to it.
6. **A new doc `New/ai/infrastructure/bus-stations-and-garages.md`** — the draft in
   `ai/temp/draft-evidence-bus-station-and-garage-costs.md` is written to be the basis of it.

---

## 14. Sources used

Commercial Motor archive (article pages, 1928-1977); Hansard and Historic Hansard (1922, 1938,
1958, 1961, 1962, 1969, 1972, 1978, 1980, 1984, 1986, 1987); House of Lords debate on
roads and traffic, 23 November 1938; Department for Transport, *Economic appraisal for
investing in local highways maintenance* (2024); Office of Rail and Road, *National Highways
regional performance summaries 2024-25* and *Benchmarking Highways England* (2016); ORR letter
to RAIB on AOCL upgrades (2016); Rail Engineer (2022); Derby Signalling (Spath); EC Harris,
*Indicative building costs* (2006, reprint); CIPFA replacement unit rates via BridgeStation
(2015/16, 2024/25); Skanska/Wisbech Access Study (2017); Cunnane Planning/Colthrop (2023);
Melrose, *Langstone Bridge* (ICE, 1958); D. V. Maskell, Fire Research Note 834 (1970);
*Traffic in Towns* (1963); Building magazine cost model (2007); Southend-on-Sea Borough
Council car parking evidence; Brighton and Hove, Hammersmith and Fulham, North Yorkshire and
Dacorum council reports; APSE street lighting trend analysis (2020); Cumbria
County Council Carlisle study (2015); London Borough of Havering committee reports (2014-16);
London Bus Museum newsletter 180; Roads and Road Transport History Association newsletter 14.
