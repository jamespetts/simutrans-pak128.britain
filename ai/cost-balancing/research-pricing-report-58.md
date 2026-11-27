---
status: draft
verified: New ex-15 @ 81ffb5911 (working tree), 2026-11-27; simutrans-extended-sources ex-15 @ ebf26cfb9b
date: 2026-11-27
---
# Research pass 58 - Road, runway and taxiway capital and maintenance

**Covers**: the formation, pavement and upkeep cost of the road family and the airfield
pavement family, the per-waytype `forge_cost_road` and `forge_cost_air` values, the way-only
target for every row of `Ways - road` and `Ways - air` in `New/cost-balancing-capital.xlsx`, and
the routine-maintenance band for both families. Read-only research: no workbook, `.dat`, config,
script, knowledge-base or git file was changed.

**Companions**: [infrastructure-cost-evidence](../infrastructure-cost-evidence.md) §3 and §9 (the
measured figures), [infrastructure-cost-synthesis](../infrastructure-cost-synthesis.md) §3.2, §3.7
and §5 (the earlier recommendations), [way-cost-audit-2026-11-26](way-cost-audit-2026-11-26.md)
(the audit that found the negative way-only values), [research-pricing-report-3](research-pricing-report-3.md)
§4 and [research-pricing-report-5](research-pricing-report-5.md) §4-§5 (formation and road costs),
and [conversion-chains](../conversion-chains.md) (the unit arithmetic).

**Price basis.** GBP1900 means pounds of 1900. Every other figure is nominal of its stated year.
Raw pakset units are not money: a `.dat` capital value of 1 is GBP1900 0.00396311 per kilometre,
and a `.dat` maintenance value of 1 is GBP1900 0.09511464 per kilometre-year (`0.00792622` per
kilometre-month). The deflator is the `infrastructure` series in `New/config/prices.tab`, 1900 =
100; the values used here are 1819 = 141, 1825 = 132, 1877 = 106, 1880 = 102, 1911 = 106, 1938 =
183, 1960 = 534, 1982 = 2993, 2011 = 6097, 2023 = 8670 and 2024 = 8850. Conversion: GBP1900 per km
× 252.3 = raw units.

**Evidence classes.** MEASURED = a contract, account, statutory return or published unit rate.
STATED = a figure an author states without showing its build-up. DERIVED = arithmetic on measured
figures, shown here. ESTIMATE = a judgement with no measurement behind it. UNAVAILABLE = the
figure could not be found.

## Terms

- **Formation** has three different meanings in the sources, and conflating them is the main
  source of error in this domain. **Bulk earthworks** are the cuttings, embankments and mass
  cut-and-fill that create the alignment. **Bed preparation** is what is done to the ground once
  the alignment exists: clearing, drainage, grading to level and crossfall, soiling and fencing.
  The **pavement box** is the excavation to formation level plus the capping or sub-base placed in
  it. Only bed preparation and the pavement box belong to the engine's forge; bulk earthworks are
  made with the raise/lower land tool (user direction, 2026-11-22).
- **Forge**: the engine setting `forge_cost_<waytype>` in `New/config/simuconf.tab`, a per-tile
  charge added once when a new plain way is built on virgin ground. It is not charged on an
  upgrade, and it is charged at 50 per cent for a parallel way.
- **Way-only value**: the audited total for an object minus the forge. It is the number the `.dat`
  `cost=` field needs so that `cost + forge` equals the total.
- **Pavement**: the layers above the formation — sub-base, base, binder and surface course. For a
  road this is what the traffic runs on; for a runway it is the slab or asphalt construction.
- **Carriageway width**: the width used to convert a rate per square metre to a rate per
  kilometre. Unless stated, 7 m for a road, 45 m for a concrete runway, 30.5 m for an asphalt
  runway, 30 m for a grass runway, and 23 m for a taxiway (the widths already used in the
  workbook's class-basis notes).

## Recommendations in brief

| Item | Present | Recommended | Basis |
|---|---|---|---|
| `forge_cost_road` | 315,000 raw = GBP1,248.38/km | **20,000 raw = GBP79.26/km** | Bed preparation of an unsurfaced track: 79 per cent of the bridleway's whole construction and 72 per cent of Telford's measured bed-preparation rate for a 32 ft road |
| `forge_cost_air` | 1,875,000 raw = GBP7,430.83/km | **110,000 raw = GBP435.94/km** | 76 per cent of the grass taxiway's whole construction; the formation share of a grass strip, from the Valuation Office Agency grass specification |
| Road routine maintenance | one value, GBP21.57/km-year, on all 22 rows | **GBP2-310/km-year by class** | 1880 rates, 1911 tarred-slag rate, 1982 motorway age ladder, modern unit rates |
| Air routine maintenance | GBP6.67/km-year on all 8 rows | **GBP7-246/km-year by class**, concrete at half the asphalt rate | 0.50 per cent of capital for asphalt, 0.25 for concrete, 1.2-1.3 for grass; section 11 |

The two forge values are per waytype, not per object, and both are floors: every object above the
cheapest carries its own excess formation inside its way object. Section 4.4 states the
consequences.

---

## 1. Road formation and levelling by era and class

### 1.1 The one measured decomposition: Telford's Holyhead Road estimate, 1825

Thomas Telford's own estimate for part of the Holyhead Road near Coventry, printed in his
*Treatise on Roads* (1838), itemises a new road of 1,882 lineal yards (1.721 km) on a 32 ft
formation. It is the only pre-modern road account found that separates the bed from the
pavement. [LITERATURE: Telford, *A Treatise on Roads*, 1838, "Management of Road Works",
estimate for the Coventry division, e-rara doi 10.3931/e-rara-66372]

| Item | Nominal 1825 | Per km | Per km at 1900 |
|---|---:|---:|---:|
| Remove 26,790 cu yd of earth at 9d | £1,004 12s 6d | £583.8 | £442.3 |
| Extra embankment, 5,200 cu yd at 6d | £130 0s 0d | £75.5 | £57.2 |
| Road-making, 1,882 yd at 15s 6d | £1,458 11s 0d | £847.6 | £642.1 |
| Fencing, 1,882 yd at 5s | £470 2s 0d | £273.2 | £206.9 |
| Drains | £50 0s 0d | £29.1 | £22.0 |
| Forming | £100 0s 0d | £58.1 | £44.0 |
| Sodding | £100 0s 0d | £58.1 | £44.0 |
| Depots | £48 0s 0d | £27.9 | £21.1 |
| Bridge | £670 0s 0d | £389.3 | £294.9 |
| Side roads, gates, extra cartage | £101 8s | £58.9 | £44.6 |
| **Total** | **£4,132 14s** | **£2,401** | **£1,819** |

Three results follow.

1. **The formation is 56.6 per cent of formation plus pavement.** Excluding the bridge, side
   roads and cartage, the formation items total £1,105.7/km nominal (£838/km at 1900) against
   road-making at £847.6/km nominal (£642/km at 1900). This is the single most useful ratio in the
   domain, and it recurs in the modern evidence (§1.2).
2. **Bed preparation alone is £110/km at 1900.** Forming, drains and sodding, excluding bulk
   earthworks and fencing, come to £145.3/km nominal, or £110.1/km at 1900, for a 32 ft
   formation. That is the number to scale for a narrower way.
3. **The earthworks volume is the one used as the "light line" check elsewhere.** 26,790 cubic
   yards over 1.07 miles is 25,000 cubic yards per mile, the same volume that
   `research-pricing-report-3.md` §4.2 uses to derive £583/km at 9d. The two agree exactly, which
   confirms that the report's £583/km is the earthworks component and not a whole formation.

J. Provis, Telford's surveyor, gave the House of Commons committee in 1836 a unit rate for the
pavement: "The expense of paving the middle sixteen feet in the usual way, with six inches of
broken stone on it, will be, per yard lineal, 3s. 0½d." At 16 ft width that is 0.57s per square
yard, or about £0.034 per square metre in 1836 money. [LITERATURE: Telford, *A Treatise on
Roads*, 1838, appendix, examination of John Provis]

### 1.2 The modern decompositions

Four modern British scheme estimates separate the formation from the pavement, and all four
give a formation share far above the 1900 road.

| Scheme | Year | Formation series | Pavement series | Formation share |
|---|---|---|---:|---:|
| Melton Mowbray distributor road | 2017 | Series 600 earthworks £6,283,342 | Series 700 pavements £5,587,991 | 52.9% |
| M2, National Highways scheme (Dadswell priced) | 2023-25 | Series 600 £8,547,181 | Series 700 £4,447,452 | 65.8% |
| Kent CC southern relief road | 2023-25 | Series 600 £36,780,446 | Series 700 £13,995,198 | 72.4% |
| Kent CC northern relief road | 2023-25 | Series 600 £7,905,123 | Series 700 £3,450,434 | 69.6% |

Sources: Leicestershire CC, *Melton Mowbray Distributor Road, Appendix C detailed cost breakdown*,
October 2017; HWA, *CD37.14.2A Appendix 2 side-by-side comparison* (National Highways M2 and Kent
CC relief roads). [LITERATURE: both published scheme cost plans]

These are new-alignment roads, so Series 600 includes the bulk earthworks for the whole corridor,
including verges, embankments, ponds and disposal of unsuitable material — work that the pakset
does with the raise/lower land tool. The share is therefore an upper bound for the forge, not the
forge itself.

The pavement-box share is much smaller and is measured at scheme level:

- **Wakefield, a Section 38 residential/distributor road, 2020s prices**: excavate carriageway to
  formation level and cart to spoil £13.80/m³, 593 m³ over 690 m² of carriageway, a box depth of
  0.86 m; 450 mm 6F2 capping £54.14/m³; 150 mm Type 1 sub-base £67.22/m³; 80 mm AC32 base plus
  60 mm AC20 binder £47.66/m²; 30 mm AC10 surface £18.50/m². Box excavation £11.86/m² plus capping
  £24.36/m² = **£36.22/m² of formation**, against £100.65/m² of formation plus pavement, a 36.0
  per cent share. Over a 7 m carriageway that is **£2,924/km at 1900**, and £1,525 per lane-km at a
  3.65 m lane. [LITERATURE: Wakefield MDC planning application appendix 3i, road cost schedule]
- **M20 junction 10a, 4Q2025 prices**: 150 mm Type 1 sub-base £100/m³, 250 mm HDM base £75/m²,
  60 mm HRA binder £28/m², 40 mm HRA PMB surface £38/m²; the whole Series 600 for 353 m² of
  formation was £27,462, or £77.8/m², and the pavement layers £156/m². [LITERATURE: Kent CC /
  National Highways, *SJP/BC/KCC243/25111901C1 Cost Plan Nr. 1*, 2025]
- **Spon's Civil Engineering and Highways Works Price Book, as tabulated by AECOM (2021)**:
  Type 1 sub-base £39.89-43.88/m³ by thickness; 6F capping £45.97/m³; AC32 base £22.20-36.73/m²;
  AC20 binder £14.48-21.28/m²; TSCS surface £10.22-15.73/m²; HRA binder £17.82-25.88/m²; RCC
  £31.03/m²; CRCP concrete 160-250 mm £97.32-141.02/m². [LITERATURE: AECOM, *Pavement Whole Life
  Cost*, MHA+ concrete roads session 3, 30 November 2021]

So the modern road has **two** formation figures that must not be mixed: the bed preparation and
pavement box, about £2,900/km per 7 m carriageway at 1900, and the bulk earthworks of a new
alignment, which is several times that and belongs to the land tool.

### 1.3 Formation by era and class

| Era and class | Bed preparation, GBP1900/km | Bulk earthworks included? | Class | Basis |
|---|---:|---|---|---|
| Track, bridleway, unsurfaced way, 3-4 m | 45-80 | No | DERIVED | Telford forming, drains and sodding (£110/km at 32 ft) scaled to a 3-4 m width, with drainage held near-constant and a share of fencing added |
| Turnpike and MacAdam rural road, 1800-1900 | 80-110 | No | MEASURED (1825) | Telford forming, drains and sodding, £110/km at 1900 |
| Turnpike and MacAdam new alignment, 1800-1900 | 610-840 | Yes | MEASURED (1825) | Telford earthworks plus bed preparation, £609/km at 1900; £838/km with fencing |
| Victorian urban street, 1850-1914 | 2,000-3,000 | No (sewers excluded) | DERIVED | Six-inch concrete bed at 5s 2½d a square yard is £2,057/km over 7 m at 1900; add box excavation and kerbs |
| Interwar trunk road, 1918-1939 | 300-1,200 | Partly | ESTIMATE | No measured split found; bracketed by the 1825 hand-built and the 1960s mechanised rates |
| Post-war and motorway, 1958-2000 | 2,000-8,000 | No | DERIVED | Wakefield box excavation and capping, £2,924/km over 7 m at 1900; the pakset motorway lane at 3.65 m is £1,525 per lane-km |
| Paved runway, 45 m | 14,600 | Yes (earthworks and subgrade) | MEASURED (1960) | Gatwick 1960 build-up: earthworks and subgrade 37.7 per cent of £4.60/m² |

The Victorian urban figure is the one that most needs stating, because it is 20-30 times the
rural figure of the same date. A granite-sett street was laid on a 6-inch Portland cement concrete
foundation. The New Westminster (British Columbia) contractor's schedule prices that foundation
separately at 5s 2½d a square yard including profit, which is £2,057/km over a 7 m carriageway at
1900. [LITERATURE: *Estimating and Costing of Architectural and Engineering Works*, prices of
1912-13, English equivalent column] Add the excavation of the road box, the kerbs and the gullies
and the urban bed is £2,000-3,000/km.

### 1.4 The transition between the eras

The 30-70 fold rise in formation cost between 1825 and 1960 is not inflation. It is three
physical changes: the capping layer (250-450 mm of imported selected fill, which no nineteenth
century road had), the regulatory cost of disposing of unsuitable material off site, and the
thicker pavement box that a 40-tonne axle load requires. Any single forge value for the road
family therefore has to choose which end of that transition it represents, which is the point §4
addresses.

---

## 2. Road construction by layer and class

### 2.1 Early roads, 1800-1860

| Item | Year | Figure | Scope | Source |
|---|---|---|---|---|
| Turnpike construction, network average | 1819 | £174/km (£280/mile) | Whole construction, existing alignment | evidence §3 |
| New Telford or McAdam road, Buxton-Manchester | 1825 | £746/km (£1,200/mile) | Whole construction, new alignment | evidence §3 |
| New Telford road, Bangor section | 1825 | £1,491/km (£2,400/mile) | Whole construction, new alignment | evidence §3 |
| Telford, Coventry division | 1825 | £2,401/km nominal, £1,819/km at 1900 | Whole construction including a bridge | Telford 1838 |
| Telford pavement (16 ft, 6 in set stone plus 6 in broken stone) | 1836 | 3s 0½d per lineal yard = £0.034/m² | Pavement only | Provis, in Telford 1838 |
| McAdam re-stoning | 1823 | £88/mile per operation = £53.09/km at 1900 | Surface renewal, not construction | evidence §3 |

The 1819 network average is an average over improvements to existing roads, so it contains almost
no formation; it is not comparable with a new-made road. The 1820s new roads at £746-1,491/km are
the comparable figures, and Telford's itemisation shows how they divide.

### 2.2 Victorian urban streets, 1860-1914

| Item | Year | Figure at 1900 | Scope | Source |
|---|---|---|---|---|
| Granite setts on 6 in concrete base, 7 m | 1912 | £7,799/km | Pavement and bed, carriageway only | New Westminster schedule |
| Granite setts alone, 7 m | 1912 | £5,743/km | Setts only | ibid. |
| Concrete base alone, 7 m | 1912 | £2,057/km | Bed only | ibid. |
| Macadam, 7 m | 1912 | £823/km | Surface only | ibid. |
| Complete street tramway track | 1877 | £2,638/km at 1900 for a single track | Rails, setts and concrete over about 2.75 m | report 13 §4.3-4.4 |
| Rails, bearers and fastenings within the above | 1877 | £1,172-1,348/km at 1900 | Metal only | report 13 §4.3 |

Two checks, one British and one colonial, bracket the answer. The 1877 Institution of Civil Engineers
discussion gives a complete street tramway at £4,500 a mile, of which "concrete, paving and rails
were more than three quarters"; removing the rails leaves £1,337-1,733/km at 1900 of concrete and
paving over the paved width, which is £3,400-4,400/km if scaled to a 7 m carriageway. The New
Westminster contractor's schedule prices granite setts on a 6-inch concrete base, in place, at
£7,799/km over 7 m at 1900, of which the setts alone are £5,743 and the base £2,057. The Canadian
figure is the higher, probably because it includes import duty and a small-quantity premium.

**A cobbled carriageway is therefore £3,400-8,000/km at 1900. The working band is £5,000-7,000/km,
midpoint £6,000, and that is the figure used in section 5. The present row's £123/km is 28-65 times
too low.** The ratio to macadam is 4-9:1, and 8.7:1 on the New Westminster prices alone.

The macadam rate is also an independent check on the pakset's own MacAdam row: 2s 1d a square
yard over 7 m gives £823/km at 1900, against the workbook's £833/km, an agreement within 1.2 per
cent.

### 2.3 Tarred surfaces, 1906-1939

| Item | Year | Figure | Scope | Source |
|---|---|---|---|---|
| Tarmac | 1906 | 2s a square yard; £1,760/mile for a 10-yard road = £1,094/km nominal | Surface only | evidence §3 |
| Tarred slag | 1911 | 3s 10d to 4s a square yard = £1,605-1,674/km nominal over 7 m | Surface only | evidence §3 |
| New road on a new alignment | 1938 | £77,600/mile = £26,349/km at 1900 | Whole construction | HL Deb 23 November 1938, County Surveyors' Association |
| Modernising an existing road to 120 ft dual carriageway | 1938 | £221,600/mile = £75,274/km at 1900 | Whole construction | ibid. |
| Motorway | 1938 | about £60,000/mile = £20,373/km at 1900 | Whole construction | ibid. |

The 1938 comparison is the only measured statement in the corpus about the relative cost of
upgrading against building new: modernisation is 2.9 times a new road on a new alignment, and a
motorway is the cheapest of the three because it is built where land is cheap and by machine. That
ordering supports the engine's rule that the forge is not charged on an upgrade.

### 2.4 Post-war roads and motorways, 1958-2011

| Item | Year | Figure | Scope | Source |
|---|---|---|---|---|
| Motorway construction | 1958 | £350,000/mile with land at £3,400/mile | Whole construction | HL Deb 1958 |
| Lancaster bypass | 1958 | £364,000/mile | Whole construction | ibid. |
| Stevenage bypass | 1961 | £251,000/mile, land excluded | Whole construction | HC Deb 1961 |
| Doncaster bypass | 1961 | £369,000/mile, land excluded | Whole construction | ibid. |
| Rural dual two-lane, contracts let 1968 | 1969 | £229,000-1,048,000/mile | Whole construction | HC Deb 1969 |
| Rural D3M | 1978-1980 | £2.49m-3.33m/mile at constant prices | Whole construction | HC Deb 1978, 1980 |
| Motorway, way only, rural D3M | 2005 | £1.2-1.5m per lane-km | Pavement and formation per lane | evidence §3 |
| Motorway, delivered | 2011 | £17,045 per yard = £18.6m/km | Whole carriageway, delivered, all costs | forum thread 6521 |

The 2011 delivered figure is not a pavement rate and cannot be compared with the 2005 per-lane
figure: at a 3-lane, 11 m carriageway it is £1,691/m² of finished road at 2011 prices, or £27.72/m²
at 1900, which includes land, structures, drainage and the whole corridor. The 2005 figure is the
one that matches the pakset's per-lane row.

### 2.5 Modern layer costs

| Layer | Rate | Year | Per m² at 1900 | Source |
|---|---|---|---:|---|
| Capping, 6F2, 450 mm | £54.14/m³ | 2020s | £0.281 | Wakefield |
| Capping, 6F, 250 mm | £45.97/m³ | 2021 | £0.155 | Spon's via AECOM |
| Type 1 sub-base, 150 mm | £67.22/m³ | 2020s | £0.116 | Wakefield |
| Type 1 sub-base, 150 mm | £42.55/m³ | 2021 | £0.086 | Spon's via AECOM |
| Type 1 sub-base, 350 mm | £42.55/m³ | 2021 | £0.201 | ibid. |
| Asphalt base AC32, 150 mm | £29.46/m² | 2021 | £0.398 | ibid. |
| Asphalt base AC32, 200 mm | £36.73/m² | 2021 | £0.496 | ibid. |
| HRA binder, 60 mm | £17.82/m² | 2021 | £0.241 | ibid. |
| HRA binder, 80 mm | £25.88/m² | 2021 | £0.349 | ibid. |
| Asphalt binder AC20, 50 mm | £14.48/m² | 2021 | £0.195 | ibid. |
| Asphalt binder AC20, 100 mm | £21.28/m² | 2021 | £0.287 | ibid. |
| Surface course TSCS, 40 mm | £12.98/m² | 2021 | £0.175 | ibid. |
| Surface course TSCS, 40 mm | £15.73/m² | 2021 | £0.212 | ibid. |
| HRA surface, 40 mm | £38.00/m² | 2025 | £0.419 | M20 J10a |
| RCC base, 200 mm | £31.03/m² | 2021 | £0.419 | ibid. |
| CRCP concrete, 200 mm | £115.74/m² | 2021 | £1.562 | ibid. |
| CRCP concrete, 250 mm | £141.02/m² | 2021 | £1.903 | ibid. |

The per-square-metre figures at 1900 look small only because the conversion is a division by 60-90;
over a 7 m carriageway a modern full-depth flexible pavement of £100/m² (2021 prices) is
£9,448/km at 1900, and the pakset's £15,844/km for a hot-rolled-asphalt road is of that order.

The asphalt-layer range in `infrastructure-cost-evidence.md` §3, £32-56/m² for 130-280 mm
(2017-21), is consistent with these layer sums: 200 mm of AC32 base at £36.73 plus 80 mm of HRA
binder at £25.88 plus 40 mm of surface at £12.98 is £75.59/m², which is £0.45-0.79/m² at 1900 on
the band and about £1.02/m² on the layer sum, the difference being the greater thickness. The
evidence band is for the asphalt layers alone, not for the whole pavement.

### 2.6 What each of the three headline rates includes

| Rate | Year | Includes | Excludes | Per km at 7 m |
|---|---|---|---|---|
| HS2 cost model, rural road, £138/m² | 2011 | Site clearance, earthworks, drainage, pavement and lighting for the road itself | Land, design, contractor costs, testing, commissioning, client costs, risk and optimism bias; station, tunnel and structure earthworks are separate line items | £966,000 nominal = £15,844 at 1900 |
| HS2 cost model, major road, £207/m² | 2011 | As above | As above | £1,449,000 nominal = £23,766 at 1900 |
| HS2 cost model, urban road, £230/m² | 2011 | As above | As above | £1,610,000 nominal = £26,406 at 1900 |
| Tarmac, 2s a square yard | 1906 | The tar-bound wearing surface only | The bed, the foundation and any stone base | £1,760/mile = £1,094/km nominal over a 10-yard road |
| Telford or McAdam new road, £1,200-2,400/mile | 1820s | The whole new road: formation, drainage, fencing and pavement | Land, bridges and, at Buxton, heavy earthworks | £746-1,491 nominal = £565-1,129 at 1900 |

The three HS2 rates are the source of the workbook's £15,844, £23,766 and £26,406 class figures:
each is the square-metre rate times 7 m times 1,000, deflated from 2011. They are whole-construction
rates for a new road, so they already contain the formation and must not have a forge added on top
when used as a total; the way-only value is the total less the forge, as section 5 does. The 1906
tarmac rate is at the opposite extreme: it is a surface treatment only, so a row built on it alone
would omit the entire bed. The 1820s new-road rates are whole construction and include the bed.

---

## 3. Road maintenance by class and era

### 3.1 The distinction the engine requires

The engine charges `weg_t::renew()` separately when an object's wear runs out. The `.dat`
`maintenance=` field must therefore carry **routine upkeep only**: patching, edge repair, drainage,
sweeping, verge and winter work. Resurfacing, re-stoning, overlay and reconstruction are renewal and
must be stripped out. Almost every historical road figure is a combined total, because parish and
county surveyors booked resurfacing to revenue.

### 3.2 Measured rates

| Item | Year | Nominal | At 1900 | Composition | Source |
|---|---|---|---:|---|---|
| Turnpike routine repair contract | 1806-15 | £10-12/mile-year | £4.54-5.44/km-year | Routine only (a repair contract) | evidence §3 |
| Turnpike maintenance | 1819 | about £50/mile-year | £22.03/km-year | Not stated | evidence §3 |
| McAdam re-stoning, per operation | 1823 | £88/mile | £53.09/km per operation | Renewal | evidence §3 |
| Main-road upkeep including re-stoning | 1880 | £35 11s/mile-year | £21.66/km-year | Routine plus re-stoning | evidence §3 |
| Minor-road upkeep | 1880 | £12 9s/mile-year | £7.58/km-year | Routine plus some re-stoning | evidence §3 |
| Tarred slag upkeep | 1911 | 1.5-2d a square yard-year | £49-65/km-year over 7 m | Surface upkeep | evidence §3 |
| Urban street maintenance | 1870-1900 | 5d to 1s 6d a square yard-year | £174-628/km-year over 7 m | Whole street upkeep, largely renewal | evidence §3 |
| Motorway, under 2 years old | 1982 | £6,000/mile-year | £124.6/km-year | Routine only (no renewal yet) | HL Deb 1982 |
| Motorway, 2-5 years | 1982 | £10,000/mile-year | £207.6/km-year | Routine plus patching | ibid. |
| Motorway, 6-10 years | 1982 | £15,000/mile-year | £311.4/km-year | Routine plus patching | ibid. |
| Motorway, over 10 years, renewal begun | 1982 | £40,000-120,000/mile-year | £830-2,491/km-year | Includes renewal | ibid. |
| Motorway structural maintenance outturn, 1984-85 | 1984 | £66,059/mile | £1,305/km-year | Structural maintenance, renewal-dominated | HL Deb 1986, via the workbook |
| Strategic-road resurfacing | 2023 | £78.53-95.71/m² | £6,335-7,721/km per operation over 7 m | Renewal | DfT 2024, UKRLG rates |
| Classified-road resurfacing | 2023 | £28.22-30.37/m² | £2,278-2,452/km per operation over 7 m | Renewal | ibid. |
| Unclassified-road resurfacing | 2023 | £15.95-18.10/m² | £1,288-1,461/km per operation over 7 m | Renewal | ibid. |
| National Highways, maintenance and renewal | 2024-25 | £48,000-112,000 per lane-mile | £336-786 per lane-km-year | Combined | ORR regional summaries |

### 3.3 What the figures mean

1. **The 1819 and 1880 main-road rates agree.** £50/mile in 1819 is £22.03/km-year at 1900;
   £35 11s/mile in 1880 is £21.66/km-year at 1900. Two measurements 61 years apart give the same
   real figure, which is why £22 is a sound anchor for an ordinary main road. It is a combined
   figure.
2. **The routine share of the 1880 main-road rate is £4-15/km-year.** Re-stoning at £53.09/km per
   operation on a 3-7 year cycle is £7.6-17.7/km-year, leaving £4.0-14.1/km-year for routine. The
   range is wide because the cycle is not recorded. Five years, the middle of the range, gives
   £10.9/km-year of re-stoning and £10.8/km-year of routine.
3. **The urban rate is 8-29 times the rural rate**, which is the largest single class effect in
   the family. Over a 7 m carriageway the Victorian range is £174-628/km-year; even the bottom of
   it is eight times the 1880 rural main-road rate.
4. **Modern resurfacing is a renewal rate and it is about 1.1-1.2 per cent of capital a year** on
   a 13-year cycle: £2,366/km at 1900 per operation divided by 13 is £182/km-year, against a
   £15,844/km asphalt road. That is the cross-check that fixes the modern routine band, because a
   routine rate of 0.3-0.5 per cent of capital sits under it and gives a combined 1.4-1.7 per cent,
   which is consistent with the measured National Highways combined figure.
5. **The motorway row's measured £1,304.74/km-year is structural maintenance, not routine.** It
   corresponds exactly to the 1984-85 outturn of £66,059 a mile for all motorways, which the
   workbook's own note records as "structural maintenance only; routine and winter maintenance
   appear to be outside it". Structural maintenance in highway accounting is reconstruction and
   resurfacing, that is, renewal. Using it as the routine target repeats the category error already
   found on the elevated ways, where bridge capital was used as annual upkeep.

### 3.4 The bands to apply

| Class | Routine maintenance, GBP1900/km-year | Basis |
|---|---:|---|
| Bridleway and unsurfaced track | 2-4 | No surface to renew; grading, grips and gates; below the 1880 minor rate |
| Rural minor made road, 1800-1930 | 5-8 | 1880 minor rate £7.58, less its re-stoning |
| Rural main made road, 1800-1930 | 5-15 | 1880 main rate £21.66 less £7.6-17.7 of re-stoning |
| Tarred or bituminous surface, 1906-1939 | 45-65 | 1911 tarred slag at 1.5-2d a square yard-year |
| Urban street, 1850-1939 | 174-628 (whole upkeep); 60-150 routine | Victorian range; the lower part of the range is routine |
| Modern paved rural road, 1950-2026 | 30-90 (0.2-0.6 per cent of capital) | DfT resurfacing at 1.1-1.2 per cent plus routine; National Highways combined |
| Motorway, 1958-2026 | 125-310 | 1982 age ladder before renewal begins |

---

## 4. The road forge

### 4.1 The constraint

The forge is one value for the whole road family. It is charged on every new plain road tile and
not on an upgrade. The cheapest road object is the bridleway, at GBP100/km of whole construction,
and the two unsurfaced rows share that figure. The forge must therefore be at or below GBP100/km,
which is 25,232 raw units. Any value above that produces a negative way-only value on three rows,
which is the defect the 2026-11-26 audit found at 315,000.

### 4.2 The recommended value: 20,000 raw = GBP79.26/km

**Recommended: `forge_cost_road = 20,000`, equal to GBP79.26 per kilometre at 1900 prices, with a
defensible band of GBP45-79/km (11,400-20,000 raw).**

The derivation:

1. The forge is bed preparation: clearing, drainage, grading to level and crossfall, soiling and
   fencing. It is not bulk earthworks (land tool) and it is not the pavement.
2. Telford's measured bed preparation for a 32 ft formation is £110.1/km at 1900: forming £44.0,
   drains £22.0, sodding £44.0. That is MEASURED for 1825 and is the only measured bed-preparation
   figure in the corpus.
3. A bridleway bed is about 3 m wide against 32 ft (9.75 m), so the width-proportional part falls
   to about a third, but the side drains do not scale with width because they run on both sides
   whatever the width. Scaling the £110.1 gives £34-45 for a 3-4 m width and £110 for no scaling;
   the correct value is between, and £79.3 is 72 per cent of the 32 ft rate.
4. £79.26 is 79 per cent of the cheapest road's whole construction (£100), which leaves the
   bridleway a positive £20.74/km for its running surface, gates and grips. It leaves headroom of
   £20.74 below the ceiling, so a small future correction to the bridleway total cannot make the
   value negative. The forge is bound to that total: if the bridleway is ever re-derived below
   £79.26, the forge must fall with it, because the ceiling is a property of the cheapest object
   and not of the forge.
5. It is far below the modern pavement-box formation of £2,924/km (§1.2), which is the intended
   consequence: the forge is the floor of the family, not its average.

### 4.3 What standard the value represents

The value represents **the bed of an unsurfaced way of bridleway width**: the cheapest standard in
the family, which is the only standard at which a single per-waytype value can be both realistic
and no larger than the cheapest object. It does not represent a paved road's bed. A 7 m asphalt
road's bed preparation and pavement box is £2,924/km at 1900; a Victorian sett street's is
£2,000-3,000/km; a concrete runway's is £14,600/km. In every one of those cases the great majority
of the formation is carried by the way object, not by the forge.

### 4.4 Consequences of the per-waytype system, stated

The user's direction of 2026-11-27 accepts a per-waytype forge in preference to a per-object forge
and requires the formation/way distinction to be kept. That choice has four consequences that must
be recorded on the affected rows.

1. **New build.** The forge charges £79.26/km for the bed of every road, from bridleway to
   motorway. For the motorway the remaining £2,845/km of bed sits in the way object and is charged
   with it.
2. **Upgrade.** No forge is charged. The way object's cost, which includes the excess formation,
   is charged in full. That is the right direction: a higher standard needs more formation, and the
   model charges for it through the more expensive way object. The 2.9:1 ratio between modernising
   an existing road and building a new one in 1938 measures widening and reconstruction, which the
   engine represents by laying a new way, so the model does not reproduce that ratio from the forge
   alone; it follows from the player's choice of object.
3. **Parallel way.** The engine discounts the forge by 50 per cent, so a second carriageway saves
   £39.63/km, not half the roadbed. For a motorway that under-recovers by about £700/km; for a
   bridleway it over-recovers by about £40/km. The error is bounded by the excess formation and is
   largest on the highest-standard objects.
4. **Renewal.** `weg_t::renew()` charges the way object's value and not the forge, so the excess
   formation is repaid at every renewal. For the modern rows that overstates renewal by the excess
   formation share, which is 18 per cent of the asphalt road's way cost and 5.5 per cent of the
   motorway lane's. For the unsurfaced rows it is correct, because a track's renewal is
   re-grading, which is maintenance.

The alternative — a per-object `forge_cost=` field in the way descriptor — would remove all four
errors and is recorded in the audit as a refinement for a future engine version. It is not
required for the per-waytype system to be coherent, and this report does not propose it.

---

## 5. Way-only targets for every road row

All values GBP1900 per kilometre. The forge is GBP79.26 on every row. "Class total" is the
workbook's class figure, which for most rows is also the measured or derived figure; where the
class total is not supported by the evidence, the note says so and gives the supported range.

| Row | `.dat` key | Intro | Class total | Forge | Way-only | What the way-only value represents |
|---|---|---|---:|---:|---:|---|
| Hot rolled asphalt road (280 mm) | `hr-asphalt-road-heavy` | 1954 | 15,844 | 79.26 | **15,764.74** | Asphalt base, binder and surface courses plus the excess formation above the forge (about £2,845) |
| Hot rolled asphalt road (210 mm) | `hr-asphalt-road-light` | 1927 | 15,844 | 79.26 | **15,764.74** | As above; the class figure does not vary by thickness, which is a defect noted in §8 |
| Hot rolled asphalt road (260 mm) | `hr-asphalt-road-medium` | 1935 | 15,844 | 79.26 | **15,764.74** | As above |
| Stone mastic asphalt road (175 mm) | `sma-road-heavy` | 1995 | 15,844 | 79.26 | **15,764.74** | SMA surface, binder and base plus excess formation |
| Stone mastic asphalt road (130 mm) | `sma-road-light` | 1996 | 15,844 | 79.26 | **15,764.74** | As above |
| Stone mastic asphalt road (165 mm) | `sma-road-medium` | 1996 | 15,844 | 79.26 | **15,764.74** | As above |
| Bridleway | `bridleway` | 1000 | 100 | 79.26 | **20.74** | The running surface of a track: soil binding, crossfall, grips and gates |
| Hot rolled asphalt road (270 mm) | `city_road` | 1932 | 26,406 | 79.26 | **26,326.74** | Thicker urban pavement, kerbs, gullies and footway share, plus the urban bed above the forge |
| Stone mastic asphalt road (140 mm) | `city_road-sma` | 1997 | 26,406 | 79.26 | **26,326.74** | As above |
| Cobblestone road | `cobblestone_road` | 1765 | 123 (not supported; see note) | 79.26 | **43.74** on the present total; **£4,921-6,921** on the derived total | Granite setts and their concrete bed. The present total is the 1819 turnpike average, not a cobble rate: a sett carriageway is £3,400-8,000/km, working band £5,000-7,000 (§2.2). On the derived total of £5,000-7,000 the way-only is £4,921-6,921 |
| Concrete viaduct elevated road | `ConcreteViaductElevatedRoad` | 1600 | 434,082 | 79.26 | **434,002.74** | The whole deck and supports; the forge is a rounding error on this row |
| Concrete road | `concrete_road` | 1936 | 23,766 | 79.26 | **23,686.74** | Concrete slab, joints and sub-base plus excess formation |
| Unsurfaced road (unimproved) | `old_dirt_road` | 1000 | 100 | 79.26 | **20.74** | Graded earth surface and grips |
| Unsurfaced road (improved) | `dirt_road` | 1700 | 100 | 79.26 | **20.74** | Graded earth with crossfall, side drains and culverts |
| Iron girder elevated road | `IronGirderElevatedRoad` | 1600 | 164,000 | 79.26 | **163,920.74** | Deck and iron supports |
| MacAdam road | `macadam_road` | 1820 | 833 | 79.26 | **753.74** | Broken-stone courses and binding gravel; the formation is the forge plus the small excess in this value. The total is independently confirmed at £823/km by the 1912 macadam rate |
| Motorway (hot rolled asphalt, 350 mm) | `motorway` | 1958 | 26,377 | 79.26 | **26,297.74** | One lane-width of pavement plus the excess formation (about £1,446). The total is per lane, not per carriageway; see §8 |
| Motorway (stone mastic asphalt, 230 mm) | `motorway-sma` | 1996 | 26,377 | 79.26 | **26,297.74** | As above |
| Tar MacAdam road (heavy) | `tarmac_city_road` | 1904 | 1,875 | 79.26 | **1,795.74** | Tar-bound surface and its frequent renewal; urban loading |
| Tar MacAdam road | `tarmac_road` | 1896 | 1,072 | 79.26 | **992.74** | Tar-bound surface on a prepared macadam base |
| Wooden trestle elevated road | `WoodTrestleElevatedRoad` | 1600 | 48,000 | 79.26 | **47,920.74** | Timber deck and trestles |
| Mothballed road | `mothballed_road` | — | none | 79.26 | **0** (no total exists) | No construction standard and no measured price. The forge would be its whole cost. Either exclude the object from the forge check or set its way cost to 0 and record that the forge is its entire price |

Notes on the table.

- The live sheet holds 22 rows, not the 24 named in the brief: 18 plain rows, 3 elevated rows and
  one mothballed row with no price.
- No way-only value is negative, including the cobblestone row on its present total.
- **Scope of the motorway row.** Its class figure comes from a *pavement-only* measured rate ("way
  only, GBP1.2-1.5m per lane-km"), not a combined total. Strictly the way object should carry the
  measured rate and the total should be that plus the forge, which would be GBP26,456 rather than
  GBP26,377; the GBP79.26 difference is 0.3 per cent and changes no conclusion. Every other road row
  is either a combined total or a formation-only total, for which total less forge is correct.
- The hot-rolled-asphalt and stone-mastic rows all share one class figure of £15,844/km. That is
  the HS2 2011 rural rate of £138/m² over 7 m, deflated. It does not vary with layer thickness, so
  the six rows are indistinguishable in the model although a 280 mm pavement costs more than a
  130 mm one. That is a limitation of the class figure, not of the forge.

---

## 6. Runway and taxiway analogy

### 6.1 The air evidence

| Item | Year | Figure | Scope | Source |
|---|---|---|---|---|
| Grass runway, "simple levelling, rolling and mowing" | 2026 note, AVD 1 April 2024 | £1.00/m² | Whole grass strip, no drainage | VOA Rating Manual, airports practice note 2026, airstrips section |
| Grass runway, "drained and stabilised" | 2026 note, AVD 2024 | £2.00-2.50/m² | Whole grass strip with mole or tile drainage and stabilisation | ibid. |
| Concrete pavement, PCN 10 | 2026 note, AVD 2024 | £69/m² | Pavement, includes excavation and disposal, imported limestone fill, lean-mix sub-base, PQC slab, drainage and AGL ducting | ibid., Table A |
| Concrete pavement, PCN 93+ | 2026 note, AVD 2024 | £189/m² | As above | ibid. |
| Concrete pavement, PCN 10 | 2023 note, AVD 1 April 2021 | £58/m² | As above | VOA practice note 2023 |
| Concrete pavement, PCN 93+ | 2023 note, AVD 2021 | £159/m² | As above | ibid. |
| Asphalt layers, 130-280 mm | 2017-21 | £32-56/m² | Asphalt layers only | evidence §9 |
| Runway and apron, including earthworks | 1960 | £4.60/m² (77s/sq yd) | Whole pavement; build-up stated | Gatwick, report 11 §5.1 |
| — earthworks and subgrade within the above | 1960 | 37.7 per cent | Formation | ibid. |
| — concrete slab and lean-mix base | 1960 | 48.0 per cent | Pavement | ibid. |
| — joints | 1960 | 14.3 per cent | Pavement | ibid. |
| Wartime average, all hard surfacing | 1945 | £1.37/m² | Whole pavement, 175 million sq yd | report 11 §5.1 |

The Valuation Office Agency description settles the point the user made: a grass runway's cost
**is** its formation. "The valuation of grass runways will therefore depend on the nature of the
surface, and costs will vary from £1.00 p s m for simple levelling, rolling and mowing to £2.50 p s
m for drained and stabilised runway surfaces." The 2026 practice note adds "For gliding sites, a
rolled and mown field typical size 1000m x 30m = 30,000sqm Valued at £1/m2. If stabilised up to £2
sqm." There is no separate "surface" cost apart from drainage, stabilisation and mowing.

The 1960 Gatwick build-up is the only measured airfield split of formation against pavement, and
it gives formation (earthworks and subgrade) 37.7 per cent of the whole for a concrete runway. That
is the air analogue of Telford's 56.6 per cent for a road, and it is the figure to use where an
airfield-specific split is absent.

### 6.2 The recommended air forge: 110,000 raw = GBP435.94/km

**Recommended: `forge_cost_air = 110,000`, equal to GBP435.94 per kilometre at 1900 prices.**

The derivation:

1. The cheapest air object is the grass taxiway at £575/km of whole construction in the workbook.
   The forge must not exceed it.
2. The grass specification gives the formation share directly. The £2.50/m² drained-and-stabilised
   rate is the £1.00 levelling plus £1.50 of drainage and stabilisation. Drainage is bed
   preparation; stabilisation and coating are surface. If between half and two thirds of the £1.50
   is drainage, the formation is £1.75-2.00/m², or 70-80 per cent of the total.
3. Seventy-six per cent of £575/km is **£435.94/km**, which is 110,000 raw units. That is the
   midpoint of the 70-80 per cent band applied to the cheapest object.
4. It leaves the grass taxiway £139.06/km for its surface, and the grass runway £327.06/km, of
   which about £188 is the extra 7 m of width that a single per-kilometre forge cannot carry.

The forge represents **the levelling and drainage of a grass strip 23 m wide**: the cheapest
standard in the air family. It does not represent a paved runway's formation, which the Gatwick
split puts at £14,614/km for a 45 m concrete runway at 1900 — 33 times the forge. That excess sits
in the paved runway's way object, which is the intended compromise.

If the grass rows are later re-deflated to the correct Valuation Office basis (see §8), the grass
taxiway becomes about £650/km and the same 76 per cent rule gives 123,000 raw, or £487.46/km. The
recommended 110,000 is deliberately below both the present and the corrected ceilings.

### 6.3 Way-only targets for every air row

All values GBP1900 per kilometre. Forge GBP435.94 on every row.

| Row | `.dat` key | Intro | Class total | Forge | Way-only | Share | What the way-only value represents |
|---|---|---|---:|---:|---:|---:|---|
| Grass runway | `GrassRunway` | 1909 | 763 | 435.94 | **327.06** | 42.9% | The extra 7 m of width above the taxiway, the stabilisation, the surface coating, mowing and markers |
| Grass taxiway | `GrassTaxiway` | 1909 | 575 | 435.94 | **139.06** | 24.2% | Stabilisation, surface coating and markers; levelling and drainage are the forge |
| Tar MacAdam runway | `tarmac-runway` | 1929 | 22,757 | 435.94 | **22,321.06** | 98.1% | Bituminous pavement and the whole formation above the forge |
| Tar MacAdam taxiway | `tarmac-taxiway` | 1929 | 17,161 | 435.94 | **16,725.06** | 97.5% | As above |
| Asphalt runway | `runway` | 1938 | 22,757 | 435.94 | **22,321.06** | 98.1% | Asphalt pavement and the whole formation above the forge |
| Asphalt taxiway | `taxiway` | 1938 | 17,161 | 435.94 | **16,725.06** | 97.5% | As above |
| Concrete runway | `concrete-runway` | 1962 | 98,440 | 435.94 | **98,004.06** | 99.6% | Concrete slab, lean-mix base, joints, drainage and AGL ducting, plus the formation above the forge |
| Concrete taxiway | `concrete-taxiway` | 1962 | 50,314 | 435.94 | **49,878.06** | 99.1% | As above |

Two observations.

- **The paved rows are 98-99.6 per cent way object.** For them the forge is a token charge, which
  is honest: their formation is 33 times the forge and there is no way to put it in a per-waytype
  constant. This is the clearest illustration of the compromise.
- **The grass runway's 42.9 per cent residual is mostly width, not surface.** The grass runway is
  30 m wide and the taxiway 23 m. A per-kilometre forge cannot scale with width, so the runway
  carries the extra 7 m in its way object. If a narrower runway were modelled the residual would
  fall towards the taxiway's 24 per cent.

A scope note on the four paved rows. Their class figures are pavement rates, and the Valuation
Office description includes the excavation, the imported fill and the lean-mix sub-base — the
pavement box — but not the bulk earthworks of the alignment. Strictly, a paved row's way object
should carry the measured pavement rate and the total should be that plus the forge. The difference
is GBP435.94/km: 2.5 per cent of the asphalt taxiway, 1.9 per cent of the asphalt runway, 0.9 per
cent of the concrete taxiway and 0.4 per cent of the concrete runway. The table uses the workbook's
convention (total less forge) because that convention is what the `.dat` field needs once the total
is fixed.

### 6.4 Air maintenance

The published rule is 1.6-2.4 per cent of capital a year. Checked against the roads, that figure is
a **combined** maintenance-and-renewal rate: a modern paved road's resurfacing alone is 1.1-1.2 per
cent of capital a year on a 13-year cycle, and its routine upkeep 0.3-0.5 per cent, giving 1.4-1.7
per cent combined. The air band's lower end therefore coincides with the road's combined rate,
which is what a 1.6-2.4 per cent band for a well-maintained pavement should do.

The band fits asphalt, not both materials. Asphalt airfield pavements are resurfaced every 10
years (Table 11.2), which at 16-20 per cent of capital an overlay is 1.6-2.0 per cent a year,
leaving 0.4-0.8 per cent for routine. Concrete airfield pavements need joint resealing every
12-25 years and occasional spall and slab repair, about 0.3-0.6 per cent a year in total. The
1.6-2.4 per cent band therefore describes the asphalt rows; the concrete rows should be 40-50 per
cent of it. Section 11 sets out the evidence. On that basis:

| Row | Capital | Routine maintenance, GBP1900/km-year | Rate | Basis |
|---|---:|---:|---:|---|
| Grass runway | 763 | **10** | 1.3% | Mowing and rolling several times a year; no overlay |
| Grass taxiway | 575 | **7** | 1.2% | As above |
| Tar MacAdam runway | 22,757 | **114** | 0.50% | Flexible: patching, crack sealing, surface preservation |
| Tar MacAdam taxiway | 17,161 | **86** | 0.50% | As above |
| Asphalt runway | 22,757 | **114** | 0.50% | As above |
| Asphalt taxiway | 17,161 | **86** | 0.50% | As above |
| Concrete runway | 98,440 | **246** | 0.25% | Rigid: joint resealing, spall and slab repair |
| Concrete taxiway | 50,314 | **126** | 0.25% | As above |

The grass strips are at 1.2-1.3 per cent of capital because mowing and rolling recur several times
a year whatever the capital value; their surface renewal is very low, as the user directed, and the
engine charges it separately. The paved rows are at 0.50 per cent for asphalt and 0.25 per cent for
concrete, a ratio of 1:2 in the rate but not in the absolute figure: the present concrete runway
capital is 4.33 times the asphalt runway's, so concrete's absolute upkeep is higher even at half
the rate. That is a symptom of the capital defect set out in section 11.1, not of the rate.

---

## 7. Maintenance bands, routine only

| Family and class | Era | Routine band, GBP1900/km-year | Renewal excluded |
|---|---|---:|---|
| Road: bridleway and unsurfaced | all | 2-4 | None: a track has no surface, its renewal is re-grading |
| Road: rural minor made road | 1800-1930 | 5-8 | Yes: 1880 minor rate less re-stoning |
| Road: rural main made road | 1800-1930 | 5-15 | Yes: 1880 main rate £21.66 less £7.6-17.7 of re-stoning |
| Road: tarred or bituminous | 1906-1939 | 45-65 | Yes: 1911 tarred-slag upkeep |
| Road: urban street | 1850-1939 | 60-150 routine; 174-628 whole upkeep | Whole upkeep includes lifting and relaying setts |
| Road: modern paved rural, asphalt | 1950-2026 | 30-90 (0.3-0.6 per cent of capital) | Yes: patching, crack sealing, surface preservation; the 1.1-1.2 per cent resurfacing rate is renewal |
| Road: modern paved rural, concrete | 1936-2026 | 0.25 per cent of capital | Yes: joint resealing and slab repair; renewal is wear-driven |
| Road: motorway | 1958-2026 | 125-310 | Yes: the 1982 age ladder before renewal begins; the £1,305 structural figure is renewal |
| Road: elevated | all | bridge upkeep 45-530 plus way upkeep | Yes: Cudworth's measured rates, 0.046-1.15 per cent of structure capital |
| Air: grass strip | 1909-2026 | 7-10 | Yes: mowing, rolling, drainage; no overlay |
| Air: paved, asphalt | 1938-2026 | 0.50 per cent of capital | Yes: the published 1.6-2.4 per cent band includes the 10-year overlay |
| Air: paved, concrete | 1962-2026 | 0.25 per cent of capital | Yes: joint resealing and slab repair only; no overlay inside the design life |

The road band runs from £2 to £310/km-year, a factor of 155; the air band from £7 to £246, a
factor of 56. A single per-waytype value cannot express either, which is why the maintenance field,
being per object, should carry the variation. The forge cannot.

---

## 8. What is not supported

1. **`forge_cost_road = 315,000` (GBP1,248.38/km).** It is 12.5 times the bridleway's whole
   construction, 10.2 times the cobblestone row and 1.5 times the MacAdam row; it produces the six
   negative way-only values the audit found. No research report derives it: the stated basis, a
   range of 250,000-380,000, appears only as a recommendation in
   `infrastructure-cost-synthesis.md` §5 and is repeated in `research-pricing-report-3.md` §4.5.
   The stated bands (early formation £50-250/km, modern roadbed £2,000-8,000/km) produce neither
   end of that range. The modern band is itself supported (§1.2), but as a modern pavement-box
   figure, not as a 1900 formation.
2. **The single road maintenance of GBP21.57/km-year on all 22 rows.** It is the 1880 main-road
   rate including re-stoning, so it is not routine only; and it is 5-10 times too high for a
   track, 8-29 times too low for an urban street, and 6-15 times too low for a motorway.
3. **`forge_cost_air = 1,875,000` (GBP7,430.83/km).** It is 9.7 times the whole grass runway and
   12.9 times the whole grass taxiway. Its basis, a GBP6,000-9,000/km modern runway subgrade
   estimate, has no entry in `infrastructure-cost-evidence.md`, is marked unverified in
   `research-pricing-report-3.md` §4.3, and cannot be reconciled with the measured Gatwick split
   of 37.7 per cent of £4.60/m², which is £14,614/km for a 45 m runway at 1900.
4. **The air maintenance of GBP6.67/km-year.** It is the rail rate, deflated twice (the £44 is
   already 1900 money), applied to every air row. For the concrete runway it is 236-354 times below
   the measured 1.6-2.4 per cent band even on the combined basis, and for the two concrete rows it
   is 60-118 times below the routine band of §6.4.
5. **The motorway row's GBP1,304.74/km-year used as a routine target.** It is 1984-85 structural
   maintenance, that is renewal, as the workbook's own note records. The audit's statement that
   the class target is "60 times below" it therefore compares a routine target with a renewal
   figure; the correct routine comparison is the 1982 age ladder's £125-310/km-year.
6. **The cobblestone row's GBP123/km total.** It is the 1819 turnpike network average, which
   measures improvements to existing roads, not a sett carriageway. Two sources, British and
   colonial, put a sett carriageway at £3,400-8,000/km at 1900 (§2.2), 28-65 times higher.
7. **The air capital rows use inconsistent deflators.** The grass rows are deflated at an index of
   about 3,932 (1989); the concrete and asphalt rows at 5,897 (2010). The Valuation Office rates
   the research used are at an antecedent valuation date of 1 April 2024 (deflator 8,850), and the
   asphalt band is 2017-21. At the correct deflator the concrete runway is £65,593/km rather than
   £98,440, and the concrete taxiway £33,525 rather than £50,314. The concrete runway figure is
   still within the historical envelope (the measured Gatwick 1960 rate is £38,764/km at 1900), so
   this is a documentation defect rather than a price error, but the rows cannot be defended as
   they stand.
8. **The motorway row's width basis is contradictory.** The workbook's class basis says "one
   lane-width per tile"; `infrastructure-cost-synthesis.md` §4.3 says "a motorway tile is one
   carriageway". The row's value is per lane, and if a tile is a carriageway the row is about three
   times too low. This must be settled before the row is used.
9. **The hot-rolled-asphalt and stone-mastic rows do not vary with layer thickness**, although the
   workbook carries 130, 165, 175, 210, 260, 270, 280 and 350 mm variants. The class figure is one
   HS2 rate; the layer evidence in §2.5 would support a thickness ladder.
10. **The 1819 average and the 1906 tarmac rate are not whole-construction rates.** The 1819
    average is an improvement rate on existing alignments and contains almost no formation; the
    1906 figure at 2s a square yard is a surfacing rate with no bed at all. A row built from either
    understates the object by the whole of the bed, which is why the cobblestone row is 28-65 times
    too low.
11. **The air "30-40 per cent of pavement cost" statement** is not an airport figure; the only
    30-40 per cent statement in `research-pricing-report-3.md` concerns electrification route
    clearance. It should not appear as an airfield basis.
12. **The concrete road row has no concrete rate behind it.** Its class basis is the HS2 2011
    "major road" rate of £207/m², which is an asphalt rate for a busier road class. The +50 per cent
    over the hot-rolled-asphalt row is the HS2 rural-to-major difference, not a material premium.
13. **The concrete runway's 4.33-fold premium over the asphalt runway is not a material premium.**
    The concrete figure is the midpoint of a PCN 10-93 strength ladder, the asphalt has no stated
    PCN, the widths are 45 m and 30.5 m, and the concrete rate covers the whole pavement box while
    the asphalt rate covers the asphalt layers only. Section 11.1 sets out the three differences.
14. **Concrete's maintenance advantage is already in `wear_capacity` and is not in the maintenance
    field.** `ways/concrete_road.dat` carries 4,000,000,000 against `ways/asphalt-roads.dat`'s
    650,000,000, and the runways 2,695,680,000 against 864,000,000, so the engine already gives
    concrete a 6.15-fold and 3.12-fold longer wear life. Charging a renewal provision in
    `maintenance=` as well double-counts it.

---

## 9. Sources

**Primary, read for this report.**

- Telford, Thomas, *A Treatise on Roads* (London, 1838), chapter VIII "Management of Road Works",
  estimate for the Coventry division of the Holyhead Road and the specification for a new road;
  and the appendix examination of John Provis, 1836. ETH-Bibliothek, doi 10.3931/e-rara-66372.
- Valuation Office Agency, *Rating Manual section 5a: valuation of all property classes —
  Airports, practice note 2026*, including Table A minor-airport pavement costs at antecedent
  valuation date 1 April 2024 and the airstrips/gliding-sites section; and the 2023 practice note
  for comparison. gov.uk guidance.
- Valuation Office Agency, *Rating Cost Guide 2026* (ninth edition; costs at AVD 1 April 2024).
- Leicestershire County Council, *Melton Mowbray Distributor Road, Appendix C detailed cost
  breakdown*, October 2017.
- Wakefield Metropolitan District Council, planning application appendix 3i, road cost schedule
  (Section 38 road).
- Kent County Council / National Highways, *M20 junction 10a Cost Plan Nr. 1*, 4Q2025.
- HWA, *CD37.14.2A Appendix 2 side-by-side comparison* (National Highways M2 and Kent CC relief
  roads).
- AECOM, *Pavement Whole Life Cost*, MHA+ concrete roads session 3, 30 November 2021 (Spon's
  Civil Engineering and Highways Works Price Book unit rates).
- *Estimating and Costing of Architectural and Engineering Works*, contractor's schedule for New
  Westminster, British Columbia, 1912-13, English-equivalent price column.
- Department for Transport, *Economic appraisal for investing in local highways maintenance*
  (2024), republishing the UKRLG unit rates at 2023 prices.
- Office of Rail and Road, *National Highways regional performance summaries 2024-25*.
- ISB (Belgian Road Research Centre), *Life cycle cost analysis of continuously reinforced concrete
  pavements (CRCP)*, 2019/20 Belgian prices: construction cost, maintenance strategy and net
  present value for CRCP, JPCP and bituminous structures.
- *Infrastructures* 2021, 6(8), 117, "Comparing the Cost of Rigid and Flexible Aircraft Pavements
  Using a Parametric Whole of Life Cost Analysis", MDPI: construction premium of 20-110 per cent,
  the maintenance schedules for rigid and flexible airfield pavements, and their 40-, 60-, 80- and
  100-year whole-of-life comparison.
- Georgia Department of Transportation, *Pavement Type Selection Manual*, Table 3.2
  "Pavement Rehabilitation Cycle": asphalt 14 years, JPCP 25 years, CRCP 30 years.
- Federal Highway Administration, *Long-Life Concrete Pavements in Europe and Canada* (2007
  international scan): Ontario JPCP joint resealing and restoration cycles; Netherlands practice of
  no maintenance in the first 15 years on bare CRCP.
- *International Journal of Engineering Research and Technology*, "An Evaluation of Life Cycle Cost
  Analysis of Airport Pavement", 2015: rigid runway +21 per cent initial cost, 78 per cent lower
  maintenance and rehabilitation.
- American Concrete Pavement Association, *Pavement Note 001: Concrete Pavement Value*, April 2020:
  the concrete industry's claim of 47-58 per cent lower maintenance and 7-22 per cent lower capital.
- Texas A&M Transportation Institute, CTR 0-6085-1, *Considerations for Rigid vs. Flexible Pavement
  Designs When Allowed as Alternate Bids*: the asphalt industry's counter-claim of 10-25 per cent
  lower initial and life-cycle cost for hot-mix asphalt.
- Federal Aviation Administration, AC 150/5320-6E, appendix 4 (economic analysis of pavement
  alternatives; 20-year analysis period, 4 per cent discount); ICAO, *Airfield Pavement Design and
  Rehabilitation*, APAC workshop, February 2024 (20-year design life, 20-year overlay life).
- House of Lords debate, 23 November 1938, County Surveyors' Association road costs; House of
  Commons and House of Lords answers of 1958, 1961, 1962, 1969, 1978, 1980, 1982 and 1986 as
  recorded in `New/ai/cost-balancing/research-pricing-report-5.md` §4-§5.

**Stored knowledge-base sources used.**

- `New/ai/infrastructure-cost-evidence.md` §3 (roads) and §9 (airports).
- `New/ai/infrastructure-cost-synthesis.md` §3.2, §3.7, §4.3 and §5.
- `New/ai/cost-balancing/research-pricing-report-3.md` §4 (formation and earthworks).
- `New/ai/cost-balancing/research-pricing-report-5.md` §4 (road construction) and §5 (road
  maintenance and resurfacing).
- `New/ai/cost-balancing/research-pricing-report-11.md` §5 (airfield pavements, the Gatwick 1960
  build-up and runway widths).
- `New/ai/cost-balancing/research-pricing-report-13.md` §4 (tram and street track, the urban road
  analogy).
- `New/ai/cost-balancing/way-cost-audit-2026-11-26.md` (§3 capital scopes, §4 maintenance, §7 the
  replacement decomposition).
- `New/ai/cost-balancing/individual-price-rows.csv` (way and airport rows).
- `New/ai/prices-forum-fragments.md` (forum thread 6521, roads and other structures).
- `New/ai/cost-balancing/measured_infra.py` and `New/config/prices.tab` (the deflator and the
  conversion constants).
- `New/cost-balancing-capital.xlsx`, sheets `Ways - road` and `Ways - air`.

**Searches run.** Five: Telford's road-cost breakdown; Victorian street-paving costs per square
yard; the Valuation Office airport pavement table and its price year; concrete against asphalt
pavement whole-life cost; concrete against asphalt airfield pavement whole-life cost. Every figure used was read
from a fetched page, not from a search summary. No figure in this report was taken from a `.dat`
price.

---

## 10. Limits and open questions

1. **The routine-versus-renewal split for the 1880 road rates is derived, not measured.** The
   re-stoning cycle is unknown; a 3-7 year band gives £4.0-14.1/km-year of routine. A measured
   re-stoning interval from a turnpike trust's minutes would close it.
2. **The interwar formation is an ESTIMATE.** No measured British split of a 1920s or 1930s road
   between formation and pavement was found. The 1938 Hansard figures give whole-construction
   rates only.
3. **The Victorian urban bed is DERIVED** from a Canadian contractor's schedule of 1912-13, checked
   against the British 1877 street-tramway figure. A British municipal sett-paving account with the
   concrete bed priced separately would replace it.
4. **The airfield formation share of 37.7 per cent rests on one scheme**, Gatwick 1960, read from
   `research-pricing-report-11.md` rather than from the original estimate.
5. **The 70-80 per cent formation share of a grass strip is DERIVED** from the Valuation Office's
   two grass rates, not measured. The split between drainage and stabilisation within the £1.50
   difference is not stated by the source.
6. **Whether the Valuation Office pavement rates include earthworks is not stated.** The
   description covers excavation and disposal of surplus material, imported limestone fill,
   lean-mix sub-base, PQC slab, drainage and AGL ducting — that is the pavement box but not the
   bulk earthworks. If a paved runway needs a formation above that, the paved air rows are
   understated by about the Gatwick share.
7. **The motorway row's tile width is unresolved** (lane or carriageway), and the 2005 per-lane
   rate and the 2011 delivered rate differ by a factor of four per lane. Both need settling before
   the row is used.
8. **The cobblestone correction has not been applied to any total.** This report gives the derived
   range and the way-only value on both the present and the derived totals, so that the decision
   can be taken separately.
9. **The 1.6-2.4 per cent air maintenance band has no recorded source.**
   `infrastructure-cost-evidence.md` §9 states it without citing the account it comes from. The
   derivation in §6.4 shows it is consistent with a combined maintenance-and-renewal rate, but its
   provenance should be traced before it is treated as a measurement rather than an author's
   figure.
10. **The two forge values are floors, and no evidence can make them averages.** A per-waytype
    forge cannot be both realistic for a bridleway and realistic for a motorway, whose formations
    differ by a factor of 30-40. The values recommended here are the highest that satisfy the
    ceiling the user set; a per-object `forge_cost=` descriptor remains the only way to make the
    new-build and renewal charges exact for every road and air object.

---

## 11. Concrete against asphalt: capital, maintenance and the renewal cycle

The question is whether concrete roads and runways cost more to build and less to keep, and whether
the pakset preserves that trade-off. The answer is that the trade-off is real and is measurable, but
the pakset preserves it in the wrong places: the *wear* field already carries most of it, the
maintenance field is 7-24 times too high on both materials, and the air capital rows are not a
like-for-like comparison at all, so concrete's maintenance advantage cannot show in the absolute
figures until they are fixed.

### 11.1 The capital premium

| Comparison | Basis | Concrete over asphalt | Evidence |
|---|---|---:|---|
| Road, CRCP against full-depth asphalt, Belgian design, 2019-20 prices | Construction cost per km for the same traffic and section | **+3.7%** (EUR 1,374,438 against 1,325,314) | MEASURED, ISB LCCA of CRCP |
| Road, CRCP against flexible, UK Spon's 2021 rates, same 230 mm sub-base | GBP139.72/m² against GBP72.39/m² | **+93%** | DERIVED from AECOM/Spon's |
| Airfield, rigid against flexible, structurally equivalent, Australian rates | Parametric whole-of-life study, 40-year period, 45 m runway | **+20% to +110%** | MEASURED, *Infrastructures* 2021 |
| Airfield, rigid against flexible, Dhaka runway design, 2015 | 31.5 in rigid against 37 in flexible | **+21%** initial | MEASURED, IJERT 2015 |
| Road, concrete industry claim | — | **−7% to −22%** (concrete cheaper) | STATED, ACPA Pavement Note 001 |
| Road, asphalt industry claim | — | **+10% to +25%** (concrete dearer) | STATED, Texas CTR 0-6085-1 |

The two industry claims point in opposite directions and both differ from the measured studies, so
they should be read as advocacy: each trade body reports the comparison its own product wins. The
measured studies give **+4 to +110 per cent, with +20 to +60 per cent the central band for a
like-for-like design**. The lower end appears where the concrete design uses a thinner base, which
it can because of its stiffness; the upper end where the pavements are of similar total thickness.

In the pakset:

- **Concrete road: £207/m² against £138/m² of hot-rolled asphalt, +50 per cent**, which is inside
  the measured band. But the class basis of the concrete row is "HS2 major road construction 2011,
  GBP 207/m2", which is an *asphalt* rate for a busier road class. **There is no concrete rate
  anywhere behind the concrete road row.** Its +50 per cent is the HS2 rural-to-major difference,
  not a material premium, and it happens to land in the right place.
- **Concrete runway: £129/m² against £44/m², +193 per cent per m² and 4.33 times per kilometre.**
  That is well above the measured band, and it is not a material comparison either: the concrete
  rate is the midpoint of a strength ladder spanning PCN 10 to PCN 93 (that is, a runway of the
  heaviest wide-body class), while no PCN is stated for the asphalt row; the concrete row is 45 m
  wide and the asphalt row 30.5 m; and the asphalt rate covers the asphalt layers while the concrete
  rate covers the excavation, imported fill, lean-mix sub-base, slab, drainage and ducting. Three
  differences, none of them the material.

### 11.2 The maintenance differential

| Pavement | Rehabilitation event and cycle | Routine work between events | Source |
|---|---|---|---|
| Asphalt road, United States agency practice | Every 14 years: 5% deep patching, mill and inlay | — | GDOT Pavement Type Selection Manual, Table 3.2 |
| Jointed plain concrete road (JPCP) | Every 25 years: 5% slab replacement, diamond grinding, joint sealing | — | ibid. |
| Continuously reinforced concrete road (CRCP) | Every 30 years: 2.5% punch-out repair | — | ibid. |
| Asphalt road, Belgian design | Top layer at year 9 on the loaded lanes and year 18 on all lanes; reconstruction at 36 years | Crack and joint treatment every 3 years; patching every year, both from year 4 | ISB LCCA of CRCP |
| CRCP road, Belgian design | Reconstruction at 40 years, 60 with an asphalt overlay at 40 | Longitudinal joint resealing every 12 years; punch-outs 0.1/km/year from year 12 | ibid. |
| JPCP road, Belgian design | Reconstruction at 36 years | Joint resealing every 10 years; slab replacement 1/km/year from year 10 | ibid. |
| Asphalt airfield pavement | Resurfacing every 10 years | Crack sealing at years 4 and 7; surface preservation at year 8; patching at years 5 and 9 at 1% of area | *Infrastructures* 2021 |
| Rigid airfield pavement | Reconstruction at 40 years, often 60 or more in service | Spall repair at years 10, 20 and 30 at 0.5% of area; joint resealing at year 25; crack route and seal at years 12, 24 and 26; slab replacement at year 35 at 1% of area | ibid. |
| JPCP, Ontario practice | Concrete pavement restoration at year 28 | Joint resealing at years 12, 18 and 28; diamond grinding at 18 and 28 | FHWA international scan, 2007 |
| Bare CRCP, Netherlands practice | — | No maintenance in the first 15 years | ibid. |

Three conclusions.

1. **The differential is in the renewal cycle first.** Asphalt is resurfaced every 9-14 years;
   concrete is reconstructed or restored every 25-40 years, and often serves 60. That is a factor of
   2.5 to 4, and it is where most of concrete's whole-life advantage comes from.
2. **It is in the annual percentage second.** Rigid routine work is 0.1-0.3 per cent of capital a
   year (joint resealing, spalling, occasional slab replacement); flexible routine work is 0.25-0.6
   per cent (crack sealing, patching, surface preservation), before its resurfacing.
3. **It is in the absolute figure third, and only where the capital premium is modest.** If concrete
   costs 1.5 times as much and maintains at half the rate, its absolute upkeep is 75 per cent of
   asphalt's. If it costs 4.3 times as much, its absolute upkeep is 2.2 times asphalt's however low
   the rate. So the absolute differential is a consequence of the capital ratio, not an independent
   fact.

### 11.3 What the pakset already models through wear

`ways/concrete_road.dat` and `ways/asphalt-roads.dat` already carry the renewal differential in
`wear_capacity`, which is the traffic a way can carry before `weg_t::renew()` is triggered:

| Object | `wear_capacity` | Approximate million standard axles in the `.dat` comment | Ratio |
|---|---:|---:|---:|
| `concrete_road` | 4,000,000,000 | 60 | 6.15 against HRA heavy |
| `hr-asphalt-road-heavy` | 650,000,000 | 10 | 1.00 |
| `hr-asphalt-road-medium` | 320,000,000 | — | 0.49 |
| `hr-asphalt-road-light` | 130,000,000 | — | 0.20 |
| `sma-road-heavy` | 1,320,000,000 | — | 2.03 |
| `motorway` | 2,000,000,000 | — | 3.08 |
| `motorway-sma` | 2,630,000,000 | — | 4.05 |
| `concrete-runway` | 2,695,680,000 | — | 3.12 against the asphalt runway |
| `runway` (asphalt) | 864,000,000 | — | 1.00 |
| `concrete-taxiway` | 2,695,680,000 | — | 3.12 against the asphalt taxiway |
| `taxiway` (asphalt) | 864,000,000 | — | 1.00 |

[CODE New ex-15 @ 81ffb5911]

The road ratio of 6.15 (60 msa against 10 msa) and the air ratio of 3.12 are both inside the
measured ranges, so **the engine already models concrete's longer life**. The consequence for the
maintenance field is direct: it must carry routine upkeep only. Any overlay or resurfacing provision
placed in `maintenance=` is charged a second time, because `weg_t::renew()` will also charge the way
object's capital when the wear runs out.

The renewal cost per unit of wear shows how much of the trade-off is already there:

| Object | Capital GBP1900/km | Wear life, msa | Capital per msa | Against asphalt |
|---|---:|---:|---:|---:|
| `concrete_road` | 23,766 | 60 | 396 | 25% of HRA heavy |
| `hr-asphalt-road-heavy` | 15,844 | 10 | 1,584 | 100% |
| `concrete-runway` | 98,440 | 40 | 2,461 | 141% of the asphalt runway |
| `runway` (asphalt) | 22,757 | 13 | 1,751 | 100% |

On the roads the model gives concrete a renewal cost per unit of traffic of a quarter of asphalt's,
which is the right direction and the right order. On the runways it gives concrete 41 per cent
*more* per unit of traffic, which is the wrong direction, because the capital premium (4.33 times)
is larger than the wear advantage (3.12 times). At a capital ratio of 1.5-2.0 times, concrete's
renewal per msa would be 48-64 per cent of asphalt's, which is right.

### 11.4 Recommended maintenance rates

The rate must be a percentage of the object's own capital, because that is the only form that
survives a capital correction and preserves the ratio between the materials. All values GBP1900 per
kilometre-year.

| Object | Capital | Rate | Routine maintenance | Basis |
|---|---:|---:|---:|---|
| Bridleway, unsurfaced (3 rows) | 100 | 3.0% | 3 | No surface; grading and grips |
| MacAdam road | 833 | 1.2% | 10 | 1880 main rate less re-stoning |
| Cobblestone road | 5,000-7,000 derived | 2.0% | 100-140 | Victorian urban band, low end |
| Tar MacAdam road | 1,072 | 4.6% | 49 | 1911 tarred-slag upkeep; annual re-tarring |
| Tar MacAdam road (heavy) | 1,875 | 3.2% | 60 | As above, urban loading |
| Hot-rolled asphalt and SMA (6 rows) | 15,844 | **0.50%** | **79** | Flexible: patching, crack sealing, surface preservation |
| Concrete road | 23,766 | **0.25%** | **59** | Rigid: joint resealing, slab repair |
| City road (2 rows) | 26,406 | **0.50%** | **132** | Flexible, urban intensity |
| Motorway (2 rows) | 26,377 | **0.50%** | **132** | Bottom of the 1982 young-motorway band, £125-310 |
| Elevated roads (3 rows) | 48,000-434,082 | structure rate | 45-530 plus way upkeep | Cudworth's measured bridge upkeep |
| Grass runway | 763 | 1.3% | 10 | Mowing and rolling |
| Grass taxiway | 575 | 1.2% | 7 | As above |
| Tar MacAdam and asphalt runway | 22,757 | **0.50%** | **114** | Flexible airfield: patching, crack sealing, surface preservation |
| Tar MacAdam and asphalt taxiway | 17,161 | **0.50%** | **86** | As above |
| Concrete runway | 98,440 | **0.25%** | **246** | Rigid airfield: joint resealing, spall and slab repair |
| Concrete taxiway | 50,314 | **0.25%** | **126** | As above |

Checked against the bands: the road asphalt at 0.50 per cent plus the 1.1-1.2 per cent resurfacing
gives 1.6-1.7 per cent combined; the road concrete at 0.25 plus an overlay at 40 years (0.5 per
cent) gives 0.75 per cent. Ratio 1:2.2, inside the measured 1:2.0-2.5. The air asphalt at 0.50 plus
a 10-year overlay (1.6-2.0 per cent) gives 2.1-2.5 per cent, at the top of the published 1.6-2.4 per
cent band; the air concrete at 0.25 plus a 40-year overlay gives 0.75 per cent, inside the measured
rigid band of 0.6-1.3 per cent.

The absolute figures preserve the trade-off on the roads — concrete £59 against asphalt £79, or 75
per cent — and do not preserve it on the airfield — concrete £246 against asphalt £114, or 216 per
cent. That difference is entirely the capital defect in section 11.1. A concrete runway at 1.5 times
the asphalt's capital would cost £85/km a year at 0.25 per cent against the asphalt's £114, a clear
concrete advantage; at 2.0 times it would cost £114, equal to the asphalt; above that the concrete
costs more in absolute terms however low its rate goes, and its advantage survives only in the
renewal cycle, where the 3.12-fold wear life against a 2-fold capital premium is still 1.56 times
better per unit of traffic.

### 11.5 Are the present `.dat` percentages right?

| Object | Present `.dat` percentage | Recommended | Present as a multiple of the recommendation |
|---|---:|---:|---:|
| `concrete_road` | 1.91% | 0.25% | 7.6x too high |
| `hr-asphalt-road-heavy` | 5.54% | 0.50% | 11.1x |
| `hr-asphalt-road-medium` | 6.38% | 0.50% | 12.8x |
| `hr-asphalt-road-light` | 6.99% | 0.50% | 14.0x |
| `sma-road-heavy` | 5.04% | 0.50% | 10.1x |
| `sma-road-medium` and `-light` | 5.40% | 0.50% | 10.8x |
| `concrete-runway` | 5.96% | 0.25% | 23.8x |
| `runway` (asphalt) | 6.99% | 0.50% | 14.0x |
| `tarmac-runway` | 10.15% | 0.50% | 20.3x |
| `concrete-taxiway` | 5.46% | 0.25% | 21.8x |
| `taxiway` (asphalt) | 6.99% | 0.50% | 14.0x |

The ratios between the materials in the present data:

- **Road: concrete 1.91 per cent against asphalt 5.54-6.99 per cent, a ratio of 1:2.9-3.7.** The
  measured ratio is 1:2.0-2.5, so the direction is right and the spread is **too wide by about 1.5
  times**.
- **Air runway: concrete 5.96 against asphalt 6.99, a ratio of 1:1.17.** The measured ratio is
  1:2.0-2.5, so the direction is right and the spread is **far too narrow, by about 2 times**.
- **Air taxiway: concrete 5.46 against asphalt 6.99, a ratio of 1:1.28.** Same verdict.

And every level is between 7.6 and 24 times the routine-only rate, which is the double count
described in section 11.3: the present percentages behave as if they contained the renewal, while
the engine charges renewal again through `weg_t::renew()`.

The synthesis's per-object recommendations are better in direction and worse in consistency:

| Pair | Synthesis raw | GBP1900/km-year | As a share of capital | Ratio |
|---|---:|---:|---:|---:|
| Concrete road | 3,500 | 333 | 1.40% | 1:1.9 |
| Asphalt road heavy | 4,500 | 428 | 2.70% | 1:1.9 |
| Asphalt road medium | 3,500 | 333 | 2.10% | 1:1.5 |
| Asphalt road light | 3,000 | 285 | 1.80% | 1:1.3 |
| Concrete runway | 30,000 | 2,853 | 2.90% | 1:3.6 |
| Asphalt runway | 25,000 | 2,378 | 10.45% | 1:3.6 |

The road pair varies in absolute terms but almost not in percentage, because the concrete row is
given the same absolute figure as the medium asphalt and its lower percentage is an accident of its
higher capital. The air pair varies far too widely in percentage: the asphalt runway is set at 10.45
per cent of capital, four times the top of the combined band, and the concrete at 2.90 per cent,
above the rigid band. Neither pair is derived from a maintenance measurement; both are absolute
figures carried over from earlier drafts.

### 11.6 Does the 1.6-2.4 per cent air rule apply to both materials?

**No.** The rule is a combined maintenance-and-renewal rate, and it fits asphalt: a 10-year
resurfacing at 16-20 per cent of capital is 1.6-2.0 per cent a year, and routine work adds 0.5 per
cent, giving 2.1-2.5 per cent. Concrete's combined rate is 0.6-1.3 per cent, so applying 1.6-2.4
per cent to concrete overstates it by 1.5-2.5 times. Concrete should be 40-50 per cent of the
asphalt rate, and in the routine-only field it should be 0.25 per cent against asphalt's 0.50.

### 11.7 Summary of the answer

1. **Capital premium**: measured at +4 to +110 per cent, central +20 to +60 per cent. The road row's
   +50 per cent is in band but is not derived from a concrete rate. The air row's +333 per cent is
   not a material comparison: it mixes a PCN 10-93 midpoint with an unstated PCN, 45 m with 30.5 m,
   and a full pavement box with asphalt layers only.
2. **Maintenance differential**: in the renewal cycle first (asphalt 9-14 years, concrete 25-40), in
   the annual percentage second (rigid 0.1-0.3 per cent of capital, flexible 0.25-0.6 before
   resurfacing), and in the absolute figure third, but only where the capital premium is under about
   2 times.
3. **Renewal treatment**: the engine already models the longer concrete life through `wear_capacity`
   (60 msa against 10 on the roads, 3.12 times on the airfield), so the maintenance field must carry
   routine work only. Concrete's advantage is mainly a longer renewal cycle, and the engine's wear
   mechanism is the right place for it.
4. **Recommended rates**: 0.25 per cent of capital for concrete, 0.50 for asphalt, on both roads and
   airfield pavements; 1.2-1.3 per cent for grass; the historic rates in the table in section 11.4.
5. **The present `.dat` percentages**: directionally right on both families, too wide on the roads
   by 1.5 times, far too narrow on the airfield by 2 times, and 7.6-24 times too high in level
   everywhere. The workbook's single rate destroys the differential entirely. The 1.6-2.4 per cent
   air rule applies to asphalt only.
