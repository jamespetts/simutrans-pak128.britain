---
status: stub
verified: New master @ 4fffcc19e
---
# Project notes

**Covers**: short cross-cutting notes that are easy to miss and apply to many tasks. Read at the
start of most tasks.

## Notes

- The base workspace root is not a git repository. Only `New/` and
  `Git Blends/Pak128.Britain-blends/` are in-scope repositories; do not interact with any other
  repository even where a `.git` directory exists. `[CODE base filesystem, 2026-09-19]`
- `.dat` files are text but may be reported as binary by some readers; read them as text.
  `[CODE New master @ e36ec2321]`
- Pakset `.dat` values are consumed by Simutrans-Extended. Changing capacities, constraints,
  prices or other save-relevant fields can affect existing savegames and network games; see
  [pakset-compatibility](pakset-compatibility.md) before doing so.
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

## Planned sections

- Further cross-cutting facts as they are discovered.

## Open questions

- Are there other recurring facts that deserve to be here rather than in a domain doc?
