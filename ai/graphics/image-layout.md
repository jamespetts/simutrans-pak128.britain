---
status: draft
verified: New ex-15 @ 8b04b2114
---
# Image layout and format

**Covers**: the `.png` format requirements, the image reference string grammar, image sheet
layout, and special colours. The engine and makeobj are the authority.

## PNG format requirements

- Cell size is the size passed to makeobj (`PAK32`…`PAK256`, default 64) unless the object sets
  `cell_size`. Most pakset objects use 128. `[CODE simutrans-extended master @ f378cf551]`
- A PNG's width and height must each be an exact multiple of the cell size, otherwise makeobj
  aborts with `Invalid image size`. Cells are square. `[CODE simutrans-extended master @ f378cf551]`
- Accepted colour types are palette, RGB, and RGBA. Grayscale is not converted and is not
  supported by the loader. `[CODE simutrans-extended master @ f378cf551]`
- 16-bit channels are reduced to 8-bit, and 1/2/4-bit images are expanded to one pixel per byte.
  `[CODE simutrans-extended master @ f378cf551]`
- There is no required palette. Any 24-bit RGB is accepted. Opaque colours are quantised to
  RGB555; colours with transparency are quantised to RGB343 with 31 alpha levels.
  `[CODE simutrans-extended master @ f378cf551]`
- Alpha in the file follows normal PNG semantics: alpha 0 is transparent and alpha 255 is
  opaque. On load the engine moves alpha first and inverts it (`utils/dr_rdpng.cc`:
  `png_set_swap_alpha`, `png_set_invert_alpha`), so internally alpha 0 is opaque and alpha
  255 is transparent. The "at or above 248" threshold applies to that internal inverted
  channel: file pixels with alpha at or below 7 are treated as fully transparent
  (`descriptor/writer/image_writer.cc`: `ALPHA_THRESHOLD`, `is_transparent`).
  `[CODE simutrans-extended master @ f378cf551]`
- Each cell is trimmed to the bounding box of its non-transparent pixels. The stored image
  offsets and dimensions are therefore the trimmed box, not the whole cell; the engine places it
  using those offsets. `[CODE simutrans-extended master @ f378cf551]`

In this pakset, image sheets use 24-bit RGB or 32-bit RGBA. Measured examples: a station sheet at
768x256, an arrow sheet at 768x128, a tree sheet at 128x128, and a borders sheet at 1152x384
(all multiples of 128). `[CODE New master @ e36ec2321]`

## Image reference string grammar

Documented in the engine's image writer:

```
"-"                                        empty image
[> ]filename_without_extension[[[[.row].col],xoffset],yoffset]
```

- A leading `> ` sets the non-zoomable flag (used for icons).
- `-` or an empty value means no image.
- The extension is always replaced with `.png`.
- `.row` selects a cell; if `.col` is omitted, the cell is read row-major:
  `col = row % (width/cell)`, `row = row / (width/cell)`.
- `xoffset,yoffset` are only parsed when `.col` is present, and shift the trimmed image's
  placement by that many pixels.
- Property names are case-insensitive, and spaces inside `[]` are stripped.

`[CODE simutrans-extended master @ f378cf551]`

Placement semantics: the compiled image stores `image.x = xoffset + first_opaque_x` and
`image.y = yoffset + first_opaque_y`, with width and height the trimmed content box; the
engine draws it at `anchor + image.x/y`, where the anchor for a vehicle is the tile screen
position plus the vehicle's screen offset. A `.dat` entry with no modifier therefore draws
the content at its raw position inside the render cell, which is the usual cause of a vehicle
sprite sitting off its way; see the aircraft offset table in
[aircraft-notes](aircraft-notes.md).
`[CODE simutrans-extended ex-15-industry-growth-test @ 1226bbe48]`

## Sheet layout

- Cells are ordered row-major. A 768x256 sheet at cell size 128 is 6 columns by 2 rows.
- A value may name the cell either by a single number (`.0`, `.1`, …) or by explicit `.row.col`.

## Special colours

A special colour is recognised only by an exact 24-bit RGB match to the engine's table. There is
no palette-index meaning. The table and the transparency colour are in
[liveries-and-special-colours](liveries-and-special-colours.md).
`[CODE simutrans-extended master @ f378cf551]`

## Transparency and anti-aliasing

- The current workflow for this pakset is anti-aliased `.png` images with a transparent alpha
  background, so that object edges blend with whatever is behind them in the game.
  `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`
- Many existing graphics in the pakset still use the old system: a flat background of the special
  transparency colour, with no anti-aliasing to the background. `[RECOLLECTION:2026-09-19]`
- The eventual aim is to convert all the old graphics to the alpha-transparency type.
  `[RECOLLECTION:2026-09-19]`
- The conversion is limited by missing source files: not all `.blend` files exist. For example,
  most London Underground vehicles have no `.blend` files and will need to be recreated. There is
  no `london-underground` folder in the blend repository.
  `[RECOLLECTION:2026-09-19]` `[CODE GitBlends master @ 1c1acf58]`

## Index mapping by object type

The meaning of each index for each object type (directions, ages, animation phases, seasons,
layouts, RIBI values, and slopes) is in
[image-index-mapping](image-index-mapping.md).

## Open questions

- Which pakset objects use `cell_size` and which size class, and why?
- Are snow and night variants always separate PNGs, or sometimes the same sheet?
