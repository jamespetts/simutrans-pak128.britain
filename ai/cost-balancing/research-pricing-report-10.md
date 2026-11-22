---
status: draft
verified: none
---
# Research pass 10: British capital costs of road furniture

**Covers**: traffic signals (police-controlled, automatic, 1960s and modern LED), road signs
(speed-limit, one-way, no-entry, direction and motorway gantry), level-crossing and rail gates,
loading bays, truck stops, bus stations, bus stops and shelters, and street furniture
cross-checks. Rows are in `ai/temp/research-pricing-rows-10.csv` (136 rows).

Nothing under `New/` was modified. No git command was run. All money is nominal, with the year
of the price; no deflation, escalation or conversion to 1900 prices has been applied. No
Simutrans `.dat` price was used as evidence, and no figure was fitted to the pakset.

---

## 1. What was priced, and a correction to the brief

The brief names 46 roadsign objects and 12 road stop objects. The checked-out files inspected
contain fewer distinct road-furniture objects than that:

- `New/ways/roadsign.dat`: 5 road signs (`OneWay`, `NoEntry`, `MotorwaySign`, `ChooseSign`,
  `PrivateRoad`) and 3 traffic lights (`traffic_light`, `traffic_light_mellor`,
  `traffic_light_led`).
- `New/ways/roadsign-old.dat`: 1 sign (`ChooseSignOld`).
- `New/ways/speedsignal.dat`: 24 rail speed boards (60, 100 and 121 mph, four railway eras,
  standard and narrow gauge).
- `New/ways/signals.dat`: the `Railgate` object.
- `New/stations/bus-stops.dat`: 9 stop objects, of which 7 have no `cost` line.
- `New/stations/truck-stops.dat`: 11 stop objects, none with a `cost` line.

That is 34 road-signal/sign objects and 18 unpriced stop objects on a literal reading. The
brief's 46 and 12 may include rail signals, maglev signals or other stop types. This report
prices the categories, not a fixed object count, so the rates apply to whichever objects the
pricing team maps onto them.

Two consequences for mapping:

1. The `traffic_light*` objects are junction-level objects in the pakset. The measured
   per-junction figures are therefore the primary evidence; the per-head figures are given so
   that a junction can be rebuilt from components.
2. The truck stops are graded by `level` (1, 2, 3, 4, 6). The evidence supports a cost per HGV
   space and a cost per square metre of hardstanding, not a cost per level. The level should be
   mapped to a number of spaces and a welfare building.

---

## 2. Traffic signals

### 2.1 Measured figures

| Year | Item | Figure | Unit | Source |
|---|---|---|---|---|
| 1929 | Early automatic signal installation, national estimate | 100 | GBP per installation | Royal Commission on Transport 1929, via Hamilton et al. 2013 |
| 1932 | Set of lamps at the four corners of a cross road | 300 | GBP per junction | Hansard HL 21 Jun 1932 |
| 1932 | Signal head, derived from the above | 75 | GBP per head | Derived, low confidence |
| 1932 | London junction installation | 400-500 | GBP per junction | Hansard HL 21 Jun 1932 |
| 1932 | Piccadilly scheme, several junctions | 1,800 | GBP per scheme | Hansard HC 8 Feb 1932 |
| 1939 | Complete vehicle-actuated installation, ordinary crossroads | 650-850 | GBP per junction | Hansard HC 26 Jul 1939 |
| 1939 | Additional three-light head, face only | 8 10s | GBP per head | Hansard HC 26 Jul 1939 |
| 1954 | Press-button pedestrian crossing signals | 350-850 | GBP per crossing | Hansard HC 18 May 1954 |
| 1956 | Traffic-light pedestrian crossing | 400-3,000 | GBP per crossing | Hansard HC 19 Dec 1956 |
| 1963 | Traffic signals at a crossroads, average | 3,100 | GBP per junction | Hansard HC 18 Dec 1963 |
| 1983 | Hyde Park Corner experiment, major multi-arm junction | 75,000 | GBP per scheme | Hansard HL 11 Apr 1983 |
| 1989 | MOVA conversion, small or medium junction | 12,200 | GBP per junction | TRL TAL 3/97 |
| 1989 | MOVA conversion, large junction | 19,800 | GBP per junction | TRL TAL 3/97 |
| c.1995 | SCOOT installation at a junction | 20,000-25,000 | GBP per junction | KonSULT |
| 2010 | Signal control at a simple T junction | 90,000 | GBP per junction | Warwickshire CC |
| 2017 | 3-aspect LED head | 526.42 | GBP per head | Southend BC |
| 2017 | 2-aspect LED head | 255.53 | GBP per head | Southend BC |
| 2017 | 1-aspect LED head | 106.44 | GBP per head | Southend BC |
| 2017 | Mounting post | 400 | GBP per post | Southend BC |
| 2017 | OMCU controller | 2,675.65 | GBP per controller | Southend BC |
| 2017 | OTU outstation transmission unit | 1,945.59 | GBP per unit | Southend BC |
| 2020 | Junction refurbishment, all on-site equipment | 120,000 | GBP per junction | York CC |
| 2020 | Junction refurbishment plus new pedestrian facilities | 150,000 | GBP per junction | York CC |
| 2021 | UTC signal junction, commuted sum | 52,653.06 | GBP per junction | BANES |
| 2023 | Average per site, 9 junctions and 81 crossings | 72,222 | GBP per site | West Sussex CC |
| 2025 | Signal junction, commuted sum | 57,496.93 | GBP per junction | Suffolk CC |
| 2025 | Pelican/Toucan crossing, commuted sum | 36,324.24 | GBP per crossing | Suffolk CC |

### 2.2 The police-controlled and early automatic era, 1926-1939

The 1926 Piccadilly trial was a police officer in a cabin operating switches; the first
automatic installation was at Princes Square, Wolverhampton, in November 1927, and it was made
permanent on poles in October 1928. Neither installation has a published cost that could be
found. The 1929 Royal Commission figure of about GBP100 per installation is the only national
estimate for the earliest automatic equipment. It appears too low for a complete junction with
four heads, poles and a controller, but the source does not say what is included, so it is
recorded as a lower bound only.

The 1932 Lords debate gives two incompatible figures. Lord Denbigh said about GBP300 for "a set
of lamps ... at each of the four corners of a cross road"; the Earl of Plymouth, replying for
the Government, said the cost "at each junction is, in London, from GBP400 to GBP500". If the
GBP300 is per corner, the junction cost is GBP1,200, which is two to three times the Minister's
figure. The Minister's figure is the more authoritative and is consistent with the 1939 range.
The derived GBP75 per head is therefore weak, and is marked low confidence.

By 1939 the technology and the accounting are clear: a complete vehicle-actuated installation at
an ordinary crossroad cost GBP650-850, with annual maintenance of GBP70-85. The additional
three-light head at GBP8 10s is a face only; it excludes fitting and cable alterations. It
cannot be multiplied by four to reconstruct a junction.

### 2.3 The 1950s and 1960s

The 1954 answer separates press-button signals with and without vehicle-actuated pads: GBP350
without, GBP850 with. The 1956 answer gives a much wider GBP400-3,000 for a traffic-light
pedestrian crossing, which shows how much the site and the type of installation dominated. The
1963 answer is the cleanest post-war figure: GBP3,100 average for a set of signals at a
crossroads. That is 4.1 to 4.8 times the 1939 figure after 24 years, a nominal compound rate of
about 6.1-6.8 per cent a year. No separate 1960s per-head price was found.

### 2.4 The 1970s to 2000s

The MOVA and SCOOT figures are equipment and commissioning costs at an existing junction, not
complete junction builds. MOVA conversion was GBP12,200 at a small or medium junction and
GBP19,800 at a large one, at 1989 prices. SCOOT was GBP20,000-25,000 a junction, but the
guidebook page is undated. These are useful for the cost of the control system and detectors;
they do not include poles, ducting, civils or traffic management.

There is a real gap between the 1963 GBP3,100 and the 2010 GBP90,000. The only intermediate
British figures found are the 1983 Hyde Park Corner experiment at GBP75,000 (a major multi-arm
scheme, not an ordinary junction) and the equipment-only MOVA/SCOOT figures. The recommended
1970-1990 band in section 8.1 is therefore interpolated and marked low confidence. It should not
be presented as measured.

### 2.5 Modern LED equipment

The Southend 2017 schedule is the best component breakdown found. It gives replacement costs
including 15 per cent labour:

- 3-aspect LED head: GBP526.42
- 2-aspect LED head: GBP255.53
- 1-aspect LED head: GBP106.44
- mounting post: GBP400
- OMCU controller: GBP2,675.65
- OTU: GBP1,945.59
- MVD detector: GBP308.86
- kerbside detector: GBP601.01
- wait lamp: GBP248.50

A four-arm junction built from these parts is about GBP8,300 of equipment: four heads at
GBP526.42 = GBP2,105.68, four posts at GBP400 = GBP1,600, one controller GBP2,675.65 and one OTU
GBP1,945.59. The measured junction figures of GBP57,000-150,000 are therefore mostly civils,
ducting, cabling, controller configuration, design and traffic management, not signal heads.
That is the single most important point for pricing a junction object: use the per-junction
figure, not four times the head price.

No separate historical pole or controller price was found. The 1932 and 1939 figures are
complete installations, and the 1939 GBP8 10s is a face only. The first clean separation of
head, post and controller is the Southend 2017 schedule.

The 2020 York figures are refurbishments of all on-site equipment: GBP120,000 without new
pedestrian facilities and GBP150,000 with them. The 2021 BANES and 2025 Suffolk figures are
commuted sums, which are whole-life asset replacement rates rather than tender prices; they sit
below the York and Warwickshire tender figures for that reason. The 2023 West Sussex figure is a
programme average over 9 junctions and 81 crossings, so it mixes very different site types.

---

## 3. Road signs

### 3.1 1935: the only pre-war supply breakdown

The 1935 Hansard answer separates the components of a 30 mph speed-limit sign:

| Component | Price | Notes |
|---|---|---|
| Standard or post | 17s 6d | Supply only |
| Beacon globe | about 5s | Supply only |
| Speed-limit disc, plain | about 5s | Supply only |
| Speed-limit disc, best reflecting | 20s | Supply only |
| Complete plain sign on a new post | 22s 6d (GBP1.125) | Derived |
| Complete reflecting sign on a new post | 37s 6d (GBP1.875) | Derived |

The same session gives 4,000 de-restriction signs at an estimated GBP1,700, or 8s 6d each. That
is less than the price of a standard alone, so it must be a plate-only figure. These are supply
prices: the Minister says the signs were "purchased and erected by highway authorities", but the
answer does not give the erection labour.

### 3.2 1972 to 2005

The TRRL 1972 bilingual-sign study is the first complete supply-and-erect figure with lighting:
about GBP200 for a simple crossroads advance direction sign and GBP170 for a Y-junction list
sign, both with three to five destinations and 4-inch lettering. The bilingual versions were
about GBP325 and GBP315. A supplementary panel was about GBP4 excluding fitting labour.

The 1989 DfT metric-conversion estimates are useful because they separate the work:

- plate over an existing sign: GBP185 per sign
- plate over, then unveil: GBP90 per sign
- extra cost for a 10-year replacement programme: GBP30 per sign

These are conversion costs, not new signs, and the first includes the plate and fitting but no
post. The 2005 Irish changeover average of EUR140 (about GBP100) per sign modified or installed
is a useful cross-check but is not British.

### 3.3 Modern supply and erection

The best measured British average is Portsmouth's 2007/8 20 mph programme: 3,128 new primary and
repeater signs on new posts plus roundels, total GBP312,671.28 including GBP30,668.03 of design,
or GBP99.96 per sign. That is a large urban programme with economies of scale.

The modern council schedules then bracket the stand-alone sign:

| Year | Item | Figure | Source |
|---|---|---|---|
| 2017 | Advance direction sign, scheme rate | 5,000 | Leicestershire CC |
| 2017 | Direction sign, scheme rate | 500 | Leicestershire CC |
| 2017 | Illuminated regulatory sign (Diag 670/671) | 355 | Leicestershire CC |
| 2020 | Single sign and post, including design and traffic management | 1,400 | Buckinghamshire CC |
| 2020 | Illuminated sign, all works | 3,000 | Buckinghamshire CC |
| 2020 | 20 mph sign and post | 500 | Faversham TC |
| 2020 | Sign fixed to an existing post | 300 | Faversham TC |
| 2024 | Warning or regulatory sign on a new post | 300-800 | Wiltshire CC |
| 2024 | Directional sign on new posts | 600-1,100 | Wiltshire CC |
| 2024 | Additional cost to illuminate | about 1,500 | Wiltshire CC |
| 2024 | Basic warning sign and post | from 635 | Kent CC |
| 2024 | Speed-limit repeater sign | 320 | Kent CC |
| 2024 | One-way or no-entry sign, illuminated, new post | 745 | Kent CC |
| 2025 | Non-illuminated standard sign, commuted sum | 157.71 | Suffolk CC |
| 2025 | Non-illuminated ADS, commuted sum | 483.07 | Suffolk CC |
| 2025 | Illuminated road sign, commuted sum | 1,908.87 | Suffolk CC |

The pattern is consistent: a small unlit regulatory sign on a new post is GBP300-800; an
illuminated one is GBP745-3,000; a direction sign is GBP500-1,100, with large advance direction
signs at GBP5,000 or more. The Suffolk commuted sums are lower because they are asset
replacement values, not full scheme costs with design and traffic management.

### 3.4 Motorway gantries and overhead signs

| Year | Item | Figure | Unit | Source |
|---|---|---|---|---|
| 1984 | Flashing motorway speed warning sign | 600 | GBP per sign | Hansard HC 18 Dec 1984 |
| 1984 | Back-to-back post-mounted matrix signals, 3 km spacing | 46,000 | GBP per site | Hansard HC 18 Dec 1984 |
| 1984 | Overhead system of three gantries | 231,000 | GBP per carriageway | Hansard HC 18 Dec 1984 |
| 1984 | One gantry, derived | 77,000 | GBP per gantry | Derived |
| 1998 | Average motorway gantry, including installation delay | 400,000 | GBP per gantry | New Civil Engineer |
| 2000 | Portal gantry structure, early design | about 100,000 | GBP per gantry | Contract Journal (historical) |
| 2000 | Gantry signalling and surveillance equipment | 15,000-60,000 | GBP per gantry | Contract Journal (historical) |
| 2021 | Super-span portal structure, non-access, 38 m | 72,500 | GBP per gantry | Highways England |
| 2021 | Super-span portal structure, full access, 34.5 m | 130,000 | GBP per gantry | Highways England |
| 2021 | Cantilever over 15 m, non-access | 53,500 | GBP per gantry | Highways England |
| 2021 | MS4/MS3 cantilever, non-access | 12,100 | GBP per gantry | Highways England |
| 2021 | Super-span location with signs and power, all-in | about 1,500,000 | GBP per gantry | Highways England |
| 2024 | MS4 accessible gantry, baseline per location | 50,000 | GBP per gantry | National Highways |

The 1984 answer is the cleanest early figure: GBP231,000 per carriageway for three gantries
including the signals, or GBP77,000 per gantry. The 1998 average of GBP400,000 is not comparable
without subtracting the GBP230,000 attributed to lane-closure delay; the structure and
installation alone are about GBP170,000. The 2021 Highways England schedule separates structure
from installation and from technology: a non-access super-span structure is GBP72,500, but the
same location with signs and power is about GBP1.5m. The gap is foundations, civils, installation,
technology and power, not steel.

For a pakset object that represents a single overhead sign rather than a full gantry, the
roadside motorway sign figures (GBP600 in 1984; over GBP4,000 for a large new post-mounted sign in
2009) are more appropriate than the gantry figures.

---

## 4. Level crossings and rail gates

### 4.1 Measured figures

| Year | Item | Figure | Unit | Source |
|---|---|---|---|---|
| 1875 | Brick signal cabin at a crossing | 16 | GBP per cabin | Cambrian Railways engineer's report |
| 1923 | Signalbox required for a crossing | 780 | GBP per box | GWR letter |
| 1928 | Crossing deck fitment renewal | 82 | GBP per crossing | GWR internal cost |
| 1929 | Crossing eliminated by a bridge, average | 19,375 | GBP per crossing | Hansard HC 28 Feb 1929 |
| 1957 | Complete AHB installation, Netherlands | 2,000-2,500 | GBP per crossing | MoT 1957 report |
| 1961 | First British AHB, Spath | 5,000-6,000 | GBP per crossing | Financial Times, via Derby Signalling |
| 1969 | Average AHB installation, pre-Hixon | 8,600 | GBP per crossing | Hansard HC 2 Dec 1969 |
| 1969 | AHB to post-Hixon standards, minimum | 13,000 | GBP per crossing | Hansard HC 2 Dec 1969 |
| 1984 | AHB installation | 70,000 | GBP per crossing | Hansard HC 26 Mar 1984 |
| 1984 | Manually controlled full-barrier installation | 120,000 | GBP per crossing | Hansard HC 26 Mar 1984 |
| 2014 | Obstacle-detection upgrade, Germany | 100,000 | EUR per crossing | Dent and Marinov 2017 |
| 2019 | Carnoustie upgrade, two barriers to four | 5,500,000 | GBP per crossing | Network Rail |
| 2022 | Miniature stop lights at a user-worked crossing | 120,000-150,000 | GBP per crossing | Rail Engineer |

### 4.2 What the figures mean

The 1961 Spath installation is the first British automatic half-barrier. It cost GBP5,000-6,000
and replaced a gated crossing and a signalbox; the Financial Times estimated a net saving of
about GBP2,000 a year in three signalmen's wages and maintenance. By 1969 the average was
GBP8,600, and the post-Hixon modifications raised the minimum to GBP13,000. By 1984 an AHB was
GBP70,000 and a manually controlled full-barrier crossing GBP120,000, with annual operating and
maintenance of GBP400 against GBP21,000. The GBP21,000 is mostly staffing, which is why the
manually controlled crossing is so much more expensive over its life.

The modern figures are much higher because they include obstacle detection, four barriers,
renewed road surfaces, signalling interfaces and road closures. Carnoustie at GBP5.5m is a major
upgrade on a busy east coast main line crossing, not a typical installation. The GBP120,000-
150,000 miniature-stop-light figure is for a user-worked crossing, a much lighter intervention
than a full barrier.

The 2024 Cambridge re-signalling order is often quoted as "GBP0.9m per crossing", but the
Inspector's wording is that combining the crossing upgrades with the re-signalling would **save**
about GBP0.9m per crossing on average. It is a saving, not a cost, and is not used as a price row.

### 4.3 The manual gate set: an explicit gap

No measured price for a set of timber level-crossing gates, posts and winding gear was found.
The sources describe the gates and the legislation but not the contract price. The nearest
British figures are:

- the 1961 Spath AHB at GBP5,000-6,000, which replaced the gates and the signalbox;
- the 1928 Croesor deck renewal at GBP82, which is the road/rail surface, not the gates;
- the 1875 crossing cabin at GBP16.

A gate set is a small fraction of a complete crossing installation. For the `Railgate` object,
the honest recommendation is to price it as a timber gate, two hanging posts and simple
fastenings, and to record the price as an estimate rather than a measurement. The 1961 AHB
figure should not be divided by four and called a gate price.

---

## 5. Loading bays and truck stops

### 5.1 Hardstanding per square metre

| Year | Surface | Figure | Unit | Source |
|---|---|---|---|---|
| 1879 | Granite setts, 7.5 in, on foundation, Liverpool | 0.6329 | GBP per m2 | ICE Minutes |
| 1879 | Granite setts, asphalt-jointed, Liverpool | 0.6777 | GBP per m2 | ICE Minutes |
| 1897 | Ordinary concrete, 6 in including bottoming | 0.2392 | GBP per m2 | Shoreditch MOH |
| 1897 | Tar paving, 4 in including bottoming | 0.1495 | GBP per m2 | Shoreditch MOH |
| 1897 | York stone, 3 in | 0.5158 | GBP per m2 | Shoreditch MOH |
| 1906 | Tarmac, 2s a square yard | 0.1196 | GBP per m2 | Existing KB |
| 2015 | Surface car parking | 55-80 | GBP per m2 | Building.co.uk |
| 2019 | Concrete lorry park | 60 | GBP per m2 | COMREW |
| 2025 | Carriageway surfacing, commuted sum | 28.72-40.97 | GBP per m2 | Suffolk CC |
| 2026 | Heavy-duty pavement for HGV yards | 80-150 | GBP per m2 | JRG Civils |

The historical rates convert at 0.836127 m2 per square yard. They are street and footway
contract rates, used here as hardstanding proxies because no separate goods-yard paving series
was found. The 1879 Liverpool setts at about GBP0.63-0.68/m2 are the heavy-duty end; the 1897
tar at about GBP0.15/m2 is the cheap end.

The modern range is wide because the specification is wide. A standard asphalt carriageway at
GBP29-41/m2 is not an HGV yard. A surface car park at GBP55-80/m2 is a light-duty standard. A
concrete lorry park at GBP60/m2 and a heavy-duty HGV pavement at GBP80-150/m2 are the relevant
rates for a truck stop or a loading bay used by heavy vehicles. The 2026 guide's own comparison
is GBP80-150/m2 for heavy-duty pavement against GBP40-60/m2 for domestic driveways.

### 5.2 Truck stops per HGV space

| Year | Item | Figure | Unit | Source |
|---|---|---|---|---|
| 2014 | Lorry park construction, White Cliffs site 57 | 29,373 | GBP per space | AECOM/KCC |
| 2014 | Lorry park construction, Westenhanger site 8 | 29,857 | GBP per space | AECOM/KCC |
| 2014 | Lorry park construction, Ashford site 6 | 29,100 | GBP per space | AECOM/KCC |
| 2014 | Capital including land, Westenhanger site 8 | 31,020 | GBP per space | AECOM/KCC |
| 2014 | Capital including land, White Cliffs site 57 | 36,727 | GBP per space | AECOM/KCC |
| 2014 | Capital including land, Ashford site 6 | 44,004 | GBP per space | AECOM/KCC |
| 2021 | London Gateway truck park, total project per m2 | 239 | GBP per m2 | Find a Tender |
| 2025 | Southampton pre-gate truck park, total project per m2 | 236 | GBP per m2 | Earlcoate |
| 2024 | New HGV space, DfT/industry programme average | 38,372 | GBP per space | DfT |

The AECOM study is the strongest evidence because it costs three layouts from the same
methodology: construction is remarkably consistent at GBP29,100-29,857 per modelled space
(2016 price base, 2014 report), excluding land. Land adds GBP1,163-14,904 per space depending
on the site, so the land-inclusive range is GBP31,020-44,004. The study assumes a standard bay
of 15 m x 3 m = 45 m2, so the construction rate is about GBP647-663 per m2 of bay area. That is
higher than the hardstanding rate because it includes earthworks, drainage, lighting, security,
circulation and site infrastructure, not just the surface.

The London Gateway and Southampton figures are total project costs divided by site area:
GBP239/m2 and GBP236/m2 respectively. They include buildings, welfare facilities and port
infrastructure, so they are all-in site rates, not hardstanding. The DfT 2024 figure of
GBP38,372 per new space is a programme average across 38 truckstops, including showers,
restaurants, lighting and fencing; it is an all-in upper bound for a welfare-equipped site.

### 5.3 Recommended treatment of loading bays and truck stops

A loading bay and a truck stop are the same physical thing at different scales: a hardstanding
area, a means of access, and sometimes a building. The evidence supports a build-up:

- hardstanding: GBP30-60/m2 for light or standard duty, GBP80-150/m2 for heavy HGV duty;
- site infrastructure and security: the AECOM per-space figure, about GBP29,000-30,000 per
  HGV space including earthworks, drainage, lighting, fencing and circulation;
- land: GBP1,000-15,000 per space, site-dependent;
- drivers' building: use building costs per m2, not a truck-stop-specific rate. No measured
  British truck-stop building rate per m2 was found. The DfT programme average of GBP38,372
  per space includes welfare works and is the best all-in check.

For the 1852-1920 loading bays, the historical hardstanding rates (GBP0.15-0.68/m2) plus a
timber or brick shed from the station-building evidence in the knowledge base are the only
defensible build-up. The 1852 object should not be priced from a modern truck-stop rate.

---

## 6. Bus stations, terminals and stops

### 6.1 Bus stations per stand and per square metre

| Year | Scheme | Total | Stands | Per stand | Per m2 | Source |
|---|---|---|---|---|---|---|
| 2001 | Walsall | 3,764,889 | 14 | 268,921 | 1,101.35 | Architects' Journal |
| 2021 | Halifax | 17,700,000 | not stated | - | - | WYCA |
| 2022 | Heckmondwike | 4,970,000 | 6 | 828,333 | - | Kirklees Council |
| 2022 | Crawley | 7,400,000 | not stated | - | - | Crawley BC |
| 2024 | Dewsbury | 23,004,469 | not stated | - | - | WYCA |
| 2024 | Huddersfield | 19,995,380 | not stated | - | - | WYCA |
| 2024 | Kingston Cromwell Road | 16,650,000 | not stated | - | - | London Assembly / TfL |

Walsall is the only scheme with a complete cost breakdown and a stand count. The accepted
tender sum was GBP3,764,889 for 11 stands under the main canopy and 3 under a satellite canopy,
with 3,171 m2 of main canopy and about 3,418 m2 of covered area in total. That gives
GBP1,101.35/m2 and GBP268,921 per stand. The purpose-made steel and glass screens at the stands
were GBP38.16/m2 of covered area, or about GBP9,317 per stand; the rest is roof, concourse,
external works, drainage and preliminaries.

Heckmondwike is the other end of the range: GBP4.97m for 6 stands, a new building with offices,
Changing Places, accessible WC and waiting area, a layover bay, green roof and solar panels. At
GBP828,333 per stand it is a Small scheme with a full building and public realm, not a canopy
over a forecourt. The two points bracket the per-stand rate at GBP269,000-828,000.

The recent total scheme costs (GBP7.4m-23.0m) are useful as upper bounds and for whole-scheme
checks, but without stand counts they cannot produce a per-stand rate. The Dewsbury figure in
particular includes keeping the station operational during construction and a large scope
increase, so it is not a clean new-build cost.

### 6.2 Bus stops, shelters and real-time displays

| Year | Item | Figure | Unit | Source |
|---|---|---|---|---|
| 1910 | Brighton glazed timber tram shelter | 62 | GBP per shelter | Existing KB |
| 1953 | Precast concrete shelter | 60 | GBP per shelter | Existing KB |
| 1955 | Sheringham concrete shelter | 200 | GBP per shelter | Existing KB |
| 1961 | London Transport standard shelter | 150 | GBP per shelter | Existing KB |
| 2024 | Bus shelter, installed range | 8,000-15,000 | GBP per shelter | Wiltshire CC |
| 2025 | Cantilever shelter, commuted sum | 2,611.80 | GBP per shelter | Suffolk CC |
| 2025 | Enclosed shelter, commuted sum | 3,482.40 | GBP per shelter | Suffolk CC |
| 2025 | Solar RTPI | 5,165.56 | GBP per display | Suffolk CC |
| 2025 | Mains RTPI | 6,906.76 | GBP per display | Suffolk CC |

The gap between the Suffolk commuted sums (GBP2,612-3,482) and the Wiltshire installed range
(GBP8,000-15,000) is the difference between an asset replacement value and a full footway
installation with foundations, electrical connection and traffic management. For a new stop, the
Wiltshire range is the relevant one. For an existing stop, the Suffolk rate is the asset value.

The historical shelters are already in the knowledge base and are repeated here as cross-checks
for the `OldBusShelter` object. They show that a simple timber or concrete shelter was a
two-figure sum in the first half of the twentieth century, not a building-scale cost.

### 6.3 Mapping to the bus stop objects

- `StagingPost` and `BusStop`: already priced; the modern bare stop is a pole, flag and
  timetable case. The knowledge base has GBP300-500 for that, and the Suffolk commuted sums
  give GBP158-483 for signs and shelters.
- `OldBusShelter`: GBP62-200 (1902-1955) for a timber or concrete shelter.
- `ModernBusShelter`: GBP2,612-15,000 depending on whether the figure is an asset value or a
  full installation. Use the lower end for a simple cantilever and the upper end for an
  enclosed, lit shelter.
- `LoadingBay1852`, `LoadingBay`, `LoadingBayCargo`: hardstanding plus a small shed; see section
  5. The 1852 object should use the historical hardstanding rates, not the modern ones.
- `OldBusTerminal` and `ModernBusTerminal`: per stand, GBP269,000-828,000, with the lower end
  for a canopy over a forecourt and the upper end for a fully enclosed station with a building.

---

## 7. Street furniture cross-checks

These are not the primary object of the pass, but they are useful for checking that the sign
and signal rates are on the right scale.

| Year | Item | Figure | Unit | Source |
|---|---|---|---|---|
| 2024 | Standard lighting column, including connection | up to 3,700 | GBP per column | Wiltshire CC |
| 2025 | Lighting column under 6 m, commuted sum | 1,758 | GBP per column | Suffolk CC |
| 2025 | Lighting column 8 m, commuted sum | 2,138 | GBP per column | Suffolk CC |
| 2025 | Lighting column 10 m, commuted sum | 2,212 | GBP per column | Suffolk CC |
| 2024 | Bollard, standard range | 400-800 | GBP per bollard | Wiltshire CC |
| 2025 | Metal bollard, commuted sum | 144.32 | GBP per bollard | Suffolk CC |
| 2024 | Pedestrian guard railing | 280-350 | GBP per m | Wiltshire CC |
| 2025 | Safety barrier, commuted sum | 195.73 | GBP per m | Suffolk CC |
| 2024 | HVM bollard | 2,815 | GBP per bollard | TfL FOI |

The lamp column and guard rail figures are consistent across the two councils once the
difference between a tender price and a commuted sum is allowed for. The bollard range is
genuinely wide: a concrete bollard at GBP36.68 and a hostile-vehicle-mitigation bollard at
GBP2,815 are different products with the same name.

---

## 8. Recommended rate table

The table gives the evidence band, not a single point, and names the object class it is
intended for. All figures are nominal and in the year shown. The pricing team should choose
within the band according to the object's era, size and specification.

### 8.1 Traffic lights

| Period | Per junction | Per head | Basis |
|---|---|---|---|
| 1927-1934 | 300-500 | 75-125 (derived) | 1932 London and four-corner figures; low confidence |
| 1935-1954 | 650-850 | 8.50 additional face (1939) | 1939 vehicle-actuated crossroads |
| 1955-1969 | 850-3,100 | no measured series | 1956 crossing range to 1963 crossroads average |
| 1970-1989 | 3,100-25,000 | no measured series | Interpolated; only MOVA/SCOOT equipment costs measured; low confidence |
| 1990-2009 | 25,000-90,000 | no measured series | SCOOT/UTC equipment to 2010 simple T junction; low confidence |
| 2010-2026 | 57,000-150,000 | 526.42 (3-aspect LED, 2017) | Warwickshire, York, Suffolk, BANES |

For a four-arm junction in the modern era, GBP57,000-150,000 is the all-in range. The equipment
alone is about GBP8,300. Do not use four times the head price as a junction cost.

### 8.2 Road signs

| Item | 1935 | 1972 | 1989-2008 | 2017-2026 |
|---|---|---|---|---|
| Small regulatory sign, unlit, new post | 1.13-1.88 | - | 100 (2007 average) | 158-800 |
| Speed-limit repeater | - | - | - | 320 |
| One-way or no-entry, illuminated | - | - | - | 745 |
| Direction sign | - | 170-200 | 185 (plate-over) | 483-1,100 |
| Advance direction sign | - | 200 | - | 483-5,000 |
| Illuminated sign, all works | - | - | - | 1,500-3,000 |
| Motorway roadside sign | - | - | 600 (1984) | over 4,000 (2009 estimate) |
| Motorway gantry, structure and installation | - | - | 77,000-400,000 (1984-1998) | 12,100-130,000 (2021) |
| Motorway gantry, all-in with signs and power | - | - | - | about 1,500,000 (2021) |

### 8.3 Level crossings and rail gates

| Item | Period | Figure | Basis |
|---|---|---|---|
| Manual gate set | any | no measured figure | Gap; price as timber gate and posts, not as an AHB |
| First British AHB | 1961 | 5,000-6,000 | Spath |
| AHB, average | 1969 | 8,600 | Hansard |
| AHB, post-Hixon minimum | 1969 | 13,000 | Hansard |
| AHB | 1984 | 70,000 | Hansard |
| Manually controlled full barrier | 1984 | 120,000 | Hansard |
| MSL user-worked crossing | 2022 | 120,000-150,000 | Rail Engineer |
| Major barrier upgrade | 2019 | 5,500,000 | Carnoustie |

### 8.4 Loading bays and truck stops

| Item | Figure | Basis |
|---|---|---|
| Hardstanding, light/standard | 30-60 GBP/m2 | 2025-2026 carriageway and car park rates |
| Hardstanding, heavy HGV | 80-150 GBP/m2 | 2026 heavy-duty pavement |
| Historical hardstanding | 0.15-0.68 GBP/m2 | 1879-1906 rates |
| Truck stop construction | 29,100-29,857 GBP per space | AECOM 2014 |
| Truck stop including land | 31,020-44,004 GBP per space | AECOM 2014 |
| Truck stop all-in with welfare | 38,372 GBP per space | DfT 2024 programme average |
| Truck park site, all-in | 236-239 GBP/m2 | London Gateway, Southampton |

### 8.5 Bus stations and stops

| Item | Figure | Basis |
|---|---|---|
| Bus station per stand | 269,000-828,000 GBP | Walsall 2001, Heckmondwike 2022 |
| Bus station per m2 | 1,101.35 GBP (2001) | Walsall |
| Bus shelter, asset value | 2,612-3,482 GBP | Suffolk 2025 |
| Bus shelter, installed | 8,000-15,000 GBP | Wiltshire 2024 |
| RTPI | 5,166-6,907 GBP | Suffolk 2025 |

---

## 9. Confidence

**High confidence** (measured contract, statutory answer, or published schedule with a clear
unit):

- 1932, 1939, 1954, 1956 and 1963 traffic signal answers (Hansard).
- 1984 AHB and MCB costs (Hansard).
- 1984 motorway sign and gantry costs (Hansard).
- 2017 Southend component costs.
- 2010 Warwickshire simple T junction.
- 2001 Walsall bus station, with a full quantity-surveyor breakdown.

**Medium confidence** (feasibility estimate, cost guide, or a schedule that is not a tender):

- 2025 Suffolk commuted sums, because they are whole-life asset rates, not prices paid.
- 2024 Wiltshire and Kent sign costs, because they are council guides rather than contracts.
- 2014 AECOM lorry park construction costs, because they are feasibility estimates.
- AECOM's land-inclusive per-space figures.
- The 1972 TRRL direction-sign costs.
- The 1935 sign costs, because they are supply-only.
- The 2021 Highways England gantry costs, because they are structure rates without foundations.
- The 2024 DfT programme average per HGV space, because it mixes parking and welfare works.

**Low confidence** (single weak source, derived, or dated):

- The 1929 GBP100 signal installation.
- The 1932 GBP75 per head.
- The 1970-1990 traffic signal band, which is interpolated.
- The 1990s SCOOT figure, because the guidebook page is undated.
- The 2000 portal gantry structure and equipment costs, because the price year is not stated.
- The 2009 motorway sign figure, which is an estimate.
- Any use of the 1983 Hyde Park Corner figure as an ordinary junction cost.

---

## 10. Dead ends

These were looked for and not found. They are recorded so that they are not searched again
without a new source.

1. **Ministry of Transport annual reports with a line-item road furniture account.** The
   reports are cited in secondary works but no digitised table of traffic signal, sign or
   crossing capital costs was found.
2. **Borough council highways committee minutes with traffic signal costs.** No accessible
   minutes with a per-junction or per-head figure were found.
3. **Institution of Municipal Engineers papers on traffic signal costs.** No paper with a cost
   series was found.
4. **Traffic Engineering and Control cost articles.** The journal is cited but no accessible
   article with a British per-junction series was found.
5. **DfT unit cost series for signs or signals.** No published per-sign or per-junction series
   was found.
6. **A measured manual level-crossing gate set.** No price for timber gates, posts and winding
   gear was found. This is the largest single gap in the pass.
7. **A 1940s-1970s per-head traffic signal price.** Only the 1939 face price and the 2017 LED
   head price were found; there is no continuous series.
8. **A bus station per-stand series.** Only Walsall (2001) and Heckmondwike (2022) give both a
   total and a stand count. The other recent schemes publish totals without stand counts.
9. **A loading-bay-specific hardstanding rate.** No source prices a loading bay as distinct from
   a road, car park or lorry park; the report uses road and parking rates as proxies.
10. **A modern British truck-stop building rate per m2.** No source separates the welfare
    building from the site works; the DfT programme average is the only all-in check.
11. **The 1927 Wolverhampton installation cost.** The council history and the plaque record the
    date and the equipment but not the price.
12. **The 1934 LNER power-operated gates at Walton Street, Hull.** The article describes the
    equipment and the contract but gives no cost.
13. **The 2015 Network Rail AOCL barrier retrofit programme.** 66 crossings were upgraded, but
    no per-crossing cost was published.
14. **The 2024 Cambridge level-crossing upgrades.** The figure of about GBP0.9m per crossing is
    a saving from combining works with re-signalling, not a cost. It is not used.

---

## 11. Sources

Hansard and parliamentary:

- HL Deb 21 Jun 1932 vol 85 cc51-4, London Traffic Lights.
  https://api.parliament.uk/historic-hansard/lords/1932/jun/21/london-traffic-lights
- HC Deb 8 Feb 1932 vol 261 cc499-500, Traffic Signals (Piccadilly).
  https://api.parliament.uk/historic-hansard/commons/1932/feb/08/traffic-signals-piccadilly
- HC Deb 3 Apr 1935 vol 300 cc350-1, Traffic Signs (Cost).
  https://api.parliament.uk/historic-hansard/commons/1935/apr/03/traffic-signs-cost
- HC Deb 6 Mar 1935 vol 298 cc1933-5, Built-up Areas (Speed Limit).
  https://api.parliament.uk/historic-hansard/commons/1935/mar/06/built-up-areas-speed-limit
- HC Deb 26 Jul 1939 vol 350 cc1485-6W, Traffic Signals.
  https://api.parliament.uk/historic-hansard/written-answers/1939/jul/26/traffic-signals
- HC Deb 26 Jul 1939 vol 350 cc1464-5, Traffic-Light Signals.
  https://api.parliament.uk/historic-hansard/commons/1939/jul/26/traffic-light-signals
- HC Deb 18 May 1954 vol 527 cc1900-2, Controlled Pedestrian Crossings (Cost).
  https://api.parliament.uk/historic-hansard/commons/1954/may/18/controlled-pedestrian-crossings-cost
- HC Deb 19 Dec 1956 vol 562 c191W, Traffic Lights (Installation and Upkeep Costs).
  https://api.parliament.uk/historic-hansard/written-answers/1956/dec/19/traffic-lights-installation-and-upkeep
- HC Deb 18 Dec 1963 vol 686 c222W, Traffic Signals (Cost).
  https://api.parliament.uk/historic-hansard/written-answers/1963/dec/18/traffic-signals-cost
- HC Deb 2 Dec 1969 vol 792 c241W, Half-barrier Level Crossings.
  https://api.parliament.uk/historic-hansard/written-answers/1969/dec/02/half-barrier-level-crossings
- HC Deb 28 Feb 1929 vol 225 c2183, Railway Level Crossings.
  https://api.parliament.uk/historic-hansard/commons/1929/feb/28/railway-level-crossings
- HL Deb 11 Apr 1983 vol 441 cc7-10, Hyde Park Corner: Traffic Lights.
  https://api.parliament.uk/historic-hansard/lords/1983/apr/11/hyde-park-corner-traffic-lights
- HC Deb 26 Mar 1984 vol 57, Railway Level Crossings.
  https://hansard.parliament.uk/Commons/1984-03-26/debates/f43d45f1-6f75-444e-9302-9c846d31a008/RailwayLevelCrossings
- HC Deb 18 Dec 1984 vol 70 cc131-2W, Motorways (Signs).
  https://api.parliament.uk/historic-hansard/written-answers/1984/dec/18/motorways-signs

Technical and academic:

- Institution of Civil Engineers, Minutes of the Proceedings, Street Carriageway Pavements,
  1879. https://doi.org/10.1680/imotp.1879.22167
- Shoreditch Medical Officer of Health Report, 1897, comparison of paving costs.
  https://www.wellcomelibrary.org/moh/report/b20056874/174
- TRRL Report LR 475, Rutley, An Investigation into Bilingual (Welsh/English) Traffic Signs,
  1972. https://www.trl.co.uk/uploads/trl/documents/LR475.pdf
- TRL Traffic Advisory Leaflet 3/97, The MOVA signal control system, March 1997.
  https://tsrgd.co.uk/pdf/tal/1997/tal-3-97.pdf
- Hamilton, Waterson, Cherrett, Robinson and Snell, The Evolution of Urban Traffic Control,
  Transportation Planning and Technology 36(1), 2013.
  https://scispace.com/pdf/the-evolution-of-urban-traffic-control-changing-policy-and-3uv4vcxn36.pdf
- Saffer and Bull, Early and Late 20th Century Developments in Traffic Control, JCT Traffic
  Signal Symposium, September 2025.
  https://jctsymposium.co.uk/wp-content/uploads/2025/12/Early-and-Late-20th-century-developments-in-Traffic-Control.pdf
- Dent and Marinov, Introducing Automated Obstacle Detection to British Level Crossings,
  RailExchange 2017. https://publications.aston.ac.uk/id/eprint/38305/1/Introducing_automated_obstacle.pdf
- Ministry of Transport and Civil Aviation, Report on Level Crossing Protection, 1957.
  https://www.railwaysarchive.co.uk/documents/MoT_LevelCrossing1957.pdf
- UK Metric Association, Metric Signs Ahead, 2006, 2009 update.
  https://ukma.org.uk/wp-content/uploads/2017/07/msa.pdf

Council, transport authority and project documents:

- Southend-on-Sea BC, Asset Management Support: Traffic Signals Life Cycle Plan, 30 June 2017.
  https://www.southend.gov.uk/downloads/file/5374/appendix-c-southend-asset-management-support---traffic-signals
- City of York Council, TSAR Traffic Signal Refurbishment, 3 November 2020.
  https://democracy.york.gov.uk/documents/s143212/Report-Signal_Renewal-Wigginton%20Road%20and%20Crichton%20Avenue.pdf
- Warwickshire CC, ITS Strategy: Appendix B.
  https://api.warwickshire.gov.uk/documents/WCCC-770-190
- Suffolk CC, Commuted Sum Rates for Development Management 2025/2026.
  https://www.suffolk.gov.uk/asset-library/commuted-sums-2025-2026.pdf
- Bath and North East Somerset Council, Highway Commuted Sums 2021-22.
  https://democracy.bathnes.gov.uk/documents/s65291/Appendix%202%20Commuted%20Sums.pdf
- West Sussex CC, Traffic Signals Halogen Replacement Programme, July 2023.
  https://westsussex.moderngov.co.uk/documents/s40129/Traffic%20Signals%20Halogen%20Replacement%20Programme%20-%20report.pdf
- Leicestershire CC, Melton Mowbray Distributor Road, Appendix C detailed cost breakdown,
  October 2017.
  https://www.leicestershire.gov.uk/sites/default/files/field/pdf/2020/10/21/Appendix-C-detailed-cost-breakdown.pdf
- Wiltshire Council, Costs of Highway Works, April 2024.
  https://www.wiltshire.gov.uk/article/1281/Costs-of-highway-works
- Kent CC, Highway Improvement Plan Information Pack 2024-25.
  https://ashford.moderngov.co.uk/documents/s28739/Highway+Information+Pack+2024-25.pdf
- Buckinghamshire CC, Traffic Calming in Buckinghamshire, July 2020.
  https://buckinghamshire.moderngov.co.uk/documents/s12321/App%20A%20TrafficcalmingGuide_2020.pdf
- Faversham Town Council, Guide Price for Signs, 2020.
  https://www.favershamtowncouncil.gov.uk/wp-content/uploads/2020/10/Guide-Price-for-Signs.pdf
- Surrey CC, Highway Works Cost Schedule, Annex 2.
  https://mycouncil.surreycc.gov.uk/documents/s51054/Annex%202%20Highway%20Works%20Cost%20Schedule.pdf
- Highways England, Gantries: Strategic Procurement Strategy, May 2021.
  https://www.supplychainschool.co.uk/wp-content/uploads/2021/04/NH-Gantries-Strategy-Final.pdf
- National Highways, MS4 accessible gantry standardisation.
  https://nationalhighways.co.uk/work-with-us/suppliers/becoming-a-supplier/lean-supplier-support/lean-efficiencies-and-case-studies/ms4-accessible-gantry-standardisation/
- AECOM for Kent CC, Kent Lorry Parks Feasibility Study - Phase 2 Report, 17 March 2014.
  https://democracy.kent.gov.uk/documents/s49182/Kent%20Lorry%20Parks%20Feasbility%20Study%20Phase%202%20-%20Appendix%202.pdf
- Earlcoate, Pre-Gate Truck Park Southampton Docks.
  https://earlcoate.co.uk/wp-content/uploads/2025/07/Pre-gate_Truck_Park.pdf
- Find a Tender, C2541 PIF Truck Park, London Gateway Port, 11 May 2021.
  https://www.find-tender.service.gov.uk/Notice/010335-2021/PDF
- Department for Transport, Better kips for better trips, 4 March 2024.
  https://www.gov.uk/government/news/better-kips-for-better-trips-16-million-boost-to-transform-truckstops-for-lorry-drivers
- Architects' Journal, The waiting game (Walsall bus station), 31 May 2001.
  https://www.architectsjournal.co.uk/archive/the-waiting-game
- West Yorkshire Combined Authority, Dewsbury Bus Station Full Business Case, 31 October 2024.
  https://westyorkshire.moderngov.co.uk/documents/s39065/IP5%20Transforming%20Cities%20Fund%20-%20Dewsbury%20Bus%20Station.pdf
- Kirklees Council, Update on Bus Station Projects, 18 October 2022.
  https://democracy.kirklees.gov.uk/documents/s48561/Update%20on%20Bus%20Station%20Projects.pdf
- West Yorkshire Combined Authority, Halifax Bus Station Business Case Summary.
  https://westyorkshire.moderngov.co.uk/documents/s21695/Item%209%20-%20Appendix%206%20-%20Halifax%20Bus%20Station%20-%20Business%20Case%20Summary.pdf
- West Yorkshire Combined Authority, Huddersfield Bus Station Business Case Summary.
  https://westyorkshire.moderngov.co.uk/documents/s28362/Item%209%20-%20Appendix%207%20-%20Huddersfield%20Bus%20Station%20-%20Business%20Case%20Summary.pdf
- London Assembly, Cromwell Bus Station (2), answer 2024/4058, 23 December 2024.
  https://www.london.gov.uk/who-we-are/what-london-assembly-does/questions-mayor/find-an-answer/cromwell-bus-station-2
- Transport for London, FOI-2790-2425, Kingston Bus station, 17 December 2024.
  https://tfl.gov.uk/corporate/transparency/freedom-of-information/foi-request-detail?referenceId=FOI-2790-2425
- Crawley BC, Town Centre Bus Station Business Case, 6 April 2022.
  https://crawley.gov.uk/sites/default/files/2022-04/Bus%20Station%20Business%20Case.pdf
- Transport for London, FOI-3866-2324, HMV bollards Old Street Roundabout, 12 February 2024.
  https://tfl.gov.uk/corporate/transparency/freedom-of-information/foi-request-detail?referenceId=FOI-3866-2324

Trade and project press:

- New Civil Engineer, A new approach, 21 May 1998.
  https://www.newcivilengineer.com/archive/a-new-approach-21-05-1998/
- Contract Journal, A question of motorway safety, 19 April 2000.
  https://trid.trb.org/view/657148
- Rail Engineer, Innovation in level crossings, 28 June 2022.
  https://www.railengineer.co.uk/innovation-in-level-crossings/
- Network Rail Media Centre, Positive signals for Carnoustie level crossing upgrade, 20 March
  2019. https://www.networkrailmediacentre.co.uk/news/positive-signals-for-carnoustie-level-crossing-upgrade
- Network Rail Media Centre, Programme to install barriers at 'open' level crossings complete,
  14 December 2015. https://www.networkrailmediacentre.co.uk/news/programme-to-install-barriers-at-open-level-crossings-complete
- Derby Signalling History, Spath AHB Level Crossing. http://www.derby-signalling.org.uk/Spath.htm
- Welsh Highland Heritage, Croesor Crossing.
  https://www.welshhighlandheritage.co.uk/wp-content/uploads/2023/11/CHRONICLES-website-edition-latest-version.pdf
- Building.co.uk, indicative rates for paving and landscaping.
  https://www.building.co.uk/download?ac=1539685
- Highways Plus, Commercial Driveways. https://www.highwaysplus.co.uk/commercial-driveways/
- COMREW, Roads and Car Parks. http://www.comrew.com/roads_car_parks.asp
- RLB, Riders Digest 2023. https://www.rlb.com/wp-content/uploads/sites/6/2023/07/Riders-Digest-2023-Final.pdf
- JRG Civils, Cost of Groundworks for New Builds: 2026 Price Guide, 14 September 2026.
  https://jrgcivils.co.uk/2026/09/14/cost-of-groundworks-for-new-builds/

---

## 12. What this pass does not do

- It does not choose a single price for any pakset object. The bands in section 8 are the
  evidence; the choice within a band is a balancing decision.
- It does not deflate to 1900 prices. The pricing team must apply the relevant index series.
- It does not price maintenance, because the CSV `kind` is `capital`. Maintenance figures found
  in the sources are in the report text only (for example GBP60 a year per London junction in
  1932, GBP70-85 in 1939, GBP50-120 in 1956, GBP2,850 in 2010, GBP450 per HGV space a year in
  2014).
- It does not cover traffic signal controllers before 1939, vehicle detectors before 1989, or
  bus station buildings before 2001 in any detail.
- It does not resolve the manual level-crossing gate price. That remains the first item for a
  second pass, with a search of railway company gate accounts, Railway Gazette contract notices
  and heritage railway restoration accounts.
