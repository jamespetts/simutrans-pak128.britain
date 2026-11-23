---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Aircraft crew complements

**Covers**: flight-deck and cabin crew complements for every vehicle object in `New/air/`,
`New/air/air192/` and `New/air/air256/`, and the declarations made in the `.dat` files.

The complements are declared as `staff[10]` flight deck and `staff[11]` cabin crew. Across the 230
objects they total 596 flight-deck persons and 449 cabin crew. See
[../crew-complements](../crew-complements.md) for the role map and
[aircraft/register](aircraft/register.md) for the airframe table.

## Scope and method

- **Airframe** means the base object for a type; the high-density, mail, freight and car variants
  are separate objects in the same `.dat` file. Each object carries its own declaration.
- **Seats** is the sum of the `payload[n]` classes of that object. It is the pakset's capacity, not
  any real cabin layout.
- **Year** is the pakset `intro_year`.
- **Flight deck crew** and **cabin crew** are whole persons. The composition follows in brackets.
- Coverage: **230 objects** in 136 files, belonging to 112 airframes: 108 with a passenger object
  and four represented only by mail or freight objects (`MailMonoPlane`, `dhc3-otter`,
  `boeing-707-320c`, `atr-42-300f`). The 182 objects in `air/`, 27 in `air192/` and 21 in
  `air256/` all compile into the same pak set.
- Cabin crew are computed **per object** from its own seat total, so 30 of the 50 high-density
  variants carry more cabin crew than the base airframe. Flight-deck complements are inherited by
  the variant.
- Flight deck complements take five values: 1, 2, 3, 4 and 5. Cabin crew values run from 0 to 12.
  The most frequent combination is two pilots with two cabin crew, on 17 objects.

## Rules applied

### F1: one pilot

Used where single-pilot operation was normal for the type: the Lockheed Vega, the Lockheed Model 9
Orion, the DH.89 Dragon Rapide, and the light twins certificated for single-pilot operation (Aero
Commander 520 and 681, King Air 200, Twin Otter).

The Junkers F 13 and W 34 are **not** F1. The F 13 source describes a two-seat open cockpit, and
the W 34 is its derivative with the same arrangement; two flight-deck persons is the sourced figure
and both are recorded with 2. The earlier one-pilot assumption is withdrawn. `[LITERATURE:
https://en.wikipedia.org/wiki/Junkers_F_13]`

### F2: two pilots

Every multi-engine public-transport aeroplane is assigned two pilots.

- The legal floor is the Air Navigation Order 1960, article 14(3): a flying machine registered in the United Kingdom and flying for public transport with a maximum total weight authorised of more than 22,500 lb "shall carry not less than two pilots as members of the flight crew thereof".
- The Order sets the floor only for aircraft above 22,500 lb. Several early multi-engine types in table 1 are below it: the Handley Page O/400 and W.8b, the Ford Trimotor, the Junkers Ju 52/3m, the Douglas DC-2 and the Lockheed Model 10 Electra. They are recorded with two pilots because two-pilot operation was the practice for multi-engine airline types of the period. That is an assumption, not a source-backed figure for each type.
- The Beech 18, the two Aero Commanders, the King Air 200 and the Twin Otter are also below the threshold. The Beech 18 and the Aero Commanders are recorded with two pilots on the same assumption; the King Air and the Twin Otter are recorded with one because they are single-pilot certificated and were commonly flown by one pilot.

### F6: two pilots, glass cockpit

The two-crew widebody standard established by the 757 and 767 certification. Boeing's account of that programme records that the Secretary of Transportation appointed a task force headed by a former FAA Administrator, that the task force determined "three crew members are not safer than two" while the 757 and 767 were still in certification testing, and that this ended the argument about crew complement for later jet transports. The 747-400 (1989) deleted the flight engineer's station; the 747-8 and the 787 were designed for two crew.

### F3: two pilots and a flight engineer

Assigned where the type carried a flight engineer as part of its certificated or standard operating crew.

- The FAA type certificates required a flight engineer on the four-engine piston types and on the early jets. The list given in the cited summary is the Boeing 307, 377, DC-6, DC-7, Constellation, 707, 727, early 747, DC-8, DC-10, L-1011 and early A300. The smaller twinjets (DC-9, 737, BAC One-Eleven, Caravelle) did not require one.
- The pakset types whose flight decks carried an engineer are the Boeing 307, 707, 727, 747 classic, DC-6, DC-7, DC-8 and L-1011 TriStar, plus the non-US types: Bristol Britannia, Comet, VC10, Trident, Vanguard, Ambassador, Caravelle, Convair 880 and 990, and L-188 Electra.
- The Boeing account records the 707, 727 and 747 as three-crew aeroplanes and the DC-9, BAC One-Eleven and 737 as two-crew aeroplanes.
- Not assigned to: DC-3, DC-4, the DC-9/737/BAC One-Eleven class of twins, and every glass-cockpit type from 1981.

The 707, DC-8, VC10, Comet and Britannia rows are F4 or F5 rather than F3 because they also carried a navigator or radio operator.

**When the flight engineer's seat went.** The 737 was certificated for two pilots from the start (1967) and never carried a flight engineer. The 757 and 767 certification established the two-crew widebody. The 747-400 (1989) was the first 747 without a flight engineer's station, and the 747-8 and 787 followed. The types that kept a flight engineer for the whole of their service, with real service-entry years, include the 707 (1958), 727 (1964), 747 classic (1970), DC-8 (1959), L-1011 TriStar (1972), VC10 (1964) and Concorde (1976; the BEA report of 2000 still records the officier mecanicien navigant). The last 747 classic in US passenger service, a 747-200, was retired in 2009, and the last 727 in major cargo service in 2013.

### F2r: two pilots and a radio operator

The DH.91 Albatross is documented with a crew of four: pilot, co-pilot, radio operator and steward. It carried no flight engineer, so the third flight-deck member is the radio operator.

### F4: F3 plus a navigator

Assigned to the long-range types that were designed and operated before self-contained navigation:

- Air Navigation Order 1960, article 14(4): a UK-registered aircraft on public transport "shall carry a flight navigator as a member of the flight crew if on the route or any diversion therefrom, being a route or diversion planned before take-off, the aircraft is intended to be more than 500 nautical miles from the point of take-off measured along the route to be flown, and over part of an area specified in the Eighth Schedule to this Order" (the oceanic and polar areas).
- Boeing's flight-deck engineers record that VOR removed the need for navigators over land in the 1950s and that "the requirement for a navigator on intercontinental flights would continue until the advent of the airborne Inertial Navigation System (INS) in the late 1960s".

Assigned to: DC-6, DC-6B, Boeing 377, Bristol Britannia, Comet 1, Comet 4, 4B and 4C, 707-120, 707-420, DC-8-10, VC10, Super VC10.

In table 1 the navigator appears on types entering service between 1943 and 1965. No type entering service after 1965 is assigned one.

Not assigned to: the 747 (in service 1970, after airborne INS had removed the requirement), the TriStar, Concorde (documented crew of three: two pilots and a flight engineer), and every short- and medium-range type.

The certificated minimum crew of the 707 and DC-8 was three; the fourth seat was the navigator's and was required by route rules, not by the type certificate. The table records the operational complement at entry into service, not the certificated minimum.

### F5: F4 plus a radio operator

Assigned to the five-crew long-range piston types: L-049, L-1049C, L-1049G, L-1649, DC-7 and DC-7C.

- Boeing's account gives the norm for long-range piston types as five: "two pilots, a flight engineer, a navigator, and a radio operator".
- Air Navigation Order 1960, article 14(5): an aircraft required to carry radio apparatus "shall carry flight radio operator as member of the flight crew, who, if he is required to operate radiotelegraph apparatus, shall be carried in addition to any other person who is carried in accordance with this Article to perform other duties".
- The dedicated radio officer is not assigned to any airframe family introduced after 1958. Jane's 1965 lists the Comet 4's fourth flight-deck member as "radio operator/navigator", one person holding both roles, and the 707, DC-8 and VC10 carried a navigator only.

In table 1 the radio operator appears on types entering service between 1943 and 1957.

### F7: airship control-car watch

Airships have no direct equivalent of an aeroplane flight deck. The figures are the control-car watch on duty, not the whole ship's company.

- The two pre-1914 ships, LZ 6 and LZ 10, carried one watch: commander, helmsman and mechanic. These two remain estimates.
- The two large ships carried three watches. LZ 127's watch was the watch officer, navigator, helmsman and radio officer. LZ 129's was the watch officer, navigator, rudderman, elevatorman and radio officer. The 1929 LZ 127 crew list has no elevatorman rating, so LZ 127 stays at four.

The radio room was a separate compartment above the control car. If it is excluded from the flight deck, the figures are 3 and 4 rather than 4 and 5.

### C1: one cabin crew member per 50 seats, rounded up

The ratio applied is the EASA/UK rule in ORO.CC.100(b)(3) of Regulation (EU) No 965/2012 as retained in UK law: "one cabin crew member for every 50, or fraction of 50, passenger seats installed on the same deck of the aircraft to be operated". The same wording appears in JAR-OPS 1.990(b)(1) and EU-OPS OPS 1.990(b)(1), which governed European operations before October 2014.

Applied as `ceil(seats / 50)`.

The ATR type certificate independently gives the same answer for the pakset's ATR 42 and ATR 72: minimum cabin crew 1 for 50 or fewer installed seats and 2 for 51 to 78. The ATR rows are therefore consistent with both the ratio and the type certificate.

### C0: no cabin crew

ORO.CC.100(a) requires at least one cabin crew member only where the maximum operational passenger seating configuration exceeds 19. Types of 19 seats or fewer are recorded with 0.

Some small types did carry a steward or stewardess. The Boeing 247, with 10 seats, is recorded with 1 under C2.

### C2: documented number recorded instead of the ratio

Used where a specific documented figure was found:

- Concorde: 6 cabin crew. The BEA final report on F-BTSC records 3 flight crew (PNT) and 6 cabin crew (PNC) for 100 passengers. The ratio would give 2.
- Boeing 307 Stratoliner: 2 cabin crew. The documented complement is five: pilot, co-pilot, flight engineer and two cabin attendants. The ratio would give 1.
- Boeing 247: 1 cabin crew. The documented complement is three. The ratio would give 0.

## Sources

| URL | What it supports |
|---|---|
| https://www.legislation.gov.uk/uksi/1960/972/pdfs/uksi_19600972_en.pdf | Air Navigation Order 1960, article 14. Paragraph (3): two pilots required on public-transport flying machines over 22,500 lb. Paragraph (4): flight navigator required beyond 500 nm if the route crosses an Eighth Schedule area. Paragraph (5): flight radio operator required on aircraft required to carry radio apparatus. Read as extracted text, pages 14 and 16. |
| https://www.legislation.gov.uk/eur/2012/965/annex/III/division/subpart+cc/data.xht | ORO.CC.100. Paragraph (a): one cabin crew member required only above 19 seats. Paragraph (b)(3): one cabin crew member per 50 or fraction of 50 passenger seats on the same deck. |
| https://eur-lex.europa.eu/eli/reg/2012/965/oj/eng | Commission Regulation (EU) No 965/2012, the instrument containing Part-ORO and Part-CAT. |
| https://ad.easa.europa.eu/blob/SIB_2014_29_withdrawn.pdf/SIB_2014-29_1 | EASA Safety Information Bulletin 2014-29, pages 3-5. Quotes JAR-OPS 1.990 and EU-OPS OPS 1.990 in full: one cabin crew member for every 50, or fraction of 50, passenger seats on the same deck, with at least one cabin crew member above 19 seats. States that under those rules the 50:1 limit became in practice the only limit, because the alternative certification-demonstration limit could be reduced. |
| https://www.easa.europa.eu/sites/default/files/dfu/TCDS_ATR_EASA_A_084_Issue-14.pdf | EASA type certificate data sheet EASA.A.084 for the ATR 42 and ATR 72. Section 18: minimum flight crew two (pilot and co-pilot). Section 19: minimum cabin crew 1 for 50 or fewer seats, 2 for 51-60 (ATR 42) and 51-78 (ATR 72). Pages 18 and 38. |
| https://www.bea.aero/uploads/tx_elydbrapports/f-sc000725.pdf | BEA final report on the Concorde F-BTSC accident, 25 July 2000. Page 13 and section 1.1: nine crew on board, "3 PNT, 6 PNC", with 100 passengers. Section 1.5.1.3 identifies the third flight crew member as the "officier mecanicien navigant" (flight engineer). |
| https://ethw.org/First-Hand:Evolution_of_the_2-Person_Crew_Jet_Transport_Flight_Deck | First-hand account by four Boeing flight-deck engineers. Five-crew norm for long-range piston types (two pilots, flight engineer, navigator, radio operator). VOR removed navigators over land in the 1950s; navigators on intercontinental flights until airborne INS in the late 1960s. FAA approval of two pilots as the 737 minimum crew. The 707, 727 and 747 as three-crew types and the DC-9, BAC One-Eleven and 737 as two-crew types. The crew-complement task force appointed by the Secretary of Transportation and the two-crew 757/767. |
| https://en.wikipedia.org/wiki/Flight_engineer | Summary of which FAA type certificates required a flight engineer: the Boeing 307, 377, DC-6, DC-7, Constellation, 707, 727, early 747, DC-8, DC-10, L-1011 and early A300, and that the DC-9, 737, BAC One-Eleven and Caravelle did not. |
| https://en.wikipedia.org/wiki/Boeing_747 | Flight crew 3 for the 747 (classic) infobox. |
| https://en.wikipedia.org/wiki/Boeing_747-8 | Flight crew 2. |
| https://en.wikipedia.org/wiki/Boeing_787_Dreamliner | Flight crew 2. |
| https://en.wikipedia.org/wiki/Boeing_707 | Flight crew 3. |
| https://en.wikipedia.org/wiki/Boeing_727 | Flight crew 3. |
| https://en.wikipedia.org/wiki/Boeing_737 | Flight crew 2. |
| https://en.wikipedia.org/wiki/De_Havilland_Comet | Comet specifications table: cockpit crew 4 (2 pilots, flight engineer and radio operator/navigator), citing Taylor 1965 (Jane's), pp. 153-154. |
| https://en.wikipedia.org/wiki/Vickers_VC10 | Crew 4 plus 3 flight attendants. |
| https://en.wikipedia.org/wiki/Hawker_Siddeley_Trident | Cockpit crew 3: captain, first officer and flight engineer. |
| https://en.wikipedia.org/wiki/Douglas_DC-8 | Cockpit crew 3. |
| https://en.wikipedia.org/wiki/Lockheed_L-1011_TriStar | Cockpit crew 3. |
| https://en.wikipedia.org/wiki/Sud_Aviation_Caravelle | Flight crew 2 or 3. |
| https://en.wikipedia.org/wiki/Convair_880 | Crew 3. |
| https://en.wikipedia.org/wiki/Convair_990_Coronado | Crew 4 plus cabin crew. |
| https://en.wikipedia.org/wiki/Lockheed_L-188_Electra | Crew 3. |
| https://en.wikipedia.org/wiki/Vickers_Vanguard | Crew 3. |
| https://en.wikipedia.org/wiki/Airspeed_Ambassador | Crew 3. |
| https://en.wikipedia.org/wiki/Bristol_Britannia | Crew 4-7. |
| https://en.wikipedia.org/wiki/Boeing_377_Stratocruiser | Crew 4 flight crew (captain, first officer, flight engineer, navigator) plus 2-3 cabin crew. |
| https://en.wikipedia.org/wiki/Lockheed_Constellation | Crew 5 flight crew, varying cabin crew. |
| https://en.wikipedia.org/wiki/Lockheed_L-1049_Super_Constellation | Crew 5: pilot, copilot, navigator, flight engineer, radio operator. |
| https://en.wikipedia.org/wiki/Lockheed_L-1649_Starliner | Crew 5. |
| https://en.wikipedia.org/wiki/Douglas_DC-7 | Crew 5 flight crew, 4 flight attendants. |
| https://en.wikipedia.org/wiki/Douglas_DC-6 | Crew 3 to 4. |
| https://en.wikipedia.org/wiki/De_Havilland_Albatross | Crew 4: pilot, co-pilot, radio operator and steward. |
| https://en.wikipedia.org/wiki/Boeing_307_Stratoliner | Crew 5, including pilot, co-pilot, flight engineer and two flight attendants. |
| https://en.wikipedia.org/wiki/Boeing_247 | Crew 3. |
| https://en.wikipedia.org/wiki/Douglas_DC-4 | Crew 4. |
| https://en.wikipedia.org/wiki/Douglas_DC-3 | Crew two. |
| https://en.wikipedia.org/wiki/Douglas_DC-2 | Crew two to three. |
| https://en.wikipedia.org/wiki/Junkers_Ju_52 | Crew two. |
| https://en.wikipedia.org/wiki/Handley_Page_Type_W | Crew 2. |
| https://en.wikipedia.org/wiki/Handley_Page_Type_O | Crew 4 or 5 (military). |
| https://en.wikipedia.org/wiki/Junkers_F_13 | Crew two. |
| https://en.wikipedia.org/wiki/Junkers_W_34 | Crew 2. |
| https://en.wikipedia.org/wiki/Ford_Trimotor | Crew 3 (pilot, co-pilot, flight attendant). |
| https://en.wikipedia.org/wiki/Lockheed_Vega | Crew 1. |
| https://en.wikipedia.org/wiki/Lockheed_Model_9_Orion | Crew 1. |
| https://en.wikipedia.org/wiki/De_Havilland_Dragon_Rapide | Crew 1. |
| https://en.wikipedia.org/wiki/Lockheed_Model_10_Electra | Crew 2. |
| https://en.wikipedia.org/wiki/Beechcraft_Model_18 | Crew 2 pilots. |
| https://en.wikipedia.org/wiki/Beechcraft_1900 | Crew 1 (2 for airline operations). |
| https://en.wikipedia.org/wiki/Dornier_228 | Crew 2. |
| https://en.wikipedia.org/wiki/Fairchild_Swearingen_Metroliner | Crew 2 (captain and first officer). |
| https://en.wikipedia.org/wiki/Fokker_50 | Crew 2 flight crew. |
| https://en.wikipedia.org/wiki/Fokker_F27_Friendship | Crew 2 or 3. |
| https://en.wikipedia.org/wiki/British_Aerospace_ATP | Crew four: two pilots and two flight attendants. |
| https://en.wikipedia.org/wiki/British_Aerospace_146 | Crew 2. |
| https://en.wikipedia.org/wiki/BAC_One-Eleven | Cockpit crew 2. |
| https://en.wikipedia.org/wiki/Airbus_A320_family | Cockpit crew two. |
| https://en.wikipedia.org/wiki/ATR_42 | Cockpit crew two. |
| https://en.wikipedia.org/wiki/Embraer_ERJ_family | Cockpit crew two. |
| https://en.wikipedia.org/wiki/Embraer_E-Jet_family | Cockpit crew two. |
| https://en.wikipedia.org/wiki/Concorde | Crew 3: two pilots and one flight engineer. |
| https://en.wikipedia.org/wiki/LZ_127_Graf_Zeppelin | Total crew 36 (airship). |
| https://en.wikipedia.org/wiki/LZ_129_Hindenburg | Total crew 40 to 61 (airship). |
| https://en.wikipedia.org/wiki/Zeppelin_LZ_10 | Total crew 13 (airship). |

Wikipedia is a secondary source. It is cited only for per-type figures that were not available in a manufacturer or certification document at the time of writing, and its figures are cross-checked against the rule where the two overlap.

## Gaps and estimates

| Row or group | Status | Assumption |
|---|---|---|
| `zeppelin-lz6`, `Zeppelin_LZ10`, `zeppelin-lz127`, `zeppelin-lz-129` | documented except the two pre-1914 ships | LZ 6 and LZ 10: 3 (commander, helmsman, mechanic, one watch) is an estimate. LZ 127: 4 (watch officer, navigator, helmsman, radio officer, three watches) is documented from the 1929 crew list. LZ 129: 5 (watch officer, navigator, rudderman, elevatorman, radio officer, three watches) is documented. Cabin crew: LZ 127 carries 3 and LZ 129 carries 8 from the documented complements, not the C1 ratio. |
| `junkers-f13`, `junkers-w34` | resolved | Two. The F 13 source describes a two-seat open cockpit, and the W 34 has the same arrangement; the earlier one-pilot assumption is withdrawn. |
| `HandleyPageO400` | estimate | Two pilots assumed for the 1918 twin-engine type. In military service the O/400 carried a crew of four or five including observer and gunners; the civil conversion is not separately documented here. |
| `ford-trimotor` | estimate | Two pilots. Wikipedia gives a crew of three including a flight attendant; the pakset row records no cabin crew because the type is below 20 seats and the attendant was not universal. |
| `beechcraft-18`, `lockheed-10-electra`, `aero-commander-520`, `aero-commander-681`, `king-air-200`, `twin-otter-300` | estimate | Two pilots (Beech 18, Electra 10) or one pilot (light twins) by the airline-use assumption. All are below the 22,500 lb threshold of the 1960 Order, so no legal minimum applies. |
| `dh-comet-1` | documented | Four: two pilots, flight engineer and navigator, from the four-place cockpit. |
| `Boeing_707_120`, `boeing-707-420`, `douglas-dc-8-10` | estimate | Four assumed (two pilots, flight engineer, navigator). The certificated minimum was three; the navigator was a route requirement under the 1960 Order and was deleted when inertial navigation arrived in the late 1960s. An earlier radio operator would make five; that combination is recorded for the piston types, not for these. |
| `bristol-britannia` | estimate | Four assumed. The source gives 4-7 without a breakdown. |
| `douglas-dc-6`, `douglas-dc-6b` | estimate | Four assumed (two pilots, flight engineer, navigator or radio operator). The source gives 3 to 4. The higher figure is used because the type was operated transatlantically. |
| `convair-cv990` | partial | Four is documented, but the role of the fourth member is not stated. A navigator is assumed. |
| `airspeed-ambassador` | partial | Three is documented; the composition (two pilots plus flight engineer) is inferred. |
| All cabin-crew figures except Concorde, Boeing 307 and Boeing 247 | rule | C1 is a legal minimum, not the staffing an airline actually carried. Airline staffing in the 1950s to 1970s was generally above the minimum. No per-type figure above the minimum was adopted because the sources found give ranges or do not separate cabin from flight crew. The table keeps the ratio so that every row can be regenerated from the seat count. |
| Years | pakset data | `intro_year` from the `.dat`. The 737-900ER row carries 1998, which precedes the real service entry in 2007. |
| Seats | pakset data | Sum of the `payload[n]` classes. The pakset distributes seats across travel classes in a way no real cabin does, and the totals differ from any manufacturer configuration. |

## Notes on individual rows

- `boeing-737-900er`: the object name is `boeing-737-900er`, the type is the 737-900ER, and the pakset year is 1998.
- `boeing-707-320c`: the pakset models this airframe only as a mail carrier. It is in table 2 rather than table 1.
- `dhc3-otter`: the pakset models this airframe only as a mail carrier. It is in table 2.
- `MailMonoPlane`: a generic 1910 mail monoplane, not a named type. One pilot is an estimate.
- The high-density variants (`-high-density`) and the cargo and mail variants (`-post`, `-piece`, `-cool`, `-mail`) inherit the airframe's crew and are not listed separately.
