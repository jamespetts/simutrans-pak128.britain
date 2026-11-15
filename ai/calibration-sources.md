---
status: draft
verified: New ex-15 @ 0a4be8077 (working tree)
---
# Calibration sources

**Covers**: how the sources of historical calibration data are recorded, and the registry of
datasets behind the year-indexed price and wage files (`config/prices.tab`, `fuel.tab`,
`staff.tab`) and historically calibrated `.dat` values.

## Rule

- Every number derived from historical data must name its source. This applies to
  `config/prices.tab`, `fuel.tab`, `staff.tab`, and to `.dat` values calibrated against
  historical prices. `[USER-DIRECTION:2026-11-15]`
- Record the source where the number lives: the header comment of the file that contains the
  series names the source, the base year and every transformation applied.
  `[USER-DIRECTION:2026-11-15]`
- Record the dataset here too when it is used in more than one file, when the file header is
  too short to carry the detail, or when a series is spliced from several sources.
- In knowledge-base prose, cite the source with `[LITERATURE:<url>]` ([claim-tags](claim-tags.md)).
- A number with no recorded source is not calibrated data. Treat it as an estimate and label
  it as one.
- A search result is not a source. Fetch and read the page or dataset before entering a
  number.

## What a source record contains

- Title and publisher.
- URL or full citation.
- Series identifier where one exists (for example an ONS series code).
- Years covered, and the base year of any index.
- Unit, and what the series measures: a nominal price, a cost index, a tender price index,
  and so on.
- Transformations: rebasing, deflation, unit conversion, interpolation, chain-linking.
- Known limitations: basis changes, coverage gaps, quality change, regional scope.
- The date the source was consulted.

For a spliced series, record every component and the overlap year used for the link. For a
derived number, record the formula and each input. Label projections and estimates separately
from observed values.

## Registry

| Series | Measures | Sources | Coverage | Config use |
|---|---|---|---|---|
| General consumer prices | UK price level | officialdata.org UK inflation (RPI-linked before 1988, CPI after) | 1750-2026 | `general` |
| Rail fares | UK rail fares | ONS series DOCW (Jan 1987 = 100) | 1987-2026, linked to earlier fare anchors | `passenger fare` |
| Postage | Inland letter rate | GBPS rate tables; Postal Museum; Hansard 1925 | 1750-2026 | `mail rate` |
| Coal | English coal price | Publisher not recorded in `fuel.tab`; the file says only "English coal prices" | 1750-2026 | `fuel[steam]` |
| Road fuel | Petrol and diesel pump prices | DESNZ annual average road fuel prices | 1900-2026 | `fuel[petrol]`, `fuel[diesel]` |
| Electricity | Non-domestic electricity price | DESNZ QEP table 3.4.1, excluding CCL | 1900-2026 | `fuel[electric]` |
| Jet fuel | Jet fuel price | EUROCONTROL/IATA (Platts) | 1900-2026 | `fuel[turbine]` |
| Wages | Average and occupational earnings | ONS AWE series a3wx; measuringworth | 1750-2026 | `staff[*]` |
| Corporation tax | UK main rate | GOV.UK rates and allowances | 1798-2023 | `corporation tax` |
| Bank Rate | Bank of England policy rate | Bank of England Bank Rate history | 1750-2025 | `base rate` |
| Building construction | Nominal price of building work | Mitchell, *British Historical Statistics* (1988) Ch VII Table 8, building costs (1930=100), 1845-1938; Holmans, *Historical Statistics of Housing in Britain*, Table M.10, construction costs (1958-60=100), 1939-1970, with 1940-1947 from Mitchell and Deane, *Abstract of British Historical Statistics* (1962) Ch IX Table 4; BIS output price index, all new construction, 1955-2013; ONS construction output price index, all new work, 2014-2026. The first two are taken from the Bank of England "A millennium of macroeconomic data" workbook, sheet A32, columns S and T. Before 1845 the 1845 real level is held and tracks the general index (backcast tested against a wage-based alternative; see [prices-config](prices-config.md)) | 1845-2026, backcast to 1750 | `buildings` |
| Civil engineering | Infrastructure construction prices | BCIS civil engineering index; ONS output price indices, infrastructure; Department of the Environment road tender indices | 1980-2026 for the infrastructure OPI; earlier under research | `infrastructure` (planned) |
| Farmland | England agricultural land price | Savills long-run England farmland series, all land types (real, rebased to 2023) | 1900-2024 | `country land` |
| Urban land | UK residential land price | JST Macrohistory Database UK nominal house price index (1900-1995 proxy); ONS land underlying dwellings, AN.21111 (1995-2025) | 1899-2025 | `city land` |
| Vehicles | Purchase prices of transport equipment | ONS CPI D7CO; CPIH L544; national accounts transport equipment deflator; historical price data | 1988-2026 from CPI; earlier under research | `vehicle purchase` (planned) |
| Vehicle maintenance | Repair and servicing prices | ONS RPI DOCT; CPI maintenance and repair components; wage and parts indices | 1987-2026; earlier under research | `vehicle maintenance` (planned) |
| Freight | Rail freight revenue per ton-mile | Railway Returns 1848-1962; British Rail and GBR statistics; ORR freight statistics | 1848-2026 | `goods rate` (planned) |

The general index measures consumer prices. Land, construction and vehicles are assets or
investment goods whose real prices can diverge from consumer prices by a large factor. The
registry exists so that each price type is tied to the series that measures that type, not to
the general index by default.

## Splicing and cross-checks

- Prefer one official series for the whole span.
- Where a splice is unavoidable, link on an overlapping year, not on a ratio between unrelated
  years. Record the link year.
- Check the spliced series against a second source at several dates before entering it.
- A block that changes basis mid-series produces a step that is not in the historical record.
  Divide the series by a known real price for several years; if the ratio is not roughly
  constant, the block is wrong.
- The land series are first-pass: `country land` is an England series and `city land` uses a
  house price proxy before 1995 and a total land value, not a value per dwelling, after it.
  They will be revisited when the engine models land value per tile.
- `buildings` is a four-block chain: Mitchell's building cost index (1845-1938), Holmans's
  construction cost index (1939-1954), the BIS output price index for all new construction
  (1955-2013) and the ONS construction output price index for all new work (2014-2026). The
  links are 1938/39 by continuity, 1955 on the overlap year of the Holmans and BIS series, and
  2014 Q1 on the only quarter published by both the BIS and ONS series.

## Open questions

- Are the loose research files in the base root (`Inflation data 1900-2022.ods`,
  `Commodity prices.ods`, `Coal_since_1853.xls`) independent compilations or copies of the
  sources in the registry? Unknown; treat them as unverified until checked.
- Should the registry record the series identifiers already used for the general index and
  wages? They were not recorded when those series were built.
- `fuel[steam]` names no publisher for its coal series. The source should be identified before
  the steam series is next revised.
