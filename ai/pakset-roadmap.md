---
status: draft
verified: New ex-15 @ 2b3ae85bf (working tree, 2026-11-21)
---
# Pakset roadmap

**Covers**: the registry of planned pakset work: assets to add, gaps to fill, and changes needed
for new engine features.

## Notes

- Read this when planning what to add in what order. Check it after completing work and close the
  relevant entry ([conventions](conventions.md), "Adding assets and features").
- The project's current long-term priorities are listed in [../../AGENTS.md](../../AGENTS.md):
  supporting the forthcoming 15.x engine version, historical balancing, new vehicles and objects,
  filling gaps, and matching new engine features.

## Planned work

- Implement the cost of capital as planned in the engine's `ai/project-roadmap.md`: a player starts
  with little or no money and borrows through dated instruments — bonds of one to ten years, or
  instalment loans — issued against a credit rating, with interest and repayment shown in the
  finance window. Today there is only a starting windfall and an untimed overdraft. The pakset must
  supply the term structure and the historical railway borrowing yields. Specification, state of
  play and acceptance tests: [cost-of-capital](cost-of-capital.md). Engine work, for the next
  release. `[USER-DIRECTION:2026-11-17]`

- `vehicle maintenance` in `config/prices.tab` is the only price type still falling back to
  `general`, and the decision is to leave it there: no UK maintenance or repair price index
  exists before January 1987, and the later series measure private motor cars. Revisit only if a
  rail or engineering repair price series is found. Method and sources:
  [prices-config](prices-config.md), [vehicle-cost-evidence](vehicle-cost-evidence.md).
  `[USER-DIRECTION:2026-11-17]`

- **Building staff: open question.** `staff.tab` is charged only for vehicle crew. Signalbox and
  control-tower staff are inside the building maintenance, not separate. Should the engine gain a
  building staff field and a charge path, so signalboxes, airports and other buildings can carry
  staff numbers and wages? If yes, the signaller wage series is ready; an ATC series would need
  NATS/CAA data. Analysis: [staff-wages/reconstruction](staff-wages/reconstruction.md).
  `[OPEN:2026-11-23]`
- **Vehicle crew complements: rail, road, tram, sea and air declared.** Every powered rail, air and
  water vehicle now declares a crew complement, and `config/staff.tab` has twelve grades: the seven
  land grades plus ship's officer (7), ship's rating (8), ship's catering (9), aircraft flight deck
  (10) and cabin crew (11). 521 rail vehicles carry a guard, 204 vessels carry sea crew and 230
  aircraft carry flight-deck crew; 449 objects carry a multiple-working code, now the real coupling
  code rather than a single shared number. The role map, the rules and the engine limitations are
  in [staff-wages/crew-complements](staff-wages/crew-complements.md). The remaining item is that
  the cost-balancing workbooks exclude crew, so the balanced vehicle targets sit below actual
  running cost. `[OPEN:2026-11-23]`
- **Vehicle fuel consumption: declared on every powered vehicle.** 1,924 objects carry `fuel_per_km`
  and `calibration_speed`, so the engine charges fuel on top of maintenance: 390 steam rail, narrow
  gauge and tram objects, 595 diesel and electric rail, 587 road, 230 air and 122 water. The unit
  convention in `config/fuel.tab` is resolved and verified (192 × pence per unit; `fuel_per_km` in
  thousandths of a unit), and the model, the researched figures and the calibration decision for each
  sector are in [fuel-consumption](fuel-consumption.md). Open: `fuel[hydrogene]` is still commented
  out, so hydrogen maglev is free; marine bunker fuel has no price series of its own; and the 1968
  point of the coal series is about half what it should be. `[OPEN:2026-11-23]`
- **Steam locomotive coal range applied.** `range` is set on 175 steam locomotives as the coal range
  at full bunker, 144-924 km with a median of 360, now that the engine is gaining replenishment.
  Recorded with the figures in [fuel/steam](fuel/steam.md#range). What is still wanted is a water
  range, which no source in the pakset supplies. `[OPEN:2026-11-24]`
- **Steam tram fuel and power re-based on measured company accounts.** The six tram engines now carry
  1,600-3,100 g of coke per km from Kinnear Clark's reproduction of the tramway companies' coal
  returns, not the sheet's unsourced grate-area guess. The finding is that a tram engine's fire is
  demand-limited rather than grate-limited, and that the true burn rate is about 5-7 kg/h per square
  foot against the sheet's 2.5-3.0. Their `power` rose from 2-6 kW to 11-31 kW from the class duty
  ratings, which is what the tractive efforts always implied. Coke still has no price series of its
  own. Method, evidence and confidence: [fuel/steam-tram](fuel/steam-tram.md). `[OPEN:2026-11-24]`
- Research each cost domain to the depth of the infrastructure study before deriving balance
  implications, and only then take the balancing decisions. Infrastructure and vehicles are
  complete: [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) and
  [vehicle-cost-evidence](vehicle-cost-evidence.md) hold the findings, and
  [balance-synthesis](balance-synthesis.md) holds the cross-domain account against Acworth.
  Fuel evidence is in [fuel-evidence](fuel-evidence.md) and staff wages in
  [staff-wages](staff-wages.md); corporate overheads are recorded in the headquarters section of
  the infrastructure synthesis. **Do not change `.dat` cost values until the conversion question
  in [balance-synthesis](balance-synthesis.md) is settled**, because it scales every value in both
  programmes by two orders of magnitude. `[USER-DIRECTION:2026-11-16]`
- **Citycar build programme: complete.** The 2026-11-15/16 register ran to order 51 and closed on
  2026-11-20 at 436 models / 1,767 objects: 425 cars, 7 outfits and 4 horse-drawn vehicles. All
  named P1, P2 and P3 gaps are closed; the pre-1920 audit is closed; the outfits are built. The
  current coverage audit and the remaining segment, marque, body-style and luxury-richness gaps
  are in [objects/citycar-asset-gaps](objects/citycar-asset-gaps.md). Produce any new car by the
  divided workflow in [graphics/car-batch-production](graphics/car-batch-production.md):
  orchestrator research, frontier-model geometry, orchestrator `.dat` and compile.
  Photograph-first per [graphics/visual-asset-controls](graphics/visual-asset-controls.md).
  `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-21]`
- Re-do citycar geometry that was built from text descriptions (dimension tables) using
  direct photographic reference, per the hard rule and
  [graphics/visual-asset-controls](graphics/visual-asset-controls.md): Ford Fiesta Mk1–Mk7,
  `BMC1100`, Ford Escort Mk2, and the Vauxhall Corsa family (`VauxhallNova`–`VauxhallCorsaF`).
  Deferred 2026-11-15 by the user as acceptable at low resolution for now — flagged to be
  redone later. The Anglia rework is complete; see the completed-work entry below.
  `[USER-DIRECTION:2026-11-15]`
- Rebase all private-car `DistributionWeight` values to the anchor principle (most popular car
  on the road at a given time = 100, assuming 5 colourways; inverse scaling for fewer
  colourways), using the parc research in
  [objects/citycar-parc-anchors](objects/citycar-parc-anchors.md). The anchor models the research
  identified are now present: Ford Fiesta Mk1–Mk7, BMC 1100/1300, the Vauxhall Cavalier and
  Astra, VW Beetle and VW Golf. The Morris Cowley is represented by the Oxford twins, pending
  ratification. `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-21]`
- Convert all remaining graphics from the old special-colour background to anti-aliased alpha
  transparency. Many graphics still use the old system, and the aim is to convert all of them. See
  [image-layout](graphics/image-layout.md) and [blender-rendering](graphics/blender-rendering.md).
  `[RECOLLECTION:2026-09-19]`
- Recreate missing `.blend` source files for existing graphics that lack them, so that those
  graphics can be converted and maintained. This notably applies to most London Underground
  vehicles; there is no `london-underground` folder in the blend repository.
  `[RECOLLECTION:2026-09-19]` `[CODE GitBlends master @ 1c1acf58]`
- GER S69 4-6-0 and B12/3 graphics (in progress, uncommitted at time of entry). S69: five
  livery blends replicate the user-corrected golden `ger-s69-ww1-human-fix.blend` plus recorded
  deltas, assertion battery passing; known remaining defects: no coupling-rod objects (a black
  mass stands in), no tender in any engine blend, cab-side number plates deleted everywhere,
  one `Vermillion`-lineage material (`Vermillion.008`) renders black unexplained, and model
  absolute scale is inconsistent (~7–25% across axes). Pre-B12 backups live in the blends
  repository at `trains/Locomotives/S69-preB12-backup/`; tier-1 references at
  `trains/Locomotives/GER-S69/`. B12/3: the three blends carry the known-wrong v1 front board;
  rebuild the board to the v2 profile (top 0.95 falling to 0.87, meeting the band's dipped tip
  at 0.915) and re-import. `[RECOLLECTION:2026-09-27]`

## Completed work

- `vehicle purchase` price series added to `config/prices.tab`, 1900 = 100, 1750-2050. A
  three-block chain: Feinstein railway rolling stock 1856-1938, Feinstein plant and machinery
  1938-1965 as a war-bridging proxy, and Blue Book 1997 vehicles, ships and aircraft 1965-1997;
  the 1997 real level is held thereafter. The Blue Book 2026 pair and ONS CPI D7CO were tested
  as tails and rejected. Method and caveats: [prices-config](prices-config.md).
  `[EXECUTION-VERIFIED:2026-11-17]`

- Engine land base split: `cost_buy_city_land` added for city land, the ×6 capital branch
  corrected and city wayleaves moved to the city base by the other agent. The pakset carries
  `cost_buy_land=1500` and `cost_buy_city_land=2625`; see [prices-config](prices-config.md).
  `[CODE simutrans-extended ex-15 @ 0d41455e]` `[USER-DIRECTION:2026-11-15]`
- `city land` and `country land` price series added to `config/prices.tab`. Country land uses
  the Savills England farmland series 1900-2024; city land uses the ONS UK land under
  dwellings series 1995-2025 chained to the JST UK house price index for 1900-1995. Method,
  sources and first-pass limitations: [prices-config](prices-config.md) and
  [calibration-sources](calibration-sources.md). `[EXECUTION-VERIFIED:2026-11-15]`
- `buildings` price series added to `config/prices.tab`, 1900 = 100, 1750-2050. A four-block
  chain: Mitchell's building cost index 1845-1938, Holmans's construction cost index 1939-1954,
  the BIS output price index for all new construction 1955-2013, and the ONS construction output
  price index for all new work 2014-2026. Sources, link periods and limitations:
  [prices-config](prices-config.md), [calibration-sources](calibration-sources.md).
  `[CODE New ex-15, working tree 2026-11-15]`
- BSA M21 600 cc side-valve motorcycle with Watsonian Maxstoke sidecar: the first of the
  motorcycle-and-sidecar series, accepted by the user and installed 2026-11-15. Three
  colourways (Black, Maroon, BSA Light Green) in `New/citycars/bsa-m21-combo.dat`; the
  citycars pak compiles with the outfit included. The `.dat` header carries the dimensions,
  parc reasoning, colour sources and image credits; the reference images are in the blends
  repository under `citycars/references/bsa-m21-watsonian/`. The build also produced the
  divided-workflow rules now in [graphics/car-batch-production](graphics/car-batch-production.md),
  including the no-automatic-correction-round rule.
  `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`
- BSA 557 cc outfit (1923 Model H with Type 1 sidecar): the second of the motorcycle series,
  built lean (nine objects, low effort, one comparison and a four-view check) and installed
  2026-11-15 under the size-based leniency rule. Two colourways (Green, Black) in
  `New/citycars/bsa-557-combo.dat`; references and sources in the `.dat` header.
  `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`
- Vauxhall Cavalier family (Mk1, Mk2, Mk3): built as separate shells with four documented
  factory colourways each and installed 2026-11-16. Mk1 180 total weight (Signal Yellow, Signal
  Red, Polar White, Regatta Blue); Mk2 300 (Helios Blue, Carmine Red, Astro Silver, White Gold);
  Mk3 320 (Star Silver, Satin Red, Diamond Black, Nautilus Blue). Comfort follows the register:
  85/458, 100/480, 110/495.
  `[USER-DIRECTION:2026-11-16]` `[EXECUTION-VERIFIED:2026-11-16]`

- Ford Anglia 100E/105E photographic geometry rework: the user accepted the replacement
  models and colour renders, including the corrected 100E boot. The replacement sprites
  are installed in the source tree and compiled into the local citycars pak. Accepted
  source files and maintenance procedure:
  [graphics/anglia-sources](graphics/anglia-sources.md).
  `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`

## Open questions

- What other work items should be entered, and in what order?
