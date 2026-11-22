---
status: draft
verified: none
---
# Research pass 9: measured British depot construction costs

**Covers**: capital costs of railway locomotive sheds and engine depots, station goods sheds and
warehouses, bus garages, tram depots, horse stables, aircraft hangars and boatyards, for pricing the
27 depot objects in `New/depots/`. Nominal money throughout, with the year of the price; no
deflation, no conversion, no adjustment to the pakset.

Rows are in `ai/temp/research-pricing-rows-9.csv` (63 rows). Nothing under `New/` was modified. No
git command was run. Every figure was read from the text of the page or record returned by the
retrieval tool; where a page could not be re-fetched (PDF records, paywalled proceedings), the row
cites the record and the excerpt it came from, and the dead-end list says so.

---

## 1. Method and what the evidence can support

The 27 depot objects are all `Dims=1,1,4`: one tile of ground, four storeys of image. They differ by
waytype, by era and by employment capacity (18 to 225 staff). No depot object has a `cost=` field,
so the engine currently derives capital from its own settings.

The historical record prices depots in four different units, and they are not interchangeable:

1. **Per shed or per complex.** Most common, because railway and municipal accounts were kept by
   project. Useless for a tile-sized object unless the shed's size is known.
2. **Per road or per vehicle place.** The natural unit for a depot, and the one this report
   recommends. Derivable wherever the source states the number of roads or vehicles.
3. **Per square metre.** Derivable wherever dimensions are stated. The best unit for a single
   building tile, and the only unit that transfers between shed types.
4. **Per engine or per car stabled.** Available for a few cases; sensitive to whether the figure
   means allocation or simultaneous accommodation.

Two systematic problems run through the whole series.

**Scope varies more than price does.** A "shed" in one account is a roof on walls; in another it
includes a wheel drop, a lathe, a smithy, offices, pits, a coaling plant and a water tank. The
1898 Accrington figure is 7 to 10 times the 1870 Barrow Hill figure per road (£4,855 tender and
£6,607 final against £685), and the difference is equipment and foundations, not inflation of that
size.

**The published figures are project prices, not rates.** Almost no British source gives a rate. The
rates below are this report's divisions of stated totals by stated dimensions, and each is marked as
derived.

---

## 2. Railway locomotive sheds and engine depots

### 2.1 Small and medium sheds, 1853-1898

| Year | Shed | Roads | Cost | Per road | Source |
|---|---|---|---|---|---|
| 1853 | Malton, NER | 2 | £435 | £218 | Hoole 1972 p.192 |
| 1853 | Monument Lane, LNWR | 3 (12 engines) | £2,795 | £932 | LNWR minutes via LNWR Society |
| 1858 | Monument Lane second shed, LNWR | 6 | £4,524 12s | £754 | ibid. |
| 1865 | Malton six-engine shed, estimate, not built | 6 | £6,817 | £1,136 | Hitches 2009 p.38 |
| 1867 | Malton lengthening to 250 ft | — | £800 | — | Addeyman 2020 p.118 |
| 1870 | Barrow Hill roundhouse, MR | 24 | £16,445 4s 9d | £685 | Barrow Hill history |
| 1872 | St John's, Northampton, MR | 2 | £4,825 | £2,412 | University of Northampton |
| 1874 | St Blazey roundhouse and works, CMR | 9 | £16,000 | £1,778 | Barker 2000 |
| 1876 | Pickering extension, one extra engine | +1 | £604 | £604 | Hoole 1972 p.191 |
| 1882 | Scarborough roundhouse, NER | 15 (11 usable) | £8,369 | £558 | Addeyman 2020 p.154 |
| 1898 | Accrington, L&YR, tender | 8 | £38,840 | £4,855 | Kenyon, Accrington Railways p.94 |
| 1898 | Accrington, final account | 8 | £52,859 | £6,607 | ibid. |

The 1872 St John's figure is the outlier at the top of the small-shed range: a two-road shed with
polychrome brickwork and a clerestory roof, built to a company architectural standard. The 1853
Malton figure is the outlier at the bottom: £435 for a two-road shed is a plain structure, and the
same company was still adding to it fourteen years later.

**Derived per-square-metre figures** (from stated dimensions):

- Barrow Hill 1870, 24 roads of 60-80 ft: about £5.7/m² if the roundhouse is taken as roughly
  2,900 m². The diameter is not stated, so this is an approximation and is not in the CSV.
- Scarborough 1882, 190 ft by 120 ft = 2,118 m²: **£3.95/m²**, including earthworks and retaining
  wall.

### 2.2 Large sheds and depots, 1915-1958

| Year | Depot | Scope | Cost | Unit | Source |
|---|---|---|---|---|---|
| 1922 | Rowsley, MR/LMS | 24 locomotives | £22,205 11s 8d | £925 per road | Disused Stations / Rowsley Association |
| 1955 | Monument Road, Birmingham, BR | 6 roads, 4 two-car sets each, DMU | £18,800 | £3,133 per road | Railway Realism |
| 1958 | Thornaby, BR | 22-road roundhouse, running shed, repair shed, coaling plant, water tank, 70 acres | £1,250,000 | £56,818 per roundhouse road | Heritage Railway 2010 |
| 2019 | Scarborough, TPE | 1 road | £7,000,000 | — | Modern Railways 2021 |

Rowsley is the cleanest large-shed figure in the series: a stated contract sum, a stated capacity of
24 locomotives, and a plain brick building. It is also the best evidence that a steam running shed
of the 1920s cost about £900-1,000 per road.

Thornaby is the opposite: a complete depot on a 70-acre site, including every building and item of
plant. Its per-road figure is an upper bound and should not be used as a shed rate.

### 2.3 Diesel depots, 1955-1980

Only two priced examples were found. Monument Road at £18,800 for six roads is a conversion of
carriage sidings with pits, fuelling points and tanks, and is the best figure for a diesel running
shed. Thornaby covers the large end. No priced example of a 1960s purpose-built diesel depot
(Tinsley, Healey Mills, Knottingley, Laira) was found: the secondary sources give dimensions,
allocations and opening dates but not contract sums.

### 2.4 Turntables, coaling stages, water towers and ash plants

**No separate measured prices were found in this pass.** The nearest items are:

- Tilbury 1906, "water tank house, offices, stores and turntable foundations", £1,245, a combined
  item already recorded in `prices-forum-fragments.md`. It cannot be split.
- Rowsley's coaling plant delayed opening by two years, but its cost is not stated.
- A Stockton and Darlington Railway history page (railcentre.co.uk) quotes £388 for a turntable in
  1886 and £870 in 1906, but the page could not be retrieved at the time of writing, so those
  figures are not used.

These are recorded as a dead end. If the pakset has separate turntable or coaling-stage objects,
they cannot be priced from this evidence.

---

## 3. Goods sheds and warehouses

| Year | Building | Size | Cost | Per m² | Source |
|---|---|---|---|---|---|
| 1853 | GNR potato warehouse, Maiden Lane | 150 ft × 40 ft, 3 floors (557 m²) | £2,000 (estimate) | £3.59 | Kay, GIAS Journal 7 |
| 1875 | Llanelli goods shed, GWR | 55 m × 14 m (770 m²), undercroft | £3,737 | £4.85 | Llanelli Goods Shed Trust |
| 1878 | GWR goods depot, Poplar Dock | 218 ft × 130 ft (2,633 m²), 2 upper floors | £24,000 | £9.12 | Survey of London 43-44 |
| 1878 | GNR goods depot, Poplar Dock | 180 ft × 125 ft (2,090 m²), 1 upper floor | £21,750 | £10.41 | ibid. |
| 1879 | LNWR goods warehouse, Poplar Dock | 4 storeys and cellar, no dimensions | £39,092 | — | ibid. |
| 1883 | Tan y Bwlch, Festiniog Railway | small stone shed, one siding | £85 10s 11d | — | Johnson 2017 p.103 |
| 1886 | Warwick, Queensland (cross-check) | 70 m × 11 m (770 m²) | £2,710 | £3.52 | Queensland Heritage Register |

The four British single-storey or two-storey sheds sit at **£3.59 to £4.85/m² in 1853-1875**, and the
two large multi-storey dock warehouses at **£9.12 to £10.41/m² in 1878**. The Australian cross-check
at £3.52/m² in 1886 agrees with the British single-storey band, which is a useful independent check
on the lower figure.

The Llanelli figure is the best single British goods-shed price: a stated total, a stated footprint,
and a building whose surviving fabric confirms the scope (single storey, stone, slate, undercroft,
one through siding). It was published by the trust that restored the building and is a secondary
statement of a contract sum, not the contract itself.

---

## 4. Bus garages and depots

### 4.1 Per square metre

| Year | Garage | Floor area | Cost | Per m² | Source |
|---|---|---|---|---|---|
| 1926 | Leicester, first portion | 1,450 sq yd (1,212 m²) | £15,786 | £13.02 | Commercial Motor 30 Jul 1929 |
| 1929 | Leicester, extension | 1,550 sq yd (1,296 m²) | £10,000 | £7.72 | ibid. |
| 1929 | Leicester, workshops | 630 sq yd (527 m²) | £4,000 | £7.59 | ibid. |
| 1929 | Glasgow, Larkfield | 300 ft × 220 ft (6,132 m²) | £33,400 | £5.45 | Commercial Motor 7 May 1929 |
| 1929 | Nottingham, Carter Gate | 400 ft × 400 ft (14,864 m²) | about £100,000 | £6.73 | Commercial Motor 28 May 1929 |
| 1938 | London Transport, Alperton | 27,000 sq ft (2,508 m²) | £40,000 | £15.95 | Commercial Motor 12 Aug 1938 |
| 1956 | Leeds, Seacroft, all buildings | 5,238 sq yd (4,380 m²) | £167,000 | £38.13 | Commercial Motor 20 Jul 1956 |

The 1929 cluster at £5.45-6.73/m² is consistent across three cities and is the strongest single
result in this report. The 1938 London figure is about 2.5 times it, and the 1956 Leeds figure about
6 times it, which is a plausible nominal-price path rather than a change in real cost.

The Nottingham per-square-metre figure is the least certain in the table: the article also says that
one acre was devoted to the garage and offices, which conflicts with a building 400 ft by 400 ft
(3.7 acres). The per-vehicle figure of about £500 does not depend on that conflict and is preferred.

The 1926 Leicester figure at £13.02/m² is high for its date. It is the first portion of a garage
designed with a large future extension in mind, so the shell may carry works for the later bays.

### 4.2 Per vehicle

| Year | Garage | Vehicles | Cost | Per vehicle | Source |
|---|---|---|---|---|---|
| 1929 | Nottingham | about 200 buses and trams | about £100,000 | about £500 | Commercial Motor 28 May 1929 |
| 1938 | London Transport, Alperton | 83 buses | £40,000 | £482 | Commercial Motor 12 Aug 1938 |
| 1954 | Coventry, Sandy Lane | 150 vehicles | £120,000 | £800 | Commercial Motor 3 Sep 1954 |
| 1956 | Leeds, Seacroft | 50 housed, 48 more in parking sheds | £167,000 | £3,340 per housed bus; £1,704 per place | Commercial Motor 20 Jul 1956 |

The per-vehicle rate **roughly doubles between 1929 and 1954** (£500 to £800), which is close to the
movement of the per-square-metre rate over the same period and therefore mutually consistent.

### 4.3 Extension and programme prices

Lincoln 1938 extension £8,288; Exeter 1938 extension £1,200; London Transport Well Street (Hackney)
extension £30,000; London Transport Gillingham Street £100,000 and Edgware £14,000, both 1938. These
are recorded because they show the range of works called "a garage" in the same year: £1,200 to
£100,000.

Birmingham's Perry Barr garage (1932) is described in Commercial Motor as covering about one acre of
floor and housing 120 vehicles, but the article gives no cost. It is recorded as a dead end.

---

## 5. Tram depots

| Year | Depot | Capacity | Cost | Per car | Source |
|---|---|---|---|---|---|
| 1899 | Wallasey, Seaview Road (estimate) | 20 cars planned | £5,129 | £256 | History of Wallasey |
| 1901 | Manchester, Queens Road: contracts | 262 cars | £53,075 | £203 | Building News 21 Jun 1901 |
| 1901 | Manchester, Queens Road: stated total | 252 cars | £90,000 | £357 | National Transport Trust |
| 1914 | Aberdeen, King Street (estimate) | 22 cars and 6 buses | £26,000 | £929 | Aberdeen Evening Express 1914 |
| 1915 | Manchester, Hyde Road extension | 90 cars plus 3-storey stores | £46,059 | £512 | Manchester Guardian 27 Oct 1915 |
| 1929 | Salford, Weaste (estimate) | 50-60 buses and 50-60 trams | £79,500 | about £723 | Manchester City News 2 Nov 1929 |

The Manchester Queens Road conflict is important and is recorded rather than resolved. Building News
in 1901 states that "the total amount of the contracts has been £53,075", with room for 262 cars. The
National Transport Trust states the depot was "built at a cost of £90,000 to house 252 tramcars".
The difference of £36,925 is consistent with land, site works and electrical plant being excluded
from the building contracts. Both are carried in the CSV; the per-car rate is therefore £203 to
£357 for the same depot.

Per car, the series runs **£203 (1901) to £929 (1914)**, with the 1915 Manchester extension at £512
for a car shed with a three-storey stores block. The spread again reflects scope: the 1901 figure is
a shed with workshops and offices on a four-acre site; the 1914 Aberdeen figure is a conversion of a
barracks site including two new sheds.

Derived per-square-metre for Manchester Queens Road 1901: the shed covered four acres (16,187 m²)
for £53,075, or **£3.28/m²**. This is low against the bus garages, which is consistent with a
single-storey wide-span shed with no heating and few pits.

---

## 6. Horse stables (the coach stable and the early road depot)

| Year | Building | Horses | Cost | Per horse | Source |
|---|---|---|---|---|---|
| 1889 | Fulham Vestry stables, with loft, house and 4 loose boxes | 44 | £5,158 | £117 | Fulham MOH report 1888 p.129 |
| 1895 | Wandsworth District Board of Works stables | 20 | £5,000 (LCC loan) | £250 | Wandsworth report 1895 p.49 |

The Fulham figure is a tender for a defined building; the Wandsworth figure is a loan for a whole
establishment including yard and fittings, which explains why it is more than twice as high. A
per-horse rate of **£117-250 in the 1890s** is the usable band.

---

## 7. Aircraft hangars

| Year | Hangar | Size | Cost | Source |
|---|---|---|---|---|
| 1937 | Grimsby (Waltham), municipal | large gabled, steel frame, asbestos | £2,526 | Ariadne record |
| 1938 | RAF standard type | not stated | £20,000-30,000 | Hansard 20 Jul 1938 |
| 1938 | Croydon, planned large hangar | not stated | £120,000 (plan) | ibid. |
| 1968 | Luton, Britannia Airways | 378 ft × 200 ft (7,023 m²) | £621,000 | New Steel Construction |

The Grimsby figure is the only municipal hangar price found and is very low because it is a storage
shed for a flying club, not a maintenance depot. The RAF figure is the standard for a service
hangar. Luton gives **£88/m²** for a large modern hangar including offices and stores, which is
consistent with the £250-750/m² modern hangar band already in
`infrastructure-cost-evidence.md` section 9 once the much greater clear height of a modern hangar is
allowed for.

None of these is a depot: they are all aircraft storage or maintenance buildings without the
workshops, stores and apron plant that a depot object implies.

---

## 8. Water depots (boatyards)

The only real equivalent found is the patent slip, the inclined railway that hauls a vessel out of
the water for repair.

| Year | Item | Cost | Source |
|---|---|---|---|
| 1832 | Patent slip for vessels up to 100 tons | £450 | Select Committee on Morton's patent, 1832 |
| 1832 | Patent slip for vessels up to 800 tons | £1,900 | ibid. |
| 1841 | Wooden covered slip roof, Pembroke Dockyard | £7,500 | GLIAS Journal 13 |
| 1928 | Small public quay slipways, Fowey | £48-£120 | Fowey Harbour history |
| 1939 | Fowey slipway extension for 1,200 tons | £1,200 (estimate) | Brazen Island history |

The 1832 evidence states directly that a slip cost one tenth of a dry dock, and that 44 patent slips
existed by that year. The covered slip roofs at Pembroke and Chatham (£7,500-15,480) are the only
prices for the covered version, and they are for naval dockyards.

A boatyard depot is therefore priceable, but only at low confidence: the pakset object is a
building, and the evidence prices the slip and its cover separately.

---

## 9. Best-supported rates

| Rate | Value | Year | Confidence | Basis |
|---|---|---|---|---|
| Rail running shed, per road | £558-932 | 1853-1882 | Medium-high | Five company records, consistent once scope is held |
| Rail running shed with repair equipment, per road | £4,855-6,607 | 1898 | High | One company, tender and final account both stated |
| Rail shed, per road, 1920s | £925 | 1922 | High | Single clean contract with stated capacity |
| Rail diesel running shed, per road | £3,133 | 1955 | Medium | One conversion; no 1960s new-build price |
| Large rail depot, complete | £1.25m for 22 roads and full plant | 1958 | Medium | Upper bound only |
| Goods shed, single storey, per m² | £3.59-4.85 | 1853-1875 | Medium | Two British sheds plus an Australian cross-check |
| Goods warehouse, multi-storey, per m² | £9.12-10.41 | 1878 | Medium | Two dock warehouses, same site, same engineers |
| Bus garage, per m² | £5.45-6.73 | 1929 | High | Three cities, same year |
| Bus garage, per vehicle | £482-500 | 1929-1938 | High | Two cities |
| Bus garage, per vehicle | £800 | 1954 | High | One city, stated capacity |
| Tram depot, per car | £203-357 | 1901 | Medium | Same depot, two published totals |
| Tram depot, per car, with stores | £512 | 1915 | High | Stated contract and capacity |
| Horse stables, per horse | £117-250 | 1889-1895 | Medium | Two municipal records |
| Hangar, small municipal | £2,526 | 1937 | Medium | One record |
| Hangar, large modern, per m² | £88 | 1968 | Medium | One contract |
| Patent slip | £450-1,900 | 1832 | Medium | Contemporary select committee evidence |

---

## 10. Proposed rate table for the 27 depot objects

The pakset needs one `cost=` per object. The honest form of that number is a measured rate at a
stated year, with the object's own intro year noted, because the pakset's price index is what carries
a figure across eras. Nothing here has been adjusted to the pakset.

"Anchor" is the measured figure and its year. Where the object's intro year is far from the anchor
year, the gap is stated rather than hidden. Where no measured basis exists, the entry says so.

### Rail depots (`waytype=track`, `narrowgauge_track`)

| Object | Intro | Anchor | Proposed figure | Basis | Confidence |
|---|---|---|---|---|---|
| OldTrainDepotelHorse | 1750 | 1889 | £117 per horse | Fulham stables | Low: 139 years earlier than the anchor |
| OldTrainDepotNarrowHorse | 1836 | 1853 | £435 per 2-road shed | Malton | Low |
| OldTrainDepot | 1813 | 1853 | £932 per road | Monument Lane | Medium |
| OldTrainDepotNarrow | 1863 | 1872 | £2,412 per 2-road shed | St John's | Medium-low |
| OldTrainDepotElectric | 1890 | 1898 | £4,855 per road (tender) | Accrington | Medium |
| OldTrainDepotDiesel | 1903 | 1898 | £4,855 per road | Accrington | Low: dates do not match the evidence |
| ModernTrainDepot | 1958 | 1955 | £3,133 per road | Monument Road | Medium |
| ModernTrainDepotElectric | 1958 | 1955 | £3,133 per road | Monument Road | Medium |
| ModernTrainDepotNarrow | 1954 | 1955 | £3,133 per road | Monument Road | Low: narrow gauge sheds are smaller |

For a one-tile object, "per road" needs a road count. A single depot tile in this pakset stands for a
small shed, so one to three roads is the reasonable reading; the 1853 Malton two-road figure of £435
and the 1872 St John's two-road figure of £4,825 bracket the range so widely that the choice of road
count matters less than the choice of building quality.

### Road depots (`waytype=road`)

| Object | Intro | Anchor | Proposed figure | Basis | Confidence |
|---|---|---|---|---|---|
| CoachStable | 1700 | 1889 | £117 per horse | Fulham stables | Low: 189 years earlier |
| OldRoadDepotSteam | 1857 | 1889 | £117 per horse | Fulham stables | Medium-low |
| OldRoadDepot | 1901 | 1929 | £500 per bus | Nottingham | Low: 28 years later |
| OldRoadDepot2 | 1919 | 1929 | £500 per bus | Nottingham | Medium |
| OldRoadDepotElectric | 1911 | 1929 | £500 per bus | Nottingham | Low-medium |
| ModernRoadDepot | 1953 | 1954 | £800 per bus | Coventry | High |
| ModernRoadDepotElectric | 1955 | 1954 | £800 per bus | Coventry | High |
| ModernRoadDepotMixed | 1967 | 1956 | £1,704 per vehicle place | Seacroft | Medium: includes open parking sheds |

### Tram depots (`waytype=tram_track`)

| Object | Intro | Anchor | Proposed figure | Basis | Confidence |
|---|---|---|---|---|---|
| OldTramDepotHorse | 1860 | 1899 | £256 per car | Wallasey | Low: horse car sheds are cheaper |
| OldTramDepotSteam | 1875 | 1901 | £203 per car | Manchester Queens Road | Low-medium |
| OldTramDepot | 1885 | 1901 | £203-357 per car | Manchester Queens Road | Medium |
| ModernTramDepot | 1957 | 1956 | £38 per m² | Leeds Seacroft bus garage | Low: no post-war tram depot price found |

### Other waytypes

| Object | Intro | Anchor | Proposed figure | Basis | Confidence |
|---|---|---|---|---|---|
| AirHangarOld | 1909 | 1937 | £2,526 per hangar | Grimsby | Medium-low |
| AirHangarModern | 1949 | 1968 | £88 per m² | Luton | Medium |
| OldBoatyard | 1750 | 1832 | £450 per slip (100 tons) | Patent slip | Low |
| OldBoatyardSteam | 1802 | 1841 | £7,500 per covered slip | Pembroke | Low |
| ModernBoatyard | 1920 | 1939 | £1,200 per slip extension | Fowey | Low |
| MaglevDepot | 2004 | none | no measured basis - leave blank | none found | None |

### Maintenance

No measured maintenance series for any depot type was found in this pass. The only British building
maintenance evidence in the knowledge base is the brick figure of 0.8-1.5 per cent of capital a year
(`infrastructure-cost-evidence.md` section 6), which is a station-building figure applied by analogy,
not a depot measurement. `infrastructure-cost-evidence.md` section 11 item 6 records that depot
maintenance in the pakset is too low against 2,797c; this pass found nothing that either supports or
refutes that, and it should be recorded as an open question rather than closed.

One qualitative point is worth carrying: the cheapest depots in the record are plain sheds with no
machinery (Malton £435, Tan y Bwlch £85), and the dearest are sheds with wheel drops, lathes and
smithies (Accrington £52,859). Maintenance ought to follow the same split, because the machinery is
what wears out. No source found quantifies it.

---

## 11. Dead ends

Recorded so that they are not searched again.

- **Institution of Civil Engineers, Webb 1885, "Standard engine shed of the London and North Western
  Railway"**, *Minutes of the Proceedings* 80, pp.258-259. The landing page returns the citation
  only; the text is behind the ICE Virtual Library paywall. No cost read. This is the single most
  promising unread source, because a standard design should carry a standard price.
- **Hunter 1887, "Locomotive engine- and carriage-sheds as used on the Caledonian Railway"**,
  *Minutes of the Proceedings* 89. Abstract only, no figures.
- **Attock 1924, "Locomotive shed layout"**, Institution of Locomotive Engineers, paper 156. The PDF
  was retrieved, but no PDF text extractor is installed on this machine, so the text could not be
  read. It contains the useful planning rule that an interior-turntable shed needs 100 per cent more
  roofed area than a parallel-road shed for the same engines, and that of 60 engines dealt with daily,
  35 are inside at once. No price was read from it, and the downloaded copy was deleted.
- **Tinsley, Healey Mills, Knottingley, Laira, Crewe diesel depots.** Dimensions, allocations and
  opening dates are published; no contract sums found.
- **Turntables, coaling stages, water towers, ash plants.** No separate prices found. The Tilbury
  1906 combined item is the only figure in the knowledge base and cannot be split.
- **Birmingham Perry Barr bus garage 1932.** Floor area and capacity stated, no cost.
- **Fulwell tram depot 1902.** Built by company staff; no contract sum published.
- **Llanelli goods shed contract.** The trust publishes £3,737; the original 1873 tender notice in
  *The Cambrian* was not accessed.
- **York 1930 municipal garage.** Commercial Motor gives "£19,000 for buildings and £110,000
  complete", which is internally inconsistent and almost certainly a scanning error. Not used.
- **Maglev depot.** No measured construction cost for a maglev depot of any nationality was found.
- **Depot maintenance.** No British series found.

---

## 12. Sources

Railway company records and monographs: LNWR Stour Valley sub-committee minutes via the LNWR Society
Journal; Midland Railway contract at Barrow Hill; Hoole, *North Eastern Locomotive Sheds* (1972);
Addeyman, *North Eastern Railway Engine Sheds* (2020); Hitches, *Steam around Scarborough* (2009);
Barker, "St Blazey", *Railway Bylines* 5(5) 2000; Kenyon, *Accrington Railways*; the Rowsley
Association history via Disused Stations; the University of Northampton conservation history of the
Midland shed; *Modern Railways* 78(875) 2021.

Trade and municipal press: *Commercial Motor* archive (1929, 1938, 1954, 1956); *Building News*
21 June 1901; *Manchester Guardian* 27 October 1915; *Manchester City News* 2 November 1929;
*Aberdeen Evening Express* 5 February 1914; the History of Wallasey tramway history.

Public records and reference works: *Survey of London* vols 43-44 (Poplar Dock); the Medical Officer
of Health reports for Fulham (1888) and Wandsworth (1895) in the Wellcome Collection; Hansard,
20 July 1938; the 1832 Select Committee on Morton's patent slip; GLIAS Journal 13 on slip cover
roofs; the Fowey Harbour history; Queensland Heritage Register; the National Transport Trust.

Every figure above was read from the text of the page or record returned by the retrieval tool,
never from recollection. The two derived rates that rest on dimensions rather than on a stated rate
(Scarborough £3.95/m², Manchester Queens Road £3.28/m²) are marked as derived, and the
approximations that could not be tied to a stated dimension (Barrow Hill) are kept out of the CSV.
