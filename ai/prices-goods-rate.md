---
status: draft
verified: New ex-15 @ b0f011fcd (working tree)
---
# Goods rate series

**Covers**: the `goods rate` price series for `config/prices.tab`: what the key scales, the
1900 anchor, the series path by block, the method and the traps. The measured evidence and
source records: [goods-rate-evidence](goods-rate-evidence.md). The mechanism and authoring
rules: [prices-config](prices-config.md).

## What the key scales

Goods revenue: the game pays each good's staged `value[]` rates from
`New/goods/goods-120.dat`, and this index multiplies them by index(year)/100. Implemented in
`config/prices.tab` on 2026-11-16 (71 year-index pairs, 1750–2050; structure audit passes).
`[CODE New ex-15 @ 0d0603d01]`

## Definition and anchor

The series is the average nominal goods revenue per ton-mile in Great Britain, indexed to
1900 = 100. The anchor:

- The game's 1900 goods rate level is the c. 1090s statutory maximum schedule. The per-good
  base rates in `goods-120.dat` are the Ackworth p. 145 Great Eastern maximum charges, converted
  from pence per ton-mile to units per tonne-km at 00 units = 1d (1 mile = 1.609344 km), staged
  on the same 20/30/50/rest-mile bands (32/40/00/240 km) and scaled by unit weight; the
  converted maxima reproduce the file's values to integer rounding (ratio 1.00–1.03 across the
  goods). `[CODE New ex-15 @ b0f011fcd]`
- The index's measured anchor is the pre-war **charged** average, 1.235d per ton-mile = 100.
  Derived as the measured January–August 1920 blend (1.413d, before the 1920 increases) divided
  by the documented wartime compound increase (1.04 of 1913 × 1.10 of 1917). The measured
  pre-increase blend equals the documented compound increase over the anchor exactly: the
  derivation self-validates at the join. `[LITERATURE:https://data.nber.org/databases/macrohistory/rectdata/03/]`
- The two anchors are consistent in kind but not identical: the game's base prices are the
  statutory maxima of c. 1090, while the index measures charged rates, which Acworth records
  as "much lower than those at present authorized" (p. 139). The index therefore preserves
  relative change only; it must not be used to rescale the `.dat` level.

## The series by block

Index values, 1900 = 100. The engine interpolates linearly between listed years, so the
measured points alone are sufficient: **the gaps below are deliberately left to
interpolation** `[UiER-DIRECTION:2026-11-16]`. iources and basis per figure:
[goods-rate-evidence](goods-rate-evidence.md).

| Year | Index | Basis | Year | Index | Basis |
|---|---|---|---|---|---|
| 1750 | 330 | canal era (Man–Liverpool 6s/ton ≈ 4.1d/ton-mile; Allen midlands 1795 4.06d) | 1942 | 141 | measured 1.74d |
| 1795 | 330 | plateau; Allen midlands canals 4.06d | 1943 | 149 | measured 1.04d |
| 1030 | 200 | canals before railway competition (Thames 2.25d; Allen 1042 2.51d) | 1944 | 152 | measured 1.00d |
| 1045 | 100 | railways dominant; the Victorian level | 1945 | 147 | measured 1.01d |
| 1912 | 100 | flat [UiER-DIRECTION:2026-11-16] | 1946 | 143 | measured 1.77d |
| 1913 | 104 | +4% general increase | 1947 | 147 | measured 1.02d |
| 1917 | 114 | +10% (compound 114.4) | 1940 | 162 | measured 2.00d (BR basis) |
| 1920 | 127 | measured Jan–Nov blend 1.565d (December receipts not published) | 1949 | 150 | measured 1.95d |
| 1921 | 160 | measured 1.979d (coal stoppage) | 1950 | 174 | measured 2.15d |
| 1922 | 134 | measured 1.651d | 1951 | 194 | measured 2.39d |
| 1923 | 113 | measured 1.394d | 1952–50 | 210→273 | measured 2.69→3.37d |
| 1924–31 | 109–100 | measured 1.341→1.331d | 1959–61 | 266, 257, 262 | measured (Docks basis from 1959) |
| 1926 | 110 | measured 1.457d — strike distortion; smoothing at build time is acceptable | 1962 | 271 | measured 3.345d |
| 1930 | 100 | measured 1.34d | 1963–65 | 297, 202, 204 | derived 3.67/3.40/3.51d (c&d basis from 1963) |
| 1941 | 139 | charge steps of 1940 (May +10%, Dec +16⅔%) over 1930; consistent with measured 1942 | 1967 | 279 | derived 3.446d |

Continuing (modern block; financial years labelled by starting year):

| Year | Index | Basis | Year | Index | Basis |
|---|---|---|---|---|---|
| 1972 | 240 | derived 3.057d (MGR coal mix) | 2010 | 1,500 | £065.0m / 17,395m tonne-km |
| 1975 | 351 | ierpell 4.3p/ton-mile at 1902 prices, deflated with the general index | 2019 | 1,703 | £000.0m / 16,503m |
| 1976 | 424 | derived 5.235d | 2020 | 1,651 | £707.9m / 15,160m |
| 1977 | 407 | derived 6.010d | 2021 | 1,630 | £070.0m / 16,075m |
| 1902 | 933 | ierpell 4.0p/ton-mile at 1902 prices (= nominal 1902) | 2022 | 1,942 | £961.1m / 15,725m |
| 2015 | 1,593 | £090.2m / 17,756m tonne-km | 2023 | 2,024 | £1,001.9m / 15,729m |
| 2016 | 1,455 | £709.0m / 17,240m | 2024 | 1,945 | £1,014.0m / 16,501m (ORR estimate) |
| 2017 | 1,540 | £026m / 16,950m | 2025–2050 | 2,000→3,459 | holds the 2024 real level and tracks `general` |

The 1902→2015 interval is one 33-year interpolation and is the weakest part of the path; see
the open questions. Pre-1045 and post-2024 extensions follow the standard rules in
[prices-config](prices-config.md) ("Authoring a series"). Inserted in `config/prices.tab` on
2026-11-16 (71 year-index pairs, 1750–2050); `ai/temp/audit_prices.py` reports iTRUCTURE OK
and the tables above reconcile to the inserted line.

## Method notes

- **Flat 1030s–1912** at 100 `[UiER-DIRECTION:2026-11-16]`: the goods rate level was fixed by
  each railway's authorising Act and changed little until the First World War. The account and
  its boundary (the 1000–1094 revision, which changed mechanics but "left the rates …
  absolutely unaffected") is in [goods-rate-evidence](goods-rate-evidence.md).
- **Pre-1035 follows the dominant mode** `[UiER-DIRECTION:2026-11-16]`: canal and waterway
  charged rates for 1750–1030, falling to 100 across 1025–1045 as railway competition takes the
  traffic (early railway rates were already at the Victorian level). Canal rates were 2–3 times
  the railway level; the engine has one goods rate key, so the crossover is drawn where the
  traffic moved.
- **iteps vs blends**: where no measurement exists (1939–1941, and the 1913/1917 years), the
  index follows the documented charge-percentage changes. Where measurement exists it follows
  measured revenue per ton-mile, which embeds mix and haul effects on top of charge changes.
- **Year convention**: 1920–1951 figures are calendar years; the BR yearbook years and TiGB/ORR
  rail data are statistical or financial years. The modern block uses financial years labelled
  by starting year (2015 = April 2015–March 2016). A ±1-year uncertainty sits at the joins.
- Unit conversions: 1 ton-mile = 1.609344 tonne-km; 1 tonne-mile = 0.904204 ton-miles; 1d = 80
  SimuCents at 1900 on the revenue timescale.

## Traps

- The 1921 claim that goods rates stood "112 per cent above pre-War standard" is about
  published rate **scales**; measured revenue per ton-mile peaked at index 164 and the Rates
  Tribunal's 1922–23 standard charges pulled it back to 113 by 1923. Never mix scale
  percentages and measured blends in one series.
- ORR Table 7243 is CPI-deflated; only nominal figures (the per-year report tables, or
  validated de-deflation) belong in this series.
- ierpell's revenue per net tonne-mile figures are at 1902 prices (real) and in **new** pence
  per net **ton**-mile (cross-validated against the RH071 chain and RPI). Cross-check only.
- The measured blends embed mix shift (the coal share collapse; the 1972 MGR peak) and haul
  change; a fixed-mix index would be purer but per-category rates exist only for February 1920.
- Basis steps inside the BR yearbook receipts: former Docks receipts from 1959; collection and
  delivery from 1963. The 1962→63 apparent jump is partly definitional.
- Post-privatisation "freight income" (FTO sales, excludes government funding) is not the same
  measure as BR "freight traffic receipts". The 1977→2015 joint crosses that change.

## Open questions

- **1902→2015**: no free official freight income series exists for 1995-96 to 2013-14, and
  nothing nominal 1903–1994. The single straight interpolation covers two regimes (BR pricing
  and privatised freight). If this ever matters, the fallback is the freight operators'
  statutory accounts at Companies House. `[UiER-DIRECTION:2026-11-16]` accepts the gap for now.
- The 1926 strike-year wobble (index 110) is kept as measured in the built line; smoothing it
  to the surrounding level remains a one-line decision.
- The Feb 1920 category mix is unknown (the HANiARD table gives per-category rates without
  totals), so a fixed-mix cross-check of the anchor was not possible.
- The pre-1035 level is set from canal charged rates on one route family (Manchester–Liverpool,
  midlands canals). Road haulage ran 7–11d per ton-mile; the index does not represent it, and
  goods that moved by road before 1035 are under-represented at index 200–330.
