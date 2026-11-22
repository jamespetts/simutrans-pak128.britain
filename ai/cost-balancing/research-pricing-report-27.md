# Research pass 27 — measured build costs of early British electric locomotives, 1890-1935

Status: draft evidence for the parent session. Compiled 2026-11-22. The knowledge base is not
edited here.

**Covers**: the capital cost of British electric locomotives from the City & South London of 1890
to the LNER EM1/EM2 orders of 1947-48, with the North Eastern Railway classes added at the
parent's request (ES1, EF1, EE1, Tyneside motor parcel van, EM1, EM2). For each class: a contract
or accounts price, the year, the builder, and whether the figure is per locomotive or a batch
total.

**Companion file**: `research-pricing-rows-27.csv` — 15 rows: 10 locomotive-domain, 4
rolling-stock and 1 component.

**Rule observed throughout**: no Simutrans `.dat` price was read, used or fitted to. Pakset
object names were used only to identify which machine was being researched. The only pakset file
read was `New/config/prices.tab`, and only to obtain the `vehicle purchase` index used to bring
prices to 1900 money; its values are quoted where used.

---

## 1. Summary

1. **Five per-locomotive figures were found** (counting the two Metropolitan alternatives): ES1
   £2,365 (1902), EF1 electrical equipment only at £4,010 equivalent (1913), EE1 £27,767 (1922),
   and the Metropolitan 1922-23 at £11,000 (secondary) or £15,600 (project average); plus the 1951
   generic electric locomotive at £37,400 and the 1955 average of £55,000 already held by the
   parent. Four of the five are North Eastern or Metropolitan.
2. **The North Eastern Railway is the best-evidenced company in the period**, because it bought
   from contractors and its contract values were reported in the technical press. The ES1 pair
   cost £4,730; the EF1 electrical contract was $195,000 for ten sets; the EE1 was £27,767
   against an estimate of £20,000.
3. **Four items in the brief are not electric locomotives.** The Waterloo & City had no
   main-line electric locomotives (Siemens supplied motor-car equipment; Jackson & Sharp built
   the car bodies). The Lancashire & Yorkshire built only two electric locomotives, neither of
   them a 1,200 V machine; the 1,200 V scheme was the 1916 Manchester-Bury multiple-unit stock.
   The LSWR 1915 stock is multiple-unit too, and is covered in section 2.10. The Harton
   locomotives existed but no price was found. See section 6.
4. **The current diesel/electric ladder is 2.5 to 3.2 times too high on the two pre-1935 series
   machines**, and about 1.4 times too high on the one prototype. On the measured points, an
   early electric cost about £4.4 per horsepower in 1900 money, against the £12-14 per horsepower
   that `28 x power^0.889` implies at those powers. A separate early-electric ladder is
   supportable and is set out in section 5.
5. **The electrical share of the cost is measurable once.** On the EF1 the electrical contract
   was about £4,010 per locomotive against a total that the scheme figures imply at £8,000-10,000,
   so electrical equipment was of the order of 40-50 per cent of the machine; by weight it was
   32.6 per cent (48,500 lb of 148,800 lb, Electric Railway Journal 1916).
6. **The largest gap is still 1890-1910.** No contract price was recovered for the City & South
   London, the District, the Metropolitan of 1905-07, or Harton. Those are the four classes where
   the pakset most needs a measured point, and all four require the company minutes or the
   electrical press rather than the sources reachable in this pass.
7. **The LSWR 1915 multiple-unit stock is priced**: £383,000 to convert 252 cars, about £1,520 per
   car and £4,560 per three-car unit, against 178-190 seats per unit. It is 600 V DC third rail,
   not 1,500 V, and the equipment was British Westinghouse, not BTH. See section 2.10.
8. **The LBSCR 1909 overhead stock is not in the pakset.** No object among the 63 `lbscr-*` files
   is an electric multiple unit; the only electric-era LBSCR items are the 48 ft and 54 ft
   suburban carriage bodies and the augmentation trailers used with the Southern 3-SUB units.
   See section 2.11.

---

## 2. Prices found, by class

Nominal money as stated. "Per loco" means the price of one complete locomotive unless the scope
column says otherwise.

| Class | Year | Price | Scope | Builder / electrical contractor | Source |
|---|---|---|---|---|---|
| NER ES1 (Quayside) | 1902 | £4,730 | pair (2 locos), £2,365 each | BTH main contractor; Brush mechanical | Ouseburn Trust 2021, from Hoole 1988 |
| NER ES1 (estimate) | 1902 | £3,000 each | per loco, estimate for 6 | Merz & McLellan proposal | Merz & McLellan report, quoted in forum |
| NER EF1 (Shildon-Newport) | 1913 | $195,000 | electrical parts for 10, $19,500 each | Darlington mechanical; Siemens Bros electrical | Commercial & Financial Chronicle, 28 Jun 1913 |
| Shildon-Newport scheme | 1915 | £200,000 | whole scheme, 10 locos + OHL + substations | NER / Siemens / BTH | Northern Echo, 3 Jul 2015 |
| NER EE1 No. 13 | 1922 | £27,767 | per loco (one-off) | Darlington; Metropolitan-Vickers electrical | LNER Encyclopedia |
| Metropolitan Rly (reconstruction estimate) | 1919 | £213,000 | 20 locos (15 new, 5 rebuilt) | Metropolitan-Vickers, Barrow | LURS report, 2024 |
| Metropolitan Rly 1922-23 | 1923 | £312,000 | 20 locos outturn, £15,600 each | Metropolitan-Vickers, Barrow | LURS report, 2024 |
| Metropolitan Rly 1922-23 | 1922 | £11,000 | per loco | Metropolitan-Vickers, Barrow | modelraildatabase (secondary) |
| LNER Woodhead equipment order | 1938 | £1,800,000 | joint OHL + equipment for 70 locos | BICC / Metropolitan-Vickers | Glossop Heritage, from Railway Gazette |
| Electric locomotive (generic) | 1951 | £37,400 | per loco | not stated | Riddles table, Modern Transport 1951 |
| W&C electrical contract | 1897 | £55,913 | generation + train equipment | Siemens | ICE Proceedings 139 |
| W&C car bodies | 1897 | £21,675 | 22 cars, £985 each | Jackson & Sharp | ICE Proceedings 139 |
| LSWR 3-car units (conversion) | 1915 | £383,000 | 252 cars, £1,520 each | Eastleigh conversion; British Westinghouse equipment | BloodandCustard |
| LSWR scheme spend | 1915 | £970,000 | scheme total to 31 Dec 1915 | LSWR | Electric Railway Journal, 1916 |
| BTH 200 hp motor | 1905 | £225 | each (District B stock order) | BTH | LURS, Connor |

### 2.1 North Eastern Railway

**ES1, 1902, £2,365 each.** The Quayside branch locomotives were ordered on 15 December 1902 from
British Thomson-Houston at £4,730 for the pair, with frames and bodies sub-contracted to Brush and
a spares package at a further £761 8s. This is a turnkey contract: no mechanical/electrical split
is stated. The contemporaneous Merz & McLellan estimate had been £3,000 each for six locomotives
of the type, so the contract came in 21 per cent under estimate. The ES1 is the earliest British
electric locomotive with a recoverable contract price in this pass, and it is eleven years earlier
than anything else found.

**EF1, 1913, $19,500 per locomotive for electrical parts.** The Commercial & Financial Chronicle
of 28 June 1913 reported the contracts awarded for the Shildon-Newport scheme: ten electric
locomotives at $195,000 "for the electrical parts alone", permanent way $308,975, substations
$63,075. At $4.86 to the pound that is £40,123 for the ten sets, £4,012 per locomotive. The
Electric Railway Journal account of 1 July 1916 confirms the arrangement (designed and built at
the company's own shops, electrical equipment installed by Siemens Brothers' Dynamo Works,
Stafford) and gives the weight split: 48,500 lb electrical, 100,300 lb mechanical, 148,800 lb
total. The mechanical cost is not published, but at the £200,000 scheme total the residual for the
ten machines is about £12,000 each.

**EE1, 1922, £27,767.** The single 2-Co-2 express locomotive cost £27,767 against an authorised
£20,000, a 39 per cent overrun. Built at Darlington with Metropolitan-Vickers equipment. The
LNER Encyclopedia gives six 300 hp motors (1,800 hp one-hour); the pakset figure of 1,342 hp is
presumably the continuous rating. A one-off, so the price includes development cost that a batch
price would not.

**Tyneside motor parcel van.** No price found. It was a motor parcels vehicle, not a locomotive,
and the Tyneside electrification contract values were not recovered.

### 2.2 Metropolitan Railway

**1922-23, £11,000 each or £15,600 average.** The LURS account of Charles Horsey's 2024 talk is
the fullest statement: a reconstruction contract signed with Metropolitan-Vickers in September
1919 at about £213,000 (1919 values), revised in 1921 to a fixed price per locomotive for fifteen
new machines, actually taking 43 months and costing £312,000, with all twenty in service by spring
1923. That gives £15,600 per locomotive across twenty, or about £20,800 if the five rebuilds are
treated as free. The £11,000 per locomotive figure is from a class-profile site and is consistent
with the £220,000 total it also quotes; it is 21 per cent below the LURS average and is recorded
as low-medium confidence.

**1905-07, no price.** The ten Westinghouse "camelback" locomotives ordered December 1904 and the
ten BTH box-cab locomotives of 1907 were traced through the LURS paper, the Street Railway Journal
of 26 August 1905 and the Wikipedia class article, and none states a price. The Metropolitan
Railway accounts for 1922 on transportist.org exist but their OCR is unusable; earlier years are
not posted there.

### 2.3 District Railway, 1905

Ten locomotives, bodies by Metropolitan Amalgamated ordered September 1904, BTH electrical
equipment, four 200 hp motors each (800 hp), 36 tons. **No contract price found.** The one usable
number is the component price from the same BTH order for the B stock: traction motors £225 each,
traction controls £360 per train, brakes £161 per train, compressor £82 each (LURS, Connor). Four
motors for a locomotive therefore cost £900 before control gear, which sets a floor and shows how
small the electrical component prices were relative to a complete machine.

### 2.4 Waterloo & City, 1898

**Not a locomotive class.** The line opened with Siemens-equipped motor cars on bodies built by
Jackson & Sharp: 11 motor cars and 11 trailers at £21,675 for the bodies (£985 per car), and a
Siemens contract of 4 January 1897 at £55,913 covering the generating and distribution plant and
the electrical train equipment. The only locomotives on the line were a four-wheel Siemens
shunting locomotive of 1898 and a Drummond-designed rescue locomotive of 1901; neither has a
recovered price. The brief's "Siemens and Jackson locomotives" conflates the electrical contractor
with the body builder.

### 2.5 Harton Colliery, 1908

Six locomotives supplied from December 1908 by Siemens Brothers' Dynamo Works (some sources say
Siemens-Schuckert, Berlin; the survivors are badged Siemens-Schuckert). 550 V DC overhead; later
ten in the fleet. **No price found.** The Electric Railway Journal of 1911 (vol 37, p. 925)
describes the installation and explicitly says the comparative operating cost had not then been
determined; it gives no capital figure either.

### 2.6 Lancashire & Yorkshire, 1912

**No 1,200 V locomotive class existed.** The L&YR built two electric locomotives: No. 1, a 600 V
machine on the frames of an Aspinall 2-4-2T for the Liverpool-Southport line, and No. 2, a
four-wheel battery steeple-cab shunter for Clifton Junction power station. The 1,200 V DC
installation was the Manchester-Bury line of 1916, and its stock was multiple-unit: 66 cars in
twelve five-car sets, 200 hp motors, Dick Kerr control equipment. No locomotive price exists to
find. This corrects item 5 of the brief.

### 2.7 London Brighton & South Coast, 1909, and London & South Western, 1915

**Neither was a locomotive class.** Both schemes were multiple-unit electrifications. The LSWR
stock is priced in section 2.10; the LBSCR 1909 stock is not in the pakset at all (section 2.11).
The brief's "1,500 V DC" does not describe the LSWR system, which was 600 V DC third rail.

### 2.8 Bury, 1917, and Manchester South Junction & Altrincham, 1904

No electric locomotive was found for either. The MSJ&AR electrification is the 1931 scheme at
1,500 V DC, worked by three-car multiple units. The Bury reference is most likely to the L&YR
Manchester-Bury stock of 1916 (section 2.6). Both recorded as dead ends.

### 2.9 LNER EM1 and EM2

**No unit price found.** The sequence is documented but the money is not: tenders invited at the
end of 1937; in January 1939 electrical equipment for 70 locomotives ordered from Metropolitan-
Vickers with final assembly at Doncaster; the order cut to one prototype in November 1939; the
prototype completed August 1940; authority to build production EM1s in July 1946, orders placed
after nationalisation (24 from Darlington in January 1948, cancelled; 57 from Gorton in July
1948), built 1950-53 with electrical equipment fitted at Dukinfield; seven EM2 built 1953-54.
The only 1930s figure is the April 1938 contract report of £1,800,000 placed jointly with British
Insulated Cables for overhead line and cable and with Metropolitan-Vickers for "motive units for
70 electric locomotives". That is a joint contract and must not be divided into a per-locomotive
price. **Regime**: any EM1/EM2 price is a British Railways (1948 onwards) price, not an LNER one;
the prototype's price would be LNER, 1940, and was not found.

### 2.10 London & South Western Railway, 1915 — multiple-unit stock

Three corrections to the brief, each from a contemporary or specialist source:

- **600 V DC third rail, not 1,500 V.** The Electric Railway Journal of 7 August 1915 describes
  the scheme and states: "it was decided to adopt direct current with a pressure of 600 volts on
  the third-rail". The substation busbars were 660 V, dropping to a nominal 600 V at the rail,
  chosen for compatibility with the District Railway over the Putney-Wimbledon joint line.
- **British Westinghouse, not British Thomson-Houston.** The traction-equipment contract of March
  1913 for design, manufacture and installation was won by the British Westinghouse Electric and
  Manufacturing Company of Trafford Park. The motors were Westinghouse type 339, 275 hp, four per
  three-car unit (two per motor bogie), 1,100 hp per unit; control was Westinghouse all-electric
  with automatic acceleration.
- **The bodies were conversions, not new build.** All 252 cars were converted at Eastleigh from
  LSWR bogie-block steam coaches built 1902-1912. British Westinghouse staff installed the
  electrical equipment at Eastleigh, using shop-floor space given to them. The LSWR calculated
  that conversion saved about £56,000 against building new stock.

**Price.** The final reported cost of converting the rolling stock was "just over £383,000":
£1,520 per car, £4,560 per three-car unit, at 1915-17 prices. No separate value for the
Westinghouse contract was found, so the mechanical/electrical split is not measurable here. The
whole scheme had spent £970,000 to 31 December 1915 (Electric Railway Journal 1916, reporting the
LSWR annual meeting), against a 1913 stage-one estimate of £1.16 million.

**Seating.** 178-190 seats per three-car unit, about a quarter first class. The three formation
patterns were 40 first + 150 third (190), 42 + 140 (182) and 48 + 130 (178). Motor brake thirds
seated 60 third class; trailers seated 70-74 in mixed first and third compartments.

**Reliability, contemporary statements.**

- Trial running, 1914: "teething problems ... associated with the automatic relay control" stopped
  further unit deliveries until November 1914 (BloodandCustard).
- Opening: the Kingston roundabout service, planned for 5 December 1915, was delayed to 30 January
  1916 by "various problems" (same source).
- Annual meeting, reported in the Electric Railway Journal for 1916: the delay in completing the
  power house forced the company to work "under very serious difficulties"; overcrowding occurred
  on the circular service in the morning and evening peaks; bookings rose 16 per cent in the second
  week of electric operation.
- Longer term: the original bogies caused "concern owing to poor riding and wear"; 382 bogies were
  modified between 1928 and 1933 and a further 178 new bogies were ordered in 1935-36.

No failure rate, availability percentage or mean-distance-between-failures figure was found for
this stock, so reliability can be described but not quantified.

**The pakset objects.** `LSWR-EMU(front)`, `LSWR-EMU(centre)` and `LSWR-EMU(rear)` form a
two-motor, one-trailer unit, which matches the prototype formation; the centre car is unpowered,
correctly. The three objects seat 70 + 78 + 70 = 218, against the 178-190 historical range, so a
per-seat price built on 218 seats would be understated by 15-23 per cent. The objects carry a June
1913 introduction date; trial running began in June 1914 and public service on 25 October 1915.

### 2.11 London Brighton & South Coast, 1909 — absent from the pakset

The 1909 Brighton overhead AC stock is **not modelled**. There are 63 `lbscr-*` object files under
`New/trains/`, all steam locomotives or steam-hauled carriages. The only electric-adjacent LBSCR
items are:

- `lbscr-sub-bogie-48ft` and `lbscr-sub-bogie-54ft`, steam suburban carriage bodies;
- `lbscr-48ft-augmentation-trailer-*` and `lbscr-54ft-augmentation-trailer-*` in
  `sr-augmentation-trailers.dat`, which are trailers for the Southern 3-SUB units, not the 1909
  stock.

No object named for the 1909 AC system, the South London line, or an LBSCR electric multiple unit
exists. If the stock is to be modelled it must be created; there is nothing to reprice.

---

## 3. What the electrical share of the cost was

Four pieces of evidence, of decreasing directness:

1. **EF1, 1913 — a measured split.** Electrical parts £4,012 per locomotive, mechanical parts
   built in-house and unpriced. Weight split 32.6 per cent electrical. If electrical equipment
   was 40-45 per cent of the works cost, the complete machine was about £9,000-10,000, which is
   consistent with the £200,000 scheme total once permanent way (£63,600), substations (£13,000)
   and erection are deducted. Treat the 40-45 per cent as an inference, not a measurement.
2. **District, 1905 — component prices.** A 200 hp BTH motor cost £225; four cost £900. Control
   equipment for a whole train cost £360, so a locomotive's control gear was a few hundred
   pounds. Electrical kit for an 800 hp locomotive was therefore of the order of £1,300-1,500
   against a complete machine that cannot have been much under £4,000-5,000 (inference from the
   component total and the contemporaneous ES1 price). That is nearer 30 per cent than 45.
3. **Waterloo & City, 1897 — an upper bound.** Siemens's £55,913 covered generation,
   distribution and train equipment, against £21,675 for the car bodies. Allocating the whole
   Siemens contract to the vehicles would make electrical equipment 72 per cent of the total;
   because it includes the power station, the true vehicle share is lower. It confirms the order
   of magnitude: on early multiple-unit stock the electrical contract was worth two to three
   times the body contract.
4. **ES1 and Metropolitan 1922-23 — no split.** Both were single contracts (BTH turnkey; Metrovick
   rebuild and new build), so neither separates mechanical from electrical.

**Working conclusion**: for a 1900-1925 electric locomotive, electrical equipment was roughly a
third by weight and 35-45 per cent by cost; mechanical parts and erection were the remainder. The
practical consequence for the pakset is that an "electrical equipment" price found in isolation
should be multiplied by about 2.2-2.8 to reach a complete machine.

---

## 4. Bringing the prices to 1900 money

Using the `vehicle purchase` index in `New/config/prices.tab` (1900 = 100): 1902 = 87, 1913 = 98,
1919 = 224, 1922 = 233, 1923 = 146, 1951 = 323, 1955 = 391.

| Class | Year | Nominal, per loco | 1900 GBP | Power, hp | 1900 GBP per hp |
|---|---|---|---|---|---|
| NER ES1 | 1902 | £2,365 | £2,718 | 480 | 5.66 |
| NER EF1, electrical only | 1913 | £4,012 | £4,094 | 1,100 (one-hour; pakset 820) | 3.72 |
| Metropolitan (Metro-Vick) | 1922 | £11,000 | £4,721 | 1,200 | 3.93 |
| NER EE1 (prototype) | 1922 | £27,767 | £11,917 | 1,342 | 8.88 |
| Riddles generic electric | 1951 | £37,400 | £11,579 | 1,500-1,800 | 6.4-7.7 |
| 1955 plan average | 1955 | £55,000 | £14,066 | 1,500-1,800 | 7.8-9.4 |

**Caveat on the index.** The `vehicle purchase` series falls from 233 in 1922 to 146 in 1923, a
37 per cent drop in one year. That is a splice artefact, not a price movement, and it makes any
1923 price deflate very differently from a 1922 one. The Metropolitan project outturn of £312,000
falls in 1923 and would come to £10,685 per locomotive at that index, against £4,721 on the 1922
per-loco figure. The two cannot both be right. The 1922 per-loco figure is used for the ladder
because it is the price of a locomotive rather than an average over a contract that includes
rebuilds; the discrepancy is recorded rather than resolved.

---

## 5. A recommended early-electric ladder

### 5.1 What the measured points say

The two series-production machines — ES1 (1902, 2 off) and Metropolitan (1922, 20 off) — give
£5.66 and £3.93 per horsepower in 1900 money. The one prototype, EE1, gives £8.88, roughly twice
the series level. The post-war points are higher again: £6.4-7.7 per horsepower in 1951 and
£7.8-9.4 in 1955, and the 1951 Manchester-Sheffield figure already in the parent's evidence
(£17,650 per 1,000 drawbar hp) is £5.47 per drawbar hp in 1900 money.

So the measured shape is: **about £4-5.5 per horsepower in 1900 money for 1902-1922 series
production, doubling for a one-off prototype, and rising to about £7-8 per horsepower by the
early 1950s.**

### 5.2 Against the current ladder

`28 x power^0.889` (1900 GBP) gives, at the pakset's powers:

| Class | Power | Current ladder | Measured, 1900 GBP | Ratio |
|---|---|---|---|---|
| NER ES1 | 480 | £6,773 | £2,718 | 2.49 |
| NER EF1 | 820 | £10,903 | not measured (electrical only £4,094) | — |
| Metropolitan 1922 | 1,200 | £15,295 | £4,721 | 3.24 |
| NER EE1 | 1,342 | £16,894 | £11,917 | 1.42 |
| LNER EM1 | 1,400 | £17,541 | no measured price | — |
| LNER EM2 | 2,060 | £24,728 | no measured price | — |
| Tyneside MPV | 200 | £3,110 | no measured price | — |

The ladder is 2.5 times too high at 480 hp and 3.2 times too high at 1,200 hp on series machines,
and 1.4 times too high on the prototype. It is nowhere too low. This is consistent with the
ladder having been fitted largely to diesel points, which are dearer per horsepower than
electrics of any era.

### 5.3 Proposed form

For electric locomotives before 1935, price in 1900 GBP as:

```
price = 4.4 x power          (series production, 2 or more built)
price = 8.8 x power          (one-off prototype)
```

that is, £4.4 per horsepower for a series machine and £8.8 for a prototype, with no meaningful
convexity: two points cannot support a power exponent different from 1. Checks: 480 hp £2,112
(measured £2,718, −22 per cent); 1,200 hp £5,280 (measured £4,721, +12 per cent); 1,342 hp
prototype £11,810 (measured £11,917, −1 per cent).

For 1948-1955 machines use £7.0 per horsepower, i.e. `price = 7.0 x power`: 1,400 hp £9,800;
2,060 hp £14,420. These sit below the 1951 Riddles and 1955 plan figures (£11,600 and £14,100 at
1,500-1,800 hp) but within their range.

A single equation across 1890-1955 is not supportable on six points with a factor-of-two
prototype effect and a real-terms rise after 1945. Two brackets, pre-1935 and post-1948, with an
explicit prototype multiplier, is the honest form.

### 5.4 What this implies for the six NER/LNER objects

1900 GBP, for the parent to convert, not `.dat` values:

| Object | Power | Series rule | Prototype rule | Current ladder |
|---|---|---|---|---|
| ner-classes1 (ES1) | 480 | £2,110 | — | £6,773 |
| ner-classef1 (EF1) | 820 | £3,610 | — | £10,903 |
| ner-classee1 (EE1) | 1,342 | £5,900 | £11,810 | £16,894 |
| ner-tyneside-mpv | 200 | £880 | — | £3,110 |
| lner-classem1 (EM1) | 1,400 | £9,800 | — | £17,541 |
| lner-classem2 (EM2) | 2,060 | £14,420 | — | £24,728 |

The EE1 is the one object where the measured price supports the current ladder's order of
magnitude, because it is a prototype. The motor parcel van is the worst case: the ladder prices a
200 hp parcels vehicle at £3,110 in 1900 money, more than the measured ES1 locomotive of 480 hp.

### 5.5 The per-seat anchor for early electric multiple-unit stock

The LSWR conversion gives the only measured per-car price for an early British electric multiple
unit: £1,520 per car in 1915, or £4,560 per three-car unit of 178-190 seats. That is about £24-26
per seat in 1915 money, or £22-24 per seat in 1900 money on the `vehicle purchase` index of 110 for
1915. Two cautions apply:

- The bodies were conversions of coaches already about ten years old, so the figure is a
  conversion-plus-equipment price, not a new-build price. New construction was estimated at only
  about £56,000 more across 252 cars, so the new-build equivalent is roughly £1,742 per car, about
  £28-29 per seat in 1915 money and £25-27 in 1900 money.
- The pakset's three objects seat 218 per unit, against 178-190 historically. Either the payloads
  or the per-seat price must be corrected; using 218 seats with the historical price would
  understate the per-seat cost by 15-23 per cent.

No equivalent measured figure was found for the LBSCR 1909 stock, which is not in the pakset.

---

## 6. Dead ends, recorded explicitly

1. **City & South London, 1890.** Checked: The Engineer vol 70 (1890), including the 7 November
   1890 article on the line (14 locomotives described, no price); Hopkinson's ICE paper of 14
   February 1893 (partial text retrieved; the appendix cost table was not reachable); Reilly's
   1985 Liverpool PhD thesis on British and American urban electric railways (read in full text;
   operating costs only, no purchase prices). The company's accounts survive as TfL Corporate
   Archives LT001652/001 (1884-1911) and were not consulted.
2. **District Railway, 1905.** Checked: LURS "District Electric Trains 8 — Electric Locomotives"
   (Connor); gbtrains class page; Street Railway Journal vol 26 (1905), including the 26 August
   1905 article on the Metropolitan locomotives. No contract value in any of them.
3. **Metropolitan Railway, 1905-07.** Checked: LURS Connor/Horsey paper on the Westinghouse
   locomotives (no monetary figures at all); Street Railway Journal vol 26 (1905) article; the
   Metropolitan Railway 1922 accounts (OCR unusable). The 1905-07 contract values remain
   unrecovered.
4. **Harton, 1908.** Checked: Electric Railway Journal vol 37 (1911) p. 925; Durham Mining Museum's
   reproduction of the 1933 Colliery Engineering article. Six locomotives, no capital figure.
5. **Waterloo & City.** No main-line electric locomotives to price (section 2.4).
6. **Lancashire & Yorkshire.** No 1,200 V locomotive class to price (section 2.6).
7. **London Brighton & South Coast 1909.** Not a locomotive class, and not in the pakset
   (section 2.11); no object exists to price.
8. **Bury 1917 and MSJ&AR 1904.** No electric locomotive found for either (section 2.8).
9. **EM1 and EM2.** No unit price found. Order, build and equipment-contract history recovered;
   money not.
10. **LSWR rolling-stock split.** Only the combined cost of converting the 252 cars was found
    (£383,000). The value of the March 1913 British Westinghouse contract, and therefore the
    mechanical/electrical split, was not recovered. The 1912 Jones report on electrification
    (Railways Archive docID 7676) survives only as a 52-page draft and its appendices are not
    online.
11. **LBSCR 1909 stock.** Absent from the pakset (section 2.11); no price researched, because
    there is no object to price.
12. **Metropolitan Railway 1923 index discontinuity.** The `vehicle purchase` series drops 37 per
    cent between 1922 and 1923, which makes the 1923 outturn figure unusable for deflation without
    a decision on the splice.

## 7. Where the missing prices are likely to be

- **North Eastern**: the company's board and Locomotive Committee minutes in The National
  Archives RAIL series; Ken Hoole, *The Electric Locomotives of the North Eastern Railway*
  (Oakwood, 1988); Ken Appleby, *Shildon-Newport in Retrospect* (RCTS). The 1913 contract values
  are in the contemporary technical press, which is where the one solid EF1 figure came from; a
  page-by-page read of The Engineer for 1913-1915 should yield the mechanical contract too.
- **Metropolitan**: Metropolitan Railway minutes at London Metropolitan Archives, GLC Acc
  1297/MET (the class used by Reilly); Ken Benest, *Metropolitan Electric Locomotives* (LURS,
  1984); the LURS journal for the 2024 Horsey research.
- **District and Underground group**: London Transport Museum archives, LT000258 series, and the
  UERL/District board minutes; the 1905 B stock order papers carry the component prices and
  probably the locomotive contract value.
- **City & South London**: TfL Corporate Archives LT001652/001; the Mather & Platt contract of
  January 1889 is the document to find, and it covered 14 locomotives, the generating plant and a
  two-year working guarantee in one sum, so it may never yield a clean per-locomotive price.
- **Harton**: William J. Hatcher, *The Harton Electric Railway* (Oakwood, 1994); Harton Coal
  Company accounts.
- **LSWR**: Herbert Jones's report of 6 December 1912 on the electrification (a near-final draft
  survives; Railways Archive docID 7676) and the LSWR board minutes at The National Archives that
  the same entry cites; the British Westinghouse traction contract of March 1913 is the document
  that would give the mechanical/electrical split.

## 8. Confidence

| Figure | Confidence | Reason |
|---|---|---|
| ES1 £2,365 each (1902) | medium-high | specific contract price, contemporaneous order date, corroborated by the 1902 estimate |
| EF1 electrical $19,500 each (1913) | medium-high | contemporary contract report; electrical only; USD conversion at 4.86 |
| Shildon-Newport £200,000 total | medium | newspaper summary of the scheme, consistent with the contract figures |
| EE1 £27,767 (1922) | medium | enthusiast encyclopedia, but a precise figure against a stated authorisation |
| Metropolitan £11,000 each (1922) | low-medium | unsourced class-profile site, consistent with its own £220,000 total |
| Metropolitan £312,000 / £15,600 (1923) | medium | LURS account of archive research; project total including rebuilds |
| Riddles £37,400 (1951) | medium | secondary citation of a published table; class and power unstated |
| W&C £55,913 and £21,675 (1897) | medium | Wikipedia citing ICE Proceedings; not locomotives |
| LSWR £383,000 for 252 cars (1915) | medium-low | detailed specialist site with a specific figure, but no document cited |
| LSWR £970,000 scheme spend (1915) | medium-high | contemporary Electric Railway Journal report of the annual meeting |
| BTH motor £225 (1905) | medium-high | LURS reproduction of order prices |

## 9. Open questions

- Is the EE1's £27,767 a works cost or a total including the electrical contract? The source says
  "final cost" without a scope statement, and the electrical equipment was a separate Metrovick
  contract.
- Did the Metropolitan's £312,000 include the value of the twenty old locomotives' recovered
  equipment? If so the true new-build cost is higher than £15,600 each.
- Which of the two 1922-23 Metropolitan figures should stand: £11,000 per locomotive or the
  £15,600 project average? A contract schedule from the Met minutes would settle it.
- What is the correct 1922-1923 splice in the `vehicle purchase` index, and should the 1923-1927
  block be re-examined before any 1923 price is used?
- Was the LSWR's £383,000 a works cost or a total including the British Westinghouse contract?
  The two would be the same if Westinghouse's work was charged through Eastleigh, which the
  installation arrangement suggests, but no source states it.
- Should the pakset's LSWR objects carry 218 seats or the historical 178-190? The per-seat
  price cannot be settled until this is decided.
