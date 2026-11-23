---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Ship and boat crew complements

**Covers**: crew complements for every vehicle object in `New/boats/`, `New/boats/boats192/`,
`New/boats/boats224/` and `New/boats/holds/`, and the declarations made in the `.dat` files.

The complements are declared in three grades: `staff[7]` officer, `staff[8]` rating and `staff[9]`
catering. Over the 344 objects the declarations total 643 officers, 1,534 ratings and 676 catering
staff. See [../crew-complements](../crew-complements.md) for the role map and
[ships/register](ships/register.md) for the per-hull table.

## Scope and counting

- 124 `.dat` files across the four folders; 29 of them are pure hold files in `boats/holds/`.
- 344 vehicle objects: 153 powered marine objects in 86 classes, 51 unpowered towed craft in 12
  classes, 129 holds, 8 add-on mail holds, 2 horses and 1 towpath tractor.
- 98 manned classes; 205 objects carry crew, 204 sea-crewed and the towpath tractor at
  `driver[5]=1`.
- The 43 objects in `boats192/` and `boats224/` are additional vessels, not duplicates: no object
  name repeats across the folders. `[CODE New ex-15 working tree, 2026-11-23]`
- **101 hull classes are listed below.** Hovercraft and cargo variants of one craft are treated as
  one hull row because they are alternatives, not parts of one convoy.
- Crew range: **0 to 418**.

### How the hull was identified

The rule applied is the one in the brief: the hull is the object with `power` greater than zero,
or, for unpowered craft, the first object in the file. Four data patterns need a note.

1. **Alternative cargo fits with duplicated power.** In `clyde-puffer.dat`, `clan-line-steamer.dat`,
   `handysize.dat`, `humber-keel.dat`, `norfolk-wherry.dat`, `skiff-wherry.dat`,
   `thames-sailing-barge.dat`, `diesel-barge.dat`, `diesel-light-barge.dat`,
   `diesel-narrowboat.dat`, `semi-diesel-narrowboat.dat` and `steam-narrowboat.dat` every cargo
   variant carries the same `power` value. These are complete single-vehicle vessels, not hull
   plus hold: each has `Constraint[Prev][0]=none` and `Constraint[Next][0]=none`. A player buys
   one. The crew declared on the first variant must therefore be repeated on every variant, or
   the vessel will be free of crew when bought in another cargo fit.
2. **Holds with no power.** Everything in `boats/holds/` has `power=0` and must keep `crew` at
   zero. Several hold files also carry `engine_type=sail` with zero power (`carferry-holds.dat`,
   `blackwall-frigate-holds.dat`); the engine type is a copy artefact, not a propulsion plant.
3. **Horse units.** `BoatHorsesSingle` and `BoatHorsesFly` are horses, not vessels. A horse is
   not staff; the boatman belongs on the boat behind it. Both are recorded as 0.
4. **`towpath-tractor.dat`** is a tractor that pulls narrowboats from the towpath. It is in the
   water pak because of the way it is coupled, but its one occupant is a driver, not a seafarer.

### Confidence labels

Each row ends with the basis in square brackets. `measured` means a published complement for
that ship or a directly comparable ship. `rule` means a stated manning ratio applied to the
class. `estimate` means no source was found and the assumption is stated. Source keys `[S01]`
to `[S44]` are in the Sources section.

The pakset `weight` field is **not** a register tonnage: many unrelated vessels share the value
300, and light vessels carry 1. Tonnage rules below were applied to the real class tonnage, not
to the `.dat` field. The `.dat` `weight` should not be used to derive crew.

---

## 1. Declaration rules

- **Three grades.** Officer (`staff[7]`): master, mates, chief and assistant engineers, radio
  officer and ETO. Rating (`staff[8]`): bosun, carpenter, sailmaker, able and ordinary seamen, boys
  and apprentices, stokers, firemen, trimmers, greasers, donkeymen and deckhands. Catering
  (`staff[9]`): cooks, stewards, cabin attendants and hotel-services staff, including pursers.
- **Every manned vessel has at least one officer**, because the master or skipper is an officer.
- **Holds and unpowered attachments carry nothing.** The 129 holds, 8 add-on mail holds and 2
  horses are 0. The towpath tractor carries `driver[5]=1`, not a sea grade.
- **Cargo variants repeat the hull's crew.** The player buys one complete vessel in the chosen
  cargo fit, so a variant without the declaration would be crewless.
- **Dumb barges carry one bargee each.** A tug with six barges pays six bargees, although the tow
  was worked by one man on the lead barge. This is the largest approximation in the water fleet.

## 2. Group rules and worked examples

### Thames sailing barge - 2

Crew 2: skipper and mate. The spritsail rig is arranged to be handled by two. Larger
coasting barges added a boy, giving 3. Nothing scales with tonnage or cargo.

Worked example: `ThamesSailingBargeBulk` (1810, 75 t) = 2. The same figure applies to
`ThamesSailingBargeLong`, `Piece`, `Cool` and `Livestock`, which are alternative cargo fits of
the same barge [S06][S07][S08].

### Coastal sailing vessel - 3 + register tons/40

For vessels of 100-500 register tons in the coastal and home trades: master, mate, cook, and one
hand per 40 tons, minimum 3, maximum 12. Below 100 tons the crew does not fall below 2 and is
fixed by the trade, not the tonnage: 2 for a cargo keel or wherry, 4-7 for a fishing vessel.

Worked example: `BrigHull` (1700, 250 tons) = 3 + 6.25, rounded to 9 (master, mate, bosun, cook,
4 ABs, boy). Basis: Board of Trade returns give 4.17 men per 100 tons in 1854 falling to 2.90 in 1880
for all sail; the Transport Board required 5 men and a boy per 100 tons for transports and half
that for coasters, which gives upper and lower bounds for the 1 per 40 tons used here [S04][S05].

### Deep-sea sailing ship - set by rig, cross-checked by tonnage

- full-rigged ship or clipper: 28-35
- barque or windjammer: 25-30
- brig: 10-12
- East Indiaman: 100-120 (defence, passengers and cargo handling, not sailing)

Tonnage cross-check: 2.5-4.2 men per 100 register tons between 1854 and 1899 [S04].

Worked example: `ClipperHull` (1837, 963 tons) = 30. Cutty Sark, 963 GRT, is recorded at a
complement of 28-35 [S15]. `EastIndiamanHull` = 120, within the recorded 100-143 for the class.

### Canal narrowboat - 2 (single), 3 (motor and butty pair), 4 (fly boat)

A motor narrowboat carries a boatman and a mate: 2. A butty under tow contributes 1, so a
motor-and-butty pair totals 3. A fly boat, running day and night, carried a master and three men
on a single boat, or a captain and four men for a pair, that is 5 across the pair.

Worked example: `DieselNarrowboatBulk` (1920) = 2 [S10]. `CompositeHullUnpoweredNarrowboatBulk`
= 1. `FlyboatPiece` = 4 (master and three men), the 1844 single-boat scale [S11]. The wartime
motor-and-butty pair was worked by three women [S09].

### Dumb barge - 1 (2 for a wooden barge worked independently)

A dumb barge under tow needs one man at the helm: 1. A wooden 50 t barge of 1750 could be worked
independently under sail or quant, so it keeps 2. This is the weakest rule in the table: no
measured complement was found.

Worked example: `SteelHullDumbBargeBulk` (1930, 50 t) = 1. `WoodenHullDumbBargeBulk` (1750, 50 t)
= 2.

### Tug - 1 to 7

- canal pusher: 1
- small steam narrowboat tug: 3
- harbour or estuarial diesel tug: 5 (master, mate, engineer, 2 deckhands)
- steam tug: 6-7, adding firemen
- large ocean tug: 8-10

No measured tug complement was found; all six tug rows are estimates built from the watch
requirements in [S16]: navigation watch, engine watch, and mooring/unmooring.

Worked example: `IronSteamTug` (1841) = 7.

### Paddle steamer - 4 + passengers/100 + engine room

Historical paddle steamers needed a large engine room: 2-4 engineers and 2-10 firemen, depending
on the number of boilers, which is 4-14 engine staff. Passenger numbers add stewards at about one
per 100. The result runs from 6 for a 40-passenger pioneer to 25 for a 900-passenger coastal
steamer. The Channel paddle packets are higher at 35 because they carry two watches and a larger
engine room.

Worked example: `PSWaverley2` (1899, 900 passengers) = 25, taken from the preserved 1947
Waverley, an analogue of the same type and route, which carries 25-26 crew for up to 925
passengers [S34][S35][S36]. `PSComet` (1812, 40 passengers) = 6, an estimate.

### Coastal steamer - 12 to 45

Clyde, Channel and estuarial steamers of 1860-1935, by passenger certificate:

- 250-400 passengers: 12-18
- 800-900 passengers: 22-25
- 1,300-1,400 passengers: 40-45

Worked example: `TSSKingEdward` (1901, 1,286 passengers) = 40 (estimate). `ClydeSteamer` (1860,
300) = 14. The 25 crew of Waverley at 900 passengers is the measured figure nearest this band
[S36].

### Ocean liner - 1 per 26-45 GRT in the steam era

Early steam liners carried very large crews because of the coal-fired engine rooms and the
steward ratio. The three measured ships give 28 GRT per crew member (Great Western), 26
(Great Britain) and 45 (Great Eastern).

Worked example: `SSGreatEastern` (1858, 18,915 GRT) = 418, measured [S14]. `SSGreatWestern`
(1838, 1,700 GRT) = 60 [S12]. `SSGreatBritain` (1844, 3,443 GRT) = 130 [S13].

### Cross-Channel ferry - 45-105

Crew depends on the passenger certificate and the number of crews carried, not on tonnage:

- 1920s-1950s short-sea steamer, 1,000-1,300 passengers: 45-65
- 1970s-1980s car ferry, 1,400-2,300 passengers: 70-90
- 1990s-2020s Dover ferry, 2,000-2,300 passengers: 85-105

Worked example: `Pride of Kent` (30,635 GT, 2,000 passengers) had a manning of 102 [S23].
`Koningin Beatrix` (31,189 GT) carried 105 crew with 1,092 passengers [S20]. `Stena Europe`
(24,828 GT) carried 59, against a minimum safe manning of 21-24 [S21] - the range is wide because
operators run one, two or three crews.

### Car ferry - 80 for 5,590 GT, 85 for 14,760 GT

Short-sea car ferries of 1970-1990 are intermediate between the freight and passenger cases: a
deck crew for vehicle loading, a full catering crew, and two or three watches.

Worked example: `SealinkHorsa` (1972, 5,590 GT, 1,400 passengers) = 80 (peer: `Herald of Free
Enterprise`, 80 at the same passenger certificate). `Pride of
Hampshire` (1974, 14,760 GT) carried 85, with the breakdown master, 4 deck officers, 1 technical
officer, 11 deck ratings, 6 engineer officers, 5 engineer ratings and 57 hotel services staff
[S22]. `Herald of Free Enterprise` carried 80 [S24]. `Norsea` (1,250 passengers) carried 90
[S25].

### Ro-ro freight ferry - 22-25

No passenger service, so no catering or hotel department is carried: master, 3 mates, 4
engineers, ETO, bosun, 6-7 ABs, 5-6 engine ratings, cook, steward.

Worked example: `TTEuropeanFreight` (1975) = 22. `POSuperEuropeanFreight` (1991) = 25. Basis:
the ITF model ship of 23 posts, which is the full-handed cargo standard, and the SIRC dry-cargo
means of 21.6-22.4 for 20,000-99,999 gt [S17][S18].

### Container ship - 13-24

No pakset object. The rule is recorded for future objects: 13 on a 194,000 dwt vessel with
reduced manning, up to 24; the ITF full-handed model is 23 [S19][S17].

Worked example: `Madison Maersk`, 194,000 dwt, crew 13 [S19].

### Bulk carrier - 35 in 1958, 21-22 today

Before automation a 20,000 dwt bulk carrier carried about 35: master, 3 mates, 4 engineers, ETO,
bosun, carpenter, 12 ABs, 8 engine ratings, cook and stewards. By 2003 the mean for dry cargo of
20,000-49,999 gt was 21.8 [S18].

Worked example: `HandysizePiece` (1958, 20,000 dwt) = 35 (estimate). A 1999-built 4,748 dwt
dry cargo ship runs with 7-9 crew [S44].

### Tanker - 23-25

No pakset object. Tankers carry one more officer for cargo operations than a dry cargo ship of
the same size. Means: 22.7 for 10,000-19,999 gt, 23.6 for 20,000-49,999, 25.0 above 100,000
[S18]. The ITF model is 23 plus the tanker officer [S17].

Worked example: `Torm Ismini`, 228 m, 74,999 dwt, normally 19-23 crew [S44].

### Hydrofoil - 4-5

No pakset object. A Boeing 929 Jetfoil ran with 4-5: master, mate, 2 engineers and cabin staff.
This is an estimate; no source was retrieved.

Worked example: a 1990s 200-300 seat hydrofoil = 5.

### Catamaran fast ferry - 12 (74 m), 16 (96 m), 22 (112 m)

Crew scales with passenger capacity because of the cabin and evacuation requirement, over a fixed
bridge and engine team of about six: one additional crew member per 50-60 passengers.

Worked example: `Incat112m` (1,200 passengers) = 22, measured on Express 1 [S30]. Incat quotes
crew cabins for 14 on a 100 m craft and for 24 on a 110 m craft [S28][S29].
`HSS-1500` (1,500 passengers) = 33 [S26].

### Hovercraft - 3, 4 or 6

- SR.N6 and AP1-88: 3 (pilot, engineer, cabin)
- stretched AP1-88 and BHT: 4
- SR.N4: 6 (3 flight deck + 3 cabin)

Worked example: `SR-N4-Mountbatten-Mk3` (418 passengers) = 6. The control cabin carried a crew of
three - captain, first officer/flight engineer, second officer/navigator [S31]. SR.N6 is
documented at 3 [S32]; AP1-88 at 3, and the 28.5 m variant at 4 [S33].

### Fishing vessel - 5-7 in this pakset, 10-20 for trawlers

- sailing drifter or netter: 5-7
- near and middle water trawler: 10-14
- distant water trawler: 16-20
- modern inshore trawler under 15 m: 2-6

Worked example: `Fifie` (1852) = 7 (estimate). A 173 gt steam trawler carried 10 (skipper, mate,
bosun, 3 deckhands, 2 engineers, fireman, cook) [S39]; a 150-160 ft steam trawler carried nine
[S40]; a 615 gt stern trawler carried 16 [S38]; Grimsby deep-sea trawlers carried 10-14 near and
middle water and up to 20 distant water [S37]. A modern 208 gt beam trawler carried six:
skipper, mate and four deckhands [S42].

### Pleasure steamer - 20-26

Preserved excursion steamers carry a full certificate crew even at low passenger numbers:
master, chief officer, mates, chief engineer, engineers, firemen, deckhands, catering.

Worked example: `MVBalmoral` (1949, 500 passengers) = 20; the preserved Waverley carries 25-26
for up to 925 passengers [S35][S36]. About 50 seagoing crew are employed across the two ships
[S36].

---

Sources for every figure, and the rows that are estimates, are in
[ships/sources](ships/sources.md).
