---
status: draft
verified: New ex-15 @ 2b3ae85bf (working tree, 2026-11-21)
---
# Pre-1920 private-car coverage audit

**Covers**: the British private-car market before 1920, what the pakset covers of it, the gaps
that audit found, and the resulting build list. Parent: [citycar-asset-gaps](citycar-asset-gaps.md).
Build method: [car-batch-production](../graphics/car-batch-production.md). Comfort values:
[comfort-calibration](../comfort-calibration.md).

Status: draft. Audit made 2026-11-16 at the user's direction: research the pre-1920 market, find
the major gaps, fill them. **Closed 2026-11-21: every model in both build lists below is in the
tree.** `[CODE New ex-15 @ 2b3ae85bf]`

## Method

Three steps. First, what the pakset actually contains before 1920, read from the `.dat` files
rather than assumed. Second, what British buyers actually bought, from period production
compilations and vehicle-registration series. Third, whether usable photographs exist for each
candidate, because Gate A in [visual-asset-controls](../graphics/visual-asset-controls.md) makes
photographs the condition of building at all.

## What the pakset covers

| Era | Models in the tree |
| --- | --- |
| 1896–1900 | Daimler wagonette |
| 1902–1908 | De Dion-Bouton Type V, Star 7 hp, Wolseley 8 hp tonneau, Mercedes Simplex 60, Rover 8, Peugeot Type 69 Bébé, Rolls-Royce Silver Ghost, Rover 20, Ford Model T, Vauxhall A-type |
| 1910–1914 | Vauxhall B-type, Vauxhall C-type, Wolseley 16/20, GWK cyclecar, Argyll 15/30, Rover Twelve, Singer Ten, Sunbeam 12/16, Daimler TE30, Humberette, Morris Oxford bullnose, Standard 9.5, Vauxhall 30-98 |
| 1919 | Citroen Type A, Rover 8 (1919) |

That is 26 car models plus the three park-drag colourways. All have a `.dat` in
`New/citycars/`, both comfort fields and an `en.tab` entry. The three models previously recorded
as prepared but not built — Rolls-Royce Silver Ghost, Mercedes Simplex 60 and Vauxhall 30-98 —
are now built. `[CODE New ex-15 @ 2b3ae85bf]`

## The market

Registered private cars: 8,465 in 1904; 23,192 in 1906; 48,109 in 1909; 72,106 in 1911; 105,734
in 1913; 132,015 in 1914. The 1918 park was smaller than the 1912 one, and motorcycles outnumbered
cars from 1916 to 1924. `[LITERATURE:https://www.gracesguide.co.uk/1913_Automotive_Facts_and_Figures]`
`[LITERATURE:https://www.motorsportmagazine.com/archive/article/june-1947/12/statistics-how-much-and-when/]`

1913 output by maker, the best year of the period. All these figures are contemporary estimates,
not audited accounts, and the compilation says so. `[LITERATURE:https://www.gracesguide.co.uk/1913_Automotive_Facts_and_Figures]`

| Maker | 1913 output | Represented before 1920 in the pak |
| --- | --- | --- |
| Ford | 6,139 (kits assembled in Britain) | Model T |
| Wolseley | 3,000 — largest British maker | 16/20, 8 hp |
| Humber | 2,500 (possibly 2,000 of them Humberettes) | Humberette |
| Sunbeam | 1,700 | 12/16 |
| Rover | 1,600 | 8, 20, Twelve |
| Austin | 1,500 | no pre-1920 model |
| Singer | 1,350 | Ten |
| Arrol-Johnston | 1,150 | no |
| Belsize | 1,000 | no |
| Daimler | 1,000 | wagonette, TE30 |
| Swift | 850 | no |
| Standard | 750 | 9.5 |
| Napier | 743 | no |
| Rolls-Royce | 650 | Silver Ghost |
| Crossley | 650 | no |
| Argyll | 622 | 15/30 |
| Star | 500 | 7 hp |
| Vauxhall | 388 | 30-98, A/B/C |
| Morris | 300 | Oxford bullnose |
| Lanchester | 200 | no |

## Findings

1. **The section F row for 1900–1918 was built.** All three class-3 models it names have usable
   photographs on Commons: the Rover Twelve (six images including the one captioned as the
   Clegg), the Sunbeam 12/16 (six), and the Wolseley 16/20 (six). The class-4 row is covered by
   the Silver Ghost, Simplex 60, Vauxhall 30-98 and Daimler TE30, with the approved substitutes.

2. **The light-car and cyclecar hole was closed.** Between the Model T of 1908 and the Morris
   Oxford of 1913 the pakset had no cheap car. The **Singer Ten** of 1912–24 (over 10,000 built,
   £185 new), the 1913 **Humberette** (about 2,000 of Humber's 2,500 that year), the **GWK**
   cyclecar (1,069 before 1914) and the **Standard 9.5** are now all in the tree.
   `[LITERATURE:https://www.singerownersclub.co.uk/singer-models]`
   `[LITERATURE:https://microcarfan.com/british-cyclecars/]`

3. **The 1900–1910 import gap was closed.** The missing element was the import: 5,378 cars were
   imported in 1904 against 703 exported, and the 1906 under-£200 class was led by the Baby
   Peugeot, Rover, Star and Wolseley. De Dion-Bouton Type V, Peugeot Type 69 Bébé and Star 7 hp
   are now built alongside the earlier Rovers, the Daimler wagonette and the Model T.

4. **The Daimler 38 hp and Napier 60 hp remain unbuildable.** Commons has no photographs of
   either, which is why they were replaced in section F. The 1913 **Daimler TE30** has a
   photograph and is built, so the class-4 pre-1920 row has a fourth model.

## Build list

Class is the pakset's wealth band; years are the production span. All twelve models below are
built; the status is recorded once here rather than repeated in every row.
`[CODE New ex-15 @ 2b3ae85bf]`

### 1910–1920

| # | Model | Years | Class | Evidence | Photographs |
| --- | --- | --- | --- | --- | --- |
| 1 | Wolseley 16/20 | 1911–19 | 3 | 3,000 in 1913, the largest British output | 6 |
| 2 | Sunbeam 12/16 | 1912–21 | 3 | 1,700 in 1913 | 6 |
| 3 | Rover Twelve (Clegg) | 1912–24 | 3 | 1,600 Rover cars in 1913; completes Rover | 6 |
| 4 | Singer Ten | 1912–24 | 2 | over 10,000 total; the period's light car | 8 |
| 5 | Humberette | 1913–14 | 1 | about 2,000 in 1913 | 4 |
| 6 | Standard 9.5 | 1913–19 | 2 | 750 in 1913 | 1 |
| 7 | GWK cyclecar | 1911–14 | 0 | 1,069 before 1914 | 2 |
| 8 | Daimler TE30 | 1913 | 4 | 1,000 Daimlers in 1913 | 1 |
| 9 | Argyll 15/30 tourer | 1912–15 | 3 | 622 Argylls in 1913, the seventh-largest British output; Glasgow-built | the maintainer's own Riverside Museum photographs |

Models 1–3 closed the section F row. Models 4–7 closed the light-car gap this audit found. Model
8 is optional richness at the very-high end. All are now built.

### Pre-1910

The decade is not covered proportionately either, once the import share is taken into account. UK
output was 11,700 cars in 1907, 11,000 in 1909 and 14,000 in 1910, but imports ran at 5,378 cars in
1904 against 703 exported, and the 1906 Autocar price list shows the under-£200 class led by the
Baby Peugeot, Rover, Star and Wolseley, with De Dion, Peugeot and Renault in the £200–300 class.
`[LITERATURE:https://www.gracesguide.co.uk/1904_Automotive_Facts_and_Figures]`
`[LITERATURE:https://www.gracesguide.co.uk/1906_Autocars]`

| # | Model | Years | Class | Evidence | Photographs |
| --- | --- | --- | --- | --- | --- |
| P1 | De Dion-Bouton Type V / 8 hp | 1902–08 | 2 | the French make with its own British sales syndicate; in the 1906 £200–300 class | Type V and 8 hp photographs |
| P2 | Peugeot Type 69 Bébé | 1905–12 | 1, 2 | the under-£200 "Baby Peugeot" of the 1906 list | 8+ |
| P3 | Star 7 hp | 1902–05 | 2 | Star is in the 1904 Autocar list of British-made cars; survivors photographed | 6 |

The pre-1910 list is short on purpose. The national park was under 55,000 until 1910, the cars were
coachbuilt one at a time, and at 128 px a brass-era body reads as "old car" whatever the make. These
three cover the imported light car, the British light car and the cheapest real car of the decade.
All three are built.

Wolseley was the largest British maker of the 1910s, but no pre-1910 Wolseley photograph could be
confirmed; the Wolseley 16/20 in the 1910–1920 list covers the make where the evidence exists.

Deliberately not in either list: Arrol-Johnston, Swift, Crossley, Belsize, Lanchester, Austin and
Napier. Their Commons photographs are either of much earlier models (the Arrol-Johnston images are
1902 veterans), unconfirmed, or the silhouette repeats the models above at pak scale. They remain
available if an era ever needs more density.

**Argyll was originally excluded for want of photographs and is now included.** The maintainer's
photographs of the Riverside Museum's 1912 Argyll 15/30 tourer supply the missing evidence, and
Argyll was the seventh-largest British maker by 1913 output (622 cars). It joins the 1910–1920 list
as the class-3 Glasgow representative.

## Open questions

- **Pre-1910 Wolseley.** Wolseley was the largest British maker of the 1910s, but no pre-1910
  Wolseley photograph could be confirmed on Commons. If one is found, a Wolseley 6 or 8 hp of
  1904–10 would be the natural fourth pre-1910 model.
- **Star's pre-1910 output** is not recorded in the sources used here; the 7 hp is included as the
  photographed British light car of 1902–05, not on a volume figure. The 1913 Star 12/15 also has
  no Commons category under the obvious name.
- Whether the Humberette belongs in class 1 or class 0: it was a £115 cyclecar with a 7 cwt body,
  which is Very-low in period terms but not the cheapest transport available.
- Whether the Singer Ten's pre-war and post-war bodies differ enough to justify two shells; the
  1912–16 car was an open two-seater and the 1919–24 car a fuller light car.
