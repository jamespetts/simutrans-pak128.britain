# Cost-balancing workbooks: handoff

**Status**: analysis complete and committed; `.dat` costs deliberately NOT changed. A fresh
session applies the remaining items. Written 2026-11-23.

## What this is

Two workbooks, `New/cost-balancing-capital.xlsx` and `New/cost-balancing-maintenance.xlsx`, compare
every `.dat` price in the pakset with a target derived from **measured historical evidence**. The
target column must never take a `.dat` price as an input: that is the quantity under audit, and
using it to build the target is circular.

Coverage: **4,071 of 4,218 objects have a capital target (97%); 4,154 have a maintenance target
(98%)**. Both workbooks rebuild with zero error cells.

## How it is built

| File | Role |
|---|---|
| `evidence_data.py` | vehicle ladders, feature multipliers, the `extrapolation()` entry point, the qualitative adjustment layer |
| `measured_infra.py` | infrastructure capital and maintenance from measured rates; writes `measured-infrastructure.csv` |
| `build_workbooks.py` | reads the inventory, research CSVs and the two files above; writes both workbooks |
| `vehicle-adjustments.csv` | 81 sourced qualitative adjustments (capital and maintenance factors) |
| `infrastructure-features.csv` | 655 infrastructure objects x 43 attributes, from `.dat` fields and comments |
| `vehicle-features-*.csv` | locomotive, multiple-unit and general vehicle attributes |
| `measured-infrastructure.csv` | per-object measured targets and their basis strings |
| `water-capacity.csv` | hull + hold capacity for the 216 water objects |
| `research-pricing-rows-*.csv` | the evidence register, one row per measured price, with source |
| `research-pricing-report-*.md` | the findings behind each pass |

Rebuild: `C:\WINDOWS\py.exe -3 ai\temp\build_workbooks.py`, then recalculate with LibreOffice
(`--headless --convert-to xlsx`) and copy the recalculated files over `New/*.xlsx`, which stores
cached values so the workbooks open with numbers rather than formulas.

## What is applied

- **Vehicles**: rail ladders (steam by weight and power, diesel/electric by power, multiple-unit
  per car), road (bus, lorry, car), tram, aircraft (hedonic fit on 116 aircraft, R2 0.948), ships
  (flat).
- **Early electric locomotives**: £4.4/hp series 1902-22, £8.8 prototype, £7 for 1948-55.
- **Features**: steam superheat/compound/cylinders/Caprotti relative to the fitted base; tenders
  and Garratt middle/rear priced zero with the front unit carrying the consist; road engine type;
  carriage dining/bogie/steel.
- **Infrastructure**: ways by measured rate and rail weight; bridges and tunnels by material and
  section; stations by platform material and building class; signals by technology and per-SEU
  system maintenance carried by the signalbox; depots, roadsigns, electrification, piers (unpriced).
- **prices.tab**: 1921-22 corrected (the 1923 value was right); mail-rate plateaus closed.

## Remaining work, in order

1. **Water size ladder.** The measured rates are ready: ferries 84.1 x GT^0.90 in 1900 GBP (R2
   0.992), coastal cargo £35/GT, inland £17/GT. Blocked because the pakset records no gross
   tonnage. `water-capacity.csv` gives hull+hold capacity in tonnes; the missing step is a
   GT-versus-capacity bridge fitted from research pass 25 (which states GT and deadweight on the
   same line). Then replace the flat £38,958 ship ladder.
2. **General feature premiums.** Only road engine type and carriage dining/bogie/steel are wired.
   Transmission, suspension, heating, air conditioning, low floor, corridor, sleeping and tram
   articulation are researched (pass 8) and have attribute columns, but no multipliers applied.
3. **Piers**: 111 objects unpriced. Decision needed: leave at zero (bridge carries the structure)
   or charge the measured 13-25% substructure share.
4. **Knowledge-base corrections awaiting review**: the 1983 and 2016 road maintenance rows are
   2.4x too small (decimal pence treated as old pence; corrected 178, 22, 12); "timber bridge
   upkeep 7-8 times plain line" should read "7-8 times the brick rate".
5. **`.dat` update.** The point of the exercise. Do it as one total-set pass, not object by object.

## Interim, not settled

- `prices.tab` `vehicle purchase` 1921 and 1922 are a constant-rate bridge pending Feinstein
  p. 150 (print only).
- `passenger fare` 1914-21 is an unclosed plateau; post-1971 mail rates need a Post Office check.
- Steam: the ladder is a complete-engine ladder on engine weight; tank/tender handling is inferred.
  Post-1900 feature premiums are applied relative to the sample's composition (baseline 1.137).
- Aircraft pressurisation and swept wing are unidentifiable in the sample and not applied.

## Rules learned the hard way

1. **Never use a `.dat` price, or a value derived from one, as a target.** Same for the old
   balancing spreadsheets (`Vehicle cost table.ods`, `Simutrans Ship Balance.xlsx` and the rest):
   they are the prior balancing, not evidence.
2. **Never use `level`.** It was used to set the old prices, so a ladder on it reproduces them.
3. **Read the inventory names; do not guess them.** Four passes were lost to name matching:
   `GWR-Churchward-Star` not `gwr-star`; `LNWR-precursor-webb` is not the Webb compound;
   Sprinters and Pacers are `br-150`, `br-142`; Underground stocks are `LUL_C_Stock` with
   underscores. A resolution step against `cost-inventory.csv` would prevent the next one.
4. **Match the sample, not the intuition.** A variance is not a premium until the sample's own
   composition is the baseline.
5. **Unit scales differ by object type**: ways and bridges per kilometre (a tile is 125 m);
   platforms at the graphics scale (28.6 m of train per tile, from vehicle `length`); per-object
   classes scaled 0.125; depots and HQ unscaled.
