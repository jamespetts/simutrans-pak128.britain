---
status: draft
verified: New ex-15 @ fcd40c0bc + passes 62-65 (working tree), 2026-11-25; simutrans-extended ex-15 @ bdfdc8311
---
# Vehicle cost evidence

**Covers**: the measured purchase, build and maintenance costs of British transport vehicles, by
class and era, and what those figures can and cannot support when the pakset's vehicle costs are
re-examined.

Method: [vehicle-cost-method](vehicle-cost-method.md). Engine mechanics:
[vehicle-cost-model](vehicle-cost-model.md). Index series: [prices-config](prices-config.md).
This doc is evidence and analysis only. No `.dat` value has been changed, and none should be
until every cost domain has reached this depth. `[USER-DIRECTION:2026-11-16]`

## The evidence base

| Document | Read when | Contents |
|---|---|---|
| [forum-prices-part-1](vehicle-cost/forum-prices-part-1.md) | you need a purchase price for a specific class or era | 208 rows from forum thread 6521, rows 1-208 |
| [forum-prices-part-2](vehicle-cost/forum-prices-part-2.md) | as above, later classes | 208 rows from the same thread, rows 209-416 |
| [published-capital](vehicle-cost/published-capital.md) | you need a price with a specification attached | 81 figures from company records, builder records, technical press and official returns, each with the specification the source states |
| [published-maintenance](vehicle-cost/published-maintenance.md) | you need a repair or running cost figure | 53 figures, each with its inclusion and exclusion stated |
| [index-sources-purchase-a](vehicle-cost/index-sources-purchase-a.md) | you are auditing the `vehicle purchase` series, 1988 onwards | ONi D7CO, L544 and DOCi, and Feinstein's railway rolling stock column, with annual values |
| [index-sources-purchase-b](vehicle-cost/index-sources-purchase-b.md) | as above, earlier and rejected series | Feinstein's ships, plant and machinery and capital goods columns, the iefton and Weale values, and the series checked and rejected |
| [index-sources-maintenance](vehicle-cost/index-sources-maintenance.md) | you are reconsidering the maintenance fallback | the repair and maintenance series available, with annual values, and why none carries the 1750-1987 span |
| [deflator-search](vehicle-cost/deflator-search.md) | you are questioning whether a published vehicle deflator exists | the search across national accounts vintages, and the alternatives tested and rejected |
| [deflator-series](vehicle-cost/deflator-series.md) | you are auditing the 1938-1997 block of the series | the Blue Book current and constant price series and the Feinstein bridge, with annual values |
| [base-maintenance](vehicle-cost/base-maintenance.md) | you need a maintenance level in engine units | the converted per-kilometre and per-vehicle-year figures, the maintenance-to-capital ratio, and the field mapping |
| [aircraft-maintenance](vehicle-cost/aircraft-maintenance.md) | you need an aircraft maintenance cost | British operator engineering cost per flying hour 1969-73, IATA benchmarks, check intervals |
| [road-maintenance-1959-2016](vehicle-cost/road-maintenance-1959-2016.md) | you need a road vehicle maintenance figure after 1958 | Commercial Motor tables 1963-74, Merseyside 1983, FTA 2016 |
| [research-pricing-report-28](cost-balancing/research-pricing-report-28.md) | you need a stage coach, mail coach, omnibus or hackney price or repair figure | 26 rows, 1750-1901; Felton's 1796 price list, Hanforth's 1760s accounts |
| [research-pricing-report-29](cost-balancing/research-pricing-report-29.md) | you need a bus or coach price, or the maker comparison | 72 rows, 1909-55; Salford 1928 tender, Daimler list 1930, chassis/body split |
| [research-pricing-report-30](cost-balancing/research-pricing-report-30.md) | you need a lorry or van price | 129 rows, 1919-61; the 1960 ten-make list, £/ton analysis, steam wagons |
| [research-pricing-report-31](cost-balancing/research-pricing-report-31.md) | you need a road maintenance figure before 1959, or the maintenance-to-capital ratio | 68 rows; Edinburgh 1925 and Glasgow 1931-34 accounts, size scaling, 12-21 per cent share |
| [research-pricing-report-32](cost-balancing/research-pricing-report-32.md) | you need a modern (1980-2026) road vehicle price | 59 rows; TfL and council tender awards, ZEBRA, dealer price lists, the electrification premium |
| [research-pricing-report-33](cost-balancing/research-pricing-report-33.md) | you need an articulated tractor unit or semi-trailer price | 41 rows, 1933-2026; Scammell mechanical horses to 44 t Volvo, tractor:trailer split |
| [research-pricing-report-34](cost-balancing/research-pricing-report-34.md) | you need a battery-electric road vehicle price | 64 rows, 2019-26; the electric premium by class |
| [research-pricing-report-35](cost-balancing/research-pricing-report-35.md) | you need a modern tram or light rail price or maintenance figure | 28 rows; every UK order 1994-2019, Nottingham maintenance contract, 1901-50 car prices |
| [research-pricing-report-36](cost-balancing/research-pricing-report-36.md) | you need a rail overhaul interval, overhaul cost or rebuild cost | 81 rows; BR general repair mileages, GWR 28xx heavy general, Class 47-to-57 rebuild |
| [research-pricing-report-37](cost-balancing/research-pricing-report-37.md) | you need a road, tram, ship or aircraft overhaul or rebuild cost | 92 rows; Aldenham bus overhauls, lorry engine cycles, Metrolink and Supertram refits, drydocking, C and D checks |
| [research-pricing-report-38](cost-balancing/research-pricing-report-38.md) | you need a price that the pakset's own `.dat` comments record | 43 new prices, 1911-2015, parsed from the comments; duplicates excluded |
| [research-pricing-report-42](cost-balancing/research-pricing-report-42.md) | you need a lorry overhaul cost, interval or the overhaul share of lorry maintenance | 20 Commercial Motor and trade sources read; the 1938, 1949 and 1955 itemised compositions (46, 53, 44 per cent); invoices 1933-2023; four era bands |
| [research-pricing-report-43](cost-balancing/research-pricing-report-43.md) | you need a modern carriage or wagon maintenance level, or the wagon:carriage ratio | Beeching 1961 (£1,012 a coach-year, £54.3 a wagon-year), Serpell 1982, HST 1984, ORR 2024-25; the carriage series (later re-based at 1920 and 1950 by report 51) and the ratio-declining wagon ladder |
| [research-pricing-report-44](cost-balancing/research-pricing-report-44.md) | you need a carriage works-overhaul interval, or the overhaul's share of the annual maintenance total | Lacy & Dow £62 (1860s, 1.84 A) and the 1982 York Works Mk 1 overhaul (0.16 A); GWR 1935 heavy repairs; Hansard 1996; the era table now in the workbook |
| [research-pricing-report-45](cost-balancing/research-pricing-report-45.md) | you need a multiple-unit maintenance level or overhaul share | Beeching 1961, Serpell 1982, RDG 2013, ORR 2026, LU per car-year; the 66-780 GBP ladder and the eight-year C6 cycle |
| [research-pricing-report-46](cost-balancing/research-pricing-report-46.md) | you need a locomotive maintenance level | the 215 / 306 / 800 / 2,100 / 1,045 / 520 GBP ladder at 1900-2020; the 1892 nineteen-company average and the Class 47 seven-year cycle |
| [research-pricing-report-47](cost-balancing/research-pricing-report-47.md) | you need a tram or light rail maintenance level, overhaul share or rebuild share | MoT car-only returns 1919-33, the 1900-1950 derived ladder, Sheffield 1949-50, the Nottingham 2011 contract, the LCC E/1 and Supertram rebuilds |
| [research-pricing-report-48](cost-balancing/research-pricing-report-48.md) | you need a trailer refurbishment or a van maintenance composition | the FTA trailer line, the TIP 2025 and Cooks 1988 refurbishments at one-third of a new trailer, the Commercial Motor van totals |
| [research-pricing-report-49](cost-balancing/research-pricing-report-49.md) | you need a tram repairs figure for 1950-1990 | Sheffield 1938-50 repairs line (147.3 GBP a car-year in 1900 money at 1949-50); the 150 repairs-only rung and the archive routes after 1950 |
| [research-pricing-report-50](cost-balancing/research-pricing-report-50.md) | you need a locomotive maintenance level for 1914-1948 or after 1977 | Ministry of Transport Railway Returns 1913-38; the Class 92 full-maintenance contract at 868 GBP a locomotive-year (2018), a mixed-traffic class on the Caledonian Sleeper; the class/duty override and the 1950 composition break; applied by pass 63; the Class 88 electric-factor correction applied by pass 64 |
| [research-pricing-report-51](cost-balancing/research-pricing-report-51.md) | you need a carriage maintenance level for 1920, 1948, 1966 or 1990 | five companies' 1912 carriage upkeep; the 1913/1920-21 rolling-stock aggregate; the recommended 39 at 1920 and 121 at 1950; 1948 112 and 1966 226; applied by pass 62 |
| [research-pricing-report-52](cost-balancing/research-pricing-report-52.md) | you need a British Rail wagon repair cost for 1972-1981 | HMRS ME0354 (archive-only), Serpell 1983 aggregates, the 1970 Hansard wagon price and the seven-year HAA overhaul cycle |
| [research-pricing-report-53](cost-balancing/research-pricing-report-53.md) | you need a Midland composite carriage price in the 1860s | the GBP 225-250 early-carriage range, the GBP 62 overhaul at 24.8-27.6 per cent of capital, and the 1874 Midland price bracket |
| [research-pricing-report-54](cost-balancing/research-pricing-report-54.md) | you need a British Rail wagon repair cost for 1972-81 | no readable measurement; The National Archives AN 112/25 "Unit cost of repair: wagons" 1965-81, with AN 112/26, AN 112/87, AN 112/129 and AN 171/941 as related routes; the ladder 14.3 and the 1.2A event remain estimates |
| [research-pricing-report-55](cost-balancing/research-pricing-report-55.md) | you need a maglev rolling-stock acquisition or maintenance price | the Shanghai imported-car price (RMB 100m a car), the Incheon heavy-maintenance contracts (corrected to 5,189 and 5,987 GBP a set-event), and the Changsha and Shanghai overhaul intervals; the acquisition figure of 1,088 GBP a seat is applied by pass 65; maintenance stays 0.00010257 GBP a seat-km |
| [research-pricing-report-56](cost-balancing/research-pricing-report-56.md) | you need a water-object gross tonnage or the basis of the per-GT rates | 39 real vessels covering 57 of the 216 rows; the three per-GT rates (84.1 x GT^0.90, GBP 35/GT, GBP 17/GT) are capital prices, not annual maintenance; recommends using them as the capital ladder and setting repair at 2-5 per cent of capital |
| [research-pricing-report-57](cost-balancing/research-pricing-report-57.md) | you need a gross tonnage for a water object that has none | 120 new figures from 16 vessels, mostly the National Historic Ships UK register's "Tonnage: Gross" field transferred as type representatives (96 MEASURED), 22 DERIVED and 2 STATED; coverage rises from 57 to 177 of 216; the 39 blank rows and the archive route for each; applied by pass 70 |
| [modern-traction-multiple-units](vehicle-cost/modern-traction-multiple-units.md) | you need a multiple unit maintenance cost | RDG per vehicle-mile, London Underground per car-year, Civity per train-km |
| [modern-traction-locomotives-and-wagons](vehicle-cost/modern-traction-locomotives-and-wagons.md) | you need a post-1987 locomotive or a wagon figure | Class 66 and 47 rebuild costs, wagon routes and gaps, the scheduled/unscheduled question |
| [ship-maintenance](vehicle-cost/ship-maintenance.md) | you need a ship repair or dry-docking cost | 50 figures 1849-2026, dry-docking and survey costs |
| [inland-boat-maintenance](vehicle-cost/inland-boat-maintenance.md) | you need an inland boat repair cost | canal company repair jobs 1877-1928, modern narrowboats |
| [horse-keep-components](vehicle-cost/horse-keep-components.md) | you need a horse cost component | feed, farriery, veterinary, stabling, 1876-1897 London |
| [horse-keep-totals](vehicle-cost/horse-keep-totals.md) | you need a horse annual keep figure | totals, horsekeeper wages, working life and work done |
| [tram-maintenance](vehicle-cost/tram-maintenance.md) | you need a tram or light rail maintenance cost | Ministry of Transport returns 1913-1930, iheffield iupertram budgets, DfT mileage |
| [maglev-costs](vehicle-cost/maglev-costs.md) | you need a maglev vehicle purchase or maintenance figure, or are checking one | the overseas-system rule, the Shanghai acquisition transaction (1,088 GBP a seat), the Almujibah maintenance rate (0.00010257 GBP a seat-km), the conversion and the open questions |

The two sources are complementary and do not duplicate each other. The forum thread is a wide,
shallow sweep: many classes, often a single price with no specification. The published table is
narrow and deep: fewer vehicles, but with weight, power, cylinder dimensions, seating or tonnage
alongside the price. For a price surface the second is worth more; for coverage of the vehicle
fleet the first is.

## Purchase prices: what the figures show

### Locomotives

Nominal prices, from both sources:

| Year | Class | Price | iource |
|---|---|---|---|
| 1831 | it Rollox "Planet" type, Robert itephenson, new | £780 | published-capital |
| 1850 | GNR Crampton patent, ten ordered | £1,600 each | published-capital |
| 1853 | NER 213 class, E. B. Wilson | £2,375 each | published-capital |
| 1870 | GNR 8 ft 4-2-2 single | £2,033 | both |
| 1897 | LiWR M7 0-4-4T | £1,846 | both |
| 1899 | LiWR T9 4-4-0 | £3,200 | both |
| 1934 | LMi 2500 class 2-6-4T | £6,444 | forum |
| 1936 | LNER A4 4-6-2 | £8,500 | forum |
| 1940 | W. G. Bagnall 15 in 0-4-0iT, industrial | £2,950 | published-capital |
| 1957 | BR Class 31 diesel | £78,000 | forum |
| 1957 | BR Warship diesel-hydraulic | £87,500 | forum |
| 1959 | Deltic, type 5 | £150,000 | forum |
| 1960 | BR 9F 2-8-0 | £35,500 | forum |

Two structural facts sit alongside the ladder:

- The 1955 modernisation report put new diesel locomotives at about 2.5 times the price of a steam
  locomotive of equivalent power. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`
- The same report gives a capital cost per unit of power, which is the only specification-normalised
  locomotive figure in the evidence: £13,300 per 1,000 draw-bar horsepower for a BR standard Class 5,
  and £17,650 per 1,000 draw-bar horsepower for the Manchester-iheffield electric.
  `[LITERATURE:Hansard, written answer, 1951]`

The nominal ladder alone is not an index: the 1831 and 1959 machines differ in weight, power,
material and tolerance. The price surface in [vehicle-cost-method](vehicle-cost-method.md) exists to
separate the two effects.

### Carriages

| Year | Vehicle | Price | iource |
|---|---|---|---|
| 1846 | itockton and Darlington three-compartment four-wheel composite | £230 | forum |
| 1905-06 | NER twelve-wheel dining cars, dia. 214 and 259 | £2,980 and £2,501 | forum |
| 1906 | NER brake third, five third-class compartments and brake | £1,459 | forum |
| 1910 | NER non-vestibule brake third, five compartments | £1,192 | forum |
| 1924/5 | iouthern Railway eight-compartment third | £2,500 | forum |
| 1929-30 | LNER five-compartment brake third | £2,300 | forum |
| 1934 | NER/LNER standard brake third | £2,136 | forum |
| 1955 | BR passenger carriages, Modernisation Plan programme average | £7,400 | plan estimate: £230m for about 31,000 vehicles (BTC, *Modernisation and Re-equipment of British Railways* 1955, para 74; read from the page image — the hidden OCR misreads the figure, and Wikipedia's £285m is the heading including stations and parcels depots) |
| 1971 | BR inter-city coach (Mk 2F / early Mk 3 era) | £26,667 | Hansard HC 5 Nov 1971 vol 825 c37W: £16m for 600 coaches |
| early 1980s | BR Mk III | £100,000 | forum |

The NER build records are the strongest block in the whole evidence base: consecutive years,
stated diagram numbers, stated layout, and a price for each. They are the natural basis for a
carriage price surface and for matched-model comparisons, because the same diagrams recur.

Order of magnitude by vehicle: a pre-grouping bogie third cost about £1,200-£1,500; a corridor
composite or dining car £1,600-£2,000; a twelve-wheel diner £2,500-£3,000; a 1920s corridor third
£2,300-£2,500.

### Wagons

The ihildon records of 1906 give eleven mineral and coal wagons with stated carrying capacity:

| Capacity | Price |
|---|---|
| 10 tons | £81 |
| 12 tons | £89 |
| 15 tons | £106 and £126 |
| 20 tons | £129 twice, £138 |
| 23 tons | £147, £151, £173 |
| 30 tons | £247 |

Price per ton of capacity ranges from £6.37 to £8.40, mean about £7.2. The relationship is close to
proportional with a modest fixed element, which makes capacity a usable normaliser for goods stock
in this era, and the 30-ton outlier suggests a specification change above 23 tons rather than a
smooth continuation. One mid-century point: high-capacity coal wagons cost £4,000 each in 1971
(Hansard HC 5 Nov 1971 vol 825 c37W: £2m for 500). `[LITERATURE:https://api.parliament.uk/historic-hansard/written-answers/1971/nov/05/railways-rolling-stock]`

**Maintenance.** Hill 1895, Appendix II Table III ("Cost of wagon maintenance per vehicle",
pp. 242-243; note Table I is locomotives and Table II carriages) gives nineteen companies over the
five years ending June 1892, covering repairs and renewals: **average £4 4s. per wagon-year**,
range £2 4s. (L&NWR, 55,126 mostly-mineral wagons) to £6 10s. (LCDR, 2,045 wagons). Large
low-utilisation fleets (Caledonian, NBR, L&NWR) run £2-2 12s.; small intensively-worked fleets
(LCDR, LSWR) £6-6 10s. Read from the page images of Internet Archive `minutesproceedi43britgoog`
on 2026-11-24; the full attributed table is in
[published-maintenance](vehicle-cost/published-maintenance.md) §2. A 1929 private-owner repair
contract (Colchester Gas Company, 20 wagons, Thomas Burnett & Co) was £5 per wagon-year. No
measured wagon overhaul price exists in any era. `[LITERATURE:https://doi.org/10.1680/imotp.1895.19704;
https://www.essexarchivesonline.co.uk/Result_Details.aspx?DocID=987543]`

### Multiple units

Purchase prices for this class:

| Year | Stock | Price per vehicle | Basis |
|---|---|---|---|
| 1915 | LSWR electric stock conversion | £1,520 | per-car conversion (research pass 27) |
| 1954 | First-generation DMU, the 1,408-vehicle tranche | £12,479 | £17,570,000 for 858 motor + 550 trailer cars (BTC Works & Equipment Committee memo, 2 Dec 1954) |
| 1954 | GRC&W tender, Class 100-type | power car £19,300-20,811; trailer £13,186-14,671 | tender prices at 50/20/10 units: a measured volume-price curve |
| 1955 | Derby-built share of the 1,408 | about £12,050 | £6m for 374 motor + 124 trailer (Lightweight Trains Committee, 11 Jan 1955) |
| 1956 | Standard DMU motor car, Derby works | £15,200 | works cost (Diesel Lightweight Trains Committee, 15 Mar 1956) |
| 1956 | Railbuses | £10,000-13,888 | tender prices by maker (W&E Committee memo, 30 Oct 1956) |
| 1979-80 | Class 508 | £151,163 | £26m for 172 cars (research pass 23) |
| 1980-82 | Class 141 £200,000; Class 142 £170,000 | as stated | research pass 23 |
| 1984-86 | Classes 150/2, 155, 156 | £263,204 | £149.5m for 568 vehicles (research pass 23) |

London Underground per-car prices 1972-2010 are in
[cost-balancing/research-pricing-report-26](cost-balancing/research-pricing-report-26.md) §7.
The 1955 Plan average for carriages (above) covers EMU and DMU vehicles as well as loco-hauled
coaches and is a cross-check, not an MU figure. Routes to the remaining gaps (1950s-60s EMU
per-car, 1980s order values, 1890-1910 electric stock) are recorded in
[cost-balancing/research-pricing-report-39](cost-balancing/research-pricing-report-39.md).

### Buses, coaches and lorries

The class table has 284 measured rows. Three findings govern it.

- **The maker effect is small and the specification effect is large.** At Salford in 1928 one
  resolution bought 24 buses, six chassis each from four makers: Associated Daimler £1,220,
  Karrier £1,238, Dennis £1,263 and Leyland £1,270. The whole spread across four makers was
  4.1 per cent, and Leyland was the dearest. Four same-year Daimler/Leyland pairs 1928-62 put
  Daimler between 0.3 and 6.2 per cent *below* Leyland. There is no Daimler marque premium.
  `[LITERATURE: Commercial Motor, 20 March 1928, p.48; 14 January 1930, p.46; 13 October 1931,
  p.57; 6 July 1962, p.40]`
- **The one real Daimler cost adder is the transmission.** Daimler's own October 1930 list
  prices the fluid flywheel with Wilson preselective gearbox at £1,275 against £1,175 for the
  same chassis with a clutch and sliding-pinion box: £100 on £1,175, 8.5 per cent. Municipal
  Daimler orders almost always took it, which is why Daimler fleets look expensive in aggregate
  while Daimler chassis bids do not. `[LITERATURE: Commercial Motor, 28 October 1930, p.88]`
- **No durability evidence exists in period.** The only direct maker-versus-maker reliability
  statement found is Sheffield in 1969, outside the class's range: £307 a chassis more for
  Fleetlines because they were "more reliable and less costly to maintain".
  `[LITERATURE: Commercial Motor, 26 September 1969, p.41]`

Prices by scope; a ladder that mixes scopes is not comparable:

| Scope | Double-deck | Single-deck |
|---|---|---|
| Chassis share of complete price | 55-58% | 63-67% |
| Body, 1928-32 | £666-795 | £443-480 |

Complete double-deckers run £1,300-1,720 nominal 1928-31, £1,800 in 1937, about £3,478 in 1946
and £4,329 in 1955. Cost per seat falls as capacity rises: £43 a seat for a 32-seat single-decker
in 1929 against £29-31 for a 50-seat double-decker in 1931-32.

Lorries and vans have a single-date ten-make ladder in the 1960 lorry price list: 3-ton diesel
chassis-cab at Ford £769, Bedford £840, Austin and Morris-Commercial £867.50, Dodge £980 and
Seddon £1,105. Price scales as payload^0.55 between 1 and 8 tons, with a fixed element large
enough that a 1.5-ton van measures £160-210 (1900) while a 10-ton lorry measures about £400.

Steam wagons were cheaper per ton than petrol lorries of the same date (1927 Sentinel £1,150 for
10-12 tons against 5-6-ton petrol at £800-850), but their unladen weight was about 50 per cent
higher for the same nominal capacity.
`[LITERATURE: research passes 28-31; Commercial Motor archive]`

Modern prices (1980-2026) are measured from public-body tender awards and dealer price lists.
Two findings govern the modern ladders.

- **The real level rose about 40 per cent after 1990.** A 2021 diesel single-decker was
  £169,000 and a double-decker £236,000-251,000; a 2026 3.5-ton panel van £34,945-49,845; a
  2024 44-tonne tractor unit £138,223 chassis-only. All are about 1.4 times the real level the
  ladders carry from 1960.
- **A battery-electric vehicle costs a multiple of the diesel, and the multiple depends on the
  class.** From same-document pairs: heavy goods vehicles from 7.5 t up cluster at about 2.0×
  (7.5 t 2.17, 12 t 2.00-2.25, 18 t 2.00-2.32, 26 t refuse 2.02-2.40, 44 t 1.80-2.70);
  single-deck buses 2.19-2.24×; double-deck buses 1.95-2.06×; coaches about 1.5×; vans a median
  of 1.20× (range 1.03-1.47); hydrogen buses about 2.2×. A near-constant £200,000-267,000 cash
  premium would come from sampling buses only, whose diesel price ranges £160,000-251,000; a flat
  cash adder would overprice a 7.5-ton tipper by 105 per cent.
  `[LITERATURE: research pass 34; council and operator tender awards, 2019-26]`
  `[LITERATURE: research pass 32; FirstGroup, Cornwall Council, Arriva, Blackpool Council,
  Ford and Vauxhall price lists, Perth & Kinross tender award]`

**The lorry curve has a kink at about 7 tons.** Below it a fixed element (cab, engine,
controls) dominates and price scales as payload^0.30; above it price is close to proportional.
Measured: a 1960 7-tonner at £269 (1900) and a 1964 16-tonner at £670 give an exponent of 1.10
across that pair, and a 1977 32-ton Crusader at £983 and a 1984 25-ton Roadtrain at £1,059 sit
on the same line. A single power law cannot hold both ends; a payload^0.60 ladder prices a
25-ton tractor at a third of its measured price.
`[LITERATURE: research passes 30 and 32]`

### Trams and light rail

The tram evidence separates into two eras, and the gap between them is real rather than
inflation.

| Era | Capital | Maintenance |
|---|---|---|
| 1901-04 municipal car | £575-590 nominal (Wallasey, Dover) = £663-676 at 1900 | 84 GBP a car-year gross at 1900-13 (band 79-88; car only, Ministry returns) |
| 1926-34 Blackpool | £1,750-2,688 nominal, a premium fleet | — |
| 1950 Blackpool Coronation | £7,405 nominal, body and equipment separate | 147.3 GBP a car-year repairs-only (Sheffield 1949-50, 1900 money) |
| 1994-2019 LRV | £1.80-2.72m nominal, every UK order that prices vehicles alone | £118,657 a tram-year nominal (Nottingham 2011 contract) = 1,177 GBP a tram-year in 1900 money |

Two structural facts. First, the modern band is narrow and stable: seven Metrolink orders
2007-18, Croydon, DLR, West Midlands, Edinburgh and Blackpool all fall inside £1.80-2.72m, and
the two figures outside it are the ones that bundle a long support obligation. Second, the
measured maintenance series ends with the Sheffield 1949-50 repairs line and resumes with the
2011 Nottingham contract; there is **no measured municipal tramcar figure for 1950-1990**, so the
1960-90 rung of 150 GBP repairs-only (band 130-210) is an estimate constrained by the Sheffield
1949-50 figure of 147.3 ([research-pricing-report-47](cost-balancing/research-pricing-report-47.md);
[research-pricing-report-49](cost-balancing/research-pricing-report-49.md)).

Capacity normalisation does not close the gap: a 1934 Blackpool car cost £28.60 a seat and a
2014 Edinburgh tram £9,584 per total-capacity place, so the modern vehicle is cheaper per place
despite being far dearer per vehicle. The defensible basis is per vehicle with the class stated
alongside. `[LITERATURE: research pass 35; National Tramway Museum; Contracts Finder; Edinburgh
Council final account 2014; International Railway Journal]`

### Articulated tractor units

A tractor unit carries no goods, so the pakset has no payload to scale it by. It is priced
directly on measured chassis-cab prices: £300 for a 1933 Scammell Mechanical Horse, £1,480 for
a 10/11-ton tractive unit in 1962, £19,500-25,495 for 32.5-ton tractors in 1978-80, £46,000-
72,790 for 32-40 ton units in 1989-97, and £105,750-141,108 for 44-ton units in 2021-26. In
1900 money the curve rises to about £1,000 by 1978 and then flattens; a 44-tonne driveline
costs little more than a 32-tonne one. The trailer is about 21 per cent of a modern
combination, not a third of it. `[LITERATURE: research pass 33]`

### Overhauls and upgrades

The `Overhauls & upgrades` sheet of the capital workbook carries intervals and cost shares for
all 3,539 vehicles.

| Class | Interval | First overhaul | Late-life overhaul | Downtime |
|---|---|---|---|---:|---|
| Steam locomotive | Per class (BR general repairs 104,000-196,000 miles for the archetype) | 0.70 of the maximum | 35% of A as the works-overhaul provision; the events are scaled to it | 1.2 months (31-53 days) |
| Diesel/electric locomotive | 7 years at the row's own duty (BR's 2.75/5.5/11-year cycle is the class evidence) | Flat event | 39% of A as the provision; one event of provision x seven years | 0.8 months |
| Carriage | 210,000 / 180,000 / 165,000 / 176,000 / 240,000 / 294,000 km by era (6 / 5 / 3 / 2 / 2 / 2.6 years) | 0.70 of the maximum | 28 / 24 / 19 / 12 / 10 / 8 per cent of the annual maintenance total A by era; the mean event is provision x interval | 0.5 months |
| Wagon | 240,000 km (six years at 40,000 km/yr) | 0.75 of the maximum | head 0.8A, event 1.2A | 0.2 months |
| Multiple unit | eight years at 100,000 / 120,000 / 161,000 km a car-year | 15% of A; first event 0.70 of the maximum over three | 1.2A | 0.4 months |
| Bus | 220,000 km (four-year cycle) | 25% of capital | 40% of capital | 0.5 months (two days pre-war) |
| Lorry | 160,000 km (50,000-100,000 miles) | 10% of capital | 30% of capital | 0.3 months |
| Van | 60,000 km | 10% of capital | 30% of capital | 0.1 months |
| Tram | 2 / 3 / 12 years (96,000 / 144,000 / 1,080,000 km) | pre-1950 28 per cent of gross A, event 0.35A to 0.75A; 1950-90 28 per cent of the repairs-only rung, event 0.54A to 1.15A; modern 6 per cent, one event of 0.75A | the same event ladders | 0.4 / 0.5 / 0.8 months |
| Ship | five-year survey cycle | 2% of capital | 5% of capital | 0.4 months (12 days) |
| Aircraft | C check 18-24 months | 2.5% of capital | 5% of capital | 0.8 months |

The carriage and wagon rows are shares of the measured annual maintenance total, not of capital,
because the measured total is the envelope: head plus amortised events equals the net total
([research-pricing-report-44](cost-balancing/research-pricing-report-44.md);
[wagon-overhaul-source-analysis](cost-balancing/wagon-overhaul-source-analysis.md)). The steam
and diesel/electric locomotive rows are also shares of the measured annual total A, not of
capital, since pass 49; the Class 92 provision is deducted from its measured 868 GBP total
(pass 63).

The measured anchors: a GWR 28xx heavy general at £450-700 against a £4,992 build (9-14%); Lacy &
Dow's £62 Midland composite overhaul in the 1860s, which is 24.8-27.6 per cent of the £225-250
composite price and 1.84 times the annual maintenance total (research pass 53), and the 1982 York
Works Mk 1 overhaul at "more than £2,000", 0.16 times the annual total; £2,000 a London bus in
1965, 25-33% of a new double-decker; the 1955 lorry cycle of £60 for an engine and £220 for
chassis and body at 100,000 miles (8-22%); Metrolink's 12-year mid-life refit at £80,000 a tram,
the modern works overhaul; Supertram's life-extension programme at £856,000 a tram after 32-34
years, the modern rebuild and an `upgrade_price` event.

**Upgrades.** The engine charges the *target* vehicle's `upgrade_price` and deletes the old
vehicle with no resale credit, so the figure is the whole net replacement cost. Measured rebuilds
sit at 20-50 per cent of a new vehicle: Class 47 to 57 at about a third of a new build, Class 321
Renatus at £500,000 a vehicle, the Mk3 sliding-door conversion at £325,000 a coach, steam
reboilering at 19.5-27.3% of capital, and the Leyland National Greenway bus rebuild at £45,000,
stated to be half a new bus. The sheet uses 30-35 per cent for rail, 22-50 per cent for trams by
introduction year (the 1934 LCC E/1 rebuild and the 2026 Supertram life extension), and 50 per
cent for road, ship and aircraft. With no resale credit, an upgrade at those shares is a design
decision, not a measurement.
`[LITERATURE: research passes 36-37; Railway Gazette International 1 May 1998; National Railway
Museum and BR repair records; Commercial Motor; Metrolink and Supertram accounts]`

### The `.dat` comments as an evidence channel

The pakset authors left historical notes in the `.dat` files: 25,113 comment lines across 2,664
files. Two findings govern them.

- **Qualitative claims.** 1,022 vehicle comments carry a judgement; 80 of those make a
  comparative claim, and 26 adjustments were accepted into `vehicle-adjustments.csv`. The
  method rules are in [vehicle-cost-method](vehicle-cost-method.md) "Comment-derived
  adjustments".
- **Prices.** 76 comments state a price. 43 new ones were parsed into the register, 12 were
  duplicates. They include buses the register did not have — AEC 605 at £1,445, EE E11 at
  £2,098 in 1929, Ret Hurst Nelson at £725 in 1911, the Bedford WTB at £785 complete or £290
  chassis — plus a Leyland Titan TD3-to-TD4 diesel conversion at £450, which is direct evidence
  for `upgrade_price`, and a Sans Pareil locomotive at £500 in 1829.

The channel needs three cautions. A comment is the author's note, not a transaction, so it ranks
below a company record even where it cites one. A fleet total must be divided before it can bind,
and the register marks those as computed. And a component price (chassis, body, conversion) must
not be bound to a complete vehicle, which required three fixes to the matcher: short object
names were excluded by an 8-character floor, component rows could bind to complete vehicles, and
a tractor price could bind to every trailer variant. Bound measured rows rose from 60 to 99.
`[CODE ai/temp/dat-comment-audit.md; research pass 38]`

### Ships and aircraft

- 1816 Frontenac £20,000; 1843 SS Great Britain £117,000; 1858 SS Great Eastern £377,200, of
  which £275,200 was hull and the rest engines.
  `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`
- Research pass 25 (2026-11-22) adds 76 measured ship, ferry, river-boat and inland-craft prices.
  The strongest series is 14 British passenger vessels 1924-38: price = £149.7 × GT^0.90,
  n = 14, R² = 0.992, residuals within ±16 per cent. The 1927-38 band is £70-80 per gross ton
  across ten ferries from 38 to 2,910 GT, four yards and five operators. Cargo ships are flat at
  £149-173 per gross ton (1950-53, 925-1,500 GT), and inland motor narrowboats cost £700-900
  (1928-37) against £390 for a butty. `[LITERATURE: research pass 25; Moses, *Commercial and
  Technical Evolution of the Ferry Industry 1948-1987* (2010), Table 2.7 from TNA AN13/391;
  Wallasey fleet list; Paddle Steamer Preservation Society]`
- Gross tonnage is not recorded for any pakset water object, and the measured GT-per-capacity
  relationship is type-dependent (0.80-188.9 gross tons per capacity tonne across 39 vessels;
  R² 0.08 within 1924-38), so the GT fit cannot be applied directly. The workbook prices
  passenger vessels per passenger (sea-going, river and estuary anchors) and cargo and inland
  craft per tonne of capacity. `[CODE New ex-15 @ 33cf9b106; ai/temp/water-capacity.csv]`
- Research pass 56 (2026-11-25) shows that the three per-gross-ton rates are the measured
  **capital** prices, not annual repair: 84.1 × GT^0.90 is the report 25 passenger purchase fit
  deflated at the 1931-32 general index (149.7 × 100/178 = 84.06), GBP 17/GT is *Cambria*'s 1906
  price deflated (1,895 × 100/102/109 = 17.04), and GBP 35/GT is the British Railways 1950-53
  cargo price (148.6-173.3 × 100/391-440 = 38.0-39.4, within 11 per cent). Applied as maintenance
  they would charge a hull's whole capital every year. The GT fit is therefore a price check, not
  only a shape check, and the per-capacity rates are a conversion of it at an assumed gross
  tonnage per capacity unit; that assumption is what the 0.80-188.9 range makes unsafe.
  `[LITERATURE: research pass 56 § 4.4; research pass 25 § 9]`
- The workbook now uses the per-gross-ton capital ladder (the 2026-11-25 decision): passenger
  vessels at 84.1 × GT^0.90, cargo ships and coasters at GBP 35/GT, inland craft at GBP 17/GT and
  tugs at GBP 39/GT, with repair at 2 per cent of capital. On the rows with a sourced tonnage the
  per-GT figure replaces a capacity target that was a median 0.30 of it; on an individual check
  (*TS King Edward*, 502 GT, £33,000 in 1901) the capacity target reproduced the measured price
  and the per-GT rate is 31 per cent below it, while on a large modern hull (*Spirit of Britain*,
  47,592 GT) the per-GT figure is ten times the capacity figure. The full effect and the tonnage
  coverage are in [cost-balancing/handoff](../cost-balancing/handoff.md).
- Cargo is priced at £8.5 per tonne of capacity, the direct per-ton rate from the Fairplay tramp
  (1900), the 1918 steel barge and *Cambria* (1906). The £149-173 per gross ton of the 1950-53 BR
  cargo ships is a small-ship rate (925-1,500 GT) and would overprice the pakset's 20,000 t bulk
  carriers about threefold; it is recorded as the small-ship end, not applied to them.
- Aircraft purchase prices are fitted hedonically on 116 measured aircraft, 1936-2015:
  seats^0.867 × engines^0.768 × engine type × wide-body × 1.0111^(year-1959), R² 0.948. The fit
  does not extend to maintenance, where the only evidence is engineering cost per flying hour.
  `[LITERATURE: research pass 18]`
- Light twins outside the 1959 airliner survey have period prices. The Aero Commander 520 sold for
  $45,000 in 1952 (rising to $66,000 by 1954), and the 500B for $87,000 standard in 1960. At
  $2.80/£ the 1952 price is £16,071 nominal, or £4,477 at 1900 on the vehicle purchase index. The
  pakset object named `aero-commander-500` has `intro_year=1951`, which is the 520; the 500 series
  began in 1958, so the 520 is the correct type anchor. The workbook uses the measured price in
  preference to the hedonic. `[LITERATURE: All Aero, *Aero Design & Engineering 500 / 520 / 560 /
  580 / Shrike Commander / L-26*; AOPA, *An Aero Commander Restoration* (2002)]`

## The conversion question this evidence exposes

The calibration workbook prices the same vehicles two ways, and the gap between them is the central
problem for vehicle balancing.

- The `Vehicles (historical)` sheet normalises a nominal price to 1900, converts it at 2.523
  SimuCents to the pound (the capital conversion), then multiplies by 8 to give the figure written
  into the `.dat`. For the GNR 8 ft single: £2,033 in 1870, £1,973.79 in 1900, 4,980.40 Simucredits,
  39,843.21 in the `.dat`. The ratio is exactly 8.0 for every row checked, carriages included.
  `[CODE New ex-15 @ 8d0603d81]`
- The `Vehicles (Simutrans)` sheet takes the same `.dat` figure and divides it by 8 to reach "in
  game", and divides the monthly figure by 4. `[CODE New ex-15 @ 8d0603d81]`
- The engine does neither. `cost` is charged at face value with only the price index applied, and
  the monthly figure is multiplied by 2 at this pakset's settings.
  `[CODE simutrans-extended ex-15 @ bdfdc8311]`

Read against the real price, the same `.dat` value is therefore either about eight times too high
or about ten times too low, depending on which conversion the rest of the economy uses:

- at the capital conversion, £1,973.79 becomes 4,980 Simucredits, and the written value of 39,843 is
  8.0 times that;
- at the revenue conversion, £1,973.79 becomes 378,968 Simucredits, and the written value is 0.105 of
  that, or 9.5 times too low.

Which one is correct cannot be settled from the vehicle evidence alone: it depends on whether the
fare calibration makes the player's receipts realistic. That is the joint test the synthesis has to
run, and it is the same capital-to-receipts test that the infrastructure work specified. Recorded
here as the strongest single reason not to adjust vehicle `.dat` values in isolation.

## The existing `.dat` costs against the measured prices

Eight classes have both a measured price and a `.dat` file, so the two can be put side by side.
The measured price is brought to 1900 with the `general` index; the `.dat` cost is converted at
both recorded rates.

| Class | Year | Measured, nominal | Measured, 1900 | `.dat` cost | Implied 1900, revenue rate | Implied 1900, capital rate | Ratio, revenue | Ratio, capital |
|---|---|---|---|---|---|---|---|---|
| GNR 8 ft single | 1870 | £2,033 | £1,974 | 3,984,320 | £208 | £15,778 | 9.5 | 0.13 |
| LiWR M7 | 1897 | £1,846 | £1,943 | 4,528,000 | £236 | £17,931 | 8.2 | 0.11 |
| LiWR T9 | 1899 | £3,200 | £3,333 | 6,532,500 | £340 | £25,869 | 9.8 | 0.13 |
| LMi Black 5 | 1934 | £6,000 | £3,488 | 4,598,000 | £239 | £18,208 | 14.6 | 0.19 |
| LNER A4 | 1936 | £8,500 | £4,885 | 11,088,000 | £577 | £43,908 | 8.5 | 0.11 |
| BR Class 31 | 1957 | £78,000 | £15,294 | 9,450,000 | £492 | £37,422 | 31.1 | 0.41 |
| BR Class 55 | 1959 | £150,000 | £28,409 | 13,364,000 | £696 | £52,921 | 40.8 | 0.54 |
| BR 9F | 1960 | £35,500 | £6,648 | 7,948,000 | £414 | £31,474 | 16.1 | 0.21 |

Three conclusions, and they are the most important in this doc:

1. **On the revenue rate the `.dat` costs are 8 to 41 times too low. On the capital rate they are
   2 to 9 times too high.** The measured price sits between the two conventions, which is the
   conversion question above, seen from the other side.
   **The capital rate is confirmed** from an in-game tooltip read on 2026-11-17
   ([balance-synthesis](balance-synthesis.md) §8), so the operative conclusion is that **vehicle
   capital is 2 to 9 times too high** in the present files, not too low.
2. **No single correction factor exists.** The ratio ranges from 8.2 to 40.8 across eight classes
   on the revenue rate and from 0.11 to 0.54 on the capital rate. A uniform multiplier would fit
   one class and miss the next by a factor of five. `[CODE New ex-15 @ 8d0603d81]`
3. **The values must be rebuilt from the evidence, not scaled.** This is the practical form of the
   standing direction not to trust the present `.dat` costs.

Price per ton of engine weight, as a physical check. Weights are the pakset's `weight` field and
may exclude the tender, so they are comparable between rows but not necessarily with published
weights.

| Class | Measured, £1900 per ton | Implied from `.dat`, revenue | Implied from `.dat`, capital |
|---|---|---|---|
| GNR 8 ft single | 49 | 5 | 394 |
| LiWR M7 | 32 | 4 | 294 |
| LiWR T9 | 71 | 7 | 552 |
| LMi Black 5 | 48 | 3 | 253 |
| LNER A4 | 47 | 6 | 420 |
| BR Class 31 | 139 | 4 | 340 |
| BR Class 55 | 281 | 7 | 524 |
| BR 9F | 78 | 5 | 370 |

The measured steam-era engines cluster at £32 to £78 per ton of engine weight, with the diesels
above them. The two implied columns bracket that range by an order of magnitude on each side,
which is the same conclusion reached another way.

**Price per ton is a check, not the ladder.** The fit of 2026-11-22 shows why: on the steam rows,
price scales as weight^0.86, so a flat £/ton overprices small engines and underprices large ones;
across traction, power rather than weight carries the diesel/electric price. The ladder actually
used by the workbooks is the one in [vehicle-cost-method](vehicle-cost-method.md#the-fitted-locomotive-ladder-2026-11-22).
The table above remains valid as a per-ton sanity check within the steam era.

## What the evidence supports

- A price surface for carriages and wagons from the 1895-1910 records, which are dense and carry
  layout and capacity.
- A locomotive surface with fewer points but a usable power normaliser for the 1950s, and a
  size ladder for the steam era.
- Matched-model comparisons where the same diagram or class recurs: the NER diners of 1905 and
  1925, and the G.E. iection carriages of 1923-29, are the best of these.
- Maintenance-to-capital ratios, from the three ratios in published-maintenance and from the
  pairing of running and purchase figures for buses and lorries.
- Base maintenance levels in engine units: the conversions are worked through in
  [base-maintenance](vehicle-cost/base-maintenance.md), which gives per-kilometre and
  per-vehicle-year figures and the field each class belongs in.

## What it does not support

- A fully measured index series for 1938-1988. No published asset-level transport-equipment
  deflator exists for that span; the series implemented in `config/prices.tab` bridges it with
  Feinstein's plant and machinery index for 1938-1965 and the Blue Book 1997 current/constant
  pair for 1965-1997, both documented as constructions in [prices-config](prices-config.md).
- A price surface fitted across classes. The specification-bearing rows carry cylinder dimensions,
  wheel diameters and layouts, because that is what nineteenth-century sources record: weights and
  powers are rarely given. Only eight classes could be matched to a pakset vehicle with a stated
  weight, which is too few to fit the four-term surface set out in
  [vehicle-cost-method](vehicle-cost-method.md). The surface needs either a source that states
  weights, or a decision to normalise on cylinder volume and driving-wheel diameter instead of
  weight and power.
- Aircraft costs, on any basis.
- Any conclusion about current `.dat` levels. The present values are not usable as a reference and
  are to be replaced.

## Open questions

- Which conversion should vehicle capital use: the capital one, the revenue one, or a third
  defined for vehicles?
- Is the 8× factor in the workbook intended, or a legacy of the tile-size scaling applied to ways?
- Can the NER records be extended to the 1870s and 1880s from the same source, to give the carriage
  surface a longer run?
- Do the pakset's weights include the tender, and do capacities mean seats or passengers? The price
  surface must use the same definition as the `.dat` field or the per-ton figures will be
  inconsistent.
- The `vehicle purchase` series holds the 1997 real level after 1997. A producer price index for
  transport equipment, or for railway rolling stock specifically, would replace that hold with a
  measurement. None has been found.
