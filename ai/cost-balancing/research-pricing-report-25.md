# Ship, ferry, river-boat and inland-craft prices: measured cost by type and size

**Status**: research pass 25. Draft, not reviewed, not a knowledge-base document.
**Companion rows**: `ai/temp/research-pricing-rows-25.csv` (76 rows).
**Scripts**: `ai/temp/build_ship_rows_25.py` (row set and per-ton arithmetic),
`ai/temp/fit_ship_ladder_25.py` (log-log and joint fits).

**The question.** The ship capital ladder is one flat figure, GBP 38,958 at 1900 prices
at 1909, with no size scaling, because no tonnage map exists. A Thames paddle steamer, a
cross-Channel car ferry and a coastal cargo ship therefore price the same. This pass asks
whether measured British prices carry enough tonnage to separate the types and to fit a
size exponent.

**The answer.** They do, for passenger ferries and river boats. Fourteen British
passenger vessels priced between 1924 and 1938 give

```
price (nominal GBP) = 149.7 x GT^0.900        n = 14, R2 = 0.992
```

with residuals inside +/-16 per cent. That is a usable size ladder. Cargo ships show a
flat price per gross ton and no credible size exponent. Inland craft are priced per boat
and per ton of carrying capacity, not per gross ton, and the sample is too small for an
exponent.

---

## 1. Method and evidence rules

- Every row is a measured or stated figure from a named source, with the year of the
  price. No `.dat` value was read, and nothing was fitted to the pakset.
- Tonnage is recorded in the row notes, with the computed pound-per-ton figure, because
  the agreed column set has no tonnage field.
- Where a price covers more than one vessel (the BR cargo pairs, the GUCCC motor/butty
  pairs) the price column holds the **per-vessel** figure and the note gives the
  as-stated total. This keeps the column comparable.
- Gross tonnage, deadweight tonnage and register tonnage are not interchangeable and are
  labelled in every row. The Fairplay series is deadweight; everything else here is gross
  tonnage except where stated.
- Two rows are marked **UNVERIFIED**: the Wallasey ferry *Leasowe* (the two fleet lists
  disagree on her tonnage) and *Royal Iris* (the two sources disagree on her price). Both
  are included because the disagreement is itself worth recording, and both are excluded
  from the fits.
- Three capacities are **assumptions**, not measurements: *Ilkeston* (25 tons),
  *Fulwell* (25 tons) and the per-car lane-metre conversions. The prices are measured; the
  divisors are not.

## 2. Headline: the type spread is real and large

Price per gross ton, nominal, same era:

| Type | Era | Median GBP/GT | Range | n |
|---|---|---:|---|---:|
| Mersey utility ferries | 1845-1901 | 30.6 | 21.0-42.0 | 9 |
| Cross-Channel, Irish Sea, estuarine ferries | 1927-1938 | 72.2 | 62.7-109.2 | 10 |
| River and Clyde excursion steamers | 1924-1949 | 96.4 | 71.0-210.3 | 6 |
| Ferries, all types | 1945-1960 | 185.7 | 139.7-450.2 | 13 |
| Ro-ro car ferries | 1962-1987 | 1,588.9 | 257.7-2,032.8 | 3 |
| Coastal cargo ships | 1950-1953 | 163.6 | 148.6-173.3 | 5 |
| Thames sailing barge | 1906 | 17.4 | 17.4-17.5 | 2 |
| Iron screw tug | 1882 | 39.1 | - | 1 |

The 1927-38 band is remarkably tight: ten passenger ferries from 38 to 2,910 GT, four
yards and five operators, nine of them between GBP 62.7 and GBP 77.3 per gross ton; only
the 38 GT *Ashton* (GBP 109) sits outside. That is the single strongest finding in the
pass: in the interwar years the British shipbuilding market priced a passenger hull and
its machinery at about GBP 70-80 per gross ton almost regardless of who ordered it or
where it was built.

## 3. Ferries

### 3.1 Cross-Channel and Irish Sea

| Year | Vessel | GT | Cost | GBP/GT |
|---|---|---:|---:|---:|
| 1927 | *Ben-my-Chree* (IOMSP, Cammell Laird) | 2,586 | 200,000 | 77.3 |
| 1929 | *Canterbury* (SR, Denny) | 2,910 | 220,225 | 75.7 |
| 1931 | *Princess Margaret* (LMS, Denny) | 2,523 | 179,446 | 71.1 |
| 1935 | *Slieve League* (LMS, Denny, cargo/passenger) | 1,343 | 84,163 | 62.7 |
| 1934 | *Mona's Queen III* (IOMSP, Cammell Laird) | 2,756 | 201,250 | 73.0 |
| 1946 | *Mona's Queen IV* (IOMSP) | 2,485 | 411,241 | 165.5 |
| 1950 | *Mona's Isle V* (IOMSP) | 2,495 | 570,000 | 228.5 |
| 1955 | *Manxman II* (IOMSP) | 2,495 | 847,000 | 339.5 |

The Isle of Man "Six Sisters" are a controlled experiment: same yard, same route, same
hull and machinery, 2,485-2,495 GT, built 1945-55. The price rises from GBP 411,241 to
GBP 847,000, that is 2.06 times, with no change of specification. Any ladder that fits a
trend across 1945-60 is fitting post-war inflation, not shipbuilding technology. That is
the same defect the handoff records for the bus and aircraft ladders.

The *Slieve League* row is the useful type control: a cargo hull with limited passenger
accommodation came in at GBP 62.7/GT against GBP 71-77 for the passenger ships of the
same years, so the passenger specification carried a premium of about 15-20 per cent.

### 3.2 Mersey and estuarine ferries

The Wallasey fleet list gives cost and gross tonnage for eighteen vessels from 1845 to
1958, the only long, single-operator series found.

| Year | Vessel | GT | Cost | GBP/GT |
|---|---|---:|---:|---:|
| 1845 | *Thomas Wilson* | 50 | 1,500 | 30.0 |
| 1847 | *Wallasey* [1] | 119 | 2,500 | 21.0 |
| 1879 | *Sunflower* | 345 | 7,800 | 22.6 |
| 1879 | *Daisy* | 285 | 9,100 | 31.9 |
| 1881 | *Wallasey* [2] | 459 | 11,300 | 24.6 |
| 1883 | *Violet* | 273 | 10,250 | 37.5 |
| 1885 | *Crocus* | 301 | 12,250 | 40.7 |
| 1891 | *Thistle* | 301 | 12,650 | 42.0 |
| 1901 | *Seacombe* [3] | 589 | 18,000 | 30.6 |
| 1927 | *Marlowe* | 606 | 41,602 | 68.7 |
| 1927 | *Wallasey* [3] | 606 | 42,298 | 69.8 |
| 1932 | *Royal Iris II* | 607 | 43,290 | 71.3 |
| 1934 | *Royal Daffodil II* | 591 | 44,790 | 75.8 |
| 1958 | *Royal Daffodil II* [2] | 609 | 225,000 | 369.5 |

Two cautions. First, the early "luggage boats" (GBP 21-31/GT) were slow double-ended
hulls; the fast passenger boats of the same decade (GBP 37-42/GT) cost a third to
two-thirds more. Second, the 1901 *Seacombe* is a luggage boat and reads low against the
1885-91 passenger boats: the type, not the year, explains the dip.

The 1951 *Leasowe* and *Royal Iris* rows disagree between sources: GBP 450/GT and
GBP 207/GT respectively, and the *Leasowe* tonnage is 311 in one list and 567 in the
other. They are recorded and flagged, not used.

### 3.3 British Railways' five-year programme

Moses (2010), Table 2.7, reproduces the Railway Executive's 1949-53 newbuilding
programme from The National Archives (AN13/391) with **gross tons and estimated cost on
the same line**. This is the single best table in the pass, because the type, size and
price are stated together by the buyer.

| Ordered | Route | Type | GT | Cost | GBP/GT |
|---|---|---|---|---:|---:|---:|
| 1949 | Harwich-Hook | passenger (night) | 5,000 | 855,000 | 171.0 |
| 1949 | Harwich-Zeebrugge | train ferry | 3,150 | 440,000 | 139.7 |
| 1949 | Channel Islands/France | passenger (day) | 3,700 | 650,000 | 175.7 |
| 1950 | Dover-Calais | motorcar carrier | 3,000 | 450,000 | 150.0 |
| 1950 | Associated Humber Lines | cargo, 850+1,000 GT pair | 925 | 137,500 each | 148.6 |
| 1951 | Dover-Calais | passenger (day) | 4,000 | 700,000 | 175.0 |
| 1951 | Channel Islands/France | passenger (day) | 3,500 | 650,000 | 185.7 |
| 1951 | Associated Humber Lines | cargo 1,000 GT pair | 1,000 | 150,000 each | 150.0 |
| 1952 | Channel Islands/France | cargo | 1,100 | 180,000 | 163.6 |
| 1953 | Channel Islands/France | cargo | 1,100 | 180,000 | 163.6 |
| 1953 | Holyhead-Dublin | cargo | 1,500 | 260,000 | 173.3 |

The thesis states the comparison in its own words: a typical cargo vessel cost about
GBP 150,000, a train ferry GBP 440,000, a day steamer GBP 650,000-700,000, and a 5,000-ton
night steamer with cabins GBP 855,000, "almost six times the cost of a 1,000-ton cargo
vessel".

This table separates three specifications at one date. Day steamers: GBP 175-186/GT.
Night steamer with cabins: GBP 171/GT on a larger hull. Train ferry: GBP 140/GT. Cargo:
GBP 149-173/GT. Crane-loaded car carrier: GBP 150/GT.

### 3.4 Ro-ro car ferries

| Year | Vessel | GT | Cost | GBP/GT | Cars / lane-m |
|---|---|---:|---:|---:|---|
| 1962 | *Free Enterprise* | 3,881 | 1,000,000 | 257.7 | 120 cars |
| 1984 | *Isle of Arran* | 3,296 | 6,700,000 | 2,032.8 | 55 cars |
| 1987 | *Pride of Dover* | 26,433 | 42,000,000 | 1,588.9 | 1,500 lane-m |

Per lane-metre, *Pride of Dover* is GBP 28,000 and *Isle of Arran* about GBP 24,400 on a
5 m car basis: two very different ships, two builders, three years apart, within 15 per
cent. That is a better basis for car ferries than gross tonnage, because the vehicle deck
is what the money buys. *Free Enterprise* at GBP 8,333 per car (1962) is consistent once
inflation is allowed.

## 4. River and estuary boats

| Year | Vessel | GT | Cost | GBP/GT | Note |
|---|---|---:|---:|---:|---|
| 1896 | *Southend Belle* | n/a | 28,617 | - | Thames estuary paddler; tonnage not found |
| 1901 | *TS King Edward* | 502 | 33,000 | 65.7 | Clyde turbine, 1,966 passengers |
| 1902 | *TS Queen Alexandra* | n/a | 49,000 | - | GBP 38,500 hull + GBP 10,500 turbines |
| 1924 | *PS Kingswear Castle* | 94 | 10,333 | 109.9 | River Dart |
| 1931 | *PS Jeanie Deans* | 635 | 52,650 | 82.9 | LNER, Craigendoran |
| 1933 | *TS Queen Mary* | 870 | 61,805 | 71.0 | Williamson-Buchanan |
| 1937 | *PS Ryde* | 603 | 46,800 | 77.6 | SR, Portsmouth-Ryde |
| 1945 | *PS Waverley* | 693 | 107,725 | 155.4 | Net of GBP 15,125 compensation: 92,600 |
| 1949 | *MV Balmoral* | 736 | 154,750 | 210.3 | Diesel, Red Funnel |

The Clyde excursion steamers sit inside the same GBP 70-83/GT band as the cross-Channel
ferries of the same years. The 94 GT *Kingswear Castle* at GBP 110/GT and the 38 GT
*Ashton* at GBP 109/GT show the small end running about 40-50 per cent above the band.
That is the size effect, and it is what the exponent of 0.90 encodes.

*Waverley* is worth a note: the quoted GBP 107,725 includes GBP 15,125 of Admiralty
compensation for the ship lost at Dunkirk, so the true building cost to the LNER was
about GBP 92,600, or GBP 133.6/GT. Both are recorded.

## 5. Inland and canal vessels

Inland craft are not measured by gross tonnage. They are measured by length (70-72 ft),
beam (7 ft) and carrying capacity (18-41 tons). The right denominator is therefore the
boat, or the ton of capacity, not the gross ton.

| Year | Craft | Price | Capacity | GBP/ton |
|---|---|---:|---:|---:|
| 1909 | *President*, FMC steam narrowboat | 600 | 18 t | 33.3 |
| 1912 | *Ilkeston*, FMC horse boat (one of 24) | 190 | ~25 t (assumed) | 7.6 |
| 1928 | *Otter*, Yarwood motor boat for FMC | 710 | ~25 t | 28.4 |
| 1935 | Star-class motor + butty pair (GUCCC) | 1,276 the pair | ~35-41 t | - |
| 1937 | *Fulbourne*, Town-class motor (one of 24) | 900 | 41 t | 22.0 |
| 1937 | *Fulwell*, wooden butty | 390 | ~25 t | 15.6 |
| 1923 | GJ Canal tunnel tug, complete | 1,065 | n/a | - |
| 1900 | GJ tunnel tug *Hasty*, new hull | 220 | n/a | - |
| 1922 | GJ tunnel tug *Hasty*, new hull | 420 | n/a | - |
| 1928 | GJ tunnel tug *Spider*, hull+engine+boiler | 1,031 | n/a | - |

Findings.

1. **A motor narrowboat cost GBP 700-900 in 1928-37**, and a paired butty about GBP 390.
   Two independent sources give GBP 1,275 and GBP 1,276 for a Star-class pair in 1935,
   which is a firm number.
2. **Price per ton of capacity varies more with machinery than with size**: GBP 33.3/t on
   an 18-ton steam boat, GBP 22.0/t on a 41-ton motor boat, GBP 7.6/t on an unpowered
   horse boat. The steam boat is penalised because engine and boiler take hold space; the
   horse boat has no machinery at all. Four boats cannot support a size exponent.
3. **The tunnel tugs are the only complete inland powered craft with an itemised price**:
   hull GBP 500, boiler GBP 255, engine GBP 210, own work GBP 100, total GBP 1,065 in
   1923. That itemisation is directly usable for a hull/machinery split.
4. **No working narrowboat or wide boat in the carrying trade has a published annual
   repair figure.** The Grand Junction minutes give per-job repairs only
   (GBP 1 15s 2d to GBP 17 2s 6d), and the Stroudwater ice boat repair was GBP 16 1s 5d,
   23 per cent of the boat's 1878 cost.

## 6. Coastal cargo and colliers

| Year | Vessel | GT/dwt | Cost | GBP/ton |
|---|---|---:|---:|---:|
| 1900 | Fairplay standard tramp | 7,500 dwt | 60,800 | 8.11/dwt |
| 1913 | Fairplay standard tramp | 7,500 dwt | 47,500 | 6.33/dwt |
| 1930 | Fairplay standard tramp | 7,500 dwt | 48,800 | 6.51/dwt |
| 1918 | steel coastal barge, 1,000 t cargo | 745 GT | ~19,708 | 26.5/GT |
| 1950-53 | BR coastal cargo ships | 925-1,500 GT | 137,500-260,000 | 148.6-173.3/GT |
| 1906 | *Cambria*, sailing barge | 109 GT | 1,895 | 17.4/GT |

The coastal cargo ships of 1950-53 sit at GBP 149-173/GT against GBP 171-186/GT for the
passenger steamers of the same programme. The gap is smaller than expected because a
1,500 GT coastal cargo ship still carries a crew, accommodation and a sea-going hull;
what it lacks is the passenger certificate and the speed.

**No priced British collier of 1,000-2,000 GT was found.** Fleet lists give tonnages
(the J. & C. Harrison colliers, 1,000-5,500 GT) but no prices. This is the largest single
gap in the pass.

The 1918 concrete-barge programme is a usable anchor despite being a government price:
average concrete barge GBP 27,000, stated to be 37 per cent above an equivalent steel
barge, giving GBP 19,708 for a 745 GT, 1,000-ton steel barge, or GBP 26.5/GT and
GBP 19.7 per cargo ton.

## 7. Tugs

One priced British tug was found: *Tasmania*, 81 GT, iron screw, Edward Wales of Hull,
1882, GBP 3,168, or GBP 39.1/GT.

Everything else is tonnage without price: the Gamecock and Watkins fleet lists give
dimensions, gross tonnage and engine power for dozens of London tugs (90-479 GT,
1882-1965) but no costs. The Caledon order book has a 1936 twin-screw steam tug at
GBP 22,256 with no tonnage. **A tug ladder cannot be built from this evidence.** If one
is needed, the working assumption should be a harbour tug of 150-250 GT at the small-craft
end of the ferry band, flagged as an assumption.

## 8. Repair and maintenance per gross ton

The brief asks for repair cost per gross ton by type. The honest answer is that **British
sources do not state it for ferries, coasters or inland craft**, and the existing KB file
already records that finding. What the pass adds is the arithmetic that can be done from
whole-vessel figures:

| Year | Vessel | Figure | Per GT/yr | Per cent of capital |
|---|---|---|---:|---:|
| 1913 | 50,000 GT passenger liner | GBP 30,000 overhaul | 0.60 | 2.0 |
| 1862 | 400-500 ton ship | GBP 120 sheathing | 0.24-0.30 | - |
| 1849 | any vessel, Llanelly slip | 0.5d per register ton per day | ~0.08 at 40 days | - |
| 2003 | 28,909 dwt handysize bulker | US$162,196 R&M | US$5.61/dwt | ~0.9 |

The 1913 liner is the origin of the 2 per cent rule, and it is a **large liner with a
large overhaul**, not a coaster. The 2003 bulker figure is US$5.61 per dwt per year; as a
share of capital it is about 0.9 per cent if a 2003 handysize newbuild was about
US$650/dwt, which is an assumption and not measured here. On that assumption the repair
share of capital roughly halved between 1913 and 2003, consistent with the sevenfold real
fall recorded in the KB.

Three consequences for the pakset.

1. **2 per cent of capital is defensible as a fleet-wide average and wrong as a
   per-type rule.** The 1913 figure is one large liner; a small ferry or a narrowboat
   spends a larger share of its capital on hull upkeep and a smaller share on machinery.
2. **Repair cost scales less than linearly with size.** The 1862 sheathing figure
   (GBP 0.24-0.30/ton) and the 1913 overhaul (GBP 0.60/GT) differ by 2-2.5 times, but the
   ships differ by 100 times in tonnage. If a maintenance exponent is wanted, about 0.85,
   matching the capital exponent, is the only defensible guess; it rests on two points and
   should be flagged as an inference, not a measurement.
3. **No measured per-GT repair rate exists for any inland craft.** The per-job figures
   (GBP 1-17 for tunnel tugs, GBP 16 for the ice boat, GBP 600/year for a modern
   narrowboat) are all that is available.

## 9. Recommended ladders

All figures are **nominal GBP at the stated year**. The pakset's own `vehicle purchase`
index must do the deflation; none of these numbers has been converted here.

### 9.1 Passenger ferries and river boats (the main result)

```
price = 150 x GT^0.90     (nominal GBP at the 1931 sample midpoint; +/- 16 per cent,
                          n = 14, R2 = 0.992)
```

Recommended: exponent **0.90**, band **0.82-0.93**, anchored per operator type. The point
estimates cluster tightly: 0.897 (1924-38, n=14), 0.881 (1945-60, n=13), 0.931 (pooled
1924-60, n=27), with 0.817 in the small 1949-51 BR sub-sample. If large ferries come out
too cheap, 0.85 is the conservative alternative.

| Type | Anchor | Per GT at anchor | Exponent |
|---|---|---:|---:|
| River/estuary paddle or turbine steamer | 1931 | 77 | 0.90 |
| Cross-Channel / Irish Sea passenger ferry | 1931 | 73 | 0.90 |
| Mersey-type utility ferry | 1931 | 71 | 0.90 |
| Small ferry or launch (<100 GT) | 1935 | 109 | 0.90 |
| Ro-ro car ferry | 1987 | 1,589 | 0.80 (3 points only) |

Worked check against the fit: 100 GT predicts GBP 9,464; *Kingswear Castle* (94 GT) cost
GBP 10,333. 2,500 GT predicts GBP 171,500; *Princess Margaret* (2,523 GT) cost
GBP 179,446. 3,000 GT predicts GBP 202,100; *Canterbury* (2,910 GT) cost GBP 220,225.
The fit runs 4-11 per cent low at the top of the 1927-38 range, which is one reason the
exponent is recommended at 0.90 rather than lower.

### 9.2 Cargo ships

No size exponent. Price per gross ton is flat at **GBP 149-173/GT (1950-53)** for
925-1,500 GT, and the Fairplay tramp is **GBP 6.3-8.1 per deadweight ton (1898-1930)**.
Use a constant per ton for cargo, with the deadweight-to-gross ratio stated if the
Fairplay rate is applied to a gross-ton figure (roughly 0.55-0.65 gross per deadweight
ton for a dry cargo ship of the period).

### 9.3 Inland craft

Price per boat, not per ton:

| Class | Nominal price (year) |
|---|---:|
| Motor narrowboat, 70-72 ft | GBP 900 (1937) |
| Unpowered butty | GBP 390 (1937) |
| Motor + butty pair | GBP 1,275-1,276 (1935) |
| Canal tunnel tug, complete | GBP 1,065 (1923) |
| Sailing barge, 109 GT | GBP 1,895 (1906) |

If a per-ton basis is needed: **GBP 22/ton of capacity** for a motor narrowboat,
**GBP 7-8/ton** for a horse boat, **GBP 11/ton** for a sailing barge.

### 9.4 Tugs and small craft

No ladder. One point: GBP 39/GT (1882, 81 GT). Flag any tug price as an assumption.

## 10. Confidence

| Finding | Confidence | Basis |
|---|---|---|
| Passenger ferries price at ~GBP 70-80/GT in 1927-38 | High | 10 rows, 4 yards, 5 operators, +/-16 per cent |
| Size exponent 0.90 for passenger vessels | High | R2 0.99, n=14; 0.88 (1945-60) and 0.93 (pooled) agree; 0.82 in the 1949-51 BR group |
| Cargo ships flat per GT | Medium | 5 rows, one buyer, 1949-53 only |
| Post-1945 GBP/GT by year | Medium | Good rows, but nominal inflation dominates and the sample is thin |
| Inland narrowboat GBP 700-900 (1928-37) | High | Three independent sources, two of them contract prices for 24 boats |
| Inland per-ton rates | Low | Capacities are partly assumed |
| Tugs | Very low | One row |
| Maintenance per GT by type | Low | Derived from four whole-vessel figures, none British for ferries or coasters |

## 11. Dead ends, recorded so they are not repeated

- **Lloyd's Register**: the volumes give tonnage but are not a price source, and the
  digitised runs are not searchable by cost.
- **Denny cost books** (Glasgow University UGD 3/5): catalogued, not digitised. This is
  the archive that would settle the Clyde ladder, and it needs a visit.
- **Caledon order book** (Dundee GD324): already transcribed for pass 2; tonnage survives
  for only three priced hulls, so no per-ton figure can be built from it alone.
- **Chamber of Shipping returns**: no accessible per-type repair or price series found.
- **The National Archives Discovery catalogue**: returns catalogue descriptions
  (for example the Hawthorn Leslie launch list, DS.HL/4/47) but no figures.
- **P&O and Cunard repair ledgers**: archival, no published series (already in
  `ship-maintenance.md`).
- **Grace's Guide Clyde steamer list**: names, builders and machinery makers, no prices.
- **Colliers**: fleet lists (J. & C. Harrison and others) give 1,000-5,500 GT tonnages but
  no prices. Repeated searches returned no priced collier.
- **Tugs**: fleet lists give tonnage and power but no price; only one price found.
- ***Southend Belle*** (1896, GBP 28,617) and ***Queen Alexandra*** (1902, GBP 49,000):
  prices found, tonnages not found, so neither can enter the per-ton ladder.
- **1929 *Canterbury***: the tonnage was initially unverified; confirmed at 2,910 GRT
  from the Wikipedia article citing Scottish Built Ships, after the first draft.

## 12. The gaps that matter most

1. **1902-1923 has no priced ferry with a tonnage.** The ladder jumps from *King Edward*
   (1901) to *Kingswear Castle* (1924). Twenty-two years of the most important
   shipbuilding era in British history are empty. The Caledon 1911 paddle ferry
   (GBP 9,450) is the only contract in the gap and its tonnage is lost.
2. **No collier price, 1890-1939.** The type that carried most British coastal coal has
   no measured capital cost at all.
3. **One tug price, from 1882.** Tugs are a large part of the pakset's water fleet.
4. **No ferry price between 1962 and 1984**, and only two after 1962.
5. **No per-GT repair figure for any ferry, coaster or inland craft.** The 2 per cent
   rule rests on a single 1913 liner.
6. **No wide-beam or barge price in the carrying trade.** The sailing barge (*Cambria*)
   and the tunnel tugs are the nearest, and neither is a canal carrying barge.

## 13. What would close them

- **Glasgow University, Denny papers UGD 3/5**: cost books and contract envelopes for
  several hundred Clyde hulls, 1860-1960. A sample of twenty with tonnage would fit the
  1902-23 gap and give the Clyde ladder directly.
- **Lloyd's Register 1900-1939**, matched by name to the Caledon and Denny contracts,
  would attach tonnage to the 66 priced Caledon hulls that lack it.
- **The Railway Executive's five-year programme file, TNA AN13/391**, is cited by Moses
  and may contain later programmes (1955-65) with the same type/tonnage/cost structure.
- **A single collier order book** (for example William Gray, Hartlepool, or the
  Sunderland yards) would give the coastal cargo ladder.
- **Alexandra Towing or William Watkins** records for tug prices; the fleet lists already
  give the tonnages, so only the prices are missing.
