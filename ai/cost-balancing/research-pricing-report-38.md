# Prices in vehicle `.dat` comments

Extraction run 23 November 2026. Source: the `#` comment lines of the `.dat` files in the ten
vehicle folders (`air`, `boats`, `bus`, `citycars`, `london-underground`, `maglev`, `narrowgauge`,
`trains`, `trams`, `livery-trains`). No `.dat` cost, `runningcost`, `fixed_cost`, `overhaul` or
`upgrade` value was read. `intro_year`, `name`, `freight` and `capacity` were read only where a
comment carried no year.

## Headline

| | |
|---|---|
| Distinct comment lines carrying a currency figure | 59 (56 with £ or GBP, 3 with US$) |
| Comment statements that state a purchase price | 48 |
| Prices parsed from them | **55** |
| New to the register | **43** |
| Already in the register | **12** |
| Comments rejected as running cost or wage | 4 |

Six of the price statements give two or three figures (seven extra prices in all: Bedford WTB,
BSA, Daimler, Class 378, DC-7C and Britannia), hence 55 prices from 48 statements.

**The scan file is a sample, not an inventory.** `ai/temp/dat-comments-vehicles.csv` holds 1,022
comment lines drawn from a much larger set: several files with prices have no rows at all
(`bus/aec-605.dat`, `bus/but-9611t.dat`, `bus/dennis-f.dat`, `bus/karrier-e4.dat`) and only one of
its 1,022 lines contains a currency symbol (`fr-hudson-toastrack`, £155 in 1923). It therefore
cannot serve as the comment inventory for this task. The sweep was run again over all 21,780
comment lines in the vehicle folders, and every line containing `£`, `GBP`, `US$` or a money word
was read in context. That produced the 59 lines above.

## Pre-decimal conversion used

| Stated | Converted |
|---|---|
| £1,811-8-4 | 1,811.417 (recorded in the register as 1,811.42) |
| £1,859-10-9 | 1,859.5375 → 1,859.54 |
| £1,325/10s | 1,325.50 |

Ranges are recorded at the midpoint and marked as such. Nothing is deflated or converted between
currencies; US dollar prices stay in dollars.

## Every parsed price

"Register" says whether the same object, year and value is already in
`New/ai/cost-balancing/individual-price-rows.csv`.

### Bus and trolleybus (road-vehicle)

| Object | File | Year | Price | Scope | Source cited in comment | Register |
|---|---|---|---|---|---|---|
| AEC 605 trolleybus | bus/aec-605.dat | 1927* | 1,445 | complete | none (.dat comment) | new |
| AEC 661T trolleybus, Portsmouth-style 50-seat body | bus/aec-661t-2.dat | 1934 | 1,811.42 | complete | none (.dat comment); British Trolleybus Database implied | duplicate |
| Bedford OB bus | bus/bedford-ob.dat | — | 1,325.50 | complete | Graces Guide, Bedford OB | new |
| Bedford WTB complete vehicle | bus/bedford-wtb.dat | 1935* | 785 | complete | none (book not named) | new |
| Bedford WTB chassis | bus/bedford-wtb.dat | 1935* | 290 | chassis only | none (book not named) | new |
| BUT 9611T trolleybus | bus/but-9611t.dat | 1949 | 5,309 | complete | none (.dat comment) | duplicate |
| Dennis 15 cwt omnibus | bus/dennis-15cwt-omnibus.dat | 1904* | 715 + lettering | complete | Baldwin pp. 8-9 | duplicate (probable) |
| Dennis 30 cwt van chassis | bus/dennis-30cwt-van.dat | 1922 | 550 | chassis only | Motor Trader 6 Mar 1922, via Graces Guide | new |
| Dennis Dominator trolleybus | bus/dennis-dominator-trolley.dat | 1977* | 100,000 | complete | Trolleybus Database CD-ROM | new |
| Dennis F chassis | bus/dennis-f.dat | 1929 | 885 | chassis only | Baldwin p. 36 | duplicate (register says 1927) |
| EE E11 trolleybus (Nottingham Corporation) | bus/ee-e11.dat | 1929 | 2,098 | complete | none (Nottingham Corp.) | new |
| Guy BT trolleybus to Reading | bus/guy-bt-56.dat | 1936 | 2,170 | complete | none (.dat comment) | duplicate |
| Karrier E4 trolleybus | bus/karrier-e4.dat | 1934 | 1,859.54 | complete | none (.dat comment) | duplicate |
| Leyland TB4 trolleybus | bus/leyland-tb4.dat | 1936 | 2,117 | complete | none (.dat comment) | duplicate |
| Leyland Titan TD3 to TD4 diesel conversion | bus/leyland-titan-td3.dat and -td4.dat | — | 450 | conversion | Phillips p. 48 | new |
| Ret Hurst Nelson electric bus | bus/ret-hurst-nelson.dat | 1911 | 725 | complete | none (.dat comment) | new |
| Volvo Alisa double-decker | bus/volvo-alisa.dat | 1972 | 25,000 | complete | none (.dat comment) | duplicate |

### Private cars and motorcycle (road-vehicle)

| Object | File | Year | Price | Scope | Source cited in comment | Register |
|---|---|---|---|---|---|---|
| BSA Model H 557 cc with BSA Type 1 sidecar | citycars/bsa-557-combo.dat | 1923 | 95 | complete outfit | BSA 1923 list via cybermotorcycle.com | new |
| BSA Model H 557 cc, solo | citycars/bsa-557-combo.dat | 1923 | 75 | solo machine | BSA 1923 list via cybermotorcycle.com | new |
| Daimler TE30 chassis | citycars/daimler-te30.dat | 1913 | 650 | chassis only | Jaguar Daimler Heritage Trust; Wikipedia | new |
| Daimler TE30 standard body | citycars/daimler-te30.dat | 1913 | 848 | body only | as above | new |
| Daimler TE30 Cranmore landaulette | citycars/daimler-te30.dat | 1913 | 1,100 | complete | Jaguar Daimler Heritage Trust | new |
| Humberette 8 hp cyclecar | citycars/humberette.dat | 1913 | 120 | complete | none (.dat comment) | new |
| Peugeot Type 69 Bebe | citycars/peugeot-type-69-bebe.dat | 1906 | 200 (under) | complete | 1906 price lists via Wikipedia | new |
| Standard 9.5 hp | citycars/standard-9-5.dat | 1913 | 185 | complete | none (.dat comment) | new |
| Toyota Corolla E100 1.6 Executive Liftback | citycars/toyota-corolla-e100.dat | 1992 | 13,210 | complete | period road test | new |
| Toyota Prius XW10 | citycars/toyota-prius-xw10.dat | 2000 | 16,495 | complete | Toyota launch material | new |
| Toyota Prius XW20 T3 | citycars/toyota-prius-xw20.dat | 2004 | 17,495 | complete | Toyota GB launch pack 2003 | new |
| Toyota Prius XW30 T3 | citycars/toyota-prius-xw30.dat | 2009 | 18,370 | complete | Toyota GB launch pack 2009 | new |
| Toyota Prius XW50 Active | citycars/toyota-prius-xw50.dat | 2015 | 23,295 | complete | Toyota GB range announcement | new |
| Toyota Prius XW60 Design | citycars/toyota-prius-xw60.dat | 2024 | 37,315 | complete | Toyota GB pricing | new |
| Toyota Yaris XP10 entry | citycars/toyota-yaris-xp10.dat | 1999 | 7,495 | complete | Toyota GB press material | new |
| Toyota Yaris XP90 1.0 VVT-i T2 | citycars/toyota-yaris-xp90.dat | 2006 | 8,995 | complete | Toyota GB launch pack | new |
| Toyota Yaris XP130 T2 | citycars/toyota-yaris-xp130.dat | 2011 | 11,170 | complete | Toyota GB launch pack 2011 | new |
| Toyota Yaris XP210 Icon | citycars/toyota-yaris-xp210.dat | 2020 | 19,910 | complete | Toyota GB launch release | new |

### Narrow gauge

| Object | File | Year | Price | Scope | Source cited in comment | Register |
|---|---|---|---|---|---|---|
| FR Hudson toastrack carriage | narrowgauge/fr-hudson-toastrack.dat | 1923 | 155 | complete | Festipedia | duplicate |

### Rail

| Object | File | Year | Price | Scope | Source cited in comment | Register |
|---|---|---|---|---|---|---|
| GNR Stirling 8 ft single | trains/gnr-stirling-8foot.dat | 1870 | 2,033 | complete | Ahrons p. 186 | duplicate |
| Sans Pareil | trains/sanspariel.dat | 1829 | 500 | complete | Ahrons p. 16 | new |
| SR West Country 4-6-2 rebuilt | trains/sr-wc-4-6-2-rebuilt.dat | 1954 | 5,428 | rebuild (overhaul) | semgonline.com | new |
| BR Class 378 fleet (152 cars) | trains/br-378.dat | — | 223,000,000 | class total | Wikipedia | new |
| BR Class 378 additional 36 carriages | trains/br-378.dat | 2010 | 36,000,000 | class total | Wikipedia | new |

### Tram

| Object | File | Year | Price | Scope | Source cited in comment | Register |
|---|---|---|---|---|---|---|
| Edinburgh Trams CAF Urbos 3 fleet (27 trams) | trams/caf-edinburgh.dat | — | 40,000,000 | class total | Wikipedia, Edinburgh Tram (vehicle) | new |
| West Midlands CAF Urbos 3, 20 trams | trams/caf-urbos-3.dat | 2012 | 40,000,000 | class total | Wikipedia, Midland Metro rolling stock | duplicate |
| Croydon Variobahn, 6 trams | trams/croydon-variobahn.dat | 2011 | 16,300,000 (2.7 each) | class total | none (.dat comment) | duplicate |

### Aircraft

| Object | File | Year | Price | Scope | Source cited in comment | Register |
|---|---|---|---|---|---|---|
| Bristol Britannia, range 700k–1.4m | air/bristol-britannia.dat | 1957 | 1,050,000 (midpoint) | complete | Wikipedia | new |
| Bristol Britannia (Flight figure) | air/bristol-britannia.dat | 1957 | 1,070,000 | complete | Flight magazine | new |
| de Havilland Comet 1 | air/dh-comet-1.dat | 1952 | 275,000 | complete | Wikipedia | new |
| de Havilland Comet 4 | air/dh-comet-4.dat | 1958* | 1,160,000 | complete | none (.dat comment) | new |
| Douglas DC-7 | air/douglas-dc-7.dat | 1954 | 570,000 | complete | none (.dat comment) | new |
| Douglas DC-7C | air/douglas-dc7c.dat | 1956 | 800,000 | complete | none (.dat comment) | new |
| Douglas DC-7C | air/douglas-dc7c.dat | 1958 | 930,000 | complete | none (.dat comment) | new |
| Vickers Vanguard 952 | air/vickers-vanguard-952.dat | 1960 | 1,000,000 | complete | none (.dat comment) | new |
| Boeing 377 Stratocruiser | air/boeing-377.dat | 1945 | 1,225,000 USD | complete | Wikipedia | new |
| Lockheed L-1649 Starliner | air/lockheed-l1649-starliner.dat | 1957* | 3,000,000 USD | complete | Wikipedia | new |
| Boeing 787-10 | air/air192/boeing-787-10.dat | 2015 | 306,000,000 USD | complete | Wikipedia | new |

`*` Year taken from the object's `intro_year` because the comment states none and the comment is
plainly about the object's own new price. This is flagged in the `notes` column of the CSV.

## Duplicates and conflicts with the register

Twelve prices repeat rows already in the register. Four of them differ in a name, a year or a
detail, and the register should be checked against the `.dat` comment:

| Object | Register | `.dat` comment |
|---|---|---|
| Dennis F chassis | 885, year 1927 | 885, "chassis only in 1929" |
| Guy BT trolleybus | "Guy BT-48", 1936, 2,170 | "£2,170 to Reading in 1936" (file is guy-bt-56) |
| Dennis 15 cwt Omnibus | "28hp motor bus", 1904, 715, Baldwin p.9 | "£715 + lettering", Baldwin pp. 8-9, intro 1904 — almost certainly the same datum |
| Croydon Variobahn | 2,716,667 per tram, 2011 | 16.3 million for 6, "2.7 a piece" — same underlying figure |

The West Midlands tram price (40 million for 20) matches the register's West Midlands Metro CAF
Urbos 3 row at 2,000,000 per tram. The Edinburgh comment (27 trams for 40 million, about 1.48
million each) does **not** match either Edinburgh row already in the register (2,000,000 and
2,396,074 per tram). It is carried as new and flagged.

## Comments rejected

| File | Comment | Reason |
|---|---|---|
| boats/mv-lochfyne.dat:18 | "Running cost £3-10-0 per day, half that of steam ships of the era" | Running cost per day, not a purchase price. |
| boats/skiff-wherry.dat:17 | "(£34/annum, assuming 8 hours/day 6 days/week)" | Annual wage used to calibrate `fixed_cost`. |
| bus/livestock_driver.dat:21 | "(£25/annum, assuming 10 hours/day 6 days/week)" | Annual wage, same. |
| bus/pack-horses.dat:24 | "(£25/annum, assuming 10 hours/day 6 days/week)" | Annual wage, same. |
| narrowgauge/hunslet-port.dat:24 | URL only | False positive; the line carries no money. |

Qualitative mentions with no figure were also excluded: "low running costs" (three Guy Arab
files), "cheaper to build and run" (two Super Sentinel files), "higher purchase but lower
running/overhaul cost" (three Mk 2 files), "These should be expensive to construct" (LBSCR
Gladstone), "costs adapted from BR Mk3 and Mk4" (Mk 5A).

Two sub-figures were absorbed rather than given their own rows: the £1,000 PowerShift grant in the
Prius XW20 comment (not a vehicle price) and the £910 Cranmore body price (the top of the body
range, already covered by the midpoint row).

## Which new prices would move a target if bound

Binding any of these needs a deflation step to the target year; nothing here has been deflated.
The points below compare the new prices with the existing register evidence, not with `.dat` values.

**Class totals must be divided first.** The Class 378 fleet (£223m for 152 cars), the 2010 batch
(£36m for 36 carriages) and the Edinburgh order (£40m for 27 trams) are order values. Bound as one
vehicle they would overstate by 152x, 36x and 27x respectively. Bound per vehicle they are about
1.47m, 1.00m and 1.48m.

**Chassis prices must not be bound as complete vehicles.** Bedford WTB £290 against £785 complete
(37 per cent), Dennis 30 cwt £550 and Daimler TE30 £650 all state chassis only. Treated as complete
buses or cars they would cut those targets by roughly 40 per cent.

**The prices most likely to move an existing target:**

- **Ret Hurst Nelson, £725 in 1911.** The register's only other 1911 bus is the LGOC B-type at
  £300. This is 2.4 times as much and would raise a 1911 electric-bus target sharply. The object is
  a battery/electric bus, so it may be a genuinely dearer machine rather than an error.
- **EE E11, £2,098 in 1929.** The nearest register evidence is the 1929 Leyland 51-seat
  double-saloon at £1,682.50 and the 1928 Leyland Lion at £1,345. It is 25 to 56 per cent above that
  cluster, so it would lift a 1929 trolleybus target by a quarter or more.
- **Daimler TE30.** The comment gives chassis £650 plus body £848 (midpoint) = £1,498, but £1,100
  for the complete surviving car. The 36 per cent gap between the two readings is larger than the
  effect of most other rows; which one is bound decides the 1913 luxury-car target.
- **Dennis 30 cwt, £550 chassis in 1922.** The register has a Dennis 20/25 cwt chassis at £295 for
  1923; a 30 cwt chassis at £550 is nearly double and would move the 1922-23 light-lorry target.
- **The nine Toyota prices, 1999-2024.** The register holds only three private-car prices (MG Y
  £525, Jaguar XK120 £1,263, both 1948, and E-Type £2,098, 1961) and nothing after 1961. These nine
  rows would create the modern private-car ladder from nothing, so they are material for every
  citycar of the last twenty-five years, not just the nine objects they name.
- **SR West Country rebuild, £5,428 in 1954.** The register's Merchant Navy overhaul rows are for
  1951 and in other units (195,934 and 40.9), so this is the only money-of-the-day rebuild figure;
  it would set the overhaul target for the rebuilt class.

**Likely small effect:**

- AEC 605, £1,445 in 1927, sits between the register's 1928 Leyland Lion (£1,345) and its 1933 AEC
  Q type (£1,847), so it confirms rather than moves the late-1920s double-decker level.
- The Bedford WTB (£785 complete) is consistent with the 1942 Bedford OWB at £810.
- The eight 1950s airliner prices (Britannia twice, Comet 1, Comet 4, DC-7, DC-7C twice, Vanguard)
  are the only 1950s airliner capital prices in the register apart from the VC10 breakeven figure,
  so they fill a gap rather than contradict anything. They are consistent with each other: piston
  airliners at 0.3-1.2m, the Vanguard at 1.0m, the jet Comet 4 at 1.16m.
- The Boeing 377 and L-1649 are in dollars and cannot be bound without a conversion.
