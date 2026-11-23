---
status: stub
verified: New ex-15 @ f22a41c83; simutrans-extended ex-15 @ b914de7f4
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
  asset-adding task: search `en.tab` for each new object's `name=` value. The search is necessary
  but not sufficient, because a malformed line elsewhere in the file can leave the key present
  and out of the loaded table; see the next two bullets. The Audi A4 B6 and the Vauxhall
  Nova/Corsa family shipped without entries and were fixed on 2026-11-15.
  `[EXECUTION-VERIFIED:2026-09-23]` `[USER-DIRECTION:2026-11-15]`
- **Any malformed line breaks the table, not just a missing entry.** `en.tab` is read as strict
  two-line key/value pairs. The reader skips only lines that begin with `#`, and drops a pair
  whose two lines are identical. Any line that does not belong in the pair being read — a blank
  line, a duplicated display line, a spurious key or value, or a line missing altogether —
  becomes a key or a value in the wrong position, which shifts every following pair by one until
  another malformed line cancels the shift. The mis-paired names never register, and the game
  shows the raw machine name. Two measured cases: the 2026-11-20 citycar check found 35
  duplicate lines that had mis-paired 820 consecutive entries; a single blank line added on
  2026-11-23 before `JaguarType01(VisionarySilver)` silenced all 144 objects of the 36 models
  appended in that commit, while a grep of the file found every key present.
  `[CODE New ex-15 @ f22a41c83]` `[CODE simutrans-extended ex-15 @ b914de7f4]`
  `[EXECUTION-VERIFIED:2026-11-20]` `[EXECUTION-VERIFIED:2026-11-23]`
- **Verify the loaded table, not the file.** Neither an even count of content lines nor a grep
  proves the table is sound: a comment line consumes one line, an identical pair consumes two and
  registers nothing, and a shifted pair still contains the key, as a value. Walk the file exactly
  as the reader does — two lines per entry from the start, skipping a line that begins with `#`,
  stripping trailing CR and LF — then assert that every `.dat` `name=` value is a stored key. At
  the 2026-11-23 fix all 1,911 citycar names resolved and none was missing.
  `[EXECUTION-VERIFIED:2026-11-23]`
- **Citycar display names use the public marketing name, not the internal generation code.**
  The 2017 additions established the pattern: `FordGalaxyMk1`/`Mk3` → `Ford Galaxy`,
  `FordMondeoMk1`/`Mk4` → `Ford Mondeo`, `NissanQashqai` → `Nissan Qashqai`. The 2026-11-21
  pass applied it to the whole fleet: `AudiA8D3` → `Audi A8`, `BMW5E39` → `BMW 5 Series`,
  `MercedesSClassW222` → `Mercedes-Benz S-Class`, `RangeRoverL405` → `Range Rover`,
  `Rover200R8` → `Rover 200`. The internal `name=` still distinguishes the generation; the
  display name does not. Every colourway of a model carries the same display name.
  `[USER-DIRECTION:2026-11-21]` `[EXECUTION-VERIFIED:2026-11-21]`
- All 1,911 citycar keys belong in the `City cars` section, in `citycars-models.csv` order,
  rather than scattered through later sections; the section also holds the two non-citycar
  road entries that historically lived there (`LondonTaxi-Lanchester`, `Volvo-V70-Police`). The
  144 keys appended on 2026-11-23 (`JaguarType01` to `VWPoloMk6`) sit at the end of the file,
  after the ferry texts, and remain to be moved into the section.
  `[EXECUTION-VERIFIED:2026-11-21]` `[EXECUTION-VERIFIED:2026-11-23]`
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
