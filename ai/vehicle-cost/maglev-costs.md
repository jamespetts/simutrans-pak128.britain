---
status: draft
verified: New ex-15 @ working tree, 2026-11-25
---
# Maglev vehicle costs

**Covers**: the price and maintenance figures for the pakset's maglev vehicles
(`New/maglev/*.dat`), the rule that governs where those figures come from, and the overseas
evidence they are drawn from. Read before setting or checking any maglev vehicle `cost`,
`runningcost` or `fixed_cost`, and before changing the maglev rows of the two cost-balancing
workbooks (`New/cost-balancing-capital.xlsx` and `New/cost-balancing-maintenance.xlsx`).

## The rule

**There are no mainline maglevs in the United Kingdom. Maglev prices therefore come from the
costs of overseas maglev systems, adjusted for differing labour costs.** `[USER-DIRECTION:2026-11-25]`

This direction was restated on 2026-11-25 with the instruction that it be recorded so that it
cannot be lost again; the user records having given it in earlier sessions, and no dated record
of those earlier statements survives in this knowledge base. It binds every maglev price: the
purchase price (`cost`), the continuous maintenance figures (`runningcost` per vehicle-km and
`fixed_cost` per vehicle-month) and the overhaul and upgrade figures if any are later added. The
fields and what the engine charges for each are explained in
[vehicle-cost-model](../vehicle-cost-model.md). It is not a preference for one research route
over another; it is the only route, because British maglev evidence does not exist.

The same rule applies in the generator: `MAGLEV_CAP_PER_SEAT`, `MAGLEV_MAINT_SEAT_KM` and the
per-metre equivalents in `New/ai/cost-balancing/evidence_data.py`, with the branch at
`cls == 'maglev-vehicles'` in `extrapolation()`. A rebuild reproduces the workbook figures below.
`[CODE New ex-15 working tree, 2026-11-25]`

## The evidence

The unit costs are those of **Almujibah and Preston (2018)**, Table 6, at 2009 prices. The paper
assembles them from the published costs of the Shanghai Transrapid, the Linimo (Nagoya), the
Incheon Airport and the Changsha systems. `[LITERATURE:https://doi.org/10.17816/transsyst201843s1298-327]`
H. Almujibah and J. Preston, "The total social costs of constructing and operating a maglev line
using a case study of the Riyadh-Dammam corridor, Saudi Arabia", *Transportation Systems and
Technology* 4(3 suppl. 1), 2018, pp. 298-327.

| Element | Rate | Grade | What the source says |
|---|---|---|---|
| Acquisition | EUR 49,233 a seat | ESTIMATE built from system costs | "The unit cost of acquiring a Transrapid" |
| Rolling-stock maintenance | EUR 0.011 a seat-km | ESTIMATE built from system costs | "Average unit cost of maintaining a Maglev trainset"; a distance-driven unit cost |

The same paper's guideway figures are already used in
[research-pricing-report-17](../cost-balancing/research-pricing-report-17.md) §7, so the two
maglev evidence routes now share one source.

**Cross-checks on the acquisition rate.** A 438-seat five-car Transrapid train costs
EUR 21.6m at this rate. The Shanghai project's German equipment and services contract was
DM 1,293m for three five-car trains, the operation control system, the propulsion and power
supply, the stator packs and the winding cables (report 17 §2); vehicles at EUR 21.6m a train are
EUR 65m of that total, a plausible share. The Emsland test facility budgeted about DM 60m for one
test vehicle (report 17 §2), roughly EUR 30m — a test vehicle, not a production car, so the
direction is right and the size is not comparable.

**Cross-check on the maintenance rate.** The pakset's Ultra 450 front car carried a `fixed_cost`
of 18,500 `.dat` (555 GBP a year in 1900 money at the workbook's conversion). At 100,000 km a year
the overseas rate for its 54 seats gives 554 GBP a year. The two agree within 0.2 per cent, which
is a useful confirmation that the existing pakset level was not absurd and that the overseas rate
is of the right order. `[CODE New ex-15 working tree, 2026-11-25]`

## The conversion

The workbook's `Index` sheet reproduces the engine's price series from `config/prices.tab`, with
1900 = 100; the series and their sources are explained in [prices-config](../prices-config.md).

| Step | Value | Basis |
|---|---|---|
| Exchange | EUR 1 = GBP 0.89 | 2009 average; the source prices are 2009 prices |
| Deflator, acquisition | 82.87 | workbook `Index` sheet, vehicle purchase, 2009 (8,287 per cent of 1900) |
| Deflator, maintenance | 91.63 | workbook `Index` sheet, general, 2009 (9,163 per cent of 1900) |
| Labour adjustment | ×0.96 | Germany, the source country, at a 25 per cent labour share: [research-pricing-report-17](../cost-balancing/research-pricing-report-17.md) §5 |

Resulting figures, in 1900 money:

- purchase **507.6 GBP a seat**;
- maintenance **0.00010257 GBP a seat-km**;
- for stock with no seat count, applied per metre of car length on the 14 m, 54-seat reference
  car: **1,957.7 GBP a metre** and **0.00039563 GBP a metre-km**.

The maintenance cost is distance-driven in the source, so the whole figure is the per-km charge
and there is no fixed charge. Where a maglev vehicle has seats (`payload[1]`, the pakset's
passenger-capacity field), the seat rate applies. Where it has none — the RMU freight and tractor
units — the per-metre rate applies; that step is an extrapolation from passenger stock and is
tagged as one, because no overseas system runs freight maglev stock.

## Application

Applied in the two workbooks and the generator on 2026-11-25, replacing the diesel/electric
locomotive ladder for capital and the Hill 1895 steam locomotive figure (253 GBP an engine-year)
for maintenance. The Hill figure had been applied to every maglev vehicle because maglev fell
through the rail branch of the generator; it is not evidence for a maglev and the workbook's own
status column already said the class had no data. `[CODE New ex-15 working tree, 2026-11-25]`

| Object | Seats or length | Class purchase (GBP 1900) | Class per-km (GBP 1900) |
|---|---|---|---|
| RMU 9000 Class | 8 m, no seats | 15,663 | 0.003165 |
| RMU Aerocab | 10 m, no seats | 19,579 | 0.003956 |
| RMU Box Car / Flat Car | 16 m, no seats | 31,326 | 0.006330 |
| Ultraspeed M10 "Zephyr" (front/rear) | 54 seats | 27,410 | 0.005539 |
| Ultraspeed M30 "Platinum Jubilee" (centre) | 108 seats | 54,821 | 0.011077 |

The full row-by-row values are in the class columns of the `Maglev vehicles` sheets in both
workbooks, with the conversion recorded in the row note.

## Open questions

- Are the Almujibah and Preston unit costs measured or modelled? They are presented as estimated
  unit costs assembled from system data, not as operator accounts. An operator account (Aichi
  Rapid Transit's rolling-stock maintenance line, or Shanghai Maglev Transportation's) would
  replace them with a measurement.
- The exchange rate and the labour factor are roundings. The German factor of 0.96 is for
  construction labour at a 25 per cent labour share; a vehicle is more labour-intensive than a
  guideway, so the true factor may be higher.
- No overseas system runs freight maglev stock, so the per-metre application to the RMU freight
  and tractor units is an extrapolation. A Transrapid or Linimo car-structure price per metre
  would replace it.
- The maintenance unit cost is per seat-km. Whether it includes heavy overhauls and component
  exchange is not stated. If it excludes them, overhaul events would be additional; the pakset
  currently has no maglev overhaul rows.
