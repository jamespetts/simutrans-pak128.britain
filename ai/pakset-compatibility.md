---
status: draft
verified: New master @ 4fffcc19e
---
# Pakset compatibility

**Covers**: how changes to pakset `.dat` values interact with savegames and network
compatibility, and the restrictions on changing them.

## Notes

- AGENTS.md hard rule 9: do not change `.dat` fields, object capacities, constraints, or other
  save/load-relevant values in a way that breaks savegame or network compatibility without first
  reading the relevant docs and presenting the intended change to the user.
- The engine is the authority on which fields are save-relevant; this project must determine
  that from the engine source rather than assume it. `[UNVERIFIED]`

## Rename and replacement mechanism (`compat.tab`)

- `New/compat.tab` lists obsolete object names and their replacements. The file header states
  that an obsolete object is replaced by the object named in the next line. Each entry is an
  ordered pair: one obsolete `name=` value, followed by its replacement `name=` value.
  `[CODE New master @ 4fffcc19e]`
- Object identity uses the lowercase `name=` field in each `.dat` file. Example:
  `New/trains/4wheel-1850s-brake.dat` declares `name=4-wheel-1850s-brake`.
  `[CODE New master @ 4fffcc19e]`
- `compat.tab` is copied to the pakset root and used directly, not compiled; build handling is
  recorded in [build-and-toolchain](build-and-toolchain.md). `[CODE New master @ 4fffcc19e]`
- Procedure: when renaming, retiring, or replacing an object, append the obsolete `name=` value
  followed by the replacement `name=` value. `[CODE New master @ 4fffcc19e]`
- Scope limit: `compat.tab` contains name pairs only. It contains no capacity, constraint, price,
  or intro/retire date logic; value changes are outside its scope.
  `[CODE New master @ 4fffcc19e]`

## Planned sections

- Which `.dat` fields and value changes are save/load-relevant and which are not.
- How existing savegames reference pakset objects (by name, index, or other key).
- Safe procedures for retiring, renaming, or replacing objects.

## Open questions

- Which engine files define savegame compatibility for pakset objects, and how should docs point
  to them?
- What is the safe procedure for changing an object's capacity or constraints without breaking
  existing games?
- What is the exact list of save/load-relevant `.dat` fields (as opposed to display-only
  fields)? Unresearched; do not assume.
