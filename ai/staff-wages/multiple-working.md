---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Multiple working and consists

**Covers**: how the engine couples vehicles and convoys, what that means for crew charging, the
multiple-working codes and their integer allocation, the pakset changes that make two units
coupleable, and the engine limitations found.

Parent doc: [crew-complements](crew-complements.md).

## How a multiple-working formation is made

There is no engine object linking two convoys. A formation is always one `convoi_t` holding the
vehicles of what were two purchases. `[CODE simutrans-extended ex-15]`

- **In a depot** the player appends individual vehicles to the convoy being assembled. The depot
  GUI filters the list by the coupling rules; the command path itself does not re-check, and an
  invalid formation is refused only at departure, with "no cab at the front of the convoy" or a
  failed validity check.
- **At a stop** a schedule entry with the `couple` or `uncouple` flag exchanges vehicles between
  two convoys that are loading at the same halt. The engine solves for a valid arrangement and
  moves vehicles between the convoys, destroying any convoy left empty. Both convoys must be on the
  same waytype.

Coupling is permitted when the leading vehicle of one part lists the following vehicle's type in
its `Constraint[Next]` list, and the following vehicle lists the leading one in `Constraint[Prev]`.
`Constraint[...][0]=none` on its own means "nothing on this side", so it closes the end.

## What that means for crew

`convoi_t::get_salaries` is the only consumer of the crew fields.

- **Drivers.** The leading vehicle's drivers are always charged. Every other vehicle's drivers are
  charged when its `multiple_working_type` differs from the front vehicle's, and every vehicle's
  are charged when the front vehicle's type is 0.
- **Everyone else.** `staff_hundredths` is summed over every vehicle in the convoy with no
  multiple-working discount, then rounded up once.
- **Rounding.** The rounding is per staff type for the whole convoy, so 50 hundredths on each of two
  vehicles pays one person, and 50 on a single vehicle also pays one. The pakset does not use this
  for guards: a guard is a whole person on a brake vehicle, because a fractional declaration would
  make the charge depend on how many vehicles the player couples.

## The declarations

The pakset now encodes the real British coupling codes in `multiple_working_type`: one integer per
control system, shared by every class that could work in multiple with the others of that code.
The code table, the integer allocation, the class lists and the evidence are in
[multiple-working-codes](multiple-working-codes.md).

- **Locomotives** carry their class code where the class was fitted for multiple working: blue star
  (1), red circle (2), orange square (4), red diamond (5), white diamond (6) and yellow triangle (7).
  A class with no multiple working carries 0, so a double-header of two such locomotives pays two
  drivers. A double-header of two fitted locomotives of the same code pays one.
- **Multiple units** carry their code on every driving car, powered or a driving trailer, and on no
  intermediate motor car or trailer. A two-unit formation therefore pays one driver. The Southern
  27-wire stock (8), the first-generation DMU codes (blue square 9, yellow diamond 10, red triangle
  11, orange star 12, white circle 13), the HST pair (14), TDM stock (15), AAR (17), BSI (18),
  Scharfenberg (19) and the post-1970 families (32-73) each have their own integer.
- **Trams** use 16, separate from every rail code. The 25 articulated cars that work in multiple
  carry it; every other tram carries 0.

The engine still compares each vehicle only with the leading vehicle, so a formation of types X, Y
and Y pays three drivers, not two. That is why classes that could work together must share one
integer exactly; a per-class integer would overcharge the trailing unit.

`multiple_working_type` is compared only with the front vehicle's value. It has no effect on
coupling, physics or the save format, and it is included in the descriptor checksum.

## Pakset changes made

Twenty-one files had a closed cab end, which the engine reads as unconnectable. Each closed end now
names the unit's own opposite cab first and keeps `none` second, so two units of the class couple
with each other and the end still terminates a train. The affected classes are the Class 43 power
cars in the base livery and all ten livery variants, the Class 390, the Class 139, the Class 489
luggage van, the NER Tyneside petrol-electric railcar, the AEC and Leyland railbuses, and the GWR
Gloucester, Gloucester parcels, Park Royal and Swindon twin-set railcars.

The remaining 213 multiple-unit classes already listed each other's cab ends and needed no change.

The multiple-working codes were then replaced: the single number 1 gave way to the real coupling
codes for locomotives and units, and the trams moved from 2 to 16 so that no rail code collides with
them. The code table and the class lists are in
[multiple-working-codes](multiple-working-codes.md). The field was written on 424 objects and
cleared on seven railcars that had no multiple-working equipment.

## Engine shortcomings

These are engine defects or limitations, not pakset errors. They should be fixed in the engine
rather than worked around in the `.dat` files.

1. **Only the `drivers` map is shared; `staff` is charged per vehicle.** The guard, fireman,
   conductor and attendant are declared in `staff`, so a coupled formation pays each unit's crew in
   full. That is deliberate for the pakset: spreading a guard across a formation with
   `staff_hundredths` would make the charge depend on the number of carriages, so each brake
   vehicle is a separate guard's post.
2. **The rule is not "one crew per type".** A formation of types X, Y and Y pays three drivers, not
   two, because every vehicle whose type differs from the front vehicle's is charged.
3. **The type does not constrain coupling.** The field and the constraint lists can contradict
   each other with no diagnostic: two classes with different numbers couple and pay two drivers;
   two classes with the same number couple and pay one even if the pakset meant them to be
   incompatible.
4. **The front vehicle decides for the whole convoy.** There is no per-unit leading vehicle:
   `is_leading()` is true only for index 0. A driving trailer or driving van at the head must carry
   the same number as the powered cars or the discount is lost.
5. **No salary settlement when vehicles are exchanged.** Salaries are booked monthly from each
   convoy's own clock. A vehicle moved between convoys at a stop is charged by the receiving convoy
   for time the donor convoy had already run, and the layover exemption does not travel with the
   vehicle.
6. **A destroyed convoy never pays its final part-month.** `convoi_t::destroy()` does not book
   salaries, so a convoy sold or scrapped mid-month pays nothing for the elapsed part of that
   month.
7. **A new convoy's salary clock starts at tick 0.** `last_salary_point_ticks` is initialised to 0
   and not set to the current tick, so the first monthly booking of a convoy created after the
   world started may cover the whole elapsed world time. This needs a test game to confirm; if it
   reproduces, every new convoy overpays its first month.
8. **Crew data is not in the descriptor checksum.** The multiple-working type is, the staff maps
   are not (there is a TODO in `vehicle_desc.cc`). Two network peers with different crew
   complements are not detected as mismatched.
9. **Depot coupling checks are GUI-only.** The command path accepts a formation the GUI would
   refuse and only departure rejects it.

## Open questions

- ~~Should the pakset give each multiple-unit class its own multiple-working number?~~ Resolved
  2026-11-23: the pakset uses the real coupling codes, with one integer per compatible group; see
  [multiple-working-codes](multiple-working-codes.md). The remaining question is whether the
  post-1970 block should be collapsed, because those groups are builder families rather than
  documented compatibility.
- Is the tick-0 salary-clock behaviour observable in a test game with a convoy bought in 1900 and
  run for two months?
