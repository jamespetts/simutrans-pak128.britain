---
status: draft
verified: New ex-15 @ fcd40c0bc + passes 64-65 (working tree), 2026-11-25
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

### Acquisition: the Shanghai transaction

The only transaction-level maglev vehicle price found is the Shanghai imported Transrapid car:
**more than RMB 100 million a car**, with 15 cars ordered. Two Chinese trade-press reports five
years apart give the same figure, the second stating that it includes the suppliers' development
cost. At the 2003 average of RMB 13.531 to GBP 1 that is GBP 7,390,579 a car, or **105,129 GBP a
car in 1900 money**. A Shanghai five-car set carries 464 seats (92.8 seats a car), so the price
is **1,133 GBP a seat** before the labour adjustment and **1,087.5 GBP a seat** after it. The
band is **761-1,133**: 761 is the 2010 domestic-build price at 30 per cent below the imported
car; 1,133 is the imported price before the labour adjustment. `[LITERATURE: *China Business
Times*, 18 May 2005, https://finance.sina.com.cn/chanjing/b/20050518/07101596819.shtml;
*Beijing Daily*, reprinted 9 April 2010, https://kunming.cn/news/c/2010-04-09/2122408.shtml]`

The Shanghai price is consistent with the German contract envelope: 15 cars at RMB 100m is
RMB 1.5bn, 30.6 per cent of the DM 1,293m equipment and services contract. It is a first batch
with development cost inside it, so the previous **Almujibah and Preston (2018)** estimate of
EUR 49,233 a seat (507.6 GBP in 1900 money) remains the **serial-production floor**. The choice
between 1,087.5 and 507.6 is a choice about production volume, not about which arithmetic is
right; the workbook applies the transaction figure and records the floor.

### Maintenance: the Almujibah rate stands

The maintenance figure remains **Almujibah and Preston (2018)**, Table 6, at 2009 prices:
**EUR 0.011 a seat-km**, converted to **0.00010257 GBP a seat-km** in 1900 money. It is an
estimate assembled from system costs, not an operator account; no operator account found in
research pass 55 separates maglev rolling-stock maintenance from infrastructure maintenance.
`[LITERATURE:https://doi.org/10.17816/transsyst201843s1298-327]`

The available evidence brackets the rate rather than displacing it:

- the Incheon Airport Maglev heavy-maintenance contracts (about KRW 3.8bn and KRW 5.77bn for four
  two-car sets) convert to **5,189 and 5,987 GBP a set-event**, or annualised 1,153 and 1,330 GBP
  a set-year. At Incheon's 57,332 train-km a set-year and 180 passengers a set that is
  **0.000112-0.000129 GBP a seat-km**, 1.1-1.3 times the current rate;
- the Shanghai 2026 spare-parts procurement budget is about **0.0000267 GBP a seat-km**, 26 per
  cent of the current rate, and covers parts only;
- a Korean work study puts maglev heavy-maintenance labour 23 per cent below heavy rail and 40
  per cent below light rail for comparable formations.

The current rate is therefore not generous, not below the parts cost, and consistent with the
lower labour requirement. Whether it includes heavy overhauls is not stated; if it excludes them,
the pakset under-charges by the annualised overhaul cost. `[Report
55](../cost-balancing/research-pricing-report-55.md).`

### The old acquisition estimate

The previous figure was **EUR 49,233 a seat** from Almujibah and Preston (2018), Table 6,
converted to 507.6 GBP a seat. The paper presents it as an estimated unit cost assembled from
system costs and does not publish the derivation of the per-seat rate. It remains the floor for a
serial-production reading, not the applied figure. `[LITERATURE:https://doi.org/10.17816/transsyst201843s1298-327]`

## The conversion

The workbook's `Index` sheet reproduces the engine's price series from `config/prices.tab`, with
1900 = 100; the series and their sources are explained in [prices-config](../prices-config.md).

| Step | Value | Basis |
|---|---|---|
| Exchange, acquisition | RMB 13.531 = GBP 1 | 2003 average; the Shanghai price is a 2003 price |
| Deflator, acquisition | 70.30 | workbook `Index` sheet, vehicle purchase, 2003 (7,030 per cent of 1900) |
| Exchange, maintenance | EUR 1 = GBP 0.89 | 2009 average; the Almujibah price is a 2009 price |
| Deflator, maintenance | 91.63 | workbook `Index` sheet, general, 2009 (9,163 per cent of 1900) |
| Labour adjustment | ×0.96 | Germany, the source country, at a 25 per cent labour share: [research-pricing-report-17](../cost-balancing/research-pricing-report-17.md) §5 |

Resulting figures, in 1900 money:

- purchase **1,087.5 GBP a seat** (band 761-1,133);
- maintenance **0.00010257 GBP a seat-km**;
- for stock with no seat count, applied per metre of car length on the 14 m, 54-seat reference
  car: **4,194.6 GBP a metre** and **0.00039563 GBP a metre-km**.

The maintenance cost is distance-driven in the source, so the whole figure is the per-km charge
and there is no fixed charge. Where a maglev vehicle has seats (`payload[1]`, the pakset's
passenger-capacity field), the seat rate applies. Where it has none — the RMU freight and tractor
units — the per-metre rate applies; that step is an extrapolation from passenger stock and is
tagged as one, because no overseas system runs freight maglev stock.

## Application

Applied in the two workbooks and the generator on 2026-11-25; the acquisition rate was re-based by
pass 65 on research pass 55. The maintenance rate was not changed. `[CODE New ex-15 working tree,
2026-11-25]`

| Object | Seats or length | Class purchase (GBP 1900) | Class per-km (GBP 1900) |
|---|---|---|---|
| RMU 9000 Class | 8 m, no seats | 33,557 | 0.003165 |
| RMU Aerocab | 10 m, no seats | 41,946 | 0.003956 |
| RMU Box Car / Flat Car | 16 m, no seats | 67,114 | 0.006330 |
| Ultraspeed M10 "Zephyr" (front/rear) | 54 seats | 58,725 | 0.005539 |
| Ultraspeed M30 "Platinum Jubilee" (centre) | 108 seats | 117,450 | 0.011077 |

Intermediate seat counts use the per-seat rate; the M10 centre (82 seats) is 89,175 and the M20
centre (81 seats) is 88,088. The full row-by-row values are in the class columns of the `Maglev
vehicles` sheets in both workbooks, with the conversion recorded in the row note.

## Open questions

- **Maintenance remains an estimate.** No operator account separates maglev rolling-stock
  maintenance from infrastructure. The routes are a Shanghai operator maintenance line, a
  Changsha 架修 (scheduled works overhaul) contract value, and an Incheon maintenance breakdown by
  asset class; [negative-findings](../cost-balancing/negative-findings.md) records them.
- **Acquisition is a first-batch price.** The Shanghai figure is a 15-car order with development
  cost inside it. A Changsha 2021 or Beijing S1 vehicle contract would test whether the 2.14
  factor is a development-cost effect; if a Chinese production price came out near 507.6, the
  serial-production reading would be vindicated.
- **The exchange rate and the labour factor are roundings.** The German factor of 0.96 is for
  construction labour at a 25 per cent labour share; a vehicle is more labour-intensive than a
  guideway, so the true factor may be higher.
- **No overseas system runs freight maglev stock**, so the per-metre application to the RMU
  freight and tractor units is an extrapolation. A Transrapid or Linimo car-structure price per
  metre would replace it.
- **The maintenance unit cost is per seat-km.** Whether it includes heavy overhauls and component
  exchange is not stated. If it excludes them, overhaul events would be additional; the workbook
  currently gives the maglev rows an overhaul provision of 15 per cent of A, event 1.2A every
  eight years, as the nearest analogue.
