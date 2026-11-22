---
status: draft
verified: none
---

# Research pass 13: five small British infrastructure cost gaps

**Covers**: headquarters and office buildings; maglev guideway; tram track by rail weight;
tunnels by material and diameter; piers as bridge substructure. Measured nominal costs only,
with the year of the price. No deflation. No Simutrans `.dat` price was used as evidence, and
no figure was fitted to the pakset.

Rows are in `ai/temp/research-pricing-rows-13.csv` (118 rows). Nothing under `New/` was
modified. No git command was run. The knowledge base was read, not edited.

---

## 1. Method and evidence grades

The five gaps differ in how well British practice can answer them. The evidence grades used
below are:

1. **Measured contract or account** — an actual tender, contract sum or company account, with
   the scope stated.
2. **Quantity-based estimate** — measured quantities priced at current contract rates. The
   1905 Copperthwaite tunnel tables are of this kind: they are not one contract, but every
   quantity and unit price is stated.
3. **Planning estimate** — an engineer's or consultant's forward estimate. The 2007 Transrapid
   Munich cost model is of this kind.
4. **Computed** — arithmetic on a measured figure, marked `[COMPUTED]` in the CSV.

The report gives the measured or estimated figure first and the recommendation second. Where
a figure is an estimate rather than an outturn, the text says so.

The web search tool available in this session was the built-in `websearch`, which takes one
query and no separate objective field. One search was made per turn, with the subject,
constraint and date window in the query text. Pages were fetched and read before any figure was
used. Several PDFs were downloaded and their text extracted locally.

---

## 2. Headquarters and office buildings (7 objects)

### 2.1 What was found

The knowledge base records that the headquarters building cost could not be established, with
three near anchors: £62,000 at Derby in 1839 for combined offices and works, £50,000 for a
training college in 1937, and about £72,000 for a United States office block in 1882. None of
the three has a floor area, so none gives a rate. This pass adds measured British building
costs, but almost none of them come with a measured floor area either, and none of them are bus
or airline offices.

| Building | City | Year | Cost | Scope | Floor area |
|---|---|---|---|---|---|
| Euston Great Hall and offices (LNWR) | London | 1846-49 | £150,000 | Great hall, meeting and board rooms, general and booking offices | not recorded |
| Euston Great Hall and offices (second figure) | London | 1849 | £122,562 | same block | not recorded |
| Euston portico and lodges | London | 1840 | £35,000 | architectural frontispiece only | not recorded |
| District Railway general offices | London | 1898 | £20,000 | offices over St James's Park station, including station alterations | not recorded |
| Port of Liverpool Building (Mersey Docks and Harbour Board) | Liverpool | 1903 contract | £277,000 | building contract, William Brown and Son | 285,120 sq ft derived |
| Port of Liverpool Building, total | Liverpool | 1907 | £350,000 | including furniture, fittings and fees | 285,120 sq ft derived |
| County Hall (LCC) Sections A-C | London | 1913 | £968,211 | superstructure only, lowest of 13 tenders | 247,300 sq ft occupied or stored, 1919 |
| County Hall Section D | London | 1930-33 | about £1,000,000 | complete section | not separated |
| 55 Broadway tower (Underground Group, later London Transport) | London | 1927-29 | not found | headquarters block | 31,000 sq ft |
| Cunard Building (Cunard head office) | Liverpool | 1913-17 | not found | headquarters | not found |
| UK Government office programme | national | 1974-75 | £54.35m | 2,007,908 sq ft gross started | 2,007,908 sq ft |
| Welsh Office building | Cardiff | 1975 | £16.9m | one building | 42,831 m² |

The two pre-1945 buildings that give both a cost and an area are therefore the Port of
Liverpool Building and County Hall. Both areas are themselves derived or partial:

- **Port of Liverpool Building.** The footprint is 264 by 216 ft and the building has five
  floors, so the gross area is about 285,120 sq ft (26,489 m²). This is arithmetic on a stated
  footprint and storey count, not a measured gross floor area.
- **County Hall.** In May 1919, 134,400 sq ft were occupied as government offices and 112,900
  sq ft were used as storage, a total of 247,300 sq ft (22,975 m²). This is a partial occupancy
  figure for the unfinished Sections A-C, not a gross area for the whole building.

The resulting rates are:

| Building | Year | Cost per m² | Basis |
|---|---|---|---|
| Port of Liverpool Building, contract | 1903 | £9.44 | £277,000 / 26,489 m² |
| Port of Liverpool Building, total | 1907 | £13.21 | £350,000 / 26,489 m² |
| County Hall, superstructure | 1913 | £42.14 | £968,211 / 22,975 m² |
| UK Government office programme | 1975 | £291.36 | £54.35m / 186,539 m² |
| Welsh Office building | 1975 | £394.57 | £16.9m / 42,831 m² |
| Modern office, 1-2 storey | 2026 | £2,090-2,330 | Costmodelling |
| Modern office, 3-5 storey | 2026 | £2,240-2,480 | Costmodelling |
| Modern office, 6+ storey | 2026 | £2,570-2,850 | Costmodelling |
| Modern office, 6+ storey, air-conditioned | 2026 | £2,980-3,300 | Costmodelling |
| Modern bank head office | 2026 | £3,840-4,260 | Costmodelling |

The gap between the Port of Liverpool Building at £13.21/m² and County Hall at £42.14/m² is
real and not a date effect: both are 1900s buildings, and County Hall is a monumental public
building with a marble council chamber, granite columns and a designed ceremonial front. The
Port of Liverpool Building is a commercial office block with a reinforced-concrete frame and
Portland stone facing. The two figures bracket the range for a large headquarters.

### 2.2 The buildings that could not be costed

- **55 Broadway.** The floor area is published (31,000 sq ft), the construction dates are
  published (1927-29), the architect, contractor, pile count and steel tonnage are published,
  but no total cost was found in the TfL research guide, the TfL archive catalogue, the
  Metadyne history or the listing text. The TfL archive holds an "estimated expenditure for
  material and costs" item of 23 August 1928 and a "Broadway Cost per Head" item, but neither
  is online as a figure. This is a dead end without an archive visit.
- **Cunard Building.** The Cunard archive at Liverpool holds the building accounts, but the
  online catalogue, the centenary article and the building history give no contract sum. The
  construction contract was with Holland, Hannen and Cubitts (articles of agreement, 1913), and
  the firm's records are at National Museums Liverpool, but no figure is published. Dead end.
- **Bus company offices.** No measured cost was found for a British bus company head office.
  The London General Omnibus Company was housed in the Underground Group's 55 Broadway from
  1924, so the bus headquarters cost is inside the 55 Broadway problem, not a separate figure.
  The 1958 Bristol Omnibus bus station cost £200,000, but it is a station and two-acre garage,
  not an office. The National Bus Company's 1969 headquarters was a new office block at
  25 New Street Square, London, with no published cost. Provincial bus offices were small and
  no itemised cost was found. Dead end.
- **Airline offices.** No measured cost was found for a British airline head office. This was
  not searched separately, because the headquarters of BOAC and BEA were leasehold space in
  London rather than purpose-built owned buildings for most of the period. Recorded as a gap,
  not as a nil.
- **Railway headquarters other than Euston.** Paddington, Derby and York were searched in the
  first query. The results returned station histories and the Euston account, not itemised
  office-building contracts. The GWR's Paddington office range was built in phases and its
  accounts were not found in an itemised form. Dead end within the search budget.

### 2.3 Recommendation

**Charge headquarters by floor area, not by a single building price.** The measured range for a
large British headquarters is:

- **£13/m² in 1907 prices** for a plain commercial head office (Port of Liverpool Building,
  total cost including fittings and fees);
- **£42/m² in 1913 prices** for a monumental public headquarters (County Hall, superstructure);
- **£291-395/m² in 1975 prices** for government offices;
- **£2,090-2,850/m² in 2026 prices** for ordinary offices, rising to £2,980-3,300 for
  air-conditioned tall offices;
- **£3,840-4,260/m² in 2026 prices** for a bank head office, the closest modern analogue to a
  prestige company headquarters, about 50 per cent above a plain tall office.

For the seven pakset objects the practical recommendation is a rate of **£15/m² at 1900-1910
prices for the ordinary levels (HQ1 and HQ2) and £40/m² for the monumental top level (HQ4)**,
with HQ3 between them. The pre-1849 objects have no measured British figure; the 1849 Euston
figure is the earliest, and applying a nineteenth-century rate to 1750 is an extrapolation, not
a measurement.

**Confidence: low to medium.** Two buildings give both cost and area, both areas are derived,
and there is no bus, airline or non-Euston railway headquarters figure. The rate is usable, but
it rests on a thin base.

**Do not** apply the 2026 rate backwards without the price conversion chain. The nominal series
above is for the years stated.

---

## 3. Maglev guideway (5 objects)

### 3.1 The guideway-only rate

The best source found is the 2007 Vieregg-Rössler cost model for the planned Munich Transrapid
line. It separates the guideway superstructure (called `Fahrweg-Überbau`) from land, earthworks,
sound barriers, third-party works, the linear motor, power supply and stations. The figures are
in 2007 prices and are a detailed quantity-based estimate against the 2007 plan approval
documents, not an outturn.

| Element | Route length | Cost per route-km | Cost per track-km |
|---|---|---|---|
| At-grade guideway superstructure | 21.74 km | €20.20m | €10.10m |
| Elevated guideway superstructure | 5.76 km | €24.70m | €12.35m |
| Earthworks | 27.50 km | €2.36m | €1.18m |
| Land acquisition | 27.50 km | €1.40m | €0.70m |
| Tunnel guideway superstructure | 10.26 km | €10.00m | €5.00m |
| Total route, including 9.05 km tunnel and two underground stations | 37.5 km | €74.8m | — |

The guideway superstructure is by far the largest single element of the surface route. Elevation
adds 22 per cent to the guideway cost (€24.70m against €20.20m per route-km), because the deck,
bearings and alignment dominate and the piers are a smaller addition than might be expected.

### 3.2 Whole-system figures, for context only

These are not guideway rates and must not be used as such:

- **Shanghai Transrapid, 2004**: €1.35bn for 30 km = **€45m per route-km**, whole system
  including vehicles, stations and propulsion. The FRA report gives $1.2bn and $64m per mile.
- **Incheon Airport maglev, 2006**: €280m total for 6.1 km = **€45.9m per route-km**; the
  construction element is stated separately at **€28.8m per km**. This is a low-speed urban
  maglev, not a Transrapid-class line.
- **Planned US maglev projects, 2004**: total capital $54-60m per route-km for full dual
  guideway, $25m for a single-track at-grade project.
- **FRA 2005**: $50-100m per route-mile for double-track urban maglev, 2004 dollars, including
  vehicles and stations.

The useful structural fact is that the **guideway is 45-48 per cent of total project cost** in
the 2004 comparison of planned Transrapid projects, and about 50 per cent on average. The
guideway unit cost in that comparison is **$21-31m per route-km**, or $13-15m per track-mile.

### 3.3 British cross-check: elevated guided transit

The DLR City Airport viaduct is **£19-24m per route-km in 2005 prices**. If the viaduct carries
two tracks, that is **£9.5-12m per track-km**; if it is single track, the full £19-24m per
track-km. The maglev elevated guideway at €12.35m per track-km in 2007 is about £8.5m per
track-km at the 2007 exchange rate, at or below the DLR range on either reading. This is a
useful independent check: a maglev guideway is not a different order of cost from a conventional
elevated light-rail viaduct; the expensive parts of a maglev system are the linear motor, power
supply and control, not the concrete and steel guideway.

The 1993 Hamburg-Berlin study gives a second cross-check: **DM21.0m per km at grade**, with a
**DM5.5m per km** addition for elevation, at 1993 prices. The elevated premium is 26 per cent,
close to the 22 per cent in the 2007 Munich model.

### 3.4 Recommendation

**Charge the maglev way at €10.1m per track-km at grade and €12.35m per track-km elevated, in
2007 prices.** The pakset way object is one track, so the per-track figure is the correct one.
The existing convention that a second parallel way is halved should not be applied to this
rate: the Munich figure is already divided between the two tracks of one shared guideway
structure, so each track carries half the double-track cost. Halving again would undercharge
the pair by 25 per cent.

Do **not** use the Shanghai or Incheon whole-system figures for the way object. They include
vehicles, stations and propulsion and would overcharge the guideway by a factor of three to
four.

**Confidence: medium-high.** The Munich model is detailed and separates the guideway, and the
DLR cross-check agrees. The limitation is that it is a 2007 planning estimate for a line that
was never built, not an as-built British account. No British maglev exists, so no British
measured guideway rate can exist.

---

## 4. Tram track by rail weight (8 objects)

### 4.1 Rail price per ton

The only official British price series found is the 1907 Board of Trade return of imports and
exports:

| Rail | Year | Price per ton | Basis |
|---|---|---|---|
| German grooved tram rails imported | 1907 | £6 9s 8d = **£6.49** | declared value, 858 tons |
| Belgian grooved tram rails imported | 1907 | £6 8s 9d = **£6.44** | declared value, 1,362 tons |
| British grooved tram rails exported | 1907 | £16 19s 11d = **£16.99** | 4,077 tons |
| Quainton estate 30 lb bridge rails | 1870 | £8 2s 6d = **£8.13** | actual purchase |

The Board of Trade explicitly said it had **no official information on the average cost of
tramway rails manufactured in the United Kingdom**. The British export price is the only
British-made figure in the return, and it is nearly three times the continental import price.
The reason is not stated in the return. It may be quality, order size or a different mix of
sections. The honest position is that the domestic price is bracketed by **£6.44 and £16.99 per
ton in 1907**, with **£10 per ton** a reasonable central value for arithmetic.

### 4.2 Rail cost per mile by weight

A single-track mile uses two rails, each 1,760 yards long. At *w* lb per yard the rail weight is
**1.5714 × w tons per mile**:

| Rail weight | Tons per single-track mile | Rail cost at £6.50/ton | at £10/ton | at £16.99/ton |
|---|---|---|---|---|
| 41 lb/yd | 64.4 | £419 | £644 | £1,095 |
| 55 lb/yd | 86.4 | £562 | £864 | £1,468 |
| 75 lb/yd | 117.9 | £766 | £1,179 | £2,002 |
| 85 lb/yd | 133.6 | £868 | £1,336 | £2,269 |
| 92 lb/yd | 144.6 | £940 | £1,446 | £2,456 |
| 98 lb/yd | 154.0 | £1,001 | £1,540 | £2,616 |

This is the table the pakset needs. It replaces a flat rate with a weight-proportional one, and
the only judgement is the price per ton.

### 4.3 Share of the total track cost that is rail

The 1911 *Encyclopaedia Britannica* article by Emile Garcke gives street tramway permanent way
as **£5,050 per mile of single track, including bonding**. Whether the paving between the rails
is inside that figure is not stated; the 1877 discussion treats paving as part of the tramway
cost, so the share below is best read as a share of a track that includes its paving. Against
that figure:

| Rail weight | Rail share at £6.50/ton | at £10/ton | at £16.99/ton |
|---|---|---|---|
| 41 lb/yd | 8.3% | 12.8% | 21.7% |
| 55 lb/yd | 11.1% | 17.1% | 29.1% |
| 75 lb/yd | 15.2% | 23.3% | 39.7% |
| 85 lb/yd | 17.2% | 26.4% | 44.9% |
| 92 lb/yd | 18.6% | 28.6% | 48.6% |
| 98 lb/yd | 19.8% | 30.5% | 51.8% |

The full range is **8 to 52 per cent**, with a central estimate of **13 to 30 per cent**. That
is a wide range, but it is not arbitrary: it is the consequence of the uncertain rail price and
the known rail weight.

An independent 1877 source agrees with the upper half of the range. The Institution of Civil
Engineers discussion of street tramways gives the metal (rails plus longitudinal bearers and
fastenings) at **£2,000-2,300 per mile** against **£4,500 per mile complete**, or **44-51 per
cent**. The rails alone are a fraction of that metal figure; the bearers and fastenings are the
rest. At 40 lb per yard, the rails alone at £10-17 per ton would be £630-1,070, leaving
£930-1,670 for bearers and fastenings. That is internally consistent.

The 1877 discussion also states that **concrete, paving and rails were more than three quarters
of the total expenditure**, and that the choice of rail weight and paving quality affected the
cost much more than the choice of rail support system.

### 4.4 Street track against reserved track

The measured comparison is Belgian, not British, but it is a same-system, same-year comparison
at 1 metre gauge and 42 lb rail:

| Track type | Year | Cost per mile | Ratio to independent formation |
|---|---|---|---|
| Independent formation (reserved) | 1911 | £793 | 1.00 |
| Beside a road (reserved) | 1911 | £977 | 1.23 |
| Laid in paving (street) | 1911 | £1,108-2,266 | 1.40-2.86 |

The British street figure of **£5,050 per mile** (1911) is much higher than the Belgian paved
figure because the British figure is a first-class city street track with granite setts,
concrete and bonding, while the Belgian figure is a metre-gauge light railway in paving. The
British conduit track in London was **£13,000 per mile**
against about **£8,000** for an overhead-system track, so the conduit itself is a large addition.

The modern comparison points the same way: the Bath Tram estimate puts reserved track at about
**£300,000 per km** against about **£1.5m per km** for Manchester city-centre street track, a
ratio of 1:5. The LR55 system claims £500,000 per km for street track, which would narrow the
ratio to 1:1.7. Modern figures include utility diversion and road reconstruction, which the
historical figures do not.

No measured British reserved tramway cost was found. The closest British evidence is the
Light Railways Act lines: the 1911 *Britannica* gives the average estimated capital cost of
British light railways as **£5,860 per mile** (including equipment and land, so not comparable),
and describes sleeper track on private land as cheap to maintain but gives no separate
construction rate. A British light railway with 37-40 lb rails on sleepers is recorded at
**£6,000 per mile**, but the date is not certain from the text.

### 4.5 The £600 per mile figure

The **£600 a mile in 1911** is recorded in
[prices-forum-fragments](../../New/ai/prices-forum-fragments.md) as "tram track laid, excluding
electrification", and [infrastructure-cost-synthesis](../../New/ai/infrastructure-cost-synthesis.md)
section 5 describes it as a **forge** rate: a street reservation sharing the road formation, so
trench and concrete bed only. It is therefore not a complete track cost, and the measured
£5,050 per mile for complete street permanent way does not contradict it. The two measure
different things.

The evidence does bound the rail element. At 41 lb and the 1907 import price, the rails alone
are **£419 a mile**; at 98 lb and £10 a ton they are **£1,540**. A £600 forge plus a separate way
object is therefore plausible: the forge carries the trench and concrete bed, the way carries
the rails and fastenings, and the road carries the paving. The flat rate cannot be a complete
street track and should not be described as one.

The measured complete track remains useful as an upper bound and as the source of the rail
share: 8-52 per cent of £5,050 is rail, and the rest is concrete, setts, paving, bonding,
bearers and labour.

### 4.6 Recommendation

**Charge the tram way by rail weight, and keep the forge separate.**

- Rail cost per mile = **1.5714 × rail weight in lb/yd × price per ton**. At £10 per ton:
  41 lb = £644, 55 lb = £864, 75 lb = £1,179, 85 lb = £1,336, 92 lb = £1,446, 98 lb = £1,540.
- Add fastenings and bonding. The 1877 metal figure (rails plus bearers and fastenings,
  £2,000-2,300 at 40 lb) suggests they are of the same order as the rails, but the split is not
  measured. A reasonable allowance is **£300-700 a mile** at 1911 prices.
- Do **not** add paving, setts or the concrete bed to the way. Those belong to the road object
  or to the forge. The £600/mile forge is not contradicted; the way cost is additional to it.
- Reserved track: the measured total is **£793-977 a mile** (Belgian, 1911), but that includes
  sleepers and ballast, which in the pakset may fall to the forge. The rail element alone is
  still given by the weight table.

**Confidence: medium.** The rail weights, the arithmetic and the complete street-track cost are
solid. The rail price per ton is a genuine range of 2.6 to 1; the fastenings allowance is
inferred; the reserved-track figures are Belgian.

---

## 5. Tunnels by material and diameter (21 objects)

### 5.1 The diameter series

The 1905 Copperthwaite tables give the cost per yard forward of cast-iron-lined shield tunnels
in London clay at six internal diameters, from measured quantities and current contract prices.
They exclude internal concrete lining, pointing and finishing.

| Internal diameter | Area | Cost per yard | Cost per metre | Cost per m² of area |
|---|---|---|---|---|
| 10 ft 6 in (3.20 m) | 8.04 m² | £27 18s 11d | **£30.56** | £3.80 |
| 11 ft 8.5 in (3.57 m) | 10.00 m² | £32 11s 6d | **£35.62** | £3.56 |
| 12 ft 6 in (3.81 m) | 11.40 m² | £36 8s 2d | **£39.82** | £3.49 |
| 15 ft (4.57 m) | 16.42 m² | £59 12s 4d | **£65.20** | £3.97 |
| 21 ft 2.5 in (6.46 m) | 32.82 m² | £104 10s | **£114.28** | £3.48 |
| 30 ft (9.14 m) | 65.67 m² | £227 | **£248.25** | £3.78 |

The cost per square metre of cross-section is nearly constant at **£3.48-3.97**, mean **£3.7**.
The cost per metre forward is therefore approximately:

> **cost per metre = £3.7 × excavated cross-section area in m²** (1905 prices, London clay,
> cast-iron lining, excluding internal finish).

Diameter is the primary variable, and cost rises with the square of diameter, not linearly.
This is the single most useful result in the tunnel gap: the pakset's 21 tunnel objects should
differ by cross-section, not by an arbitrary ladder.

The modern Munich figures confirm the rule. A 9.0 m single tube is €45m/km; a 10.2 m tube is
€58m/km. The area ratio is 1.285 and the cost ratio is 1.289. Ninety-five years apart, the same
relationship holds.

### 5.2 Material separation

The material evidence is real but confounded by ground conditions:

| Tunnel | Internal diameter | Ground | Year | Cost per metre |
|---|---|---|---|---|
| Brick sewer, London contract | 9 ft | good material | 1905 | **£25.15** |
| Brick sewer, London contract | 11 ft 6 in | disintegrated chalk, gravel, water | 1905 | **£49.21** |
| Iron tunnel, concrete lining only | 9 ft | London clay | 1905 | **£29.80** |
| Iron tunnel, masonry lining | 10 ft | London clay | 1905 | **£33.52** |
| Masonry tunnel under shield, Clichy | — | — | 1905 | **£30.89-40.83** |
| Sydenham brick tunnel, estimate | single track | good ground | 1877 | **£87.49** |
| Sydenham brick tunnel, actual | single track | broken ground | 1877 | **£131.23** |
| Kilsby tunnel, actual | single track | hard rock and water | 1840 | **£142.17** |
| Rotherhithe, river section | 30 ft external | Thames gravel | 1908 | **£450.57** |
| Blackwall, heavy lining | 27 ft | Thames gravel | 1897 | **£413.39** |

The 9 ft brick sewer at £25.15/m is **cheaper** than the 9 ft iron tunnel with concrete lining
at £29.80/m. The 11 ft 6 in brick sewer at £49.21/m is **dearer** than the 11 ft 8.5 in iron
tunnel at £35.62/m. The two comparisons point in opposite directions because the larger brick
sewer was in water-bearing gravel and the contractor found brick construction impracticable at
the price.

**Conclusion: the sources do not support a clean brick/stone/concrete multiplier.** Ground,
diameter and depth are larger effects than lining material. The honest treatment is:

- use the diameter/area rate as the primary cost;
- treat lining material as a **±15 per cent adjustment at most**, not as a multiplier series;
- if a material ladder is required, use brick at **0.85-1.0** of the iron-lined rate for the
  same diameter in good ground, and concrete at **0.9-1.0**. Stone masonry is within the same
  band.

This is a negative result for the original question, and it should be recorded as such rather
than filled with an invented ladder.

### 5.3 Track number

The Lindal tunnel gives a direct single-track/double-track comparison. The single-track masonry
tunnel was contracted at **$77.50 per yard** in 1849, about £15.50 at Storrow's own rate of
$5 to the pound. The engineer estimated that the same tunnel built for double track would have
cost **$225 per yard** in masonry (about £45), or **$105 per yard** in rock. The masonry ratio
is **2.9 times** for two tracks; the rock ratio is 3.5 times. That is more than double because
the double-track section is wider and higher, not merely twice the rails.

This does **not** support the open-way convention that a second parallel way costs half the
first. In a tunnel the excavation is duplicated, so the second track is the dearer part, not the
cheaper one. The halving convention applies to open parallel ways where the formation is shared;
it should not be carried into tunnels.

### 5.4 Cut-and-cover

The knowledge base already has **£120-170 per metre in cities** for cut-and-cover. No new
measurement was added. The Rotherhithe contract includes cut-and-cover approaches but does not
separate them from the shield-driven river section. The Munich model separates open construction
(€80m/km) from mined tunnel (€116m/km) for a double-track section, but that is a modern
motorway-scale tunnel, not a Victorian cut-and-cover railway.

**Cut-and-cover remains under-evidenced.** The existing range is not contradicted, but it is not
strengthened either.

### 5.5 Recommendation

**Use a diameter-based rate, not a material ladder.** At 1905 prices:

- 3.2 m (10 ft 6 in): **£30.50 per metre**
- 3.6 m (11 ft 8 in): **£35.60 per metre**
- 3.8 m (12 ft 6 in): **£39.80 per metre**
- 4.6 m (15 ft): **£65.20 per metre**
- 6.5 m (21 ft): **£114.30 per metre**
- 9.1 m (30 ft): **£248.30 per metre**

The general rule is **£3.7 × area in m²**. For a larger or smaller bore, scale by the square of
the diameter.

For lining material, apply **no more than ±15 per cent**, and record that the measured pairs are
confounded by ground. Do not create separate brick, stone and concrete rates from these sources.

**Confidence: medium-high for diameter, low for material.** The diameter series is a
quantity-based estimate with every quantity and price stated, and the modern Munich pair
confirms the area rule. The material comparisons are measured contracts but are not matched
pairs.

---

## 6. Piers as bridge substructure (111 objects)

### 6.1 The measured shares

| Structure | Year | Substructure share | Basis |
|---|---|---|---|
| Tower Bridge | 1886-89 | **15.8%** | piers and abutments £131,344 of £830,005 contract sum; 13.4-14.6% of the final building cost |
| Humber worked example | 1900 | **25%** | 1,200 ft bridge at 60 ft, 150 ft spans, piers about 25% |
| Maynard, 200 ft high piers | 1868 | **65.9%** | 15 piers at £2,140 = £32,100 of £48,740 |
| Maynard, 60 ft spans, 200 ft piers | 1868 | **82.3%** | 26 piers at £2,140 = £55,640 of £67,640 |

The share is not a property of bridges in general. It is a function of **pier height and span**:

- A major river bridge with deep foundations but relatively few, massive piers: **13-16 per cent**.
- A 60 ft high bridge with 150 ft spans: **25 per cent**.
- A tall viaduct with 200 ft piers: **66 per cent**.
- The same tall viaduct with short spans, so that piers are numerous: **82 per cent**.

Maynard states the economics explicitly: where piers are high, large spans are more economical;
where piers are low, small spans and more piers are cheaper. Brunel made the same point in the
1850 Chapple Viaduct discussion: the cheapest span depends on the cost of the piers and their
foundations. The share is therefore a design variable, not a constant.

### 6.2 Component prices that are useful

- **Iron pier against masonry pier, 1868**: a complete iron pier cost **£2,541 18s** against
  **£4,110 0s 6d** for the masonry pier of the same duty, about **38 per cent cheaper**. The
  iron pier used 163 tons of castings at £13 and 7 tons of wrought iron at £16, with 1,400 cubic
  feet of ashlar and 42 yards of concrete. The masonry pier used 1,041 yards of footing masonry
  and 2,120 yards of masonry. These are complete pier costs, not shares.
- **Crumlin Viaduct, 1868**: gross cost **£68,800**, or **£41 10s per foot**, for 1,658 ft on
  ten 150 ft spans with iron piers. The ironwork material value was 1.09 tons per foot at £16
  per ton, or £17 9s per foot, which is 42 per cent of the gross. The remaining 58 per cent
  covers piers, abutments, flooring, erection and profit, so it is not a clean substructure
  share, but it is consistent with a tall viaduct having a substructure share above half.

### 6.3 Recommendation

**Leave the piers unpriced.** The bridge object already includes the structure, and the
substructure share ranges from 16 to 82 per cent depending on height and span. The pakset
deliberately does not cost bridge height or span, so a single pier charge would be wrong for
most bridges and would introduce a second arbitrary variable. This is now an evidence-based
decision, not an assumption.

If the pakset later decides to charge piers, the defensible rates are:

- **13-25 per cent** of the bridge cost for a low bridge or viaduct (13 per cent for Tower
  Bridge, 25 per cent for a 60 ft bridge);
- **50-65 per cent** for a tall viaduct (150-200 ft);
- the measured maximum was **82 per cent**, for a 200 ft viaduct with 60 ft spans.

**Confidence: high for the range, low for any single share.** The four cases agree that the
share rises with pier height and falls with span. None of them gives a British nineteenth-century
average, and no average would be meaningful without the height distribution of the bridge stock.

---

## 7. What remains open

1. **Headquarters: a measured 55 Broadway cost.** The floor area (31,000 sq ft) and all the
   construction details are published; the cost is in the TfL Corporate Archives but not online.
   An archive request for LT000157 and the 1928 "estimated expenditure" item would close it.
2. **Headquarters: a bus or airline head office.** No measured British figure was found. The
   London General Omnibus Company was inside 55 Broadway from 1924, so it is not a separate
   building. Provincial bus offices were small and unrecorded in the sources searched.
3. **Headquarters: a railway headquarters other than Euston.** Paddington, Derby and York were
   searched but returned station histories, not itemised office contracts. The GWR and Midland
   accounts may hold them; they were not reachable online within this pass.
4. **Maglev: an as-built guideway-only cost.** The Munich figure is a 2007 planning estimate for
   a cancelled line. Shanghai and Incheon publish whole-system costs only. No operator publishes
   a guideway-only as-built rate.
5. **Tram track: a British reserved-track contract.** The measured reserved-track comparison is
   Belgian (1911). The British Light Railways Act lines exist, but no itemised permanent-way
   contract was found.
6. **Tram track: the domestic rail price.** The Board of Trade had no domestic price. The
   British export price is nearly three times the import price and the reason is not stated.
   A municipal contract ledger for 1900-1914 would settle it.
7. **Tunnels: cut-and-cover.** The existing £120-170/m range is not contradicted but was not
   strengthened. A London or provincial cut-and-cover contract with a stated length would help.
8. **Tunnels: a clean material pair.** The brick and iron prices are measured, but the ground
   differs between the pairs. A single contract with two lining designs in the same ground was
   not found.
9. **Piers: a British average share.** The four sources give a range, not an average. A sample
   of, say, twenty viaduct contracts with component costs would give a distribution, but that is
   a much larger task than this pass.

---

## 8. Search record

One search per turn. The built-in `websearch` was used; no Exa MCP search tool was exposed in
this session.

| Turn | Query subject | What it returned |
|---|---|---|
| 1 | British railway headquarters building costs, Euston, Paddington, Derby, York, 55 Broadway | Survey of London Euston account (£150,000); Metadyne District Railway history; TfL 55 Broadway guide; Paddington station history; no itemised office contracts |
| 2 | 55 Broadway construction cost and floor area | TfL guide and archive catalogue, Metadyne, listing text; 31,000 sq ft; no cost figure |
| 3 | British office construction cost per square foot 1900-1990 | County Hall contract and floor areas; Port of Liverpool Building; Maiwald building cost index; Costmodelling 2026 rates |
| 4 | Cunard Building construction cost | Cunard archive catalogue, centenary article, building history; no contract sum |
| 5 | Maglev guideway cost per kilometre, Shanghai, Emsland, Japan, Korea | Korea Urban Maglev Program paper; Shanghai construction paper; Maglev 2004 comparison; FRA 2005 report; Almujibah and Preston 2018 |
| 6 | Transrapid guideway cost per kilometre alone and guideway share | Vieregg-Rössler 2007 Munich cost model with guideway-only rates; 1993 Hamburg-Berlin study; Maglev 2004 guideway share |
| 7 | British tramway track cost per mile and rail price per ton by weight | Hansard 1908 tram rail import and export values; 1911 Britannica tramway article; 1877 ICE street tramway discussion; 1906 Paterson paper |
| 8 | British domestic tram rail price per ton 1895-1913 | Hansard 1908 again; Accrington relaying item; no domestic contract price |
| 9 | Reserved tramway track cost per mile against street track | 1911 Britannica light railways (Belgian £793/£977/£1,108-2,266 per mile); Bath Tram modern costs; Quainton 1870 rail price |
| 10 | Tunnel cost per metre by material, diameter and track number | 1877 Sydenham paper; Copperthwaite 1905 full text with Statement I; Rotherhithe 1909; Storrow 1862; Lindal single/double comparison |
| 11 | Viaduct substructure share, piers, foundations, abutments | Tower Bridge contract list; 1850 Chapple discussion; 1905 concrete viaduct discussion; Maynard 1868 Viaduct Works Handbook with pier estimates |
| 12 | British bus company head office building cost, 1920-1970 | Bristol Omnibus 1958 bus station £200,000 (a station and garage, not an office); National Bus Company 1969 headquarters at 25 New Street Square with no cost; Bristol Archives catalogue; no measured office cost |

Pages fetched and read in full: Survey of London Euston and County Hall chapters; Metadyne
District Railway history; Wikipedia Port of Liverpool Building; Vieregg-Rössler Munich cost
model; 1911 Britannica Tramway and Light Railways; Hansard 1908 returns; Hansard 1975 returns;
Copperthwaite 1905 (full text, 400 pages, downloaded and searched locally); Storrow 1862 (full
text, downloaded and searched locally); Maynard 1868 (full text, downloaded and searched
locally); Costmodelling 2026 table; Tower Bridge contracting page.

Three limitations are recorded rather than concealed. The 1877 Sydenham and 1909 Rotherhithe
figures come from the published ICE abstracts; the full papers are paywalled and were not read.
The FRA 2005 PDF returned HTTP 403, so its cost range is quoted from the CalPoly 2009 report and
used as context only. The Munich 2007 model was read in full on the author's own page.

---

## 9. Sources

1. *Survey of London*, vol. 21, part 3, pp.107-114, "Euston Station and railway works" (1949).
   https://www.british-history.ac.uk/survey-london/vol21/pt3/pp107-114
2. *The New Euston Station 1968*, BRB Residuary, p.2. Barrowmore Model Railway Group PDF.
3. Metadyne, "The District Railway HQ" (2019).
   http://www.metadyne.co.uk/DistrictPages/MDR_55_Broadway.html
4. TfL Corporate Archives, *Research Guide No 8: 55 Broadway*.
   https://content.tfl.gov.uk/research-guide-8-55-broadway.pdf
5. *Survey of London* Monograph 17, *County Hall* (1991), chapters V and "The north front".
   https://www.british-history.ac.uk/survey-london/bk17/pp49-56
6. National Museums Liverpool, Archive sheet 35, Port of Liverpool Building; and Wikipedia,
   "Port of Liverpool Building" (footprint, five floors, cost).
   https://en.wikipedia.org/wiki/Port_of_Liverpool_Building
7. Hansard, HC Deb 5 November 1975, vol. 899, cc.229-32W, government office space and costs.
   https://api.parliament.uk/historic-hansard/commons/1975/nov/05/government-property
8. Costmodelling, "Typical UK Construction Costs of Buildings", release 1 July 2026.
   https://costmodelling.com/building-costs
9. Vieregg-Rössler GmbH, *Ermittlung der wahrscheinlichen Baukosten der geplanten
   Transrapid-Strecke München Hbf - Flughafen München*, March 2007.
   http://www.vr-transport.de/vr/tr_kosten2007.html
10. Vieregg-Rössler GmbH, *Wirtschaftlichkeit des Transrapid-Vorhabens Hamburg-Berlin*, 1997.
    http://www.vr-transport.de/transrapid-wirtsch/n004t.html
11. "Comparison of Maglev Projects Planned for U.S. and Germany using Transrapid Technology",
    Maglev 2004 conference.
    http://www.maglev.ir/eng/documents/papers/conferences/maglev2004/topic1/IMT_CP_M2004_T1_6.pdf
12. US Federal Railroad Administration, *Report to Congress: Costs and Benefits of Magnetic
    Levitation*, September 2005 (direct PDF returned HTTP 403; figures quoted via source 30).
    https://railroads.dot.gov/sites/fra.dot.gov/files/fra_net/1176/maglev-sep05.pdf
13. H. Almujibah and J. Preston, "The total social costs of constructing and operating a maglev
    line", *Transportation Systems and Technology* 4(3), 2018.
    https://eprints.soton.ac.uk/427209/2/maglev_line.pdf
14. Hansard, HC Deb 11 November 1908, vol. 196, cc.272-4, tram rail import and export values.
    https://api.parliament.uk/historic-hansard/commons/1908/nov/11/imports-of-ship-plates-and-tram-rails
15. *Encyclopaedia Britannica*, 11th edition (1911), "Tramway", by Emile Garcke.
    https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Tramway
16. *Encyclopaedia Britannica*, 11th edition (1911), "Railways/Light Railways".
    https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Railways/Light_Railways
17. Institution of Civil Engineers, *Minutes of the Proceedings*, 1877, "Discussion. Street
    Tramways". https://doi.org/10.1680/imotp.1877.22319
18. A. Paterson Jr, "On tramway permanent-way construction", ICE *Minutes* 165 (1906), 238-248.
    https://doi.org/10.1680/imotp.1906.16756
19. Buckinghamshire Railway Centre Stockbook, Quainton tramway article (30 lb rails at
    £8 2s 6d per ton, 1870). https://www.brc-stockbook.co.uk/qn_15_09.htm
20. Bath Tram, "Track types" (modern reserved and street track costs).
    https://bathtram.org/tfb/tT30.htm
21. W. C. Copperthwaite, *Tunnel Shields and the Use of Compressed Air in Subaqueous Works*,
    Archibald Constable, London, 1905 (preface dated October 1905), Statement I and pp.370-371.
22. ICE *Minutes of the Proceedings*, 1877, "On tunnel construction, and on the Sydenham
    Tunnel" (published abstract only). https://doi.org/10.1680/imotp.1877.22518
23. ICE *Minutes of the Proceedings*, 1909, "The Rotherhithe Tunnel" (published abstract only).
    https://doi.org/10.1680/imotp.1909.17453
24. C. S. Storrow, *Report on European Tunnels*, Boston, 1862, including Kilsby, Lindal,
    Woodhead and the Brotherhood evidence.
25. Tower Bridge, "Contracting" (the eight contract values).
    https://towerbridge.me.uk/contracting/
26. H. N. Maynard, *The Viaduct Works Handbook*, E. and F. N. Spon, London, 1868, including
    the Crumlin Viaduct, iron and masonry pier costs, and the span-cost examples.
    https://tekniskkulturarv.dk/book/0ae58308-6caa-4d82-80dd-4688a268fb94/the-viaduct-works-handbook.pdf
27. ICE *Minutes of the Proceedings*, 1850, "Discussion. The Chapple Viaduct".
    https://doi.org/10.1680/imotp.1850.24163
28. ICE *Minutes of the Proceedings*, 1905, "Discussion. On the construction of a concrete
    railway viaduct". https://doi.org/10.1680/imotp.1905.16884
29. `New/ai/infrastructure-cost-evidence.md` sections 2, 4, 6 and 9, for the figures already in
    the knowledge base (Humber piers 25%, DLR viaduct £19-24m/km, cut-and-cover £120-170/m).
30. C. Nuworsoo, *Preliminaries to a Feasibility Analysis of the Maglev Proposal of the Southern
    California Association of Governments for the Region*, Cal Poly, 2009, quoting the FRA 2005
    report. https://digitalcommons.calpoly.edu/crp_fac/51
