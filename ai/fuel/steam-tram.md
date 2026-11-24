---
status: draft
verified: New ex-15 working tree @ e7f821c7d
---
# Fuel consumption: steam tram engines

**Covers**: the six steam tram engines in `New/trams/` — `kitson-standard-1`, `kitson-standard-2`,
`kitson-standard-3`, `merryweather-standard-1`, `merryweather-standard-2` and `wilkinson-engine` —
and why their coal figures are not railway locomotive figures. Engine semantics and the unit
convention: [fuel-consumption](../fuel-consumption.md). Railway steam is in [steam](steam.md).

## Why a tram engine is a separate case

A railway locomotive works with two men: the fireman shovels coal continuously onto a thin fire, the
blast pipe gives a hard draught, and the boiler meets a large and continuous demand. The measured
result is 27 to 45 kg of coal per hour per square foot of grate.

A tram engine worked with a driver alone. The fire was built up at the terminus, the damper shut
while the engine waited, and the fire stoked again at the next terminus. The draught was weak, the
grate small, and the work — one tramcar at 8 mph — far lighter.

**The fire is demand-limited, not grate-limited.** Grate area sets the maximum the boiler can be
forced to, not the average it burns. The same engine that could burn 12 to 15 kg/h/sq ft in a short
burst on a 1 in 25 gradient averaged 5 to 7 over a shift, and about 1.5 to 2 while standing at a
terminus with the damper shut. Any derivation from grate area alone therefore overstates a tram
engine's coal, which is what the pakset's steam sheet did.

## The evidence

The strongest evidence is the companies' own coal and coke accounts, reproduced in D. Kinnear Clark,
*Tramways: Their Construction and Working*, 2nd edition, 1894, chapter II.
`[LITERATURE:https://archive.org/details/tramwaystheircon00clar]` Each is a measured issue of fuel
against miles run:

| Line | Engine | Gross load | Speed | Fuel | lb/mile | kg/km | kg/h |
|---|---|---|---:|---|---:|---:|---:|
| Dewsbury, Batley & Birstal, 1881 | Merryweather, 7 t | 10 t | 6.0 mph | coke, 122½ t over 39,700 miles | 6.91 | 1.95 | 18.8 |
| Wantage, c. 1881 | Hughes, 6.5 t | 13.1 t | 9.4 mph | coke, 307 lb/day over 40 miles | 7.67 | 2.16 | 32.7 |
| Rouen, 1881 | Merryweather condensing, 6.5 t | 14 t | 6.05 mph | coke, 5.36 kg/mile | 11.8 | 3.33 | 32.4 |
| Paris, 1879-80 | Hughes, 7.5 t | 11.65 t | 7.0 mph | coke, 17 lb | 17.0 | 4.79 | 54.0 |
| Bristol, c. 1881 | Hughes, 7 t | 11 t | ~6.5 mph | coke, 12½ t/week over 1,717 miles | 16.31 | 4.60 | ~48 |
| Lille, 1880 | Hughes, 10 t | — | — | coke, 17½ lb | 17.5 | 4.93 | — |
| Philadelphia, 1877 | Baldwin steam car | — | ~8 mph | coal, 4,950 lb over 616 miles | 8.03 | 2.26 | ~29 |
| Dublin & Lucan, 1881 | Perrett steam car, 9 t | 10.5 t | 8 mph | gas coke, 6 cwt/day over 52 miles | 12.9 | 3.64 | ~46 |

The split is by gradient, not by engine. On level or near-level lines the figure is 6.9 to 8.0
lb/mile, 1.95 to 2.26 kg/km, whatever the country of origin. On the severely graded lines — Rouen
1 in 20, Bristol 1 in 24, Lille 1 in 22, Paris 1 in 20 — it is 16 to 17.5 lb/mile, 4.6 to 4.9 kg/km.

Two further figures corroborate the range: the Burnley engines were "stated to be at the rate of from
8½ lbs to 9 lbs per mile-run" (2.40 to 2.54 kg/km), and the 1885 Institution of Civil Engineers
correspondence records a Henschel engine taking 40 tons gross up 1 in 30 at 10 mph on 10 lb of coal
per mile (2.82 kg/km). `[LITERATURE:https://doi.org/10.1680/imotp.1885.21519]`

The Dewsbury account is the single most valuable item: a 7-ton Merryweather, a 3-ton car with eleven
passengers, a line with a falling gradient of 1 in 200, 15 to 25 stops each way over 3.5 miles, and
122.5 tons of coke issued against 39,700 engine-miles. That is 6.911 lb/mile, checkable from the
tonnage alone (122.5 × 2240 ÷ 39,700).

## Burn rate and efficiency

On grate areas of 4 to 6 square feet for these engines, the measured accounts give **4 to 7 kg per
hour per square foot in service, centred on about 5.5**, with the high end belonging to gradient work
and the low end to a level line at 6 mph. The steam sheet's 2.50 to 3.00 is below the bottom of the
measured range.

Thermal efficiency, coal to drawbar, is **about 2.5 to 3.0 per cent over a stop-start duty**, against
4 to 6 per cent for a saturated main-line locomotive. The reason is not a worse boiler: the tram
engine spent most of its day at part load, standing, or accelerating from rest, and the standing
losses were charged against relatively few miles. A measured 9.7 lb of water per lb of coke evaporated
for the Wilkinson boiler is consistent with this. The steam sheet's band of 2.25 to 4.00 per cent
needs no change.

## The figures

`fuel_per_km` is the service average per kilometre, as the pakset's calibration rule requires.
Calibration speed is each object's existing maximum speed.

| Object | Before | Now | Implied kg/h | Grate, sq ft | kg/h/sq ft | Confidence |
|---|---:|---:|---:|---:|---:|---|
| `kitson-standard-1` | 1620 | **2200** | 35.2 | 5.17 | 6.8 | moderate |
| `kitson-standard-2` | 1880 | **2800** | 44.8 | 6.00 | 7.5 | moderate |
| `kitson-standard-3` | 2750 | **3100** | 49.6 | 8.80 | 5.6 | moderate |
| `merryweather-standard-1` | 1670 | **1600** | 19.2 | 4.00 | 4.8 | low |
| `merryweather-standard-2` | 1590 | **1650** | 23.1 | 3.70 | 6.2 | low to moderate |
| `wilkinson-engine` | 1720 | **1780** | 28.5 | 5.00 | 5.7 | moderate |

The six were derived by fitting `fuel per mile = a × engine weight + b × gross weight` to the two
level-line accounts, which gives 0.52 and 0.33 lb per mile per ton and reproduces both exactly, and
then applying it to each engine with one car. Everything except the smallest Merryweather is within
3 per cent of that fit; it is extrapolated below the lightest anchor and raised 12 per cent for the
fixed loss of a boiler that does not fall in proportion to weight.

The uncertainty is about ±25 per cent on the burn rate and ±20 to 25 per cent on the individual
engines. At 2.5 per cent efficiency instead of 2.8 the figures rise 12 per cent; at 3.0 they fall 7.

The full derivation, with every source and the weight-scaling fit: [steam-tram-derivation](steam-tram-derivation.md).

## Power

The `power` figures were 2 to 6 kW, which is not a rating at all: they were the output that fell out
of the sheet's 2.50 kg/h/sq ft burn rate and its 2.25 to 4.00 per cent efficiency, never checked
against a rated horsepower. They are now set from the one documented duty rating in the evidence,
scaled by engine weight, which is how boiler size scales:

| Object | Was, kW | Now, kW | hp | Weight, t |
|---|---:|---:|---:|---:|
| `kitson-standard-1` | 3 | 20 | 27 | 7.0 |
| `kitson-standard-2` | 4 | 27 | 36 | 9.5 |
| `kitson-standard-3` | 6 | 31 | 42 | 11.0 |
| `merryweather-standard-1` | 2 | 11 | 15 | 4.0 |
| `merryweather-standard-2` | 3 | 14 | 19 | 5.0 |
| `wilkinson-engine` | 3 | 16 | 21 | 5.5 |

Clark's class table rates the Kitson no. 3 to haul 19 tons net up 1 in 25 at 6 mph. At Clark's own
30 lb per ton resistance that is 27 kW at the rail if the 19 tons is the trailing load and 43 kW if
it is the gross weight; the independent band from the boilers' heating surface and the other returns
is 22 to 34 kW. The figure taken is 31 kW, 42 hp, in the middle of the range, and the other five are
scaled from it. The results sit inside the researched bands: 27 to 42 hp for the Kitsons and the
Wilkinson, 15 to 21 hp for the Merryweathers.

Two checks confirm the old figures were unusable rather than merely pessimistic. The tractive efforts
already in the data are 6 to 18 kN, and a 12 kN engine at 3 kW could not use its adhesion above about
1 km/h. And at the new maximum power with the coal figures above, the implied efficiency is 6 to 7
per cent, which is what a saturated boiler reaches at full firing where its efficiency peaks; the
2.8 per cent average is over a whole shift.

What it changes in play is acceleration. A 20 kW engine with a 5-ton car accelerates at about
0.35 m/s² at line speed against 0.05 before, so the trams can now keep to a timetable at all.

## What the change to the coal did

The previous coal figures were only 0 to 50 per cent low, not ten times wrong, because the change of
`calibration_speed` from half the maximum speed to the full maximum had already doubled the hourly
burn the `.dat` files charge: the shipped data implied 5.0 to 6.0 kg/h/sq ft, not 2.50 to 3.00.

**The speeds are right, and should not be raised.** The Board of Trade requirements reproduced by
Parsons set a hard 8 mph limit for a steam tram with a 10 mph governor. The engines could reach 16 to
19 mph, but did not run there in service, so the pakset's 12 to 16 km/h is the legal and service
maximum, not a misreading.

## The fuel price

The measured accounts are mostly **coke**, not coal: Dewsbury, Wantage, Rouen, Paris, Bristol, Lille
and Dublin all issued gas coke, because a coke fire is smokeless and smoke in towns was the reason the
Tramways Act required a condensing or smokeless engine. Coke cost more per ton than coal. The
`fuel[steam]` series is a coal price, so a coke-burning tramway is charged less than it paid; a
premium of perhaps a half again would be nearer the mark. This is recorded rather than corrected,
because the price series is owned by [fuel-evidence](../fuel-evidence.md).

## Open questions

- Should coke have its own price series? Seven of the eight measured accounts above are coke, and the
  same applies to the early coke-burning railways.
- The weight scaling assumes one car. A pakset player may run two, and the engine is then charged for
  one; the engine's own weight-based physics partly compensates but does not model the extra coal.
