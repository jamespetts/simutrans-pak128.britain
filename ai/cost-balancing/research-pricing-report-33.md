# Articulated tractor units and semi-trailers: measured UK prices, 1896-2026

Research pass for the Pak128.Britain-Ex cost-balancing project. Written 23 November 2026.
Companion data file: `ai/temp/road-rows-tractors.csv`.

Scope: the prime mover (tractor unit, "mechanical horse", tractive unit) and the semi-trailer
as two separate capital objects, plus the split of a complete combination between them.

No `.dat` cost, runningcost or fixed_cost value was read. `.dat` files were read only for
`intro_year`, `power` and `weight`, to map measured prices onto pakset objects.
No deflator, exchange rate or other conversion was applied. All money is nominal GBP of the
year stated.

## 1. Method

1. One Exa search per turn, each naming subject, constraint, date window and source
   preference. Sixteen searches were run. Search results were treated as leads only: every
   figure below was read out of the fetched page.
2. Two source families carried the work.
   - The Commercial Motor archive (`archive.commercialmotor.com`). Article pages fetch
     directly and carry the OCR text of the printed page, including price panels and, from
     1962, whole "prices of the new models" lists. The archive's own search is behind a
     JavaScript challenge and was not used. Some article pages return an empty body on a
     first request and need retries; several 1950s pages have no usable OCR text at all.
   - Public-sector award data (`govmarket.uk`, `stotles.com`, Contracts Finder). Council
     fleet awards state the total contract value and the number of units, which gives a
     measured price per unit.
3. Industry cost tables (RHA, ERM, Logistics UK) were used only where they print a
   representative price for a named vehicle class; they are tagged ESTIMATE, not MEASURED.
4. Each figure is classified:
   - MEASURED: a price paid or tendered, or an advertised sale price.
   - LIST: a manufacturer's or dealer's asking/list price, including "price as tested".
   - ESTIMATE: a costing, model or journalistic approximation.
5. Scope is stated for every figure: chassis-cab only (a tractor has no body, so this is the
   comparable scope), with body, or a complete combination. VAT treatment is stated where the
   source states it; where it does not, that is recorded as a caution.

## 2. Measured figures

Sources are keyed [S1]...[S31] and listed in section 7. "GCW" is gross combination weight.
Pre-1973 UK prices carry purchase tax where the source includes it; Commercial Motor list
prices are generally ex-tax unless stated.

### 2.1 Mechanical horses and their trailers

| Year | Make / model | Tractor or trailer | Payload / GCW | Price (GBP) | Scope | Basis | Src | Conf. |
|---|---|---|---|---|---|---|---|---|
| 1933 | Scammell Mechanical Horse, 3-ton, 5-wheel artic | tractor | 3 ton | 300 | chassis only ("first cost of about GBP 300") | LIST (approximate) | S1 | medium |
| 1939 | Mechanical-horse equipment: 1 motive unit + 4 trailers | combination, class | not stated | 1,400 | complete, municipal specification | ESTIMATE (journalist's costing) | S2 | medium |
| 1930s (date not established) | 1 mechanical horse + 2 trailers | combination | 3 ton | 420 | complete | ESTIMATE, derived (5% interest = GBP 21; 20% depreciation = GBP 84) | S3 | low-medium |
| 1962 | Scammell 10/11-ton tractive unit, chassis | tractor | 10-11 ton payload | 1,480 | chassis, no coupling gear | LIST | S4 | high |
| 1962 | Scammell 10/11-ton tractive unit with automatic coupling | tractor | 10-11 ton payload | 1,633 | chassis + coupling gear | LIST | S4 | high |
| 1962 | Scammell 12-ton tractive unit, chassis | tractor | 12 ton payload | 1,565 | chassis, no coupling gear (1,718 with coupling) | LIST | S4 | high |
| 1964 | Scammell bogie semi-trailer, flat platform, 2 ft 6 in headboard | trailer | not stated | 1,695 | trailer only, retail after a GBP 100 cut | LIST | S5 | high |
| 1965 | Scammell Townsman 3-ton artic | combination | 3 ton | 1,737 | complete outfit "as tested" | LIST | S6 | high |

The 1930s paired figure has no year on its source page. The data file carries 1935 as a
numeric placeholder so that the row can be sorted; treat it as "1930s, exact year unknown".

The two 1962 coupling-gear figures price the fifth-wheel equivalent on a mechanical horse
family tractor: GBP 153 on the 10/11-ton unit (10.3 per cent of the chassis price) and
GBP 153 on the 12-ton unit. A tractor unit price must therefore be read as "chassis plus
coupling"; the pakset tractor object includes the coupling, so the with-coupling figure is
the comparable one.

### 2.2 Heavy tractive units, 1969-1999

| Year | Make / model | Tractor or trailer | GCW / payload | Price (GBP) | Scope | Basis | Src | Conf. |
|---|---|---|---|---|---|---|---|---|
| 1969 | York 1824 single-axle van semi-trailer, 32 ft | trailer | 24 ton GCW, 17 ton payload | 2,094 | trailer only, "subject to discount" | LIST | S7 | high |
| 1977 | Scammell Crusader | tractor | 38/44 ton range | 16,622 | basic chassis, before fifth wheel and extras ("under GBP 17,000 as tested") | LIST | S8 | high |
| 1978 | Seddon Atkinson 400 series, Cummins E290 | tractor | 32.5 ton GCW | 19,500 | basic chassis; 20,535 as tested (sleeper cab, axle option, fifth wheel) | LIST | S9 | high |
| 1980 | Leyland T45 Roadtrain 4x2 | tractor | 32.39 ton GCW | 25,495 | as tested, including GBP 500 fifth-wheel installation | LIST | S10 | high |
| 1989 | Leyland DAF 95.310 | tractor | 38 ton | 46,000 | chassis | LIST | S11 | high |
| 1989 | Scania R143 MA Topline | tractor | 38 ton | 61,680 | chassis with Topline cab | LIST | S11 | high |
| 1993 | Leyland DAF FT85.360 4x2 | tractor | 38 ton GCW | 61,080 | chassis; 64,445 as tested ex-VAT | LIST | S12 | high |
| 1996 | D-Tec spaceframe semi-trailer (Dutch) | trailer | not stated | 19,000 | trailer only, "about GBP 19,000", GBP 1,000 cheaper than aluminium-chassis equivalents | LIST (approximate) | S13 | medium |
| 1997 | DAF 95XF | tractor | 44 ton class | 72,790 | basic chassis; 78,000 as tested ex-VAT | LIST | S14 | high |
| 1997 | Scania R144 460 | tractor | 44 ton class | 79,375 | retail | LIST | S14 | high |
| 1999 | Iveco EuroTech MH 440E35 | tractor | 40 ton GTW | 56,520 | basic; 61,802 as tested ex-VAT | LIST | S15, S16 | high |
| 1999 | DAF FT 85CF 340 | tractor | 40 ton GTW | 62,360 | base list price | LIST | S16 | high |
| 1999 | Scania P114L 340 4x2 | tractor | 40 ton GTW | 54,225 | base list price | LIST | S16 | high |
| 1999 | MAN 19.364 FLS | tractor | 40 ton GTW | 52,500 | base list price | LIST | S16 | high |

The 1999 group test states its method: "The prices we have quoted in the specification panels
are the new prices given in the latest Glass's Guide." These are therefore published list
prices, not transaction prices. The same article notes that "actual selling prices rarely
have much to do with list prices".

### 2.3 Modern tractive units and trailers, 2021-2026

| Year | Make / model | Tractor or trailer | GCW / payload | Price (GBP) | Scope | Basis | Src | Conf. |
|---|---|---|---|---|---|---|---|---|
| 2021 | DAF, 4 units, Bradford MDC (Motus Commercials) | tractor | 44 ton class | 105,750 each (423,000 for 4) | chassis-cab | MEASURED (award) | S17 | high |
| 2024 | Volvo 6x2 44 t, 2 units, Perth & Kinross Council | tractor | 44 ton GTW | 138,223 each (271,900 for 2) | chassis-cab, RHD double drive | MEASURED (award) | S19 | high |
| 2024 | RHA representative 6x2 tractor, 44 t combination | tractor | 44 ton GCW | 139,243 | chassis-cab, "representative" | ESTIMATE (industry cost table) | S20 | high (as a class figure) |
| 2024 | RHA representative tri-axle curtainsider | trailer | 13.6 m | 36,946 | trailer only, 10-year depreciation assumed | ESTIMATE (industry cost table) | S20 | high (as a class figure) |
| 2025 | DAF 44 t, 7 units, with 6 BMI ejector trailers, Bradford MDC | combination | 44 ton | 1,400,085.53 for the lot | 7 tractors + 6 trailers | MEASURED (award) | S18 | high |
| c.2024-2026 (date not established) | DAF 44 t, Scottish Borders Council | tractor | 44 ton | 113,000 | chassis-cab | MEASURED (award) | S17 | medium (date) |
| c.2024-2026 (date not established) | DAF 6x2, Scottish Borders Council | tractor | not stated | 128,220 | chassis-cab | MEASURED (award) | S17 | medium (date) |
| c.2024-2026 (date not established) | Mercedes-Benz 6x4, 26,000 kg, Bradford MDC (Northside) | tractor | 26 ton | 87,160.52 | chassis-cab | MEASURED (award) | S17 | medium (date) |
| 2026 | RHA representative 6x2 tractor, 44 t combination | tractor | 44 ton GCW | 141,108 | chassis-cab, "representative" | ESTIMATE (industry cost table) | S21 | high (as a class figure) |
| 2026 | RHA representative tri-axle curtainsider | trailer | 13.6 m | 33,075 | trailer only | ESTIMATE (industry cost table) | S21 | high (as a class figure) |
| 2026 | Typical new 44 t tractor unit | tractor | 44 ton | 90,000-140,000 | chassis-cab | ESTIMATE (trade compilation) | S24 | medium |
| 2026 | Typical new tri-axle curtainsider | trailer | 13.6 m | 30,000-38,000 (worked example 34,000) | trailer only | ESTIMATE (trade compilation) | S25 | medium |
| 2026 | New Berger tautliner semi-trailer, 3 axles, coil | trailer | not stated | 31,299 | trailer only, asking price ex-VAT | MEASURED (advertised) | S26 | high |

Two modern award values are known only as combined totals. The 2025 Bradford award covers
7 x 44 t DAF tractors and 6 x BMI ejector trailers for 1,400,085.53. Splitting that requires
an assumed tractor price: at the 2024 Perth level of 138,223 the 7 tractors would take
967,561 and leave 432,524 for 6 trailers (72,087 each); at the 2021 Bradford level of
105,750 they would take 740,250 and leave 659,836 (109,973 each). Ejector trailers are
specialist capital equipment, so the higher trailer figure is the more plausible. This is
an ESTIMATE derived from measured endpoints, not a measured split.

## 3. The tractor : trailer split

### 3.1 Every paired figure found

| Year | Pair | Tractor | Trailer | Combination | Trailer share |
|---|---|---|---|---|---|
| 1962 / 1964 | Scammell 10/11-ton tractive unit (1962) + Scammell bogie semi-trailer (1964) | 1,480 | 1,695 | 3,175 | 53.4% |
| 1996 / 1997 | DAF 95XF basic (1997) + D-Tec spaceframe semi-trailer (1996) | 72,790 | 19,000 | 91,790 | 20.7% |
| 2024 | RHA cost tables, 44 t 6x2 + tri-axle curtainsider | 139,243 | 36,946 | 176,189 | 21.0% |
| 2026 | RHA cost tables, 44 t 6x2 + tri-axle curtainsider | 141,108 | 33,075 | 174,183 | 19.0% |
| 2025 | Bradford MDC, 7 tractors + 6 ejector trailers | not separable | not separable | 1,400,085.53 | not separable |

The first pair is the only pre-1990 pair found, and it is weak: the tractor is a 10/11-ton
payload unit and the trailer a bogie semi-trailer of unstated capacity, two years apart. It
is included because it is the only evidence for the early period and because it points the
opposite way to the modern pairs: on a small tractor a heavy bogie trailer cost more than the
tractor.

The 2024 and 2026 RHA pairs are the strongest evidence in the whole pass. Both figures come
from the same table, for the same vehicle class, in the same year, and the tables state that
depreciation is taken over 6 years for the tractor and 10 years for the trailer.

### 3.2 What the split means for the pakset

The working assumption recorded in the handoff (tractor about 45 per cent, trailer about
55 per cent) is not supported. For a heavy articulated combination the measured and
representative evidence puts the trailer at 19-21 per cent of capital, and the tractor at
79-81 per cent. The 1960s pair is the exception, at 53 per cent trailer, but it compares a
small tractor with a heavy trailer.

Recommended working splits, by era:

| Era | Tractor share | Trailer share | Basis |
|---|---|---|---|
| 1934-1966 (mechanical horses and small artics) | 50-60% | 40-50% | 1939 four-trailer set at 1,400 against a 300 unit implies about 275 a trailer (an inference that mixes a 1933 price with a 1939 one), i.e. a trailer at roughly half the unit price; the 1962/64 pair gives 53% trailer |
| 1967-2000 (heavy artics) | 70-78% | 22-30% | 20.7% trailer in the 1996/97 pair; trailer prices rose more slowly than tractor prices through the 1980s and 1990s |
| 2001-2026 | 78-81% | 19-22% | 21.0% (2024) and 19.0% (2026) RHA pairs; 31,299 advertised new trailer against a 138,223 measured 2024 tractor gives 18.5% |

Consequence for the pakset, stated without touching any `.dat` value: the trailers carry the
full lorry price at present, so the correction is not "raise the tractor only". It is to
price the tractor at roughly three-quarters of the combination and the trailer at roughly a
quarter, keeping the sum close to the present sum. The mechanical-horse family is the
exception: there the trailer is nearer half the combination, because the unit itself is small.

### 3.3 Maintenance and standing costs

No paired maintenance figure for tractor and trailer was found for any year before 2024.
Two modern pointers:

- RHA Cost Tables 2024, time costs for the 44 t combination, carry a line "Ownership of
  1 trailer (page 14) 4,803" against total time costs of 133,443 per year, i.e. the trailer's
  ownership charge is 3.6 per cent of the combination's time-related cost. This is a
  depreciation-and-interest charge over a 10-year trailer life, not a maintenance figure.
- The same tables give depreciation as 14.3 per cent of total cost for the combination and
  10.2 per cent for the trailer alone.

A 25/75 or 20/80 split of standing cost between trailer and tractor is therefore consistent
with the capital split, but the only figure actually printed is the trailer's 3.6 per cent
ownership line, which is a depreciation share rather than a whole standing-cost share. Treat
any maintenance split as an ESTIMATE.

## 4. Mechanical horses

- 1933: the Scammell Mechanical Horse was in full production at 25 a week and had a "first
  cost of about GBP 300" (S1). This is the only pre-war unit price found, and it is the
  anchor for the pakset object `ScammellMechanicalHorse` (intro_year 1934).
- 1939: a municipal specification of one motive unit and four trailers, for refuse
  collection, street cleansing, gully emptying and general haulage, would cost "about
  GBP 1,400", against "in the neighbourhood of GBP 3,500" for four separate modern vehicles
  (S2). This is the only pre-war statement that separates the mechanical-horse family from
  conventional lorries, and it is a class-level ESTIMATE.
- A company cost comparison reproduced by Historic Roadways gives, for "one mechanical
  horse, two trailers, driver and mate", interest on capital at 5 per cent on GBP 420, and
  depreciation at 20 per cent = GBP 84. That implies GBP 420 of capital for the unit and
  two trailers (S3). The page does not date the comparison; the figures (fuel at 1s 4d a
  gallon, wages at GBP 3 a week) place it in the 1930s. Confidence low-medium.
- 1962: Scammell's list gives 10/11-ton and 12-ton tractive units at 1,480-1,718 (S4). These
  are the heavy end of the mechanical-horse family, not the 3-ton Scarab/Townsman.
- 1965: a Townsman 3-ton outfit cost 1,737 as tested (S6). No separate tractor price was
  printed, so the split within that outfit is not measurable.
- The Karrier Cob and the Reliant are named in the brief but no measured price for either
  was found; see dead ends.

The 1948 Scarab launch (S-fail, CM 17 September 1948) has no usable price in its OCR text,
so the pakset's 1948 Scarab has no measured anchor of its own. The nearest measured points
are 300 in 1933 and 1,480 in 1962.

## 5. Electric tractor units

No UK truck manufacturer publishes a list price for an electric tractor. The DAF press
release of 5 November 2025 on the 100-unit XD Electric offer states battery, range and
charging but contains no GBP figure at all. The Volvo FH Electric model page states no
price. The Mercedes-Benz UK dealer pages (Marshall, Rygor) state no price. Prices therefore
come from teardowns and industry statements, and are ESTIMATES.

| Year | Item | Price (GBP) | Battery / range | Src | Basis |
|---|---|---|---|---|---|
| 2026 | Battery-electric arctic tractor unit, price teardown | 285,000 (component 199,008 + non-component and margin 85,992) | battery alone "could cost over 108,000" | S22 | ESTIMATE |
| 2026 | Diesel arctic tractor unit, same teardown | 130,000 (component 87,100 + 42,900) | n/a | S22 | ESTIMATE |
| 2026 | New eHGV, "around" | 300,000 | n/a | S23 | ESTIMATE |
| 2026 | New 6x2 diesel tractor unit, same source | 120,000 | n/a | S23 | ESTIMATE |

The ERM teardown is the most useful of the three because it prices a diesel and a battery
tractor on the same basis in the same year: the electric premium is 155,000, or 2.19 times
the diesel price. That ratio, not the absolute figure, is the transferable result.

Government support: from January 2024 the UK plug-in grant of up to 25,000 applied to
approved electric tractor models including the Volvo FH Electric (S29). Any price recorded
from a 2024-2026 award may therefore be net of grant; none of the awards used here states
whether it is.

Specifications read from fetched pages:

- Volvo FH Electric: up to 540 kWh on board, 460 kWh usable (S28). Volvo's 2026 FH Aero
  Electric is quoted at up to 700 km (S31).
- DAF XD Electric 350 FT 4x2 tractor: 525 kWh lithium iron phosphate pack, 462 kWh usable,
  real-world range up to 500 km, DC charging to 325 kW (S27).
- Mercedes-Benz eActros 600: 500 km range (S31, manufacturer claim).
- MAN eTGX (new generation, 2026): up to 644 kWh, up to 720 km (S31).
- Tesla Semi (European specification, shown September 2026): 550 km at 40 t, 800 kW
  Megacharging, deliveries from 2027 (S31). No UK price, and no UK order value, was found.

Running cost caution: the RHA reported in March 2026 that an electric 6x2 costs 28,282 a
year more to run than its diesel equivalent, falling to 15,738 where the 2-tonne electric
axle-weight derogation applies, with a payload penalty of up to 11.8 per cent (S30). That is
a running-cost and productivity statement, not a capital price, and it should not be used as
a capital figure.

## 6. Price per ton and price by era

### 6.1 Price per ton of gross combination weight (nominal, no deflation)

| Year | Vehicle | Price (GBP) | GCW (t) | GBP per t GCW |
|---|---|---|---|---|
| 1978 | Seddon Atkinson 400/E290 | 19,500 | 32.5 | 600 |
| 1980 | Leyland T45 Roadtrain | 25,495 | 32.39 | 787 |
| 1989 | Leyland DAF 95.310 | 46,000 | 38 | 1,211 |
| 1993 | Leyland DAF FT85.360 | 61,080 | 38 | 1,607 |
| 1999 | DAF FT 85CF 340 | 62,360 | 40 | 1,559 |
| 2021 | DAF 44 t, Bradford | 105,750 | 44 | 2,403 |
| 2024 | Volvo 44 t, Perth & Kinross | 138,223 | 44 | 3,141 |
| 2024 | RHA representative | 139,243 | 44 | 3,165 |
| 2026 | RHA representative | 141,108 | 44 | 3,207 |

Nominal price per ton of GCW rose about 5.3 times between 1978 and 2026. Because the
denominator barely moves (32.5 t to 44 t, a 35 per cent rise), almost all of that is price
inflation, not specification. The useful signal is the shape: a steep rise 1989-1993
(33 per cent in four years), flat 1993-1999, then a further rise to 2021 and 2024.

For trailers, the only pair with a stated payload is 1969: 2,094 for a 17-ton-payload van
semi-trailer, i.e. 123 per ton of payload. No later source states payload with price, so a
trailer price-per-ton series cannot be built.

### 6.2 Price by era, and the best measured tractor price for each

| Era | Best measured or listed tractor price | Item | Notes |
|---|---|---|---|
| 1896-1932 | none found | n/a | no articulated tractor price located; see dead ends |
| 1933-1948 | 300 (1933) | Scammell Mechanical Horse | only pre-war unit price; applies to the 1934 pakset object |
| 1949-1966 | 1,480 (1962), 1,633 with coupling | Scammell 10/11-ton tractive unit | 1,737 buys the complete 3-ton Townsman outfit in 1965 |
| 1967-1985 | 19,500 (1978), 25,495 (1980) | Seddon Atkinson 400; Leyland T45 Roadtrain | 16,622 for a Crusader in 1977 |
| 1986-2000 | 46,000 (1989); 61,080 (1993); 72,790 (1997); 62,360 (1999) | Leyland DAF 95.310; FT85.360; DAF 95XF; DAF 85CF | the 1999 figure is the DAF 85CF, the nearest measured ancestor of the 2000 DAF CF |
| 2001-2019 | none found | n/a | gap; interpolate with caution between 62,360 (1999) and 105,750 (2021) |
| 2020-2026 | 105,750 (2021); 138,223 (2024) | DAF 44 t; Volvo 44 t 6x2 | RHA representative 139,243 (2024) and 141,108 (2026) confirm the level |

Mapping onto the pakset objects, using only `intro_year` from the `.dat` files:

| Pakset object | intro_year | Best measured price | Year of that price |
|---|---|---|---|
| ScammellMechanicalHorse | 1934 | 300 | 1933 |
| ScammellScarab | 1948 | none (nearest 300 in 1933) | - |
| ScammellTownsman | 1967 | 1,480-1,718 | 1962 |
| LeylandT45Roadtrain | 1978 | 25,495 | 1980 |
| LeylandDAF95Artic | 1987 | 46,000 | 1989 |
| LeylandDAF85Artic | 1988 | 61,080 | 1993 |
| DAFCFArtic | 2000 | 62,360 | 1999 |
| DAFXFArtic | 2000 | 72,790 | 1997 |

The two 1930s mechanical-horse trailers and the 1978/1987 artic trailer families
(`ScammellMechHorseTrailer*`, `StandardArticTrailer*`, `LargeArticTrailer*`) should take the
trailer figures of the matching era: about 275 each implied for 1939, 1,695 (1964) and 2,094
(1969) for the 1978 family's era, 19,000 (1996) for the late 1980s and 1990s, and 33,075-
36,946 (2026/2024) for the modern family.

## 7. Sources

- [S1] Commercial Motor, 2 June 1933, page 42, "Scammell's Mechanical Horse".
  https://archive.commercialmotor.com/article/2nd-june-1933/42/scammells-mechanical-horse
- [S2] Commercial Motor, 31 March 1939, page 99, "Value of the Mechanical Horse to the Small
  Town". https://archive.commercialmotor.com/article/31st-march-1939/99/value-of-the-mechanical-horse-to-the-small-town
- [S3] Historic Roadways, "Hooves v Wheels" (company cost comparison, undated).
  http://www.historicroadways.co.uk/hooves-v-wheels.html
- [S4] Commercial Motor, 2 March 1962, page 69, "Prices of the new models" (Scammell list).
  https://archive.commercialmotor.com/article/2nd-march-1962/69/prices-of-the-new-models
- [S5] Commercial Motor, 31 July 1964, page 35, "Lower prices for Scammell units".
  https://archive.commercialmotor.com/article/31st-july-1964/35/lower-prices-for-scammel-i-units-b-ecause-of-incre
- [S6] Commercial Motor, 11 June 1965, page 62, road test of the Scammell Townsman 3-ton artic.
  https://archive.commercialmotor.com/article/11th-june-1965/63/mechani-horse-si-il-ie
- [S7] Commercial Motor, 4 July 1969, page 62, "Variety in standard" (York semi-trailers).
  https://archive.commercialmotor.com/article/4th-july-1969/62/variety-in-standard
- [S8] Commercial Motor, 16 December 1977, page 30, "Crusader goes on Rolls standard".
  https://archive.commercialmotor.com/article/16th-december-1977/33/crusader-goes-on-rolls-standard
- [S9] Commercial Motor, 26 May 1978, page 81, Seddon Atkinson 400/E290 road test.
  https://archive.commercialmotor.com/article/26th-may-1978/83/graham-ivlontgomerie-tests-the-new-cummins-powered
- [S10] Commercial Motor, 5 July 1980, page 118, "Top of the list features in T45".
  https://archive.commercialmotor.com/article/5th-july-1980/118/top-of-the-list-features-in-t45
- [S11] Commercial Motor, 12 January 1989, page 34, "38 tonne: three axle".
  https://archive.commercialmotor.com/article/12th-january-1989/34/38-tonne-three-axle
- [S12] Commercial Motor, 9 September 1993, page 36, Leyland DAF FT85.360 road test.
  https://archive.commercialmotor.com/article/9th-september-1993/36/price-as-tested-64445-ex-vat-includes-61080-for-ft
- [S13] Commercial Motor, 5 September 1996, page 39, "Which curtainsider gives you outstanding
  value for money?".
  https://archive.commercialmotor.com/article/5th-september-1996/39/which-curtiainsider-gives-you-outstanding-value-fo
- [S14] Commercial Motor, 23 October 1997, page 39, DAF 95XF road test.
  https://archive.commercialmotor.com/article/23rd-october-1997/39/212-roadtest
- [S15] Commercial Motor, 8 July 1999, page 29, "Eurotech Cursor".
  https://archive.commercialmotor.com/article/8th-july-1999/29/eurotech-cursor
- [S16] Commercial Motor, 23 December 1999, page 25, four-marque tractive unit group test
  (prices from Glass's Guide).
  https://archive.commercialmotor.com/article/23rd-december-1999/25/its-a-commercialmotortradition-that-every
- [S17] GovMarket, "Purchase of 4 Tractor Units for Bradford Metropolitan District Council",
  awarded 17 September 2021, value 423,000, supplier Motus Commercials/DAF; page also lists
  related awards to Scottish Borders Council (44 t DAF tractor, 113,000; DAF 6x2 tractor,
  128,220) and Bradford (26,000 kg 6x4 tractor, Mercedes, 87,160.52).
  https://govmarket.uk/contract/purchase-of-4-tractor-units-for-bradford-metropolitan-district-council-281683
- [S18] GovMarket, "Supply of 7 Tractor Units and 6 Ejector Trailers to City of Bradford
  Metropolitan District Council", awarded 14 April 2025, value 1,400,085.53, supplier Motus
  Commercials (DAF chassis, BMI trailers).
  https://govmarket.uk/contract/supply-of-7-tractor-units-and-6-ejector-trailers-to-city-of-bradford-metropolitan-district-council-228921
- [S19] Stotles notice, "GB-Perth: TPPL Perth & Kinross Council NEPO HGV Lot 1 - 2 x RHD
  Double Drive Tractor Unit Chassis with a Minimum GTW of 44t (15515)", value 271,900,
  supplier Volvo Truck and Bus. The per-unit figure of 138,223 was supplied in the task
  brief and was not re-derived here.
  https://www.stotles.com/explore/notices/8bd69667-f611-4845-8f19-e4233d8c88f8/gb-perth-tppl-perth-kinross-council-nepo-hgv-lot-1-2-x-rhd-double-drive-tractor-unit-chassis-with-a-minimum-gtw-of-44t-15515
- [S20] Road Haulage Association, Cost Tables 2024, pages 13-14 (44 t 6x2 + tri-axle
  combination; tri-axle trailer).
  https://www.rha.uk.net/Portals/0/Membership/Annual%20Cost%20and%20Pay%20Surveys/Cost-Tables-2024.pdf
- [S21] Road Haulage Association, Cost Tables 2026, pages 13-14.
  https://www.rha.uk.net/Portals/0/Membership/Annual%20Cost%20and%20Pay%20Surveys/Cost%20Tables%202026.pdf
- [S22] ERM, "Upfront Pricing of eHGVs: Risks and Opportunities for Electric Truck Uptake",
  March 2026, section 4 price teardown of a diesel and BEV arctic tractor unit.
  https://www.erm.com/globalassets/reports/upfront_pricing_of_ehgvs_risks_and_opportunities_for_electric_truck_uptake.pdf
- [S23] Logistics UK, Project JOLT blog, 13 May 2026.
  https://logistics.org.uk/blog/project-jolt-discovering-the-economic-viability-of-an-electric-fleet/
- [S24] The Fleet Magazine, "How Much Does a Lorry Cost in the UK? New and Used HGV Prices",
  13 October 2026. https://thefleetmagazine.co.uk/how-much-does-a-lorry-cost-in-the-uk-new-and-used-hgv-prices/
- [S25] The Fleet Magazine, "Trailer Leasing vs Ownership Costs for UK Hauliers",
  16 September 2026. https://thefleetmagazine.co.uk/trailer-leasing-vs-ownership-costs-for-uk-hauliers/
- [S26] Market-Truck.co.uk, new Berger tautliner semi-trailer, 3 axles, coil, 31,299 ex-VAT.
  https://www.market-truck.co.uk/berger-tautliner-semi-trailer/3-axles-nordrhein-westfalen/ts-vi11513505/new.html
- [S27] DAF Trucks UK, press release 5 November 2025, "DAF Trucks pledges diesel parity with
  100 XD Electric tractors".
  https://www.daf.co.uk/en-gb/news-and-media/news-articles/gb/2025/daf-trucks-pledges-diesel-parity-with-100-xd-electric-tractors-and-bold-five-year-tco-claim
- [S28] Volvo Trucks UK, Volvo FH Electric model page (540 kWh, 460 kWh usable).
  https://www.volvotrucks.co.uk/en-gb/trucks/electric/volvo-fh-electric.html
- [S29] Volvo Trucks UK, press release 12 January 2024, plug-in grant of up to 25,000.
  https://www.volvotrucks.co.uk/en-gb/news/press-releases/2024/first-volvo-electric-tractor-units-approved-for-governments-25000-plug-in-grant.html
- [S30] Motor Transport, 27 March 2026, "Call to increase gross vehicle weights to boost eHGV
  uptake" (RHA running-cost comparison).
  https://motortransport.co.uk/call-to-increase-gross-vehicle-weights-to-boost-ehgv-uptake/89795.article
- [S31] EVwire, "Electric truck specs compared: Europe" (accessed 23 November 2026).
  https://evwire.com/etrucks/specs

## 8. Dead ends and cautions

1. **1896-1932.** No articulated tractor price was found. Articulated steam and petrol
   tractors of that period were one-off or converted machines and no price list or award
   value surfaced. Any pakset object in this window has no measured anchor.
2. **Commercial Motor 1950s road tests.** The 27 November 1953 ERF 10-ton artic test and the
   25 May 1956 Leyland Comet tractor test both fetch with a body of 9,000 characters that
   contains no figures at all: the pages are image-only or the OCR failed. Several other
   article pages return an empty body on the first request and need retries. The archive is
   usable but not reliably so before about 1960.
3. **Karrier Cob and Reliant.** No measured price for either was found. The 9 December 1930
   Karrier article on "the tractor which displaces the horse" carries no price in its OCR
   text, and no Reliant mechanical-horse price surfaced.
4. **Scammell Scarab, 1948.** The launch article (17 September 1948) has no usable price
   text. No 1948-1955 Scarab price was found, so the pakset's 1948 object has no measured
   anchor nearer than 1933.
5. **2001-2019 tractors.** No measured figure was found. Commercial Motor road tests of the
   2004-2016 period were searched and returned no price panel in their OCR text. The gap
   between 62,360 (1999) and 105,750 (2021) is real and should not be interpolated as if it
   were measured.
6. **Electric list prices.** No UK list price for any electric tractor exists in public form.
   The DAF, Volvo and Mercedes-Benz UK pages state none. All electric figures here are
   ESTIMATES from teardowns and industry statements. The Tesla Semi has no UK price and no
   UK order value; its European specification was shown only in September 2026 with
   deliveries from 2027.
7. **VAT.** Pre-1973 list prices are generally ex-purchase-tax. 1990s Commercial Motor road
   tests state "ex-VAT". Modern council award values do not usually state whether VAT is
   included; the Bradford 2021 award (423,000 for 4 units) is consistent with ex-VAT at the
   market level of the time, but this is inference, not stated.
8. **Scottish Borders awards.** The 113,000 and 128,220 awards appear in GovMarket's related
   contracts panel without dates. A search of the Scottish Borders contract register for 2026
   found only a "Purchase of Tractor Unit & Palfinger Crane" (235,168, awarded 6 October
   2025), which is a crane purchase and not comparable. The two figures are recorded with a
   date caution.
9. **Trailer maintenance.** No paired tractor/trailer maintenance figure was found for any
   year. The only printed trailer-specific cost is the RHA's 4,803 a year ownership charge
   for a tri-axle trailer in 2024, which is depreciation and interest, not maintenance.
10. **RHA cost tables 2014.** The 2014 edition fetched but its tractor price (77,500 per an
    index highlight) could not be confirmed in the extracted text, so it is not used.
11. **thefleetmagazine and similar compilations.** Ranges such as 90,000-140,000 for a new
    44 t tractor are secondary summaries of the market, not quotes. They are used only to
    corroborate the measured and RHA figures, never as the sole basis for a row.
