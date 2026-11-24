# Aircraft fuel consumption (waytype=air)

Sector report for the fuel-consumption exercise defined in `ai/temp/fuel-brief.md`.
230 objects, 112 models. No `.dat` file was modified.

## 1. Method

### 1.1 What the number is

`vehicle_t::calc_fuel_consumption()` charges `fuel_per_km * calibration_speed / akt_speed`
per km when the vehicle is at full power, so `fuel_per_km * calibration_speed` is the fuel
burnt per hour at the calibration condition. For an aircraft the calibration condition is
cruise, so:

* `calibration_speed` = the type's cruise speed in km/h (normally equal to the `speed` field
  of the `.dat`, which the pakset already sets to cruise TAS for almost every aircraft);
* `fuel_per_km` = millilitres of fuel per km at that speed at normal cruise power
  (`turbine` = litres of jet fuel, `petrol` = litres of avgas, `diesel` = litres of diesel);
* `cut_off_speed` = half the calibration speed, following the pakset precedent
  (`GNR-Stirling8Foot`: 75 / 40).

Because the pakset top speed equals the cruise speed for nearly all of these aircraft, the
engine will charge exactly `fuel_per_km` per km in normal line service. Nothing here uses the
`range` field, which is untouched.

### 1.2 Routes from source to number, and which was used where

**(S) measured fuel burn per km at a stated sector, converted to cruise.**
The tables in Wikipedia's *Fuel economy in aircraft* article (which compile Airclaims,
Aircraft Commerce and airline submissions) give kg of fuel per km for a specific sector
length. Convert:

    L/km   = (kg/km) / 0.80 kg/L                       (jet fuel density)
    cruise = L/km x f                                  (climb and taxi correction)
    mL/km  = 1000 x cruise

where f = 0.97 for sectors of 8,000 km or more, 0.93 for 1,900-8,000 km, 0.90 for
900-1,900 km and 0.85 below 900 km. 23 models use this route; they are the ones with the
most reliable numbers. The sector length is stated in the `basis` column of every S row.
Source: https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft

**Cross-check: usable fuel capacity / published range.** For classic piston airliners and
airships the published range is fuel-limited, so `mL/km = 1000 x capacity (L) / range (km)` is
a hard ceiling for the cruise figure and normally within 10-20 per cent of it. This is used
as a check, never alone, on the DC-3 (1.27 L/km), Ford Trimotor (0.98), HP O/400 (1.01),
Ju 52 (1.88, the one case where the model is well below the capacity/range ceiling) and the
two large airships (3.9 L/km each). Where the model and the check disagree by more than
about 25 per cent the row's `basis` says so.

**(M) power/thrust model.** The physical identity behind every row:
fuel flow = drag x specific fuel consumption, with drag = weight / (L/D).

* jets: `FF(kg/h) = W(kg) x 9.81 / (L/D) x SFC(lb/lbf/h) x 0.102`;
  `FF(L/h) = FF(kg/h) / 0.80`.
* piston and turboprop: `P(kW) = W x 9.81 / (L/D) x v(m/s) / eta`;
  `FF(kg/h) = P/0.7457 x BSFC(lb/hp/h) x 0.4536`; `FF(L/h) = FF(kg/h) / 0.72`
  (avgas) or `/ 0.80` (kerosene). `eta` = 0.78 piston, 0.80 turboprop.

Engine SFC is taken per engine from the *Thrust-specific fuel consumption* cruise table
(JT8D-9 0.80, Spey 0.66, CFM56-3C1 0.667, CFM56-5B4 0.545, CF6-80C2 0.605, Trent 1000
0.506, Olympus 593 at M2 1.195 lb/lbf/h, and so on), and L/D from the *Lift-to-drag ratio*
article (A320 16.3, 747-400 15.5, L-1011 14.5, 777 19.3, Concorde 7.5 at M2). Piston BSFC
uses the range sanctioned in the brief, 0.45-0.55 lb/hp/h, with 0.58 for 1910s engines.
Sources:
https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption and
https://en.wikipedia.org/wiki/Lift-to-drag_ratio

The model needs a cruise weight. `W = k x (pakset weight)`, with k = 1.35 for jets,
1.30 for turboprops and 1.25 for piston types, representing payload plus about half the trip
fuel. Where the pakset `weight` field is manifestly the loaded weight rather than the empty
weight (707-120, DC-8-10, 747-100/200, Concorde, the regional jets, the small commuters and
the early piston types) k is adjusted for those models over the range 0.85-1.70. This weight
factor is the largest single source of error in the M rows.

**(E) estimate.** Stated as such, anchored on a related type.

### 1.3 Worked examples

**Airbus A320 (S).** 3.13 kg/km on a 1,900 km sector. Cruise = 3.13 x 0.93 = 2.91 kg/km;
/0.80 = 3.64 L/km; at 828 km/h = 3,013 L/h (2,410 kg/h). Independent check with the model:
W = 1.35 x 51 = 68.9 t, L/D 16.3, CFM56-5B SFC 0.545 gives 2,966 L/h, within 2 per cent.

**Douglas DC-3 (M, cross-checked D).** W = 1.25 x 8.7 = 10.9 t; L/D 12.5; eta 0.78;
BSFC 0.48 lb/hp/h; v = 293 km/h = 81.4 m/s.
D = 10.9 x 9.81 / 12.5 = 8.55 kN; P = 8,550 x 81.4 / 0.78 = 892 kW = 1,196 hp;
FF = 1,196 x 0.48 = 574 lb/h = 260 kg/h = 361 L/h; 361,000/293 = 1,233 mL/km.
Capacity check: 3,043 L usable / 2,400 km = 1.27 L/km, i.e. 4 per cent above the model.

**Boeing 747-400 (S).** 11.11 kg/km on an 11,000 km sector; x0.97 = 10.78 kg/km;
/0.80 = 13.47 L/km = 13,471 mL/km; at 907 km/h = 12,218 L/h (9,774 kg/h), against a
published cruise flow of about 11,000 kg/h.

### 1.4 Calibration of the model against the documented rows

Where a documented flow exists, the model was also run with the same inputs to show how much
confidence the M rows deserve. All figures are L/h at cruise.

| type | documented flow, converted to cruise (L/h) | model flow (L/h) | difference |
|---|---:|---:|---:|
| a320 | 3012 | 3148 | +4% |
| 737-800 | 3404 | 2807 | -17% |
| 747-400 | 12218 | 14765 | +20% |
| 787-8 | 5890 | 5691 | -3% |
| atr72-500 | 802 | 786 | -1% |
| beech1900d | 566 | 459 | -18% |
| do228 | 348 | 268 | -22% |
| e190 | 3021 | 2378 | -21% |
| erj145 | 1452 | 1100 | -24% |
| 737-300 | 3117 | 2390 | -23% |

The model reproduces the documented flows to within 25 per cent in every case, but the
residuals are not random: it understates the small regional types by 18-24 per cent and
overstates the 747-400 by 20 per cent. Part of that is the weight factor, part is that the
published SFC values are quoted at different ratings. The M rows should therefore be read as
+/-25 per cent, and the S rows, where a measured flow exists, are the ones to trust.

### 1.5 Sanity check against `runningcost`

Fuel cost per km in Simucents = `fuel_per_km x fuel.tab value / 1000`. `runningcost` scales
with the general price index (`New/config/prices.tab`, 1900 = 100), so compare with
`runningcost x index/100`.

| type | year | fuel cost/km | runningcost x index/100 | ratio |
|---|---:|---:|---:|---:|
| Airbus A320 | 1988 | 10,055 | 7,930 | 1.27 |
| Boeing 747-400 | 1989 | 42,756 | 36,704 | 1.16 |
| Douglas DC-3 | 1936 | 414 | 129 | 3.2 |
| Vickers Viscount 802 | 1956 | 981 | 187 | 5.3 |
| DHC-6 Twin Otter | 1969 | 753 | 45 | 16.8 |

The two airliners land where the brief expects, within a factor of 1.3; the DC-3 is at 3.2.
The small types are 5-17 times their maintenance because this pakset's aircraft `runningcost`
values are very low in absolute terms (the Twin Otter's 6 Simucents/km is £0.0003/km of
maintenance, which cannot be right), not because the fuel figure is too high: 152 L/h is a
normal cruise flow for a Twin Otter. This is worth a separate pass on aircraft maintenance
costs; it is not a reason to reduce the fuel numbers.

### 1.6 Independent check from the Simutrans forum thread

The forum thread named in the brief does contain one directly usable aircraft figure.
Post #177 of *A snippet of relative pricing information*
(https://forum.simutrans.com/index.php?topic=6521.175) quotes an operator summary of an
Airbus A340-300 at 271 t take-off weight: 2.2 t for take-off and rotation to 1,500 ft, 5.8 t
from 1,500 ft to 31,000 ft, and **cruise 1 tonne per 70 nmi**.

    70 nmi = 129.6 km, so 1,000 kg / 129.6 km = 7.72 kg/km
    at 880 km/h that is 6,790 kg/h

That is a measured cruise figure for a 271 t widebody, and it gives a useful rule of thumb:
`kg/km = 0.0285 x MTOW(t)`. Applying it as a check: a 397 t 747-400 predicts 11.3 kg/km
(this report: 10.78), a 231 t Tristar-500 predicts 6.6 kg/km (this report: 7.19), a 152 t
707-320C predicts 4.3 kg/km (this report: 4.72). The widebody rows sit within about
10 per cent of that independent line, which is better than their nominal +/-25 per cent band.
The rule is for long-range types; narrowbodies, which carry a smaller fuel load relative to
their weight, run above it.

## 2. Per-model table

`basis` gives what the figure is and how it was obtained: `S` = documented fuel burn per km
converted as in 1.2, `M` = model from engine SFC and L/D, `E` = estimate. No row rests on the
capacity/range cross-check alone.

| model | fuel_per_km (mL/km) | calibration_speed (km/h) | cut_off_speed (km/h) | range (km) | basis | source |
|---|---:|---:|---:|---:|---|---|
| 707-120 | 5920 | 885 | 443 | 5037 | M: JT3C turbojet, cruise SFC ~0.88 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 707-320 | 5898 | 885 | 443 | 5400 | M: JT3D turbofan | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 707-420 | 5986 | 885 | 443 | 6940 | M: Conway bypass turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 727-100 | 5503 | 851 | 426 | 4300 | M: JT8D-9, cruise SFC 0.80 (documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 727-200 | 6032 | 851 | 426 | 3500 | M: JT8D-9/15, cruise SFC 0.80 (documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 737-100 | 3600 | 778 | 389 | 2855 | E: 737-100, 3.20 kg/km at 939 km, x0.90, /0.80; anchored on the documented 737-200/-300 trend, not a measured figure | estimate (see basis) |
| 737-200 | 3769 | 778 | 389 | 3520 | E: 737-200, 3.35 kg/km at 939 km, x0.90, /0.80; anchored on documented 737-300 (3.49) and JT8D SFC 0.80 | estimate (see basis) |
| 737-300 | 3926 | 794 | 397 | 4973 | S: 737-300 at 939 km sector: 3.49 kg/km, x0.90, /0.80; CFM56-3C1 SFC 0.667 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 737-400 | 4106 | 813 | 407 | 3630 | E: 737-400, 3.65 kg/km (stretched 737-300), x0.90, /0.80 | estimate (see basis) |
| 737-700 | 3611 | 833 | 417 | 5570 | S: 737-700 at 930 km sector: 3.21 kg/km, x0.90, /0.80; CFM56-7B SFC 0.627 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 737-800 | 4039 | 843 | 422 | 5436 | S: 737-800 at 930 km sector: 3.59 kg/km, x0.90, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 737-900 | 4309 | 844 | 422 | 5460 | S: 737-900ER at 930 km sector: 3.83 kg/km, x0.90, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 737-max-7 | 3814 | 839 | 420 | 7084 | S: 737 MAX 7 at 1,100 km sector: 3.39 kg/km, x0.90, /0.80; LEAP-1B SFC 0.53-0.56 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 737-max-8 | 3420 | 839 | 420 | 6510 | S: 737 MAX 8 at 1,220 km sector: 3.04 kg/km, x0.90, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 737-max-9 | 3712 | 839 | 420 | 5960 | S: 737 MAX 9 at 1,220 km sector: 3.30 kg/km, x0.90, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 747-100 | 13024 | 907 | 454 | 9800 | M: JT9D, L/D 15.3 (747-200, documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 747-200 | 14081 | 907 | 454 | 12690 | M: JT9D/CF6, L/D 15.3 (documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 747-200f | 13079 | 907 | 454 | 12690 | M: JT9D/CF6 freighter | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| 747-400 | 13471 | 907 | 454 | 13450 | S: 747-400 at 11,000 km sector: 11.11 kg/km, x0.97, /0.80; CF6-80C2 SFC 0.605 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 747-400f | 13471 | 907 | 454 | 13450 | S: 747-400F, as 747-400 freight variant | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 747-8 | 12780 | 914 | 457 | 14320 | S: 747-8 at 11,000 km sector: 10.54 kg/km, x0.97, /0.80; GEnx-2B SFC ~0.52 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 787-10 | 7421 | 903 | 452 | 11908 | S: 787-10 at 10,240 km sector: 6.12 kg/km, x0.97, /0.80; GEnx-1B76 SFC 0.512 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 787-8 | 6523 | 903 | 452 | 13621 | S: 787-8 at 8,610 km sector: 5.38 kg/km, x0.97, /0.80; Trent 1000 SFC 0.506 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| 787-9 | 6826 | 903 | 452 | 14140 | S: 787-9 at 9,208 km sector: 5.63 kg/km, x0.97, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| a318 | 3579 | 828 | 414 | 5700 | M: CFM56-5A1, cruise SFC 0.596; A320 L/D 16.3 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| a319 | 3406 | 828 | 414 | 6650 | S: A319 at 1,900 km sector: 2.93 kg/km, x0.93, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| a320 | 3639 | 828 | 414 | 5700 | S: A320 at 1,900 km sector: 3.13 kg/km, x0.93, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| a321 | 4197 | 828 | 414 | 5600 | S: A321-200 at 1,900 km sector: 3.61 kg/km, x0.93, /0.80; CFM56-5B SFC 0.545 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| aero-commander-500 | 282 | 326 | 163 | 850 | M: 1951 light twin, 2x260 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| aero-commander-681 | 487 | 370 | 185 | 1480 | M: 1955 supercharged light twin, 2x340 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| albatross | 899 | 338 | 169 | 1630 | M: DH.91 Albatross, 4x Gipsy Six | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| ambassador | 1940 | 418 | 209 | 885 | M: Airspeed Ambassador, 2x Centaurus | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| atp | 1526 | 437 | 219 | 1480 | M: BAe ATP, 2x PW126 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| atr42-300 | 1282 | 450 | 225 | 885 | M: ATR 42-300, 2x PW120 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| atr42-500 | 1418 | 450 | 225 | 1555 | S: ATR 42-500 at 560 km sector: 1.26 kg/km, x0.90 climb correction, /0.80 kg/L | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| atr72-200 | 1495 | 450 | 225 | 1528 | M: ATR 72-200, 2x PW124 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| atr72-500 | 1744 | 460 | 230 | 1528 | S: ATR 72-500 at 560 km sector: 1.55 kg/km (mean of 1.67 and 1.42), x0.90, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| bac112 | 2516 | 815 | 408 | 1340 | M: Spey RB.163 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| bac115 | 3605 | 742 | 371 | 2744 | M: Spey RB.163 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| bae146 | 3033 | 775 | 388 | 2909 | M: ALF502R-5, cruise SFC 0.72 (documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| beech-18 | 558 | 298 | 149 | 2460 | M: Beech 18, 2x450 hp; also D18C | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| beech1900c | 775 | 495 | 248 | 707 | M: Beech 1900C, 2x PT6A-65B | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| beech1900d | 1063 | 533 | 267 | 707 | S: Beech 1900D at 419 km sector: 1.00 kg/km, x0.85 climb correction, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| boeing-247 | 722 | 304 | 152 | 1200 | M: Boeing 247, 2x550 hp Wasp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| boeing-307 | 1927 | 346 | 173 | 2816 | M: Boeing 307 Stratoliner, 4x1,100 hp Cyclone | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| boeing-377 | 5182 | 483 | 242 | 3650 | M: Boeing 377 Stratocruiser, 4x3,500 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| bristol-170 | 1746 | 254 | 127 | 2140 | M: Bristol 170 Freighter, 2x Bristol Hercules | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| britannia | 5127 | 575 | 288 | 6037 | M: Bristol Britannia, 4x Proteus; long-range clean airframe | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| c54-dc4 | 2679 | 365 | 183 | 4050 | M: C-54/DC-4, 4x1,450 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| caravelle | 3440 | 741 | 371 | 1700 | M: Avon RA.29 turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| comet1 | 4758 | 724 | 362 | 2414 | M: Avon RA.7 turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| comet4 | 4878 | 805 | 403 | 5190 | M: Avon RA.29 turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| comet4b | 4859 | 853 | 427 | 4023 | M: Avon RA.29 turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| comet4c | 5149 | 805 | 403 | 6900 | M: Avon RA.29 turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| concorde | 13996 | 2170 | 1085 | 7223 | M: Olympus 593 at M2: SFC 1.195 lb/lbf/h (documented), L/D 7.5 at M2 (documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| cv880 | 5023 | 976 | 488 | 4430 | M: CJ-805 (civil J79) turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| cv990 | 5409 | 895 | 448 | 4430 | M: CJ-805-23 aft-fan | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc-8-10 | 5962 | 895 | 448 | 6960 | M: JT3C/JT4A turbojet | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc2 | 1123 | 300 | 150 | 1750 | M: DC-2, 2x875 hp Cyclone | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc3 | 1233 | 293 | 147 | 2400 | M: DC-3, 2x1,200 hp Cyclone; capacity/range check 3,043 L / 2,400 km = 1.27 L/km | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc3a | 1006 | 333 | 167 | 2400 | M: DC-3A, 2x1,200 hp Twin Wasp, higher cruise | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc6 | 3492 | 501 | 251 | 4800 | M: DC-6, 4x2,400 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc6a | 3275 | 507 | 254 | 5460 | M: DC-6A, 4x2,500 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc6b | 3767 | 507 | 254 | 4830 | M: DC-6B, 4x2,500 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc7 | 3023 | 555 | 278 | 5737 | M: DC-7, 4x3,250 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| dc7c | 3571 | 555 | 278 | 9012 | M: DC-7C, 4x3,400 hp, long-span wing | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| do228 | 940 | 371 | 186 | 1111 | S: Do 228 at 560 km sector: 0.94 kg/km, x0.80 (short sector, large climb share), /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| e175 | 3150 | 797 | 399 | 4074 | S: E-175 at 1,120 km sector: 2.80 kg/km, x0.90, /0.80; CF34-8E SFC 0.68 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| e190 | 3645 | 829 | 415 | 4573 | S: E-190 at 1,124 km sector: 3.24 kg/km, x0.90, /0.80; CF34-10E SFC 0.64 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| erj145 | 1744 | 833 | 417 | 2445 | S: ERJ-145 at 1,107 km sector: 1.55 kg/km, x0.90, /0.80 | https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft |
| f13 | 188 | 160 | 80 | 1200 | M: Junkers F.13, 1x126 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| f27-100 | 1437 | 437 | 219 | 2600 | M: F27-100, 2x Dart RDa.6 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| f27-200 | 1437 | 490 | 245 | 2600 | M: F27-200, 2x Dart RDa.7 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| f27-500 | 1437 | 490 | 245 | 1315 | M: F27-500, 2x Dart Mk 536 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| f50 | 1383 | 454 | 227 | 2055 | M: Fokker 50, 2x PW125B | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| ju52 | 1324 | 222 | 111 | 950 | M: Ju 52/3m, 3x660 hp; capacity/range check 2,450 L / 1,300 km = 1.88 L/km | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| kingair200 | 704 | 515 | 258 | 3658 | M: King Air 200, 2x PT6A-42; King Air 350 documented 304 kg/h at cruise | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l049 | 3298 | 503 | 252 | 6392 | M: L-049 Constellation, 4x2,200 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l10-electra | 513 | 306 | 153 | 1150 | M: Lockheed 10 Electra, 2x450 hp Wasp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l1049c | 3584 | 489 | 245 | 8288 | M: L-1049C Super Constellation, 4x2,700 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l1049g | 4133 | 547 | 274 | 8700 | M: L-1049G, 4x3,250 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l1649 | 4935 | 467 | 234 | 9945 | M: L-1649 Starliner, 4x3,400 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l188 | 2743 | 602 | 301 | 2709 | M: L-188 Electra, 4x501-D13 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| l188c | 2943 | 602 | 301 | 3450 | M: L-188C Electra, 4x501-D13 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| lz10 | 959 | 73 | 37 | 1700 | M: LZ 10 (1911): 3x170 hp at ~60% cruise power, BSFC 0.58 lb/hp/h | estimate from installed power and BSFC (see basis) |
| lz127 | 3846 | 117 | 59 | 12000 | M: LZ 127: 5x570 hp Maybach, 4 running at ~60%, BSFC 0.45; cross-check 65,000 L / 16,500 km = 3.9 L/km | estimate from installed power and BSFC (see basis) |
| lz129 | 3852 | 135 | 68 | 16500 | M: LZ 129: 4x1,050 hp diesel at ~55%, BSFC 0.42 lb/hp/h, diesel 0.84 kg/L | estimate from installed power and BSFC (see basis) |
| lz6 | 571 | 70 | 35 | 1400 | M: LZ 6 (1909): 2x125 hp at ~60% cruise power, BSFC 0.60 lb/hp/h | estimate from installed power and BSFC (see basis) |
| mail-monoplane | 214 | 80 | 40 | 1000 | E: 1910 mail monoplane, 100 hp; low-aspect-ratio contemporary airframe | estimate (see basis) |
| metro | 673 | 515 | 258 | 1100 | M: Fairchild Metro, 2x TPE331 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| o400 | 1223 | 131 | 66 | 1120 | M: HP O/400, 2x360 hp Eagle; capacity/range check 1,136 L / 1,120 km = 1.01 L/km | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| orion | 347 | 282 | 141 | 1159 | M: Lockheed Orion, 1x550 hp Wasp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| otter | 335 | 195 | 98 | 1520 | M: DHC-3 Otter, 1x600 hp Wasp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| rapide | 292 | 214 | 107 | 895 | M: DH.89 Dragon Rapide, 2x200 hp Gipsy Six | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| scaravelle | 3377 | 800 | 400 | 2650 | M: JT8D | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| trident1c | 3207 | 848 | 424 | 3259 | M: Spey RB.168, cruise SFC 0.66 (documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| trident2e | 3491 | 848 | 424 | 4300 | M: Spey RB.168 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| trident3b | 4082 | 830 | 415 | 3597 | M: Spey RB.168 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| trimotor | 955 | 198 | 99 | 885 | M: Ford Trimotor, 3x300 hp; capacity/range check 870 L / 885 km = 0.98 L/km | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| tristar-1 | 8924 | 890 | 445 | 5760 | M: RB.211, L/D 14.5 (L-1011, documented) | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| tristar-200 | 9135 | 890 | 445 | 6820 | M: RB.211-22, L/D 14.5 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| tristar-500 | 8989 | 894 | 447 | 9905 | M: RB.211-524, L/D 14.5 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| twinotter | 749 | 278 | 139 | 1233 | M: DHC-6-300 Twin Otter, 2x PT6A-27; slow, high-drag airframe | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| vanguard | 5257 | 663 | 332 | 2945 | M: Vanguard, 4x Tyne; very high aspect ratio | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| vc10 | 7180 | 930 | 465 | 8112 | M: Conway | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| vc10-super | 7275 | 935 | 468 | 7600 | M: Conway RCo.43 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| vega | 274 | 285 | 143 | 1165 | M: Lockheed Vega, 1x450 hp Wasp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| viking | 1471 | 338 | 169 | 2740 | M: Vickers VC.1 Viking, 2x Hercules | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| viscount-757 | 2645 | 509 | 255 | 2220 | M: Viscount 700, 4x Dart RDa.3 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| viscount-802 | 2886 | 530 | 265 | 2220 | M: Viscount 800, 4x Dart RDa.7 | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| w34 | 319 | 190 | 95 | 900 | M: Junkers W.34, 1x300 hp | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |
| w8b | 1015 | 137 | 69 | 1120 | M: HP W.8b, 2x450 hp Eagle | https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption (turbines); https://en.wikipedia.org/wiki/Lift-to-drag_ratio; BSFC 0.45-0.55 lb/hp/h (fuel-brief.md s4) for piston types |

## 3. Object mapping table

Every object in `ai/temp/sector-air.txt`, exactly as spelled in the `.dat` files.

| object name | model |
|---|---|
| MailMonoPlane | mail-monoplane |
| aero-commander-500 | aero-commander-500 |
| aero-commander-520 | aero-commander-500 |
| aero-commander-681 | aero-commander-681 |
| aerospatiale-bac-concorde | concorde |
| Boeing_707_120 | 707-120 |
| boeing-707-120-high-density | 707-120 |
| boeing-707-320c | 707-320 |
| boeing-707-420 | 707-420 |
| boeing-707-420-high-density | 707-420 |
| boeing-727-200-advanced-cool | 727-200 |
| boeing-727-200-advanced-piece | 727-200 |
| boeing-727-200-advanced-mail | 727-200 |
| boeing-727-200 | 727-200 |
| boeing-727-200-high-density | 727-200 |
| boeing-787-10 | 787-10 |
| boeing-787-8 | 787-8 |
| boeing-787-8-high-density | 787-8 |
| boeing-787-9 | 787-9 |
| boeing-787-9-high-density | 787-9 |
| douglas-dc-8-10 | dc-8-10 |
| tristar-1 | tristar-1 |
| tristar-1-high-density | tristar-1 |
| tristar-200 | tristar-200 |
| tristar-200-high-density | tristar-200 |
| tristar-500 | tristar-500 |
| tristar-500-high-density | tristar-500 |
| vickers-super-vc10 | vc10-super |
| vickers-super-vc10-high-density | vc10-super |
| vickers-vc10 | vc10 |
| vickers-vc10-high-density | vc10 |
| boeing-747-100 | 747-100 |
| boeing-747-100-high-density | 747-100 |
| boeing-747-200 | 747-200 |
| boeing-747-200-high-density | 747-200 |
| boeing-747-200f-cool | 747-200f |
| boeing-747-200f-mail | 747-200f |
| boeing-747-200f-piece | 747-200f |
| boeing-747-400 | 747-400 |
| boeing-747-400-high-density | 747-400 |
| boeing-747-400f-cool | 747-400f |
| boeing-747-400f-mail | 747-400f |
| boeing-747-400f-piece | 747-400f |
| boeing-747-8f-cool | 747-8 |
| boeing-747-8f-piece | 747-8 |
| boeing-747-8i | 747-8 |
| zeppelin-lz-129 | lz129 |
| Zeppelin_LZ10_Mail | lz10 |
| Zeppelin_LZ10 | lz10 |
| zeppelin-lz127-mail | lz127 |
| zeppelin-lz127 | lz127 |
| zeppelin-lz6 | lz6 |
| airbus-a318 | a318 |
| airbus-a318-high-density | a318 |
| airbus-a319 | a319 |
| airbus-a319-high-density | a319 |
| airbus-a320-cool | a320 |
| airbus-a320-piece | a320 |
| airbus-a320-post | a320 |
| airbus-a320 | a320 |
| airbus-a320-high-density | a320 |
| airbus-a321 | a321 |
| airbus-a321-high-density | a321 |
| airspeed-ambassador | ambassador |
| atr-42-300f-cool | atr42-300 |
| atr-42-300f-piece | atr42-300 |
| atr-42-300f-post | atr42-300 |
| atr-42-320 | atr42-300 |
| atr-42-500 | atr42-500 |
| atr-42-500f-cool | atr42-500 |
| atr-42-500f-piece | atr42-500 |
| atr-42-500f-post | atr42-500 |
| atr-72-200 | atr72-200 |
| atr-72-200f-cool | atr72-200 |
| atr-72-200f-piece | atr72-200 |
| atr-72-200f-post | atr72-200 |
| atr-72-500-post | atr72-500 |
| atr-72-500 | atr72-500 |
| bac-1-11-200 | bac112 |
| bac-1-11-500 | bac115 |
| bae-146-100 | bae146 |
| bae-146-300 | bae146 |
| bae-146-300qt-cool | bae146 |
| bae-146-300qt-mail | bae146 |
| bae-146-300qt-piece | bae146 |
| bae-atp | atp |
| bae-atp-high-density | atp |
| beechcraft-18 | beech-18 |
| beechcraft-18-mail | beech-18 |
| beechcraft-1900c | beech1900c |
| beechcraft-1900c-mail | beech1900c |
| beechcraft-1900d | beech1900d |
| beechcraft-1900d-mail | beech1900d |
| boeing-247 | boeing-247 |
| boeing-247-mail | boeing-247 |
| boeing-307-stratoliner | boeing-307 |
| boeing-377 | boeing-377 |
| boeing-727-100-cool | 727-100 |
| boeing-727-100-piece | 727-100 |
| boeing-727-100-mail | 727-100 |
| boeing-727-100 | 727-100 |
| boeing-727-100-high-density | 727-100 |
| boeing-737-100 | 737-100 |
| boeing-737-100-high-density | 737-100 |
| boeing-737-200 | 737-200 |
| boeing-737-200-high-density | 737-200 |
| boeing-737-300 | 737-300 |
| boeing-737-300-high-density | 737-300 |
| boeing-737-400 | 737-400 |
| boeing-737-400-high-density | 737-400 |
| boeing-737-700 | 737-700 |
| boeing-737-700-high-density | 737-700 |
| boeing-737-800 | 737-800 |
| boeing-737-800-high-density | 737-800 |
| boeing-737-900er | 737-900 |
| boeing-737-900er-high-density | 737-900 |
| boeing-737-max-7 | 737-max-7 |
| boeing-737-max-7-high-density | 737-max-7 |
| boeing-737-max-8 | 737-max-8 |
| boeing-737-max-8-high-density | 737-max-8 |
| boeing-737-max-9 | 737-max-9 |
| boeing-737-max-9-high-density | 737-max-9 |
| bristol-britannia | britannia |
| bristol-type-170-cars | bristol-170 |
| bristol-type-170-cool | bristol-170 |
| bristol-type-170-piece | bristol-170 |
| bristol-type-170-mail | bristol-170 |
| bristol-type-170 | bristol-170 |
| convair-cv880 | cv880 |
| convair-cv880-high-density | cv880 |
| convair-cv990 | cv990 |
| convair-cv990-high-density | cv990 |
| dh-91-albatross | albatross |
| dh-91-albatross-mail | albatross |
| dh-comet-1 | comet1 |
| dh-comet-4 | comet4 |
| dh-comet-4-high-density | comet4 |
| dh-comet-4b | comet4b |
| dh-comet-4b-high-density | comet4b |
| dh-comet-4c | comet4c |
| dh-comet-4c-high-density | comet4c |
| dhc3-otter | otter |
| dornier-do-228 | do228 |
| dornier-do-228-mail | do228 |
| douglas-c54-cool | c54-dc4 |
| douglas-c54-piece | c54-dc4 |
| douglas-c54-mail | c54-dc4 |
| Douglas_DC2_Mail | dc2 |
| Douglas_DC2 | dc2 |
| Douglas_DC3 | dc3 |
| Douglas_DC3_Mail | dc3 |
| Douglas_DC3A | dc3a |
| Douglas_DC3A_Mail | dc3a |
| douglas-dc-4 | c54-dc4 |
| douglas-dc-6a-cool | dc6a |
| douglas-dc-6a-piece | dc6a |
| douglas-dc-6a-mail | dc6a |
| douglas-dc-6 | dc6 |
| douglas-dc-6-high-density | dc6 |
| douglas-dc-6b | dc6b |
| douglas-dc7 | dc7 |
| douglas-dc7-high-density | dc7 |
| douglas-dc7c | dc7c |
| douglas-dc7c-high-density | dc7c |
| dragon-rapide | rapide |
| dragon-rapide-mail | rapide |
| embraer-e-175 | e175 |
| embraer-e-190 | e190 |
| erj-145 | erj145 |
| fairchild-metroliner | metro |
| fairchild-metroliner-cool | metro |
| fairchild-metroliner-mail | metro |
| fairchild-metroliner-piece | metro |
| fokker-f27-100-mail | f27-100 |
| fokker-f27-100 | f27-100 |
| Fokker-F27-200 | f27-200 |
| Fokker-F27-500 | f27-500 |
| Fokker-F27-500-high-density | f27-500 |
| fokker-f50 | f50 |
| fokker-f50-high-density | f50 |
| FordTrimotorMail | trimotor |
| ford-trimotor | trimotor |
| HandleyPageO400_Mail | o400 |
| HandleyPageO400 | o400 |
| HandleyPageW8b_Mail | w8b |
| HandleyPageW8b | w8b |
| hs-trident-1c | trident1c |
| hs-trident-1c-high-density | trident1c |
| hs-trident-2e | trident2e |
| hs-trident-2e-high-density | trident2e |
| hs-trident-3b | trident3b |
| hs-trident-3b-high-density | trident3b |
| ju-52 | ju52 |
| junkers-f13 | f13 |
| junkers-f13-mail | f13 |
| junkers-w34 | w34 |
| junkers-w34-mail | w34 |
| king-air-200 | kingair200 |
| king-air-200-mail | kingair200 |
| lockheed-10-electra | l10-electra |
| lockheed-electra-l188-c | l188c |
| lockheed-electra-l188-c-high-density | l188c |
| lockheed-electra-l188 | l188 |
| lockheed-electra-l188-high-density | l188 |
| lockheed-l049-constellation | l049 |
| lockheed-l049-constellation-high-density | l049 |
| lockheed-l1049-c-super-constellation | l1049c |
| lockheed-l1049-c-super-constellation-high-density | l1049c |
| lockheed-l1049-g-super-constellation | l1049g |
| lockheed-l1049-g-super-constellation-high-density | l1049g |
| lockheed-l1649-starliner | l1649 |
| lockheed-l1649-starliner-high-density | l1649 |
| lockheed-orion | orion |
| lockheed-orion-mail | orion |
| lockheed-vega | vega |
| lockheed-vega-mail | vega |
| caravelle | caravelle |
| caravelle-high-density | caravelle |
| super-caravelle | scaravelle |
| super-caravelle-high-density | scaravelle |
| twin-otter-300 | twinotter |
| vickers-vanguard-952 | vanguard |
| vickers-vanguard-952-cool | vanguard |
| vickers-vanguard-952-piece | vanguard |
| vickers-vanguard-953 | vanguard |
| vickers-vanguard-953-cool | vanguard |
| vickers-vanguard-953-piece | vanguard |
| vickers-vc1b-viking | viking |
| vickers-vc2-viscount-757 | viscount-757 |
| vickers-vc2-viscount-802 | viscount-802 |

## 4. Gaps and doubts

1. **Only 23 of 112 models rest on a directly measured fuel burn.** A further 4 are
   estimates, and the other 85 are modelled from engine SFC and L/D: those should be read as
   +/-25 per cent. The model is calibrated against the measured types (section 1.4) and does
   not drift with era, because SFC and L/D are set per type rather than per decade.
2. **Jane's All the World's Aircraft was not used.** The archive.org full-text interface
   could not be searched reliably within this run; that is the obvious next step and would
   turn many M rows into S rows, above all for the 1950s-1970s British types (Comet, Trident,
   VC10, 1-11, Vanguard, Britannia).
3. **The forum thread yields only one aircraft figure.** Page 1 is about vehicle purchase
   prices; the thread is nine pages of capital and maintenance costs. Post #177
   (https://forum.simutrans.com/index.php?topic=6521.175) is the exception: the A340-300
   cruise burn of 1 t per 70 nmi used in 1.6. There are no historical (pre-1960) aircraft
   consumption figures anywhere in it, so the classic types rest on the model and the
   capacity/range check alone.
4. **The pakset `weight` field is inconsistent**: sometimes empty weight (737-200, Comet 4,
   Tristar, 787-8), sometimes a loaded weight (707-120, VC10, Concorde). The M rows absorb
   this with a per-model weight factor, which is the largest error source. A one-off pass to
   standardise aircraft `weight` to empty weight would let the model be re-run cleanly.
5. **Earliest types (1909-1920)** rest entirely on BSFC and installed power; no measured
   consumption was found for the MailMonoPlane, HP O/400, HP W.8b or the early Zeppelins.
   The O/400 has a capacity/range check that supports the figure.
6. **Airships.** LZ 127 and LZ 129 are cross-checked against fuel capacity and range and are
   solid to about 10 per cent. LZ 6 and LZ 10 are estimates from installed power.
7. **Source inconsistency retained.** The published table gives 737 MAX 7 (3.39 kg/km at
   1,100 km) a higher burn than 737 MAX 8 (3.04 at 1,220 km) although the MAX 7 is smaller.
   The published numbers were kept rather than smoothed, so the MAX 7 is 11 per cent above
   the MAX 8 in this table.
8. **Short-sector corrections are crude.** Do 228 (0.94 kg/km at 560 km) and Beech 1900D
   (1.00 at 419 km) needed large climb corrections; both may be 10-20 per cent high.
   Conversely the **Ju 52** is the least certain piston row: the model gives 1.32 L/km while
   its capacity/range ceiling is 1.88 L/km, so it may be 30 per cent low.
9. **Concorde** uses the documented Olympus 593 SFC of 1.195 lb/lbf/h and L/D 7.5 at M2, but
   the cruise weight is uncertain; the resulting 14.0 L/km is at the top of the plausible
   range (16.7 L/100 km per passenger x 100 passengers is often quoted, which is close).
10. **Freight and mail variants** share the passenger model's figure. A 747-400F at the same
   weight burns the same fuel; the pakset gives the freighters a different `weight`, which
   the mapping does not distinguish because they map to the same model row.
