---
status: stub
verified: New master @ 4fffcc19e
---
# Project notes

**Covers**: short cross-cutting notes that are easy to miss and apply to many tasks. Read at the
start of most tasks.

## Hard rule: photographic reference (2026-11-15)

**ALL visual asset creation MUST use direct reference photographs of the real subject (or
scale drawings if photographs cannot be found). This binds the agent actually driving the
Blender MCP session: that agent must work from the photographs itself — look at them,
measure the subject's proportions from them, and iterate the geometry against them. NEVER
build shape from text descriptions, dimension tables or memory: text cannot convey shape.
If reference photographs (or drawings) cannot be found, STOP and prompt the user to supply
them. No geometry is built without photographic (or drawing) reference in hand.**
`[USER-DIRECTION:2026-11-15]`

**Every 2D-image-to-.blend run also captures views of the model regularly during
construction, each from the same angle as one of the reference images, and matches the
model at those angles; views with no reference image are rendered too and must be coherent
with the matched ones (no gaps, no floating parts).** Full rule:
[graphics/visual-asset-controls](graphics/visual-asset-controls.md) (Gate B, same-angle
capture rule). `[USER-DIRECTION:2026-11-15]`

## Notes

- The base workspace root is not a git repository. Only `New/` and
  `Git Blends/Pak128.Britain-blends/` are in-scope repositories; do not interact with any other
  repository even where a `.git` directory exists. `[CODE base filesystem, 2026-09-19]`
- `.dat` files are text but may be reported as binary by some readers; read them as text.
  `[CODE New master @ e36ec2321]`
- Pakset `.dat` values are consumed by Simutrans-Extended. Changing capacities, constraints,
  prices or other save-relevant fields can affect existing savegames and network games; see
  [pakset-compatibility](pakset-compatibility.md) before doing so.
- Every number derived from historical data must name its source, in the header of the file
  that holds it and in the dataset registry. A number with no recorded source counts as an
  estimate and must be labelled as one. Rule and registry:
  [calibration-sources](calibration-sources.md). `[USER-DIRECTION:2026-11-15]`
- Translation texts are a required part of every new asset: each new object needs its
  `New/text/en.tab` entry as part of creation, not as a later follow-up
  ([translations-and-text](translations-and-text.md)). `[USER-DIRECTION:2026-11-15]`
- The pakset has two halves kept in two repositories: the compiled sources in `New/` and the
  Blender meta-sources in `Git Blends/Pak128.Britain-blends/`. A graphics change normally starts
  in the latter and ends as `.png` files in the former.
- AI `.blend` work now runs in a live Blender 4.5 session through MCP; that is the only
  process shown to work to any extent, and the extent is still being established (2026-11-15).
  Under the superseded pre-MCP script pipeline, novel `.blend` creation was unstable while
  minor edits and the `.blend`→`.pak` pipeline were workable. AI readings of renders inform
  iteration but are not verification. Status and failure record:
  [graphics/blend-creation](graphics/blend-creation.md); procedure:
  [graphics/ai-pipeline](graphics/ai-pipeline.md).
  `[RECOLLECTION:2026-09-27]` `[USER-DIRECTION:2026-11-15]`
- Private cars are now produced by a divided workflow: the orchestrating agent researches
  identity, photographs, dimensions, colour range and dates, writes a build brief that carries
  the image files, and does the `.dat`, text entry and compile; a delegated builder agent on
  GPT-6.1 Sol builds the geometry in the live Blender MCP session. The builder must view the
  photographs itself and measure shape from them — a brief that describes shape in words is
  forbidden. A badly wrong build is reported to the user, not sent back for automatic
  correction: correction rounds cost frontier tokens and are the user's decision. Roles, brief
  template and handover files:
  [graphics/car-batch-production](graphics/car-batch-production.md). `[USER-DIRECTION:2026-11-15]`
- Acceptance strictness follows the asset's size on screen: motorcycle outfits and the smallest
  cars are judged on their outline alone; cars get the outline plus defining features; trains,
  ships and aircraft get progressively stricter treatment, though all remain low-poly. Full
  scale: [graphics/visual-asset-controls](graphics/visual-asset-controls.md#strictness-scales-with-the-objects-size).
  `[USER-DIRECTION:2026-11-15]`
- Third-party research material — reference photographs, brochure scans, downloaded
  documents — stays local and is never committed or pushed. Both blends repositories are
  public; only material we hold rights to may be published. In the blends repository,
  `citycars/references/` and `*/references/` are gitignored for this reason.
  `[USER-DIRECTION:2026-11-15]`
- Before selecting a model for Blender MCP, read the
  [local model experience](graphics/model-selection.md#local-blender-mcp-model-experience):
  the user identifies GPT 6.1 Sol as the only successful model so far and a Terra model
  (as offered, GPT-5.6 Terra) as worth trying; the unsuccessful models are recorded there.
  `[USER-DIRECTION:2026-11-15]` `[RECOLLECTION:2026-11-15]`

## Planned sections

- Further cross-cutting facts as they are discovered.

## Open questions

- Are there other recurring facts that deserve to be here rather than in a domain doc?
