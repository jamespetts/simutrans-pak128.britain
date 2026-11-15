---
status: stub
verified: none
---
# Graphics creation pipelines

**Covers**: how `.png` images are produced for the pakset, from Blender meta-sources and from
other sources, and how they are laid out and coloured.

Read the child doc for the stage a task touches. Scaling conventions for art and models are
separate; see [scaling-conventions](scaling-conventions.md).

## Child docs

- [blender-rendering](graphics/blender-rendering.md) — read when working from `.blend` sources: headless Blender, render scripts, direction views, and alignment.
- [ai-pipeline](graphics/ai-pipeline.md) — read before any AI-authored geometry task: the MCP procedure stages, what the pre-MCP pipeline was, and current procedure status.
- [error-categories-pre-mcp](graphics/error-categories-pre-mcp.md) — read when checking AI geometry work for known failure modes: the historical error checklist of the superseded pre-MCP pipeline.
- [blender-mcp](graphics/blender-mcp.md) — read before any geometry work that drives a live Blender session: installed environment, permitted writes, dispatch workaround, and session findings.
- [model-selection](graphics/model-selection.md) — read before choosing a model for an asset task, or before claiming a model change will fix a recorded failure: published per-model measurements and where models fail.
- [blend-creation](graphics/blend-creation.md) — read before creating or reshaping `.blend` geometry: current status, failure record, and verification doctrine (AI readings of renders inform iteration but are never acceptance evidence).
- [aircraft-notes](graphics/aircraft-notes.md) — read when working on aircraft: scale, render conversion, mirrors, TexFace liveries, and exposure rules.
- [image-layout](graphics/image-layout.md) — read when producing or editing `.png` image sheets and their layout in `.dat` files.
- [photo-to-pak-pipeline](graphics/photo-to-pak-pipeline.md) — read when building a pakset vehicle image from a photograph and a description: the experimental end-to-end run, file-placement rules (4.5 sources under `<folder>/4.5/`, 2.79 working copies elsewhere), and what remains manual.
- [liveries-and-special-colours](graphics/liveries-and-special-colours.md) — read when adding liveries or using special colours, snow images, or night images.

## Open questions

- Are there graphics pipelines other than the Blender one (for example direct drawing, or
  conversion from elsewhere) that need their own child doc?
- Which pipeline is used for ground, water, and UI imagery?
