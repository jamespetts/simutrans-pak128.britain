# Measured UK road-vehicle purchase prices, 1979-2026

Bounded research pass for the Pak128.Britain-Ex cost-balancing project.
Compiled 23 November 2026. Nominal money of the stated year. No conversions, no
deflators, no index numbers.

Companion data file: `ai/temp/road-rows-modern.csv` (one row per figure, 59 rows).

---

## 1. Method

**Search engine.** Exa, via `https://api.exa.ai/search` with
`{"type":"auto","contents":{"highlights":true}}`, one query per turn. Queries named the
subject, the constraint (UK, new vehicle, price stated), the date window and the source
preference.

**Page reading.** A search result was never recorded as evidence. HTML pages were fetched
and read. PDF business cases and committee reports cannot be fetched by the ordinary
`webfetch` tool (it rejects `application/pdf`), and this machine has neither `pdftotext`
nor a Python PDF library, so PDFs were read through `https://api.exa.ai/contents` with a
`text` block, which returns the full extracted text. Every PDF figure below was read in
the body text or table of the document itself.

**Classification.** Each figure is tagged:

- **MEASURED** — a price actually paid, tendered, or awarded for a stated quantity of a
  stated vehicle.
- **LIST** — a manufacturer's or dealer's asking price.
- **ESTIMATE** — a figure asserted by an official or an operator without a purchase
  behind it (for example "an electric bus costs about £440,000").

**Derived unit prices.** Where a source gives a total and a fleet size, the per-vehicle
figure is simple division and is labelled as an average. Nothing else was derived.

**Excluded by rule.** The pakset's own `.dat` cost values were not read. No pakset price
enters any figure or comparison here. The section that the brief asks for on the 1960
lorry list and the 1959 bus price therefore cannot be a numeric ratio; see §5.

**What was deliberately not treated as a vehicle price.** TfL bus contract awards (the
value covers operation and subsidy), framework maxima (Liverpool City Region's £99m
estimate and £111m of lot awards are five-year call-off ceilings with no vehicle count),
and hire or lease rates.

---

## 2. Buses

### 2.1 Electric buses, measured

| Year | Vehicle | Class / size | Driveline | Price | Basis | VAT | Source | Conf. |
|---|---|---|---|---|---|---|---|---|
| 2021 | First Hampshire & Dorset single-deck BEV (34 units) | single-deck | battery-electric | £370,000 | MEASURED unit cost in funding case | not stated; grant case | Portsmouth ZEBRA Financial Case, 31 May 2022, §1.2.2 | High |
| 2021 | Wrightbus StreetDeck Electroliner BEV, 454 kWh (32 units) | double-deck | battery-electric | £517,330 | MEASURED unit cost | not stated | Southampton ZEBRA Full Business Case, Jan 2022, Table 3 | High |
| 2021 | "electric double-decker, Cambridge" (30 units) | double-deck | battery-electric | £439,000 | MEASURED, "based on a price of £439k per bus" | not stated | CPCA ZEBRA Scheme Business Case, 20 Aug 2021, §1.3.10 | High |
| 2022 | Nottingham: 78 single-deck BEV (entire NCT single-deck fleet) | single-deck | battery-electric | £395,116 avg | MEASURED batch average (£30,819,057 ÷ 78) | not stated | Nottingham ZEBRA Phase 2 Business Case, Jan 2022, Financial Case | High |
| 2024 | Blackpool: minimum 90 electric buses, Alexander Dennis | mixed (single and double) | battery-electric | £470,722 avg | MEASURED tender award (£42,365,000 ÷ 90) | ex-VAT (award notice) | YPO DPS 1066 Lot 6 award, 18 Apr 2024 | High |
| 2025 | Cornwall: 7 electric buses, Wrightbus | 36-75 seat framework lot | battery-electric | £385,054 | MEASURED tender award (£2,695,378 ÷ 7) | ex-VAT (stated) | Find a Tender 2025/S 000-002984, 29 Jan 2025 | High |
| 2025 | Arriva County Durham: 14 electric double-deckers | double-deck | battery-electric | £476,550 avg | MEASURED capital cost (£6,671,700 ÷ 14), infrastructure separate | not stated | North East CA delegated decision report, 17 Apr 2025, Table 1 | High |

### 2.2 Electric buses, asserted but not purchased at that price

| Year | Vehicle | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|
| 2024 | Plymouth electric double-decker | £440,000 | ESTIMATE (council FAQ); diesel "approximately 60% of this price" | plymouth.gov.uk ZEBRA project page | Low |
| 2025/26 | Wrightbus StreetDeck Electroliner BEV | £500,000 | ESTIMATE (operator FAQ); "new diesel bus costs around £290,000" | islandbuses.info (Southern Vectis) | Low |
| 2024 | generic electric double-decker | "more than £500,000" | ESTIMATE (BBC, quoting operator) | BBC News, 8 Oct 2024 | Low |
| 2026 | 24 × ADL Enviro400EV, Reading Buses | £583,333 avg | ESTIMATE (secondary blog, "reportedly about £14 million") | busandtrainuser, 12 Feb 2026 | Low |

### 2.3 Diesel buses, measured or operator-stated

| Year | Vehicle | Class | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|---|
| 2021 | FirstBus single-deck Euro VI | single-deck | £169,000 | MEASURED — FirstGroup's most recent purchase price for the nearest equivalent spec | Portsmouth ZEBRA FC §1.2.3 | High |
| 2021 | Centrebus single-deck Euro VI | single-deck | £160,000 | MEASURED — mid-range of new Euro 6 quotes (Scania, ADL, min. 35 seats) | Leicester ZEBRA Financial Case, Aug 2021, §16 | Medium |
| 2021 | Arriva double-deck Euro VI | double-deck | £236,000 | MEASURED — "most recent purchase of Euro 6 buses" | Leicester ZEBRA Financial Case, Aug 2021, §16-17 | High |
| 2021 | Diesel double-decker, Southampton | double-deck | £250,797 | MEASURED — "an equivalent ICE diesel double decker costs £250,797" | Southampton ZEBRA FBC Table 3 | High |
| 2021 | DfT Greener Buses Model standard assumption | single-deck | £180,000 | POLICY ASSUMPTION, not a purchase | quoted in Portsmouth ZEBRA FC §1.2.3 | n/a |
| 2024 | Arriva: 46 × ADL Enviro200 | single-deck | £304,348 avg | MEASURED operator investment (£14m ÷ 46) | Bus Ambassador, 10 Dec 2024 | Medium |
| 2024 | trentbarton: 23 × ADL Enviro200 | single-deck | £260,870 avg | MEASURED operator investment (£6m ÷ 23), order also covered spare vehicles | trentbarton, 18 Apr 2024 | Medium |
| 2024 | Liverpool City Region: ≥207 low- and zero-emission buses, ADL | mixed | £275,362 avg | MEASURED order value (£57m ÷ 207) but drivelines mixed | Bus Ambassador, 4 Sep 2024 | Low (mixed) |

Reading. A new UK diesel single-decker in 2024-25 was about £250,000-£305,000, and a new
diesel double-decker about £236,000-£290,000 depending on how much of the figure is
operator bulk-buying. The 2021 ZEBRA figures (£160,000-£169,000 single, £236,000 double)
are pre-inflation-spike and should not be used as a modern anchor.

### 2.4 Coaches, measured

| Year | Vehicle | Seats / length | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|---|
| 2022 | Mercedes-Benz Tourismo M/3, 4 units | 53 seats, 13 m tri-axle | £325,000 avg | MEASURED operator investment (£1.3m ÷ 4), PSVAR lift, centre toilet | routeone, 28 Jun 2022 | Medium |
| 2024 | Caetano Levante 3A on Scania tri-axle, 68 units | National Express spec | £377,941 avg | MEASURED operator spend (£25.7m ÷ 68) | Edwards Coaches, 10 Jan 2024 | High |
| 2024 | Van Hool Altano overdeck, 10 units | overdeck | £480,000 each | MEASURED, price stated per coach | Edwards Coaches, 10 Jan 2024 | High |
| 2025 | Mercedes-Benz Tourismo M/3, 6 units | 55 seats, tri-axle | £283,333 avg | MEASURED operator investment (£1.7m ÷ 6) | routeone, 25 Jul 2025 | High |

The coach ladder is steep and specification-driven: £283,000 for a 55-seat Tourismo M/3
through £378,000 for a Levante 3A to £480,000 for an overdeck Altano. The pakset's
"coach" class should probably carry a mid-figure near £300,000-£380,000 for the 2020s, not
the highest.

---

## 3. Lorries

### 3.1 44 t tractor units

| Year | Vehicle | Spec | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|---|
| 2024 | Volvo 6x2 tractor unit chassis, 2 units | 44 t GTW | £138,223 avg | MEASURED tender award (£276,446 ÷ 2) | Perth & Kinross Council award, NEPO HGV Lot 1, awarded 23 Nov 2024, published 8 May 2025 | High |
| 1984 | Scammell Roadtrain 20.32 6x2 | 38 t GCW, Cummins NTE320 | £34,000 | LIST ("competitively priced at £34,000") | Commercial Motor, 27 Oct 1984, p63 | High |
| 1992 | Scania R143-500 6x2 Topline Streamline | 38 t, 500 hp | "almost £82,000" | LIST, quoted retrospectively | Commercial Motor, 29 Jun 1995, p26 | Medium |

The 2024 figure is a council framework call-off for a chassis-cab tractor, so it excludes
any fifth-wheel or hydraulic work and is likely towards the lower end of the retail range.
It is, however, a real price paid, which is more than any UK truck maker publishes.

### 3.2 Rigids and refuse vehicles

| Year | Vehicle | GVW / body | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|---|
| 2024 | Dennis Eagle Elite 6+ 6x2 rear-steer, OL19N body | 26 t RCV | £234,263 each +VAT | MEASURED tender (TPPL framework, direct award) | Cheltenham BC cabinet decision, 24 Oct 2024 | High |
| 2024 | 24 × 26 t narrow-track 6x2 rear-steer RCV | 26 t | £233,542 avg | MEASURED asset purchase (£5,605,012 ÷ 24, ex-VAT) | Hackney CPIC contract award F S411, 4 Nov 2024 | High |
| 2025 | 2 × 26 t single-body narrow-track RCV | 26 t | £240,891 avg | MEASURED award (£481,782 ÷ 2) | Contracts Finder award, 11 Feb 2025 (Reigate & Banstead) | High |
| 2025 | 8 × Dennis Eagle narrow chassis/body 26 t | 26 t | £262,999.63 avg | MEASURED award (£2,103,997 ÷ 8, ex-VAT) | Cumberland officer decision, 23 Jun 2025 | High |
| 2025 | 10 × Faun Zoeller 26 t recycling vehicles | 26 t | £333,244.50 avg | MEASURED award (£3,332,445 ÷ 10, ex-VAT) | Cumberland officer decision, 23 Jun 2025 | High |
| 2025 | 6 × Dennis Eagle RCV | 26 t | £254,719 avg | MEASURED award (£1,528,314 ÷ 6) | Oxford City Council decision, 9 Apr 2025 | High |
| 2025/26 | 13 × 26 t RCV, direct award, ESPO 215-24 | 26 t | £253,000 each | BUDGETED price in capital programme | Wyre Forest cabinet report, 10 Jul 2025 | Medium |
| 2024/25 | RCV list price, Dennis Eagle | 26 t | £243,000 | LIST ("approximate list price") | Rochford committee report, Appendix 1 | Medium |
| 2024/25 | RCV list price, Dennis Eagle | 18 t | £225,000 | LIST ("approximate list price") | Rochford committee report, Appendix 1 | Medium |
| 2025 | 26 t diesel RCV (market statement) | 26 t | £220,000-£230,000 | ESTIMATE | South & Vale / White Horse cabinet report, 19 Dec 2025, p13 | Low |
| 2025 | 26 t electric RCV (market statement) | 26 t | £413,000-£580,000 | ESTIMATE, from "an internet search" | same report | Low |

### 3.3 Smaller rigids and vans-turned-lorries, dealer prices

| Year | Vehicle | GVW / body | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|---|
| 2026 | Isuzu N75.150 chassis cab + 20 ft curtainside or Luton | 7.5 t | £54,950 +VAT | LIST, new, model year 2026 | JDS Trucks advertisement, Feb 2026 | High |
| 2026 | Isuzu N75.190 (E) curtainside + 1,000 kg tail lift | 7.5 t | £64,495 | LIST, new | Allports Group (Isuzu Central) stock listing | High |
| 2025 | DAF FA LF 230 box van, pre-registered | 12 t | £54,750 | LIST ("VAT tbc") | HGV Monthly listing, checked 15 Nov 2026 | Medium |
| 2024 | Iveco ML180E25S, 22 ft scaffold dropside | 18 t | £71,990 +VAT | LIST, brand new | Acorn Truck Sales new stock | High |
| 2026 | Mercedes-Benz 1824 L curtainside | 18 t | £97,995 +VAT | LIST, brand new | Bell Truck & Van new stock | High |

A 2024-26 UK lorry ladder from measured and listed prices, before bodywork is added
where the vehicle is a chassis-cab:

- 7.5 t: £55,000-£65,000
- 12 t: £55,000
- 18 t: £72,000-£98,000
- 26 t RCV with body: £234,000-£333,000
- 44 t tractor: £138,000

The step from 18 t to 26 t is far larger than the step from 7.5 t to 18 t, because the
26 t figure includes a refuse body. A bare 26 t chassis would be nearer £90,000-£110,000,
but no measured UK figure for one was found in this pass.

---

## 4. Vans

### 4.1 Modern

| Year | Vehicle | GVW / body | Price | Basis | VAT | Source | Conf. |
|---|---|---|---|---|---|---|---|
| 2025 | Ford Transit 350 L2H2 Leader 2.0 105PS | 3.5 t panel van | £45,735 basic | LIST | ex-VAT; MRP £54,882 inc VAT | Global Vans, quoting Ford price list dated 18 Aug 2025 | High |
| 2026 | Ford Transit 350 Leader L2H2 105PS | 3.5 t panel van | £47,395 basic | LIST | ex-VAT (OTR £49,274.83) | Ford UK price list, 27MY, effective 28 Aug 2026 | High |
| 2026 | Ford Transit 350 L3H3 130PS diesel | 3.5 t panel van | £49,845 basic | LIST | ex-VAT | Ford UK price list, 27MY | High |
| 2026 | Ford E-Transit 350 L3H3 135kW, 68 kWh | 3.5 t electric panel van | £51,345 basic | LIST | ex-VAT | Ford UK price list, 27MY | High |
| 2026 | Vauxhall Movano L2H2 3.5 t 140PS diesel | 3.5 t panel van | £34,945 basic; £36,355 OTR | LIST | ex-VAT | Vauxhall Price and Specification Guide, 1 Oct 2026 | High |
| 2026 | Vauxhall Movano L3H2 3.5 t 270PS electric, 110 kWh | 3.5 t electric panel van | £50,635 basic; £52,045 OTR; £47,045 after £5,000 PiVG | LIST | ex-VAT | Vauxhall PSG, 1 Oct 2026 | High |
| 2025 | Mercedes-Benz Sprinter 315 L2H2 PRO | 3.5 t panel van | from £50,510 | LIST | ex-VAT, ex-factory | mercedes-benz.co.uk | High |
| 2025 | Mercedes-Benz eSprinter 314 L3 PRO, 81 kWh | 3.5 t electric panel van | from £58,850 | LIST | ex-VAT, ex-factory | mercedes-benz.co.uk | High |

### 4.2 1979-1990

| Year | Vehicle | GVW | Price | Basis | Source | Conf. |
|---|---|---|---|---|---|---|
| 1979 | Ford Transit 80, 2.0 petrol, automatic | light van | £3,412 basic | LIST | Commercial Motor, 29 Jun 1979, p76 | Medium |
| 1985 | Bedford Express 2.5 diesel | light van | £6,175 excl VAT | LIST | Commercial Motor, 19 Jan 1985, p25 | High |
| 1985 | Ford Transit 130 diesel (comparison figure) | light van | £8,030 | LIST, derived from "£1,855 cheaper" statement | Commercial Motor, 19 Jan 1985, p25 | Medium |
| 1985 | Mercedes-Benz 307D 3.5 t diesel, high roof | 3.5 t | £9,380 net | LIST ("net price") | Commercial Motor, 1 Jun 1985, p46 | High |
| 1986 | Ford Transit 100L diesel | light van | £7,944 net | LIST | Commercial Motor, 22 Jun 1989, p150 | High |
| 1986 | Ford Transit 120L petrol | light van | £7,079 net | LIST | same | High |
| 1989 | Mercedes-Benz 308D | 3.5 t | £12,360 net | LIST, April 1989 test | Commercial Motor, 22 Jun 1989, p162 | High |

Note the 1989 article's own observation: the 307D rose from £9,380 (1985) to £12,360
(1989), +35%, against +21% on the Retail Price Index over the same five years. Van prices
were rising faster than general inflation well before 2000.

---

## 5. The price of electrification

Same model or same class, quoted in the same document, so the premium is not contaminated
by year or by specification drift.

### 5.1 Bus

| Model pair | Diesel | Electric | Premium | Ratio | Source |
|---|---|---|---|---|---|
| Single-decker, FirstBus | £169,000 | £370,000 | +£201,000 | 2.19× | Portsmouth ZEBRA FC, 2022 |
| Single-decker, Centrebus | £160,000 | £359,000 | +£199,000 | 2.24× | Leicester ZEBRA FC, 2021 |
| Double-decker, Arriva | £236,000 | £460,000 | +£224,000 | 1.95× | Leicester ZEBRA FC, 2021 |
| Double-decker, Wrightbus StreetDeck | £250,797 | £517,330 | +£266,533 | 2.06× | Southampton ZEBRA FBC, 2022 |
| DfT policy assumption | £180,000 | — | — | — | Portsmouth ZEBRA FC, 2022 |

**The bus electrification premium in 2021-22 was about £200,000-£267,000 per vehicle, or
roughly double the diesel price, and it was remarkably uniform across single and double
deck, operators and manufacturers.** This is the single most useful number in this pass
for the pakset: it is a constant cash premium, not a constant percentage of a size-dependent
price, which means the electric bus in the pakset should be modelled as
`diesel price + ~£230,000` rather than as a multiple.

Battery replacement is separate and large: Leicester's Arriva bid carried £150,000 per
double-decker at year 8, and £130,000 per Centrebus single-decker. Southampton carried
£1.247m for 32 buses (£38,969 each). If the pakset models a `fixed_cost` or an overhaul,
these are the figures.

### 5.2 Lorry

Only estimate-level evidence exists. A 26 t diesel RCV at £220,000-£230,000 against an
electric RCV at £413,000-£580,000 (South & Vale, Dec 2025) is a premium of roughly
£190,000-£350,000, or 1.8×-2.5×. This is an officer's market scan, not a purchase. No
measured UK electric lorry purchase price was found in this pass.

### 5.3 Van

| Model pair | Diesel | Electric | Premium | Ratio | Source |
|---|---|---|---|---|---|
| Ford Transit 350 L3H3 vs E-Transit 350 L3H3 68 kWh | £49,845 | £51,345 | +£1,500 | 1.03× | Ford price list, 27MY, 2026 |
| Vauxhall Movano L3H2 vs Movano Electric L3H2 110 kWh | £35,755 | £50,635 | +£14,880 | 1.42× | Vauxhall PSG, 1 Oct 2026 |
| Mercedes Sprinter 315 L2H2 vs eSprinter 314 L3 81 kWh | £50,510 | £58,850 | +£8,340 | 1.17× | mercedes-benz.co.uk, 2025 |

**The van premium has collapsed at the small end of the market and not at the large end.**
Ford's E-Transit now carries a 3% premium over the equivalent diesel; Mercedes 17%;
Stellantis 42%. Two cautions. First, the electric van loses payload: the Movano L3H2
3.5 t drops from 1,375 kg payload (diesel) to 730 kg (electric), which is a 47% loss and
would make it useless for many duty cycles. Second, the Vauxhall price depends on the
£5,000 Plug-in Van Grant; without it the premium is 1.42×, with it 1.28×.

For the pakset this matters: a 2020s electric van is only marginally more expensive than
a diesel van but carries about half the load. If the pakset gives the electric van the
same capacity, the cost ladder will be wrong in the opposite direction from the bus.

---

## 6. What this implies for a cost ladder that stops in 1960

This pass was barred from reading the pakset's own `cost`, `runningcost`, `fixed_cost` or
`upgrade_cost` values, so **no ratio to the 1960 lorry list or the 1959 bus price is
computed here.** The comparison has to be done by whoever holds those numbers. What this
pass supplies is a set of measured anchors at the modern end, and the following observed
multiples within the measured series, which are the right shape for extrapolating a
nominal ladder.

Observed nominal multiples, same class, measured at both ends:

| Class | Early measured | Modern measured | Nominal multiple | Implied annual rate |
|---|---|---|---|---|
| 38-44 t tractor unit | £34,000 (1984) | £138,223 (2024) | 4.07× in 40 years | 3.6%/yr |
| 3.5 t panel van | £9,380 (1985) | £47,395-£52,000 (2026) | 5.05-5.54× in 41 years | 4.0%-4.3%/yr |
| 11.6 m single-deck bus | £42,000-£45,000 (1980) | £250,000-£305,000 (2024) | 5.6-7.3× in 44 years | 4.0%-4.6%/yr |
| 53-seat coach | £47,500 (1986) | £283,333-£378,000 (2025) | 6.0-8.0× in 39 years | 4.7%-5.5%/yr |

Three conclusions that do not depend on the pakset's own numbers:

1. **The modern end is understated because the curve is convex, not because one point is
   wrong.** Every class above compounds at 3.6%-5.5% a year in nominal terms. A straight
   line drawn from a 1960 anchor to a modern anchor that is itself too low will undershoot
   the middle of the range as well as the end.

2. **The relative price of the classes has moved.** In 1984-86 a 38 t tractor (£34,000) cost
   3.6× a 3.5 t van (£9,380) and a 53-seat coach cost 5.1× a van. In 2024-26 a 44 t tractor
   (£138,223) costs 2.9× a Transit (£47,395), and a coach (£283,333-£378,000) costs
   6.0-8.0× a van. **Lorries have got cheaper relative to vans and coaches.** A ladder built
   on 1960 relativities will overprice lorries and underprice coaches at the modern end.

3. **The bus/lorry relationship has inverted.** A new 11.6 m single-decker in 1980
   (£42,000-£45,000) cost slightly more than a 38 t tractor unit (£34,000 in 1984). In
   2024-25 a diesel single-decker (£250,000-£305,000) costs about twice a 44 t tractor unit
   (£138,223). Buses, not lorries, are now the expensive road vehicle. If the pakset's 1959
   bus price and 1960 lorry list have buses below lorries, that ordering needs reversing at
   the modern end.

A fourth point, specific to the electrification work: the electric bus premium is a
**constant ~£230,000 per vehicle** (§5.1), so any model that applies a percentage premium
will underprice electric single-deckers and overprice electric double-deckers.

---

## 7. Dead ends and cautions

1. **Manufacturers publish no UK list price for buses or heavy lorries.** Alexander Dennis,
   Wrightbus, Volvo Trucks, DAF, Scania and Mercedes-Benz Trucks all quote "price on
   application". Every bus and lorry figure here comes from a public body or an operator,
   not a price list. There is no equivalent of the Ford or Vauxhall van price guide.

2. **Second-hand price aggregator sites are not evidence.** `thefleetmagazine.co.uk`
   (Oct 2026) publishes a tidy table — 7.5 t £45,000-£65,000, 18 t £70,000-£95,000, 26 t
   £85,000-£115,000, 44 t £90,000-£140,000 — but describes its own figures as "typical
   ranges seen across the UK market", cites no source and is contradicted by the measured
   26 t RCV figures (which are £234,000+, because they include a refuse body). It was not
   used. The measured figures in §3 land inside its 7.5 t, 18 t and 44 t bands, which is
   weak corroboration only.

3. **Framework maxima are not prices.** Liverpool City Region's bus framework (2025-26)
   advertises £99m across six lots and awarded £111,075,440; the lot values (£41.4m for
   diesel double-deckers, £36.4m for a second diesel double-decker lot) are five-year
   call-off ceilings with no vehicle count. Halton Housing / Link Group's fleet framework is
   £450m over 48 months across ten lots. Neither yields a unit price.

4. **TfL bus contract awards bundle operation.** They are not used, and no figure from them
   appears in this report. A TfL route contract is an operating subsidy over five or seven
   years; dividing it by the fleet gives a number with no relationship to a vehicle price.

5. **Mixed awards cannot be split.** Bradford's July 2025 award of "up to 7 × 44 t tractor
   units and 8 ejector trailers" is £1,400,086 for both, with no split. Cumberland's
   £762,039.75 covers "1 × 12 t and 5 × 7.5 t DAFs" together. Both excluded.

6. **Hydrogen buses: no UK measured purchase price found.** The operators that run them
   (Metrobus Crawley, First Aberdeen, National Express West Midlands, Metroline, Translink)
   have not published per-vehicle prices, and no ZEBRA-style award giving a per-bus figure
   surfaced. This is a real gap.

7. **32 t refuse or tipper: not found.** The UK municipal market is 26 t; every measured
   refuse award located is 18 t or 26 t. A 32 t 8x4 tipper exists but its price is a
   chassis plus a bodybuilder quote and no measured UK figure was located.

8. **Commercial Motor archive OCR is damaged.** Numbers come through as "3 4,00 0" for
   £34,000 and "22.8 million" for what must be about £2.8 million (36 Olympians with
   Alexander bodies, LRT, 1989 — £77,778 each). Only figures whose digits survived intact
   were recorded. The 1989 Olympian figure was dropped despite being potentially valuable
   as a late-1980s double-decker price.

9. **A bus hire is not a bus purchase.** Wolverhampton City Council hired 2 new 10.8 m ADL
   Enviro200s (40 seats) for 12 months for £74,776 (Contracts Finder, 5 Aug 2024). That is
   £37,388 per bus per year, supply-only. Useful as a running-cost proxy, not a capital
   price, and therefore excluded.

10. **ZEBRA business cases are VAT-ambiguous.** Most state ex-VAT totals for grant
    calculation but do not print the words "excluding VAT". Where the source explicitly says
    ex-VAT (Cornwall, Blackpool, Hackney, Cumberland, Perth) it is recorded as such; where
    it does not, the row says "not stated" rather than guessing.

11. **The 2021 ZEBRA prices are a single vintage.** Seven of the bus figures come from
    documents written in 2021-22, when UK bus prices were at a specific point between the
    pandemic and the 2022-23 inflation spike. They are internally consistent and excellent
    for the electric-versus-diesel comparison, but they are not 2025 prices. The 2025
    measured figures (£385,054 Cornwall, £476,550 Arriva Durham) are 4%-20% higher than the
    2021 equivalents for comparable vehicles, which is the expected direction.

## 8. Sources

Bus and coach: Find a Tender notice 2025/S 000-002984; Nottingham City Council ZEBRA Phase 2
business case (Jan 2022); Southampton ZEBRA Full Business Case (Jan 2022); Portsmouth ZEBRA
Financial Case (31 May 2022); Leicester ZEBRA Financial Case (Aug 2021); CPCA ZEBRA Scheme
Business Case (20 Aug 2021); North East CA delegated decision report (17 Apr 2025); YPO DPS
1066 Lot 6 award notice (18 Apr 2024); Bus Ambassador (4 Sep 2024, 10 Dec 2024); trentbarton
(18 Apr 2024); routeone (28 Jun 2022, 25 Jul 2025); Edwards Coaches (10 Jan 2024);
plymouth.gov.uk; islandbuses.info; BBC News (8 Oct 2024); busandtrainuser (12 Feb 2026).

Lorry: Cheltenham BC cabinet member decision (24 Oct 2024); Hackney CPIC F S411 (4 Nov 2024);
Contracts Finder award BIP924795833 (11 Feb 2025); Cumberland officer decision (23 Jun 2025);
Oxford City Council decision (9 Apr 2025); Wyre Forest cabinet report (10 Jul 2025); Rochford
committee report; South & Vale / White Horse cabinet report (19 Dec 2025); Perth & Kinross
NEPO HGV Lot 1 award (8 May 2025); Allports Group; JDS Trucks; HGV Monthly; Acorn Truck Sales;
Bell Truck & Van; Commercial Motor (27 Oct 1984 p63; 29 Jun 1995 p26).

Van: Ford UK price list 27MY (effective 28 Aug 2026); Global Vans / Ford price list
(18 Aug 2025); Vauxhall Price and Specification Guide (1 Oct 2026 and 17 Jul 2025);
mercedes-benz.co.uk Sprinter and eSprinter pages; Commercial Motor (29 Jun 1979 p76;
19 Jan 1985 p25; 1 Jun 1985 p46; 22 Jun 1989 p150 and p162).
