# Research pass 3 — railway electrification, track renewal and formation costs

Date: 2026-11-22. Subagent pass for the cost-balancing project. Outputs: this report,
`research-pricing-rows-3.csv` (103 rows), `br-electrification-costs-1955-1991.md`,
`network-rail-track-renewal-unit-costs.md`.

Nothing under `New/` was modified. No git commands were run.

## Method

One search per turn; each search result was treated as a lead and the page was fetched
before any number was recorded. Five source documents were downloaded and read as PDFs
rather than through search summaries: Cmnd 9691 (1955), BTC *Electrification* (1955),
BRB *Your New Railway* (1966), the ORR CP6 efficiency evidence report, and the Cantrell
1962 Permanent Way Institution paper.

Currency is nominal throughout. No deflation and no exchange conversion is applied in
the CSV. Where a derived per-km figure is given, the arithmetic is stated in the row.

Searches run, in order:

| Subject | What it produced |
|---|---|
| Southern Railway third-rail cost per track mile, 1925-1937 | Four scheme figures via Brown/Wikipedia; IEE Cock 1948 and TNA Railway Gazette supplements as leads |
| BR 1955 Modernisation Plan electrification | Cmnd 9691 PDF; Hansard; BR *Facts and Figures* 1956 |
| Network Rail / ORR electrification unit cost | ORR Arup benchmarking; RIA Cost Challenge; HoC Transport Committee 2021; Modern Railways |
| London Midland main line electrification cost | IMechE Emerson 1966 (abstract); Hansard 1968; BRB *Your New Railway* PDF; IEE Broughall 1962 |
| Network Rail track renewal unit cost | ORR CP6 benchmarking and Schedule 4 papers; RSSB SPARK; Railway Gazette 2000 |
| Renewals of permanent way, 1900-1939 | ICE Madras discussion 1859; GSWR 1913 accounts; ICE renewal papers 1946 and 1951; LMS 1935 via SteamIndex |
| Railway earthworks, 1900-1939 | Brees 1839; Whishaw 1840; Webb 1922; NSW 1900 |
| 25 kV feeder and substation cost | DeltaRail 2010; Crossrail 2014; Network Rail Scotland 2022; ORR traction power TAR |
| Southern Region electrification maintenance | IEE Warder 1950; Cantrell 1962; IEE Sykes 1962; BTC 1955 |
| East Coast Main Line electrification | Rail Engineer 2017 (project director); Hansard 1984 and 1996; BRB completion certificate |

## 1. Coverage before and after

| Domain | Before this pass | After this pass |
|---|---|---|
| Electrification capital | 11 rows; one third-rail scheme (1925), one 1928 short section, two 1955 programme totals, one 1986 scheme, two modern ranges | 45 rows; four third-rail schemes 1913-1939 with track mileage, the 1955 programme split by scheme, the 1966 WCML scheme, the 1984-91 East Coast scheme with a component split, eight modern unit-cost and project figures, feeder-station and grid-connection costs, tram OLE |
| Electrification maintenance | One tramway figure (58/km-year, 1930-31) | Unchanged. No electrification maintenance series was found |
| Track renewal | NER 1878 relaying and new way; installed permanent way 1830-98; maintenance series 1820-2015 | 55 way rows: 1859 renewal with rail/substructure split, 1935 LMS programme, 1961 S&C layout, 2000 relay, 2002/03 volumes, and a complete CP5/CP6 component unit-cost table |
| Formation | 1803, 1830, 1855 typical, 2005 DLR viaduct; road formation bases | 1839 excavation rates by lead, 1840 heavy-earthworks cost per mile, 2011 HS2 cutting/embankment/retaining-wall rates, 2017 road earthworks breakdown, 2009 price-book excavation rates |
| Bridges | 45 rows | 3 new rows: HS2 bridge and viaduct rates per square metre, ECML bridge clearance per bridge |
| Tunnels, signals | 24 and 20 rows | No new evidence found |

## 2. Electrification

### 2.1 Third rail, 1913-1939

Four Southern Railway (and predecessor) schemes give a consistent nominal series:

| Scheme | Year | Cost | Route miles | Track miles | Per track km | Per route km |
|---|---|---|---|---|---|---|
| LSWR stage 1 (estimate, unbuilt) | 1913 | £1,160,000 | 50 | 150 | £4,833 | £14,500 |
| SR Guildford and Dorking | 1925 | £833,000 | 33 | 67 | £7,713 | £15,717 |
| SR Portsmouth No. 1 | 1937 | £3,000,000 | 95 | 242 | £7,712 | £19,608 |
| SR Reading and Camberley | 1939 | £1,000,000 | — | 88 | £7,042 | — |

The 1925 and 1937 figures are almost identical per track km in nominal terms, twelve years
apart. That is the strongest single observation in this domain: third-rail capital per track
km was stable in money of the day across the interwar period, so any real-terms fall came
from the price level, not from a change in the cost of the work.

These four figures are secondhand: they come from Brown, *Southern Electric*, cited through
Wikipedia. The underlying page references are given in the CSV. They are marked SECONDHAND
and should be replaced with the Brown page or a Railway Gazette supplement before use in a
KB claim tagged `[LITERATURE]`.

The 1930 Windsor extension is recorded but must not be divided by its 15 route miles: the
£600,000 covers three schemes and no allocation is stated.

Scope: the 1925 figure includes seven rotary-converter substations, conductor rail, and
platform lengthening. It excludes rolling stock. It is therefore a fixed-equipment figure,
which is the right comparator for a pakset electrification way object.

### 2.2 The 1955 programme and 25 kV

Cmnd 9691 (primary, read directly rather than through a summary) states:

- Main-line fixed installations: "around £125 million" (p.15, para 44), with 1,100 electric
  main-line locomotives at about £60 million. The paragraph follows the three trunk-route
  schemes, so "all these schemes" most plausibly means those 820 route miles, which gives
  £152,439 per route mile, or £94,722 per route km. If the £125m instead covers every Plan
  scheme (1,460 route miles) the average is £85,616 per route mile, or £53,200 per route km.
  The wording is ambiguous and the CSV records both readings.
- Southern Region extension: "about 250 route miles ... approximately £25 million for the
  fixed equipment" (p.15, para 42). That is £100,000 per route mile, or £62,137 per route km.
- The Plan covers 820 route miles of trunk route, 390 route miles of suburban electrification
  and 250 route miles on the Southern Region (BTC, *Electrification*, 1955, p.21).

The existing knowledge-base row "BR 1955 AC £40m for 390 route miles" is not supported by
Cmnd 9691. The 390 route miles is the suburban programme, and the Plan's fixed-installation
figure is £125m, not £40m. The 390-mile programme's own cost could not be recovered: the
table on p.14 is a scanned multi-column table whose OCR interleaves the columns, and the
apparent £20m cannot be tied to the mileage with confidence. It is recorded as UNVERIFIED.

The most useful new figure is the comparative estimate for the Euston-Manchester-Liverpool
scheme in BTC *Electrification* (1955), p.19-20, para 102:

| Item | 25 kV AC | 1,500 V DC |
|---|---|---|
| Power supply and overhead system, including clearances | £38.6m | £47.9m |
| Motive power, including electric trains but excluding hauled stock | £46.3m | £44.0m |
| Signalling | £24.5m | £24.0m |
| Depots | £2.7m | £2.7m |
| Train heating and lighting | £7.1m | £8.1m |

The scheme covers 495 route miles including diversionary lines. The AC power-supply and
overhead figure is therefore £78,000 per route mile, or £48,454 per route km. If the route
averaged two tracks, that is about £24,200 per track km. The document does not state track
mileage, so this is an inference and is marked as such.

This is the only clean 1950s 25 kV capital figure found. It separates the electrification
work from signalling, depots and rolling stock, which the 1966 scheme total does not.

### 2.3 The 1966 West Coast scheme

BRB, *Your New Railway* (April 1966) gives the finished scheme: 412 route miles, "nearly
1,500 miles of track" provided with electric power, £175 million, 12 feeder stations, 58
track section cabins, 109 relay rooms, clearance at 669 bridges and 27 tunnels, and 89
stations rebuilt or refurbished.

£175m over 1,500 track miles is £72,494 per track km; over 412 route miles it is £263,930
per route km. This is an upper bound for electrification alone because the total includes
track, signalling and station work.

Hansard, 27 May 1968, vol. 765 c.170W, gives a tighter figure: the net capital cost was
"about £90 million including electric rolling stock", excluding track repairs and
improvements that were required in any case. That is the figure to use for an
electrification-only comparison, but the locomotive share is not separated.

### 2.4 Fixed equipment: feeders, substations, OLE

- A 25 kV single- or double-track feeder station costs about £1,000,000, with a further
  about £2,000,000 for the grid connection (DeltaRail for DfT, 2010, section 3.1.7). 25 kV
  substations are spaced up to 50 km apart and rated about 15 MVA.
- Crossrail's 2014 contract for eight 25 kV auto-transformer substations plus one feeder
  station and civil works was £16m, about £1.78m per site (Balfour Beatty, 17 June 2014).
- Scotland's 2022-26 programme is £120m for six new feeder stations and nine upgrades
  (Network Rail, 8 November 2022).
- The Reading Independent Feeder is expected to cost more than £50m and take five years
  (ORR, Traction Power Modelling and Capability TAR, 19 August 2022).
- OLE base rates: £377 per route metre single track, £544 two-track, £1,084 four-track
  (HS2 cost model, Q2 2011 prices, base cost only). Per track km that is £271,000-377,000.
- Tramway 750 V DC OLE is £150,000-200,000 per single track km including design and
  installation; about £600,000 per route km once feeder substations and grid connection are
  added (DeltaRail, 2010).
- East Coast Main Line, 1984-91, at 2017 prices: 28,537 foundations and 27,667 masts £290m
  (about £10,200 each); 19 feeder stations and 31 track sectioning cabins £43m (about
  £860,000 per site); immunisation of 350 route km £66m (£188,571 per route km); 127 bridges
  £70m (about £551,000 each). Source: Heath, *Rail Engineer*, 27 November 2017.

The feeder-station figures matter for the pakset because the engine has no separate power
supply object: the catenary way object has to carry the whole fixed installation. A single
feeder station at £1-3m is equivalent to 3-8 track km of OLE at the 2011 rate, so on short
schemes the fixed supply is a large share of the total. That is an argument for a per-km
electrification cost that is higher on short or isolated routes, which the engine cannot
express.

### 2.5 Modern all-in unit costs

| Source | Year | £ per single track km | Scope |
|---|---|---|---|
| RIA, simpler project | 2019 | 750,000-1,000,000 | OLE, power, distribution, share of design and delivery |
| RIA, complex project | 2019 | 1,000,000-1,500,000 | as above; excludes route clearance |
| Network Rail TDNS | 2020 | 1,000,000-2,500,000 | 2020 prices |
| Great Western | 2017 | 2,000,000-2,500,000 | outturn, abandoned part-way |
| Cumbernauld-Springburn | 2014 | 1,079,000 | 57 stk, £61.5m |
| Stirling-Dunblane-Alloa | 2018 | about 1,000,000 | 100 stk |
| Schonbuchbahn, Germany | 2017 | €314,000 OLE only | no grid connection, no route clearance |
| East Coast Main Line | 1983 | 91,700 | 60% of the £344.4m final cost, 1,400 track miles; infrastructure only |
| East Coast Main Line | 2017 | 297,800 | same scope at the source's 2017 price level |

The RIA report states that route clearance is excluded from its ranges and can add 30-40%
of project cost. That is the single largest reason the Great Western outturn is two to
three times the efficient range.

The East Coast scheme is the missing 1980s point and the only scheme found with a published
component split. Its final cost was £344.4m at 1983 prices, of which 60% was electrification
infrastructure and 40% traction and rolling stock, for 1,400 single-track miles. That is
£91,700 per track km at 1983 prices, or £297,800 at the 2017 price level the project director
uses. The same source puts Great Western at £3.54m per track mile at 2017 prices, £2.2m per
track km: a factor of 7.4 between the two schemes, which is the increase the article is
written to explain. The article attributes it to traffic, possession charging and the end of
free grid connections, and states that those factors are unlikely to explain a 740% rise.

### 2.6 Maintenance, renewal and asset lives

No electrification maintenance series was found. The only measured figure remains the
tramway line-equipment figure of £58/km-year in 1930-31. The 1955 BTC annual-cost table
aggregates "maintenance and depreciation of fixed equipment, signalling and motive power"
into one line, so it cannot be decomposed.

The 1962 Cantrell paper gives two conductor-rail facts that bear on renewal:

- Conductor rail is never renewed with the running rails; it has a much longer life.
- Welding conductor rail into quarter-mile lengths saved £900 per mile on the Southern
  Region's post-war extensions.

The knowledge-base asset lives (contact wire 35-40 years, registration 50-60, steelwork 80,
foundations 120, conductor rail 60-80) are consistent with the Cantrell statement but were
not independently re-verified this pass.

## 3. Track renewal

### 3.1 The modern component table

The ORR report *Evidence on top-down and bottom-up efficiency adjustments for Network Rail's
CP6 maintenance and renewals* contains, at Table 4.3, unit costs per linear metre of track
renewal by work type, averaged over CP5 and CP6. This is the first measured component series
for the modern era and the most valuable single find of the pass.

| Work type | CP5 (2014-19) £/m | CP6 (2019-24) £/m | CP5 as % of full replacement |
|---|---|---|---|
| Plain line, all work types | 499 | 451 | 34% |
| Replace, full | 1,451 | 1,411 | 100% |
| Replace, partial | 501 | 493 | 35% |
| Re-rail only | 319 | 255 | 22% |
| Re-ballast, high output | 611 | 664 | 42% |
| Re-rail and re-sleeper, conventional | 617 | 758 | 43% |
| Re-rail and re-sleeper, high output | 893 | 826 | 62% |
| Refurbishment | 258 | 93 | 18% |
| Fencing, off-track | 46 | 44 | — |

Per track km, the multipliers are 1,000. A full plain-line renewal is therefore £1.41-1.45m
per track km; rail-only renewal £255,000-319,000; re-ballast £611,000-664,000.

The refurbishment fall from £258 to £93 is not an efficiency gain: the CP6 figure includes
rail milling, which changes the measured output. The ORR says so explicitly.

Switch and crossing costs in the same table are quoted per S&C unit, although the table is
headed "per linear metre": CP5 average £262,522, full replacement £895,431, refurbishment
£120,701; CP6 average £270,291, full £848,317, refurbishment £60,125. The unit basis is
inferred from Network Rail's S&C counting convention (full renewal 1 unit, partial 0.5) and
is marked UNVERIFIED in the CSV. If the figures are per unit they are plausible; if they are
per metre they are two orders of magnitude too high.

Two further ORR publications give all-in averages:

- Seven-year average conventional track renewal unit cost: £677,000 per track km, with
  Anglia highest at £892,000 and London North East lowest at £514,000 (ORR, year 2 of CP6,
  July 2021, para 3.14).
- 2023-24: £1,108,000 per track km GB average, Wales and Western £1,500,000, Eastern
  £899,000 (ORR, annual report 2023-24, para 3.18).

ORR reports a real-terms increase of about 7% a year since 2014-15, or 3% after controlling
for track length and electrification. The endpoint comparison, the CP5 average of £578,000
against £1,108,000 in 2023-24, is about 10% a year. That is the only long modern series found
and it is directly usable as a renewal trend.

### 3.2 Historical series

| Date | Figure | Scope | Source |
|---|---|---|---|
| 1859 | £100 per mile-year | UK average renewal, excluding ordinary maintenance | Samuel, ICE discussion |
| 1859 | £37 rails / £63 substructure | component split of the above | Samuel, ICE discussion |
| 1878 | £661 per km | NER relaying (already in KB) | — |
| 1935 | £2,000,000 for 600 miles | LMS renewal programme | Locomotive Magazine, via SteamIndex |
| 1961 | £35,000 | complete renewal of one heavy S&C layout | Cantrell, PWI |
| 2000 | £18.2m for 24 km | Settle and Carlisle relay with drainage | Railway Gazette International |

The 1859 figure is the earliest measured renewal cost found and the only one with a
component split: 37% rails, 63% sleepers, ballast, chairs and substructure. That ratio is
the historical counterpart of the modern table. Rail-only renewal is 18-22% of a full
renewal today, against 37% in 1859. The difference is in the direction expected if rails
became a smaller share as sleeper and ballast renewal became mechanised.

The 1935 LMS figure is the only interwar programme total found. Its mileage basis is
ambiguous: "600 miles of track" at £2m gives £3,333 per track mile (£2,071 per track km),
but the material quantities conflict: 90,000 tons of rails is about 1,000-1,200 track miles
at 95-110 lb/yd, while 1,300,000 sleepers is about right for 600 track miles at 24 per 60 ft.
The quantities therefore do not settle whether 600 means route or track miles. If it means
route miles, the per-track-km figure halves to about £1,036. The CSV records the upper figure
and states the ambiguity.

### 3.3 Switches and crossings

- Borough Market Junction, Southern Region: a complete cast-manganese layout installed in
  October 1944, renewed in March 1954, renewed again in October 1961 at about £35,000. The
  junction carried about 1,200 trains a day, 80 per hour in the peak (Cantrell, 1962).
- CP5/CP6 full S&C replacement: £848,000-£895,000 per unit (ORR).
- 2002/03: 270 S&C units renewed in the year (Network Rail Business Plan 2003).

The 1961 figure is not directly comparable with the modern per-unit figures because a
"layout" at Borough Market is several units. It is useful as an order of magnitude and as
evidence that S&C renewal is dominated by labour and possession time, not material.

### 3.4 Possessions and signalling

The ORR's 2008 Schedule 4 paper estimates the compensation paid to train operators for
possessions: £61m for plain-line track renewals in 2006/07, £8m for S&C renewals, £6m for
electrification renewals. These are not in the per-metre renewal unit costs and are a real
additional cost of renewal on a busy railway. They are recorded here rather than in the CSV
because they are compensation payments, not construction cost.

### 3.5 What the numbers mean

1. **The "50-60% of new permanent way" rule in the KB is too coarse.** Modern data put
   rail-only renewal at 18-22%, re-ballast at 42-46%, and re-rail plus re-sleeper at 43-62%
   of a full renewal. The 50-60% band fits a combined rail and sleeper renewal, not a
   relaying operation in general.
2. **A full renewal is the right anchor for the pakset way object.** At £1.41m per track km
   in 2021, a Simutrans tile at 125 m is £176,000 per tile at modern prices. The present
   track way costs are far below that at 1900 prices, which is the known conversion problem,
   not a new finding.
3. **The CP5/CP6 table gives the pakset a defensible set of relative prices** between rail,
   sleeper, ballast and S&C renewal, which is what a component-based renewal model needs.

## 4. Formation and earthworks

### 4.1 Measured rates

| Date | Rate | Scope | Source |
|---|---|---|---|
| 1839 | 9d per yd³ | Grand Junction cutting, 1 mile lead, all-in | Brees |
| 1839 | 11d per yd³ | 1.5 mile lead | Brees |
| 1839 | 1s 1d per yd³ | 3 mile lead | Brees |
| 1839 | 4.5-5d per yd³ | subcontract, labour only | Brees |
| 1840 | 13d per yd³ | Midland Counties average, leads 1-4 miles | Whishaw |
| 2009 | £2.01-6.73 per m³ | general excavation, 0.25-5 m depth | Spon's |
| 2009 | £20.89-53.96 per m³ | rock excavation | Spon's |
| 2011 | £27.91 per m³ | HS2 cutting, average of four depths | HS2 cost model |
| 2011 | £11.02 per m³ | HS2 embankment, average of four heights | HS2 cost model |
| 2017 | £0.60 per m³ excavation, £2.50 deposition, £30 capping | Melton Mowbray distributor road | Leicestershire CC |

### 4.2 Volumes per mile

Whishaw gives two measured earthwork volumes per mile:

- London & Birmingham: 142,000 cubic yards per mile.
- Midland Counties: 94,112 cubic yards per mile, at an average 13d per yard, longest lead
  4 miles. That is £5,098 per mile, or £3,168 per km.

The Midland Counties figure is a heavy-engineering case, and it agrees closely with the
Liverpool & Manchester heavy-earthworks figure of £3,284/km already in the knowledge base.
That agreement is a useful check: two sources a decade apart, both describing 1830s heavy
works, give the same order of magnitude.

A light line with, say, 25,000 cubic yards per mile at 9d would cost £938 per mile, or £583
per km. That is the range in which the knowledge base's "£250-400/km typical (1855-1900)"
sits only at the very bottom. The implication is that the £250-400/km figure describes
clearing, drainage and bed preparation, not bulk earthworks.

### 4.3 By waytype

- **Rail, heavy terrain**: £3,168-3,284 per km (1840, nominal) for 94,000 yd³/mile.
- **Rail, light terrain**: about £580 per km at 25,000 yd³/mile and 9d (derived, not a
  measured scheme).
- **Road, turnpike**: £174 per km (1819, already in KB).
- **Road, modern**: HS2 rates £138-230 per m² of finished road, which includes earthworks,
  drainage, pavement and lighting; the earthworks share is not separated.
- **Canal**: the Leeds & Liverpool 1776 estimate gives cutting £880/mile and puddling
  £88/mile, with bridges and culverts 45% of the total (already in KB).
- **Tram**: no measured formation figure found. The KB's £600-1,200/km street reservation
  remains an estimate.
- **Air**: no new figure; the KB's £6,000-9,000/km subgrade estimate remains unverified.

### 4.4 What is included

The 1839 and 1840 rates cover excavation and haul only, with the contractor's wagons, rails
and barrows. They exclude land, fencing, drainage culverts, bridges and ballast. Brees gives
fencing separately at 4s to 10s per running yard, but states that the 10s Grand Junction
figure includes ballasting, so it cannot be used as a fencing rate.

The HS2 rates cover "site clearance, earthworks, soiling, seeding and small structures for
the permanent way only"; station, road, tunnel and structure earthworks are in other line
items. They exclude contractor costs, design, testing, commissioning, client costs, risk and
optimism bias.

The Melton Mowbray breakdown is the clearest statement of what a modern formation consists
of: strip topsoil, bulk excavation, deposition and compaction, import of suitable fill,
disposal of unsuitable material, capping, and top-soiling. At the rates given, a cubic metre
placed in the formation costs roughly £33 once excavation, deposition and capping are added.

### 4.5 What the numbers mean for `forge_cost_*`

The synthesis recommendation for `forge_cost_track` is a setting of 76,000-101,000, which is
£301-400 per route km at 1900 prices, against a measured formation range of £250-400/km. The
new evidence does not overturn that arithmetic, but it sharpens the definitional problem:

- If the forge is the difference between renewing on an existing bed and creating a new one,
  then it should carry clearing, drainage, fencing and the bulk earthworks. On a heavy line
  that is £3,168/km in 1840 money; on a light line about £580/km. Both are above £400/km.
- If the forge is only the bed preparation (trimming, drainage, fencing), £250-400/km is
  plausible, but then the bulk earthworks have no home in the model at all: the way object
  is defined as the permanent way alone.

This is an open question for the user, not a recommendation. The pakset cannot represent
both a light and a heavy formation with one setting, and the current setting implicitly
chooses the light case.

The road forge recommendation (250,000-380,000, i.e. £991-1,506 per route km at 1900
prices) is consistent with the turnpike formation figure and inconsistent with the modern
road formation. The HS2 rate of £138-230 per square metre of finished road is £0.97-1.61m
per km for a 7 m carriageway at 2011 prices, which cannot be compared with a 1900 figure
without a deflator. The synthesis already says one value cannot fit both eras.

## 5. Dead ends

1. **Cmnd 9691 p.14 suburban table.** The OCR interleaves the columns; the total cost cannot
   be tied to the 390 route miles. Not resolved.
2. **Great Southern & Western Railway 1913 accounts** (CIE archive PDF, 262 pages). The PDF
   is a scan with no usable text layer on the Abstract A pages. The search snippet shows a
   renewal of running lines and "miles of track renewed 29", but the column alignment cannot
   be trusted. Not recorded.
3. **IEE papers.** Cock 1948 (SR electric traction), Sykes 1962 (SR electrification),
   Constant and Craig 1950 (conductor rail), Warder 1950 (traction substations), Emerson
   1966 (LMR electrification) and Crompton and Wallace 1953 (overhead equipment economics)
   are all paywalled at the IET digital library. Abstracts only; none of the cost tables
   could be read.
4. **RSSB SPARK.** The BR Research reports "BR track costs and statistics" (Dyer, 1979) and
   the ballast/reballasting periodicity reports are abstract-only.
5. **1900-1930 formation rates.** No measured British contract rate for earthworks in this
   period was found. The gap between 1840 and 2009 remains.
6. **Electrification maintenance.** No per-track-km maintenance series was found for either
   third rail or 25 kV. The tramway £58/km-year remains the only measured figure.
7. **Tunnels.** No new tunnel cost evidence was found; the HS2 report refers to British
   Tunnelling Society data without reproducing it.
8. **Signals.** No new signal cost evidence was found.

## 6. Most valuable points

1. **The 1955 electrification row in the knowledge base is wrong.** The 390 route miles is
   the suburban programme; Cmnd 9691 gives £125m for the trunk-route fixed installations
   (with an unresolved ambiguity about whether the suburban and Southern Region schemes are
   included), and the Southern Region extension is 250 route miles for £25m. This should be
   corrected before any further electrification balancing.
2. **The Euston-Manchester-Liverpool estimate gives a clean 1955 25 kV capital figure:**
   £38.6m for 495 route miles of power supply and overhead line including clearances. It is
   the only figure found that separates electrification from signalling, depots and stock.
3. **The ORR CP5/CP6 component table is the first measured rail/sleeper/ballast/S&C split.**
   It replaces the single "relaying is 50-60% of new" rule with a set of relativities.
4. **The 1859 renewal figure with its 37/63 split** is the earliest measured renewal cost and
   the historical bookend to the modern table.
5. **Feeder stations and grid connections are £1-3m each**, which the pakset cannot
   represent and which makes short electrification schemes disproportionately expensive.
6. **The 1840 Midland Counties earthworks figure** independently confirms the Liverpool &
   Manchester heavy-earthworks anchor at about £3,200/km, and shows that the "typical"
   formation figure in the KB is a bed-preparation figure, not a bulk-earthworks figure.

## 7. Proposed knowledge-base updates

For review; nothing has been changed.

1. `infrastructure-cost-evidence.md` §8:
   - replace the 1955 row with the Cmnd 9691 figures (£125m trunk-route fixed installations,
     scope ambiguous; 250 route miles for £25m on the Southern Region) and the
     Euston-Manchester-Liverpool £38.6m/495 route miles;
   - add the 1937 and 1939 Southern Railway schemes to the third-rail series;
   - add the 1966 WCML totals and the 1968 net capital figure;
   - add the feeder-station and grid-connection costs;
   - add the modern unit-cost range with the RIA/ORR distinction between efficient and
     troubled schemes.
2. `infrastructure-cost-evidence.md` §2:
   - add the 1859 renewal figure and the 37/63 split;
   - add the 1935 LMS renewal programme with the mileage caveat;
   - add the CP5/CP6 component unit costs and the 2023-24 all-in average.
3. `infrastructure-cost-evidence.md` §2 formation paragraph:
   - replace "£250-400/km typical (1855-1900)" with a statement of what it covers, or mark
     it as bed preparation only;
   - add the 1839 rates by lead and the 1840 heavy-earthworks figure per mile;
   - add the HS2 cutting and embankment rates as the modern bound.
4. `infrastructure-cost-synthesis.md` §3.6 and §5: revisit the electrification per-km
   recommendations and the `forge_cost_track` range in the light of the definitional
   question in §4.5 above.
5. `cost-data-coverage.md`: electrification moves from "one scheme" to "four third-rail
   schemes, two programme totals and a modern range"; way renewal moves from "one 1878
   relaying figure" to "a component series".
6. `infrastructure-cost-evidence.md` §2 currently says "Relaying costs 50-60% of new
   permanent way". That should become "rail-only renewal is 18-22% of a full renewal,
   re-ballast 42-46%, and rail plus sleeper 43-62%, on 2014-24 Network Rail data".

## 8. Open questions

1. Does the forge represent bulk earthworks or only bed preparation? The answer decides
   whether `forge_cost_track` should be near £300/route km or near £3,000/route km at 1900
   prices.
2. Should the pakset carry a fixed electrification supply cost per scheme, given that a
   feeder station is £1-3m and the engine has no object for it?
3. Is the 1935 LMS "600 miles of track" route miles or track miles? The rail tonnage suggests
   route miles and the sleeper count suggests track miles, so the per-track-km figure is
   uncertain by a factor of two.
4. Can the Brown, *Southern Electric* page references be checked against a copy, so that the
   four Southern Railway figures can be tagged `[LITERATURE]` rather than SECONDHAND?
