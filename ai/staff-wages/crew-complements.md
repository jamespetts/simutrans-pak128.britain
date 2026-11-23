---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Vehicle crew complements

**Covers**: the `driver[n]`, `staff[n]`, `staff_hundredths[n]` and `multiple_working_type`
declarations in the vehicle `.dat` files under `New/`, the rules used to assign them, and what
the engine does with them. Wages themselves are in [../staff-wages](../staff-wages.md); the
charging path is described in [../vehicle-cost-model](../vehicle-cost-model.md).

Read with [../vehicle-cost-model](../vehicle-cost-model.md) (how `fixed_cost` and `runningcost`
are charged), [../staff-wages](../staff-wages.md) (the rates),
[multiple-working](multiple-working.md) (coupling and consists), [bus-conductors](bus-conductors.md)
(the road conductor dates) and [driver-only-operation](driver-only-operation.md) (which multiple
units carry a guard).

## Role map

The staff types are defined by `config/staff.tab` and are read by the engine as indices 0-254.

| Type | Grade in `staff.tab` | Declared as | Charged on |
|---:|---|---|---|
| 0 | Train/engine driver | `driver[0]=1` | locomotive, railcar, multiple-unit driving car, tram engine (not trams, see 5) |
| 1 | Fireman | `staff[1]=1` | steam locomotive only |
| 2 | Guard | `staff[2]=1` | brake carriage, brake van, one car of a guarded multiple unit |
| 3 | Carriage attendant | `staff[3]=n` | dining, kitchen, buffet, Pullman and TPO vehicles |
| 4 | General labourer | not used | station and goods handling is a building cost |
| 5 | Tram/bus driver | `driver[5]=1` | bus, tram, trolleybus, lorry, van, horse omnibus |
| 6 | Tram/bus conductor | `staff[6]=1` | bus or tram before one-person operation; DLR train captain |

`[USER-DIRECTION:2026-11-23]` confirmed these placements: one driver and one fireman on each
steam locomotive except steam tram locomotives, which have no fireman; the guard travels in the
rear guard's carriage and not in the locomotive; on a multiple unit the guard is in the car whose
code contains "B" (for example DMBS) and, where no car is so marked, in the rear cab.

## Engine mechanics

Verified against the ex-15 engine source. `[CODE simutrans-extended ex-15]`

- `driver[n]` and `staff[n]` declare whole persons; `staff_hundredths[n]` declares hundredths of a
  person. `staff[n]` and `staff_hundredths[n]` write the same map, so declaring both for one index
  is a mistake.
- `convoi_t::get_salaries` (`simconvoi.cc`) runs per staff type and per convoy. It sums
  `staff_hundredths` over every vehicle and rounds that total up **once**; it sums `drivers` over
  the leading vehicle and, when the front vehicle's `multiple_working_type` is non-zero, over every
  vehicle whose type differs from it, and over every vehicle when the front's type is 0.
- The salary is `staff.tab` rate for the game month × the count × the fraction of the month,
  passed through `calc_adjusted_monthly_figure`. No salary is charged while the convoy is laid
  over, in a depot, under maintenance or under overhaul.
- `multiple_working_type` is read by no other engine code: it does not affect coupling, physics or
  the save format. It is in the descriptor checksum; the staff maps are not.

## What is declared

`[CODE New ex-15 working tree, 2026-11-23]` Declarations are in 1,244 `.dat` files, on 2,048 of the
3,788 vehicle objects; 407 objects carry a multiple-working type. Totals by role:

| Role | Objects | Where |
|---|---:|---|
| `driver[0]` | 840 | 381 steam locomotives, 77 diesel and electric locomotives, 382 multiple-unit driving cars and unpowered driving trailers |
| `staff[1]` | 381 | steam locomotives |
| `staff[2]` | 532 | 362 brake carriages, 19 brake vans, 129 multiple units, 22 coaches |
| `staff[3]` | 122 | 78 catering cars, 27 TPOs, 17 Pullman parlour cars |
| `driver[5]` | 692 | 343 buses, 283 lorries and vans, 60 tram cars, 6 pre-1900 tramcars |
| `staff[6]` | 281 | 238 bus conductors, 34 tram conductors, 6 pre-1900 tramcars, 3 DLR train captains |

Tenders, wagons, mail coaches, trailers of all kinds, horses and maglev cars carry no crew.

## Rules applied

### Rail locomotives

- Steam: `driver[0]=1` and `staff[1]=1` on every steam locomotive and steam tram locomotive; the
  steam tram locomotive omits the fireman. `[USER-DIRECTION:2026-11-23]` The game has no fatigue
  model, so two-man firing is not modelled and no class gets a second fireman.
- Diesel and electric: `driver[0]=1`.
- Tenders carry nothing. The driver is charged once because the leading vehicle is the locomotive.

### Rail multiple units

- `driver[0]=1` on each driving car (a car with a closed end, that is a cab). Not on intermediate
  motor cars, which have no controls, and not on trailers.
- `multiple_working_type=1` on each driving car. This is the only field the engine shares across a
  coupled formation, so it is what makes a two-unit train pay one driver. Trailer cars declare
  neither a driver nor a type: they contribute no drivers, and a type would be meaningless on a
  vehicle that does not work in multiple.
- The guard is declared `staff[2]=1` on one car per unit: the B-coded car where the class has one,
  otherwise a rear driving car.
- No guard on classes introduced for driver-only operation. The rule and its class lists are in
  [driver-only-operation](driver-only-operation.md).

### Passenger coaches, brake vehicles and vans

- Brake carriage or brake van: `staff[2]=1`, one whole person. The guard is never split across the
  formation: the crew cost of a train must not change with the number of carriages the player
  couples, so each brake vehicle is a separate guard's post and a train with two of them pays two
  guards. `[USER-DIRECTION:2026-11-23]` The same reasoning rules out `staff_hundredths` here, which
  would make the charge depend on how many vehicles happened to be in the convoy.
- The per-vehicle rule is exactly right for the earliest stock. Before continuous brakes every
  brake vehicle was worked by its own brakesman, because the brakes were applied by hand on each
  vehicle, so a train with two brake vehicles did carry two men. Continuous brakes removed that
  need and one guard per train became enough, so the declaration is exact before the 1890s and
  slightly high afterwards for a train that happens to carry two brake vehicles.
  `[USER-DIRECTION:2026-11-23]`
- Ordinary coaches, mail coaches and wagons: nothing.

### Catering and mail

- Dining, restaurant and kitchen cars: `staff[3]=3`. The anchor is the measured 1896 LNWR 56 ft
  dining car, staffed by one cook, one attendant and one page for £195 a year, £65 each
  ([../staff-wages/evidence-1914-1946](../staff-wages/evidence-1914-1946.md) section 6).
- Buffet and miniature buffet cars: `staff[3]=1`; a restaurant buffet with a kitchen: 2.
- Pullman parlour cars: `staff[3]=1` each.
- TPO: `staff[3]=3`, matching the sorting staff already declared on the 1870s TPO.

### Buses

`driver[5]=1` on every bus. The conductor rule is in [bus-conductors](bus-conductors.md): no
conductor on vehicles of 12 seats or fewer; a conductor before 1931 above that; from the 1931
regulations a conductor above 26 seats until 1968; none from 1968; the Routemaster family keeps its
conductor for its whole life.

### Lorries, vans and carts

`driver[5]=1` on every powered goods vehicle and on every non-trailer drawn vehicle. Trailers,
semi-trailers and dollies carry nothing, so a lorry and trailer pays one driver.

### Trams

`driver[5]=1` on each powered tram car, with `multiple_working_type=2` on those cars that can
couple to another powered car, so that a multi-car tram pays one driver. One conductor,
`staff[6]=1`, on sets built before one-person working. Modern trams are driver only; Sheffield
Supertram keeps a conductor; the Blackpool Centenary and Millennium cars are driver only from 1984.
Trams are handled apart from rail because their driver is grade 5 and their conductor grade 6.

Every electric tramcar before 1992 is closed at both ends in its own constraints and therefore ran
singly: 34 of the 60 electric tram cars in `New/trams/`, covering the London County Council,
Glasgow, Sheffield, Leeds and Blackpool fleets up to the 1984 Centenary cars. Each carries
`Constraint[Prev][0]=none` and `Constraint[Next][0]=none` as single entries, which makeobj turns
into `unconnectable`, so they take no multiple-working type. The one pre-1992 exception is the
Blackpool Progress Twin power car of 1958, which couples to its own trailer; it is the only
powered car in its set, so it takes no type either. The articulated light-rail cars from 1992
onward — Metrolink T86, Sheffield Supertram, Midland Metro T69, then Croydon, Edinburgh, NET,
Blackpool's Flexity and the Vossloh tram-train — are the only cars that carry
`multiple_working_type=2`. `[USER-DIRECTION:2026-11-23]`
`[CODE New ex-15 working tree, 2026-11-23]`

The pre-1900 tramcars are the one case where a vehicle that does not work in multiple carries a
driver. A tramcar of that generation is drawn either by horses or by a steam tram engine, and
neither the horse nor the engine declares a crew, so the driver and the conductor are both
declared on the car: `driver[5]=1` and `staff[6]=1`, and no multiple-working type, because a
tramcar never works in multiple. That is also why the type is not needed there: in Britain a steam
tram locomotive was permitted to draw only one trailer, so a set is one engine and one car and
there is never a second driver to suppress. `[USER-DIRECTION:2026-11-23]`

### DLR

`staff[6]=1` on one car per unit and no driver: the train captain is the only crew member and is
priced at the conductor rate. `[USER-DIRECTION:2026-11-23]`

## Multiple working

Two units couple when each cab end lists the other in its `Constraint` list. Most of the pakset
already does this. Twenty units had both ends closed with a single `Constraint[...][0]=none`, which
the engine reads as "unconnectable"; those ends now name the unit's own opposite cab and keep
`none` as the second entry, so two units of the class can couple and the end still terminates a
train. The mechanism, the engine defects and the remaining gaps are in
[multiple-working](multiple-working.md).

## Not yet declared

- **Ships and aircraft.** The complements are researched and tabulated per hull and per airframe
  ([ships](crew-complements/ships.md), [aircraft](crew-complements/aircraft.md)), but no declaration
  is made, because `config/staff.tab` has no sea or air grade and the pakset rule is that every
  wage names a source. The measured anchors that a new grade would use are the 1912 able-seaman
  rate of 100s a month and the 2019 and 2026 ASHE means for ship and hovercraft officers and for
  aircraft pilots; the ratings and cabin-crew grades have no measured long series.
- **Buildings cannot declare staff at all.** `staff.tab` is charged only through
  `convoi_t::get_salaries`, so station, depot, signalbox and goods staff cannot be charged. This is
  an open question, not a defect to fix in the pakset. `[CODE simutrans-extended ex-15]`
- **Declarations are static for the life of a vehicle.** A bus built in 1955 and withdrawn in 1975
  declares one complement for both ends of that life, because `.dat` crew cannot vary with the game
  date. This is the largest approximation in the scheme.

## Open questions

- Should the guard be charged on the locomotive as well, so that every train pays a guard whether
  or not it has a brake vehicle?
- Are there classes documented as two-man fired that should get `staff[1]=2`?
- Should the maglev cars carry a crew? They are declared driverless on the assumption that the
  pakset's maglevs are automated.
