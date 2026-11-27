---
status: stub
verified: none
---
# Public buildings

**Covers**: `Obj=building` objects placed by the player or the world rather than grown as city
buildings: stops and stations, station extensions, depots, signalboxes, attractions, monuments,
harbours, and headquarters.

## Initial facts

- `type=` values present in this group: `stop` (stops and stations), `extension` (station
  extensions), `depot`, `signalbox`, `cur` and `mon` (attractions and monuments), `habour`, and
  `hq`. `[CODE New master @ e36ec2321]`
- Source folders include `New/stations/`, `New/depots/`, `New/signalboxes/`, `New/attractions/`,
  and `New/hq/`. `[CODE New master @ e36ec2321]`
- Passenger-enabled stop and station-extension buildings carry the waiting-comfort fields
  `maximum_comfortable_wait_minutes`, `maximum_tolerable_wait_minutes` and `comfort_capacity`.
  Method, values and evidence: [stop-waiting](../../comfort/stop-waiting.md).

## Planned sections

- Stops and stations: how station buildings, platforms, and extensions combine.
- Depots and signalboxes.
- Attractions and monuments.
- Harbours and headquarters.
- Player-building and timeline fields.

## Open questions

- How do station `extension` buildings attach to stops in Simutrans-Extended?
- Should signalboxes move to the signals/signs area rather than public buildings?
