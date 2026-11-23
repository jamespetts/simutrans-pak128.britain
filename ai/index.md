---
status: draft
verified: none
---
# Knowledge base index

Retrieval protocol: choose docs from the **read when** keys below; load only what the task
needs; never bulk-load this folder. Claim tags and doc rules: [conventions](conventions.md).
Agent hard rules: [../../AGENTS.md](../../AGENTS.md).

## Structure

This knowledge base is a hierarchy of markdown documents. Only top-level documents are listed
here. A listed document may itself key nested child documents; follow those keys to descend.
The folder is placed in `New/ai/` so that the `New/` git repository tracks and backs it up. It
is deliberately not placed in a root-level `ai/`, which holds only scratch space (`ai/temp/`).
Filenames are lowercase-kebab-case. Inside the knowledge base, use relative markdown links;
do not use line-number references to files that change. Never edit a document's status to
`reviewed` without an interactive user review.

## Orientation

- [project-overview](project-overview.md) — read when context is needed on what this pakset is, where it came from, and how it relates to Standard pak128.Britain and Simutrans-Extended.
- [glossary](glossary.md) — read when Simutrans or pakset vocabulary is unclear in data files, comments, or conversation.
- [repo-map](repo-map.md) — read before navigating the tree; tells real pakset source apart from clutter, historical folders, and out-of-scope repositories.
- [conventions](conventions.md) — read before writing or updating any doc.
- [claim-tags](claim-tags.md) — read before interpreting claims or statuses.
- [project-notes](project-notes.md) — read at the start of most tasks: short cross-cutting notes that are easy to miss.
- [known-bugs](known-bugs.md) — read when starting any bug-fix task or after fixing a bug (the list must be updated); open bugs only, priority-ranked.
- [engine-bugs](engine-bugs.md) — read before investigating a discrepancy between an engine-reported cost or distance and the value the pakset data implies; engine defects that block pakset balancing, with the evidence to fix them.
- [documentation-architecture](documentation-architecture.md) — read before authoring or restructuring any doc: what belongs in docs and the size, nesting and canonical-location rules.

## Design & planning

- [high-level-design-goals](high-level-design-goals.md) — read before any design or balancing work: the amended design goals that govern pakset assets and data.
- [pakset-roadmap](pakset-roadmap.md) — read when planning what assets or features to add in what order; registry of planned work. Check after completing work to close its entry.
- [balancing](balancing.md) — read when tuning prices, costs, capacities, speeds, or intro/retire dates, or when judging economic and historical realism.
- [cost-balancing-register](cost-balancing-register.md) — read when starting or tracking cost-balancing work on any class or item: the coverage status (balanced? class data? individual data? extrapolation feasible?) for every costed class, keyed to the cost-balancing spreadsheets.
- [cost-data-coverage](cost-data-coverage.md) — read when judging how good the historical cost data is for a class of objects before setting any price: the per-class coverage quality, what each class's data can support, and the gaps.
- [calibration-sources](calibration-sources.md) — read before entering any historically derived value in a config file or `.dat`: the source-recording rule and the dataset registry.
- [prices-config](prices-config.md) — read when editing or extending `config/prices.tab`: the price types, the index method, the unit conversion and the outstanding series.
- [conversion-chains](conversion-chains.md) — read before converting any cost, fare, wage or fuel price between `.dat` units and pounds: the canonical table for every category, with its timescale, monthly factor and status.
- [vehicle-cost-model](vehicle-cost-model.md) — read before setting or changing any vehicle `cost`, `runningcost`, `fixed_cost` or `upgrade_cost`: what each field is charged for, and how `bits_per_month` and `meters_per_tile` scale it.
- [vehicle-cost-method](vehicle-cost-method.md) — read before comparing vehicle prices across eras or classes: how to hold the specification constant, how to estimate a 1900 base level, and the traps in matched-model evidence.
- [vehicle-cost-evidence](vehicle-cost-evidence.md) — read when a measured historical vehicle price or maintenance figure is needed: the evidence by class and era, the conversion question it exposes, and what it does not support.
- [fuel-evidence](fuel-evidence.md) — read before setting or checking a fuel price in `config/fuel.tab`: the published coal, oil, petrol, electricity and aviation series by year, the long coal series, and the unresolved unit question for steam.
- [balance-synthesis](balance-synthesis.md) — read before changing any cost or revenue value: the whole-pakset operating account against Acworth, the conversion challenge that affects every absolute figure, the four standing hypotheses and the decisions outstanding.
- [cost-of-capital](cost-of-capital.md) — read before changing starting money, borrowing, the credit limit or the interest rate: what the engine already does, why a new company cannot borrow, and the proposed founding credit facility.
- [borrowing-rates](borrowing-rates.md) — read before setting any interest rate, bond coupon or credit-rating loading: the rates at which British companies and railways actually borrowed, 1830-2026.
- [commercial-rates-1945-2026](commercial-rates-1945-2026.md) — read before setting a modern borrowing rate: corporate bond yields by credit quality and bank borrowing costs for British companies, 1945-2026.
- [transport-finance-1945-2026](transport-finance-1945-2026.md) — read when financing a road fleet, ship or aircraft: hire purchase, leasing, ship mortgages, aircraft finance and sector evidence.
- [borrowing-land-transport-1750-1948](borrowing-land-transport-1750-1948.md) — read before setting a pre-1948 borrowing rate for a canal, omnibus or tramway company: the rates those companies actually paid.
- [borrowing-docks-shipping-1750-1948](borrowing-docks-shipping-1750-1948.md) — read for a dock, shipping or general industrial benchmark rate before 1948, and for Bank Rate and bill rates.
- [staff-wages](staff-wages.md) - read before setting or checking a crew wage in `config/staff.tab`: the published wage rates by grade and era, 1750-2050, the reconstructed series, and the gaps.
- [prices-forum-fragments](prices-forum-fragments.md) — read when a single building or structure price is needed for an era, or before setting the station, depot and platform multipliers: what the forum pricing thread supplies and what it does not.
- [prices-goods-rate](prices-goods-rate.md) — read when building, reviewing or amending the `goods rate` series in `config/prices.tab`: the 1900 anchor, the series path by block, the method and the traps.
- [goods-rate-evidence](goods-rate-evidence.md) — read when a historical goods freight rate figure or source is needed: the measured evidence by block, canal era to the present, with source records.
- [infrastructure-cost-evidence](infrastructure-cost-evidence.md) — read before rebalancing any infrastructure object, or when a measured historical cost is needed: the evidence behind the cost recommendations, by domain, with sources.
- [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) — read when deciding what an infrastructure object should cost: the scaling map, the cross-cutting maintenance finding, current against recommended values, and the decisions taken or outstanding.
- [class](class.md) — read when touching passenger or mail classes, accommodation, comfort, catering, or fare-dependent revenue; keyed from [balancing](balancing.md).
- [comfort-calibration](comfort-calibration.md) — read before setting or changing any comfort value: what the number means, the anchors, the line, the per-type methods and the register of calibrated vehicles.

## Build, data & infrastructure

- [build-and-toolchain](build-and-toolchain.md) — read when compiling `.pak` files, touching the build files, or dealing with makeobj and its versions.
- [pak-format-and-objects](pak-format-and-objects.md) — read when creating or editing `.dat` objects, choosing an object type, or working out which folder compiles into which `.pak`.
- [pakset-compatibility](pakset-compatibility.md) — read before changing capacities, constraints, prices, or other save/load-relevant `.dat` values, to avoid breaking savegames or network compatibility.

## Object types

- [object-types](object-types.md) — read before creating or editing any object; the entry point to the per-type docs, one for each `Obj=` type the pakset uses (vehicles, buildings, ways, bridges, tunnels, signals, crossings, industries, piers, ground, trees, private cars, pedestrians, UI, and the rest). Each type's doc is keyed from there.

## Graphics & presentation

- [graphics-pipelines](graphics-pipelines.md) — read when producing or changing images; keys the Blender rendering, image layout, and livery child docs.
- [scaling-conventions](scaling-conventions.md) — read when deciding model or image scale, dimensions, or multi-tile sizes.

## Content, text & community

- [translations-and-text](translations-and-text.md) — read when touching user-facing text: `text/` `.tab` files, city name lists, simutranslator, or object names.
- [releases-and-versioning](releases-and-versioning.md) — read when making a release or incrementing the pakset version.
- [research-and-forum](research-and-forum.md) — read when sourcing historical or balancing data; how to use and cite the Simutrans forum and research material.
