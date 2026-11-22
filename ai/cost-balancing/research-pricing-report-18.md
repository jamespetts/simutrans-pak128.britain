# Research pass 18 — measured British road and canal tunnel sections

Status: draft evidence. Compiled 2026-11-22. Output for the parent session; the knowledge base is
not edited here.

Purpose: replace the stated rectangular sections used for canal, road and power tunnels in
`measured_infra.py` (`tunnel_rate`: road 40 m2, water 16 m2, power 4 m2) with measured British
sections, so that the 1905 rule `cost per metre = GBP 3.7 x area` rests on a real bore rather than
an assumption.

## 1. Method, and the difference between an excavation and a waterway

The sources almost never state a cross-section area. They state a width and a height, and the two
are not always the same quantity:

- **Excavation envelope.** The 19th-century engineering tables quote the ground excavated: width
  at the widest point and full height from invert to crown. This is the quantity that scales the
  cost, and it is what the table in §2 mainly uses.
- **Finished waterway.** Modern canal guides quote the navigable width and headroom, which are
  smaller (Braunston, for example, is 4.8 m x 3.76 m finished against a 16 ft x 18 ft excavation
  elsewhere in the same period).

Areas are derived as a **rectangle** (W x H) unless stated, because that is how the period cost
tables pair the two numbers with a cost per yard. An arched section is smaller. For a semicircular
crown of diameter W springing at height H - W/2:

```
A = W (H - W/2) + pi W^2 / 8
```

This is 8-10 per cent below the rectangle for the canal sections here (Harecastle 18.86 against
20.81 m2; Foulridge 25.55 against 28.43 m2). The rectangle is therefore a slight upper bound; the
conclusions do not turn on the choice.

## 2. Canal tunnels by size class

| Tunnel | Canal | Year | Class | Width | Height | Area (m2) | Basis | Source |
|---|---|---|---:|---|---:|---:|---|---|
| Harecastle (Brindley) | Trent & Mersey | 1777 | narrowboat, single, legged | 9 ft (2.743 m) | 12 ft (3.658 m) | **10.03** | excavation | Wikipedia; Grace's Guide |
| Standedge | Huddersfield Narrow | 1811 | narrowboat, single, legged | 9 ft (2.743 m) | 17 ft (5.182 m) | **14.21** | excavation | Historic England list entry |
| Braunston | Grand Union | 1796 | narrowboat, two-way | 4.8 m | 3.76 m | **18.05** | finished waterway | Wikipedia; Engineering Timelines |
| Harecastle (Telford) | Trent & Mersey | 1827 | narrowboat, single, towpath | 14 ft (4.267 m) | 16 ft (4.877 m) | **20.81** | as built | Telford's report via Grace's Guide |
| Blisworth | Grand Union | 1805 | narrowboat, two-way | 16 ft 1 in (4.902 m) | 18 ft (5.486 m) | **26.89** | excavation | ETH table |
| Netherton | Birmingham Canal Nav. | 1858 | narrowboat, two-way, two towpaths | 27 ft (8.230 m) | 16 ft (4.877 m) | **40.13** | overall width | Wikipedia; Walker, ICE 1860 |
| Foulridge | Leeds & Liverpool | 1796 | broad, 14 ft beam | 17 ft (5.182 m) | 13 ft (3.962 m) | **20.53** finished / **28.43** excavation | both stated | Leeds Intelligencer, 9 May 1796 |
| Shropshire Canal (Snedshill, Stirchley) | Shropshire | 1792 | tub-boat | 10 ft (3.048 m) | 13 ft (3.962 m) | **12.08** | waterway | Wikipedia; Morriss 1991 |
| Berwick | Shrewsbury | 1797 | tub-boat | 10 ft (3.048 m) | not published | **12.08** (assumed 13 ft) | waterway | Wikipedia; Shropshire HER |
| Strood | Thames & Medway | 1824 | broad, towpath | 22 ft 6 in (6.858 m) | 39 ft 8 in (12.09 m) | **82.92** (doubtful) | table | ETH table |

Reading the canal sizes:

- **Narrowboat tunnels (7 ft beam)** run from 10.0 m2 (Brindley's Harecastle, the tightest) to
  40.1 m2 (Netherton, which is wide because it carries two towpaths). The central and best-evidenced
  group is **14-16 ft wide by 16-18 ft high, 20-27 m2**. Harecastle Telford at 20.81 m2 is the
  cleanest single figure: Telford's own dimensions, a single boat, a towpath, and a known cost.
- **Barge / broad-beam tunnels (14 ft beam)** are about **17 ft x 18 ft excavation, 28.4 m2**, with
  a finished waterway of 17 ft x 13 ft. Foulridge is the only broad tunnel with both dimensions
  published. Gannow (559 yd, Burnley) is the other well-known broad tunnel, but its dimensions are
  not published (dead end).
- **Tub-boat tunnels** are **10 ft x 13 ft, 12.1 m2**, a genuine class of their own, on the
  Shropshire and Shrewsbury canals. The boats were 5 ft 2 in to 6 ft 4 in beam, not 7 ft.

Corrections to the brief's examples:

- **Standedge is a narrowboat tunnel, not a barge tunnel.** It is 9 ft wide and 17 ft high, and only
  one narrowboat fits. The BW 2002 width survey found under 7 ft clear at water level in places near
  Marsden. There is no separate "Marsden canal tunnel": Marsden is the western portal of Standedge,
  and the Marsden *railway* tunnels (1848, 1871, 1894) run alongside it.
- **Gannow** is broad but unpublished; **Foulridge** is the usable broad-beam measurement.

## 3. Road tunnels by class

| Tunnel | Year | Lanes / bores | Width | Height | Area (m2) | Source |
|---|---:|---|---:|---:|---:|---|
| Queensway, Liverpool | 1934 | 4 lanes, one circular bore | not published | 3.9 m nearside / 4.75 m offside | — | Wikipedia; Grace's Guide |
| Kingsway, Liverpool | 1971 | twin bores, 2 x 12 ft lanes each | 7.32 m carriageway; bore not published | not published | — | Wikipedia |
| Dartford, west bore | 1963 | 2 lanes, one bore | 8.53 m diameter | 8.53 m | **57.20** | Wikipedia |
| Tyne, first bore | 1967 | 2 lanes, one bore | 9.53 m diameter; 7.32 m roadbed | 9.53 m | **71.26** | Wikipedia |
| Tyne, second bore | 2011 | 2 lanes, immersed tube | not published | not published | — | Wikipedia |
| Hindhead, each bore | 2011 | 2 lanes per bore, dual carriageway | 11.6 m excavated | 11.6 m | **84.55** (horseshoe) | Wikipedia |
| Conwy, A55 | 1991 | 2 tubes, 2 lanes each, one monolith | 24.1 m overall | 10.4 m overall | ~125 per tube gross | ITA-AITES case 115 |
| Limehouse Link | 1993 | twin cut-and-cover | not published | not published | — | Wikipedia |

**Design standard, two-lane single carriageway.** PIARC's cross-section working group gives, for a
bi-directional two-lane tunnel: minimum 8.50 m total travel width (2 x 3.50 m lanes + 0.75 m hard
clearance each side), **9.70 m between walls with 0.60 m walkways**, and 13.20 m recommended. The UK
lane is 3.65 m and the UK two-lane carriageway 7.30 m (DMRB TD 27). A UK two-lane tunnel therefore
has an internal width of about 9.7 m and a maintained headroom of about 5.0-5.3 m: **a box section
of about 50 m2**, or **57-71 m2 if bored as a circle**, because a circle large enough to give 9.7 m
at road level carries unusable area above the springing.

**Dual carriageway.** The measured standard is one bore per carriageway, 11.6 m excavated at
Hindhead, giving about 85 m2 per bore; Conwy carries both carriageways in a 24.1 m x 10.4 m
immersed element, about 125 m2 gross per tube including the central wall and roof.

## 4. Cost per metre found, and the GBP 3.7/m2 check

Nominal money, no deflation applied. The last column is the price-index ratio needed to bring the
measured rate up to the rule's GBP 3.70/m2; if the parent's `infrastructure` series ratio between
the tunnel year and 1905 equals that number, the rule reproduces the tunnel.

| Tunnel | Year | Cost as stated | GBP/m | Area (m2) | GBP/m2 | Ratio to reach 3.70 |
|---|---:|---|---:|---:|---:|---:|
| Blisworth | 1805 | GBP 13/yd | 14.22 | 26.89 | 0.53 | 7.00 |
| Foulridge | 1796 | GBP 24/yd; GBP 40,000 total | 26.25 / 26.84 | 28.43 | 0.92 | 4.01 |
| Harecastle (Telford) | 1827 | GBP 40/yd; GBP 113,000 total | 43.74 / 42.23 | 20.81 | 2.03 | 1.82 |
| Standedge | 1811 | GBP 160,000 | 30.83 | 14.21 | 2.17 | 1.71 |
| Netherton | 1858 | GBP 302,000 | 109.10 | 40.13 | 2.72 | **1.36** |
| Strood | 1824 | GBP 32/yd | 35.00 | 82.92 | 0.42 | 8.77 |
| Dartford (west) | 1963 | GBP 13m project | 9,091 | 57.20 | 159 | 0.023 |
| Hindhead (per bore) | 2011 | GBP 155,000/m twin | 77,500 | 84.55 | 917 | 0.004 |

Findings:

1. **Two independent sources agree on two of the canal costs.** Foulridge's GBP 24/yd and its
   GBP 40,000 total agree within 2 per cent; Harecastle's GBP 40/yd and GBP 113,000 agree within
   4 per cent. The ETH table is therefore a reliable compilation, not a stray figure.
2. **The rule is consistent with Netherton, the latest and most heavily lined canal tunnel.** At
   GBP 2.72/m2 nominal in 1858, the rule's GBP 3.70 is reached with a price ratio of 1.36 between
   1858 and 1905 — entirely plausible, and the parent's infrastructure series can confirm it
   exactly. This is the strongest available validation of the rule outside rail.
3. **The rule overstates the early, cheap tunnels.** Blisworth, Foulridge and Strood come in at
   GBP 0.42-0.92/m2 and would need implausible ratios of 4-9 to reach the rule. They were built
   before the fully lined, towpathed, brick-arch section that the 1858 tunnel represents. This is a
   real spread in the data, not a measurement error: the period table itself shows a 4.5-fold range
   in cost per yard for the same 14 ft x 18 ft section (Comptich GBP 36, Charleroy GBP 52,
   Harecastle GBP 40) because ground conditions dominate.
4. **The rule does not transfer to road tunnels at all.** Even the cheapest modern-era measurement,
   Dartford 1963 at GBP 159/m2 nominal, is 43 times the rule's rate before any deflation; Hindhead
   is about 250 times. Road tunnels carry ventilation, lighting, finishes, walkways, fire safety and
   much larger spans, none of which the 1905 shield-tunnel rule contains. Applying GBP 3.7 x 50 m2 =
   GBP 185/m to a two-lane road tunnel in 1905 would price a road tunnel below a canal tunnel of the
   same bore.

The correct reading: the rule is a **bore-excavation-and-lining** rate calibrated on shield-driven
rail tunnels. It is usable for canal tunnels and for the structural bore of a road tunnel, but a
road tunnel object priced with it alone will be an order of magnitude cheap against every measured
British road tunnel.

## 5. Recommended section for each pakset tunnel family

Important mapping point found while checking the constraints. In `New/ways/tunnels.dat`:

- `CanalTunnel` has `way_constraint_prohibitive[2]=2` (barge). Barges are excluded, narrowboats are
  not. **It is the narrowboat tunnel.**
- `CanalTunnelNarrow` has `way_constraint_prohibitive[4]=4` (narrow). Narrowboats are excluded. It
  is therefore the **tub-boat tunnel**, despite the name, and matches `CanalNarrow` /
  `CanalTub` on the way side.
- **There is no barge-sized canal tunnel object.** If the parent's brief assumes `CanalTunnel` is the
  barge tunnel, that is a mismatch worth resolving before the price is set.

| Pakset object | Measured analogue | Section to use | Area | Rule cost @1905 | Confidence |
|---|---|---|---:|---:|---|
| `CanalTunnel` (narrowboat) | Harecastle Telford | 4.27 m x 4.88 m | **20.8 m2** | GBP 77/m | High |
| `CanalTunnelNarrow` (tub-boat) | Shropshire Canal | 3.05 m x 3.96 m | **12.1 m2** | GBP 45/m | Medium-high |
| (barge tunnel, if added) | Foulridge | 5.18 m x 5.49 m | **28.4 m2** | GBP 105/m | High |
| `RoadTunnelBrick` (1900+) | PIARC + Dartford/Tyne | 9.7 m x 5.3 m box | **51.4 m2** | GBP 190/m | High for the standard |
| `RoadTunnelConcrete` (1960+) | Tyne / Dartford | 9.53 m circle | **71.3 m2** | GBP 264/m | High |
| `RoadTunnelConcrete`, dual carriageway variant | Hindhead | 11.6 m horseshoe per bore | **84.6 m2** | GBP 313/m | High |
| `RoadTunnelStone` (pre-1900) | none measured | — | — | — | None — dead end |
| power / cable tunnel (4 m2, out of brief) | none sought | unchanged | 4.0 m2 | GBP 15/m | Unchanged |

Effect against the present code: canal narrowboat tunnels rise from 16 to 20.8 m2 (+30 per cent),
tub-boat tunnels fall from 16 to 12.1 m2 (-24 per cent), and road tunnels rise from 40 to 51.4 m2
(+29 per cent) for a two-lane box, or to 71.3 m2 (+78 per cent) if the bore is modelled as a circle.

Recommendation on the road family: use **51.4 m2** for the brick and concrete road tunnels, because
it is the design-standard internal section and is directly derived from PIARC plus the UK lane
width; use 71.3 m2 only if the object is meant to represent a bored circular bore. Do **not** apply
the rule's output as the road tunnel's whole cost without a road multiplier: the measured road
evidence is 40-250 times the rule per m2.

## 6. Confidence

- **High:** Harecastle Telford (Telford's own report, corroborated by the period cost table at
  4 per cent); Foulridge (contemporary newspaper plus two agreeing costs); Netherton (Wikipedia,
  the 1860 ICE paper and the 1858 overspend all consistent); Dartford and Tyne diameters; PIARC
  design widths; UK lane widths.
- **Medium-high:** Shropshire Canal tub-boat section (a measured waterway width and height from a
  cited secondary source); Braunston (published finished dimensions, a different quantity from the
  excavation figures).
- **Medium:** Berwick (width measured, height assumed equal to the Shropshire tunnels).
- **Low / not usable:** Strood (the 39 ft 8 in second dimension is probably not a height); Queensway,
  Kingsway, Tyne 2, Limehouse and Conwy internal sections (not published); `RoadTunnelStone`.

## 7. Dead ends and corrections

- **Hatton Hill road tunnel**: no British road tunnel of this name with published dimensions was
  found in the sources searched. Not used.
- **A55 "Colwyn Bay tunnels"**: the Colwyn Bay bypass (1984-85) has no tunnel. The A55 tunnels are
  Conwy (1991, immersed tube, dimensions found), Penmaenbach (1932, rebuilt 1989) and Pen-y-Clip
  (1935, rebuilt 1993). Penmaenbach and Pen-y-Clip dimensions were not found.
- **Gannow Tunnel** (Leeds & Liverpool, 559 yd, broad): length confirmed, dimensions not published.
- **Marsden**: not a separate canal tunnel; it is the Standedge portal, and the Marsden railway
  tunnels are a different group.
- **Queensway bore diameter**: the bore is circular cast iron (100,000+ segments), four lanes, but
  no diameter is published in the sources read. Height restrictions only.
- **Kingsway, Tyne 2, Limehouse Link**: lane counts and costs found, cross-sections not published.
- **Road tunnels before 1900**: no measured British example with a published section was found.
  `RoadTunnelStone` cannot be given a measured section from this pass.
- **Canal tunnel costs after 1858**: Netherton is the last British canal tunnel of the canal age, so
  no canal tunnel cost exists near 1905. Any 1905-rule canal figure is an extrapolation of a
  47-year-old price basis, which is exactly why the Netherton check in §4 matters.
- **Not done**: no attempt to deflate the 19th-century costs; that needs the `infrastructure` series
  in `config/prices.tab`, which the parent session holds. The implied ratios in §4 are the test.

## 8. Sources

- Grace's Guide, *Harecastle Tunnel* (Telford's dimensions and cost, from the obituary of James
  Potter): https://www.gracesguide.co.uk/Harecastle_Tunnel
- Wikipedia, *Harecastle Tunnel* (Brindley 9 ft x 12 ft; Telford GBP 113,000):
  https://en.wikipedia.org/wiki/Harecastle_Tunnel
- E-rara / ETH, *River and inland navigation*, table of tunnels (Blisworth, Foulridge, Strood,
  Harecastle, Kilsby, and continental tunnels, with width x height and cost per yard):
  https://www.e-rara.ch/zut/content/pagetext/21154933
- Wikipedia, *Braunston Tunnel* (4.8 m x 3.76 m): https://en.wikipedia.org/wiki/Braunston_Tunnel
- Wikipedia, *Blisworth Tunnel*: https://en.wikipedia.org/wiki/Blisworth_Tunnel
- Wikipedia, *Netherton Tunnel Branch Canal* (27 ft x 16 ft; GBP 302,000; Walker's 1860 ICE paper):
  https://en.wikipedia.org/wiki/Netherton_Tunnel_Branch_Canal
- Wikipedia, *Standedge Tunnels*: https://en.wikipedia.org/wiki/Standedge_Tunnels
- Heritage Gateway, West Yorkshire HER MWY7873, Standedge portal ("3 yards wide and 17 feet high"):
  https://historicengland.org.uk/listing/heritage-gateway/results/record/c08bded6-08f6-4d13-8699-29c79effb01d/MWY7873
- Grace's Guide, *Foulridge Tunnel* (Leeds Intelligencer, 9 May 1796: 1,630 yd, 13 ft high,
  17 ft wide): https://www.gracesguide.co.uk/Foulridge_Tunnel
- Wikipedia, *Leeds and Liverpool Canal* (Foulridge GBP 40,000; Gannow 559 yd):
  https://en.wikipedia.org/wiki/Leeds_and_Liverpool_Canal
- Wikipedia, *Shropshire Canal* (tunnels 10 ft wide, 13 ft high; boats 5 ft 2 in):
  https://en.wikipedia.org/wiki/Shropshire_Canal
- Wikipedia, *Berwick Tunnel*; Shropshire HER via Heritage Gateway; Shrewsbury & Newport Canals Trust:
  https://en.wikipedia.org/wiki/Berwick_Tunnel
- Wikipedia, *Dartford Crossing* (two-lane bore 28 ft / 8.6 m; GBP 13m):
  https://en.wikipedia.org/wiki/Dartford_Crossing
- Wikipedia, *Tyne Tunnel* (31 ft 3 in diameter, 24 ft roadbed; GBP 139m):
  https://en.wikipedia.org/wiki/Tyne_Tunnel
- Wikipedia, *Hindhead Tunnel* (11.6 m excavated; GBP 155,000/m; GBP 371m):
  https://en.wikipedia.org/wiki/Hindhead_Tunnel
- Wikipedia, *Queensway Tunnel* and Grace's Guide, *Queensway Tunnel* (four lanes, heights, GBP 8m):
  https://en.wikipedia.org/wiki/Queensway_Tunnel
- Wikipedia, *Kingsway Tunnel* (twin bores, two 12 ft lanes each):
  https://en.wikipedia.org/wiki/Kingsway_Tunnel
- Wikipedia, *Limehouse Link tunnel* (twin cut-and-cover, GBP 293m):
  https://en.wikipedia.org/wiki/Limehouse_Link_tunnel
- ITA-AITES case record 115, *Conwy Tunnel* (element 24.1 m x 10.4 m, two tubes two lanes each):
  https://cases.ita-aites.org/search-the-database/project/115-conwy-tunnel
- CIHT Motorway Archive, *A55 North Wales Coast Road* (Conwy contract GBP 102m, settled GBP 144m):
  https://ukmotorwayarchive.ciht.org.uk/motorways-by-region/a55/
- PIARC, *Cross section design for uni- and bi-directional road tunnels* (table: 9.70 m minimum
  with walkways, 13.20 m recommended, 8.50 m minimum travel width):
  https://proceedings-durban2003.piarc.org/en/pdf/doc_pdf/communications/C5fp-Rigter-e.pdf
- National Highways, DMRB CD 352 *Design of road tunnels* (scope and geometric design; no section
  table in the parts read): https://www.standardsforhighways.co.uk/tses/attachments/b4618cc3-c639-44d5-b031-ecbc255b599f
- PIARC table 5-1 reproducing UK TD 27 lane 3.65 m and carriageway 7.30 m:
  https://tunnelsmanual.piarc.org/files/tunnelsmanual/wysiwyg/import/Chapters%20PIARC%20reports/2001%2005.11.B%20Chap%205%20EN.pdf
