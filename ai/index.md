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
- [documentation-architecture](documentation-architecture.md) — read before authoring or restructuring any doc: what belongs in docs and the size, nesting and canonical-location rules.

## Design & planning

- [high-level-design-goals](high-level-design-goals.md) — read before any design or balancing work: the amended design goals that govern pakset assets and data.
- [pakset-roadmap](pakset-roadmap.md) — read when planning what assets or features to add in what order; registry of planned work. Check after completing work to close its entry.
- [balancing](balancing.md) — read when tuning prices, costs, capacities, speeds, or intro/retire dates, or when judging economic and historical realism.
- [calibration-sources](calibration-sources.md) — read before entering any historically derived value in a config file or `.dat`: the source-recording rule and the dataset registry.
- [prices-config](prices-config.md) — read when editing or extending `config/prices.tab`: the price types, the index method, the unit conversion and the outstanding series.
- [prices-forum-fragments](prices-forum-fragments.md) — read when a single building or structure price is needed for an era, or before setting the station, depot and platform multipliers: what the forum pricing thread supplies and what it does not.
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
