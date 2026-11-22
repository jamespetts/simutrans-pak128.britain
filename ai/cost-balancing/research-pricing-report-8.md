---
status: draft
verified: none
---
# Research pass 8: a taxonomy of vehicle feature premiums

**Covers**: measured price differences between variants of the same vehicle or class, for every
vehicle class in the pakset, organised as a feature taxonomy rather than a list of keywords.
Aircraft engine number and type, pressurisation, swept wing, wide-body and range; bus deck type,
integral construction, air suspension, transmission, steering, low-floor and air conditioning;
road vehicle fuel, transmission, brakes, overdrive, cab and body type and four-wheel drive;
carriage heating, lighting, air conditioning, corridor, catering, sleeping, brake type, bogies,
panelling and class; tram articulation, bogies, electrical equipment, brakes, multiple-unit and
enclosure; ship propulsion, refrigeration and accommodation class.

Rows are in `ai/temp/research-pricing-rows-8.csv` (72 rows). Parent method:
`New/ai/vehicle-cost-method.md`. Nothing under `New/` was modified. No git command was run.
Nominal money throughout; no deflation or conversion.

---

## 1. Method and the central problem

A feature premium is only measurable when two vehicles differ in one feature. Almost no published
price list is designed for that, so the evidence falls into four grades:

1. **Same-vehicle option price.** One chassis, one catalogue, one option: the Bristol RE list of
   1966 is the best British example, with five priced options on one chassis. This is a strong pair.
2. **Same-model variant.** Two factory versions of one design, differing in one or two stated
   respects: the Convair 880/990, the Avro 748 Series 1/2, the Fleetline single/double-deck chassis.
   Strong, but the second difference has to be stripped out.
3. **Same-class pair.** Two vehicles of similar size and role from different makers: the Electra
   and DC-6B, the Caravelle and Comet 4. Medium, because maker and specification differ.
4. **Cross-section or planning norm.** A regression over many types, or an industry rule of thumb.
   Weak for any single feature, useful as a check on the pairs.

The report gives the pair first and the multiplier second. Where the only evidence is an absolute
adder (a superheater, a set of air brakes, an engine), the report says so, because a percentage
applied to a larger vehicle is a different claim from a fixed sum.

**A warning from the aircraft cross-section.** Fitting log price on log seats, engine count and a
jet dummy across twenty 1959 types gives an engine coefficient of +33 per cent per engine with
R² = 0.91. That is not an engine premium: four-engine aircraft are larger, faster and longer-range.
Adding maximum take-off weight drops the coefficient to +6.7 per cent and changes the other
coefficients. The estimate is unstable because engine count proxies size. This is exactly the trap
`vehicle-cost-method.md` describes, and the reason the tables below rest on pairs, not on the
cross-section.

---

## 2. Aircraft

### 2.1 Engine number

Two pairs bracket the answer.

| Pair | Year | Engines | Seats | MTOW | Price | Difference |
|---|---|---|---|---|---|---|
| Convair 880-22 | 1959 | 2 x CJ-805-3 | 124 | 184,500 lb | £1.29m | — |
| Convair 990 | 1959 | 4 x CJ-805-21 | 139 | 234,200 lb | £1.57m | **+£280,000, +21.7%** |
| Vickers Viscount 700D | 1959 | 4 x Dart RDa.6 | 53 | 64,500 lb | £400,000 | — |
| Fokker F.27 | 1959 | 2 x Dart RDa.6 | 48 | 37,500 lb | £218,000 | **+£182,000, +83.5%** |

Neither is clean. The 990 has two more engines, a 10 ft fuselage plug and 50,000 lb more weight.
The Viscount has two more engines but is 72 per cent heavier and carries five more seats.

The stretch can be priced from two same-family pairs:

- **Super VC10 against standard VC10, 1961**: +13.6 per cent for a 27 ft stretch and 60 more seats,
  same four Conway engines. That is 0.50 per cent per foot.
- **Boeing 720 against 707-120, 1959**: the 720 is 25.6 per cent cheaper with an 8 ft 4 in shorter
  fuselage and the same four engines. That is 3.1 per cent per foot, but the 720 also has 44,000 lb
  less maximum weight, so it is an upper bound.

Applying the VC10 stretch rate to the 990's 10 ft gives +5.0 per cent for the stretch, leaving
+15.9 per cent for two extra engines, or **+7.7 per cent per engine** (an upper bound: the 990 also
has a larger wing and 50,000 lb more weight, and its price is "fully equipped" while the 880's is a
basic price). Applying the seat elasticity from the 1959 cross-section (0.886) to the 990's 15 extra
seats gives +10.7 per cent, leaving +10.0 per cent for two engines, or **+4.9 per cent per engine**.
The Viscount/F.27 pair, adjusted for its five extra seats (+9.2 per cent) and its 72 per cent weight
difference (+58 per cent at the weight elasticity of 0.844), leaves +6.3 per cent for two engines,
or **+3.1 per cent per engine**; that is a lower bound, because maximum weight is itself largely
engines and fuel, so the adjustment over-controls for the feature.

These three routes therefore bracket the answer at 3.1 to 7.7 per cent per engine, and the physical
check agrees: an engine is 15 to 25 per cent of a four-engine airliner, so 4 to 6 per cent each.

**Recommended: ×1.06 per engine, range ×1.04 to ×1.08.** Medium confidence.

### 2.2 Engine type

**Piston to turboprop.** The best pair is the Lockheed Electra and the Douglas DC-6B, both
four-engine, 99 and 107 seats, 116,000 and 107,000 lb:

| Type | Engines | Year | Price | Difference |
|---|---|---|---|---|
| DC-6B | 4 x R-2800 piston | 1958 | £500,000 | — |
| Electra | 4 x Allison 501-D13 turboprop | 1959 | £818,000 | **+£318,000, +63.6%** |

**Recommended: ×1.60, range ×1.45 to ×1.75.** Medium-strong; one pair, but the sizes match well.

**Turboprop to turbojet.** Two pairs, both confounded by size:

| Pair | Seats | Price | Difference | Per seat |
|---|---|---|---|---|
| Caravelle III (2 Avon) against Electra (4 turboprop) | 80 against 99 | £950,000 against £818,000 | +16.1% | **+43.6%** |
| Comet 4 (4 Avon) against Britannia 320 (4 Proteus) | 81 against 149 | £1.14m against £1.07m | +6.5% | **+96%** |

The jet is 16 per cent dearer with 19 per cent fewer seats, or 6.5 per cent dearer with 46 per cent
fewer seats. Per seat the premium is 44 to 96 per cent; the difference is range and speed, not the
engine alone. **Recommended at equal seating: ×1.45, range ×1.25 to ×1.60.** Medium.

**Turbojet to turbofan.** No same-type pair with both prices was found. The 1961 survey prices the
707-120 (JT3C) but not the 707-120B (JT3D); the 1972 index gives used values only. Recorded as
unquantified; a 3 to 5 per cent allowance is the engineering expectation, not a measurement.

**Engine mark change on the same airframe.** Two strong pairs:

- Boeing 707-320 against 707-120, 1959: **+5.4 per cent** for JT4A-3 against JT3C-6, 41 per cent
  more thrust, a larger wing and an 8 ft stretch. The engine element alone is less than 5.4 per cent.
- Avro 748 Series 2 against Series 1, 1961: **+15.5 per cent** for Dart RDa.7 against RDa.6, with
  higher weights. Series E adds another 12.6 per cent for RDa.10s and a 6 ft stretch.

**Recommended: ×1.05 to ×1.15 for a one-mark engine uprate, depending on how much weight grows with
it.** Strong pairs.

### 2.3 Pressurisation

The only pair is the Douglas DC-4 and DC-6, both four-engine, both 1946-47:

| Type | Engines | Pressurised | Price | Difference |
|---|---|---|---|---|
| DC-4 | 4 x R-2000, 1,450 hp | No | £140,000-160,000 | — |
| DC-6 | 4 x R-2800, 2,400 hp | Yes | £210,000-230,000 | **+46.7% at midpoints** |

The DC-6 also has 65 per cent more engine power and 33 per cent more weight. If the engine upgrade
accounts for 20 to 25 points and the weight for 5, pressurisation is worth 15 to 20 per cent.
**Recommended: ×1.15, range ×1.10 to ×1.20.** Weak; one confounded pair plus an arithmetic split.

Every postwar airliner in the pakset is pressurised, so the feature only matters for the 1930s-40s
types (DC-3, DC-4, York, Lancastrian) and for the few unpressurised freighters.

### 2.4 Swept wing

Not separable from the jet premium. Every jet in the 1959 survey is swept and every turboprop is
straight, so the 44 to 96 per cent per-seat jet premium contains the wing, the speed and the
engine type together. No pair with the same engines and different sweep was found. **No separate
multiplier**; include it in the turboprop-to-jet factor.

### 2.5 Wide-body

The 1972 price index gives new equipped prices for four wide-bodies and the 707-320B. Dividing by
typical two-class seating:

| Type | Price | Seats (assumed) | Price per seat |
|---|---|---|---|
| Boeing 707-320B | $10.0m | 180 | $55,600 |
| Airbus A300B | $17.5m | 250 | $70,000 (+25.9%) |
| Boeing 747 | $24.0m | 366 | $65,600 (+18.0%) |
| McDonnell Douglas DC-10 | $20.0m | 270 | $74,100 (+33.3%) |
| Lockheed TriStar | $20.0m | 250 | $80,000 (+44.0%) |

Median +29.5 per cent per seat. The seat counts are not printed in the table and are typical
configurations, so the row is medium rather than strong. **Recommended: ×1.30 per seat, range ×1.18
to ×1.44.** This is a per-seat factor: a wide-body carries more people, so its total price is much
higher while its price per seat is only 18 to 44 per cent higher.

### 2.6 Range

The 707-320 against 707-120 is the cleanest range pair: **+5.4 per cent for about 40 per cent more
range** (3,500 against 2,500 nautical miles), with the same engine count. The DC-7C against DC-7B,
1958, is +13.2 per cent for a smaller range increase but more payload. Range is cheap in capital
terms because it is mostly fuel tankage and a slightly heavier structure.

**Recommended: ×1.00 to ×1.02 for a long-range version of the same aircraft; do not apply a large
range multiplier.** Weak-medium.

### 2.7 Equipment fit

Hawker Siddeley 125, 1961: basic price £140,000; "radar and radio would add about £25,000" =
**+17.9 per cent**. On a small executive aircraft avionics are a large share; on a 150-seat airliner
they are a few per cent. Recorded as an absolute adder of about £25,000 in 1961, not as a constant
percentage. Strong single pair.

---

## 3. Buses and coaches

### 3.1 Deck type

The cleanest pair is the Daimler Fleetline chassis in 1968, same maker, same year, same Gardner
engine family:

| Chassis | Length | Price | Difference |
|---|---|---|---|
| Fleetline single-deck (South Shields, 6) | 36 ft | £3,714 each | — |
| Fleetline double-deck (Manchester, 44) | 33 ft | £4,175 each | **+£461, +12.4%** |

The single-decker is 3 ft longer, so the deck premium is at least 12.4 per cent on the chassis. The
body is a separate matter: a double-deck body has a second deck, stairs and roughly twice the
panelling. No same-year single/double body pair was found, so the body element is inferred at 10 to
15 per cent, giving a complete-vehicle premium of about **×1.12 to ×1.15**. Medium for the chassis,
weak for the body.

A second, older pair points the same way: Cardiff's Guy Arab V 30 ft chassis cost £97 (3.6 per cent)
more than the 27 ft, and the body £120 (3.8 per cent) more. Length, not deck, is being priced there.

### 3.2 Body on chassis against integral construction

British buses were chassis-and-body until the 1970s. The body share of the complete vehicle is well
measured:

| Year | Vehicle | Chassis | Body | Body share |
|---|---|---|---|---|
| 1955 | Glasgow BUT 9613T trolleybus | £3,195 | £2,821 | 46.9% |
| 1964 | Coventry Fleetline | £3,240 | £3,560 | 52.3% |
| 1965 | Cardiff Guy Arab V | £2,792 | £3,265 | 53.9% |

So the body is 47 to 54 per cent of a complete bus, and a coach body is at the top of that range.
Integral construction does not remove the engine, axles or suspension; it removes the separate
chassis frame and some assembly. No measured integral/chassis pair was found (the Leyland National
price of £20,000 in 1972 is a special business-commuter version and cannot be paired with a 1966
chassis). **Recommended: integral ×0.95 against chassis-and-body, range ×0.92 to ×0.98.** Weak,
inferred from the body share and the nature of the change.

### 3.3 Air suspension, transmission, steering and heating

The Bristol RELL list of 4 November 1966 is the single best bus document found, because five
options are priced against one list price of £3,335:

| Option | Price | Percentage |
|---|---|---|
| Gardner 6LX engine (against Leyland 0.600) | £385 | +11.5% |
| Fluid clutch and five-speed semi-automatic transmission | £364 | **+10.9%** |
| Firestone Airide air suspension (against leaf springs) | £206 | **+6.2%** |
| Exhaust water heater and Varivane shutter (saloon heating) | £135 15s | **+4.1%** |
| Clayton Dewandre automatic lubrication | £87 | +2.6% |
| **Total as tested** | **£4,512 15s** | +35.3% |

Independent cases agree on the transmission range: Brighton 1965, semi-automatic £260 on a complete
£6,300 bus = +4.1 per cent; Seddon 1972, Allison automatic £480 (no base price). The percentage is
lower on a complete vehicle because the base includes the body.

Power steering was a £60 option on a £3,620 Bedford SB coach in 1957 = **+1.7 per cent**, and was
standard on PSV chassis by the early 1960s (the 1962 Bedford VAL lists it as standard and says the
cost is not a particular detriment). **Recommended: ×1.02, 1950s only.**

**Recommended: air suspension ×1.06 (strong); semi-automatic ×1.08 (range ×1.04 to ×1.11, strong);
saloon heating ×1.04 (strong); power steering ×1.02 (medium, 1950s).**

### 3.4 Low-floor and accessible buses

Two kinds of evidence, neither a matched pair:

- **Manufacturer statement, 1995.** Scania/Wrights launched the Axcess-ultralow with the aim of a
  low-floor bus "no more than 5 per cent more expensive than a conventional single decker", and the
  article says the project achieved it: £100,000 for a 12 m 47-seat bus, at least £10,000 cheaper
  than rivals. That is **≤5 per cent**, and it is a design target that was met, not a measured pair.
- **Planning norm.** The ITDP BRT guide puts the low-floor addition at 4.5 per cent for a 40-seat
  mini, 4.25 per cent for a 53-seat midi, 4 per cent for a 75-seat conventional and 2 per cent for a
  120-seat articulated bus.
- **TRL 1998.** Capital costs are higher for low-floor buses, and "the current price differential
  ... has fallen substantially since these trials began"; the overall operating cost difference is
  1 to 4 per cent.

**Recommended: ×1.03, range ×1.02 to ×1.05.** Medium. By the 2000s the low-floor design was
universal, so the premium is a 1990s transition feature, not a permanent one.

### 3.5 Bus and coach air conditioning

No British measured pair was found. The ITDP table gives 11.5 to 12.5 per cent of total vehicle
price across sizes. That is a planning norm for hot climates; a British coach installation is
smaller and often engine-driven. **Recommended: ×1.08, range ×1.05 to ×1.12.** Weak-medium.
Recorded as a real gap, not as a measurement.

### 3.6 Trolleybus against motorbus

Commercial Motor, 19 September 1952: a two-axle 56-seat 8 ft double-deck motorbus cost about
£4,200 and an equivalent trolleybus £4,800 = **+£600, +14.3 per cent**, excluding the overhead line
(about £10,000 a mile). Strong single pair. The trolleybus chassis already includes the electrical
equipment, which is why its body share (46.9 per cent) is lower than a diesel bus's.

---

## 4. Road vehicles

### 4.1 Fuel

The diesel premium is already established at **×1.17** from 33 same-model pairs in the 1960
Commercial Motor list, banded by size: ×1.22 under 2 tons, ×1.17 at 2-4 tons, ×1.14 at 5-7 tons.
The structure is an absolute adder of about £125 in 1960, not a constant percentage. No new work
was needed; the pass confirms it and uses it as the anchor for the other vehicle features.

### 4.2 Transmission

| Case | Year | Price | Premium |
|---|---|---|---|
| Bristol RELL semi-automatic | 1966 | £364 on £3,335 | **+10.9%** |
| Brighton double-decker semi-automatic | 1965 | £260 on £6,300 | +4.1% |
| Seddon Pennine-6 Allison automatic | 1972 | £480 extra | no base |
| ERF 68GX automatic, net of standard gearbox | 1965 | £850 - £338 = £512 | **+17% inferred on a £3,000 chassis** |

**Recommended: semi-automatic ×1.08 (range ×1.04 to ×1.11); heavy-duty full automatic ×1.15
(range ×1.10 to ×1.20).** Strong for the light/medium case, medium for the heavy.

### 4.3 Two-speed axle and overdrive

- Bedford SB, 1957: two-speed axle £185 on £3,620 = **+5.1 per cent**.
- Bedford SL1, 1960: two-speed axle £95 on £1,143 = **+8.3 per cent**.
- Ford R Series, 1970: overdrive gearbox "as an option at no extra cost" = **0 per cent**. A
  negative result: by 1970 overdrive was not a priced feature on that chassis.

**Recommended: two-speed axle ×1.06 (range ×1.05 to ×1.08); overdrive ×1.00 from about 1965.**

### 4.4 Cab type

Six same-model pairs from the 1960 price list, all petrol, all chassis and cab:

| Make and tonnage | Normal control | Forward control | Premium |
|---|---|---|---|
| Austin 3-ton | £707 | £735 | +4.0% |
| Austin 4-ton | £773 | £795 | +2.8% |
| Austin 5-ton | £819 | £854 11s | +4.3% |
| Bedford 4-ton | £765 | £810 | +5.9% |
| Bedford 5-ton | £840 | £853 | +1.5% |
| Bedford 6-ton | £875 | £902 | +3.1% |
| Bedford 7-ton | £1,080 | £1,002 | **-7.2%** (anomaly) |

Median of the six positive pairs: **+4.0 per cent**. The 7-ton anomaly is probably a different
specification and is excluded. **Recommended: forward control ×1.04, range ×1.02 to ×1.06.** Strong.

### 4.5 Body type

- Ford Thames Trader 5-ton, 1960: platform chassis £845, tipper chassis £885 = **+4.7 per cent**
  (petrol); £960 against £1,020 = **+6.3 per cent** (oil).
- Thames Trader 7-ton: tipper £15 cheaper than platform (-1.5 per cent), an anomaly.
- No paired tanker price was found. A tanker body is a specialist fabrication worth more than a
  platform; the body-share evidence for buses (47-54 per cent) suggests the body can exceed the
  chassis price, so the tanker premium is likely 30 to 60 per cent of the chassis, unmeasured.

**Recommended: tipper ×1.05 (range ×1.04 to ×1.06); tanker not quantified.**

### 4.6 Four-wheel drive

Bedford forward-control 4x4, 1960: £1,260 petrol against £810 for the 4-ton 4x2 forward-control =
**+55.6 per cent**. The 4x4 is a different model and probably a different gross weight, so this is
an upper bound. A Land-Rover comparison is not a lorry comparison. **Recommended: ×1.35, range
×1.25 to ×1.55.** Weak.

### 4.7 Servo brakes, synchromesh and other standard equipment

No priced option survives into the 1950s-60s lists because both had become standard: the 1960
Bedford and Austin chassis all have hydraulic servo brakes, and the Ford R Series of 1970 has a
five-speed synchromesh box as standard. Earlier option prices were not found. **No multiplier**;
treat them as specification thresholds (pre-1930 vs post-1935), not as priced features.

---

## 5. Railway carriages

### 5.1 Corridor against open

The NER build records give same-year, same-length, same-wheel pairs:

| Pair | Layout | Price | Difference |
|---|---|---|---|
| 1906 dia. 251/1 | 5 third compartments, all corridor | £1,459 10s | — |
| 1906 dia. 308 | 3 corridor + 2 open | £1,389 8s 4d | **+5.0% for the corridor car** |
| 1910 dia. 970 | 2 corridor + composite + 3 corridor | £1,621 0s 5d | — |
| 1911 dia. 1047 | 6 corridor + composite | £1,600 16s 6d | **-1.3% for the corridor car** |

The second pair reverses the first, so the corridor premium is small and not robust. The likely
reason is that a corridor costs side space and joinery but saves compartment partitions. **Recommended:
×1.02, range ×1.00 to ×1.05.** Medium. Gangwayed stock is the same feature plus end vestibules; no
separate price.

### 5.2 Catering

The best pair in the whole carriage set, same year, same length, same wheel arrangement:

| 1909 NER 8-wheel | Layout | Price |
|---|---|---|
| Dia. 1266 dining car | pantry / kitchen / pantry, 52 ft 6 in | £2,304 4s 5d |
| Dia. 824 composite | lavatory, 52 ft 6 in | £1,594 14s 1d |

**+£709 10s 4d = +44.5 per cent.** This is a full kitchen and dining saloon against a composite.
A buffet or pantry car without a kitchen is a smaller step; no paired buffet price was found, so
**buffet ×1.15 is inferred, not measured**. **Recommended: kitchen/dining ×1.45 (range ×1.35 to
×1.55), strong; buffet ×1.15, weak.**

### 5.3 Heating and lighting

**Lighting.** Hansard, 11 March 1930: the LMS estimated £287,500 to convert 1,250 coaches from gas
to electric lighting = **£230 per coach**, with a Development Act grant. The GWR put £80,000 and the
LNER £56,000 into the same programme without stating the number of coaches. On a 1930 coach of about
£2,000, £230 is 11.5 per cent, but it is a conversion including removal of gas fittings, so a
new-build electric lighting premium is lower, perhaps 5 to 8 per cent.

**Recommended: electric lighting against gas ×1.06, range ×1.05 to ×1.12.** Medium for the absolute
figure, weak for the percentage. Gas lighting itself is the baseline; no separate gas-lighting price.

**Heating.** No priced pair was found. Steam heating is a pipe, radiator and control system fed from
the locomotive; the hardware is much cheaper than electric lighting. The 1957 Institution of
Locomotive Engineers paper by Pepper discusses initial cost as a criterion but prints no figures,
and the Pullman 1957 tender enquiry asked builders to price air conditioning, lighting, heating and
interior separately, but the returned prices are not in the published article. **Recommended:
steam heating ×1.02, range ×1.01 to ×1.03; electric heating ×1.03, range ×1.02 to ×1.05.** Weak;
an engineering estimate, not a measurement.

### 5.4 Air conditioning

No British measured pair. The Pullman enquiry specified Stone-Carriers 5-ton self-contained
equipment with an individual internal-combustion power plant per car, which is a large installation;
the returned price is not published. Modern railway air conditioning is 8 to 12 per cent of car
cost by the same order of magnitude as the bus figure. **Recommended: ×1.10, range ×1.08 to ×1.12.**
Weak; recorded as a gap.

### 5.5 Sleeping cars

Jenkinson gives average sleeping car costs of about £3,000 before the First World War and £4,000
after it, against ordinary carriages of £1,200-1,500 for a pre-grouping bogie third and £2,300-2,500
for a 1920s corridor third. Sleeping cars are therefore **×2.0 to ×2.5 an ordinary third**, but the
comparison mixes lengths, classes and dates. **Recommended: ×2.2, range ×1.8 to ×2.5.** Weak.

### 5.6 Brake type

No paired price for vacuum, air or dual-braked carriages was found. The railway evidence prices
brake equipment at the wagon or component level, not as a carriage option. **No multiplier**;
treat vacuum as the baseline and dual braking as a small adder of 1 to 3 per cent, unmeasured.

### 5.7 Bogies and wheels

- Midland, 1870s: six-wheel against four-wheel bogie carriage, **£979 against £820 = +19.4 per cent**.
  Same body and order.
- Highland, 1908: a complete set of new bogies **£33 per carriage**, on a carriage costing about
  £1,000-1,500, so 2 to 3 per cent as a replacement component (not a new-build premium).

**Recommended: bogie against four-wheel ×1.20, range ×1.15 to ×1.25.** Strong pair, but the
comparison is six-wheel against four-wheel bogie rather than four-wheel rigid against bogie.

### 5.8 Panelling, class and roof

| Feature | Pair | Result | Confidence |
|---|---|---|---|
| Steel against wood panelling | GWR Toplight, c.1903-10: £1,500 against £1,200 | **+25.0%** | Strong |
| First against third, same body and weight | Highland 1873: £517 5s against £290 | **+78.4%** | Strong |
| Clerestory against arc roof | Midland 1880: £25 on about £1,000 | **+2.6%** | Strong, small |
| Elliptical against clerestory | Midland 1915: £35-40 cheaper, 12 cwt lighter | **-3.5 to -4.0%** | Strong, negative |

The class premium is finish, not structure. The roof result is a warning: the later, lighter roof
was cheaper, so a ladder should mark the clerestory up rather than the arc roof down.

---

## 6. Trams

### 6.1 Air brakes

Two independent cases:

- **Wallasey, 1901.** British Westinghouse tendered £11,940 for 20 cars without air brakes (£597
  each) plus £1,000 for air brakes = **£50 each, +8.4 per cent**. ER&TCW's £590 was without brakes;
  Blackwell's £696 5s was with them.
- **Melbourne, 1923.** Air brake equipment £154 on a complete car of £2,674 = 5.8 per cent of the
  car, or **+6.1 per cent** as an add-on (154/(2674-154)).

**Recommended: ×1.07, range ×1.06 to ×1.08.** Strong.

### 6.2 Body and electrical equipment

| Source | Body | Electrical | Bogies | Other | Total |
|---|---|---|---|---|---|
| Melbourne W, 1923 | £1,383 (51.7%) | £880 (32.9%) | £150 (5.6%) | £261 (9.8%) | £2,674 |
| Blackpool Coronation, 1950 | £4,902 (37.2%) | £2,503 (19.0%) | £5,765 (43.8%) | — | £13,170 |

The electrical share ranges from 19 to 33 per cent, and the earlier Hawthorn case puts equipment at
44.6 per cent of body plus equipment. The bogie share ranges from 5.6 to 43.8 per cent because
Blackpool's sprung bogies were a special design. **Recommended: electrical equipment ×1.30 over a
body-only price (range ×1.20 to ×1.50); bogies ×1.06 over a four-wheel truck (range ×1.03 to ×1.10),
weak.**

The practical use for the pakset is to decide what the tram `cost` includes. If the object price is
a complete car, the equipment is already inside it and the feature multiplier should not be stacked
again. The share table is for decomposing a complete-car price, not for adding to it.

### 6.3 Articulation, multiple-unit and enclosure

- **Articulation.** No paired articulated/single price was found. An articulated car has two bodies
  and three trucks instead of one body and two trucks, so the structure is roughly 1.6 to 1.8 times
  a single car while capacity is about 1.5 times. **Recommended: ×1.30 for a two-section articulated
  car against a single car of the same seating, range ×1.20 to ×1.40.** Weak, inferred.
- **Multiple-unit equipment.** No separate price. It is part of the electrical equipment share
  above; a multiple-unit car needs train-line and control gear, perhaps 5 to 10 per cent more
  electrical equipment. **No multiplier.**
- **Enclosure.** Sydney, 1906: adding an open upper deck to an existing car estimated at £140, glazed
  in at £180, plus £35 to lengthen platforms. Glazing the deck is **+£40, +28.6 per cent on the deck**,
  about +6.7 per cent on a car of roughly £600. **Recommended: glazed/enclosed against open
  ×1.07, range ×1.05 to ×1.10.** Weak-medium; a conversion estimate, not a contract price.

### 6.4 Bogie against four-wheel

Wallasey, 1902: five bogie single-deck combination cars at £585 each against £590 paid for
four-wheel double-deckers of the same fleet = **-0.8 per cent**. Deck type and bogie mounting did
not separate the prices because capacity did. The Melbourne bogie component is 5.6 per cent of the
car. **Recommended: ×1.05, range ×1.03 to ×1.08.** Weak, with a negative result recorded.

### 6.5 Builder spread

Wallasey, 1901, one specification, four tenders: £590, £597, £660 and £696 5s per car. The spread
is **17.9 per cent**. This is not a feature premium, but it is the uncertainty band within which any
single tram pair sits, and it should be quoted whenever a tram multiplier is used.

---

## 7. Ships

### 7.1 Steam against diesel, and turbine against reciprocating

The marine engineering literature prices the machinery, not the ship. Two independent tables:

**Cleghorn, 1926, cost of plant (£000):**

| SHP | Recip. coal | Recip. oil | Turbine coal | Turbine oil | Diesel |
|---|---|---|---|---|---|
| 2,500 single screw | 38 | 39 | 45 | 46 | **68** |
| 6,000 twin screw | 85 | 86 | 95 | 96 | **120** |

- Diesel against reciprocating coal: **+78.9 per cent at 2,500 SHP, +41.2 per cent at 6,000 SHP**.
- Turbine against reciprocating coal: **+18.4 per cent at 2,500 SHP, +11.8 per cent at 6,000 SHP**.

**Seaton, 1928, machinery cost per ship:**

| Machinery | Cost | Against triple expansion |
|---|---|---|
| Triple expansion | £11,800 | — |
| Single-reduction geared turbines | £17,500 | +48.3% |
| R-W double-acting diesel, steam auxiliaries | £20,200 | +71.2% |
| R-W double-acting diesel, electric auxiliaries | £22,400 | +89.8% |
| Doxford diesel, steam auxiliaries | £24,800 | **+110.2%** |
| Doxford diesel, electric auxiliaries | £27,200 | +130.5% |

The diesel premium falls as the machinery grows and depends heavily on the engine maker. For a
complete ship, the premium is the machinery difference times the machinery share:

- Fairplay 7,500 dwt cargo steamer at about £9 a ton in 1926 = £67,500.
- Seaton's diesel premium of £13,000 is **19.3 per cent of that**; the turbine premium of £5,700 is
  8.4 per cent.
- The *Duchess of Bedford* case, 1929: a motor ship of similar capacity would have cost £100,000
  more, about 7 per cent on a large liner.

**Recommended: diesel against steam ×1.15, range ×1.10 to ×1.25; turbine against reciprocating
×1.05, range ×1.04 to ×1.08.** Medium. The low end applies to large, high-power ships; the high end
to small cargo ships.

### 7.2 Refrigeration and passenger class

No measured price was found for either. Refrigerated cargo spaces need insulation, a compressor
plant and air circulation; the plant is a substantial item but no yard price was located. Passenger
accommodation class is a fit-out cost, not a propulsion feature, and the ship contract prices in the
evidence base do not separate it. **No multipliers**; both are recorded gaps.

---

## 8. Recommended multiplier table

Factors are on the price of the same vehicle without the feature. Where the evidence is an absolute
adder, the table says so; the absolute form is more faithful but needs the 1900 conversion settled
first. Do not stack factors from different eras without checking that both features existed on the
same vehicle.

### Aircraft

| Feature | Factor | Range | Applies | Evidence | Confidence |
|---|---|---|---|---|---|
| Each additional engine | **×1.06** | 1.04-1.08 | 1945-1980 | CV-880/990; Viscount/F.27; VC10 stretch | Medium |
| Piston to turboprop | **×1.60** | 1.45-1.75 | 1950-1970 | Electra against DC-6B, 1958-59 | Medium-strong |
| Turboprop to turbojet, equal seats | **×1.45** | 1.25-1.60 | 1955-1975 | Caravelle/Electra; Comet/Britannia | Medium |
| Turbojet to turbofan | ×1.04 | 1.03-1.05 | 1960-1985 | No pair; engineering estimate | Weak |
| Pressurisation | **×1.15** | 1.10-1.20 | 1940-1960 | DC-4/DC-6, confounded | Weak |
| Swept wing | included in jet factor | — | 1950-1970 | Not separable | Unquantified |
| Wide-body, per seat | **×1.30** | 1.18-1.44 | 1970-2000 | 1972 price index, four types | Medium |
| Long-range version, same type | ×1.02 | 1.00-1.02 | 1955-1980 | 707-320/120 | Weak |
| Full radio and radar fit | +£25,000 (1961) | — | 1950-1970 | HS.125, 1961 | Strong single pair |
| Engine mark uprate | ×1.05-1.15 | — | 1955-1975 | 707-320/120; 748 S2/S1 | Strong pairs |

### Buses and coaches

| Feature | Factor | Range | Applies | Evidence | Confidence |
|---|---|---|---|---|---|
| Double deck against single deck | **×1.13** | 1.12-1.15 | 1930-1980 | Fleetline chassis 1968; body inferred | Medium |
| Integral against chassis-and-body | ×0.95 | 0.92-0.98 | 1970-2000 | Body share 47-54%; no pair | Weak |
| Air suspension | **×1.06** | 1.05-1.07 | 1960-1990 | Bristol RELL, £206 on £3,335 | Strong |
| Semi-automatic transmission | **×1.08** | 1.04-1.11 | 1955-1985 | Bristol 1966; Brighton 1965 | Strong |
| Full automatic, heavy chassis | ×1.15 | 1.10-1.20 | 1965-2000 | ERF 1965, net £512 | Medium |
| Power steering | ×1.02 | 1.01-1.03 | 1950-1965 | Bedford SB 1957, £60 | Medium |
| Saloon heating | **×1.04** | 1.03-1.05 | 1950-1980 | Bristol RELL exhaust heater | Strong |
| Air conditioning | ×1.08 | 1.05-1.12 | 1980-2026 | ITDP planning norm | Weak-medium |
| Low floor / accessible | ×1.03 | 1.02-1.05 | 1990-2010 | Scania 1995; ITDP; TRL | Medium |
| Trolleybus against motorbus | **×1.14** | 1.13-1.15 | 1930-1960 | 1952 pair, £4,200/£4,800 | Strong single pair |

### Road vehicles

| Feature | Factor | Range | Applies | Evidence | Confidence |
|---|---|---|---|---|---|
| Diesel against petrol, light | **×1.22** | — | 1930-1970 | 33 pairs, 1960 | Strong |
| Diesel against petrol, medium | **×1.17** | — | 1930-1970 | 33 pairs, 1960 | Strong |
| Diesel against petrol, heavy | **×1.14** | — | 1930-1970 | 33 pairs, 1960 | Strong |
| Semi-automatic transmission | **×1.11** | 1.09-1.13 | 1960-1980 | Bristol RELL 1966 | Strong |
| Full automatic, heavy | ×1.17 | 1.12-1.20 | 1965-2000 | ERF 1965, inferred | Medium |
| Two-speed axle | ×1.06 | 1.05-1.08 | 1950-1970 | Bedford 1957 and 1960 | Strong |
| Overdrive | ×1.00 | — | 1965-1980 | Ford R Series 1970, no charge | Strong, negative |
| Forward-control cab | **×1.04** | 1.02-1.06 | 1950-1970 | Six 1960 pairs | Strong |
| Tipper body | ×1.05 | 1.04-1.06 | 1950-1970 | Thames Trader 1960 | Medium |
| Tanker body | not quantified | — | — | No pair | Unknown |
| Four-wheel drive | ×1.35 | 1.25-1.55 | 1950-1980 | Bedford 4x4 1960, upper bound | Weak |
| Servo brakes, synchromesh | ×1.00 | — | 1935 onwards | Standard by 1960 | Threshold, not price |

### Railway carriages

| Feature | Factor | Range | Applies | Evidence | Confidence |
|---|---|---|---|---|---|
| Steam heating | ×1.02 | 1.01-1.03 | 1880-1960 | No pair; engineering estimate | Weak |
| Electric heating | ×1.03 | 1.02-1.05 | 1930-1990 | No pair | Weak |
| Electric against gas lighting | **×1.06** | 1.05-1.12 | 1900-1935 | LMS 1930, £230 per coach | Medium |
| Air conditioning | ×1.10 | 1.08-1.12 | 1935-2026 | No pair; Pullman enquiry | Weak |
| Corridor against open | **×1.02** | 1.00-1.05 | 1890-1935 | NER 1906 +5.0%, 1910/11 -1.3% | Medium |
| Gangwayed | included in corridor | — | 1890-1935 | Same feature | Medium |
| Kitchen/dining car | **×1.45** | 1.35-1.55 | 1880-1960 | NER 1909, +44.5% | Strong |
| Buffet car | ×1.15 | 1.10-1.20 | 1900-1960 | Inferred from kitchen | Weak |
| Sleeping car | ×2.2 | 1.8-2.5 | 1870-1970 | Jenkinson averages | Weak |
| Dual brake | ×1.02 | 1.01-1.03 | 1900-1960 | No pair | Unknown |
| Bogie against four/six-wheel | **×1.20** | 1.15-1.25 | 1870-1920 | Midland, £979/£820 | Strong |
| Steel against wood panelling | **×1.25** | 1.20-1.30 | 1900-1930 | GWR Toplight | Strong |
| First against third class | **×1.78** | 1.70-1.85 | 1870-1930 | Highland 1873 | Strong |
| Clerestory against arc roof | ×1.026 | 1.02-1.03 | 1870-1900 | Midland 1880 | Strong, small |
| Elliptical against clerestory | ×0.96 | 0.96-0.965 | 1905-1935 | Midland 1915 | Strong, negative |

### Trams

| Feature | Factor | Range | Applies | Evidence | Confidence |
|---|---|---|---|---|---|
| Articulated against single | ×1.30 | 1.20-1.40 | 1920-1955 | No pair; structure and capacity | Weak |
| Bogie against four-wheel | ×1.05 | 1.03-1.08 | 1900-1950 | Wallasey 1902 -0.8%; Melbourne 5.6% | Weak |
| Electrical equipment over body | **×1.30** | 1.20-1.50 | 1900-1950 | Melbourne 32.9%; Blackpool 19.0% | Medium |
| Air brakes | **×1.07** | 1.06-1.08 | 1900-1930 | Wallasey 1901; Melbourne 1923 | Strong |
| Multiple-unit equipment | included in electrical | — | 1900-1950 | No separate price | Unknown |
| Enclosed against open | ×1.07 | 1.05-1.10 | 1900-1930 | Sydney 1906 glazing estimate | Weak-medium |
| Builder spread (uncertainty) | ±18% | — | 1900-1930 | Wallasey 1901, four tenders | Strong |

### Ships

| Feature | Factor | Range | Applies | Evidence | Confidence |
|---|---|---|---|---|---|
| Diesel against steam, complete ship | **×1.15** | 1.10-1.25 | 1920-1960 | Cleghorn 1926; Seaton 1928 | Medium |
| Turbine against reciprocating, complete ship | ×1.05 | 1.04-1.08 | 1905-1950 | Cleghorn 1926; Seaton 1928 | Medium |
| Refrigeration | not quantified | — | — | No price | Unknown |
| Passenger class | not quantified | — | — | No separated price | Unknown |

---

## 9. The strongest pairs

Ranked by how narrowly the two vehicles differ and how completely the source states the price.

1. **Bristol RELL, 1966.** Five options on one chassis with one list price: air suspension £206,
   semi-automatic £364, Gardner engine £385, saloon heater £135 15s, auto lubrication £87. The best
   single document in this pass, and the model for what a bus price list can yield.
2. **Daimler Fleetline, 1968.** 36 ft single-deck chassis £3,714 against 33 ft double-deck £4,175,
   same maker, year and engine family.
3. **Lockheed Electra against Douglas DC-6B, 1958-59.** Four turboprops against four pistons, 99
   against 107 seats: +63.6 per cent.
4. **NER 1909 dining car against composite.** Same length, same wheels, same year: +44.5 per cent.
5. **NER 1906 brake thirds.** Same length, same year, same wheels, corridor against mixed open:
   +5.0 per cent, with the 1910/11 pair reversing it to -1.3 per cent, which is why the corridor
   factor is small.
6. **Convair 880-22 against 990, 1959.** The only same-family engine-number pair with both prices:
   +21.7 per cent for two engines and a stretch.
7. **Standard against Super VC10, 1961.** Same engines and wing, 27 ft stretch: +13.6 per cent.
   This is what makes the Convair pair usable.
8. **Wallasey air brakes, 1901.** £50 on £597: +8.4 per cent, with the same tenderer quoting both.
9. **1960 Commercial Motor cab pairs.** Six same-model normal/forward-control pairs; median +4.0
   per cent.
10. **Avro 748 Series 2 against Series 1, 1961.** Same airframe, Dart mark change: +15.5 per cent.
11. **Midland six-wheel against four-wheel bogie.** Same body: +19.4 per cent.
12. **Highland 1873 first against third.** Same dimensions and weight: +78.4 per cent.

**Ranges, not pairs**: the diesel premium before 1960; the trolleybus figure; the wide-body per-seat
figures (seat counts assumed); the ship machinery tables (machinery, not complete ships); every
low-floor and air-conditioning figure.

**Weak or inferred**: pressurisation, turbojet-to-turbofan, integral bus construction, articulated
trams, tram enclosure, carriage heating and air conditioning, ship refrigeration and passenger class.

---

## 10. What could not be quantified

Recorded so that the next pass does not repeat the search.

1. **Aircraft pressurisation, cleanly.** Every postwar type is pressurised, so the only pair is the
   DC-4/DC-6, which also changes engines and weight.
2. **Swept wing on its own.** No same-engine swept/straight pair exists in the price surveys.
3. **Turbojet to turbofan.** The 1961 survey prices the 707-120 but not the 707-120B; the 1972 index
   gives used values only.
4. **Bus double-deck body against single-deck body.** No same-year body builder price list with both.
   The chassis pair is measured; the body element is inferred.
5. **Integral bus against chassis-and-body.** The Leyland National price is a special version and
   the Metro-Scania is a different market; no clean pair.
6. **Coach air conditioning in Britain.** Only the ITDP planning norm, which is a hot-climate
   figure.
7. **Lorry tanker body.** No paired tanker/platform price. The body-share evidence shows the body
   can exceed the chassis, but the tanker itself is unmeasured.
8. **Servo brakes and synchromesh as priced options.** Both were standard before the period in which
   full price lists survive.
9. **Carriage steam heating, electric heating and air conditioning.** The 1957 Pullman enquiry asked
   for separate prices for exactly these items, and the returned tender prices are not in the
   published article. The Pepper 1957 paper discusses initial cost but prints no figures.
10. **Carriage brake type.** No vacuum/air/dual paired price at carriage level.
11. **Tram articulation and multiple-unit equipment.** No paired articulated/single price; MU gear
    is inside the electrical equipment share.
12. **Ship refrigeration and passenger class.** No yard price separates either.
13. **The 1962-1971 aircraft block.** The Flight surveys stop at 1961 and the price index starts in
    1972; only individual contract prices bridge it.
14. **A second year of the 1972 airliner price index.** If it ran annually, the 1973-1985 pages
    would close the wide-body and turbofan gaps. The Wayback capture has to be found by exact
    viewer URL.

---

## 11. Search record

One search per turn, as required. Queries and what they returned:

| Turn | Query subject | Result |
|---|---|---|
| 1 | Bus chassis prices, single against double deck, 1960s | Fleetline 1968 single £3,714 and double £4,175; Cardiff, Coventry, Reading prices |
| 2 | Bus option prices: air suspension, steering, automatic, integral | Bristol RELL 1966 full option lattice; Bedford VAL power steering standard; Ford R1600 prices |
| 3 | Lorry four-wheel drive, tipper and cab type, 1955-1970 | 1960 "What Will It Cost?" full list; cab and tipper pairs; ERF automatic 1965; Ford overdrive 1970 |
| 4 | Railway carriage electric lighting and steam heating cost | Hansard 1930 LMS £230 per coach; NBR carriage records; no heating price |
| 5 | Railway carriage steam heating apparatus price | Dead end: no priced heating equipment; HRA guidance only |
| 6 | Pepper 1957 carriage heating paper | Abstract and SteamIndex summary; no cost figures |
| 7 | Articulated tram against four-wheel, 1925-1950 | Blackpool 1934 open £2,688; Aberdeen £5,000-11,000; no articulation pair |
| 8 | Motor ship against steamship cost, 1920-1938 | Cleghorn 1926 and Seaton 1928 machinery tables; *Duchess of Bedford* £100,000 |
| 9 | Low-floor bus and coach air conditioning premium | Scania 1995 ≤5%; ITDP 2-4.5% low floor and 11.5-12.5% air conditioning; TRL 271 |
| 10 | BR Mk II / LNER air-conditioned carriage cost | Pullman 1957 enquiry with separate air-conditioning item; no returned prices |

Pages fetched and read in full: Commercial Motor 10 May 1968, 20 Dec 1968, 4 Nov 1966, 6 May 1960;
Flight 1959 and 1961 survey text (downloaded from Internet Archive and searched locally). The
Pullman PDF was downloaded but its text layer is partly glyph-encoded and the body pages did not
yield usable text; the tender breakdown could not be read.

---

## 12. Sources

1. *Flight International*, "Commercial Aircraft of the World", 20 November 1959, pp.576-620.
   Internet Archive `sim_flight-international_1959-11-20_76_2645`.
2. *Flight International*, "Commercial Aircraft of the World", 23 November 1961, pp.795-850.
   Internet Archive `sim_flight-international_1961-11-23_80`.
3. *Flight International*, "Airliner price index", 10 August 1972, p.183. Wayback copy of
   `http://www.flightglobal.com/FlightPDFArchive/1972/1972 - 2020.PDF`.
4. *The Commercial Motor*, "What Will It Cost?", 6 May 1960, p.134.
   https://archive.commercialmotor.com/article/6th-may-1960/134/what-will-it-cost
5. A. J. P. Wilding, "Bristol RE single-deck bus chassis", *The Commercial Motor*, 4 November 1966,
   p.64. https://archive.commercialmotor.com/article/4th-november-1966/64/bristol-re-single-deck-bus-chassis
6. *The Commercial Motor*, "More o-m-o double-deckers for Manchester", 10 May 1968, p.33.
   https://archive.commercialmotor.com/article/10th-may-1968/33/more-o-m-o-double-deckers-for-manchester
7. *The Commercial Motor*, "Standardization?", 20 December 1968, p.25.
   https://archive.commercialmotor.com/article/20th-december-1968/25/standardization
8. *The Commercial Motor*, "In brief", 22 January 1965, p.30 (Cardiff Guy Arab V chassis and body).
9. *The Commercial Motor*, "Now Fleetlines for Coventry", 31 July 1964, p.24.
10. *The Commercial Motor*, "Low price-tag on low-floor bus", 16 March 1995, p.16.
11. *The Commercial Motor*, "Trolleybuses cheaper than motorbuses", 19 September 1952, p.80.
12. *The Commercial Motor*, "From Cardiff to Edinburgh on one foot", 6 August 1965, p.48 (ERF
    automatic transmission).
13. *The Commercial Motor*, "Improved psv from Ford", 31 July 1970, p.29 (overdrive no extra cost).
14. *The Commercial Motor*, 9 August 1980, p.66, quoting the 1957 Bedford SB list.
15. *The Commercial Motor*, 15 April 1960, p.51 (Bedford SL1 two-speed axle).
16. NER carriage records, National Railway Museum, transcribed in
    `New/ai/vehicle-cost/forum-prices-part-1.md` rows 40-60.
17. Lacy and Dow, Midland Railway carriages, and Tatlow, Highland Railway carriages, via
    `forum-prices-part-1.md`.
18. Harris, GWR coaches, via `forum-prices-part-1.md`.
19. Hansard, HC Deb 11 March 1930, vol. 236, cc.1091-3, "Railway Coaches (Lighting)".
    https://api.parliament.uk/historic-hansard/commons/1930/mar/11/railway-coaches-lighting
20. History of Wallasey, "Wallasey Electric Tramway 1902-1918, part 1", quoting the 1901 tenders.
    https://www.historyofwallasey.co.uk/wallasey/Wallasey_Electric_Tramway_(1902-1918)_part_1/index.html
21. Melbourne Tram Museum, "Building the W class tram", by Warren Doubleday.
    https://www.trammuseum.org.au/papers/wclassbuild.htm
22. Blackpool Coronation component costs, in `ai/temp/research-pricing-report.md` section 2.4.
23. V. C. Solomons, "Sydney's double deck electric cars", *Trolley Wire*, May 1991.
24. D. Griffiths, "British Marine Industry and the Diesel Engine", *The Northern Mariner*, 1997,
    reproducing W. G. Cleghorn, "Steam versus Diesel Machinery for Cargo Vessels", *Trans. IESS* 70
    (1926), and A. E. Seaton, *A Manual of Marine Engineering* (1928).
25. E. C. Smith, "The Progress of the Motor Ship", *Nature*, 24 August 1929, p.307.
26. ITDP, *BRT Standard*, "Vehicle Costs", table 20.10.
    https://brtguide.itdp.org/branch/master/guide/vehicles/vehicle-costs
27. TRL Report 271, *Evaluation of low-floor bus trials in London and North Tyneside*, 1998.
    https://www.trl.co.uk/uploads/trl/documents/TRL271.pdf
28. Pullman Car Services Archive, *Special Edition No.13*, "BR Mark 1 Pullman Cars 1960-1961",
    including the 1957 tender enquiry. https://sremg.org.uk/coach/coupe/coupe_se13.pdf
