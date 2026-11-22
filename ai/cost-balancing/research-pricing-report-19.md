# Research pass 19 — measured British maintenance of bridges and tunnels

Status: draft evidence. Compiled 2026-11-22. Output for the parent session. The knowledge base is
not edited here.

**Covers**: annual maintenance of bridges and tunnels, per metre-year and per structure-year, split
by material; maintenance as a share of capital; timber deck renewal; canal aqueducts. Nominal money
throughout, with the year of the price.

**Question addressed**: the infrastructure maintenance column has measured upkeep for permanent way
and for stations but not for the 17 bridge objects or the tunnel material variants. This pass looks
for British measured rates to fill that column, using Cudworth 1886 as the anchor.

---

## 1. Method, and what "measured" means here

Three evidence classes are kept apart, and every row in the CSV carries one of them in its notes:

- **Measured** — an account, contract or statutory return for a named structure over a stated
  period. Cudworth's viaduct figures and the London County Council (LCC) bridge table are measured.
- **Derived** — a measured total divided by a measured length or a measured capital sum, for
  example the Forth Bridge £1m over 2,467 m, or an LCC maintenance figure over a bridge length.
  The arithmetic is shown in the row so it can be checked.
- **Inferred** — a rate transferred from one material to another on the strength of a stated
  ranking. Thorpe's material ordering is the only source used this way, and every such row says so.

Lengths used for the per-metre conversions come from the structure's own recorded dimensions
(Forth Bridge 2,467 m; Union Chain span 137 m; Pontcysyllte 307 m) or from the bridge infobox
(LCC bridges). Those are secondary for length only, never for cost.

---

## 2. The anchor re-examined: Cudworth 1886

The paper is **three pages long** (ICE Minutes of Proceedings vol. 85, pp. 340-342, Paper No. 2128)
and covers **only the Belah and Deepdale viaducts**. There is no third structure, no brick arch
series and no tunnel content in it. The eighteen-year account run is the whole of the quantitative
content.

That settles one question: Cudworth cannot be extended within its own paper. Anything further has
to come from a different source, which is what sections 3 to 6 do.

The four figures already in the knowledge base are confirmed and are the only measured railway
viaduct rates found in this pass:

| Structure | Material | Rate | Ratio to plain line |
|---|---|---:|---:|
| Belah Viaduct, 195 ft high | iron | £0.25/m-yr | 1.32 |
| Deepdale Viaduct, 158 ft high | iron | £0.23/m-yr | 1.21 |
| Hownes Gill Viaduct | firebrick | £0.05/m-yr | 0.26 |
| Plain line, for comparison | — | £0.19/m-yr | 1.00 |

---

## 3. Bridges by material

### 3.1 Iron — measured, high confidence

£0.23-0.25 per metre-year (1886, eighteen-year mean of North Eastern Railway accounts). Two
independent structures of different height agree within 9 per cent, which is the strongest feature
of the whole dataset: **height barely affects upkeep per metre** once the structure is standing.

### 3.2 Brick — measured, high confidence for one structure

£0.05 per metre-year (1886, Hownes Gill). One structure only. It is a firebrick arch viaduct, so it
is a true brick masonry rate, but it is a single observation and the paper gives no second brick
structure to test it against.

### 3.3 Stone and masonry — measured, but not for a railway viaduct

No British railway masonry viaduct upkeep rate was found. The measured masonry figures are the LCC
Thames road bridges, 1907-08:

| Bridge | Material | Length | Upkeep | Per metre-year | Share of capital |
|---|---|---:|---:|---:|---:|
| Waterloo (1817) | stone arch | 375 m | £1,102 | £2.94 | 0.20% |
| Putney (1886) | stone arch | 213 m | £653 | £3.07 | 0.15% |
| Westminster (1862) | iron arches on granite piers | 250 m | £1,491 | £5.96 | 0.38% |
| Vauxhall (1906) | steel arch | 247 m | £1,109 | £4.49 | 0.24% |
| Hammersmith (1887) | suspension | 213 m | £421 | £1.98 | 0.21% |
| Battersea (1890) | iron | 221 m | £512 | £2.32 | 0.16% |
| Wandsworth (1873) | iron lattice | 198 m | £410 | £2.07 | 0.62% |
| Albert (1870) | suspension, timber deck | 216 m | £1,296 | £6.00 | 1.07% |
| Lambeth (1862) | suspension | not verified | £496 | — | 1.04% |

These are **10 to 25 times the railway viaduct rates**, and the reason is not material. A Thames
road bridge is 15-20 m wide, carries horse and later motor traffic, has footways, parapets,
lighting, gas and water mains, and in several cases a timber deck. A single-track railway viaduct
is about 5 m wide and carries nothing but rail traffic.

The correct reading is therefore: **the LCC figures measure a road bridge per metre of length, not
a material.** They are usable for a road bridge object. They are not usable to set a railway
masonry viaduct rate, and the gap between £0.05 (brick rail viaduct) and £2.94 (stone road bridge)
should not be read as a material effect.

For the railway masonry viaduct the only evidence is qualitative, and it points **below** brick:
Thorpe (1906) says masonry bridges "will be practically nothing in favourable cases" and ranks
masonry first for low maintenance charges.

### 3.4 Steel — derived, low confidence for a small bridge

Two figures, neither of them a typical underbridge:

- **Forth Bridge, 1993: £405 per metre-year** (£1m a year over 2,467 m; £450,000 labour, £65,000
  materials, £425,000 contracts). A 2,467 m steel cantilever over a tidal estuary, carrying about
  200 trains a day, with 135 acres of paint. This is an upper bound by a wide margin.
- **Thorpe 1906: painting alone is 0.33-1.0 per cent of first cost a year** for wrought iron or
  steel, at 5d to 1s per square yard on a five-year cycle, with steel "somewhat higher" because
  the interval is shorter. Thorpe also states that steel corrodes faster than iron and needs more
  attention, which supports a steel rate modestly above the iron rate.

No British per-metre series for a steel plate-girder underbridge was found. The defensible
inference is that **steel sits slightly above iron** and well below the Forth Bridge figure.

### 3.5 Concrete — no measured basis

Nothing found. The 1905 ICE paper on the Cannington and Holsworthy concrete viaducts gives capital
cost (32s 1d and about 30s per cubic yard; £10,820 and £10,550 total) and one remark that a
semicircular arch "was easier to maintain" than an elliptical one. It gives no upkeep figure, and
the viaducts were only a year or two old when the paper was read, so no upkeep figure could have
existed.

Thorpe (1906) treats concrete only as a rust protection for ironwork, not as a bridge material.

**Concrete has no measured British maintenance series in this pass.** Any concrete rate in the
pakset is currently an inference from another material.

### 3.6 Timber — measured for renewal, not for routine upkeep

The only measured annual timber figure is Cudworth's deck renewal at £0.52-0.55 per metre-year,
which is renewal and is recorded separately in section 6. Routine timber upkeep is not measured
anywhere in this pass.

Thorpe gives the qualitative position: timber is last of the materials for low maintenance
charges, repairs may be needed after ten years, and the life is about 25 years (range 15-35).
Cost rises as the structure ages because each member costs more to replace than it did to build.

---

## 4. Maintenance as a share of capital

This is the cross-check the brief asked for, and the answer is that **1 per cent a year is a
defensible central figure with a wide measured spread.**

| Source | Structure | Year | Share of capital a year |
|---|---|---|---:|
| LCC accounts | Putney, stone arch | 1908 | 0.15% |
| LCC accounts | Battersea, iron | 1908 | 0.16% |
| LCC accounts | Waterloo, stone arch | 1908 | 0.20% |
| LCC accounts | Hammersmith, suspension | 1908 | 0.21% |
| LCC accounts | Vauxhall, steel arch, nearly new | 1908 | 0.24% |
| LCC accounts | **median of nine bridges** | 1908 | **0.24%** |
| LCC accounts | Westminster, iron on granite | 1908 | 0.38% |
| LCC accounts | Wandsworth, iron lattice | 1908 | 0.62% |
| LCC accounts | Lambeth, suspension | 1908 | 1.04% |
| LCC accounts | Albert, suspension with timber deck | 1908 | 1.07% |
| Thorpe | wrought iron or steel, painting only | 1906 | 0.33-1.0% |
| Warwickshire TAMP | all-material target | 2008 | 1.0% (budget 0.54%) |

Two readings follow.

- For **sound masonry**, the measured share is 0.15-0.20 per cent. That is well below 1 per cent.
- For **metal bridges**, 0.2-1.0 per cent is measured, and Thorpe's painting-only band of 0.33-1.0
  per cent sits inside it.

The 1 per cent now used for tunnels is therefore at the **top** of the measured bridge range, not
the middle. It is defensible as a whole-life figure that includes periodic renewal, but it is too
high for masonry upkeep alone and too low for a structure with a timber deck.

---

## 5. Tunnels by lining material

### 5.1 The aggregate, and what it actually contains

The known 2023-24 figure is **£65.67 per metre-year across about 630 tunnels**. This pass found its
composition, and the composition changes how it should be used:

Network Rail's published expenditure breakdown for 2023-24 separates structures by type for the
only time in public:

| Asset type | 2023-24 | 2024-25 |
|---|---:|---:|
| Underbridges | £176m | £183m |
| Overbridges | £69m | £78m |
| Major structures | £32m | £18m |
| **Tunnels** | **£22m** | **£29m** |
| Minor works | £97m | £95m |
| Other | £40m | £60m |

£22m over 327 km of tunnel (the length Network Rail reported to its independent reporter in 2011)
is £67.28 per metre-year, which reproduces the £65.67 figure to within 3 per cent. The £65.67 is
therefore the **tunnels expenditure line divided by tunnel length**.

The important caveat: **that line aggregates maintenance and renewal.** It is not pure upkeep. If
the pakset charges tunnel renewal separately, using £65.67 as maintenance double-counts. The
year-on-year move from £22m to £29m (+32 per cent) with no change in tunnel length is itself
evidence that the line is dominated by lumpy renewals rather than a steady annual upkeep rate.

### 5.2 No material split exists in public

No British source was found that splits tunnel maintenance by lining material. The 2011 ORR
reporter review, the 2013 Arup policy review and the 2021 AMCL whole-life-cost review all state
that Network Rail's structures unit rates are not published and are inconsistent between regions;
the AMCL review records that "there is only one cost code and volume line for the structures asset
class", which means tunnels cannot be separated by lining in the finance system at all.

### 5.3 What the qualitative record does support

The 1947 ICE paper "Tunnel Maintenance" and its discussion are the best British source on lining
behaviour, and they give an ordering without costs:

- **Brick** — the standard lining. Spalling of the inner ring is the characteristic defect, caused
  by the tunnel atmosphere attacking the brick and the mortar. Repair is by cutting out and
  re-lining, described as "much the most advantageous method" and "also the most expensive".
  Staffordshire Blue and Accrington bricks performed best; London stock bricks gave little trouble.
  Repointing with the wrong mortar could itself cause spalling.
- **Stone** — Woodhead, 3 miles, two single tunnels, millstone-grit facing in lime mortar, 100 years
  old: the stone face was "still excellent" with no spalling, but sulphur fumes had eaten the
  joints until the wall "could almost be regarded as a dry wall", and bulges required cutting out
  and re-facing in brick. Stone therefore fails at the joints, not the face.
- **Cast iron** — used for London tube tunnels and some service tunnels. "Satisfactory for electric
  lines", but bolts corroded where steam traffic and poor ventilation persisted. No fabric
  maintenance rate is given.
- **Concrete** — not discussed as a tunnel lining in the 1947 paper.

Populations recorded, which allow a per-metre denominator if a company account is ever found:
LNER 243 tunnels totalling about 110 track-miles (1947); one LMS district 25 tunnels totalling
7.5 miles.

### 5.4 The one quantified tunnel cost driver

The Severn Tunnel (brick, 6,408 m) is the best-documented British tunnel for running cost, and the
figure is qualitative: the Great Spring "involved an annual expenditure of many thousand pounds on
pumping" (W. W. Grierson, who had maintained the tunnel for over 20 years, ICE 1932). No pound
figure was ever published in the sources reached.

The same discussion gives a harder number of a different kind: **rail life inside the tunnel was
about four years against a normal fifteen to twenty-five**, because of corrosion from the wet,
sulphurous atmosphere. That is a track cost, not a fabric cost, but it is measured and it is the
reason a wet tunnel is expensive.

---

## 6. Timber deck renewal, kept distinct from upkeep

Cudworth's £0.52-0.55 per metre-year is a renewal charge and is 2.7 times his plain-line
maintenance figure. The Union Chain Bridge (137 m wrought-iron suspension span, Tweed) gives the
same operation priced as discrete events across 120 years:

| Year | Work | Cost | Per metre |
|---|---|---:|---:|
| 1871 | deck substantially renewed | not recorded | — |
| 1902 | renewal of timber deck | £650 | £4.74 |
| 1919 | repairs to timberwork | £240 | £1.75 |
| 1925 | replacing wooden sleepers | £372 | £2.72 |
| 1926 | repainting ironwork | £130 | £0.95 |
| 1933 | renewal of cross beam | £763 | £5.57 |
| 1952 | ironwork cleaned and repainted, tower repairs | £1,217 | £8.88 |
| 1957 | repairs to deck | £800 | £5.84 |
| 1963 | repainting and north anchorage | £550 | £4.01 |
| 1964 | replace footpath timbers | £346 | £2.53 |
| 1969 | repairing bridge | £900 | £6.57 |
| 1974 | renew deck | £37,000 | £270.07 |

Two conclusions.

- A timber deck renewal is a **capital event every 25-70 years**, not an annual charge. Annualising
  the 1902 and 1974 renewals over the 72-year interval gives about £3.8 per metre-year in mixed
  nominal money, which is meaningless; the operation must be carried at the price of its own year.
- The 1974 renewal at £270 per metre is **1,000 times** the 1902 rate in nominal terms. That is
  price inflation plus a change in specification, and it shows why a single nominal timber renewal
  figure cannot be carried across eras.

For the pakset the usable statement is the Cudworth one: timber deck renewal is a separate annual
charge of £0.52-0.55 per metre-year at 1886 prices, additional to routine upkeep.

---

## 7. Canal aqueducts and tunnels

Canal companies did keep aqueducts as distinct assets, and two records give priced events:

**Pontcysyllte (cast-iron trough on masonry piers, 307 m, 1805)** — 1866 repair of the south
abutment, pier, arch and broken iron ribs, £396 (£1.29/m); 1886 scraping and painting of the whole
structure, £500 (£1.63/m); 1936 tarring, £397 (£1.29/m). The repaint interval is the notable
feature: Telford recommended painting in 1813 and the first recorded repaint is 1886, so no annual
painting rate can be derived from it.

**Marple (stone arch, 94 m, 1800)** — the recorded work between 1800 and 1960 was tie bars in 1860
and 1912 only. The north-east arch face collapsed in January 1962 after water penetrated the
puddle clay and froze; repair was priced at £32,000 (£340/m) against demolition at £25,000. The
recorded description is that "maintenance was sparse".

The canal evidence therefore supports the same conclusion as the railway masonry evidence:
**masonry aqueducts and viaducts carry very little routine maintenance, and their cost is a rare,
large repair.** It does not provide an annual per-metre rate.

---

## 8. Recommended rate for each pakset material

All rates are in the money of the stated year and **per metre of structure per year**, excluding
the permanent way on top. The pakset bridge and tunnel objects bundle the way, so the way rate must
be added: Cudworth's plain line is £0.19/m-yr at 1886 prices.

### Bridges

| Material | Recommended rate | Year | Basis | Confidence |
|---|---:|---|---|---|
| Brick | **£0.05** | 1886 | Measured, Hownes Gill | High for a brick arch viaduct; single observation |
| Iron | **£0.23-0.25** | 1886 | Measured, Belah and Deepdale | High: two structures, 18-year means |
| Stone | **£0.04-0.05** | 1886 equivalent | Inferred from Thorpe's ranking below brick | Low: no measured railway masonry rate |
| Steel | **£0.27-0.32** | 1886 equivalent | Inferred: iron x 1.1-1.3, from Thorpe's shorter painting interval for steel | Low: no per-metre series; Forth Bridge is 1,300x higher and not comparable |
| Concrete | **No measured basis** | — | None | None |
| Timber | **£0.52-0.55 renewal, plus routine** | 1886 | Measured renewal; routine not measured | Medium for renewal, none for routine |

Bundle totals at 1886 prices, if the way is charged inside the object: brick £0.24, stone
£0.23-0.24, iron £0.42-0.44, steel £0.46-0.51, timber £0.71-0.74 plus timber routine.

The material ordering that the evidence supports, from cheapest to dearest upkeep: **stone, brick,
cast iron, wrought iron, steel, timber.** This is Thorpe's order, and Cudworth's four figures are
consistent with it.

### Tunnels

| Lining | Recommended rate | Year | Basis | Confidence |
|---|---:|---|---|---|
| All linings (aggregate) | **£65.67/m-yr, maintenance and renewal combined** | 2023-24 | Measured, Network Rail | Medium as an aggregate; the line includes renewals |
| Brick | No separate measured rate | — | Only the aggregate exists | None for brick alone |
| Stone | No measured basis | — | Woodhead qualitative only | None |
| Concrete | No measured basis | — | Not discussed in the British record | None |
| Cast iron | No measured basis | — | London tube practice qualitative only | None |

The honest recommendation is **one tunnel rate for all linings**, with the material difference
carried as a qualitative factor of at most 1.5 either way, and an explicit note that no British
source splits tunnel maintenance by lining. Inventing a brick/stone/concrete/cast-iron spread would
be fitting to the pakset rather than to evidence.

Two adjustments are needed before the aggregate is used as an upkeep rate:

1. Strip the renewal content, or charge tunnel renewal separately. The £22m line is not pure
   maintenance, and the 32 per cent year-on-year movement shows the renewal component is large.
2. Treat the Severn Tunnel as an outlier, not a sample. A wet tunnel costs several times a dry one
   because of pumping and because rail life falls to about four years.

---

## 9. Confidence, and what would change the answer

| Finding | Confidence | What would overturn it |
|---|---|---|
| Iron viaducts £0.23-0.25/m-yr at 1886 | High | A second railway's account series showing a different order |
| Brick viaduct £0.05/m-yr at 1886 | Medium | A second brick viaduct figure; one observation only |
| Masonry railway viaducts cost less than brick | Low | Any measured masonry viaduct series |
| Steel slightly above iron | Low | A measured steel underbridge series |
| Concrete has no measured basis | High that none was found | A post-1920 concrete structure account |
| Iron and steel painting is 0.33-1% of first cost | Medium | Thorpe is a handbook statement, not an account |
| LCC bridges 0.15-1.07% of capital, median 0.24% | High for the population | — |
| 1% is a target for bridge maintenance, not an outturn | High | Warwickshire states the target and its own budget was 0.54% |
| Tunnel £65.67/m-yr includes renewals | High | The £22m line and the 32% swing both point to it |
| No tunnel material split exists publicly | High | A Network Rail structures unit-rate release |

The single change that would most improve the answer is a **British railway company account that
separates "repairs of bridges" from "repairs of tunnels" and gives the structure count**. The Board
of Trade returns from 1873 and the Railway Companies (Accounts and Returns) Act 1911 standard form
both contain a maintenance-of-way heading; if either subdivides bridges and tunnels, a per-structure
rate follows directly. That was not reached in this pass.

---

## 10. Dead ends

Recorded so they are not searched again.

| Source | Outcome |
|---|---|
| Cudworth, ICE 1886 (vol. 85, pp. 340-342) | Three pages; Belah and Deepdale only. Fully mined already. |
| Marriott, "Strengthening and Maintenance of Early Iron Bridges", ICE 1905 | Gives strengthening costs only: West Lynn £8,000 against £40,000-50,000 new; Potter Heigham £2,050 against £20,000 new. No annual upkeep. |
| Discussion and correspondence on the above, ICE 1905 | Painting technique and steel corrosion; no rates. |
| Wood-Hill and Pain, "Concrete Railway Viaduct", ICE 1905 | Capital only; viaducts too new to have an upkeep record. |
| Robarts, "Tunnel Maintenance", ICE 1947, and discussion | Inspection and repair practice; no costs. Populations only. |
| Hawkins, "Maintenance Considerations in the Design of Railway Works", ICE 1950 | Paywalled; abstract only; no figures retrievable. |
| Royal Commission on Canals and Waterways, 1906-1911 | Capital estimates for canal improvement; no per-metre maintenance reached in the accessible text. |
| Severn Tunnel, GWR and later | Pumping cost described as "many thousand pounds a year"; no figure published. |
| Kilsby Tunnel | Construction pumping and capital cost (£291,030; £125 a yard); no operating cost. |
| Network Rail asset policy and ORR/Arup/AMCL reviews | Confirm structures unit rates exist but are unpublished and not separable by asset or material. |
| Oxfordshire County Bridges book, 1905 | Repair events per bridge over 70 years; no annual totals, so no per-bridge-year rate. |
| LCC annual reports on archive.org | Not reached; the 1911 Britannica table gave the 1907-08 figures directly. Later years would extend the series. |

---

## 11. Arithmetic check on the knowledge-base ratios

Two of the four stated ratios reproduce exactly and two do not, which matters before any of this is
used.

- **Iron 1.2-1.5 times plain line.** Reproduces: 0.25/0.19 = 1.32; 0.23/0.19 = 1.21.
- **Brick 0.25-0.5 times plain line.** Reproduces at the bottom of the range: 0.05/0.19 = 0.26.
- **Timber 7-8 times plain line.** Does **not** reproduce: 0.52/0.19 = 2.7. Timber deck renewal is
  2.7 times plain line, not 7-8 times.
- The 7-8 multiplier **does** reproduce against the brick rate: 7 x 0.05 = 0.35 and 8 x 0.05 =
  0.40. The likely correct statement is "timber 7-8 times the brick rate", not "7-8 times plain
  line". The parent should confirm which was intended before using the multiplier.

---

## 12. Sources

- Cudworth, W. J., "The Maintenance of the Belah and Deepdale Viaducts on the North Eastern
  Railway", *Minutes of the Proceedings of the Institution of Civil Engineers* 85 (1886) 340-342.
- Marriott, W., "The Strengthening and Maintenance of Early Iron Bridges", ibid. 162 (1905) 213-222,
  with discussion 223-240 and correspondence 240-260.
- Wood-Hill, A., and Pain, E. D., "On the Construction of a Concrete Railway Viaduct", ibid. 160
  (1905) 1-12, with discussion and correspondence.
- Grierson, W. W., in discussion on "Cementation in the Severn Tunnel", ibid. 234 (1932) 290.
- Robarts, "Tunnel Maintenance", *ICE Engineering Division Papers* 5(5) (1947) 1-21, with
  discussion 22-34 (Wilson, Barbey, Dunton, Barton, Reed, Nixon, Hawkins, Salt, Neale).
- Hawkins, L. E., "Maintenance Considerations in the Design of Railway Works", ibid. 8(7) (1950)
  1-23.
- Thorpe, W. H., *The Anatomy of Bridgework* (E. and F. N. Spon, London, 1906), ch. XV, pp. 165-170,
  and ch. XIII on timber bridges. Full text: Internet Archive item `anatomyofbridgew00thorrich`.
- "London", *Encyclopaedia Britannica*, 11th edition (1911), Bridges section: London County Council
  bridge capital and maintenance table for 1907-08, and Bridge House Estates expenditure for 1907.
- Paxton, R., *Historic Berwick-upon-Tweed Bridges* (2018), table of Tweed Bridges Trust maintenance
  1884-1974.
- Priestley, S., "The Maintenance of Pontcysyllte Aqueduct", *Railway and Canal Historical Society
  Journal*, November 2005.
- Network Rail, *Annual expenditure 2023-24* and *Annual expenditure 2024-25* (structures and
  tunnels breakdown).
- Arup for the Office of Rail Regulation, *Review asset policy, stewardship and management of
  structures: final report* (March 2011), §§4.2-4.3 and 6.6; the Warwickshire Transport Asset
  Management Plan 1 per cent statement is quoted at §4.3.4.
- AMCL, *A review of Network Rail's whole lifecycle costing framework* (November 2021), structures
  unit-cost findings.

Structure lengths for the per-metre conversions: Forth Bridge 2,467 m (Network Rail, via Wikipedia);
Union Chain span 137 m; Pontcysyllte 307 m; Marple 94 m; LCC bridges from their Wikipedia infoboxes
(Waterloo 1,230 ft, Westminster 250 m, Albert 710 ft, Battersea 725 ft 6 in, Hammersmith 700 ft,
Putney 700 ft, Vauxhall 809 ft, Wandsworth 650 ft, Tower 940 ft).
