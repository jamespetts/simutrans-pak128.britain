---
status: draft
verified: New ex-15 @ 81ffb5911 (working tree, uncommitted pass 72), 2026-11-27; simutrans-extended-sources ex-15 @ ebf26cfb9b
---
# Way and forge cost model: audit, 2026-11-26

**Covers**: the capital and maintenance targets of every `Ways - *` sheet in
`New/cost-balancing-capital.xlsx` and `New/cost-balancing-maintenance.xlsx`, the engine fields they
become, the `forge_cost_*` settings in `New/config/simuconf.tab`, and the measured-price binder in
`New/ai/cost-balancing/evidence_data.py`. No workbook, `.dat`, config, script or knowledge-base
file was changed by the audit.

**Companions**: [handoff](handoff.md) (the standing rules and the outstanding work),
[sanity-check-2026-11-25](sanity-check-2026-11-25.md) (the independent review that raised finding
B2), [infrastructure-cost-synthesis](../infrastructure-cost-synthesis.md) (the recommendations),
[infrastructure-cost-evidence](../infrastructure-cost-evidence.md) (the measured figures) and
[conversion-chains](../conversion-chains.md) (the unit arithmetic).

**Claim tags**: `[CODE New ex-15 @ 81ffb5911]` for pakset files; `[CODE
simutrans-extended-sources ex-15 @ ebf26cfb9b]` for engine files; `[LITERATURE:<source>]` for an
external source recorded in the knowledge base; `[UNVERIFIED]` for an inference that the stored
evidence does not settle. Evidence class is marked MEASURED, STATED, DERIVED, ESTIMATE or
UNAVAILABLE.

**Price basis**: GBP1900 means pounds of 1900. A `.dat` value or a `simuconf.tab` value is a raw
pakset integer, not money. The canonical conversions are in [conversion-chains](../conversion-chains.md):
capital GBP1900 per km = raw value x 0.00396311; maintenance GBP1900 per km-year = raw value x
0.09511464 (x 0.00792622 per km-month). One tile is 125 m, so a kilometre is eight tiles.

## Terms

- **Way object**: one `Obj=way` entry in a `ways/*.dat` file. Its `cost` field is a per-tile price
  and its `maintenance` field a per-tile monthly price.
- **Forge**: the engine's `forge_cost_<waytype>` setting in `config/simuconf.tab`. It is a per-tile
  charge added once when a new plain way is first built on a tile. It has no `.dat` field of its
  own.
- **Way-only value**: the audited total minus the forge. It is the value the `.dat` `cost` field
  would need so that `cost + forge` equals the measured total. A negative way-only value means the
  forge is larger than the measured total from which it is subtracted.
- **Combined total**: a measured price for the finished object, including formation and surface.
  **Formation-only**: a measured price for the bed alone. **Pavement-only** or **way-only**: a
  measured price for the surface layers or the permanent way, with the formation excluded.
- **Class target**: the value in the workbook's class group. **Measured target**: the value the
  workbook binds from the research register. The Match verdict uses the measured target when one
  exists.

## 1. Verdict

The way/forge decomposition is undefined without a scope for each measured price and each object.
The forge is a single constant per waytype; the measured prices are per object and cover
combined-total, formation-only and pavement-only scopes. The subtraction `way = total - forge` is
valid only where the measured price is a combined total for the same object and the forge is its
formation component. The workbook applies it to every row.

Consequences established by the audit:

1. **Eight class-side negative way-only values**, the rows named in finding B2, plus **three
   measured-side negative values** (the 41 lb tramway, the concrete runway and the asphalt runway).
   Eleven distinct object rows carry at least one negative value.
2. **Nine rows have a forge above half the class total**, including Tar MacAdam road (heavy) at 67
   per cent even though it stays positive. The maximum is 1,292 per cent (grass taxiway).
3. **The forge derivations do not support the values applied.** Rail is valid; narrow gauge is valid
   by analogy; tram, water, maglev, air and road are not. The water value has been corrected to zero
   in the workbook, the generator and both `simuconf.tab` copies.
4. **The maintenance chain has a second, independent failure.** The generator wrote per-tile
   maintenance into a per-kilometre column (a factor of eight, corrected manually in the live
   workbook and now corrected in the generator); rail and water are deflated a second time; air and
   power take the rail rate; road uses one 1880 main-road rate for every surface; elevated ways
   added the bridge **capital** as annual upkeep. The elevated rows and the generator's factor of
   eight are corrected in pass 72 (§1a); the rail, water, air, road, tram and maglev rates remain
   outstanding.
5. **The measured-price binder repeats the same failure.** Seven of the nine measured way binds are
   wrong in unit or scope. Pass 72 rejects the four wrong water binds, so the 3.98 billion large-ship
   value is gone; the 41 lb tramway and the two paved-runway binds remain, and the binder itself is
   unfixed.

The `.dat` `cost=` and `maintenance=` fields have not been changed for cost balancing. The only live
change in this way cost-balancing work is the `forge_cost_*` block in `config/simuconf.tab`, applied
on 2026-11-22 and with `forge_cost_water` set to 0 on 2026-11-27. The workbook values are proposals.
The present game therefore charges each old `.dat` cost plus the live forge; it does not charge any
suggested total from this workbook.

## 1a. Amendments, 2026-11-27

The user's directions of 2026-11-27 changed two spreadsheet treatments and the replacement rule.

- **Water forge zero.** The capital workbook's 16 water rows now carry forge 0, the way-only value
  equals the whole channel construction, and the Params `FORGE_WATER` cell states the decision. The
  four measured water binds the audit found to be a boat hull, a forum number and two whole
  projects are rejected; those rows use the class group. The generator returns 0 for water. The
  source and live runtime `simuconf.tab` copies were set to 0 on 2026-11-27.
- **Elevated maintenance corrected.** The maintenance workbook's 17 elevated rows now use the
  measured bridge upkeep rate from Cudworth 1886 plus the plain-way upkeep, not the bridge capital.
  Examples at 1900: brick rail/narrow 56.67 GBP/km-year (596 raw units), iron 246.67 (2,593),
  masonry 51.67 (543), timber 536.67 (5,642), concrete 56.67 using the brick proxy; brick road
  71.57 (752), iron road 261.57 (2,750), timber road 551.57 (5,799). The previous figures were about
  98-100 per cent of capital a year and are withdrawn. The ground/bed preparation is the forge
  capital item, which is retained; the plain-way upkeep covers the bed's routine upkeep. There is no
  separate measured ground-levelling upkeep figure.
- **The per-waytype forge is retained for every non-canal waytype.** The user's direction is that
  the formation-versus-way distinction is real for road, rail, narrow gauge, maglev, monorail,
  runway and taxiway, including a grass runway (levelling against surface and features). Only
  canals get forge 0. The replacement rule in §7 has been revised accordingly: one realistic
  formation value per waytype, no greater than the cheapest object's whole construction, with the
  way object carrying the rest.
- **Road and air research is applied (pass 73).** The road formation, construction and maintenance
  evidence, with the runway and taxiway analogy, gives `forge_cost_road = 20,000` raw
  (GBP79.26/km) and `forge_cost_air = 110,000` raw (GBP435.94/km), plus per-object routine
  maintenance rates. They are applied to the capital and maintenance workbooks and to the
  generator; the live `simuconf.tab` road and air settings are still 315,000 and 1,875,000, and
  their change is outstanding.

## 1b. Road and air applied, 2026-11-27

The [road and air research report](research-pricing-report-58.md) (2026-11-27) gives the first
measured decomposition of a road bed (Telford's 1825 Holyhead Road estimate) and the first measured
airfield formation share (Gatwick 1960, 37.7 per cent). It sets both per-waytype forges from the
cheapest object of the family, which is the only standard at which one value can be both realistic
and no greater than the cheapest object:

- **Road forge 20,000 raw = GBP79.26/km.** It is 79 per cent of the bridleway's GBP100/km whole
  construction and 72 per cent of Telford's measured bed preparation. The bridleway retains
  GBP20.74/km for its running surface and gates; every higher road carries its excess formation in
  its way object.
- **Air forge 110,000 raw = GBP435.94/km.** It is 76 per cent of the grass taxiway's GBP575/km
  whole construction, from the Valuation Office Agency grass specification (GBP1.00/m2 simple
  levelling, GBP2.00-2.50 drained and stabilised). The grass taxiway retains GBP139.06/km and the
  grass runway GBP327.06/km.

Both values are below the cheapest object of their waytype, so no way-only value is negative. The
eight class-side negative rows from the audit are resolved. The cobblestone row was separately
defective: its GBP123/km was the 1819 turnpike network average, not a sett carriageway. It now
carries the sett band midpoint GBP6,000/km (measured band GBP3,400-8,000, working band
GBP5,000-7,000), with a way-only value of GBP5,920.74.

The maintenance replacement uses routine-only rates, because the engine charges renewal separately
through `weg_t::renew()` and `wear_capacity`:

| Object | Routine maintenance GBP1900/km-year | Rate | Basis |
|---|---:|---|---|
| Bridleway, Unsurfaced (both) | 3 | 3.0% of capital | grading and grips; no surface renewal |
| MacAdam | 10 | 1.2% | 1880 main rate less re-stoning |
| Cobblestone | 120 | 2.0% of the corrected GBP6,000 | Victorian urban band, low end |
| Tar MacAdam / heavy | 49 / 60 | 4.6% / 3.2% | 1911 tarred-slag upkeep |
| Hot-rolled asphalt and SMA (6) | 79 | 0.50% | patching, crack sealing, surface preservation |
| Concrete road | 59 | 0.25% | joint resealing and slab repair |
| City road (2) | 132 | 0.50% | flexible, urban intensity |
| Motorway (2) | 132 | 0.50% | bottom of the 1982 young-motorway band |
| Grass runway / taxiway | 10 / 7 | 1.3% / 1.2% | mowing and rolling; no overlay |
| Asphalt and Tar MacAdam runway / taxiway | 114 / 86 | 0.50% | flexible airfield |
| Concrete runway / taxiway | 246 / 126 | 0.25% | rigid airfield: joint resealing, spall and slab repair |

The concrete/asphalt differential is now explicit in two places. The routine rate is 0.25 per cent
for concrete against 0.50 for asphalt, a ratio of 1:2, inside the measured 1:2.0-2.5. The renewal
life is in `wear_capacity` (concrete road 4 billion against 130 million-1.32 billion; concrete
runway 2.695 billion against 864 million). The absolute road figure favours concrete (GBP59 against
GBP79, 75 per cent). The absolute air figure does not (GBP246 against GBP114) because the concrete
runway's class capital is 4.33 times the asphalt's; the research shows that 4.33 is not a material
premium but a comparison of a PCN 10-93 midpoint at 45 m against an unstated PCN at 30.5 m with a
full pavement box against asphalt layers only. Fixing that capital comparison is a separate pass.

The two paved-runway measured binds (GBP69 per square metre bound as GBP per kilometre) are
rejected, as the four water binds were in pass 72. The live `simuconf.tab` road and air forge
settings remain 315,000 and 1,875,000; the workbooks and generator carry the research values and say
so on the Params sheet. The road and air config change is outstanding.

The research leaves four matters open: the concrete runway capital comparison; whether a motorway
tile is a lane or a carriageway (the row differs by a factor of three); the different deflators
used for the grass, tarmac and asphalt air rows (1989, 2010 and 2017-21 where the sources are
2017-24); and the six hot-rolled-asphalt and stone-mastic rows sharing one class capital, so the
layer thickness does not change the price.

## 2. What is not the cause

- **The conversion chain.** `0.00396311` and `0.09511464` reproduce the workbook columns; the
  `PER_KM = 252.3` constant is correct to 0.01 per cent. `[CODE New ex-15 @ 81ffb5911]`
- **The 125 m tile.** Every way is priced per kilometre, and the eight tiles cancel the
  `meters_per_tile/1000` scale for both capital and maintenance.
- **The `.dat` prices.** They are the quantity under audit and were not used as evidence.
- **The engine mechanics.** The forge is charged on new build and not on upgrade, pier deck, bridge
  or tunnel; it is reduced for parallel ways; `weg_t::renew()` charges the way value, not the forge.
  `[CODE simutrans-extended-sources ex-15 @ ebf26cfb9b, bauer/wegbauer.cc 2544, boden/wege/weg.cc
  1569, dataobj/settings.cc 4049]`
- **A handful of rows.** The same failure produces the nine over-half rows, the eleven negatives,
  the eight-fold maintenance error, the 60-fold motorway maintenance error, the elevated-way error
  of up to 7,241-fold, and one way-sheet value above the signed 32-bit field that is a binder
  artefact rather than a genuine price.

## 3. Capital: the scope failure

### 3.1 The rule and why it fails

`way = total - forge` is valid only when:

1. the total and the forge are measured for the same object;
2. the forge is the formation component of that same total; and
3. the total is at least the forge.

The model satisfies none of the three across a waytype. The forge is one number per waytype; the
totals are per object and span a factor of 4,341 on roads (GBP100-434,082 per km) and 171 on air
(GBP575-98,440 per km). The forge was derived from the high-standard member (air) or from a range
that matches neither end (road). Several totals are formation-only, so the forge charges a
component the total already contains; several are pavement-only, so the total contains no formation
for the forge to represent.

### 3.2 Scopes of the measured way prices

| Waytype | Measured price | Scope | Source |
|---|---|---|---|
| Rail | GBP1,300-1,900/km, anchor 1,600 | permanent way only; formation separate | [infrastructure-cost-evidence](../infrastructure-cost-evidence.md) §2 |
| Narrow gauge | the rail band by analogy | permanent way only | same |
| Tram | GBP5,050/mile complete street track; GBP3,487/mile non-rail base | complete track including the bed | research report 13 §4.3-4.5 |
| Water | GBP1,850-33,000/km by class; large ship GBP272,000/km | whole channel including formation | [infrastructure-cost-evidence](../infrastructure-cost-evidence.md) §5 |
| Air grass | GBP1-2/m2 | whole graded and seeded strip | §9 |
| Air paved | GBP69-189/m2 concrete, GBP32-56/m2 asphalt | pavement layers only; formation unmeasured | §9 |
| Road bridleway/unsurfaced | GBP100/km | formation and grading only | [infrastructure-cost-synthesis](../infrastructure-cost-synthesis.md) §3.2, §5 |
| Road cobble/MacAdam | GBP123/GBP833 per km | whole construction | §3.2 |
| Road tarmac | GBP1,072-1,875 per km | surface treatment | §3.2 |
| Road asphalt/concrete/city | GBP15,844-26,406 per km | whole construction including earthworks | §3.2 |
| Road motorway | GBP26,377 per km | way only | §3.2 |

The workbook's `measured-infrastructure.csv` and `measured_infra.py` record the number and a basis
string, but no scope field. The workbook applies the same subtraction to every scope.

### 3.3 The eight class-side negative rows

| Row | Sheet | Class total GBP1900/km | Forge GBP1900/km | Way-only GBP1900/km | Forge share |
|---|---|---:|---:|---:|---:|
| Bridleway | Ways - road | 100 | 1,248.38 | -1,148.38 | 1,248% |
| Unsurfaced (unimproved) | Ways - road | 100 | 1,248.38 | -1,148.38 | 1,248% |
| Unsurfaced (improved) | Ways - road | 100 | 1,248.38 | -1,148.38 | 1,248% |
| Cobblestone | Ways - road | 123 | 1,248.38 | -1,125.38 | 1,015% |
| MacAdam | Ways - road | 833 | 1,248.38 | -415.38 | 150% |
| Tar MacAdam | Ways - road | 1,072 | 1,248.38 | -176.38 | 116% |
| Grass runway | Ways - air | 763 | 7,430.83 | -6,667.83 | 974% |
| Grass taxiway | Ways - air | 575 | 7,430.83 | -6,855.83 | 1,292% |

The ninth over-half row is Tar MacAdam road (heavy), total GBP1,875, forge GBP1,248, way-only
GBP627 (67 per cent).

The three measured-side negatives are the 41 lb tramway (way-only -82,173 raw units), the concrete
runway (-1,874,572) and the asphalt runway (-1,874,572). They are binder errors, not forge errors;
see §5.

### 3.4 The forge derivations

| Waytype | Setting (raw) | GBP1900/km | Stated basis | Verdict |
|---|---:|---:|---|---|
| Rail | 88,000 | 348.75 | formation GBP250-400/km, measured | **Valid.** The permanent-way rate excludes formation and the formation is separately measured. |
| Narrow gauge | 95,000 | 376.50 | rail band by analogy | **Valid by analogy.** No separate narrow-gauge measurement. |
| Tram | 225,000 | 891.70 | GBP600/mile (GBP352/km at 1900) | **Invalid.** 2.54 times its source, and the way rate already includes the non-rail bed. |
| Water | 125,000 | 495.39 | none; decision is 0 | **Invalid and superseded.** Applied to the workbook, generator and both `simuconf.tab` copies as 0 in pass 72. |
| Maglev | 108,000 | 428.02 | "if a ground formation" | **Invalid in kind.** The guideway is elevated; the formation belongs with the piers. |
| Air | 1,875,000 | 7,430.83 | GBP6,000-9,000/km subgrade, explicitly unverified | **Invalid.** 9.74 times the whole grass runway and 12.92 times the grass taxiway. |
| Road | 315,000 | 1,248.38 | range 250,000-380,000, no derivation found | **Invalid.** 12.48 times the bridleway, 10.15 times the cobble, 1.50 times the MacAdam, 1.16 times the tarmac, and above every pre-1906 whole construction. |

The road range 250,000-380,000 appears as a recommendation in
[infrastructure-cost-synthesis](../infrastructure-cost-synthesis.md) §5 and is repeated in research
report 3 §4.5; no research report derives it. The stated basis is the early formation band
GBP50-250/km and the modern roadbed band GBP2,000-8,000/km; GBP991-1,506/km matches neither. The
air 30-40 per cent of pavement cost is not an airport figure: the only 30-40 per cent statement in
research report 3 is about electrification route clearance.

### 3.5 What the present game charges

The present charge is the old `.dat` `cost=` plus the live forge, not the workbook target. It shows
the direction and scale of the error, not the proposed value.

| Row | Present charge GBP1900/km | Workbook class target | Present / target |
|---|---:|---:|---:|
| Bridleway | 1,254.72 | 100 | 12.5x too high |
| Cobblestone | 1,274.14 | 123 | 10.4x too high |
| MacAdam | 1,299.90 | 833 | 1.56x too high |
| Tar MacAdam | 1,406.90 | 1,072 | 1.31x too high |
| Grass runway | 7,450.65 | 763 | 9.76x too high |
| Grass taxiway | 7,442.72 | 575 | 12.9x too high |
| Asphalt road | 1,612.99 | 15,844 | 9.8x too low |
| Motorway | 2,001.37 | 26,377 | 13.2x too low |
| Concrete runway | 8,986.34 | 98,440 | 11.0x too low |

The forge is the dominant error for the cheap roads and the grass runways; the old, unbalanced
`.dat` costs are the dominant error for the modern roads and runways. The two together compress the
road range by a factor of about 165 and the air range by about 107.

## 4. Maintenance: the second failure

The maintenance targets are also per-waytype constants, but the field is per object and could carry
the measured variation. The defects are independent of the forge and each other.

### 4.1 The factor-of-eight generator defect

`measured_infra.maintenance()` returns a per-tile-year figure (`to1900(per_km, y) / 8.0`, line 740).
`measured_infra.main()` labels the row `GBP/km` (line 810) and writes the per-tile figure to
`maint_gbp_yr`. `build_workbooks.fill_maint_row()` writes it into the "Class fixed (GBP/yr)" column,
which is per kilometre. A rebuild was therefore eight times low on every way maintenance target. The
live workbook was correct only because it carried a manual x8 correction that the generator did not
reproduce; `build_workbooks.py` line 46 names "the x8 way-maintenance columns" among the manual
corrections. Pass 72 adds the ×8 correction to the generator for ways and bridges, and a test
rebuild now reproduces the live way and bridge class fixed values to rounding (for example brick
rail 56.64 against the live 56.67). `[CODE New ex-15 @ 81ffb5911]`

### 4.2 Rail and water: a second deflation

`measured_infra.py` line 739 uses `44.0, 1966` and line 733 uses `62.0, 1938`. The evidence document
opens "Everything here is in 1900 prices unless stated", and
[infrastructure-cost-synthesis](../infrastructure-cost-synthesis.md) §2 is headed "Figures, 1900
prices". The rail £44 and the water £62 are therefore already 1900 money; the code deflates them
again.

| Anchor | Code target | Correct at 1900 | Understatement |
|---|---:|---:|---:|
| Rail £44/km-year | 6.67 | 44.00 | 6.6x |
| Water £62/km-year | 33.88 | 62.00 | 1.83x |

The synthesis's own cross-check says the current `wssr` maintenance of £52 per km-year "sits just
inside the measured £44-334 range". The workbook's £6.67 is outside it. The £44 anchor is itself
`[UNVERIFIED]` in scope and may be 7-8 times low; that is a separate reason not to use it as the
sole rail target.

### 4.3 Air and power: the rail rate

The `maintenance()` branch tests water, road, tram and maglev, and otherwise uses the rail rate. Air
and power therefore take a railway permanent-way upkeep rate:

| Object | Capital GBP1900/km | Correct band GBP1900/km-year | Workbook target | Understatement |
|---|---:|---:|---:|---:|
| Grass runway | 763 | 12.2-18.3 | 6.67 | 1.8-2.7x |
| Grass taxiway | 575 | 9.2-13.8 | 6.67 | 1.4-2.1x |
| Asphalt runway | 22,757 | 364-546 | 6.67 | 55-82x |
| Asphalt taxiway | 17,161 | 275-412 | 6.67 | 41-62x |
| Concrete runway | 98,440 | 1,575-2,363 | 6.67 | 236-354x |
| Concrete taxiway | 50,314 | 805-1,208 | 6.67 | 121-181x |
| Power line | 2,942 | 10.14 | 6.67 | 1.52x |

The air band is the measured 1.6-2.4 per cent of capital a year
([infrastructure-cost-evidence](../infrastructure-cost-evidence.md) §9). The power figure is GBP650
per km-year nominal 2015 deflated to 1900. `[CODE New ex-15 @ 81ffb5911]`

### 4.4 Road: one rate for every surface

The code uses the 1880 main-road rate, GBP22 x 100/102 = GBP21.57 per km-year, on all 24 road rows.
The same evidence gives minor roads GBP7.58 per km-year and urban streets GBP174-628 per km-year
(the Victorian 5d-1s 6d per square yard range over a 7 m carriageway). The single rate is 2.85 times
too high for a minor road, 21.6 per cent of the bridleway's capital, and 8.1-29.1 times too low for
an urban street. The motorway row carries a measured GBP1,304.74 per km-year; the class target is 60
times below it.

### 4.5 Elevated ways: capital used as upkeep

`measured_infra.py` lines 746-751 add `bridge_rate(row) / 8.0` to the annual maintenance.
`bridge_rate()` returns the bridge **capital** in GBP per kilometre, not its upkeep. Dividing by
eight converts per-kilometre capital to per-tile capital; it does not convert capital to upkeep. The
result is maintenance at about 98-100 per cent of capital a year:

| Row | Structure capital GBP1900/km | Measured upkeep, structure plus way GBP1900/km-year | Current `.dat` maintenance | Workbook class fixed GBP1900/km-year | Workbook suggested `.dat` | Workbook / measured |
|---|---:|---:|---:|---:|---:|---:|
| Brick viaduct elevated track | 109,100 | 56.67 | 205 | 107,506.67 | 1,130,285 | 1,897x |
| Iron girder elevated track | 165,600 | 246.67 | 1,269 | 164,006.67 | 1,724,780 | 665x |
| Concrete viaduct elevated track | 411,917 | 56.67 (brick proxy) | 149 | 410,323.20 | 4,314,986 | 7,241x |
| Wooden trestle elevated track | 49,600 | 536.67 | 4,480 | 48,006.67 | 504,842 | 89.4x |

The measured bridge upkeep band is 0.045-0.53 GBP per metre-year, i.e. GBP45-530 per km-year, about
0.046-1.15 per cent of structure capital. `[LITERATURE:infrastructure-cost-evidence.md §4, Cudworth
1886]`

Pass 72 replaces the workbook targets in the table with the measured bridge upkeep rate plus the
plain-way upkeep (brick rail 56.67 GBP/km-year, iron 246.67, timber 536.67, and the road equivalents
71.57, 261.57 and 551.57). The table above records the defect that was found and is withdrawn; it is
not the current treatment.

### 4.6 Tram and maglev

The `maintenance()` branch returns `None` for both. The maintenance workbook has no suggested
target for any tram or maglev way row, although the synthesis §3.1 and §3.7 carry recommended values
(500-800 raw units for tram, 42,000 for maglev).

## 5. The measured-price binder

`evidence_data.match()` lines 1430-1432 accept any row whose `kind` is `capital` and whose
`price_unit` contains "GBP" as the object's capital price. They do not require a per-kilometre unit
or a matching scope. Seven of the nine measured way binds are wrong:

| Row | Bound value | Bound as | What the source is | Effect |
|---|---:|---|---|---|
| Barge canal | GBP500 (1891) | GBP/km | a boat hull; the note says "hull cost; engines a further 336" | false measured target |
| Narrowboat canal | GBP900 (1935) | GBP/km | a number from a multi-item forum post | false measured target |
| Large ship canal | GBP15,000,000 (1894) | GBP/km | a whole 58 km project | 54.8x too high; 3,984,111,893 raw units, above the signed 32-bit field |
| Ship canal (improved) | GBP300,000 (1905) | GBP/km | a whole 9 km project | 9.0x too high |
| 41 lb tramway | GBP600 (1911) | GBP/km | the tram forge rate, GBP600/mile | measured-side negative |
| Concrete runway | GBP69 (1990) | GBP/km | GBP69 per square metre | 45,000x too low; measured-side negative |
| Asphalt runway | GBP69 (1990) | GBP/km | the concrete rate, wrong surface | 45,000x too low; measured-side negative |

The two clean binds are the power line (GBP15,535/km nominal 1959) and the motorway (the row's own
measured GBP1,304.74 per km-year, with a 1982/1986 year discrepancy of about 5 per cent). The
large-ship-canal 3.98 billion value is a unit artefact, not a genuine price; it should be removed by
the binder, not by widening the engine field.

## 6. The fundamental cause

The way family's cost model carries a waytype but not the object's construction standard, and a
number but not its scope. Three fields repeat the same collapse:

1. **The forge** is one value per waytype, applied to objects whose whole construction ranges from
   GBP100 to GBP434,082 per km.
2. **The maintenance target** is one value per waytype, applied to the same range; the elevated
   branch is a capital/upkeep category error on top.
3. **The measured binder** accepts a number without its unit or scope, so a boat hull, a whole
   project, a square-metre rate and a forge rate all become per-kilometre capital.

The canal decision of 2026-11-24 is the correct precedent **for canals only**: for a canal the
forging is the building, the formation differs by class, and one `forge_cost_water` cannot carry it,
so the whole construction sits in the way object and the forge is zero. For every other waytype the
formation and the way are distinct real components, including a grass runway, where levelling is
distinct from the surface and its very slight features. The failure is not that the split exists; it
is that the split has been implemented with one value per waytype that is not the formation
component of the objects to which it is applied. The replacement keeps the split and sets a
realistic per-waytype formation value, with the way object carrying the remainder.

## 7. A replacement decomposition

### 7.1 The rule

**Keep one forge per waytype, and make it a real formation value.** The forge is the bed
preparation: clearing, drainage, levelling, fencing and the sub-base. It is charged for every
waytype except canals. The value must be realistic for the waytype and no greater than the whole
construction of the cheapest object of that waytype, so no way-only value can be negative. The way
object carries its own surface or permanent-way cost and any formation above the common forge.

This preserves the engine features that exist for realism: the new-build charge on virgin ground,
the absence of the charge on an upgrade, and the parallel-way discount. The cost of the compromise
is that a high-standard object's excess formation sits in its way object and is repaid at renewal
and at a parallel build. That is a bounded error and must be stated on every affected row.

The scope of each measured price still has to be recorded, because the arithmetic differs:

- **Way-only** measured price (rail and narrow-gauge permanent way, the motorway "way only" rate, the
  paved runway rates): total = way + forge; the workbook must **add** the forge, not subtract it.
- **Combined** measured price (tram complete street track, early road whole construction, the HS2
  road rates): total = measured; way = measured - forge.
- **Formation-only** measured price (bridleway, unsurfaced road): the way object is the small
  surface/features component; the forge is the formation, and the whole measured price is the
  formation plus that small component.
- **Canal** measured price (whole channel): forge 0; way = measured.

### 7.2 The options

- **Per-waytype forge (chosen).** One realistic formation value per waytype; the way object carries
  its surface and the excess formation. No engine change. This is the per-waytype system the user
  endorsed, and it keeps the formation/way distinction that the engine implements for realism.
- **Per-object forge (refinement, engine change).** Add an optional `forge_cost=` to the way
  descriptor, defaulting to the waytype setting, and thread it through the forge call sites
  (`boden/grund.cc` 2076 and 2100, `bauer/wegbauer.cc` 2544 and 2611, `simworld.cc` 13527,
  `simtool.cc` 2888, `grund.cc` 803-813). This makes the new-build charge and the renewal charge
  exact for every object and preserves the parallel-way discount. It requires a `.pak` format change
  (descriptor field plus reader/writer version) and a new engine and pakset release. It is a
  refinement, not a requirement, and can be bundled with the signed 32-bit field decision.
- **Zero forge for non-canal waytypes (rejected).** It removes a real distinction, loses the
  new-build premium and the parallel-way discount, and contradicts the user's direction.
- **Keep the current midpoint (rejected).** Rule 0 and the user's direction.

### 7.3 Recommendation

1. **Adopt the per-waytype rule in §7.1 as a standing rule**, recorded beside rule 6 in the
   [handoff](handoff.md).
2. **Set `forge_cost_water = 0`** and make the water way-only value equal the whole channel
   construction. This is done in the capital workbook, the generator and both `simuconf.tab` copies.
3. **Fix the elevated maintenance** to the measured bridge upkeep rate plus the plain-way upkeep.
   This is done in the maintenance workbook and the generator.
4. **Apply the road and air research** (pass 73): road forge 20,000, air forge 110,000, the
   cobblestone capital correction, and the per-object routine maintenance rates, including the
   concrete/asphalt 0.25/0.50 per cent differential. The live `simuconf.tab` road and air settings
   remain outstanding.
5. **Correct the rail and narrow-gauge scope**: add the measured formation to the permanent-way
   rate, so the workbook total is way + forge, not way - forge. This raises those totals by the
   forge (about 22-24 per cent) and is a correction, not a cut.
6. **Resolve the tram double count**: the measured complete street track includes the bed and the
   forge also charges the bed. Either re-derive the tram way rate as rails and fastenings with the
   bed in the forge, or set the forge to the bed component and the way to the rest. Keep a forge,
   because the track and the street bed are distinct.
7. **Set a realistic maglev and monorail foundation/formation forge**, not the current placeholder,
   and state that it is an ESTIMATE because no British mainline exists.
8. **Fix the maintenance targets in the same pass** (§7.4) and **the binder** (§7.5).
9. **Plan the per-object forge only as a refinement** for a future engine version, not as the
   condition for realism.

### 7.4 The maintenance replacement

| Waytype | Replacement target | Basis |
|---|---|---|
| Rail | the per-object [synthesis](../infrastructure-cost-synthesis.md) §3.1 values, with the 1966 deflation removed; do not use the £44 anchor until its scope is re-derived | synthesis §3.1; report 39 §4.4 |
| Narrow gauge | as rail, with the narrow-gauge class values | synthesis §3.1 by analogy |
| Water | GBP62 per km-year at 1900, no second deflation; a stated class scale for ship canals | evidence §5 |
| Road | routine only, applied in pass 73: bridleway/unsurfaced 3; MacAdam 10; cobblestone 120; Tar MacAdam 49/60; HRA/SMA 79 (0.50%); concrete 59 (0.25%); city and motorway 132 (0.50%). Renewal is in `wear_capacity` | road research 2026-11-27 §11.4 |
| Air | routine only, applied in pass 73: grass runway 10, grass taxiway 7; asphalt and Tar MacAdam runway 114, taxiway 86 (0.50%); concrete runway 246, taxiway 126 (0.25%). The 1.6-2.4 per cent rule is combined and fits asphalt only | road research 2026-11-27 §6.4, §11.4 |
| Tram | 500-800 raw units (GBP47.6-76.1 per km-year) | synthesis §3.1 |
| Maglev | 42,000 raw units (GBP3,995 per km-year), the synthesis §3.7 value, which is 2 per cent of its elevated-way capital | synthesis §3.7 |
| Power | GBP10.14 per km-year (GBP650 nominal 2015 deflated) | evidence §9 |
| Elevated | the bridge upkeep rate, not the capital: 0.045-0.53 GBP per metre-year (GBP45-530 per km-year) plus the way upkeep; where no material rate exists, 2 per cent of capital and say so | evidence §4; Cudworth 1886 |

### 7.5 The binder replacement

`evidence_data.match()` must accept a capital row only if:

- its `price_unit` is per kilometre, or convertible to per kilometre by a stated factor (per mile
  divides by 1.609344; per square metre multiplies by a stated width and 1,000; a whole-project
  figure divides by a stated length);
- its scope matches the object (a pavement rate cannot bind to a formation-only object; a boat hull
  cannot bind to a canal; a forge rate cannot bind to a capital field);
- its price basis is recorded (nominal year or 1900) so the deflation is applied once.

Rows that cannot meet those tests are rejected with a reason, not bound.

### 7.6 Checks that would prove the replacement coherent

1. No negative way-only value on any way row, class or measured side; state the minimum.
2. Forge not above the total on every row; state the maximum share.
3. Maintenance within the measured band for the object's own standard and era (road concrete 0.25
   per cent of capital, asphalt 0.50, motorway 0.50; air concrete 0.25, asphalt 0.50, grass 1.2-1.3;
   rail 0.4-3 per cent; water 0.9-1.7 per cent for narrow canals; elevated within 0.046-1.15 per
   cent of structure capital plus way upkeep).
4. Every measured bind has a unit, a scope and a price basis.
5. A sample of rows built in the debug game matches the workbook total within 1 per cent
   (bridleway, MacAdam, motorway, grass runway, concrete runway, `wssr`, a canal).
6. A rebuild with `COST_BALANCE_OUT` reproduces every way row, including the x8 maintenance factor.
7. The present-game compression is removed: the bridleway and motorway current-charge/target ratios
   are both within the workbook tolerance.

## 8. What could not be verified

- The basis of the BR 1966 £44 anchor. The evidence doc and the synthesis present it as 1900 money;
  the code treats it as nominal 1966. The source is untraced, so the correct deflation cannot be
  settled from the stored evidence. Either the code or the two documents is wrong; the workbook
  cannot be right under both.
- The derivation of the road forge range 250,000-380,000. No research report contains it, and the
  stated bands do not produce it.
- The air subgrade estimate GBP6,000-9,000 per km. Research report 3 calls it unverified and the
  evidence doc has no entry for it. The conclusion does not depend on its exact value: any single
  air forge above GBP763 per km produces a negative grass runway.
- Whether the tram GBP5,050 per mile includes paving. Research report 13 says it is not stated and
  that it is "best read as" including it. The double count with the forge is probable, not certain.
- The re-stoning cycle behind the 1880 road anchor, so the routine-only component (GBP4-11 per
  km-year) is a derived range, not a measurement.
- Whether a live build charges the forge on elevated ways. The code excludes only upgrade and pier
  deck, so it does; no build was run to observe it.
- The 1982/1986 year discrepancy on the motorway maintenance row, about 5 per cent.

## 9. Files changed and still to change

**Changed in pass 72 (2026-11-27):**

- `New/ai/cost-balancing/wb_fv_pass72.py` (new): the water forge and elevated maintenance patch.
- `New/ai/cost-balancing/measured_infra.py`: the workspace base path, the `bridge_upkeep()` helper,
  and the elevated maintenance branch (capital replaced by the measured upkeep rate).
- `New/ai/cost-balancing/build_workbooks.py`: water forge 0 and the Params note, 0 written as 0,
  and the ×8 way and bridge maintenance correction.
- `New/cost-balancing-capital.xlsx`: the 16 water rows, the four rejected water measured binds, and
  the Params `FORGE_WATER` cell.
- `New/cost-balancing-maintenance.xlsx`: the 17 elevated rows in `Ways - rail`, `Ways - road` and
  `Ways - narrow gauge`.
- `New/ai/cost-balancing/measured-infrastructure.csv`: regenerated with the corrected elevated
  upkeep and the sett cobblestone capital.

**Changed in pass 73 (2026-11-27):**

- `New/ai/cost-balancing/wb_fv_pass73.py` (new): the road and air research patch.
- `New/cost-balancing-capital.xlsx`: road forge 20,000, air forge 110,000, the cobblestone capital
  correction, and the rejection of the two paved-runway measured binds.
- `New/cost-balancing-maintenance.xlsx`: the 18 plain road and 8 air routine-maintenance rows.
- `New/ai/cost-balancing/evidence_data.py`: the per-object synthesis maintenance override, scoped
  away from elevated ways and bridges.
- `New/ai/cost-balancing/build_workbooks.py`: road and air forge overrides, the water Params note,
  and the corrected way/bridge maintenance unit.
- `New/ai/cost-balancing/measured_infra.py`: the sett cobblestone capital and the way maintenance
  unit.
- `New/ai/cost-balancing/synthesis-recommended.csv`: the road and air per-object maintenance values
  and the six hot-rolled-asphalt and stone-mastic rows.

**Still to change:**

- `New/config/simuconf.tab`: `forge_cost_water` 0 (done on 2026-11-27, source and live runtime
  copy). `forge_cost_road` 315,000 -> 20,000 and `forge_cost_air` 1,875,000 -> 110,000 are
  outstanding; the workbooks and generator carry the research values.
- The rail and narrow-gauge scope correction (add the formation, do not subtract it).
- The tram double count; the maglev and monorail foundation forge.
- `New/ai/cost-balancing/evidence_data.py`: the binder unit and scope tests.
- `New/ai/cost-balancing/wb_audit_coherence.py`: extend it beyond the vehicle sheets to the way
  sheets; add the checks in §7.6.
- `New/ai/cost-balancing/handoff.md`, `sanity-check-2026-11-25.md`, `infrastructure-cost-synthesis.md`,
  `infrastructure-cost-evidence.md`, `cost-data-coverage.md` and `cost-balancing-register.md`: the
  forge rule, the maintenance treatment and the scope requirement.
- If the per-object forge refinement is approved: the engine descriptor, reader, writer and the six
  forge call sites.

## Open questions

- Should the concrete runway capital comparison be corrected? The present 4.33-fold premium is a
  PCN 10-93 midpoint at 45 m against an unstated PCN at 30.5 m and a full pavement box against
  asphalt layers only; the measured material premium is +20 to +60 per cent. Correcting it would
  make the concrete runway's absolute routine maintenance fall below the asphalt's.
- Is a motorway tile a lane or a carriageway? The research and the workbook differ, and the row
  differs by a factor of three.
- Should the grass, tarmac and asphalt air rows be re-deflated to one basis? They use 1989, 2010
  and 2017-21 deflators where the sources are 2017-24.
- Is the BR 1966 £44 anchor routine length-gang upkeep only, or the combined head? Its scope decides
  whether the rail target is the synthesis's per-object ladder or a higher band.
- Should the tram way rate be re-derived as rails and fastenings only, with the bed carried by the
  forge, as research report 13 §4.5 describes?
- Is the per-waytype compromise acceptable permanently, or is the per-object forge refinement worth
  the engine change? The refinement is not needed for realism; it reduces the excess formation in
  the high-standard way objects.
- Should the tram way rate be re-derived as rails and fastenings only, with the paving carried by
  the road object, as research report 13 §4.5 describes?
