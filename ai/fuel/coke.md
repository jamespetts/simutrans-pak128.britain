---
status: draft
verified: New ex-15 working tree, 2026-11-24
---
# Coke prices

**Covers**: British coke price series by grade (gas coke; furnace and foundry coke), 1846-2026,
with the basis of each figure (at ovens, ex works, delivered, f.o.b.). Read before pricing coke as
a fuel in `config/fuel.tab`, or before using coke to check a steam vehicle's fuel cost. The
research record: [cost-balancing/research-pricing-report-39](../cost-balancing/research-pricing-report-39.md)
§7.2. Coal itself: [coal](coal.md).

## Why coke has its own series

The steam tramways issued coke, not coal ([steam-tram-derivation](steam-tram-derivation.md)), and
early coke-burning railways are in the same position; charging them the coal price understates
their fuel by roughly a half. The observed coke:coal price ratio is **about 1.5-2.5** at every date
checked (1863, 1907, 1913-14, 1930s).

**Grade matters.** *Gas coke* is what the steam tramways burned and is the grade to use for tram
and early-railway fuel. *Furnace/foundry coke* is the metallurgical grade quoted by the trade press
and Hansard; it is usually dearer and must not be mixed into a gas-coke series without a note.

## The series (2,240 lb ton pre-1971)

| Year | Grade and basis | Figure | Source |
|---|---|---|---|
| 1846, 1848, Jan 1849 | Coke at the ovens, John Bowes & Partners, Durham | 9s, 9s, 8s | Mountford, *History of John Bowes & Partners up to 1914* (Durham M.A. 1967) pp.120-21 |
| 1853 | Marley Hill coke at ovens | 13s | same |
| 1868-69 | Coke contract (Bowes with Palmers) | 10s 6d net | same |
| c.1862-63 | Durham coke at the mines 8s-9s (cost 8s: coal 6s 9d + making 1s 3d); delivered Cleveland 10s-11s; best coke f.o.b. Tyne 12s 6d-14s | as stated | Gruner & Lan, *Mining and Smelting Magazine* June 1863 p.324 |
| 1873 | Pontop ovens coke contract | 23s (yr 1), 18s (yr 2) | Mountford p.131 (Strathmore MSS, Durham CRO) |
| 1881 | Gas coke, Dewsbury (steam tram fuel) | 23s 6d | Kinnear Clark, *Tramways* (1894) p.453 |
| 1907 | Gas coke and breeze ex works, UK gas undertakings, average value of output | 11s 8¼d (companies 12s 7d; public authorities 10s 2d) | Census of Production 1907 Preliminary Tables Part IX |
| 1914-17 | Foundry coke f.o.b. Tyne 19s-23s; best Durham blast-furnace coke Tees-side 19s (Jan 1915) → 36s (Jan 1916) → 42s 6d (Jul 1916) | as stated | Redmayne, *The British Coal-Mining Industry During the War* (1923) pp.9, 48, 85 |
| 1919 | Foundry coke f.o.b. Tyne 49s 6d-110s by market | as stated | same p.228 (column-mapping caveat) |
| Feb 1920 | Gas coke exports £4 13s 9d; other coke £5 0s 6d | f.o.b. average value | Hansard HC 15 Mar 1920 c1770 |
| Q1 1922 / Q1 1923 | Gas coke exports 30s 6d / 29s 2d | f.o.b. average value | Hansard HC 2 Jul 1923 cc44-5 |
| 1926 | Gas coke, Wotton-under-Edge gasworks | 24s 6d | R. Wilson, GSIA Journal 1998 (secondary) |
| Mar 1930-38 | Durham furnace coke delivered Middlesbrough | 20.00, 16.00, 16.35, 15.50, 20.10, 19.13, 23.13, 28.50, 36.00s | Hansard HC 13 Apr 1938 c1117 (Colliery Guardian quotations) |
| Nov 1945 | Large coke, London, ex gas works 59s 3d-64s 5d by lot; 74s 10d retail | as stated | Hansard WA 20 Nov 1945 cc400-1W |
| 1959-65 | Gas coke, area gas boards average realisation | £7.47 → £9.57 (8.4m → 7.4m tons p.a.) | Hansard WA 1 Feb 1966 c181W (Ministry of Power digest) |
| 1960 | Bagged branded gas coke retail, south London | 11s 6d per cwt (≈£11 10s/ton) | Hansard HC 28 Nov 1960 |
| May 1968 | Gas coke basis-price increase | +25s a ton (NBPI-approved) | Hansard WA 23 May 1968 c135W |
| 2017-26 | Metallurgical coke, European export benchmark | €194/t (Jan 2021) → €519-722/t (2022 peak) → €270-380/t (mid-2026) | steelonthenet (Trade Data Monitor data) |

**Modern Britain has no coke ovens** (Port Talbot closed 20 Mar 2024, DUKES 2026 ch.2), so the
defensible modern series is EU import parity; the ONS PPI "Coke and refined petroleum products"
(GBBK) is an index only and mixes the categories.

## Gaps and routes

1816-1914 continuous: Matthews, *The London Gasworks* (Hull PhD 1981) Figure 11 is the one document
that would close the whole steam era — the Hull repository PDF is Cloudflare-blocked to automated
access (browser session, BL EThOS or Hull library). Annual gas-coke levels 1882-1935 come from the
BPP "Return relating to all authorised Gas Undertakings" (coke sold and value per undertaking;
HathiTrust is completely blocked to this client — ProQuest/library route). Also: *Gas World*/*Gas
Journal* annual reviews; Colliery Guardian quotations (BNA/Gale) for furnace coke pre-1930; Durham
Record Office NCB I/CO 493-494 (coke price ascertainments 1924-47) and I/CO 81-85 (selling-price
certificates 1871-1946); pre-1845 via early railway coke contracts (S&DR, L&M minutes, RAIL).

## Open questions

- Is a coke-burning tramway or railway to be charged `fuel[steam]` at the coke series once it
  exists as a separate `fuel[]` entry, or is `fuel[steam]` itself to become a weighted blend?
- The 1873 "average price" of 36s (Mountford p.176) is scope-ambiguous (probably furnace coke) and
  the 1878 figure is OCR-uncertain; neither should anchor a level without confirmation.
