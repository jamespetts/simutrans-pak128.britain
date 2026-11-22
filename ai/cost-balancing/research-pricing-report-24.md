# Research pass 24 — anecdotal and source-backed cost and reliability differentials: aircraft, ships, trams

Status: draft evidence. Compiled 2026-11-22. Output for the parent session. The knowledge base is
not edited here.

**Covers**: British-operated aircraft types, British coastal, ferry and cargo ships, and British
tramcars and tram equipment, where a contemporary or near-contemporary source says the type, class
or builder was more or less expensive to build or maintain, or more or less reliable, than a
comparable one. Each row gives the direction, the mechanism, the source and a confidence grade.

**Companion file**: `research-pricing-rows-24.csv` — 63 rows: 27 prices or contract figures and
36 adjustments (16 aircraft, 11 ship, 9 tram).

**Rule observed throughout**: no Simutrans `.dat` price was read, used or fitted to. The fitted
ladders in `New/ai/vehicle-cost-method.md` are used once, as a cross-check on whether a measured
price is high or low for its specification, and never as the source of an adjustment.

---

## 1. Method, grades and what "adjustment" means

One web search per turn through the Exa-backed `websearch` tool, then the page fetched and read
before any claim was used. Where a page blocked fetching (Cloudflare, paywall, 403) the claim is
either dropped or carried at low confidence with the block recorded, never silently promoted.

Three kinds of evidence are kept apart:

- **Measured** — a contract, published price, company account or Government answer for a named
  type. These rows state a real number.
- **Stated** — a named engineer, operator, museum or historian says a type was expensive,
  unreliable or durable, without a number. The adjustment is then a band.
- **Inferred** — a band transferred from a measured related case. Marked low confidence.

| Grade | Meaning |
|---|---|
| High | A primary document states it (Hansard, a company table) or two independent sources agree |
| Medium-high | One good source with a clear mechanism, or a primary figure with an uncertain basis |
| Medium | One secondary source, no contradiction found |
| Low-medium / Low | Inference, a stated reputation without a number, or a blocked/untraced source |

**Direction convention.** In the CSV, `kind=adjustment` rows state a signed percentage in `price`.
Positive raises cost; negative lowers it. `scope` says whether it applies to build, maintenance,
operating cost or availability. `kind=price` rows state money in `price_unit`.

**The adjustment layer must not double-count.** Where a real price row exists for the same item
(for example the Super VC10 against the 707), the model should use the price row instead of the
capped percentage, not both.

---

## 2. Aircraft

### 2.1 de Havilland Comet 1 — small production run and a short-life engine

Two independent cost mechanisms, both measured:

- **Engine life.** The Ghost 50 required a combustion-chamber inspection every 125 hours and a
  complete overhaul every 375 hours. The Dart in the Viscount was cleared to 1,050 hours in
  1956-57 and 1,600 hours in 1958. The Comet's engine therefore went to overhaul about 2.8 times
  as often as the best turboprop in British service. The later Avon 524 in the Comet 2 was cleared
  to 1,000 hours by 1958, which shows the 375-hour figure is an early-jet figure, not a de
  Havilland figure.
- **Production volume.** Hansard's 1955 table records Comet I net development expenditure of
  £4.25m against 19 aircraft ordered and 9 delivered. After the 1954 grounding de Havilland held
  about £15m of unsalable aircraft, jigs and tools. The fixed cost per delivered airframe was
  therefore very high.

The price band in the 1953 Lords debate is £500,000-£750,000 for "the jet aircraft, such as the
Comet, and the turbo-prop, such as the Britannia — the big ones", against £250,000-£300,000 for a
Viscount. A Comet was therefore roughly twice a Viscount for a similar order of seating capacity.
Lord De L'Isle's phrase — the Comet II cost "as much as an ocean-going merchant ship of 5,000 gross
tons" — is the single most useful cross-domain sentence found in the pass.

**Adjustment**: build +15, maintenance +15. Confidence medium-high for the engine, medium for the
build.

### 2.2 Bristol Britannia — early engine problems, then a productive aircraft

The Proteus entered service at 500 hours between overhauls. BOAC's Britannias suffered 16
in-flight engine failures and 49 unscheduled engine changes in the first eight months of
operational trials (secondary count, but consistent with Hansard). Entry was two years late. The
Government had put £18m of public money into the aircraft by November 1957 and BOAC lost about £2m
that year.

The important counterweight: by August 1958 the fleet was achieving 3,750 hours per aircraft a
year, described as unprecedented for a trunk route, and the Proteus had been cleared to 1,600
hours, rising to 2,400 by 1962. The Britannia's cost problem was concentrated in the introduction,
not spread over its life.

**Adjustment**: maintenance +10, reliability +10, no build adjustment. The £768,000 price agreed
in 1955 falls within the Comet/Britannia band quoted in 1953 and is not obviously a premium price.

### 2.3 Vickers VC10 — expensive to buy, expensive per hour, but not unreliable

This is the most interesting case in the pass because the reputation and the measurements
conflict.

- **Price.** Vickers quoted £1,750,000 a copy in 1957 on a 35-aircraft order. By 1959 the agreed
  price was £1.2m when a realistic price was £1.4m. The Super VC10 cost "something like £3.5
  million" in 1964 against £2.75m for a Boeing 707 with spares: a measured +27 per cent.
  Vickers also paid BOAC £20,000 per Standard VC10 for missing the drag and operating-cost
  guarantees — about 1.3 per cent of an airframe, and evidence that the cost problem was known and
  priced at delivery.
- **Engineering cost per flying hour.** £130 against £120 for the 707-436 in 1969/70 (+8 per
  cent), and £154 against £141 in 1972/73 (+9 per cent). Against the later 707-336 the gap is
  wider (+27 to +31 per cent), but that is a different engine and airframe, so it is not a fair
  like-for-like.
- **Reliability.** In the same 1964 statement the Minister of Aviation said the VC10 "has lost
  only about half the time through maintenance trouble that was lost by the Boeing 707" in its
  introductory period, despite the 707 having been proved by Pan American first.

The mechanism is weight and drag, not unserviceability. B.O.A.C. demanded short-field performance;
the resulting weight penalty raised fuel burn and "marginally increased running costs" — the
Minister's own words. The VC10 is a case where an operator-imposed specification, not the type's
engineering, set the cost.

**Adjustment**: Super VC10 build +15 (measured +27, capped); Standard VC10 build 0, because its
contract price of £1.2-1.4m shows no premium over the 707; both maintenance +10; availability −5.

### 2.4 Hawker Siddeley Trident — a capacity decision with a cost consequence

BEA cut the DH.121 from 111-130 seats to 79-90 at its own insistence, in the belief that the
Vanguard would hold the trunk routes. The 727-200 and DC-9 were then more economical "in terms of
range, revenue generation and seat-mile costs". The 1959 contract was £28m for 24 aircraft
(£1.167m each on the compiler's division, which may include spares).

There is no measured Trident maintenance differential. The defensible statement is about seat-mile
cost, and it is a capacity effect, not an engineering one.

**Adjustment**: operating +5 only. Confidence low-medium.

### 2.5 Concorde — the largest measured maintenance differential in the pass

Air France reckoned 20 maintenance man-hours per flight hour, about double a Mirage III. On a
capacity basis both BA and Air France spent about five times as much on maintenance as on their
747 fleets. Separately, Concorde averaged 782 hours per aircraft-year in 1977-78 against over
4,000 for the 747 fleet, so fixed cost per hour added a second penalty.

Programme cost to 1978: £575m development, £352m production, £139m receipts. The 1972 list price
was US$33.8m, but BA and Air France did not pay it; the aircraft passed through government
arrangements at far lower prices. The list price is therefore not an operator's cost and should be
used with that caveat.

**Adjustment**: maintenance +15 (the cap understates a 5x measured ratio; the model's
size/capacity term must account for the rest), fixed +10.

### 2.6 Short Belfast — volume, not engineering

Ten aircraft were built against a forecast break-even of 30, on production jigs. Development cost
was refused in the Commons. A drag problem held the first five aircraft below the guaranteed
performance until a rear fairing was developed. The class is a pure fixed-cost-recovery case.

**Adjustment**: build +15. Confidence medium.

### 2.7 Vickers Vanguard — cheap per seat-mile, wrong decade

The Vanguard's reputation as a failure is a market-timing judgement, not a cost judgement. In the
139-seat all-tourist layout it had "very low operating costs per seat-mile". Its real defects were
a Tyne compressor problem that delayed entry by about a year, and a passenger preference for jets
that no cost advantage could overcome. Trans-Canada kept a Constellation on standby because a Tyne
might fail to start.

BEA's 1962-63 report put the combined cost of introducing the Comet 4B and the Vanguard at more
than £6m over two years. The split is not published.

**Adjustment**: introduction +5, maintenance +5, operating −5. These largely cancel; the net is
small and the confidence is low.

### 2.8 Vickers Viscount — the counter-example

A Dart ran more than 5,000 hours between overhauls in 1964, "the longest operating time between
overhauls for which any aero engine has remained in an aircraft". BEA extended V.701 check 4 from
1,500 to 3,000 hours in 1957-58. The Viscount is the benchmark against which the Britannia,
Comet and Vanguard engine burdens should be read.

**Adjustment**: maintenance −10.

---

## 3. Ships

### 3.1 Diesel against steam — first cost up, upkeep down

Four independent cost tables agree on the direction and roughly on the size:

| Year | Source | Diesel machinery against steam |
|---|---|---|
| 1921 | Barfoed, *The Motor Ship* | whole ship +9 per cent against oil-fired turbine, +11 per cent against coal triple expansion |
| 1926 | Cleghorn, Inst. Engineers and Shipbuilders in Scotland | +79 per cent at 2,500 shp against coal reciprocating; +41 per cent at 6,000 shp |
| 1928 | Seaton, *Manual of Marine Engineering* | +110 per cent against triple expansion, +42 per cent against geared turbine |
| 1932 | Freeman, IMechE | +3 to +23 per cent against high-pressure steam turbine |

Machinery is only part of a ship, so the whole-ship build premium is about +10 per cent for a
1920s cargo ship. That is the row to use.

On the other side, Alfred Holt's Blue Funnel fleet published actual costs, analysed by
L. H. Cripps in 1930. Taking the steamer *Arteus* as 100:

| Ship | Propulsion | Engine upkeep | Engine stores | Cost per 7,800 t cargo |
|---|---|---|---|---|
| Arteus | steam reciprocating, coal | 100 | 100 | 100 |
| Keemun | steam reciprocating, coal | 143 | 112 | 105.3 |
| Nestor | steam reciprocating, superheated | 198 | 88 | 94.8 |
| Adrastus | steam turbine, coal | 75 | 97 | 80.7 |
| Sarpedon | steam turbine, superheated, coal | 162 | 131 | 95.2 |
| Antenor | steam turbine, superheated, oil | 161 | 123 | 106.8 |
| Peisander | diesel | 56 | 84 | 45.3 |
| Orestes | diesel | 68 | 92 | 47.1 |
| Dolius / Medon | diesel | 49 | 92 | 43.5 |

Diesel engine upkeep was 49-68 per cent of the steamer baseline, and total cost per cargo ton
43-47 per cent. Those are measured fleet figures, not estimates. They are also much larger than a
15 per cent adjustment, so the layer caps them and leaves the rest to the fuel and crew terms.

The qualification: diesel needed more skilled engineers, had higher spare-gear and lubricating-oil
charges, and early reliability was suspect enough that twin screws were used as insurance. The
maintenance advantage is real but it is not free.

**Adjustment**: motor ship build +10, maintenance −15, stores −5, operating −15.

### 3.2 Turbine against reciprocating

Turbine machinery cost 12-18 per cent more than reciprocating in 1926 and 48 per cent more in
1928, but it was smoother and more compact at high power. For cargo ships the reciprocating engine
survived on first cost. For fast ferries the 1954 Watson report came down for steam turbines in the
fast ships and diesels for the rest — a service-speed decision, not a simple cost ranking. That
zero row is recorded so the point is not lost.

**Adjustment**: geared turbine build +5.

### 3.3 Builders, yards and national cost

- Vickers' crosshead marine diesel had three broken crankshafts to 1930 and four ships towed to
  port with defective machinery. A builder-specific reliability penalty of +10 per cent is
  defensible for that engine family.
- Furness Withy ordered five motor ships from Deutsche Werft in 1925 at £150,000 each because
  British tenders were £60,000-100,000 higher. No British yard would match even a £10,000 premium.
  That is a +40 to +67 per cent gap, capped at +15.
- The same difference appears again: in 1969 the Stranraer-Larne ferry went to an Italian yard whose tender
  was £250,000 below the next lowest on a £2.5m ship (+10 per cent), with a better delivery date.
  British Railways maintained a buy-British policy until 1971 in spite of the premium.

### 3.4 Ferry prices

| Ship | Year | Cost | Note |
|---|---|---|---|
| Lord Warden | 1952 | £0.7m | steam car ferry, Dover Straits |
| Maid of Kent | 1959 | £1.7m | larger and faster |
| Hengist | 1972 | £4.0m | 840 cars, 5,600 passengers per 12 h, 79 crew |
| St Anselm | 1980 | £18.0m | end of the series |

These are nominal and not like-for-like. They are useful as scale anchors, not as a price index.

---

## 4. Trams

### 4.1 Prices found

| Item | Year | Price | Basis |
|---|---|---|---|
| Perth, Dick Kerr car | 1900 | about £600 | newspaper approximation |
| LCC F class, United Electric Car Co. | 1908 | £750 | unit price |
| Northampton, Brush body | 1914 | £460 | body only |
| Northampton, Dick Kerr equipment | 1914 | £289 14s 6d | electrical equipment |
| Northampton, complete | 1914 | £749 14s 6d | sum of the two contracts |
| Blackpool Standard, Hurst Nelson | 1926 | £1,750 | contractor price |
| Average car, 56-60 seats | 1934 | £2,000 | *Commercial Motor* average |
| Glasgow Coronation 1282 | 1940 | £3,354 | cost when new |

The Northampton pair is the most useful because it splits body from electrical equipment: the
equipment was about 39 per cent of the complete car. That is a direct check on any tram ladder that
treats the car as one homogeneous product.

### 4.2 Builder spreads

- Blackpool built 35 "rebuilds" in its own works for £400 less per car than Hurst Nelson's £1,750,
  a measured −23 per cent. The in-house cars were accounted as rebuilds and used some new parts, so
  the comparison overstates the in-house advantage; the cap is −15. This is the only same-design,
  same-year builder comparison in the pass whose page could be read in full.
- The Wallasey 1902 tender list and the Accrington 1907 contract would give two more same-year
  spreads (about 12 per cent at Wallasey; an unquantified "slightly higher" tender at Accrington),
  but neither page could be fetched (see dead ends). On the readable evidence there is no consistent
  "Brush premium" or "Dick Kerr discount" across the period. The defensible statement is that
  builders competing for the same order differed by roughly a tenth, and that a municipal works
  could beat all of them.

### 4.3 Class and equipment effects

- **Glasgow Coronation (1937-41).** High specification — teak body rails, Alhambrinal panelling,
  EMB lightweight bogies, heating and ventilation — and £3,354 new in 1940. Stated to be "expensive
  to build and operate", and unsuitable for tight curves. Build +15, maintenance +10.
- **Glasgow Cunarder (1948-52).** The same family, simplified for maintenance and weight, but "not
  regarded as being as quite as reliable or capable as the Coronation trams". Maintenance +5. This
  is a within-class comparison, which is the cleanest tram evidence in the pass.
- **Glasgow Kilmarnock-bogie cars (1928).** Prone to derailing on Glasgow's curves and restricted to
  straight, flat routes. Maintenance +10, and a warning that vehicle-track interaction can dominate
  a class's reputation.
- **Feltham (1931).** The three prototypes had non-standard equipment and caused maintenance
  problems; two were disposed of early. The 100 production cars were standard and lasted to the end
  of London's tramways. +10 applies to the prototypes only.
- **Leeds Horsfield (1930-31)** and **Blackpool Standard (1923-32).** Both are standardised,
  all-route designs; the Horsfield body rests on the truck rather than being bolted to it, which
  made truck replacement quick. −5 maintenance each. These are reputational, not measured.

### 4.4 The maintenance benchmark

H. Scott Hall's 1934 comparison in *The Commercial Motor* is the best single tram cost source
found: a tram cost £2,000, had a 300,000-mile life and cost 1.50d a mile to maintain, against 2.33d
for a petrol bus and an oil bus. That is a measured −36 per cent in favour of the tram, before the
track and overhead line are charged. Capped at −15 for the cross-mode row.

The 1913 ICE split used in pass 15 (about 0.58d per car-mile, 30 per cent of the combined
statutory head) points the same way and is consistent with Hall's 1.50d figure once the price level
and the later date are allowed for.

---

## 5. Recommended adjustment table

Only the values the evidence supports. All are qualitative unless the basis column says
"measured".

| Domain | Item | Scope | Per cent | Confidence | Basis |
|---|---|---|---:|---|---|
| Aircraft | Comet 1 | build | +15 | Medium | 9-12 airframes against £4.25m development |
| Aircraft | Comet 1 | maintenance | +15 | Medium-high | Ghost 375 h overhaul against Dart 1,050 h |
| Aircraft | Britannia | maintenance | +10 | Medium-high | Proteus 500 h at entry against Dart 1,050 h |
| Aircraft | Britannia | availability | +10 | Medium-low | 16 failures and 49 engine changes in trials |
| Aircraft | Standard VC10 | build | 0 | Medium-high | contract price £1.2-1.4m; no measured premium over the 707 |
| Aircraft | Standard VC10 | maintenance | +10 | Medium-high (measured +8/+9) | £130 against £120 per hour, 1969/70 |
| Aircraft | Standard VC10 | availability | −5 | Medium-high | Half the 707's maintenance-lost time |
| Aircraft | Super VC10 | build | +15 | High (measured +27, capped) | as above |
| Aircraft | Super VC10 | maintenance | 0 | Medium-high (measured −6 to +3) | within noise of the 707-436 |
| Aircraft | Trident 1C | operating | +5 | Low-medium | shrunk to 79-90 seats; higher seat-mile cost |
| Aircraft | Concorde | maintenance | +15 | Medium-high (measured about 5x) | 20 man-hours per flight hour |
| Aircraft | Concorde | fixed cost | +10 | High for hours, medium for value | 782 h/year against 4,000 |
| Aircraft | Belfast | build | +15 | Medium | 10 built against break-even 30 |
| Aircraft | Vanguard | build/introduction | +5 | Low | share of BEA's £6m introduction cost |
| Aircraft | Vanguard | maintenance | +5 | Low-medium | Tyne compressor defects, standby aircraft |
| Aircraft | Vanguard | operating | −5 | Medium-low | very low seat-mile cost at 139 seats |
| Aircraft | Viscount | maintenance | −10 | Medium-high | Dart 5,000 h overhaul life |
| Ship | Motor ship, 1920s-30s | build | +10 | Medium | machinery +41 to +79 (1926); whole ship +9 to +11 (1921) |
| Ship | Motor ship, 1920s-30s | maintenance | −15 | Medium-high (measured −32 to −51) | Blue Funnel engine upkeep |
| Ship | Motor ship, 1920s-30s | stores | −5 | Medium | Blue Funnel engine stores |
| Ship | Motor ship, 1920s-30s | operating | −15 | Medium-high (measured −53 to −57) | cost per cargo ton |
| Ship | Geared turbine | build | +5 | Medium | machinery +12 to +18 per cent |
| Ship | Vickers marine diesel | maintenance | +10 | Medium-high | crankshaft failures and tows |
| Ship | British yard, 1920s | build | +15 | Medium (measured +40 to +67, capped) | German tender comparison |
| Ship | British yard, 1960s | build | +10 | Medium-high (measured) | Italian tender £250,000 lower |
| Tram | Contractor-built vs municipal works | build | +15 | Medium (measured −23 for in-house, capped) | Blackpool |
| Tram | Glasgow Coronation | build | +15 | Medium | £3,354 in 1940; high specification |
| Tram | Glasgow Coronation | maintenance | +10 | Low-medium | "expensive to build and operate" |
| Tram | Glasgow Cunarder | maintenance | +5 | Low-medium | less reliable than the Coronation |
| Tram | Glasgow Kilmarnock bogie | maintenance | +10 | Medium | derailment-prone on Glasgow track |
| Tram | Feltham prototypes | maintenance | +10 | Low-medium | non-standard equipment |
| Tram | Leeds Horsfield | maintenance | −5 | Low-medium | standard, all-route, easy truck swap |
| Tram | Blackpool Standard | maintenance | −5 | Low-medium | standard, long-lived, cheap to run |
| Tram | Generic tram vs bus | maintenance | −15 | High (measured −36, capped) | 1.50d against 2.33d per mile, 1934 |

**How to apply.** Multiply the build ladder by (1 + build adjustment) and the maintenance ladder by
(1 + maintenance adjustment). Do not stack a real price row with its own percentage. Do not apply
the ship national-premium rows to a named class: they describe a country's yards, not a vessel.

---

## 6. The strongest statements in the pass

1. **Comet II cost "as much as an ocean-going merchant ship of 5,000 gross tons"** — HL Deb
   17 Feb 1953, c.456. A direct, contemporary cross-domain price comparison.
2. **"The VC10 has lost only about half the time through maintenance trouble that was lost by the
   Boeing 707"** — HC Deb 22 Jul 1964, c.503. The best single corrective to the VC10's reputation.
3. **Concorde: 20 maintenance man-hours per flight hour; about five times the 747's maintenance per
   unit of capacity** — Australian Aviation, Jan 1987.
4. **Blue Funnel diesel engine upkeep 49-68 per cent of the steamer baseline; total cost per cargo
   ton 43-47 per cent** — Cripps, Trans. INA 72 (1930), via Griffiths (1994).
5. **Tram maintenance 1.50d a mile against 2.33d for a bus, 1934** — H. Scott Hall, *The Commercial
   Motor*, 9 Feb 1934, p.110.
6. **Blackpool saved £400 a car by building in its own works against Hurst Nelson's £1,750** —
   National Tramway Museum, Blackpool 40.
7. **The Ghost needed a complete overhaul every 375 hours** — This Day in Aviation, citing the
   Ghost 50's service schedule; the Dart reached 5,000 hours by 1964.

---

## 7. Dead ends, recorded so they are not retried

- **Wallasey 1902 tender list.** The page gives four tenders for 20 cars (Electric Railway & Tramway
  Carriage Works £11,800; British Westinghouse £11,940 plus £1,000 for air brakes; Brush £13,200;
  Blackwell £13,925), which would be a clean same-year builder spread of about 12 per cent. The site
  returned Cloudflare 403 on fetch. Not used as evidence; recorded in the report only.
- **Accrington 1907 contract.** A book viewer page shows Brush winning a combined cars-and-overhead
  contract at £19,450 over a "slightly higher" Dick Kerr tender. The viewer could not be fetched
  reliably; not used.
- **Short Belfast unit price.** Hansard refused the development cost in 1962 and no unit price was
  found in Flight, Hansard or the RAF Museum file. The row is a volume adjustment only.
- **Comet 1 price of £275,000 (1952).** Asserted by French Wikipedia, citing Flight 1974. It
  conflicts with the 1953 Lords band of £500,000-750,000 and with the 1946 contract price of about
  £450,000. Untraced; do not use.
- **Concorde's actual British Airways purchase price.** The aircraft passed through government
  arrangements at prices far below the $33.8m list. No reliable per-airframe figure was found, and
  the list price is not an operator's cost.
- **IEE 1932 paper "Modern tramway rolling stock" (E. R. L. Fitzpayne).** The most promising source
  for Glasgow per-car costs and maintenance. The IET Digital Library returned 403.
- **Hurst Nelson (Price, 1978).** Internet Archive copy is lending-only; no text.
- **Lloyd's List.** Not accessible without a subscription. The casualty evidence used here comes
  from Griffiths' thesis, which worked the casualty lists.
- **The Motor Ship / Le Mesurier & Humphreys (1934-35).** Only the title and the tables reproduced
  in Griffiths were obtainable; the paper itself was not.
- **Cometra's BOAC Comet 4 introduction PDF.** 403 on download. Its snippet ("cheap price at the
  bowsers", reduced maintenance from smooth jet running) was not used because the page could not be
  read.
- **Glasgow municipal tramway committee minutes.** Not online in text form; the Glasgow evidence is
  museum and encyclopedia level only.
- **Flight pdfarchive links.** Most original `flightglobal.com/pdfarchive` URLs are dead; Wayback
  copies work for some pages (the 1972 price index did), but not reliably.

---

## 8. Largest gaps

1. **No measured per-class tram maintenance figure.** The 1934 *Commercial Motor* rate and the 1913
   ICE split are system averages. A municipal abstract of accounts that separates "repairs and
   maintenance of cars" from permanent way would settle it; none is online.
2. **No British aircraft engine removal rate per 1,000 hours.** Overhaul life is a proxy. The
   RAeS 1966 paper "Lessons from Engine Experience" plots unscheduled removals and in-flight
   shutdowns for four Rolls-Royce engines; the graph is behind a paywall and was not read.
3. **No ship repair cost by British builder.** The Blue Funnel data is operator-level and the
   Vickers failure count is a casualty-list proxy. A yard's repair accounts would be better.
4. **No Belfast or Britannia development cost split.** Hansard gives programme totals, not the
   per-aircraft fixed cost the model needs.
5. **No 1945-1980 British tram building prices beyond Glasgow.** The period after 1945 is almost
   empty: the Cunarder is the only class with a reputation statement, and no price was found for it.

---

## 9. Proposed knowledge-base changes (for review; nothing edited)

- Add a short subsection to `New/ai/vehicle-cost-evidence.md` under aircraft: "Engine overhaul life
  as the maintenance axis", with the Ghost 375 h, Proteus 500 h, Dart 1,050-5,000 h and Avon 524
  1,000 h figures, and the VC10 reliability correction.
- Add to the ship section the Blue Funnel relative-cost table and the 1926/1932 machinery-cost
  tables, as the measured basis for a motor-ship build premium and maintenance discount.
- Add to the tram section the Northampton body/equipment split, the Blackpool in-house comparison
  and the 1934 *Commercial Motor* rates, and note that builder spreads are about 10-15 per cent
  rather than a consistent brand premium.
- Record in `New/ai/vehicle-cost-method.md` that production volume is a missing regressor: the
  Comet 1 and Belfast are the two clear cases where the fitted ladder cannot see the fixed-cost
  recovery per airframe.
