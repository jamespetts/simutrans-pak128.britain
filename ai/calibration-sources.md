---
status: draft
verified: New ex-15 @ cedd39abc (working tree, 2026-11-23)
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
| Wages | Railway, tram and general wages | Board of Trade railway and public-utility enquiries 1906-1907; Hansard 1922, 1925, 1962, 1976 and 1980; Williamson 1982 (via Stanier's archived page); Simutrans forum topic 6521; *British Labour Statistics: Historical Abstract 1886-1968* Table 50; New Earnings Survey April 1980 (ONS adhoc 005457); ONS ASHE 4-digit occupational timeseries 1999-2016 and Table 14.7a 2017-2026 | 1710-2026 measured, projected to 2050 | `staff[*]` |
| Corporation tax | UK main rate | GOV.UK rates and allowances | 1798-2023 | `corporation tax` |
| Bank Rate | Bank of England policy rate | Bank of England Bank Rate history | 1750-2025 | `base rate` |
| Building construction | Nominal price of building work | Mitchell, *British Historical Statistics* (1988) Ch VII Table 8, building costs (1930=100), 1845-1938; Holmans, *Historical Statistics of Housing in Britain*, Table M.10, construction costs (1958-60=100), 1939-1970, with 1940-1947 from Mitchell and Deane, *Abstract of British Historical Statistics* (1962) Ch IX Table 4; BIS output price index, all new construction, 1955-2013; ONS construction output price index, all new work, 2014-2026. The first two are taken from the Bank of England "A millennium of macroeconomic data" workbook, sheet A32, columns S and T. Before 1845 the 1845 real level is held and tracks the general index (backcast tested against a wage-based alternative; see [prices-config](prices-config.md)) | 1845-2026, backcast to 1750 | `buildings` |
| Civil engineering | Infrastructure construction prices | ONS output price index for new work: infrastructure, 1980-2026, chained from BIS Construction Price and Cost Indices Table 1 column 13 (1980-2011), the ONS interim construction output price indices back history (1996-2015) and the current ONS construction output price indices (2014 onward). Before 1980 the `buildings` index is held as a stand-in; the forum's individual canal, aqueduct, viaduct and tunnel prices were tested as a substitute and rejected | 1980-2026 from the ONS series, 1750-1980 from `buildings` | `infrastructure` (implemented) |
| Farmland | England agricultural land price | Savills long-run England farmland series, all land types (real, rebased to 2023) | 1900-2024 | `country land` |
| Urban land | UK residential land price | JST Macrohistory Database UK nominal house price index (1900-1995 proxy); ONS land underlying dwellings, AN.21111 (1995-2025) | 1899-2025 | `city land` |
| Vehicles | Purchase prices of transport equipment | Feinstein 1972 table 63 column 6 (railway rolling stock, 1856-1938) and column 4 (plant and machinery, 1938-1965); Blue Book 1997 tables 13.2 and 13.4 (vehicles, ships and aircraft, 1965-1997); the 1997 real level held thereafter | 1750-2050 | `vehicle purchase` (implemented) |
| Vehicle maintenance | Repair and servicing prices | ONS RPI DOCT; CPI maintenance and repair components; wage and parts indices | 1987-2026; earlier under research | `vehicle maintenance` (planned) |
| Car access | Share of households with a car or van, by income quintile | National Travel Survey table NTS0703, "Household car availability by household income quintile: England, 2002 onwards" (DfT, NTS 2025 release, 10 September 2026), value = 100 minus the "no car or van" percentage; the general Great Britain vehicle-availability series in DfT Transport Statistics Great Britain 2008, section 9, is the anchor for the 1951-2001 rows, which are extrapolations, not measurements | 2002-2025 measured; 1951-2001 extrapolated; 2030 and 2050 projected by a logarithmic continuation of the 2002-2025 trend, with the three highest classes held at their 2025 equality | `privatecar.tab` |
| Freight | Rail freight revenue per ton-mile | Canal Acts and Acworth 1905 (pre-1845); Cmd. 525 (1920) and HANSARD charge changes (1913-1923); Ministry of Transport monthly Railway Statistics via NBER (1920-1931); Annual Abstract of Statistics (1938-1951); BR Facts and Figures and GERS yearbooks RH087/RH062/RH071 (1948-1977); Serpell 1982 (real, cross-check); ORR Table 1310 and nominal freight income (1982-2026) | 1750-2050 | `goods rate` (implemented) |

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
- `privatecar.tab` is a measured block (NTS0703, 2002 onwards) behind extrapolated rows
  (1951-2001). NTS revises earlier years at each release, so replace the whole 2002-latest
  block from the current NTS0703 rather than appending the new year alone; the 2026 release
  changed the 2009 and 2013 values that the 2024 copy had recorded.
- `buildings` is a four-block chain: Mitchell's building cost index (1845-1938), Holmans's
  construction cost index (1939-1954), the BIS output price index for all new construction
  (1955-2013) and the ONS construction output price index for all new work (2014-2026). The
  links are 1938/39 by continuity, 1955 on the overlap year of the Holmans and BIS series, and
  2014 Q1 on the only quarter published by both the BIS and ONS series.
- `infrastructure` chains three ONS and BIS vintages of one measure, each link measured on an
  overlap year, and holds the `buildings` path before 1980 because no civil engineering series
  reaches back that far. The consequence is that the pre-1980 range of that index carries
  building prices. The method, the link factors and the test that rejected the forum structure
  prices as a substitute are in [prices-infrastructure](prices-infrastructure.md).
- `staff[*]` is compiled as nominal annual old pence and converted at **×10/3** to the engine's
  monthly Simucents: 1 old penny = 80 Simucents at the revenue rate, divided by 12 months and by
  the engine's ×2 monthly factor. The anchor table, the measured/derived/estimated status and the
  remaining gaps are in [staff-wages](staff-wages.md) and
  [staff-wages/reconstruction](staff-wages/reconstruction.md).

## Open questions

- Are the loose research files in the base root (`Inflation data 1900-2022.ods`,
  `Commodity prices.ods`, `Coal_since_1853.xls`) independent compilations or copies of the
  sources in the registry? Unknown; treat them as unverified until checked.
- Should the registry record the series identifiers already used for the general index and
  wages? They were not recorded when those series were built.
- `fuel[steam]` names no publisher for its coal series. The source should be identified before
  the steam series is next revised.
