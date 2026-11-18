---
status: draft
verified: New ex-15 @ f05e52352
---
# Pre-1920 private-car coverage audit

**Covers**: the British private-car market before 1920, what the pakset covers of it, the gaps
that audit found, and the resulting build list. Parent: [citycar-asset-gaps](citycar-asset-gaps.md).
Build method: [car-batch-production](../graphics/car-batch-production.md). Comfort values:
[comfort-calibration](../comfort-calibration.md).

Status: draft. Audit made 2026-11-16 at the user's direction: research the pre-1920 market, find
the major gaps, fill them.

## Method

Three steps. First, what the pakset actually contains before 1920, read from the `.dat` files
rather than assumed. Second, what British buyers actually bought, from period production
compilations and vehicle-registration series. Third, whether usable photographs exist for each
candidate, because Gate A in [visual-asset-controls](../graphics/visual-asset-controls.md) makes
photographs the condition of building at all.

## What the pakset covers

| Model | File | Objects | Years | Class |
| --- | --- | --- | --- | --- |
| Daimler wagonette | `daimler-wagonette.dat` | 3 | 1896–1900 | 3, 4 |
| Rover 8 | `rover-8.dat` | 3 | 1904–07 | 3 |
| Rover 20 | `rover-20.dat` | 3 | 1907–08 | 3 |
| Ford Model T | `ford-t.dat` | 1 | 1908–1935 | 0–3 |
| Morris Oxford bullnose | `morris-oxford-bullnose.dat` | 4 | 1913–16 | 2, 3 |
| Citroën Type A | `citroen-type-a.dat` | 3 | 1919–20 | 2, 3 |
| Rover 8 (1919) | `rover-8-1919.dat` | 5 | 1919–21 | 2, 3 |

Prepared but not built: Rolls-Royce Silver Ghost, Mercedes Simplex 60 hp, Vauxhall 30-98.
`[CODE New ex-15 @ f05e52352]`

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
| Wolseley | 3,000 — largest British maker | no |
| Humber | 2,500 (possibly 2,000 of them Humberettes) | no |
| Sunbeam | 1,700 | no |
| Rover | 1,600 | Rover 8, Rover 20 |
| Austin | 1,500 | no |
| Singer | 1,350 | no |
| Arrol-Johnston | 1,150 | no |
| Belsize | 1,000 | no |
| Daimler | 1,000 | wagonette of 1896 only |
| Swift | 850 | no |
| Standard | 750 | no |
| Napier | 743 | no |
| Rolls-Royce | 650 | Silver Ghost prepared |
| Crossley | 650 | no |
| Argyll | 622 | no |
| Star | 500 | no |
| Vauxhall | 388 | 30-98 prepared |
| Morris | 300 | Oxford bullnose |
| Lanchester | 200 | no |

## Findings

1. **The section F row for 1900–1918 is buildable as written.** All three class-3 models it names
   have usable photographs on Commons: the Rover Twelve (six images including the one captioned
   as the Clegg), the Sunbeam 12/16 (six), and the Wolseley 16/20 (six). The class-4 row is
   already covered by the three prepared models and the approved substitutes.

2. **The real hole is the light-car and cyclecar end, which no section of the register records.**
   Between the Model T of 1908 and the Morris Oxford of 1913 the pakset has no cheap car at all.
   The biggest-selling British light car of the period is absent: the **Singer Ten** of 1912–24,
   over 10,000 built, £185 new, the car that took Singer from a bicycle maker to a volume car
   producer. The 1913 **Humberette** — about 2,000 of Humber's 2,500 that year — and the **GWK**
   cyclecar (1,069 before 1914, the only firm cyclecar figure) are the other volume sellers, and
   the cyclecar boom of 1912–14 was the pre-1920 equivalent of the motorcycle outfit for buyers
   who could not afford a full car.
   `[LITERATURE:https://www.singerownersclub.co.uk/singer-models]`
   `[LITERATURE:https://microcarfan.com/british-cyclecars/]`

3. **1900–1910 is not covered proportionately either.** Four built models cover 1896–1908: the
   Daimler wagonette, two Rovers and the Model T. The missing element is the import: 5,378 cars
   were imported in 1904 against 703 exported, and the 1906 under-£200 class was led by the Baby
   Peugeot, Rover, Star and Wolseley, with De Dion, Peugeot and Renault just above. Three models
   close the decade: De Dion-Bouton, Peugeot Bébé and Star 7 hp.

4. **The Daimler 38 hp and Napier 60 hp remain unbuildable.** Commons has no photographs of
   either, which is why they were replaced in section F. A 1913 **Daimler TE30** does have a
   photograph, so a fourth class-4 pre-1920 model is possible if wanted.

## Build list

Class is the pakset's wealth band; years are the production span.

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

Models 1–3 close the section F row. Models 4–7 are the light-car gap this audit found. Model 8 is
optional richness at the very-high end.

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
