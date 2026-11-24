# Coal consumption of British steam tram engines

Research report for the six steam tram objects in `New/trams/`. Prepared 2026-11-24.
All conversions: 1 lb = 0.45359237 kg; 1 mile = 1.609344 km; 1 lb/mile = 0.281849 kg/km.

---

## 1. The answer

A British steam tram engine in ordinary street service burned **about 19 to 35 kg of coal or
coke per hour** for a 6.5-7 ton engine and up to about 50 kg/h for an 11-ton one, which is
**about 5 to 7 kg per hour per square foot of grate** while running, and **about 1.6 to 3.1 kg
per kilometre**. The fire was demand-limited, not grate-limited: the same engine that could burn
12-15 kg/h/sq ft in a short burst on a 1-in-25 gradient averaged 5-7 kg/h/sq ft over a shift, and
about 1.5-2 kg/h/sq ft while standing at a terminus with the damper shut. Thermal efficiency,
coal to drawbar, was **about 2.5-3.0 per cent** over a stop-start duty — roughly half the 4-6 per
cent of a saturated main-line locomotive, but for a different reason: the tram engine's boiler
and engine were not much worse, they simply spent most of the day at part load, standing, or
accelerating from rest, and the standing losses were charged against relatively few miles. The
pakset's present efficiency band of 2.25-4.00 per cent is therefore right. Its burn rate of
2.50-3.00 kg/h/sq ft is wrong by a factor of about two, and its `power` figures of 2-6 kW are
wrong by a factor of three to ten; the `fuel_per_km` figures, however, are only 0-50 per cent low,
because the change of `calibration_speed` from half speed to full speed doubled the hourly burn
the `.dat` files actually charge. The recommended values are in §7. Confidence: moderate to good
on the burn rate and efficiency (±25 per cent), moderate on the individual engines (±20-25 per
cent, worse for the smallest Merryweather), and high that the present derivation is unsound and
that the true burn rate is nearer 6 than 2.5 kg/h/sq ft.

---

## 2. What the present figures actually do

The six rows on `New/steam-physics-calcs.ods`, sheet `Extrapolation`, do not contain a measured
burn rate. They contain a typed grate area, a typed burn rate of 2.50-3.00 kg/h/sq ft, a typed
efficiency of 2.25-4.00 per cent, and a power calculated from the three:

`power = grate × burn rate × calorific value × efficiency`

For Kitson no. 1 that is 5.17 × 2.50 × 6.784 × 0.03 = **2.63 kW**. The power is an output of
the assumptions, not a check on them. Nothing in the row tests 2.63 kW against a rated
horsepower, a tractive effort or a measured coal account.

Three defects follow from this.

**The rows are not calculated the same way.** Rows 117, 123, 124, 132 and 147 type the
efficiency and derive the power. Row 140 (Kitson no. 2) types the power (4 kW) and derives the
efficiency (3.93 per cent) by the inverse formula. The six figures are therefore not a
consistent set even internally.

**The same row contradicts itself by a factor of ten.** Column M, headed "Max.", holds
`(heating surface ÷ 2.5) × 0.7457` — the sheet's own estimate of the boiler's maximum output.
For these six engines it reads 32, 35, 50, 32, 38 and 45 kW. The power column reads 2, 3, 3, 3,
4 and 6 kW. The sheet simultaneously asserts that a Kitson no. 1 boiler can develop 35 kW and
that the engine develops 3 kW.

**The hourly burn in the `.dat` is double the sheet's.** The sheet's `kg/km` cell is
`burn rate ÷ (speed ÷ 2) × grate`, that is, kilogrammes per kilometre at *half* the maximum
speed. The `.dat` files set `calibration_speed` to the *full* maximum speed while keeping that
`kg/km` figure. Because `fuel_per_km × calibration_speed` is the hourly burn the engine
charges, every tram now burns twice what the sheet specifies: Kitson no. 1 is charged
1.62 kg/km × 16 km/h = **25.9 kg/h**, not 12.9 kg/h. The effective burn rate in the shipped
data is therefore **5.0-6.0 kg/h/sq ft**, not 2.5-3.0.

That accident is why the `.dat` figures are closer to the evidence than the sheet is.

---

## 3. The evidence

### 3.1 Company coal and coke accounts (the strongest evidence)

All of the following are coal or coke *issued per mile run* — the quantity the brief asks for.
They come from D. Kinnear Clark, *Tramways: Their Construction and Working*, 2nd edition
(London: Crosby Lockwood & Son, 1894), chapter II, "Mechanical Power on Tramways", which
reproduces the companies' own monthly and annual returns. Full text:
<https://archive.org/details/tramwaystheircon00clar> (a second, better scan at
<https://archive.org/details/tramwaystheircon02clargoog>).

| Line | Engine | Gross load | Speed | Fuel | lb/mile | kg/km | kg/h |
|---|---|---|---:|---|---:|---:|---:|
| Dewsbury, Batley & Birstal, 1881 | Merryweather, 7 t | 10 t | 6.0 mph | coke, 122½ t over 39,700 miles | **6.91** | **1.95** | 18.8 |
| Wantage, c. 1881 | Hughes, 6.5 t | 13.1 t | 9.4 mph | coke, 307 lb/day over 40 miles | **7.67** | **2.16** | 32.7 |
| Rouen, March 1881 | Merryweather condensing, 6.5 t | 14 t | 6.05 mph | coke, 5.36 kg/mile | **11.8** | **3.33** | 32.4 |
| Paris, Bastille-Charenton, 1879-80 | Hughes, 7.5 t | 11.65 t | 7.0 mph | coke, 17 lb | **17.0** | **4.79** | 54.0 |
| Bristol, Horfield, c. 1881 | Hughes, 7 t | 11 t | ~6.5 mph | coke, 12½ t/week over 1,717 miles | **16.31** | **4.60** | ~48 |
| Lille-Haubourdin, 1880 | Hughes, 10 t | — | — | coke, 17½ lb | **17.5** | **4.93** | — |
| Philadelphia, Market Street, 1877 | Baldwin steam car | — | ~8 mph | coal, 4,950 lb over 616 miles | **8.03** | **2.26** | ~29 |
| Coney Island, 1876 | Ransom steam car | — | 13.5 mph running | coal, 600 lb/day over 81 miles | **7.40** | **2.09** | — |
| Dublin & Lucan, 1881 | Perrett steam car, 9 t | 10.5 t | 8 mph | gas coke, 6 cwt/day over 52 miles | **12.9** | **3.64** | ~46 |
| Lausanne, c. 1881 | Brown steam car | — | 9 mph | coal, 3 cwt/day over 29 miles | **11.5** | **3.24** | ~46 |

What the table shows is a clean split. On **level or near-level** lines the figure is
**6.9-8.0 lb/mile (1.95-2.26 kg/km)** regardless of whether the engine was British, French or
American. On **severe gradients** (Rouen 1 in 20 and 1 in 40; Bristol 1 in 24 to 1 in 68;
Lille 1 in 22; Paris 1 in 20 to 1 in 29) it is **16-17.5 lb/mile (4.6-4.9 kg/km)**, two and a
half times as much. The difference is gradient work, not engine type.

The locomotive-hauled trains were all an engine and **one car** (Wantage excepted, with two), so
for those the coal per car-mile is the same as the coal per engine-mile: **6.9-8.0 lb per
car-mile on the level, 12.9-17.5 lb on the graded lines**. That is the figure the brief asked
for, and it is the one to compare with the pakset, because the pakset charges the engine for its
own fuel and the car separately for its weight.

The **Dewsbury** account is the single most valuable item, and it is the closest analogue to the
pakset's Kitsons: a 7-ton Merryweather engine, a 3-ton car with eleven passengers (10 tons
gross), a line with a falling gradient of 1 in 200, 15 to 25 stops each way over 3.5 miles, a
6 mph average, and a measured annual issue of 122½ tons of coke against 39,700 engine-miles.
That is 6.911 lb/mile, checked from the tonnage as well as read from the text
(122.5 × 2240 ÷ 39,700 = 6.91). At 6 mph it is 41.5 lb/h = **18.8 kg/h**.

The **Wantage** account is the second: a 6.5-ton Hughes engine, two cars, 13.1 tons gross,
9.4 mph average, 307 lb of coke a day over 40 miles = 7.67 lb/mile = **32.7 kg/h**. Its
consumption per ton-mile, 0.58 lb, is the lowest in the set and the best efficiency case.

Two more figures put the range of manufacturer claims around the same place. Clark records that
the Burnley tramways engines (Falcon Works, 8-inch cylinders, one 46-passenger car, gradients
1 in 17 to 1 in 20, governor limiting to 10 mph) were "stated to be at the rate of from 8½ lbs
to 9 lbs per mile-run" — **2.40-2.54 kg/km**. And the 1885 Institution of Civil Engineers
correspondence records a Henschel engine of the Merryweather type, 8 tons, taking 40 tons gross
up 1 in 30 at 10 mph on "10 lbs of coal per mile" — 2.82 kg/km, with fifteen engines averaging
nearly 14,000 miles each in 1883 (Minutes of the Proceedings of the ICE, vol. 79, 1885,
correspondence p. 184 ff., <https://doi.org/10.1680/imotp.1885.21519>).

The Castlederg and Victoria Bridge Steam Tramway (two 14-ton Kitsons, 12 in × 15 in cylinders,
160 psi) spent 1.80d per mile on coal in the half-year to December 1884 over 9,464 miles. The
same volume's discussion of the Henschel engines quotes coal at 32s 6d a ton; at that price
1.80d buys 10.3 lb, or **2.90 kg/km**. At 25s a ton it would be 13.4 lb, or 3.8 kg/km. The coal
price is the weak link here, so I treat this as corroboration only.

### 3.2 What the figures mean per hour and per square foot

The hourly figures in the last column above are the product of lb/mile and speed. They are the
quantity the pakset's `fuel_per_km × calibration_speed` represents, and they are large:
**19-33 kg/h for a 6.5-7 ton engine**, 45-54 kg/h for the 7.5-10 ton Hughes engines on severe
gradients.

The corresponding grate figures need the grate areas, which the sources give only patchily.
Clark gives 4.8 sq ft for the 10-ton Stoke-on-Trent Merryweather (197.3 sq ft heating surface)
and 3.82 sq ft for the Lille Hughes (162.5 sq ft). A 6.5-7 ton Merryweather of the Dewsbury or
Rouen type had a grate of about 4-4.5 sq ft. On that basis:

- Dewsbury: 18.8 kg/h ÷ 4.0-4.5 sq ft = **4.2-4.7 kg/h/sq ft**.
- Rouen: 32.4 kg/h ÷ 4.5 sq ft = **7.2 kg/h/sq ft** (severe gradients).
- Wantage: 32.7 kg/h ÷ 5-6 sq ft = **5.5-6.5 kg/h/sq ft**.

So **4-7 kg/h/sq ft in service**, centred on about 5.5, with the high end belonging to gradient
work and the low end to a level line at 6 mph. The present sheet's 2.5-3.0 is well below the
bottom of the measured range, and is not supported by any account I found.

### 3.3 The fire is demand-limited, not grate-limited

This is the conceptual correction that matters more than any single number. A main-line
locomotive's 27-45 kg/h/sq ft is a *maximum-output* figure: the fireman stokes a thin fire as
fast as the blast pipe will draw it, and the grate area is what limits the boiler. A tram
engine's fire is built up at the terminus and then left; Hughes's engines were described as
having the fire "made up at the beginning of the trip, and not touched during the passage", and
lasting a ten-mile run without fresh stoking (Clark, p. 457). The grate is therefore not the
independent variable. The coal burned is whatever the work demands, plus the standing loss, and
the burn rate per square foot is an *output* of the duty cycle.

The grate does bind at the top end. Clark's Kitson standard table rates no. 3 (9 × 15 in
cylinders, 8 tons empty, 10¾ tons in working order) to take 19 tons net up 1 in 25 at 6 mph.
That duty — 29.75 tons gross against 1 in 25 plus 30 lb/ton of resistance — is about 15.8 kN of
tractive effort at 2.68 m/s, or 42 kW at the rail. At 4-5 per cent efficiency that needs
105-131 kg/h, or **12-15 kg/h/sq ft** on its 8.8 sq ft grate. So the tram engine's *maximum*
burn rate was about a third of a hard-worked locomotive's, and its *service average* about a
sixth. Both statements are true at once, which is why the brief's two "internally consistent
readings" do not exhaust the possibilities: the third reading — low average output, moderate
burn rate, low efficiency — is the correct one.

### 3.4 Cross-check against the pakset's measured steam wagons

The road sector's figures, from *Commercial Motor* tests, are the closest measured analogue in
the pakset's own data:

| Vehicle | Load | Speed | lb/mile | kg/km |
|---|---|---:|---:|---:|
| Foden (1910, five in service) | 8-9 t | — | 7.90-9.35 | 2.23-2.64 |
| Super-Sentinel (1923) | 8.2 t | 13.3 mph | 5.91 | 1.67 |
| Sentinel DG6 (1927) | 12 t | 17.05 mph | 8.66 | 2.44 |
| Sentinel DG6 (1930) | 12 t | — | 5.21 | 1.47 |
| Sentinel S4 (1933) | — | — | 2.94 | 0.83 |
| Sentinel S4 (1968 re-test) | — | ~25 mph | — | 1.05 |

A steam tram should sit at or a little above the lower half of that band: it ran more slowly
than a wagon (much less windage and rolling resistance per ton-mile) but stopped far more often
and had an older, low-pressure, saturated engine. My recommended 1.6-3.1 kg/km does exactly
that. A figure above about 3.5 kg/km would need a gradient or a very heavy train to explain it;
a figure below about 1.2 kg/km would be hard to reconcile with a 7-ton engine hauling a car.

---

## 4. The efficiency question

The present 2.25-4.00 per cent band is **right**, and for the right order of magnitude. Three
independent lines of evidence support it.

**From the measured coal and the tractive work.** Take the Dewsbury account. Clark's own adopted
average resistance for tram rails is 30 lb/ton (he gives 15 lb/ton on clean wet rails as a
minimum and 60 lb/ton as an occasional maximum). For 10 tons gross that is 300 lb = 1334 N,
or 0.596 kWh per mile. About 5.7 stops per mile at 6 mph add 0.058 kWh, giving 0.654 kWh/mile
at the rail. The coal, 6.911 lb = 3.135 kg, is 25.4 kWh of input at 8.1 kWh/kg. Overall
efficiency = **2.6 per cent**. The Wantage account, worked the same way (13.1 tons, 9.4 mph,
only the terminus stops, 7.67 lb/mile), gives **2.8-2.9 per cent**. A resistance of 20 lb/ton
instead of 30 lowers these to 1.8-1.9 per cent; 40 lb/ton raises them to 3.4 and 3.7 per
cent. The band is 1.8-3.7 per cent, centred on 2.6-3.0.

**From the boiler.** The 1885 ICE correspondence gives a measured evaporation for the Wilkinson
boiler with Field tubes of **9.7 lb of water per lb of coke** (the source calls it "evaporative
efficiency"; it is an evaporation ratio), feed at 62°F, blowing off at 50 psi. That is about
11,100 BTU recovered from perhaps 12,500 BTU of coke — **85-89 per cent boiler efficiency**, far
above what a hard-worked locomotive boiler achieves. Small, lightly fired boilers with generous
heating surface relative to the firing rate are efficient boilers. The loss in a tram engine is
not in the boiler.

**From the engine.** A small saturated engine of this period, running at 25-40 per cent cut-off
with 30-35 lb of steam per indicated horsepower-hour, converts 6-7 per cent of the coal's heat
into indicated work; at 85 per cent mechanical efficiency that is 5-6 per cent at the drawbar
*while working*. The service figure of 2.6-2.9 per cent is about half that, and the difference
is exactly the standing and part-load loss: Dewsbury's engines stopped 15-25 times each way over
3.5 miles, and Rouen's were 10 h 8 min on duty but 12 h 40 min in steam, with the fire burning
through every stop and every wait at the terminus.

So the efficiency is not the defect. A tram engine was *not* a 2 per cent machine by
construction; it was a 5 per cent machine that spent half its coal staying hot. That distinction
matters for the pakset because `fuel_per_km` is charged only while moving, so the correct
figure is the service average (which includes the standing loss spread over the miles), not the
instantaneous running rate. The measured lb/mile accounts are already service averages, which is
why they are the right basis.

Two errors in the sheet's efficiency treatment are worth recording anyway. The Kitson and
Merryweather rows are assigned a calorific value of **6.784 kWh/kg**, which is sub-bituminous
coal; British tram engines burned bituminous coal or coke at 8.1 kWh/kg. That assignment makes
every derived power 16 per cent low for a given efficiency. And the Wilkinson row alone uses
8.115, so the six rows are not even on a common calorific basis.

---

## 5. Service speed, and the pakset's top speed

The brief asked for the documented service speed, and the evidence requires a qualification to
the premise.

**The legal limit was 8 mph.** The Board of Trade requirements for steam on tramways, as
reproduced by Parsons from the 1875 regulations, required a governor that shut off steam and
applied the brakes at 10 mph, and then provided: "The speed at which the engine and carriages
shall be driven or propelled along the tramways shall not exceed the rate of **8 miles an hour**,
and the speed at which such engine shall pass through movable facing points shall not exceed the
rate of 4 miles an hour" (Parsons, pp. 99-100). Clark's Appendix prints the later template, in
which the speed in regulation IV is left blank to be fixed in each Provisional Order, but the
Orders follow the same pattern; the Merryweather engine built for the Board of Trade had a
centrifugal governor that closed the throttle "when the speed exceeds eight miles per hour".

**Service averages were lower still.** Rouen was limited to 5 mph in town and 8 mph outside and
averaged 6.05 mph; Dewsbury averaged 6 mph; Bristol ran 65½ miles per engine per day, implying
6-7 mph; Wantage averaged 9.4 mph (a rural light railway rather than a street tramway).
Wilkinson's engine is described as having a "regulation speed of 8 miles per hour", with a
piston speed of 436 ft/min at that speed.

**Mechanical capability was higher, but it was not used.** The same Wilkinson engine "has been
worked at a speed of 16 miles per hour"; the Baldwin car reached 16-18 mph; Brown's car 19 mph.
So 16-20 mph was attainable on the level, as the brief says. It was not the normal street speed
and it was nearly twice the legal limit. The distinction matters: the brief's "normally ran at up
to about 20 mph" is not supported — the engines *could* do it, but the Orders, the governors and
the traffic prevented it.

**What this means for the pakset.** The six objects are coded at 12-16 km/h, which is 7.5-10
mph. That is a good match to the 8 mph legal limit and the 10 mph governor threshold, and about
40-55 per cent below the demonstrated mechanical maximum. As a *maximum speed* in the Simutrans
sense the figures are therefore defensible, and I would not change them; the Kitsons at 16 km/h
(10 mph) are at the governor setting and the Merryweathers at 12-14 km/h are at or just below
the legal limit. The earlier suspicion that the pakset had confused service speed with maximum
speed is only partly right: it has used the legal/service limit, which is the correct constraint
for a street tramway, not the machine's capability. No change is recommended.

If a player wants the engines to be able to run at their mechanical maximum outside town, the
defensible values would be 19-20 km/h (12 mph) for the smaller engines and 24-26 km/h (15-16
mph) for the Kitsons, with 32 km/h (20 mph) as the demonstrated maximum on level track. That is
a gameplay choice, not a historical correction.

---

## 6. How the per-engine figures were derived

I used the measured accounts as anchors and scaled by engine and train weight, because the
standing loss scales with the boiler (roughly the engine's size) while the running loss scales
with the gross load. Fitting `F = a·W_engine + b·W_gross` to the two level-line accounts
(Dewsbury: 7 t engine, 10 t gross, 6.91 lb/mile; Wantage: 6.5 t engine, 13.1 t gross,
7.67 lb/mile) gives **a = 0.52, b = 0.33 lb/mile per ton**. The fit reproduces both anchors
exactly and predicts Rouen's 14-ton gradient duty at 8.0 lb/mile against the measured 11.8, the
difference being the gradients, as it should be.

Applying that to each engine with one tramcar and passengers (6 tons for the Kitsons and the
Wilkinson, 5 tons for the smaller Merryweathers) gives the values in §7. The figures are at
6-9 mph; the measured per-mile rate falls only slowly with speed above that (the fixed term is
about two-thirds of the total), so they can be used at the pakset's 12-16 km/h without a
correction larger than the uncertainty. The implied burn rate per square foot is then a check,
not an input: it comes out at 4.8-7.5 kg/h/sq ft, consistent with §3.2.

---

## 7. The six objects

Recommended `fuel_per_km` in grammes of bituminous coal per kilometre, with the implied hourly
burn, the implied burn rate per square foot of grate, and the average power at 2.8 per cent
efficiency. `calibration_speed` is left at the object's present maximum speed, per the pakset's
design rule. **These are recommendations only; no `.dat` file has been edited.**

| Object | `fuel_per_km` now | **Recommended** | `calibration_speed` | kg/h implied | Grate (sq ft) | kg/h/sq ft | Avg kW at 2.8% | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `kitson-standard-1` | 1620 | **2200** | 16 | 35.2 | 5.17 | 6.8 | 8.0 | Dewsbury + Wantage scaling; 7 t engine, 13 t gross |
| `kitson-standard-2` | 1880 | **2800** | 16 | 44.8 | 6.00 | 7.5 | 10.2 | Scaling between Dewsbury and Wantage; 9.5 t engine, 15.5 t gross |
| `kitson-standard-3` | 2750 | **3100** | 16 | 49.6 | 8.80 | 5.6 | 11.3 | Class table duty (19 t up 1 in 25); 11 t engine, 17 t gross |
| `merryweather-standard-1` | 1670 | **1600** | 12 | 19.2 | 4.00 | 4.8 | 4.4 | Extrapolated below the anchor range; 4 t engine, 9 t gross. Low confidence |
| `merryweather-standard-2` | 1590 | **1650** | 14 | 23.1 | 3.70 | 6.2 | 5.2 | Scaling; 5 t engine, 10 t gross |
| `wilkinson-engine` | 1720 | **1780** | 16 | 28.5 | 5.00 | 5.7 | 6.5 | Scaling; 5.5 t engine, 10.5 t gross; 2:1 gearing |

The weight-scaling fit gives 2235, 2836, 3194, 1423, 1663 and 1783 g/km respectively. I have
rounded the first three down by 1-3 per cent, because the linear fit over-penalises a larger
grate at part load. I have raised the Merryweather no. 1 by 12 per cent above the fit, because
the fit is an extrapolation below its lightest anchor (6.5 tons) and the fixed loss of a boiler
does not fall in proportion to weight; the present 1670 is also within the uncertainty band.
Everything except the Merryweather no. 1 is within 3 per cent of the fitted value.

**Implied efficiency of the recommended figures:** 2.8 per cent overall in each case, by
construction. The central evidence band is 2.6-3.0 per cent, so the pakset's 2.25-4.00 per cent
needs no change. If a reviewer prefers 2.5 per cent, the grammes rise by 12 per cent; at 3.0 per
cent they fall by 7 per cent.

**Real rating (not to be changed in `power`, but reported as the brief asks).** These engines
were rated at roughly **30-45 hp (22-34 kW) maximum** for the Kitsons and the Wilkinson, and
**15-25 hp (11-19 kW)** for the two Merryweathers. The evidence: Clark's class table rates the
Kitson no. 3 to 19 tons net up 1 in 25 at 6 mph, which is 42 kW at the rail; the Stoke
Merryweather took 9-10 tons up 1 in 16 at 4-5 mph, about 28-31 kW; the sheet's own
heating-surface column caps the six boilers at 32-50 kW. The pakset's 2-6 kW is not a rating at
all — it is the output that fell out of a 2.5 kg/h/sq ft assumption, and it is 3-10 times too
low. The average power over a shift, at 2.8 per cent and the recommended coal, is 4-11 kW, which
is consistent with a 30-45 hp maximum at 20-30 per cent average load.

---

## 8. What I could not establish, and what would settle it

**What I could not establish.**

1. **A boiler trial with indicator diagrams.** I found no trial of a tram engine giving coal per
   hour, water evaporated and indicated horsepower together. The 9.7 lb water/lb coke figure is a
   boiler measurement, not an engine trial; it also comes from the ICE correspondence as indexed
   by the search engine, not from a page image, because the ICE library returns 403 to a direct
   fetch. The efficiency above is derived from coal and tractive work, not measured at the
   cylinder, and that derivation does not depend on the 9.7 figure.
2. **A coal account with both tonnage and price for a British line**, which would let the
   lb/mile be read directly rather than inferred. Dewsbury gives both (122½ tons over 39,700
   miles, coke at 23s 6d); Birmingham & Aston gives only the cost, 0.90d per mile over 176,528
   miles, and without its coke price that is anything from 7 to 14 lb/mile. I did not find the
   price.
3. **The grate areas of the Dewsbury, Wantage and Rouen engines.** The per-square-foot figures
   in §3.2 rest on 4-6 sq ft, inferred from Clark's 4.8 sq ft Stoke engine and 3.82 sq ft Lille
   engine. A measured grate area for a 7-ton Merryweather would tighten them.
4. **Whether the figures are coal or coke.** Most of the accounts are coke, which has a similar
   calorific value per kilogramme (8.08 vs 8.11 kWh/kg) but different combustion behaviour and
   price. For `fuel_per_km` in kilogrammes this does not matter, as the pakset's steam doc
   already notes; for the economics it does.
5. **Anything useful in the Simutrans forum thread.** I checked page 1 of
   `topic=6521.0`; it is a vehicle-and-carriage-price thread and contains no tram fuel figure.
   I did not exhaust all nine pages.

**What would overturn the conclusion.**

- A tramway company account showing **under 3 lb/mile on a level line at 8-10 mph** (about
  11 kg/h on a 4.5 sq ft grate). That would put the burn rate back near 2.5 kg/h/sq ft and
  vindicate the sheet.
- A boiler or road trial showing a 7-ton tram engine developing **3-4 kW average** over a shift,
  which would mean the fire really was burning at 2.5 kg/h/sq ft.
- Evidence that British tram engines **normally ran at 15-20 mph in service** rather than 6-9
  mph. That would cut coal per kilometre by 30-40 per cent for the same hourly burn and bring
  the figures down towards 1.2-1.5 kg/km. The byelaw and Order evidence points the other way,
  but a municipal line with a 12 mph order and long inter-stop distances would qualify.
- A measured evaporation **below 6 lb of water per lb of coal** for a tram boiler, which would
  push the efficiency towards 1.5-2 per cent and require either more coal or less work for the
  same duty.
- A measured grate area much smaller than 4 sq ft on the 7-ton engines, which would raise the
  burn rate per square foot above 7 and make the "grate-limited" reading more nearly right.

**What would confirm it further.** The Birmingham & Aston and Dudley & Stourbridge coke
accounts, with tonnages (both are quoted only as pence per mile in Clark); the Manchester, Bury,
Rochdale & Oldham and South Staffordshire accounts, which between them worked 97 engines and
would give a large sample; and any Kitson or Merryweather specification sheet stating coal per
mile for the standard classes.

---

## 9. Sources

1. D. Kinnear Clark, *Tramways: Their Construction and Working*, 2nd ed., Crosby Lockwood &
   Son, 1894. Chapter II, "Mechanical Power on Tramways", pp. 430-495, and Appendix,
   "Regulations ... with respect to the use of Steam Power on Tramways", pp. 699-701.
   <https://archive.org/details/tramwaystheircon00clar> and
   <https://archive.org/details/tramwaystheircon02clargoog>.
   Figures used: Dewsbury, Batley & Birstal (p. 453); Rouen (p. 445); Paris
   Bastille-Charenton (p. 461); Bristol Horfield (p. 462); Lille-Haubourdin (p. 464); Burnley
   (p. 468); Kitson standard classes (pp. 469-471); Wantage (p. 491); Baldwin (p. 433);
   Ransom; Perrett; Brown; Mekarski at Nantes (pp. 519-520).
2. R. C. Parsons, "The Working of Tramways by Steam", *Minutes of the Proceedings of the
   Institution of Civil Engineers*, vol. 79 (1885), pp. 98-119, including the Board of Trade
   requirements at pp. 99-100; discussion pp. 128-160; fuel table p. 115.
   <https://doi.org/10.1680/imotp.1885.21516>.
3. "Correspondence. Steam Tramways", *Minutes of the Proceedings of the ICE*, vol. 79 (1885),
   pp. 184 ff. <https://doi.org/10.1680/imotp.1885.21519>. Castlederg coal account (1.80d per
   mile over 9,464 miles); Wilkinson boiler evaporation 9.7 lb water/lb coke; Henschel 8-ton
   engine at 10 lb coal per mile.
4. *Iron*, 20 May 1876, report of the Merryweather trial on the Dewsbury, Birstall & Batley
   Tramway, quoted in the Industrial Railway Society archive,
   <https://shop.irsociety.co.uk/Archives/60/Tramway.htm>.
5. D. K. Clark, *The Steam Engine: A Treatise on Steam Engines and Boilers*, vol. IV, Blackie &
   Son, 1890, description of the Merryweather condensing tram engine (8 mph governor), quoted at
   the same IRS page.
6. `New/steam-physics-calcs.ods`, sheet `Extrapolation`, rows 117, 123, 124, 132, 140, 147, and
   the `Max.` formula in column M. Read directly from the file.
7. `New/ai/fuel/road-derivation.md` §1.3 (S14-S22), for the *Commercial Motor* steam-wagon
   figures used as the cross-check in §3.4.
8. `New/trams/*.dat` for the present `fuel_per_km`, `calibration_speed`, `power` and `speed`.
