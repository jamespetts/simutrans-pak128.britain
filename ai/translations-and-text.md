---
status: stub
verified: New ex-15 @ 0ba8d7fc6
---
# Translations and text

**Covers**: user-facing text: `text/` `.tab` files, city name lists, simutranslator, and object
names.

## Initial facts

- `New/text/` contains translation `.tab` files (for example `be.tab`, `ca.tab`) and city name
  lists (`citylist_*.txt`, with a `citylists/` subfolder). These are copied into the built pakset
  rather than compiled. `[CODE New master @ e36ec2321]`
- The `simutranslator` target in `New/Makefile` packages `.dat` and `.png` files into zips for
  upload to simutranslator. `[CODE New master @ e36ec2321]`

## Object name entries in `en.tab` (required for every new object)

- **Translation texts are a required part of every new asset.** Any new object with a
  user-visible name is not complete until its `New/text/en.tab` entry exists; do not commit a
  new asset without it. The English text is required at creation; other languages follow
  through the translation workflow (see planned sections). `[USER-DIRECTION:2026-11-15]`
- Every new object needs an entry in `New/text/en.tab`. The file is plain ASCII text composed of
  two-line pairs: the object's internal `name=` value (from its `.dat`) on one line, then the
  English display name on the next. The display name is what the player sees; the key is the
  machine name, never localised. `[EXECUTION-VERIFIED:2026-09-23]`
- The file is divided by `#___…___` comment headers into sections; vehicle object names live in
  the per-waytype sections (`air-vehicle`, `NarrowGaugeVehicle`, `rail-vehicle`,
  `tram-vehicle`, `road-vehicle`, `water-vehicle`, `maglev-vehicle`) and are grouped by
  manufacturer/operator. Insert a new entry beside its peers, not at the end of file.
  `[EXECUTION-VERIFIED:2026-09-23]`
- The `Livery schemes` section holds operator-level scheme display names (for example
  `Wartime-Austerity` → `Austerity`); per-`liverytype` keys (for example `GER-Ultramarine`,
  `LNER-Standard`, `Douglas-Demonstrator`) are absent throughout, including for long-shipped
  liveries, so new liveries need no `en.tab` livery entry — follow the precedent. How the game
  displays an unlisted livery name is unverified (raw key fallback presumed).
  `[CODE New ex-15 @ 8b04b2114]`
- Forgetting the `en.tab` entry leaves the raw machine name (e.g. `ger-s69`,
  `douglas-dc-8-10`) shown in game. Checking this is a mandatory final step of every
  asset-adding task: search `en.tab` for each new object's `name=` value. The Audi A4 B6 and
  the Vauxhall Nova/Corsa family shipped without entries and were fixed on 2026-11-15.
  `[EXECUTION-VERIFIED:2026-09-23]` `[USER-DIRECTION:2026-11-15]`
- A **stray duplicate display line** is as damaging as a missing entry. The file is read as
  strict two-line key/value pairs, so an extra line shifts every following pair until the next
  extra line. The 2026-11-20 citycar check found 35 duplicate lines that had mis-paired 820
  consecutive entries; all were removed. Verify that the number of content lines is even and
  that no citycar key is followed by another citycar name.
- Editing `New/text/en.tab` (or `config/`, `sound/`) does NOT reach the game by itself: the
  build's `copy` target (`New/Makefile`, `cp -p text/*.* $(PAKDIR)/text`) copies these into
  the pakset directory only when `make` runs. After editing any `text/`, `config/`, or
  `sound/` file, re-run `make` before deploying/testing, otherwise the built pakset and the
  in-game UI carry the stale copy. This was the cause of the S69/DC-8 names not appearing.
  `[EXECUTION-VERIFIED:2026-09-24]`

## Planned sections

- How object names and texts are translated and uploaded.
- City name list conventions and variants.
- Program texts and `simutranslator` workflow.

## Open questions

- What is the current simutranslator workflow for this pakset?
