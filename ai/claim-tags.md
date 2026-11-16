---
status: draft
verified: New master @ 30444805f
---
# Claim tags (inline)

- `[CODE <repo> <branch> @ <short-sha>]` — verified against the checked-out data or files at the
  stated repository, branch and commit (for example `[CODE New master @ e36ec2321]`). This is the
  strongest tag for pakset facts: `.dat` values, image properties, build files, blend sources.
- `[EXECUTION-VERIFIED:<date>]` — observed by actually building the pakset or running Blender on
  the maintainer's machine (build results, render output, timings); machine-specific, so treat as
  a dated observation, not a universal constant.
- `[FORUM:<url>]` — from a Simutrans forum thread; cite the thread and, where possible, the post
  date. The pak128.Britain board is https://forum.simutrans.com/index.php/board,75.0.html .
- `[LITERATURE:<url>]` — from published external work (paper, benchmark, standard, vendor
  documentation). Evidence about the world outside this repository, never about pakset data or
  files; cite the specific source, and record the version or date where the result is likely to
  age.
- `[RECOLLECTION:<date>]` — user statement from memory. An indication, not a verified fact:
  verify against the data before relying on it.
- `[UNVERIFIED]` — agent inference, not yet confirmed. Must be verified or removed at review.
- `[PRIOR]` — model training-data knowledge. Search hint only, never a claim; convert to `[CODE]`
  or delete. Applies to Simutrans, Simutrans-Extended, and all paksets.

Untagged prose in a `draft`/`reviewed` doc is implicitly `[CODE]` at the frontmatter `verified:`
value.
