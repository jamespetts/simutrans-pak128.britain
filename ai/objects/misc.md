---
status: stub
verified: none
---
# Miscellaneous objects (`misc`)

**Covers**: `Obj=misc` objects.

## Initial facts

- `Obj=misc` is used for the sidewalk (`New/ways/pavement.dat`, `Name=Sidewalk`) and for power
  lines (`New/ways/Powerlines.dat`, `Name=PowerSource` and `PowerDest`, `waytype=power`).
  `[CODE New master @ e36ec2321]`
- `PowerSource` and `PowerDest` carry no `cost` or `maintenance` field; they are the visual
  endpoints of a power line. The purchasable substation is the engine's transformer, priced by
  `cost_transformer` and `cost_maintain_transformer` in `simuconf.tab`, and represents one 132 kV
  grid supply point at each power station and town. `[CODE New ex-15 working tree, 2026-11-24]`
- `misc` is also used for UI images in `New/gui/`; see [ui](ui.md).
  `[CODE New master @ e36ec2321]`

## Planned sections

- The range of uses of the `misc` object type.
- Sidewalks and power lines.

## Open questions

- What does `Obj=misc` mean in the engine, and which uses are intended for paksets?
- The display names in `New/text/en.tab` still read "Distribution substation" and "Local
  substation". Under the grid-scale model the substation is a 132 kV grid supply point, so both
  names need review.
