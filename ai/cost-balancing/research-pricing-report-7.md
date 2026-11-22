---
status: draft
verified: none
---
# Research pass 7: cost premiums for engineering and type features

**Covers**: measured price differences between variants of the same vehicle, by feature, for the
pakset's vehicle cost ladders. Steam locomotive cylinder count, superheat, compounding and valve
gear; road vehicle diesel against petrol, transmission, body and traction type; horse type; carriage
and wagon features; tram bodies against electrical equipment. Rows are in
`research-pricing-rows-7.csv`. Parent method: `New/ai/vehicle-cost-method.md`, price surface section.

Nothing under `New/` has been modified. No git command was run.

## 1. The question this pass answers

The locomotive ladder in `vehicle-cost-method.md` prices a steam engine as
`weight^0.86 x a power term`. Weight and power cannot distinguish a four-cylinder compound from a
two-cylinder simple of the same weight and power, a superheated engine from a saturated one, or a
Caprotti engine from a Walsestearts one. The same gap exists in every other class.

What is needed is a set of multipliers, each measured on a pair of vehicles that differ in one
feature only, with the year and the source stated.

## 2. Findings

### 2.1 Steam locomotives: superheat, compounding and cylinders

The single best source found is George Hughes's 1910 Institution of Mechanical Engineers paper,
*Compounding and Superheating in Horwich Locomotives*. Hughes was Chief Mechanical Engineer of the
Lancashire and Yorkshire Railway and reported his own works' costs for batches built specifically
for comparison. His statement of the method is the reason the paper matters:

> "The boilers, steam-pressures, grate areas, heating surfaces, valve-motions, wheels — both in
> number and diameter — were exactly the same in both instances. A similar remark also applied to
> the simple saturated and the superheater engines."
> (Proc. IMechE 1910, vol. 78, p. 433)

Four figures follow, all 1907-1910, all absolute:

| Comparison | Premium | Basis |
|---|---|---|
| Ten 4-cylinder compounds against ten 2-cylinder simple sisters (built 1907) | **£260 per engine** | "the average first cost of the ten new compound engines was £260 per engine more than the average of ten new sister simple engines" (p. 456) |
| Twenty superheated against twenty non-superheated engines | **£350 per engine** | "the actual average extra cost of twenty new superheater over twenty new non-superheater engines was £350 per engine" (p. 456) |
| The same, expected for future lots | **£300 per engine** | "future lots of engines could be built for £300 per engine extra" (p. 456) |
| Superheating as done at Brighton (Marsh, in the discussion) | **about £175 per engine** | "it had been done on the Brighton Railway for about half that amount" (p. 469) |

The paper reports the same two premiums a second way, as annual standing charges at 10 per cent for
interest, depreciation and repairs: £26 a year on the compound and £35 a year on the superheater.
Both are exactly 10 per cent of £260 and £350, which confirms the OCR reading of the two figures
(the scan prints them as "52260" and "2350").

Two further figures from the same discussion bound the conversion cost for existing engines: the
high-degree systems needed "over £600" of new parts delivered abroad, of which £300 was new
cylinders and gear, while the Trevithick smoke-box system needed "less than £100" (pp. 470-1).

**Converting £ to a percentage.** The paper does not state the base price of the engines. The
nearest well-evidenced base for a 1907-1910 main-line engine is about £3,000: the LSWR T9 cost
£3,200 in 1899 and the NER P3 0-6-0 £3,500 in 1908 (both in `published-capital.md`), and a Midland
new build of the mid-1910s is put at about £3,000. On £3,000:

| Feature | Central | Range on a £2,500-3,500 base |
|---|---|---|
| Superheat | **+11.7%** | +10.0 to +14.0% |
| Superheat, expected cost | +10.0% | +8.6 to +12.0% |
| Superheat, Brighton conversion | +5.8% | +5.0 to +7.0% |
| Compound (4-cyl against 2-cyl simple) | **+8.7%** | +7.4 to +10.4% |
| Compound (2-cyl against 2-cyl simple, Worsdell) | +6.7% | +5.7 to +8.0% |

**The compounding result is not what the brief expected, and it matters.** E. M. Gass, reading a
paper to the Institution of Locomotive Engineers in 1926, stated that "the four-cylinder compound
locomotive with only two sets of valve gear cost practically the same to build as the four-cylinder
single expansion engine" (Paper 208, p. 25). He also gave the two-cylinder case: "the Worsdell
von-Borries compound cost approximately £200 more to build than the single expansion engine", the
two having the same tractive power.

Read together with Hughes, the cost driver is **cylinders and valve gear**, not the double-expansion
principle:

- at two cylinders, compounding adds about £200, because the low-pressure cylinder and its valve
  gear are extra;
- at four cylinders, compounding adds approximately nothing, because the cylinder count and the two
  sets of valve gear are already paid for;
- going from two cylinders to four, with compounding, adds £260.

So the ladder should carry a **per-cylinder-pair term**, and a compound term that applies only where
the cylinder count is unchanged at two. That is a different shape from "compound = dearer".

**Cylinder count on its own.** No clean 2- against 3-cylinder or 2- against 4-cylinder price pair
was found. The obvious candidates all failed:

- LMS Stanier 2-6-4T: the three-cylinder No. 2500 cost £6,444 at Derby in 1934 (NRM exhibit
  board), but no two-cylinder cost for the same class is published. The two-cylinder version is a
  different boiler and different cylinders, built from 1935, so even a price would not be a clean
  pair.
- LNER and GWR four-cylinder classes: no works cost by variant found in open sources.
- NER P3: 80 saturated engines 1906-09 and 35 superheated 1921-23, each £3,500-£3,550 depending on
  contractor — fifteen years and different builders apart, so useless for the superheat premium.

The working estimate for a third cylinder is therefore **inferred** from the £260 for two extra
cylinders: about £130 per additional cylinder at 1910 prices, or +4 to +5 per cent per cylinder on a
£3,000 engine. Mark it weak.

**Poppet valves and Caprotti.** One strong pair, 1957, same class, same works, same year:

| BR Standard Class 5, 1957 build | Price | Difference |
|---|---|---|
| Walschaerts valve gear, Nos. 73165-71 | £25,606 each | — |
| British Caprotti, Nos. 73146-54 | £28,469 each | **£2,863 = +11.2%** |

Source: D. Wardale, *Piston vs Caprotti Valves — The Final Discussion?* (2009), quoting J. Duncan's
BR cost figures; Wardale recomputes Duncan's rounded 10 per cent as 11.2 per cent. Secondary, but
the two absolute prices are stated and the class is identical apart from valve gear and cylinders.

**Boiler pressure, grate area, feedwater heaters, boosters.** Nothing usable. The Hughes discussion
mentions feed-water heating repeatedly but never prices it. No source found that states the cost of
a pressure increase or a larger grate as a separate item. Recorded as unknown.

### 2.2 Road vehicles: fuel, transmission, body and traction

**Diesel against petrol.** This is the strongest block of evidence in the pass, because *The
Commercial Motor* printed a full price list every year with petrol and oil (diesel) prices side by
side for the same model. The 6 May 1960 list alone gives 33 usable pairs. The pattern:

| Measure | Value |
|---|---|
| Number of pairs | 33 (Austin, Bedford, Commer, Dodge, Ford Thames, Karrier, Morris-Commercial, Land-Rover) |
| Absolute premium | £45 to £246; median about **£125** |
| Percentage premium | **7.5% to 26.0%**; median **16.6%**; interquartile range 13.8% to 19.3% |

Selected pairs, all 1960, all same model and page:

| Vehicle | Petrol | Oil | Difference |
|---|---|---|---|
| Austin 1-ton chassis | £443 | £545 | +£102 (+23.0%) |
| Bedford 3-ton chassis and cab | £715 | £840 | +£125 (+17.5%) |
| Bedford 5-ton chassis and cab | £840 | £1,025 | +£185 (+22.0%) |
| Bedford 7-ton chassis and cab | £1,080 | £1,205 | +£125 (+11.6%) |
| Bedford passenger chassis | £984 | £1,109 | +£125 (+12.7%) |
| Ford Thames 2-ton | £624 | £724 | +£100 (+16.0%) |
| Ford Trader 7-ton | £1,037 | £1,172 | +£135 (+13.0%) |
| Bedford forward-control 4x4 | £1,260 | £1,355 | +£95 (+7.5%) |

**The structure is an absolute adder, not a percentage.** The Bedford premium is £105, £105, £125,
£125, £185, £185, £125, £125 as the chassis rises from 25 cwt to 7 tons: nearly flat while the base
price roughly doubles. That is why the percentage falls from 23 per cent at 1 ton to 11.6 per cent at
7 tons. The diesel engine is a roughly constant cost increment, and the ladder should model it that
way if it can: a fixed sum in 1900 money, or a multiplier that declines with vehicle size.

The earlier pairs are consistent with the same structure at a higher price level:

| Year | Comparison | Premium |
|---|---|---|
| 1931 | T.S.M. 3½-ton chassis, Gardner oil against 5.1-litre petrol | £720 against £903 = **+25.4%** |
| 1933 | Leyland Cub diesel against petrol | **+£135** (no base price stated) |
| 1963 | Bedford VAS chassis, diesel against petrol | £860 against £1,045 = **+21.5%** |

**Trolleybus against motorbus.** One clean statement, 1952: "A two-axled double-deck 56-seat 8-ft
wide motorbus costs about £4,200 and an equivalent trolleybus £4,800" (Commercial Motor, 19
September 1952, p. 80, reporting a paper by Mr Frith). That is **+£600, +14.3%**. It excludes the
overhead line, which the same paper puts at about £10,000 a mile on average.

**Transmission.** Two stated option prices:

- 1966 Bristol RELL bus chassis: standard £3,335; "fluid clutch and five-speed semi-automatic
  transmission £364" = **+10.9%**.
- 1972 Seddon Pennine-6: Allison automatic "extra charge £480"; the V8 Pennine-4 version £360 more
  again (£840) for a larger gearbox. No base price on the page.

**Body on chassis.** Three independent cases, spread over forty years:

| Year | Chassis | Body or complete | Body as share of chassis |
|---|---|---|---|
| 1928 | Fiat 30 S.P.A. £680 | complete £1,075 | £395 = 58.1% |
| 1932 | Portsmouth Crossley £1,075 | English Electric body £690 | 64.2% |
| 1960 | Bedford 25-cwt chassis and cab £625 | van £831 | £206 = 33.0% |

The bus body (a 56-seat double-decker) is worth about 60 per cent of the chassis; a light van body
about a third. This is the figure the ladder needs for "chassis-cab against complete vehicle".

**Engine configuration.** Ford Trader 5-ton, 1960: four-cylinder petrol £845 against six-cylinder
petrol £995 = **+£150 (+17.8%)**; the same option in oil, £960 against £1,035 = +£75 (+7.8%). A
1931 Dennis Arrow six-cylinder engine was a £100 option over the four.

### 2.3 Horses

The type differential is consistent across three independent families, but the families overlap in
time rather than being a single matched year.

| Comparison | Year | Prices | Premium |
|---|---|---|---|
| Shire five-year-old against half-bred light van or bus horse | 1891 | £60-100 against £40-45 | +33% to +150%, midpoint +50% |
| Heavy draught (vestry cart horse) against light omnibus or cab horse | 1890-97 against 1893 | £47-70 against £30-35 | +34% to +133%, midpoint +34% |
| Army troop horse against cob | 1909 | £42 against £30 | +40% |
| Army charger against cob | 1909 | £60 against £30 | +100% |
| Fleming's draught range, ordinary to best dray | c.1900 | £36 to £80-90 | +122% to +150% at the top |

The 1891 Shire letter is the cleanest statement of the breed premium because it compares the two
types at the same age and for the same urban buyer: the Shire went "into the towns" at £60-100, the
half-bred "into a light van or a bus" at £40-45 (R. N. S. Nelthorpe, *The Spectator*, 14 March 1891,
p. 15). It is a breeder's statement, not a sale record.

Two index points, useful for the horse price series rather than for type premiums:

- Shire Horse Show sales: 121 horses averaged £60 2s in 1895; 149 averaged £127 7s in 1911; 142
  averaged £120 9s in 1912 (Board of Agriculture and Fisheries, *British Breeds of Live Stock*,
  1913). That is +112 per cent over sixteen years.
- London and North Western and London and South Western Railway horses: £50-55 in 1872 against
  £35-44 six years earlier (Moore-Colyer, *Agricultural History Review* 43.1), +25 per cent.

### 2.4 Carriages and wagons

| Feature | Year | Prices | Premium |
|---|---|---|---|
| Six-wheel bogies against four-wheel bogies, Midland bogie carriage | 1870s | £979 against £820 | **+19.4%** |
| Steel panelling against wood panelling, GWR 57 ft Toplight | c.1903-10 | £1,500 against £1,200 | **+25.0%** |
| First class against third class, same body and weight, Highland Railway | 1873 | £517 5s against £290 | **+78.4%** |
| Dining car against composite, both eight-wheel, NER | 1909 | £2,304 against £1,595 | **+44.5%** |
| Dining car against brake third, NER | 1906 | £2,501 against £1,460 | +71.3% (confounded by length) |
| Arc roof against clerestory, Midland | 1880 | £25 less | **−2.5%** |
| Elliptical roof against clerestory, Midland | 1915 | £35-40 less | about −3.5% to −4% |
| A complete set of new bogies | 1908 | £33 per carriage | component price |

Notes on these:

- The Midland bogie pair and the Highland class pair are the cleanest: same body, same order, one
  variable.
- The roof pairs are negative: the clerestory was the expensive option and the later low roofs were
  cheaper by 2.5 to 4 per cent while being 12 cwt lighter. A ladder that prices roof type should
  therefore mark the clerestory up, not the arc roof down.
- The NER dining cars are the best evidence for a kitchen premium because the records give the
  diagram number, the year and the exact cost. The 1909 pair (dia. 1266 against dia. 824) holds
  wheel arrangement constant; the 1906 pair does not.
- Corridor against open could not be paired. The GWR figures in circulation (four-wheel £380-450 in
  the mid-1890s against clerestory corridor £1,000-1,200) differ in length, wheel arrangement and
  roof as well as corridor, so the apparent 130-160 per cent is not a corridor premium.

**Wagons.** Only one paired figure was found, and it is forum-sourced: a Midland 8-ton open cost
about £60-62 and the 12-ton replacement required £17 more, about +28 per cent for 50 per cent more
capacity. That is a capacity effect, not a feature effect. Two absolute prices are recorded for
context: a GWR Mink van of 1913 at about £110, and a Southern Railway 20-ton vacuum-fitted ballast
wagon of 1928 at £189, described by the source as "not much more than a standard open wagon without
doors".

### 2.5 Trams

The British evidence gives complete-car prices but rarely a body/equipment split. The Australian
contract records give the split precisely, in sterling:

| Melbourne, 1922-23 (W class, per car) | £ | Share of £2,674 |
|---|---|---|
| Body (Holden, including painting) | 1,383 | 51.7% |
| Four-motor electrical equipment (including duty) | 880 | 32.9% |
| Bogies (Perry Engineering) | 150 | 5.6% |
| Air brake equipment (including duty) | 154 | 5.8% |
| Blinds | 45 | 1.7% |
| Wheels, axles, centres and tyres | 62 | 2.3% |
| **Total** | **2,674** | |

A second, earlier case gives the same shape: Hawthorn Tramways Trust, 1915-16, bodies at £548 2s 6d
each and British Westinghouse motors and magnetic brakes at £441 per car — equipment at 44.6 per cent
of body plus equipment, with the truck excluded.

British prices for complete cars, 1901, one specification, four tenders (Wallasey):

| Tenderer | Total for 20 cars | Per car |
|---|---|---|
| Electric Railway & Tramway Carriage Works | £11,800 without air brakes | £590 |
| British Westinghouse | £11,940 plus £1,000 for air brakes | £597 |
| Brush | £13,200 without air brakes | £660 |
| R. W. Blackwell | £13,925 with air brakes | £696 |

Two conclusions. First, **air brakes cost £45-50 per car, 7.6 to 8.4 per cent**, which is the only
British tram feature premium found with both prices stated. Second, **the spread between builders
for an identical specification is 17.9 per cent**, which is the uncertainty band that any single
tram price carries.

**Deck type.** A negative result, worth recording: when Wallasey's manager asked for five bogie
single-deck combination cars in 1902, Dick Kerr quoted £585 each against the £590 paid for the
four-wheel double-deckers of the same fleet. Deck type and even bogie mounting did not separate the
prices, because capacity did. The Sydney conversion estimate of 1906 points the same way: adding an
open upper deck to an existing four-wheel car was estimated at £140, glazed in at £180, plus £35 to
lengthen the platforms.

## 3. Recommended multipliers

These are factors on the price of the same vehicle without the feature. Read the confidence column
before using any of them.

### Steam locomotives

| Feature | Factor | Applies | Evidence | Confidence |
|---|---|---|---|---|
| Superheat | **×1.12** (1.10-1.14) | 1905-1930 | £350 on 20 identical engines, LYR 1910 | Strong pair; percentage derived from a £3,000 base |
| Superheat, cheap conversion | ×1.06 | 1905-1920 | £175, LBSCR, 1910 | Medium; conversion not new build |
| Compound on a two-cylinder layout | **×1.07** (1.06-1.08) | 1900-1930 | £200, Worsdell, reported 1926 | Medium; one pair, earlier generation |
| Compound on a four-cylinder layout | **×1.00** | 1910-1935 | Gass 1926, "practically the same" | Weak-medium; a negative result |
| Additional cylinder pair (2 to 4), with compounding | **×1.09** (1.07-1.10) | 1900-1935 | £260, ten against ten, LYR 1907 | Strong pair; the best in the set |
| One extra cylinder (2 to 3) | **×1.045** | 1900-1950 | Inferred from £260 for two | Weak; inferred, no pair |
| Caprotti or other poppet valve gear | **×1.11** | 1930-1960 | £2,863 on £25,606, BR5 1957 | Strong pair |
| Boiler pressure, grate area, feedwater heater, booster | — | — | None found | Unknown |

A practical implementation for the existing ladder:

```
price = 132 x weight^0.86 x (power/600)^0.15 x k_cyl x k_compound x k_superheat x k_valve
```

with `k_cyl` = 1.00 for two cylinders, 1.045 for three, 1.09 for four; `k_compound` = 1.07 only
where the cylinder count is two, otherwise 1.00; `k_superheat` = 1.12 from about 1905 and 1.05
before; `k_valve` = 1.11 only for poppet gear.

The absolute-figure alternative is to add £350 and £260 (1907-10 money) converted through the
established index. That is more faithful to the evidence, because a superheater is a per-boiler cost
rather than a proportion of the engine, but it requires the 1900 conversion to be settled first. The
multiplicative form above is the stopgap.

### Road vehicles

| Feature | Factor | Applies | Evidence | Confidence |
|---|---|---|---|---|
| Diesel against petrol, light vehicle (under 2 tons) | **×1.22** | 1930-1970 | 1960 list at 1 ton; 1963 Bedford VAS | Strong; 33 pairs plus two |
| Diesel against petrol, medium (2-4 tons) | **×1.17** | 1930-1970 | 1960 list at 2-4 tons | Strong |
| Diesel against petrol, heavy (5-7 tons) | **×1.14** | 1930-1970 | 1960 list at 5-7 tons | Strong |
| Diesel against petrol, 1930s | ×1.25 | 1930-1940 | 1931 TSM, 1933 Leyland | Medium; two cases |
| Trolleybus against diesel bus | **×1.14** | 1930-1960 | £4,200 against £4,800, 1952 | Strong single pair |
| Automatic or semi-automatic transmission | **×1.11** | 1960-1980 | £364 on £3,335, 1966 | Strong pair |
| Six-cylinder against four-cylinder engine | ×1.18 | 1930-1970 | Ford Trader, 1960 | Medium |
| Complete bus against chassis | **×1.60** | 1928-1970 | body 58-64% of chassis | Medium; two cases |
| Complete light van against chassis-cab | ×1.33 | 1960 | Bedford 25-cwt | Weak; one case |

Because the diesel premium is close to a constant absolute sum, the ladder should prefer the
size-banded factors above to a single number.

### Horses

Factors on the price of an ordinary cart or dray horse:

| Type | Factor | Evidence | Confidence |
|---|---|---|---|
| Cart, dray, heavy draught | **1.00** | £47-70, 1890-97; £36-90 range, c.1900 | Strong |
| Omnibus or cab horse (light) | **0.60** | £30-35, 1893 | Medium; one source family |
| Coach or harness horse, half-bred | **0.85** | £40-45, 1891 | Medium |
| Shire or Clydesdale, five-year-old, town quality | **1.30-1.45** | £60-100, 1891 | Medium |
| Troop horse | 1.40 on the cob price | £42 against £30, 1909 | Medium |
| Charger or hunter | 1.70-2.00 on the cob price | £60 against £30, 1909 | Medium |
| Cob or pony | 0.60 | £30, 1909; £8-12 open market, 1902 | Medium |

### Carriages

| Feature | Factor | Evidence | Confidence |
|---|---|---|---|
| Six-wheel bogies against four-wheel bogies | **×1.19** | £979 against £820, Midland 1870s | Strong pair |
| Steel panelling against wood | **×1.25** | £1,500 against £1,200, GWR | Strong pair |
| First class against third, same body | **×1.78** | £517 against £290, Highland 1873 | Strong pair |
| Dining car with kitchen against composite, same wheel arrangement | **×1.45** | £2,304 against £1,595, NER 1909 | Medium |
| Clerestory roof against arc roof | **×1.026** | £25 on about £1,000, Midland 1880 | Strong pair, small effect |
| Corridor against open | **not quantified** | Confounded with length everywhere | Unknown |
| Complete set of bogies | £33 in 1908 | Highland | Component price only |

### Wagons

| Feature | Factor | Evidence | Confidence |
|---|---|---|---|
| Capacity 8 tons to 12 tons | ×1.28 | £60 against £77, Midland, c.1900 | Weak; forum-sourced |
| Vacuum fitted against unfitted | **not quantified** | No paired price found | Unknown |
| Steel body against wood | not quantified | Direction only ("cheaper to build and repair") | Unknown |

### Trams

| Feature | Factor or share | Evidence | Confidence |
|---|---|---|---|
| Body only, without electrical equipment | body = **52%** of complete car | Melbourne 1923 | Medium; Australian |
| Electrical equipment alone | **33%** of complete car | Melbourne 1923 | Medium; Australian |
| Electrical equipment as share of body plus equipment | 45% | Melbourne 1916 | Medium; Australian |
| Air brakes | **×1.08** | £45-50 on £590-597, Wallasey 1901 | Strong pair |
| Bogies or trucks | 6% of complete car | Melbourne 1923 | Medium |
| Upper deck added to an existing car | £140-180 (1906) | Sydney | Weak |
| Double deck against single deck at equal capacity | approximately nil | Wallasey 1902 | Weak, negative result |
| Builder spread on one specification | 18% | Wallasey 1901 | Medium |

## 4. Strength of the evidence

**Strong pairs** (same class, same year, same builder, one feature different):

1. LYR 1907: ten 4-cylinder compounds against ten 2-cylinder simples, £260. The paper states that
   every other element was identical.
2. LYR 1910: twenty superheated against twenty non-superheated, £350. Same statement.
3. BR5 1957: Caprotti against Walschaerts, £2,863 on £25,606.
4. The 1960 Commercial Motor list: 33 diesel/petrol pairs on one page.
5. Midland 1870s: six-wheel against four-wheel bogies, £979 against £820.
6. GWR Toplight: steel against wood panelling, £1,500 against £1,200.
7. Highland 1873: first against third, same dimensions and weight.
8. 1966 Bristol RELL: semi-automatic transmission, £364 on £3,335.
9. Wallasey 1901: air brakes, £45 on £590.

**Ranges only**, where the years or the buyers differ: every horse figure; the diesel premium before
1960; the trolleybus figure (one source); the dining-car premium; the tram body/equipment split
(Australian, not British).

**Weak or inferred**: the third-cylinder premium; the wagon capacity figure; the deck-type result;
the pre-1900 carriage figures taken from forum transcriptions of Lacy and Dow and Tatlow.

A caution that applies to all the absolute figures: they are per-engine or per-vehicle sums measured
on one class in one year. Turning them into a percentage applies them proportionally to engine size,
which is defensible for a superheater (a per-boiler item) and for cylinders, but is an assumption,
not a measurement.

## 5. Dead ends

Recorded so that the next pass does not repeat them.

1. **LMS Stanier 2-6-4T two-cylinder cost.** The three-cylinder figure (£6,444, 1934) is well
   attested; the two-cylinder figure is not published anywhere found. Rowledge, *Engines of the LMS*,
   is the place it would be, and it is not online.
2. **NER P3 saturated against superheated.** Batches fifteen years apart and by different
   contractors; the price difference is builder and year, not superheat.
3. **Poppet valve premiums before 1957.** The 1929-31 Institution of Locomotive Engineers papers on
   poppet valves exist but are paywalled and the searched extracts carry no cost figures.
4. **Feedwater heaters, boosters, boiler pressure, grate area.** No British price found for any of
   them as a separate item. The 1910 discussion refers to feed-water heating repeatedly without
   pricing it.
5. **Vacuum-fitted against unfitted wagons.** No paired price in any source reached. The trade and
   society material describes the equipment and its operational value but never prices the option.
   The only route left is a component build-up from wagon builders' specification books.
6. **Corridor against open carriage.** Every apparent pair differs in length, wheel arrangement or
   roof as well as corridor.
7. **British tram body against complete car.** British tram accounts give complete-car prices; the
   split is only in the Australian contract records.
8. **Diesel against petrol for private cars.** Not searched in this pass; the commercial-vehicle
   evidence is better and more relevant to the pakset's lorry and bus ladders.
9. **Horse breed prices at auction.** The breed society and Board of Agriculture material gives
   show-ring averages and record prices for pedigree stock (£500 stallions, £9,500 for a mare), which
   are not working-horse prices and must not enter the ladder.

## 6. What remains unknown

- The price of a third cylinder on its own, uncontaminated by compounding.
- Whether the superheat premium fell after 1920 as the equipment became standard. The Hughes figures
  are 1910; the BR5 pair gives a 1957 valve-gear premium but no 1957 superheat premium, because by
  then every engine was superheated.
- The cost of a boiler pressure increase, which is the feature most likely to explain the gap
  between a 200 lb/sq in engine of 1930 and a 250 lb/sq in engine of 1950.
- The fitted-wagon premium, which the pakset needs because fitted and unfitted wagons are separate
  objects.
- British tram body/equipment splits after 1920, when body building and electrical equipment became
  separate contracts as a matter of course.
- Whether the horse type differential held outside London and outside the 1890s.

## 7. Search record

One search per turn, as required. Queries and what they returned:

| Turn | Query subject | Result |
|---|---|---|
| 1 | Superheater cost per locomotive, saturated against superheated, IMechE | Hughes 1910 paper; the richest single source of the pass |
| 2 | Stanier 2-6-4T two- and three-cylinder costs; GWR two against four cylinder | £6,444 confirmed; no two-cylinder figure; no GWR pair |
| 3 | Four-cylinder against two-cylinder percentage, I.Loco.E. | Gass 1926; the £200 Worsdell compound and the zero-cost four-cylinder result |
| 4 | Tramcar body against complete with electrical equipment | Melbourne and Sydney contract splits; Wallasey tenders |
| 5 | British municipal tramcar contract prices | Wallasey, Bolton, Accrington, Kilmarnock |
| 6 | Vacuum-fitted against unfitted wagon | Nothing; SR 20-ton wagon and GWR Mink prices only |
| 7 | Trolleybus against diesel bus | The 1952 £4,200/£4,800 pair |
| 8 | Automatic transmission option prices | Bristol RELL 1966, Seddon 1972 |
| 9 | Caprotti against Walschaerts cost | BR5 1957 pair; Duke of Gloucester |
| 10 | LMS 2-6-4T £6,444 two-cylinder | NRM sign-board confirmed; no pair |
| 11 | Bogie against four-wheel carriage; corridor | LYR 1895 carriage cost comparison; Tatlow Highland figures; GWR Harris figures |
| 12 | Horse prices by breed and type | Fleming, *Spectator* 1891, Board of Agriculture 1913, Moore-Colyer |
| 13 | Wagon brake equipment cost | Nothing usable |

Pages fetched and read in full: Hughes 1910 (PDF, 116 pages, text extracted), Holcroft 1923 (no cost
data, discarded), Commercial Motor 6 May 1960 price list (verified), and the search-engine text of
the Wallasey tramway page (direct fetch returned 403).

## 8. Sources

1. G. Hughes, "Compounding and Superheating in Horwich Locomotives", *Proceedings of the Institution
   of Mechanical Engineers*, 1910, vol. 78, p. 399 and discussion pp. 452-72.
   https://www.lyrs.org.uk/images/uploads/Paper_-_Hughes_1910_-_I.Mech.E_-_Compounding_and_Superheating_in_Horwich_Locomotives.pdf
2. E. M. Gass, "The Application of the Compound Principle to Locomotives", Paper 208, Institution of
   Locomotive Engineers, 29 October 1926.
   https://www.lyrs.org.uk/images/uploads/Paper_-_Gass_1927_-_I.Loco.E_-_The_Application_of_the_Compound_Principle_to_Locomotives.pdf
3. "What Will It Cost?", *The Commercial Motor*, 6 May 1960, p. 134.
   https://archive.commercialmotor.com/article/6th-may-1960/134/what-will-it-cost
4. "Trolleybuses Cheaper than Motorbuses", *The Commercial Motor*, 19 September 1952, p. 80.
   https://archive.commercialmotor.com/article/19th-september-1952/80/trolleybuses-cheaper-than-motorbuses
5. A. J. P. Wilding, "Bristol RE single-deck bus chassis", *The Commercial Motor*, 4 November 1966,
   p. 64. https://archive.commercialmotor.com/article/4th-november-1966/64/bristol-re-single-deck-bus-chassis
6. "Auto transmission for Seddon bus", *The Commercial Motor*, 1 September 1972, p. 25.
   https://archive.commercialmotor.com/article/1st-september-1972/25/auto-transmission-for-seddon-bus
7. "Municipal purchases and proposals", *The Commercial Motor*, 19 April 1932, p. 45.
   https://archive.commercialmotor.com/article/19th-april-1932/45/municipal-purchases-and-proposals
8. D. Wardale, "Piston vs Caprotti Valves - The Final Discussion?", 2009.
   https://advanced-steam.org/wp-content/uploads/2017/05/Wardale-responses-to-Caprotti-proposals-3-Sept-2009.pdf
9. History of Wallasey, "Wallasey Electric Tramway 1902-1918, part 1", quoting the Tramways Committee
   tenders of 1901.
   https://www.historyofwallasey.co.uk/wallasey/Wallasey_Electric_Tramway_(1902-1918)_part_1/index.html
10. Melbourne Tram Museum, "Building the W class tram".
    https://www.trammuseum.org.au/papers/wclassbuild.htm
11. V. C. Solomons, "Sydney's double deck electric cars", *Trolley Wire*, May 1991.
    https://www.sydneytramwaymuseum.com.au/tramway/wp-content/uploads/2023/07/245-Trolley-Wire-May-1991.pdf
12. R. N. S. Nelthorpe, letter "Shire Horses", *The Spectator*, 14 March 1891, p. 15.
    https://archive.spectator.co.uk/article/14th-march-1891/15/shire-horses
13. George Fleming, *The Practical Horse Keeper*, chapter on agricultural and heavy draught horses.
    https://chestofbooks.com/animals/horses/Practical-Horse-Keeper/Agricultural-And-Heavy-Draught-Horses.html
14. Board of Agriculture and Fisheries, *British Breeds of Live Stock*, 2nd edition, 1913.
    https://doi.org/10.5962/bhl.title.22579
15. Richard Moore-Colyer, "Aspects of Horse Breeding and the Supply of Horses in Victorian Britain",
    *Agricultural History Review* 43.1. https://www.bahs.org.uk/AGHR/PDFS/ARTICLES/43n1a4.pdf
16. Lancashire & Yorkshire Railway Society, "Carriage Costs, &c., December 1895" (National Archives
    RAIL 343/793).
    https://lyrs.org.uk/new/wp-content/uploads/2022/04/Document_1895_Carriage_Costs.pdf
