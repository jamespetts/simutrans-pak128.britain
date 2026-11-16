---
status: draft
verified: New ex-15 @ 0a4be8077 (working tree)
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

- Complete the three price types that still fall back to `general` in `config/prices.tab`:
  `goods rate`, `vehicle purchase` and `vehicle maintenance`. Research sources and method:
  [prices-config](prices-config.md), [prices-infrastructure](prices-infrastructure.md);
  source-recording rule: [calibration-sources](calibration-sources.md).
  `[USER-DIRECTION:2026-11-15]`
- Research each cost domain to the depth of the infrastructure study before deriving balance
  implications, and only then take the balancing decisions. Infrastructure is complete:
  [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) holds the recommendations and
  the decisions taken, [infrastructure-cost-evidence](infrastructure-cost-evidence.md) the
  measured figures. The remaining domains are revenue and fares, vehicles, staff, fuel, and
  corporate overheads. **Do not change `.dat` cost values until the whole body of research is
  available**, because the balance implications have to be derived from all of it together.
  `[USER-DIRECTION:2026-11-16]`
- Add the missing citycar assets listed in
  [objects/citycar-asset-gaps](objects/citycar-asset-gaps.md) — the comprehensive gap
  register (P1: Very-high luxury cars for 1922–1947 and 1989–2025; P2: entry cars including
  the motorcycle and sidecar; P3: Cavalier/Astra/Golf/Beetle; P4–P5: luxury richness and
  texture). Work it photograph-first per
  [graphics/visual-asset-controls](graphics/visual-asset-controls.md).
  `[USER-DIRECTION:2026-11-15]`
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
  [objects/citycar-parc-anchors](objects/citycar-parc-anchors.md), and decide whether to add
  the missing anchor models the research identified (Ford Fiesta, BMC 1100/1300, possibly a
  Morris Cowley). `[USER-DIRECTION:2026-11-15]`
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
- Ford Anglia 100E/105E photographic geometry rework: the user accepted the replacement
  models and colour renders, including the corrected 100E boot. The replacement sprites
  are installed in the source tree and compiled into the local citycars pak. Accepted
  source files and maintenance procedure:
  [graphics/anglia-sources](graphics/anglia-sources.md).
  `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`

## Open questions

- What other work items should be entered, and in what order?
