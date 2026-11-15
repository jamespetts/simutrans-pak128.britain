---
status: draft
verified: none
---
# Aircraft authoring notes

**Covers**: aircraft-specific refinements to the AI pipeline: scale, render conversion,
mirror workflow, the TexFace livery system, procedural livery artwork, and exposure rules.
Parent: [graphics-pipelines](../graphics-pipelines.md). General pipeline rules:
[ai-pipeline](ai-pipeline.md).

## Scale and placement

- Aircraft use a separate linear length scale: 128 pixels (one tile) represents 46 m, via the
  `air/46m-rule.dae` ruler. Oversized cells (192, 224, 256 classes in `New/Makefile`) apply;
  the 707 and the newer widebody aircraft render at 192.
  [FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]
- Aircraft render 8 views with the render script's **normal alignment** (`op_list` "1"),
  consistent with the legacy sheet-based 707 renders.
  `[EXECUTION-VERIFIED:2026-09-23]`
- New aircraft use one `.png` per direction (192×192 for the 192 class) with RGBA transparent
  backgrounds. `[CODE New ex-15 @ 8b04b2114]`
- Scale a 707-derived model at authoring scale by the 46 m rule: the 10-unit 707 model by
  0.801 (the Italian note in `air/Boeing/707/Boeing_707_320_420_C.txt`), the 45.9 m DC-8 by
  0.796; then raise it 2.2 Blender units in Z so the rendered aircraft sits in the cell like
  the reference aircraft. Save the scaled, positioned model in the blend (render-ready): the
  earlier failure mode was an unscaled model rendered about 25% too large.
  `[EXECUTION-VERIFIED:2026-09-24]`
- Per-direction 192-class `.dat` entries use one standard offset table; see "Per-direction
  image offsets" below.

## Per-direction image offsets (192-class)

One standard modifier table is used for every direction of the per-direction 192-class
aircraft (VC-10, Super VC-10, Tristar, 787). It was published in the
workflow post and is verified against the shipped `.dat` files:

| Direction | Modifier |
|-----------|----------|
| E         | `,-64,-56` |
| SE        | `,-32,-32` |
| S         | `,-110,0` |
| SW        | `,-32,-32` |
| W         | `,0,-24` |
| NW        | `,-32,-32` |
| N         | `,-110,0` |
| NE        | `,0,-32` |

`[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`
`[CODE New ex-15 @ 8b04b2114]`

- The legacy sheet-based 707 uses a uniform `,-31,-46` on all views instead; its sheet was
  hand-aligned per cell and it is not the model for per-direction images.
  `[CODE New ex-15 @ 8b04b2114]`
- The table assumes the standard cell framing: the rendered content sits in the cell as on the
  reference aircraft (whose models are render-ready). A model left at Z 0 without the Z raise
  renders about 30 px (192-class) too low in the cell; the offset table cannot correct that.
  `[EXECUTION-VERIFIED:2026-09-24]`
- The 256 class uses a uniform `,-62,-92` instead (747-8 and the new Zeppelin `.dat` entries).
  `[CODE New ex-15 @ 8b04b2114]`
- The DC-8 does NOT use this table. Its renders (707-model placement convention) frame the
  content like the 707's sheet, not like the VC-10's renders. Its offsets were derived by
  placing each sprite coincident with the corresponding 707 sheet cell (binary-silhouette
  cross-correlation, IoU 0.90–0.96, confirmed by four-point extreme agreement) and confirmed
  in game against the 707 stopped at the same apron position: E `,-20,-44`;
  SE `,-31,-41`; S `,-46,-47`; SW `,-22,-47`; W `,-14,-44`; NW `,-31,-16`; N `,-48,-41`;
  NE `,-19,-46`. `[EXECUTION-VERIFIED:2026-09-24]`

## Orientation standard (mirrored vs conventional)

- Rail vehicles (and road/tram by the render script's own setup) run their length along Y with
  the nose/front at **−Y**, and render correctly with the "vehicle alignment" (`op_list` "2")
  cameras. `[EXECUTION-VERIFIED:2026-09-23]`
- Legacy aircraft (the 707 and 737 among them) run the fuselage along X with the nose at −X
  (707: X ≈ −4.97…+4.64; 737: X ≈ −14.3…+13.4). `[EXECUTION-VERIFIED:2026-09-24]`
- The DC-8-10 blend (`air/Douglas-DC-8-10.blend`) is the 707 model rotated +90° about Z: the
  fuselage runs along Y with the tail fin at +Y and the nose at −Y (fin mesh at Y 2.6…4.8,
  nose tip Y ≈ −4.9), the same length orientation as rail vehicles. Each per-direction file is
  assigned to the `.dat` entry of the same render-script view name (file `_W.png` →
  `EmptyImage[W]`). This orientation and mapping is confirmed in game (depot, taxiway and
  apron, all rotations). `[EXECUTION-VERIFIED:2026-09-24]`

## Render conversion checklist (every legacy aircraft file)

Older aircraft files use the old pipeline throughout. Convert in the working copy before
rendering, and check every file (recorded 2026-09-23):

- Output PNG RGB → RGBA; background SKY → transparent alpha.
- Anti-aliasing (OSA) 16 → 11.
- Resolution stays as authored (707: 192×192). The **sun rig does not**: the saved rigs do
  not light the model correctly under the script, so replace the rig with the verified one in
  the exposure section below before rendering. `[EXECUTION-VERIFIED:2026-09-24]`

## Mirror workflow

- Source models vary: some are mirrored half-models (7 Y-mirrors on the 707), some are
  conventional full models, and some rely on textures whose image files may now be missing
  from the repository. `[RECOLLECTION:2026-09-23]` Inspect each asset before choosing a path:
  mirror modifiers present, UV layers present, and every referenced image file present on disk
  (packed or alongside the blend). Missing textures must be re-authored, not worked around.
- Interchange drops unapplied modifiers, so apply them in the working copy first
  (`stageA_export.py --apply-mirrors`, reported in JSON). Reshaping by moving vertices
  preserves per-face UV assignments, which are independent of positions.
- Constrained numeric edits run natively in the 2.79 working copy (transforms baked first),
  keeping mirrors (once applied), UVs, materials, and image links intact with zero interchange
  loss. The modern-Blender DAE path is reserved for vision-loop novel geometry.

## TexFace livery system

- Livery variants paint the airframe with face-assigned images on `TexFace` materials (707:
  side+windows image on the fuselage tube, tail image on the fin; flat grey elsewhere), while
  unpainted base files carry no UVs or links at all. Face images do not survive interchange;
  record the mesh-to-image mapping and re-link by path.
- New liveries are 2D artwork fitted to the existing UV layout: image X runs nose-to-tail
  station, rows run crown-to-keel (proven by diagnostic stripe render). Template window/door
  pixel positions are reused; only colours, titles, and nose/tail regions are repainted.
- Titles and registrations use a hand-encoded 5×7 bitmap font rasterized procedurally; at
  pak scale they render ~2 px tall (present, marginal — matches production title visibility).

## Exposure and shading (all models)

- All faces shaded flat (`use_smooth = False` on every polygon); smooth shading produces
  visible artifacts on curved airframe surfaces. `use_smooth = True` in old files is from an
  early Blender version and must be turned off. `[RECOLLECTION:2026-09-24]`
- The sun lamp sets the rendered brightness, not the material diffuse value alone. The
  verified working setup is:
  - lamp type SUN, colour RGB `(0.56, 0.56, 0.56)` (the grey sun required by the Italian note
    in `air/Boeing/707/Boeing_707_320_420_C.txt`), energy `0.028` (the value saved in the
    707/737 blends; the DC-8 uses `0.035` after in-game review of the first delivery, which
    matches the 707's shipped image means and clips at most ~3% of lit pixels);
  - rig: the lamp parented to the `Sphere` handle with `matrix_parent_inverse = identity` and
    local rotation `(117.3791°, 0, -143.7421°)`; the render script's per-view `Sphere`
    rotation then places the sun about 45° above and to the camera's left, slightly in front;
  - materials diffuse intensity 0.8, specular intensity 0.5 (matching the 707 and VC-10),
    world ambient colour `(0, 0, 0)`.
  `[EXECUTION-VERIFIED:2026-09-24]`
- Saved sun rigs in legacy blends are NOT the render-time state. The 707, 737 and
  `air-template.blend` rigs produce a horizontal beam under the script, and the DC-8's
  delivered rig (identity `matrix_parent_inverse`, local rotation Z 45°) produced an upward
  beam, rendering the aircraft black. Verify before rendering that the lamp's world beam
  direction (its `matrix_world` applied to `(0, 0, -1)`) points downward; a rig with a
  non-negative Z beam component is broken. `[EXECUTION-VERIFIED:2026-09-24]`
- The 0.8-diffuse "too light" and 0.5-diffuse/zero-specular "too dark" material experiments on
  the DC-8 were made while its rig was broken and are not the correct settings.
  `[EXECUTION-VERIFIED:2026-09-24]`
- `.dat` image references must match the PNG filenames EXACTLY. The DC-8 `.dat` reads
  `dc-8-10_*` (hyphen after "dc") but several re-render batches were written to `dc8-10_*`
  (no hyphen) and silently ignored for hours. A changed `makeobj LIST` byte size proves new
  images were consumed, but an unchanged size does not prove they were not: re-encoding the
  same silhouettes with different pixel values (or changing offset modifiers) leaves the
  size equal because the run-length structure and the offset fields are fixed-width. When in
  doubt, check the rebuilt `.pak` timestamp and compare renders. `[EXECUTION-VERIFIED:2026-09-24]`

## DC-8-10 instance (confirmed)

- Source: `air/Boeing/707/Boeing_707_320_420_C_BOAC.blend`, layers 1 (+3 rig). Livery:
  `Private-operator`. Artwork: `air/DC8-10-lato.png`, `air/DC8-10-timone.png`.
- The blend `air/Douglas-DC-8-10.blend` is saved render-ready: model scaled to the 46 m rule
  (factor 0.796) and raised 2.2 Blender units, flat-shaded, verified sun rig (energy 0.035),
  192×192 RGBA, OSA 11, `op_list` "2" as built. Rendering it with the stock script reproduces the
  shipped images bit-for-bit. `[EXECUTION-VERIFIED:2026-09-24]` Per the 2026-09-25 direction,
  new aircraft renders use normal alignment (`op_list` "1"); the DC-8 images are verified in
  game and stand as final with no rework required. `[RECOLLECTION:2026-09-25]`
- The `.dat` uses the 707-coincident offsets above; `make` and the headless-engine
  map-generation smoke test pass. `[EXECUTION-VERIFIED:2026-09-24]`
- In-game alignment, heading and appearance confirmed against the 707 at the same apron
  position, all rotations. `[EXECUTION-VERIFIED:2026-09-24]`

## End-to-end procedure (new aircraft)

Inputs: visual references (livery, proportions) and data references (dimensions, dates,
performance). Given a base `.blend` (existing model or `air-template.blend`):

1. **Model**: orient fuselage along Y, nose at −Y; scale to the 46 m rule (128 px = 46 m;
   for a 707-sized model in a 192 cell: factor ≈ 0.80, then raise +2.2 Z); flat-shade every
   polygon; apply mirror modifiers.
2. **Light rig**: SUN lamp parented to `Sphere` with `matrix_parent_inverse = identity`,
   local rotation `(117.3791°, 0, -143.7421°)`, colour `(0.56, 0.56, 0.56)`; set energy by
   matching a shipped sibling's lit-pixel means (DC-8: `0.035`); world ambient `(0,0,0)`.
   Verify the beam points downward before rendering. Materials: diffuse 0.8, specular 0.5.
3. **Render**: enable layers 1+3, output 192×192 RGBA, OSA 11, `op_list` "1" (normal alignment); save the blend
   **before** rendering, never after (the script displaces the light rig). Render 8 views.
4. **Offsets**: do NOT copy another aircraft's table blindly — first check which render
   framing the model follows. If forked from the 707, derive per-view offsets by silhouette
   cross-correlation against the shipped 707 sheet cells plus the 707's uniform `,-31,-46`
   (expect IoU ≥ 0.90 and four-point agreement within ~2 px). If framed like the VC-10
   renders, use the canonical table above. A uniform screen-space error across all views
   means the model Z placement is off, not the table.
5. **Build and verify**: write the `.dat` (exact filenames; offsets appended as
   `.row.col,x,y`), `make` the size class, confirm the object changed via `makeobj LIST`
   (note: pixel-only changes may keep the byte size; check the `.pak` timestamp),
   `test-pakset.ps1` → `MAP-GEN: PASS`, then in-game check per rotation against a shipped
   sibling stopped at the same position.
6. **Record**: blend render-ready state, offsets + method, verification results here.

## Related docs

- [blender-rendering](blender-rendering.md) — render workflow, placement, test records.
- [scaling-conventions](../scaling-conventions.md) — rulers and oversize rules.
- [liveries-and-special-colours](liveries-and-special-colours.md) — livery system, HSV table.

## Open questions

- The DC-8-10 was built with `op_list` "2" and verified in game, while headless
  normal-alignment ("1") renders reproduce the shipped 707 sheet within 4 px: is the
  alignment choice material for aircraft renders, or is either acceptable? Open until a "1"
  aircraft render is verified in game.
- Which further aircraft need render conversion, and in what order?
- Should converted legacy files be saved back to the blends repository, and when?
- Should the verified sun rig be written into `air-template.blend` and the legacy aircraft
  blends, so a future renderer cannot repeat the black-model failure?
