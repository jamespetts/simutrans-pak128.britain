---
status: draft
verified: New ex-15 @ f60346f99 (working tree), 2026-11-27
---
# Stop waiting comfort

**Covers**: the three waiting-comfort fields on passenger-enabled `Obj=building` objects in
`New/stations/`: `maximum_comfortable_wait_minutes`, `maximum_tolerable_wait_minutes` and
`comfort_capacity`. It states what the fields mean, how they were calibrated, and the value for
every passenger-enabled stop, station building, extension, harbour and airport terminal. The
evidence and source records are in [stop-waiting-evidence](stop-waiting-evidence.md).
Parent: [comfort-calibration](../comfort-calibration.md).

## What the fields mean

- `maximum_comfortable_wait_minutes`: the longest wait, in minutes, that is fully comfortable.
  Below this value the engine charges the actual wait. Above it, the comfort curve adds perceived
  time, rising to the tolerable limit. The `_tenths` form is an alternative; specify only one.
- `maximum_tolerable_wait_minutes`: the hard limit. A journey requiring a longer **expected** wait
  at the stop is refused, and a passenger who actually waits longer than this at the stop is
  discarded.
- `comfort_capacity`: the number of waiting passengers to whom this building's comfort applies.
  `0` means unlimited. It is not the building's `capacity` field, which is its contribution to the
  halt's total station capacity.

Each field has its own default. If both time fields are omitted, the engine uses 180 minutes
comfortable and 540 minutes tolerable; a time value of 0 is treated as "not specified" and falls
back to those defaults. `comfort_capacity` is different: 0 is a real value meaning unlimited, not a
missing value.

The halt gathers every passenger-enabled building on its tiles and sorts them by
`maximum_comfortable_wait_minutes`, highest first. It assigns waiting passengers to each building
in that order. A building's `comfort_capacity` is the number of passengers that can receive its
comfortable value. If `comfort_capacity` is 0, the building has no limit: it takes every passenger
not already assigned to a better building. If every building has a finite capacity and all are
full, the passengers left over receive `max_comfortable_wait_overcrowded` (10 minutes in
`New/config/simuconf.tab`). The halt's effective comfortable and tolerable values are the
passenger-weighted averages of the assigned values.

The engine's expected wait is the mean of observed waits, or half the service interval when no
sample exists. A once-daily service therefore has a 720-minute expected wait and an actual wait
spread from zero to 1,440 minutes. The tolerable value must cover the actual wait if the service is
to keep all its passengers, not just the route.

## Method

1. **Comfortable is a property of the waiting environment.** It is set from the historical and
   modern facility ladders: an open stop is uncomfortable after about 10 minutes, a roof-only
   shelter after about 18, an enclosed unheated room after about 30, a heated room after about
   40-45, a large concourse after about 60, and an airport holdroom after 90-120.
2. **Tolerable is the maximum a passenger will endure.** It is the longest wait a passenger will
   accept before abandoning, rebooking, leaving or not travelling. It is set from the upper tail of
   observed and stated tolerance, not from the mean or 90th-percentile wait. Typical dwell at a
   major terminal is 19-24 minutes, but passengers have waited four to six hours during disruption
   and have slept overnight in terminals; the hard limit reflects the latter, not the former.
3. **Comfort capacity is a waiting-area count.** It is `round_to_5(k x station capacity)` using the
   factors in the capacity research: 0.4 for a shelter, 0.45-0.60 for a platform or through-station
   building, 0.70-0.78 for a harbour, 0.95-1.0 for a terminal or airport holdroom, and 0.20 for an
   entrance building. Open stops, open platforms and quays take `0` (unlimited).
4. **The base stop is the open-air condition; the building is the comfort layer.** When a waiting
   room fills, the surplus falls back to platform comfort.
5. **Planned and unplanned waits are different quantities.** The engine models the scheduled wait
   in the timetable, not a delay after a failure. Disruption evidence is used to bound what the
   facility can support, not to justify a scheduled wait of the same length.

The values are estimates, not measurements. Every number carries the evidence and confidence note
in [stop-waiting-evidence](stop-waiting-evidence.md).

## Facility ladder

| Amenity | Comfortable (min) | Maximum tolerated (min) |
| --- | --- | --- |
| Nameboard only, open to the sky | 10 | 120 roadside; 240 rail |
| Roof, no seat, no heat, no light | 18 | 240 roadside; 360 rail |
| Enclosed room, bench seats, unheated or poorly lit | 30 | 360 |
| Enclosed room, seats, fire, light, toilets | 40-45 | 720 |
| Great terminus: rooms by class, restaurant, hotel | 60-75 | 720-1,440 |
| Coaching inn: parlour, food, fire, beds | 75-90 | 1,440-2,160 |
| Harbour waiting room | 60 | 900-1,440 |
| Airport holdroom | 60-120 | 720-1,440 |

## Per-object values

`Capacity` is the existing station capacity in the `.dat`. `Comfort capacity` is the number of
waiting passengers who get the building's comfortable value; `0` means unlimited. All time values
are minutes.

### Early coaching, 1700-1844

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `StagingInn` | stop | 1700-1844 | 40 | 75 | 1,440 | 30 |
| `LargeInn` | extension | 1700-1844 | 120 | 90 | 2,160 | 80 |

### Open roadside stops

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `StagingPost` | stop | 1700-1852 | 10 | 10 | 120 | 0 |
| `staging-post-rail` | stop | 1807-1835 | 10 | 10 | 120 | 0 |
| `BusStop` | stop | 1820- | 12 | 10 | 120 | 0 |

### Roadside shelters

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `OldBusShelter` | stop | 1832-1950 | 25 | 15 | 240 | 10 |
| `OldBusShelterWmail1852` | stop | 1852-1874 | 25 | 15 | 240 | 10 |
| `OldBusShelterWmail` | stop | 1874-1950 | 25 | 15 | 240 | 10 |
| `ModernBusShelter` | stop | 1949- | 25 | 15 | 240 | 10 |

### Roadside terminals

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `OldBusTerminal` | stop | 1920-1952 | 85 | 30 | 360 | 60 |
| `ModernBusTerminal` | stop | 1952- | 100 | 30 | 360 | 80 |

### Open railway platforms

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `WoodenPlatformTrainStop` | stop | 1825-1960 | 0 | 10 | 240 | 0 |
| `BrickPlatformTrainStop` | stop | 1858-1957 | 0 | 10 | 240 | 0 |
| `BrickPlatformTrainStopNarrow` | stop | 1836- | 0 | 10 | 240 | 0 |
| `ConcretePlatformTrainStop` | stop | 1957- | 0 | 10 | 240 | 0 |
| `ConcretePlatformMaglevStop` | stop | 1960- | 0 | 10 | 240 | 0 |

### Covered platforms and overall roofs

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `woodenPlatformOverallTrainStop` | stop | 1825-1858 | 42 | 18 | 360 | 20 |
| `BrickPlatformOverallTrainStop` | stop | 1858-1957 | 48 | 18 | 360 | 30 |
| `BrickPlatformOverallTrainStopNarrow` | stop | 1849- | 35 | 18 | 360 | 20 |
| `ConcretePlatformOverallTrainStop` | stop | 1957- | 50 | 18 | 360 | 30 |
| `ConcretePlatformOverallMaglevStop` | stop | 1960- | 52 | 18 | 360 | 30 |

### Platform buildings and enclosed waiting rooms

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `BrickPlatformBuildingTrainStop` | stop | 1858-1957 | 30 | 30 | 360 | 15 |
| `BrickPlatformBuildingTrainStopNarrow` | stop | 1849- | 22 | 30 | 360 | 10 |
| `ConcretePlatformBuildingTrainStop` | stop | 1957- | 31 | 30 | 360 | 15 |
| `ConcretePlatformBuildingMaglevStop` | stop | 1960- | 36 | 30 | 360 | 20 |

### Underground platforms

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `LT_Station1_pc_1standard` | stop | 1890- | 8 | 10 | 120 | 0 |
| `LT_Station1_pc_2overpass` | stop | 1890- | 8 | 10 | 120 | 0 |
| `LT_Station1_pc_3levelpass` | stop | 1890- | 8 | 10 | 120 | 0 |

### Country and masonry station buildings

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `StationWoodBuilding` | extension | 1825-1958 | 50 | 30 | 360 | 25 |
| `StationStoneBuilding` | extension | 1825-1922 | 85 | 40 | 720 | 40 |
| `CountryStationBuilding` | extension | 1860-1960 | 75 | 35 | 720 | 40 |
| `ConcreteStationBuildingSmall` | extension | 1958- | 60 | 30 | 360 | 30 |

### Main-line urban and terminal-scale station buildings

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `DecoStationBuildingEntrance` | extension | 1922-1949 | 95 | 30 | 480 | 20 |
| `1950sStationBuilding` | extension | 1949-1977 | 115 | 30 | 480 | 60 |
| `1950sStationBuildingEntrance` | extension | 1949-1977 | 92 | 30 | 480 | 20 |
| `ModernStationBuilding` | extension | 1977- | 135 | 45 | 720 | 75 |
| `ModernStationBuildingEntrance` | extension | 1977- | 75 | 45 | 720 | 15 |

The large main-line buildings carry the terminal-scale values. Stacking them increases comfort
capacity but not the comfortable value; a separate object is only needed if the greatest termini
should exceed the 12-hour maximum.

### Underground station buildings

These are London Underground (metro) station buildings, not main-line terminals. Their waits are
short because the trains are frequent and the platforms are hot and crowded.

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `Yerkes-station-building` | extension | 1890-1932 | 125 | 25 | 120 | 65 |
| `art-deco-underground-station-building` | extension | 1932- | 140 | 25 | 120 | 75 |

### Harbour waiting buildings

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `HarbourPassengerOld` | habour | 1750-1922 | 85 | 60 | 1,440 | 60 |
| `HarbourPassengerDeco` | habour | 1922-1949 | 95 | 60 | 1,200 | 70 |
| `HarbourPassenger1950s` | habour | 1949-1977 | 115 | 60 | 1,080 | 85 |
| `HarbourPassengerModern` | habour | 1977- | 135 | 60 | 900 | 105 |

### Water stops and quays

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `OldPassengerQuay` | stop | 1750-1949 | 0 | 10 | 240 | 0 |
| `ModernPassengerQuay` | stop | 1949- | 0 | 10 | 240 | 0 |

### Airport terminals

| Object | Type | Intro-retire | Capacity | Comfortable | Maximum tolerated | Comfort capacity |
| --- | --- | --- | --- | --- | --- | --- |
| `DecoTerminalBuildingTower` | extension | 1909- | 95 | 60 | 720 | 90 |
| `DecoTerminalBuildingEntrance` | extension | 1922-1949 | 95 | 60 | 720 | 20 |
| `1950sTerminalBuilding` | extension | 1949-1977 | 115 | 75 | 1,080 | 110 |
| `1950sTerminalBuildingEntrance` | extension | 1949-1977 | 92 | 75 | 1,080 | 20 |
| `TerminalModernBuilding` | extension | 1977- | 135 | 120 | 1,440 | 130 |
| `TerminalModernBuildingEntrance` | extension | 1977- | 75 | 120 | 1,440 | 15 |

## Overflow setting

`New/config/simuconf.tab` sets `max_comfortable_wait_overcrowded = 10`. This is the same as the
open-platform comfortable value, so a passenger who cannot get into a shelter or waiting room is
treated as waiting in the open, not as being more comfortable than the people inside. The setting is
stored in savegames, so changing it affects existing games.

## Consequences

- Long waits are permitted but heavily penalised: the comfort curve adds up to 100 per cent of the
  actual wait at the tolerable limit.
- A daily service can produce a 1,440-minute actual wait. The coaching inn, old harbour and modern
  airport cover it; a 720-minute main-line station or a 480-minute 1950s station will discard the
  longest-waiting passengers. That is a service-frequency problem, not a reason to raise the
  tolerance beyond what a passenger will endure.
- The Underground buildings use short limits because their trains are frequent; they are not
  main-line terminals.

## Build note

The fields require a makeobj built from the current ex-15 source. The checked-in
`makeobj-extended` dated 23 November 2026 contained the key strings but silently dropped the fields;
a makeobj rebuilt from the current source writes them. The rebuilt binary is in
`New/makeobj-extended`. It is dynamically linked against the MSYS2 libpng and libstdc++ libraries,
so the build must run with `C:\msys64\mingw64\bin` on `PATH` (the MSYS2 build used here does).
Verify any new building field by compiling a test pak with and without it and comparing the
building node bytes, not by searching the executable for the key name.

## Open questions

- Should the greatest termini receive a 24-hour maximum? `StationStoneBuilding` currently uses 720
  minutes; 1,440 would cover a full overnight and a daily service, but would also allow a 24-hour
  planned wait at any large stone station.
- Should airport terminals use `comfort_capacity = 0` (unlimited)? The apron is not
  passenger-enabled, so the terminal is the only building on an airport halt; when its finite
  capacity is exceeded, the surplus receives the 10-minute overflow value, which is far below
  terminal comfort.
- Should a separate first-class or luxury waiting room exist? The engine gives one comfort value per
  building regardless of passenger class, so a class-specific lounge cannot be represented with the
  current fields.
- The engine under-prices short waits: below the comfortable limit, waiting costs 1.0 minute per
  minute, while UK evidence puts it at 1.5-2.5. This affects every stop and is outside the scope of
  this calibration.
