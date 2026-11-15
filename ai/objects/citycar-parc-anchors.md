---
status: draft
verified: New ex-15 @ 66e9c2dfd
---
# Private-car popularity anchors (parc research)

**Covers**: the research record underpinning `DistributionWeight` rebasing for private cars: the
most numerous car model in use on GB roads at 5-year points 1920–2025, the evidence and
confidence for each point, and whether each model exists in `New/citycars/`. Field definitions
and the colour-share method: [citycar](citycar.md). Source practice:
[research-and-forum](../research-and-forum.md). Claim tags: [claim-tags](../claim-tags.md).

## Purpose and measure

`[USER-DIRECTION:2026-11-15]` For private cars, `DistributionWeight` (the citycar's spawn
frequency relative to other citycars; see [citycar](citycar.md)) only ever means **relative**
popularity at a given time compared with other cars; absolute car frequency is determined
elsewhere. The most popular car on the road at a given time is the anchor:
`DistributionWeight = 100`, assuming 5 colourways. A model with fewer colourways scales
inversely (single colourway, e.g. `FordT(Black)`, → 500). All other cars of that era are
weighted relative to the anchor.

Popularity is measured as the **number of that model in use on GB roads (the parc)**, not
new-car sales. `[USER-DIRECTION:2026-11-15]`

## Data-availability limits

No official GB in-use statistics broken down by make and model exist for 1920–1993. The
DfT/DVLA make-and-model licensing series (`df_VEH0120_GB`) begins at 1994 Q4 only
`[LITERATURE:https://www.gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files]`;
UK model-level registration statistics were secret until 1969
`[LITERATURE:https://autos.yahoo.com/policy-and-environment/articles/why-british-car-makers-kept-180851225.html]`;
pre-war Ministry of Transport returns classified cars only by taxation class
`[LITERATURE:https://api.parliament.uk/historic-hansard/written-answers/1947/mar/12/motor-vehicle-licences]`.
Rows before 1990 therefore rest on proxies. Evidence types used in the table: **(a)** genuine
in-use/parc figure; **(b)** best-seller or cumulative-production proxy; **(c)** period or expert
narrative.

## The anchor table

Pakset membership checked against `New/citycars/` at the frontmatter commit (2026-11-15);
re-derive live membership from the folder before relying on it. Key sources are abbreviated in
the Evidence column and listed with full references at the end.

| Year | Most popular car on the road (parc) | Evidence | Conf. | In pakset? |
| --- | --- | --- | --- | --- |
| 1920 | Ford Model T | (a) 1919: 41% of registered cars were Fords [S1] | High | Yes — `FordT` (`ford-t.dat`) |
| 1925 | Ford Model T | (b) 250,000th British Ford Apr 1925 vs 154,244 total Bullnose Morrises [S2] | Medium | Yes — `FordT` |
| 1930 | Morris Cowley | (b) 350k+ built by 1931; period "most popular car on the British market" claim [S3] | Low | Partial — twin models `MorrisOxfordBullnose` / `MorrisOxfordFlatnose` only |
| 1935 | Morris Cowley or Austin Seven (unresolvable) | (b) proxies only [S3][S4] | Low | Partial (as above) / Yes — `AustinSeven` |
| 1940 | Morris Eight | (b) ~250,000 sold by outbreak of war; best-seller of late 1930s [S5] | Medium | Yes — `MorrisEight` |
| 1945 | Morris Eight | (b)/(c) wartime parc frozen; pre-1930 cars scrapped [S5][S6] | Medium-low | Yes — `MorrisEight` |
| 1950 | Unresolved: no model-level evidence exists | (c) only a 1949 make-level roadside count (Austin 21%, Morris 16%) [S7] | — | Candidates all present (`MorrisEight`, `AustinTen`/`AustinTen1937`, `MorrisMinor`) |
| 1955 | Morris Minor | (c)+(b) narrative + ~393k built by end-1955 [S8] | Low-medium | Yes — `MorrisMinor` |
| 1960 | Morris Minor | (b) ~885k cumulative; 1,000,000th Dec 1960 [S8] | Low | Yes — `MorrisMinor` |
| 1965 | Morris Minor (stock inference) vs BMC 1100 (sales proxy) — conflicting measures | (b) 1100 was best-seller 1965 (157,679) [S9]; Minor led on accumulated stock [S8] | Low | `MorrisMinor` yes; **BMC 1100 no** |
| 1970 | BMC 1100/1300 (ADO16) | (b) best-seller 1968–71; 2.15m built [S9][S10] | Low-medium | **No** |
| 1975 | Ford Cortina | (b) #1 new-car seller 1972–75; ~2.8m UK sales [S9][S10] | Medium | Yes — `FordCortina` |
| 1980 | Ford Cortina | (b) best-seller 1980 (190,281); 1.41m registered in the 1970s [S11] | Low | Yes — `FordCortina` |
| 1985 | Ford Escort (Mk3) | (b) best-seller 1982–85; Cortina alternative unexcluded [S9] | Low | Yes — `FordEscort-mk3` |
| 1990 | Ford Escort | (a) DVLA extract Dec 1989: Escort Mk3 alone >1.5m, 50%+ ahead of #2 [S12] | Medium-high | Yes — `FordEscort-mk3` / `FordEscort-mk4` |
| 1995 | Ford Escort | (a) VEH0120 1995 Q4: 1.67m licensed [S13] | High | Yes — `FordEscort-mk4` |
| 2000 | Ford Fiesta (cars-only measure; Escort leads if car-derived vans are counted with the model) | (a) VEH0120 2000 Q4: Fiesta 1.52m vs Escort 1.40m [S13] | Medium | Yes — `FordFiestaMk4`/`FordFiestaMk5` (added 2026-11-15) |
| 2005 | Ford Fiesta | (a) VEH0120 2005 Q4: 1.26m licensed [S13] | High | Yes — `FordFiestaMk5`/`FordFiestaMk6` (added 2026-11-15) |
| 2010 | Ford Focus | (a) DfT: most common model "unchanged since 2008"; #1 at end-2011 (1.4m) [S14] | Medium | Yes — `FordFocus` |
| 2015 | Ford Fiesta (took the lead during Q4 2015; Focus led earlier in the year) | (a) VEH0120: Fiesta 1,427,082 at end-2015 [S15] | High | Yes — `FordFiestaMk6`/`FordFiestaMk7` (added 2026-11-15) |
| 2020 | Ford Fiesta | (a) DfT VEH0128: 1.5m vs Focus 1.2m; SMMT Motorparc agrees [S16] | High | Yes — `FordFiestaMk7` (added 2026-11-15) |
| 2025 | Ford Fiesta | (a) SMMT Motorparc 2025: 1,368,335, only model above 1m [S17] | High | Yes — `FordFiestaMk7` (added 2026-11-15) |

## Coverage gaps found by this research

1. **Ford Fiesta** — CLOSED 2026-11-15: `FordFiestaMk1`–`Mk7` added (`ford-fiesta-mk1.dat`
   to `ford-fiesta-mk7.dat`, 28 colourway objects, 7 generations spanning 1977–2023 road
   presence). It was the parc leader at five sample points (2000, 2005, 2015, 2020, 2025).
2. **BMC/Morris 1100/1300 (ADO16)** — dominant UK car 1963–71; without it, the 1965 and 1970
   rows have no true anchor.
3. **Morris Cowley** (1926–1935) — only its twin models are present. The
   `MorrisOxfordFlatnose` .dat already declares it "intended to represent also the very similar
   Morris Oxford Six"; whether it should also stand for the Cowley is open.
4. **1950 is unresolvable** from published sources; its likely candidates are all present, so
   the anchor for that era has to be fixed by mutual scaling instead.
5. Absent but relevant to surrounding traffic density (never an anchor row): Ford Anglia, Ford
   Escort Mk2, Vauxhall Cavalier/Astra/Corsa, VW Beetle/Golf.

## Sources

- [S1] `[LITERATURE:https://www.britainbycar.co.uk/trafford-park/341-ford-motor-co-ltd]` — 1919:
  41% of British registered cars were Fords (Ford in Britain, Eric Dymock). Corroborated at
  `[LITERATURE:https://earlyfordregistry.org/library/the-importance-of-fords-early-presence-in-europe/]`.
- [S2] `[LITERATURE:https://morris-archive.co.uk/F-L-I-P/pflip/PDFS/reviews1/Cowley_Profile-fb.pdf]`
  (Morris Archive, *Cowley Profile*); Model T best-seller 1913–23 and lost the lead to Morris in
  1924: `[LITERATURE:https://doi.org/10.1017/s0022050725000014]` (Eli, Hausman & Rhode, *The Model
  T*, J. Econ. Hist. 85(1), 2025).
- [S3] `[LITERATURE:https://morris-archive.co.uk/F-L-I-P/pflip/PDFS/reviews0/1933cars_MO_09_32.pdf]`
  (*Morris Owner*, Sept 1932: "For a whole decade the Morris Cowley has held its place as the most
  popular car on the British market"); builds:
  `[LITERATURE:https://www.gracesguide.co.uk/Morris:_Flatnose]`.
- [S4] Austin Seven cumulative figures:
  `[LITERATURE:https://www.classicandsportscar.com/features/austin-seven-100-car-got-britain-moving]`,
  `[LITERATURE:https://www.hemmings.com/stories/austin-seven/]`.
- [S5] Morris Eight: `[LITERATURE:https://nationalmotormuseum.org.uk/collections/vehicles/morris-eight-series-ii/]`;
  `[LITERATURE:https://wrap.warwick.ac.uk/id/eprint/36384/1/WRAP_THESIS_O%27Connell_1995.pdf]`
  (O'Connell PhD thesis, Warwick 1995); `[LITERATURE:https://morris8.nz/wp-content/uploads/2025/06/M8-Profile.pdf]`.
- [S6] Wartime parc: `[LITERATURE:https://archive.commercialmotor.com/article/9th-august-1946/41/new-registrations-drop-by-80-per-cent]`;
  pre-1930 fleet near-extinct by 1947:
  `[LITERATURE:https://www.motorsportmagazine.com/archive/article/june-1947/12/statistics-how-much-and-when/]`.
- [S7] 1949 Austin roadside count (make level):
  `[LITERATURE:https://www.motorsportmagazine.com/archive/article/december-1952/24/austin-popularity/]`.
- [S8] Morris Minor production:
  `[LITERATURE:https://www.morrisminorspares.com/production-figures-i19]`;
  1,000,000th in Dec 1960: `[LITERATURE:https://en.wikipedia.org/wiki/Morris_Minor]`.
- [S9] SMMT best-seller tables 1965–1999:
  `[LITERATURE:https://www.aronline.co.uk/facts-and-figures/best-selling-cars-1965-1999/]`;
  `[LITERATURE:https://www.autoexpress.co.uk/car-news/95144/best-selling-cars-1965]`;
  `[LITERATURE:https://www.autoexpress.co.uk/car-news/95146/best-selling-cars-1975]`.
- [S10] ADO16 and Cortina volumes: `[LITERATURE:https://www.aronline.co.uk/cars/mini/bmcmgs-top-ten-sellers-1952-2005/]`;
  `[LITERATURE:https://www.aronline.co.uk/news/news-cortinas-50th-celebrated-on-the-beeb/]`.
- [S11] 1980s registrations: `[LITERATURE:https://bestsellingcarsblog.com/1982/01/uk-1980-1981-last-years-of-ford-cortina-domination/]`.
- [S12] Home Office Car Theft Index (Houghton 1992, DVLA records at Dec 1989), quoted in
  `[LITERATURE:https://onlinelibrary.wiley.com/doi/10.1111/hojo.12158]` (Farrell 2016, *Howard
  Journal*).
- [S13] DfT VEH0120 per-model series (1994 Q4 onward):
  `[LITERATURE:https://www.stillontheroad.co.uk/cars/FORD/ESCORT]` and sibling per-model pages.
- [S14] DfT vehicle licensing statistics 2011 and quarterly releases:
  `[LITERATURE:https://www.gov.uk/government/statistics/vehicle-licensing-statistics-2011]`;
  `[LITERATURE:https://assets.publishing.service.gov.uk/media/5a800983ed915d74e622c192/vls-q2-2015.pdf]`.
- [S15] DfT vehicle licensing statistics 2015:
  `[LITERATURE:https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/516429/vehicle-licensing-statistics-2015.pdf]`.
- [S16] DfT vehicle licensing statistics 2020:
  `[LITERATURE:https://www.gov.uk/government/statistics/vehicle-licensing-statistics-2020/vehicle-licensing-statistics-2020.pdf]`;
  SMMT Motorparc 2020: `[LITERATURE:https://www.smmt.co.uk/britains-cars-getting-older-but-van-ownership-reaches-historic-highs/]`.
- [S17] SMMT Motorparc 2025:
  `[LITERATURE:https://www.best-selling-cars.com/britain-uk/2025-britain-total-number-of-cars-motorparc-on-british-roads/]`;
  DfT VEH0120-derived: `[LITERATURE:https://www.ukmotoring.co.uk/statistics/most-popular-cars/]`.

## Open questions

- Should the missing anchor models (Ford Fiesta, BMC 1100/1300) be built as new citycars? If
  not, the affected eras must be anchored by the next-most-popular model present.
- Should `MorrisOxfordFlatnose` stand for the Morris Cowley as well (as it already does for the
  Morris Oxford Six), or should a separate Cowley object be added?
- 1935: Cowley vs Austin Seven cannot be resolved from the sources found. A period census or
  registration record could settle it; none was found.
- 2000: the ranking flips if car-derived vans are counted with the model (Escort first) instead
  of the cars-only measure (Fiesta first). Which measure should the weights use? The cars-only
  measure is the standard published one.
