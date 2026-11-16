---
status: draft
verified: none
---
# Liveries and special colours

**Covers**: the engine's special-colour table and transparency, and the livery system the pakset
uses.

## Special colours

The engine defines 31 special colours. A pixel is a special colour only when its 24-bit RGB value
exactly matches one of these; there is no palette-index meaning.
`[CODE simutrans-extended master @ f378cf551]`

| Index | RGB | Meaning |
|---|---|---|
| 0–7 | `0x244B67`, `0x395E7C`, `0x4C7191`, `0x6084A7`, `0x7497BD`, `0x88ABD3`, `0x9CBEE9`, `0xB0D2FF` | Player colour 1, eight shades |
| 8–15 | `0x7B5803`, `0x8E6F04`, `0xA18605`, `0xB49D07`, `0xC6B408`, `0xD9CB0A`, `0xECE20B`, `0xFFF90D` | Player colour 2, eight shades |
| 16 | `0x57656F` | Dark windows, lit yellowish at night |
| 17 | `0x7F9BF1` | Lighter windows, lit bluish at night |
| 18 | `0xFFFF53` | Yellow light |
| 19 | `0xFF211D` | Red light |
| 20 | `0x01DD01` | Green light |
| 21–25 | `0x6B6B6B`, `0x9B9B9B`, `0xB3B3B3`, `0xC9C9C9`, `0xDFDFDF` | Non-darkening greys 1–5 (menus) |
| 26 | `0xE3E3FF` | Nearly white by day, yellowish at night |
| 27 | `0xC1B1D1` | Windows, lit yellow |
| 28 | `0x4D4D4D` | Windows, lit yellow |
| 29 | `0xFF017F` | Purple light |
| 30 | `0x0101FF` | Blue light |

The transparency special colour is `0x00E7FFFF` (the `SPECIAL_TRANSPARENT` constant). Pixels with
an alpha byte at or above 248 are also treated as transparent.
`[CODE simutrans-extended master @ f378cf551]`

Because a special colour is matched exactly, any image that needs one must contain the exact RGB
values above. The Blender render script's `sp_` mask mode was intended for this, but the current
workflow states that it is obsolete and belongs to a different pakset, and it should be ignored.
The current workflow uses alpha transparency, and special colours are needed only for multi-tile
buildings and for objects that use player colours (which this pakset does not).
`[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`

## Day/night and night window lighting are not used

This pakset does not use the day/night cycle or night window lighting. The window and light
special colours (dark windows, lighter windows, yellow/red/green/purple/blue light, and the
nearly-white day/night colour, indices 16–20 and 26–30) are therefore not used by this pakset.
The non-darkening greys (21–25) are for menus and are separate. This is consistent with the render
script's `sp_` mask mode being obsolete. `[RECOLLECTION:2026-09-19]`

## Player colours are not used by this pakset

The pakset does not currently use player colours (indices 0–15). It uses Simutrans-Extended's
livery system instead. `[RECOLLECTION:2026-09-19]`

## The livery system

A vehicle declares named liveries with `LiveryType[i]`, and supplies a separate image set for
each livery through the livery index of `EmptyImage[dir][livery]` and
`FreightImage[type][dir][livery]`. The example in `New/trains/4-wheel-1860s.dat` lists 11 liveries
and a separate eight-direction image set for each.
`[CODE New master @ e36ec2321]` `[CODE simutrans-extended master @ f378cf551]`

The pakset also has a `New/livery-trains/` source folder. `[CODE New master @ e36ec2321]`

Liveries are built in the Blender model from separate coloured polygons (planes), or from textures
applied to the model; the pakset graphics guide describes both methods. They are not built from
player colours. `[FORUM:https://forum.simutrans.com/index.php/topic,2401.0/all.html]`

## Livery selection and dates

- Livery schemes are defined in `New/config/simuconf.tab` (`livery_scheme[i]`, dated
  `livery[i][j]` entries with `intro_year`/`intro_month`, optional scheme retirement). A
  convoy holds one scheme; each vehicle automatically wears the scheme livery with the latest
  introduction date not in the future, among the liveries that vehicle carries.
  `[CODE New ex-15 @ 8b04b2114]`
- Matching is by livery NAME string (`vehicle_desc_t::check_livery`), so livery indices do
  not need to align between vehicles in a consist: an engine with 4 liveries and a tender
  with 5 share names, and each follows the same dated evolution. Retirement (`retire_year`)
  ends new purchase only and does not block later liveries appearing on owned stock, which
  is why short-lived classes carry liveries long past their retirement dates.
  `[CODE simutrans-extended ex-15 @ d4893f3]` (see `dataobj/livery_scheme.cc`,
  `get_latest_available_livery`; `vehicle.cc`, `update_livery`)
- The step-by-step vehicle tutorial confirms the procedure end to end: livery names come from
  the simuconf schemes, schemes are player-chosen per convoy, and dated liveries apply
  automatically; adding a livery is a new `liverytype[i]` line plus its image set.
  `[FORUM:https://forum.simutrans.com/index.php/topic,17510.0.html]`

## Rail livery production (measured method)

- Each rail livery is a separate `.blend` (for example `trains/Locomotives/ger-claud.blend`
  for GER ultramarine plus `ger-claud-ww1`, `-lner`, `-wartime`, `-br` blends), rendered to
  its own per-direction `.png` set (`ger-belpaire-claud-ww1_E.png` and peers) and indexed
  into the same `.dat` (`EmptyImage[dir][livery]` with matching `liverytype[i]` names).
  `[CODE New ex-15 @ 8b04b2114]`
- A livery differs from its sibling by body material values (for example `MainColour1`:
  GER ultramarine 0.07,0,0.35; LNER apple green 0,0.483,0.161; wartime and BR-early black
  0.1,0.1,0.1, all Blender Internal diffuse RGB as saved in the blends), plus lining and
  marking changes below. New liveries reuse the sibling values verbatim for consistency;
  the periodically updated standard list is the forum HSV post (see below).
  `[CODE GitBlends master @ 1c1acf58]`
- Markings live on dedicated layers enabled at render alongside the model layers: number
  and lettering `FONT` objects on layer 1 and/or 13 (cabside numbers with an offset dark
  shadow duplicate behind the light face, for example `6763` in `Lettering` straw
  0.76,0.8,0 over `Black lining` 0.12,0.12,0.12), and imported logo planes on layer 11.
  `[CODE GitBlends master @ 1c1acf58]`
- De-GER-ifying rule (measured across all four Claud non-GER blends, applied to the S69):
  every `Vermillion`-lineage material goes black (0.1,0.1,0.1); olive `Trim` is kept in all
  liveries; only BR darkens the roof (`Roof grey` 0.4 to 0.25). The BR crest lives on the
  tender only, never on the loco. `[CODE GitBlends master @ 1c1acf58]`
  `[RECOLLECTION:2026-09-25]`
- Wheel splashers are separate round arches (body color) with a light `Trim` edge ring,
  one per driving axle per side, fitted over the 6'6" drivers — not shared with the donor
  (Claud arches fit 7' drivers at other stations). `[RECOLLECTION:2026-09-25]`

## Logo and lettering components

- Reusable markings live in `Git Blends/Pak128.Britain-blends/components/`: `br-logo-1950s.dae`
  (simplified 1950s BR crest as flat gold/red planes) and `br-arrows.*` (the post-1966 BR
  arrows in `.blend`, `.dae`, `.ply`, `.stl`, `.x3d`), among lining, chimneys, domes, and
  other shared parts. `[CODE GitBlends master @ 1c1acf58]`
- Usage, as built in the shipped models: import the component into the working copy, place
  the flat planes just in front of the body surface that carried the logo in reality (the BR
  Claud carries red 0.26x0.28 and gold 0.13x0.46 `Logo` planes each side of the cab), and
  render with the marking layer enabled. Lettering that is words or numbers (cabside
  numbers, `L N E R`, wartime `N E`) is authored with Blender's text feature as `FONT`
  objects, converted to mesh at interchange time. `[CODE GitBlends master @ 1c1acf58]`
  `[RECOLLECTION:2026-09-25]`

## Standard livery colours

- The authoritative and periodically updated list of standardised livery colours, given as Blender
  HSV values, is the forum post
  https://forum.simutrans.com/index.php/topic,2401.msg140831.html#msg140831
  `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg140831.html#msg140831]`. Read that
  post at task time.
- It is not copied here, because it is updated periodically; see
  [conventions](../conventions.md) on pointing to changing data rather than duplicating it.
- The rules stated in that post: values are HSV; the value (intensity) is 0.800 unless the entry
  gives another figure; interior windows, and only interior windows, are `fg0,0,0`; any colour
  named "black" should be about `0,0,0.1`; aircraft use textures rather than Blender colours; and
  the list covers standardised liveries only, not non-standard items or non-livery parts such as
  wheels.

## Open questions

- Which special colours (indices 16–30) does this pakset actually use, and for which images?
- Which objects still require special colours, given that only multi-tile buildings now need
  post-processing?
- Should a snapshot of the standard livery colours be kept in the knowledge base, or is reading the
  forum post at task time acceptable? For any unattended tooling the answer must be "pin
  them": a script cannot read the forum post. `[RECOLLECTION:2026-09-27]`
- The component-colour convention for non-livery parts (frames, wheels, buffers, brass) is
  undocumented, though consistent in practice across many blends; the HSV post covers
  standardised liveries only. Material-role binding failures (one `Vermillion` lineage serving
  both connecting rods and buffer beam) show the convention needs writing down before role
  checks can exist. `[RECOLLECTION:2026-09-27]`
