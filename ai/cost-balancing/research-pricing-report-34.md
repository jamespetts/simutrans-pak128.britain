# Battery-electric road vehicles in the UK: measured prices 2010-2026

Bounded research pass for the Pak128.Britain-Ex cost-balancing project.
Compiled 23 November 2026. Nominal money of the stated year. No conversions, no
deflators, no index numbers.

Companion data file: `ai/temp/road-rows-electric.csv` (64 rows, one per figure).

**No pakset `.dat` cost, `runningcost`, `fixed_cost` or `upgrade_cost` value was read, and no
pakset price enters any figure, ratio or recommendation below.**

---

## 1. Method

**Search.** Exa, `https://api.exa.ai/search`, `{"type":"auto","contents":{"highlights":true}}`,
one query per turn. Queries named the subject, the class, the constraint (UK, price stated),
the date window and the source preference (council papers, tender awards, manufacturer price
lists, trade press, in that order). Fourteen searches were run.

**Page reading.** No search result was recorded as evidence. Every PDF and HTML page behind a
row was fetched through `https://api.exa.ai/contents` with a text block and read. Figures were
taken from the body text or a table of the document itself.

**Classification.**

- **MEASURED** — a price paid, tendered, awarded, quoted in a binding supplier offer, or adopted
  in a council decision as the purchase price. Includes contract conversions and ex-demonstrator
  purchases, which are flagged in the notes and excluded from new-vehicle averages.
- **LIST** — a manufacturer's, importer's or dealer's asking price, including price-list "basic"
  prices and trade-show launch prices.
- **ESTIMATE** — a figure asserted by an officer, operator or industry body without a purchase
  behind it, including council budget tables built from "current list prices or industry
  estimates".
- **LEASE** — a contract price that is not a purchase. No lease figure is used in any comparison.

**Derived figures.** Where a source gives a total and a quantity, the unit figure is simple
division and is labelled average. Two derived figures go further and are labelled DERIVED in
the data file: the ZEHID tractor price (§3.6) and the Ipswich implied new price (§3.5).

**Excluded by rule.** Framework maxima and call-off ceilings with no vehicle count; TfL route
contracts (operation, not vehicles); lease and contract-hire rates; TCO parity offers; residual
values; second-hand prices except where explicitly recorded as such; European prices in euros
(recorded once, unconverted, only to show the asking-price level).

**What this pass adds.** The 2026-11-23 modern pass already recorded seven 2021-25 electric bus
awards and four diesel bus prices. Those rows are carried into the tables here, marked
"carried", because the premium cannot be computed without them. All lorry, van, coach, midibus,
hydrogen and tractor rows are new to this pass.

---

## 2. Headline finding

The 2021-25 bus pass concluded that the electric premium is a near-constant **£200,000-£267,000
in cash**, and recommended modelling it as a cash adder. This pass finds that conclusion is an
artefact of looking at one class over a narrow diesel-price band.

Across classes, with both prices taken from the same document, the premium is **proportional**:

| Band | Diesel price | Electric price | Ratio | Cash premium |
|---|---|---|---|---|
| 3.5 t van | £24,000-£50,000 | £33,000-£61,000 | 1.03-1.47× | £1,500-£16,000 |
| 7.5 t tipper | £66,456 | £144,456 | 2.17× | £78,000 |
| 12 t rigid | £120,000-£175,000 | £240,000-£350,000 | 2.00-2.25× | £120,000-£175,000 |
| 18 t rigid | £145,000-£200,000 | £336,000-£400,000 | 2.00-2.32× | £191,000-£200,000 |
| 26 t RCV | £187,215-£215,000 | £435,000-£450,000 | 2.02-2.40× | £220,000-£263,000 |
| Single-deck bus | £160,000-£169,000 | £359,000-£370,000 | 2.19-2.24× | £199,000-£201,000 |
| Double-deck bus | £236,000-£250,797 | £460,000-£517,330 | 1.95-2.06× | £224,000-£267,000 |

The cash premium rises monotonically with the diesel price from £1,500 at the van end to
£267,000 at the double-decker end. The ratio sits at about **2.0** for every class from 7.5 t
upwards, including buses. The bus band looks constant in cash only because a bus's diesel price
(£160,000-£251,000) happens to sit in the same range as a 18-26 t lorry's.

**The rule for heavy vehicles is therefore `electric = 2.0 × diesel`, not `diesel + £230,000`.**
A flat £230,000 adder would price a 7.5 t tipper at £296,000 against a measured £144,456 (105 per
cent too high) and a 12 t RCV at £350,000 against £240,000-£350,000 (at the top of the range).

Two classes do not follow the 2.0× rule: vans (about 1.2×) and coaches (about 1.5×). Hydrogen
buses sit above it at about 2.2×.

---

## 3. Measured and listed figures by class

Basis codes: M = MEASURED, L = LIST, E = ESTIMATE. Full notes, grant treatment and source URLs
are in the CSV.

### 3.1 Buses: single-deck

| Year | Vehicle | Battery / range | Price | Basis | Diesel comparator | Source |
|---|---|---|---|---|---|---|
| 2021 | First Hampshire & Dorset single-deck BEV, 34 units | n/s | £370,000 | M | £169,000 → +£201,000, 2.19× | Portsmouth ZEBRA Financial Case, 31 May 2022, §1.2.2 |
| 2021 | Centrebus single-deck BEV, 6 units | n/s | £359,000 | M | £160,000 → +£199,000, 2.24× | Leicester ZEBRA Financial Case, Aug 2021 |
| 2022 | Nottingham City Transport, 78 units | n/s | £395,116 avg | M | none in document | Nottingham ZEBRA Phase 2 Business Case, Jan 2022 |
| 2024 | Blackpool, min. 90 ADL, mixed single/double | n/s | £470,722 avg | M | none | YPO DPS 1066 Lot 6 award, 18 Apr 2024 |
| 2025 | Cornwall, 7 Wrightbus | n/s | £385,054 avg | M | none | Find a Tender 2025/S 000-002984 |

### 3.2 Buses: double-deck

| Year | Vehicle | Battery / range | Price | Basis | Diesel comparator | Source |
|---|---|---|---|---|---|---|
| 2021 | Arriva double-deck, 22 units | n/s | £460,000 | M | £236,000 → +£224,000, 1.95× | Leicester ZEBRA Financial Case |
| 2021 | Wrightbus StreetDeck Electroliner, 32 units | 454 kWh | £517,330 | M | £250,797 → +£266,533, 2.06× | Southampton ZEBRA FBC, Jan 2022, Table 3 |
| 2021 | Cambridge class price, 30 units | n/s | £439,000 | M | none | CPCA ZEBRA Business Case, 20 Aug 2021, §1.3.10 |
| 2024 | Isle of Wight, 22 ZEBs (Southern Vectis) | n/s | £514,187 avg | M | none | IOW Cabinet report, 9 May 2024, §25 |
| 2025 | Arriva County Durham, 14 units | n/s | £476,550 avg | M | none | North East CA decision, 17 Apr 2025, Table 1 |
| 2025 | Stagecoach North East, 18 units | n/s | £406,644 avg | M | none | North East CA decision, 8 Apr 2025, Table 1 |

### 3.3 Midibuses and minibuses

| Year | Vehicle | Battery / range | Price | Basis | Source |
|---|---|---|---|---|---|
| 2023 | Mellor Orion, Moray, 3 units | n/s | £186,840 | M | Moray Council FOI 101003260058, 23 Mar 2023 |
| 2023 | EVM Cityline, Moray, 2 units | n/s | £231,841 | M | same |
| 2023 | 23-seat e-bus, Islington | n/s | £165,200 | M | Islington Fleet Procurement Plan, Appendix 1 |
| 2023 | 35-seat e-bus, Islington | n/s | £203,000 | M | same |
| 2024 | ADL Enviro100EV 8.5 m, Stagecoach West Scotland, 20 units | 354 kWh, 285 mi | £250,000 avg | M | routeone, 21 Oct 2024 |
| 2025 | BCP Council, 2 midi-buses | n/s | £373,255 avg | M | Contracts Finder, 3 Nov 2025 |

The midibus class has no same-document diesel pair. Against an assumed diesel minibus price of
£95,000-£120,000 (not measured in this pass) the premium would be £70,000-£280,000.

### 3.4 Coaches

| Year | Vehicle | Battery | Price | Basis | Source |
|---|---|---|---|---|---|
| 2019 | Yutong TCe12 | 258 kWh | £305,000 +VAT | L | routeone and Bus & Coach Buyer, 3 Jul 2019 |
| 2023 | Yutong GTe14 | 422 kWh | £485,000 | L | Bus & Coach Buyer, 10 Oct 2023 |
| 2023 | Yutong GTe14 | 563 kWh | £515,000 | L | same |
| 2023 | Yutong U11DD double-decker | 422.87 kWh | £485,000 | L | same |
| 2024 | Yutong GT12 diesel (comparator) | — | £325,000 avg | M | routeone, 22 Aug 2024 |

The only electric/diesel coach pair is cross-model and cross-year: GTe14 at £485,000 against a
GT12 diesel at £325,000 gives +£160,000, 1.49×. Treat as indicative only.

### 3.5 Hydrogen fuel-cell buses

| Year | Vehicle | Battery / H2 | Price | Basis | Diesel comparator | Source |
|---|---|---|---|---|---|---|
| 2019 | Wrightbus hydrogen double-decker, TfL framework, 20 | n/s | £514,000 (2018/19 prices) | M | none | TfL Contracts Finder pricing schedule, scp 001548 |
| 2021 | Wrightbus hydrogen double-decker, Route 7, 20 | 48 kWh + 27 kg H2 | £542,500 | M | £250,797 → +£291,703, 2.16× | TfL FOI-2253-2021, 26 Feb 2021 |
| 2023 | Wrightbus hydrogen bus, Surrey, 34 | n/s | £484,355 avg | M | none | Surrey CC delegated decision, 9 Aug 2023 |
| 2023 | Hydrogen double-decker class price, Liverpool City Region | n/s | £550,000 | E | £210,000 → +£340,000, 2.62× | LCR ZEBRA value-for-money proforma |
| 2023 | Hydrogen bus, Metrobus Crawley | n/s | £500,000 | E | "double" a diesel → about +£250,000, 2.0× | BBC News, 29 Jun 2023 |

The TfL net cost after grants was £238,000 per bus (£1.41m OLEV plus £5.22m FCH JU), which shows
how far grant can move a hydrogen bus and why the gross price must be recorded.

### 3.6 Lorries: rigid

| Year | Class / vehicle | Price | Basis | Diesel comparator | Source |
|---|---|---|---|---|---|
| 2024 | 5.5 t rear-loading RRV, Blaenau Gwent | £94,000 | E | £47,000 → +£47,000, 2.00× | BG Fleet Renewal, Appendix 1 |
| 2024 | 6.5 t Isuzu narrow-access, Blaenau Gwent | £90,000 | E | £45,000 → +£45,000, 2.00× | same |
| 2024 | 7.5 t cage tipper, Thanet | £144,456 | E | £66,456 → +£78,000, 2.17× | Thanet OSP report, 15 Oct 2024 |
| 2024 | 12 t DAF/Romaquip RRV, Blaenau Gwent | £350,000 | E | £175,000 → +£175,000, 2.00× | BG Fleet Renewal |
| 2024 | 12 t DAF RCV, Blaenau Gwent | £240,000 | E | £120,000 → +£120,000, 2.00× | same |
| 2024 | 18 t Dennis RCV, Blaenau Gwent | £400,000 | E | £200,000 → +£200,000, 2.00× | same |
| 2023 | 18 t gritter, Edinburgh | £336,000 | E | £145,000 → +£191,000, 2.32× | Edinburgh Fleet Asset Plan, Nov 2023 |
| 2023 | 26 t RCV, Edinburgh | £435,000 | E | £215,000 → +£220,000, 2.02× | same |
| 2023 | Truck-mounted sweeper, Edinburgh | £385,000 | E | £195,000 → +£190,000, 1.97× | same |
| 2024 | 26 t RCV, Aberdeen | £447,609 | E | £215,000 → +£232,609, 2.08× | Aberdeen Phase 5 Fleet Plan |
| 2024 | 26 t RCV, East Cambridgeshire | £450,000 | E | £187,215 → +£262,785, 2.40× | East Cambs agenda item 8, Dec 2024 |
| 2025 | 26 t eRCV, Lewes | £495,000 | E | none in document | Lewes Cabinet report, 10 Jul 2025 |
| 2025 | 26 t eRCV, Salford (Mercedes/Terberg/Dennis Eagle) | £291,000 | M | none in document | Salford Procurement Board, 19 May 2025 |
| 2022 | 26 t side-loading eRCV, Brighton & Hove | £580,000 | M | none | Brighton & Hove news, 20 May 2022 |
| 2022 | Dennis Eagle eCollect conversion to 26 t | £353,480 | M | none | Find a Tender 2022/S 000-024394 |
| 2021 | Dennis Eagle eCollect conversions, 2 units | £333,886 avg | M | none | Find a Tender 2021/S 001-024636 |
| 2025 | Ex-demonstrator 2021 eRCV, Ipswich | £95,000 | M (used) | council states 74.64% below new | Ipswich decision OD/25/08 |
| 2022 | DAF LF Electric 19 t | £300,000 +VAT | L | diesel LF about £60,000-£70,000 | Move Electric, 30 Apr 2022 |

The Salford £291,000 is the only recent **new** eRCV price that is an actual award rather than a
budget table. It is a discounted single-supplier exception, and it is £144,000-£204,000 below
every council estimate for a 26 t eRCV. Either the estimates are conservative or the Salford
vehicle is a cheaper specification (Mercedes chassis, Dennis Eagle body). It is not enough on
its own to move the class level.

### 3.7 Lorries: 44 t tractor units

| Year | Item | Price | Basis | Source |
|---|---|---|---|---|
| 2024 | Volvo 44 t 6x2 diesel tractor chassis, Perth & Kinross, 2 units | £138,223 avg | M | NEPO HGV Lot 1 award, 8 May 2025 |
| 2026 | Electric 42-44 t tractor, ZEHID programme average, derived at 2.7× diesel | £373,202 | DERIVED | WSP, ZEHID Annual Report 2026, Oct 2026 |
| 2025 | Generic eHGV, Energy UK TCO assumption | £270,000 | E | Energy UK, 30 Sep 2025, footnote 12 |
| 2026 | DAF XF 350 4x2 Electric 525 kWh, new dealer stock, Netherlands | €248,800 | L (EUR) | BAS World listing, 22 Oct 2026 |

**No measured UK purchase price for a new battery-electric tractor unit was found.** This is the
single largest gap in the pass. The ZEHID annual report gives the best available anchor: "the
funded trucks cost around 2.7 times diesel to buy", across more than 240 deployed vehicles, most
of them 42-44 t tractors. Applied to the measured £138,223 diesel price that is £373,202, a cash
premium of £234,979. The Energy UK assumption (1.8×) is the bottom of the plausible band.

The ZEHID ratio is programme-level and includes vehicles bought under demonstration grants, so it
may not be a clean market price. It is, however, a measured programme outcome, not a vendor claim.

### 3.8 Vans and light commercial

| Year | Vehicle | Battery | Price | Basis | Diesel comparator | Source |
|---|---|---|---|---|---|---|
| 2023 | 3.5 t panel van, Aberdeen | n/s | £61,000 | E | £45,000 → +£16,000, 1.36× | Aberdeen Phase 5 Fleet Plan |
| 2023 | Small van, Aberdeen | n/s | £32,825 | E | £24,277 → +£8,548, 1.35× | same |
| 2023 | 3.5 t drop-side, Aberdeen | n/s | £62,400 | E | £52,000 → +£10,400, 1.20× | same |
| 2024 | Ford E-Transit 4.25 t, Islington, 30 units | n/s | £64,742 avg | M | none | Islington decision I028364, 10 May 2024 |
| 2023 | Ford E-Transit 425 cage tipper, Cheltenham | n/s | £67,730 (incl. £5,000 grant) | M | none | Cheltenham decision, 12 Jun 2023 |
| 2025 | 4.25 t electric tipper, Bristol, 9 units | n/s | £70,000 before grant | M | none | Bristol committee, 20 Jan 2025 |
| 2025 | Renault Master E-Tech 87 kWh | 87 kWh, 285 mi | £42,500 basic; £37,500 after PiVG | L | none | Renault UK press release |
| 2026 | Ford E-Transit 350 L3H3 68 kWh | 68 kWh | £51,345 | L | £49,845 → +£1,500, 1.03× | Ford 27MY price list, 28 Aug 2026 |
| 2026 | Vauxhall Movano L3H2 Electric 110 kWh | 110 kWh | £50,635 | L | £34,945 → +£15,690, 1.45× | Vauxhall PSG, 1 Oct 2026 |
| 2025 | Mercedes eSprinter 314 L3 81 kWh | 81 kWh | £58,850 | L | £50,510 → +£8,340, 1.17× | mercedes-benz.co.uk |
| 2026 | Citroen e-Relay L3H2 3.5 t 270 hp | 110 kWh | £49,485 | L | £33,675 → +£15,810, 1.47× | Citroen MY26 price guide, Feb 2026 |
| 2026 | VW e-Transporter T32 70 kWh | 70 kWh | £42,740 | L | £36,415 → +£6,325, 1.17× | VW price list, 3 Nov 2026 |
| 2026 | Ford E-Transit Custom 320 71 kWh | 71 kWh | £43,160 | L | £40,100 → +£3,060, 1.08× | Ford Transit Custom price list |

The van premium is not one number: it ranges from 3 per cent (Ford, 2026) to 47 per cent
(Citroen, 2026), with the after-grant premium as low as 4 per cent. No 2019-22 same-model pair was
found in this pass, so the direction of travel cannot be measured directly; the 2023 Aberdeen
planning prices (1.20-1.36×) are consistent with a higher premium before the 2026 convergence.

The payload penalty is larger than the price premium and is not captured by any of these rows:
the Movano L3H2 3.5 t drops from 1,375 kg to 730 kg (−47 per cent). An electric van that keeps
the diesel's capacity in the pakset will be materially under-costed in operation.

---

## 4. The premium: cash against percentage

### 4.1 Same-document pairs only

| Class | Pairs | Diesel | Premium | Ratio | Confidence |
|---|---|---|---|---|---|
| 3.5 t van | 9 | £24k-£50k | £1.5k-£16k | 1.03-1.47× (median 1.20) | High |
| 7.5 t tipper | 1 | £66,456 | £78,000 | 2.17× | Medium |
| 12 t rigid | 2 (+1 second vintage) | £120k-£175k | £240k-£350k | 2.00-2.25× | Medium |
| 18 t rigid | 2 | £145k-£200k | £191k-£200k | 2.00-2.32× | Medium |
| 26 t RCV | 3 | £187k-£215k | £220k-£263k | 2.02-2.40× | Medium |
| Single-deck bus | 2 | £160k-£169k | £199k-£201k | 2.19-2.24× | High |
| Double-deck bus | 2 | £236k-£251k | £224k-£267k | 1.95-2.06× | High |
| Coach | 1 (weak) | £325,000 | £160,000 | 1.49× | Low |
| Hydrogen bus | 2 | £210k-£251k | £292k-£340k | 2.16-2.62× | Medium |
| 44 t tractor | 0 | £138,223 | £120k-£235k | 1.80-2.70× | Low |

Every heavy class from a 7.5 t tipper to a double-decker sits between 1.95× and 2.40×, and the
median of the twelve heavy-vehicle pairs is **2.07×**. That is a single rule covering buses,
rigids and refuse vehicles, and it is the most useful result of the pass.

### 4.2 Is it constant in cash?

Within one class at one time, yes, approximately: the 2021 bus pairs give £199,000-£267,000.
Across classes, no. The cash premium is £78,000 for a 7.5 t tipper and £1,500 for a Ford E-Transit
in the same market. The apparent constancy in the bus pass came from sampling one class whose
diesel price varied only between £160,000 and £251,000.

The correct description is: **cash premium = diesel price × (ratio − 1)**, with the ratio about
1.0 for heavy vehicles and about 0.2-0.5 for vans and coaches. In cash that produces a rising
schedule, not a flat one.

### 4.3 Has the ratio moved over time?

There is a genuine warning here. The 2024-25 bus awards have no same-document diesel comparator,
but their electric prices (£385,054-£514,187) sit inside or just above the 2021 electric range
(£359,000-£517,330), while the best available 2024 diesel bus prices are £260,870-£304,348 for a
single-decker and about £290,000 for a double-decker. On those figures the 2024-25 bus ratio would
be about 1.3-1.8×, not 2.0×.

I do not treat that as established. The 2024 diesel figures are operator order totals divided by
vehicle counts and may include support packages; the 2021 figures were quotes for a bare vehicle.
What can be said is:

- The electric bus price has been broadly flat in cash from 2021 to 2025 (£359,000-£517,000).
- The diesel bus price rose sharply over the same period.
- If that is right, the *ratio* is compressing while the *cash* premium is falling, from about
  £200,000-£267,000 in 2021 to roughly £80,000-£225,000 in 2024-25.
- Both the "constant cash" and the "constant 2.0×" descriptions are approximations that hold
  within a short window; neither holds across the whole 2021-26 period.

For pakset work covering 2020-2026: use 2.0× for rigid lorries throughout (the 2023-24 pairs are
all at 2.0), and for buses use 2.0× for 2020-23 and 1.6-1.8× for 2024-26. For the earlier electric
era (2010-2019) there is almost no UK price evidence at all; see §7.

### 4.4 Does the premium track battery size?

Partly, but not well enough to use as the rule.

| Vehicle | Battery | Premium | Premium per kWh |
|---|---|---|---|
| Wrightbus StreetDeck Electroliner | 454 kWh | £266,533 | £587 |
| Dennis Eagle eRCV (26 t) | about 300-360 kWh | £220,000-£263,000 | £611-£877 |
| Edinburgh 18 t gritter | n/s | £191,000 | — |
| Yutong GTe14 coach | 422 kWh | £160,000 | £379 |
| ZEHID 44 t tractor (derived) | 450-621 kWh | £234,979 | £378-£522 |
| Vauxhall Movano Electric | 110 kWh | £15,690 | £143 |
| Mercedes eSprinter | 81 kWh | £8,340 | £103 |
| Ford E-Transit | 68 kWh | £1,500 | £22 |

The van end is an order of magnitude cheaper per kWh than the truck end. Battery cost alone does
not explain the premium; integration, low volume, bodywork and market power do. A per-kWh rule
would misprice vans badly. **Use the class multiplier, not £/kWh.**

---

## 5. Grants and VAT

### 5.1 Bus grants

ZEBRA and ScotZEB pay a share of the **difference** between the zero-emission bus and a diesel
equivalent, not a fixed sum per bus. In the ZEBRA 1 business cases the split is 75 per cent grant
/ 25 per cent operator on the vehicle difference and on infrastructure. The recorded bus prices
are therefore **gross vehicle prices before grant**; the grant changes who pays, not the price.

Consequence for the pakset: a ZEBRA-era electric bus should carry the full gross price. Do not net
off the grant. The same applies to the £484,355 Surrey hydrogen bus and the £514,187 Isle of Wight
bus.

### 5.2 Truck grants

The Plug-in Truck Grant (to March 2026) and the Zero Emission Truck Grant (from April 2026) are
applied as a **discount at the point of sale**, so a quoted price may be net. Current caps:

| Weight | From Apr 2026 | Jan-Mar 2026 uplift | Cap as share of price |
|---|---|---|---|
| 4.25-12 t | £15,000 | £20,000 | 20% |
| 12-18 t | £37,000 | £60,000 | 40% |
| 18-26 t | £52,000 | £80,000 | 40% |
| Over 26 t | £81,000 | £120,000 | 40% |

The January 2026 uplift was temporary. The April 2026 caps are lower than the uplift but the
scheme now runs to 2030. The Scottish Zero Emission Truck Fund (from 2027) caps vehicle support at
the **difference in cost** over diesel: £20,000 for 7-12 t and up to £100,000 for over 26 t. That
is a policy estimate of the premium, and it is consistent with a 2.0× rule at the heavy end but
well below it at 7.5 t.

Consequence: where a council price says "including OZEV grant" (Cheltenham, £67,730), the gross
price is £5,000 higher. Where it does not say, assume gross unless the document states otherwise.

### 5.3 Van grants

Plug-in Van Grant: £2,500 small van, £5,000 large van, deducted at the point of sale. The Citroen,
Vauxhall, VW and Renault price lists print both the basic price and the post-grant price. The
premium after grant is 1.04-1.32×, against 1.03-1.47× before it. For the pakset the gross price is
the right capital figure; the grant is a purchase subsidy, not a cost reduction.

### 5.4 VAT

- Council tender awards and Contracts Finder notices are normally ex-VAT, and the ones that say so
  are recorded as such.
- ZEBRA business cases mostly state that all costs exclude VAT; where they do not, the row says
  "VAT not stated".
- Manufacturer van price lists are ex-VAT basic prices; the on-the-road figure including VAT is
  also printed and is not used here.
- TfL's £542,500 is a contract price with no VAT statement.

Do not add VAT to any figure in the CSV. The pakset's price level is a nominal producer price.

---

## 6. Recommendation for the pakset

### 6.1 The rule to apply

| Class | Multiplier on the diesel price | Evidence | Confidence |
|---|---|---|---|
| Minibus (up to 9.5 m) | 2.0× | no direct pair; midibus prices £165k-£373k | Low |
| Single-deck bus (10.5-12 m) | **2.2×** | two 2021 pairs, 2.19-2.24 | High |
| Double-deck bus (10.5-13 m) | **2.0×** | two 2021 pairs, 1.95-2.06 | High |
| Articulated bus | 2.0× | no UK evidence | Low |
| Coach | **1.5×** | one weak cross-model pair | Low |
| Hydrogen bus | **2.2×** | two pairs, 2.16-2.62 | Medium |
| Van 2.0-3.5 t | **1.35×** | nine pairs, 1.03-1.47 | High |
| 4.25 t chassis cab | 1.4× | no pair; E-Transit awards £64,742-£70,000 | Medium |
| 7.5 t rigid | **2.2×** | one pair, 2.17 | Medium |
| 12 t rigid | **2.0×** | two pairs, 2.00-2.25 | Medium |
| 16/18 t rigid | **2.0×** | two pairs, 2.00-2.32 | Medium |
| 26 t rigid / RCV | **2.0×** | three pairs, 2.02-2.40 | Medium |
| 32 t rigid | 2.0× | no UK evidence | Low |
| 44 t tractor | **2.0×** (band 1.8-2.7) | ZEHID 2.7×, Energy UK 1.8×, no invoice | Low |

### 6.2 What this means in practice

1. **Keep the existing 2.00× for battery-electric buses** (the handoff records this as already
   applied). Refine it: single-deckers are 2.2×, double-deckers 2.0×. The current flat 2.0×
   under-prices a single-decker by about £34,000 at 2021 prices.
2. **Extend 2.0× to rigid lorries from 7.5 t upwards.** This is new. The lorry ladder's modern
   real level is a diesel level; the electric variant needs its own multiplier on top of it.
3. **Do not use a flat cash adder.** At the heavy end it happens to give nearly the same answer
   as 2.0× (a 26 t RCV at £215,000 + £230,000 = £445,000 against £435,000-£450,000 in the council
   figures). At 7.5 t it is wrong by a factor of two.
4. **Treat vans separately** at 1.35×, and consider cutting their capacity. The measured payload
   loss is 45-50 per cent on a 3.5 t van and the pakset's capacity field is the place to show it.
   This is a design decision, not a price one; flag it rather than apply it silently.
5. **Coaches at 1.5×**, not 2.0×. The coach carries a large battery but its diesel comparator is
   already expensive, so the percentage premium is lower.
6. **Hydrogen at 2.2×** the diesel bus, with the caveat that the two best pairs are 2021-23 and
   the technology's price is falling.
7. **Battery replacement is a separate cost, not part of the vehicle price.** Leicester costed
   £150,000 per double-decker and £130,000 per single-decker at year 8; Southampton £38,969 per
   bus; Pelican quoted £130,000 for a 17-year battery warranty on a single-decker. If the pakset
   has an overhaul or `fixed_cost` mechanism, these are the figures.
8. **For 2024-26 buses, consider 1.6-1.8×** rather than 2.0×. The electric price has been flat
   while diesel rose. This is a caution, not an established finding, because no same-document
   2024-25 pair exists.

### 6.3 What would change the recommendation

- One measured UK invoice for a 44 t electric tractor. That single number would settle the
  tractor band, which is currently the weakest.
- One 2024-25 ZEBRA business case that prints both the electric and the diesel unit cost in the
  same table. That would settle whether the bus ratio has compressed.
- Two or three actual eRCV awards at the Salford level (£291,000) rather than budget estimates
  (£435,000-£495,000). That would move the 26 t class down by 30 per cent.

---

## 7. Dead ends and cautions

1. **No UK manufacturer list price for buses or heavy lorries.** ADL, Wrightbus, Volvo, Scania,
   Mercedes-Benz Trucks, DAF and Renault all quote "price on application". Every bus and lorry
   figure comes from a public body, an operator or a dealer, not a price list.
2. **No measured UK electric tractor unit price.** Several operator order announcements were read
   (Maritime 18 units, Wincanton 24, Ashcourt 4, Fred Sherwood 2, DSV 4) and none states the order
   value. The ZEHID 2.7× ratio and the Energy UK 1.8× assumption bracket it; the Dutch dealer's
   €248,800 is an asking price outside the UK.
3. **The 2021 and 2024 price levels are not comparable.** UK bus and lorry prices rose sharply in
   2022-23. A 2021 pair should not be used as a 2025 anchor. Where a row is 2021 it says so.
4. **Most rigid-lorry ratios are council planning figures, not invoices.** Blaenau Gwent,
   Edinburgh, Aberdeen and East Cambridgeshire are all "estimated prices to replace" or
   "estimates only". They are consistent across five authorities and four weight classes, which
   is why the 2.0× ratio is credible, but they are not contracts. The only recent new eRCV award
   found (Salford, £291,000) is 33 per cent below the nearest estimate.
5. **No 32 t rigid and no articulated electric bus.** The UK municipal market is 26 t; no 32 t
   electric rigid price was found. Yutong's 18 m U18 artic is not offered in the UK ("no immediate
   plans to bring it in", Bus & Coach Buyer, Oct 2023), and no UK operator runs one.
6. **Hydrogen lorries.** No UK price. The HyHAUL project was terminated in December 2025 after
   failing to secure fleet agreements.
7. **Coach diesel comparator is weak.** The only pair is a 2023 Yutong GTe14 list price against a
   2024 Yutong GT12 diesel purchase, different models and years. The 1.5× coach multiplier rests
   on that one pair.
8. **Framework maxima are not prices.** The Halton/Link fleet framework is £450m over 48 months
   across ten lots with no vehicle count. Liverpool City Region's bus framework lots are five-year
   call-off ceilings. Neither yields a unit price. TfGM refused unit prices for the Bee Network
   fleet under FOI s43(2).
9. **Lease and TCO-parity offers are not purchase prices.** DAF's November 2025 offer of 100 XD
   Electric tractors at five-year TCO parity, and the various manufacturer lease packages, are
   contract pricing. They are recorded as dead ends, not rows.
10. **VAT ambiguity in ZEBRA cases.** Most state ex-VAT totals for grant calculation but do not
    print "excluding VAT". Where the source says ex-VAT it is recorded; where it does not, the row
    says "not stated" rather than guessing.
11. **Residual values are a real risk and are not in the price.** Aberdeen's 25 hydrogen buses,
    bought for about £13.9m (£556,000 each), were reported in 2026 as being sold to First Bus at
    £30,000 each after about three and a half years. The report is secondary (Longbridge,
    summarising a Press and Journal story) and the figure is not used in any calculation, but it
    is a warning against treating the purchase price as the whole cost.
12. **The 2010-2019 period is almost empty.** Before the ZEBRA awards, UK public bodies did not
    publish per-vehicle electric bus or lorry prices. The only pre-2020 figures found are list
    prices: Yutong TCe12 at £305,000 (2019) and the TfL hydrogen framework at £514,000 (2018/19
    prices). A pakset that introduces electric road vehicles before 2020 will be extrapolating.
13. **Ex-demonstrator and conversion prices are not new-vehicle prices.** Ipswich's £95,000
    (used), Newport's £333,886-£353,480 (repower) and Brighton's £580,000 (specialist side-loader)
    are recorded but excluded from the class averages.

---

## 8. Model specifications used in the rows

| Model | Battery | Stated range | Source |
|---|---|---|---|
| Wrightbus StreetDeck Electroliner | 454 kWh | n/s | Southampton ZEBRA FBC |
| Wrightbus StreetDeck Hydroliner | 48 kWh + 27 kg H2 at 350 bar | n/s | Translink, Hydrogen in Transport, May 2024 |
| ADL Enviro100EV | 354 kWh | 285 miles | routeone, 21 Oct 2024 |
| Yutong TCe12 | 258 kWh (2019); 281 kWh (2023) | over 200 miles | routeone, 3 Jul 2019 and 9 Jan 2024 |
| Yutong GTe14 | 422 or 563 kWh | n/s | Bus & Coach Buyer, 10 Oct 2023 |
| Yutong U11DD | 422.87 kWh (385 kWh option) | n/s | same |
| DAF LF Electric 19 t | 282 kWh (252 kWh usable) | 174 miles | Move Electric, 30 Apr 2022 |
| DAF XF Electric 4x2 | 525 kWh (462 kWh usable) | up to 500 km | DAF UK, 5 Nov 2025 |
| Volvo FH Electric 6x2 | 540 kWh max (six packs) | about 300 km | Volvo UK, 2024 |
| Mercedes-Benz eActros 600 | 621 kWh | 500 km | Daimler Truck UK / Amazon, Nov 2025 |
| Dennis Eagle eCollect | five packs, kWh n/s | n/s | Find a Tender 2022/S 000-024394 |
| Citroen e-Relay | 110 kWh | n/s | Citroen MY26 price guide |
| VW e-Transporter | 65 kWh (Jun 2025); 70 kWh (Nov 2026) | n/s | VW price lists |
| Ford E-Transit 350 | 68 kWh | n/s | Ford 27MY price list |
| Ford E-Transit Custom | 71 kWh | 373 km | Ford UK |
| Mercedes eSprinter 314 | 81 kWh | n/s | mercedes-benz.co.uk |
| Vauxhall Movano Electric | 110 kWh | n/s | Vauxhall PSG |
| Renault Master E-Tech | 87 kWh | 285 miles WLTP | Renault UK |

---

## 9. Sources

**Buses and coaches.** Portsmouth ZEBRA Financial Case (31 May 2022); Leicester ZEBRA Financial
Case (Aug 2021); Nottingham ZEBRA Phase 2 Business Case (Jan 2022); Southampton ZEBRA Full
Business Case (Jan 2022); CPCA ZEBRA Scheme Business Case (20 Aug 2021); YPO DPS 1066 Lot 6 award
(18 Apr 2024); Find a Tender 2025/S 000-002984 (29 Jan 2025); North East CA delegated decisions
(17 Apr 2025 and 8 Apr 2025); Isle of Wight Cabinet report (9 May 2024); Contracts Finder
BOOURN001-DN787890-63130070 (3 Nov 2025); Moray Council FOI 101003260058 (23 Mar 2023); Islington
Fleet Procurement Plan; routeone (3 Jul 2019, 14 Jun 2023, 9 Jan 2024, 22 Aug 2024, 21 Oct 2024);
Bus & Coach Buyer (3 Jul 2019, 10 Oct 2023); Surrey County Council delegated decision (9 Aug
2023); TfL FOI-2253-2021 (26 Feb 2021); TfL Contracts Finder pricing schedule scp 001548;
Liverpool City Region ZEBRA value-for-money proforma; BBC News (29 Jun 2023).

**Lorries and vans.** Thanet District Council OSP report (15 Oct 2024); Blaenau Gwent Fleet
Renewal Appendix 1 (2024/25); City of Edinburgh Fleet Asset Management Plan 2023-2029 (21 Nov
2023); Aberdeen City Council Phase 5 Fleet Replacement Programme 2024/25, Appendix B; East
Cambridgeshire Replacement Refuse Collection Vehicles (Dec 2024); Lewes and Eastbourne Cabinet
report (10 Jul 2025); Salford Procurement Board (19 May 2025); Brighton & Hove City Council news
(20 May 2022); Find a Tender 2021/S 001-024636 and 2022/S 000-024394; Ipswich Borough Council
OD/25/08 (12 Aug 2025); Move Electric (30 Apr 2022); Islington officer key decision I028364
(10 May 2024); Cheltenham Borough Council decision (12 Jun 2023); Bristol Strategy and Resources
Policy Committee (20 Jan 2025); Newcastle City Council award (1 Apr 2023); Blackburn with Darwen
Fleet Replacement 2025/26; Perth & Kinross NEPO HGV Lot 1 award (8 May 2025); Energy UK (30 Sep
2025); WSP, ZEHID Annual Report 2026 (Oct 2026); Citroen UK e-Relay and Relay Prices and
Specifications (MY26, Feb 2026); Vauxhall Price and Specification Guide (1 Oct 2026); Volkswagen
Commercial Vehicles Transporter price list (3 Nov 2026); Ford UK price lists (27MY, 28 Aug 2026;
Transit Custom, accessed Nov 2026); Renault UK press release (2024/25); mercedes-benz.co.uk
Sprinter and eSprinter pages.

**Grant and policy.** GOV.UK, Zero emission vehicles eligible for a grant: Trucks (current);
GOV.UK, Using the zero emission vehicle grant portal; SAU report on the Zero Emission Truck Grant
and Zero Emission Van Grant (24 Mar 2026); SAU report on the Scottish Zero Emission Truck Fund
(29 Sep 2026); DfT, Consultation on a new HGV CO2 emissions regulatory framework (Jan 2026);
Energy Saving Trust fleet decarbonisation toolkit, Tables 19-20 (April 2022 data).
