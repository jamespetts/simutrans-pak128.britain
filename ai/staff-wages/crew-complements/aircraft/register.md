---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Crew register: aircraft

Evidence for [../aircraft.md](../aircraft.md). One row per airframe, not per object.

The pakset holds 230 air vehicle objects in three folders (`air/`, `air192/`, `air256/`): 158
passenger objects (108 airframes plus 50 `-high-density` variants), 39 mail objects and 33 freight
objects. Each object carries its own declaration. The cabin-crew column below is the base
airframe's figure; 30 of the 50 high-density variants carry more cabin crew because their own seat
total crosses a 50-seat boundary. The full object-level table is in the research record used to
make the declarations, and the declared values are in the `.dat` files. `[CODE New ex-15 working
tree, 2026-11-23]`

## Table 1: passenger airframes

| Pakset object | Manufacturer and type | Year | Seats | Flight deck crew | Cabin crew | Basis |
|---|---|---:|---:|---|---:|---|
| `zeppelin-lz6` | Luftschiffbau Zeppelin LZ 6 | 1909 | 20 | 3 (3 in the control-car watch) | 1 | F7, C1 - estimate |
| `Zeppelin_LZ10` | Luftschiffbau Zeppelin LZ 10 Schwaben | 1911 | 20 | 3 (3 in the control-car watch) | 1 | F7, C1 - estimate |
| `HandleyPageO400` | Handley Page O/400 | 1918 | 8 | 2 (2 pilots) | 0 | F2, C0 - twin-engine |
| `junkers-f13` | Junkers F 13 | 1920 | 4 | 2 (2 pilots) | 0 | F2, C0 - two-seat open cockpit, sourced |
| `HandleyPageW8b` | Handley Page W.8b | 1921 | 12 | 2 (2 pilots) | 0 | F2, C0 - twin-engine |
| `ford-trimotor` | Ford Trimotor | 1926 | 12 | 2 (2 pilots) | 0 | F2, C0 - three-engine |
| `junkers-w34` | Junkers W 34 | 1926 | 6 | 2 (2 pilots) | 0 | F2, C0 - two-seat cockpit, same arrangement as the F 13 |
| `lockheed-vega` | Lockheed Vega | 1928 | 6 | 1 (1 pilot) | 0 | F1, C0 - single-engine |
| `zeppelin-lz127` | Luftschiffbau Zeppelin LZ 127 Graf Zeppelin | 1928 | 20 | 4 (4 in the control-car watch) | 1 | F7, C1 - estimate |
| `ju-52` | Junkers Ju 52/3m | 1931 | 17 | 2 (2 pilots) | 0 | F2, C0 - three-engine |
| `lockheed-orion` | Lockheed Model 9 Orion | 1931 | 6 | 1 (1 pilot) | 0 | F1, C0 - single-engine |
| `boeing-247` | Boeing 247 | 1933 | 10 | 2 (2 pilots) | 1 | F2, C2 - documented crew of three including one cabin attendant |
| `Douglas_DC2` | Douglas DC-2 | 1934 | 14 | 2 (2 pilots) | 0 | F2, C0 |
| `dragon-rapide` | de Havilland DH.89 Dragon Rapide | 1934 | 8 | 1 (1 pilot) | 0 | F1, C0 - single-engine |
| `lockheed-10-electra` | Lockheed Model 10 Electra | 1935 | 10 | 2 (2 pilots) | 0 | F2, C0 |
| `Douglas_DC3` | Douglas DC-3 | 1936 | 21 | 2 (2 pilots) | 1 | F2, C1 - radio operator carried by some operators |
| `zeppelin-lz-129` | Luftschiffbau Zeppelin LZ 129 Hindenburg | 1936 | 50 | 4 (4 in the control-car watch) | 1 | F7, C1 - estimate |
| `beechcraft-18` | Beechcraft Model 18 | 1937 | 8 | 2 (2 pilots) | 0 | F2, C0 - airline operation |
| `dh-91-albatross` | de Havilland DH.91 Albatross | 1938 | 22 | 3 (2 pilots + radio operator) | 1 | F2r, C1 - documented crew of pilot, co-pilot, radio operator and steward |
| `Douglas_DC3A` | Douglas DC-3A | 1939 | 21 | 2 (2 pilots) | 1 | F2, C1 - radio operator carried by some operators |
| `boeing-307-stratoliner` | Boeing 307 Stratoliner | 1940 | 33 | 3 (2 pilots + flight engineer) | 2 | F3, C2 - documented crew of five including two cabin attendants |
| `douglas-dc-4` | Douglas DC-4 | 1942 | 80 | 2 (2 pilots) | 2 | F2, C1 - no flight engineer required |
| `lockheed-l049-constellation` | Lockheed L-049 Constellation | 1943 | 60 | 5 (2 pilots + flight engineer + navigator + radio operator) | 2 | F5, C1 |
| `bristol-type-170` | Bristol Type 170 Freighter/Wayfarer | 1946 | 44 | 2 (2 pilots) | 1 | F2, C1 |
| `douglas-dc-6` | Douglas DC-6 | 1946 | 48 | 4 (2 pilots + flight engineer + navigator) | 1 | F4, C1 |
| `vickers-vc1b-viking` | Vickers VC.1B Viking | 1946 | 24 | 2 (2 pilots) | 1 | F2, C1 |
| `boeing-377` | Boeing 377 Stratocruiser | 1949 | 84 | 4 (2 pilots + flight engineer + navigator) | 2 | F4, C1 - documented four flight crew |
| `vickers-vc2-viscount-757` | Vickers Viscount 757 | 1950 | 70 | 2 (2 pilots) | 2 | F2, C1 |
| `aero-commander-520` | Aero Commander 520 | 1951 | 7 | 1 (1 pilot) | 0 | F1, C0 - light twin, single-pilot certificated |
| `airspeed-ambassador` | Airspeed AS.57 Ambassador | 1951 | 60 | 3 (2 pilots + flight engineer) | 2 | F3, C1 - composition inferred from a documented crew of three |
| `lockheed-l1049-c-super-constellation` | Lockheed L-1049C Super Constellation | 1951 | 64 | 5 (2 pilots + flight engineer + navigator + radio operator) | 2 | F5, C1 |
| `douglas-dc-6b` | Douglas DC-6B | 1952 | 89 | 4 (2 pilots + flight engineer + navigator) | 2 | F4, C1 |
| `lockheed-l1049-g-super-constellation` | Lockheed L-1049G Super Constellation | 1952 | 62 | 5 (2 pilots + flight engineer + navigator + radio operator) | 2 | F5, C1 |
| `dh-comet-1` | de Havilland Comet 1 | 1952 | 36 | 4 (2 pilots + flight engineer + navigator) | 1 | F4, C1 - estimate; no crew breakdown located |
| `douglas-dc7` | Douglas DC-7 | 1953 | 64 | 5 (2 pilots + flight engineer + navigator + radio operator) | 2 | F5, C1 |
| `aero-commander-681` | Aero Commander 681 Turbo Commander | 1955 | 11 | 1 (1 pilot) | 0 | F1, C0 - light twin, single-pilot certificated |
| `douglas-dc7c` | Douglas DC-7C | 1956 | 70 | 5 (2 pilots + flight engineer + navigator + radio operator) | 2 | F5, C1 |
| `vickers-vc2-viscount-802` | Vickers Viscount 802 | 1956 | 80 | 2 (2 pilots) | 2 | F2, C1 |
| `bristol-britannia` | Bristol Britannia | 1957 | 139 | 4 (2 pilots + flight engineer + navigator) | 3 | F4, C1 - source gives 4-7 for the type; 4 assumed |
| `lockheed-l1649-starliner` | Lockheed L-1649 Starliner | 1957 | 67 | 5 (2 pilots + flight engineer + navigator + radio operator) | 2 | F5, C1 |
| `Boeing_707_120` | Boeing 707-120 | 1958 | 137 | 4 (2 pilots + flight engineer + navigator) | 3 | F4, C1 - certificated minimum 3; navigator added for oceanic operation |
| `fokker-f27-100` | Fokker F27-100 | 1958 | 44 | 2 (2 pilots) | 1 | F2, C1 |
| `lockheed-electra-l188` | Lockheed L-188 Electra | 1958 | 74 | 3 (2 pilots + flight engineer) | 2 | F3, C1 |
| `dh-comet-4` | de Havilland Comet 4 | 1958 | 56 | 4 (2 pilots + flight engineer + radio operator/navigator) | 2 | F4, C1 - Jane's 1965: 4, the fourth being radio operator/navigator |
| `douglas-dc-8-10` | Douglas DC-8-10 | 1959 | 144 | 4 (2 pilots + flight engineer + navigator) | 3 | F4, C1 - certificated minimum 3; navigator added for oceanic operation |
| `Fokker-F27-200` | Fokker F27-200 | 1959 | 44 | 2 (2 pilots) | 1 | F2, C1 |
| `lockheed-electra-l188-c` | Lockheed L-188C Electra | 1959 | 74 | 3 (2 pilots + flight engineer) | 2 | F3, C1 |
| `caravelle` | Sud Aviation Caravelle | 1959 | 72 | 3 (2 pilots + flight engineer) | 2 | F3, C1 - documented as 2 or 3; 3 with a flight engineer |
| `dh-comet-4b` | de Havilland Comet 4B | 1959 | 71 | 4 (2 pilots + flight engineer + radio operator/navigator) | 2 | F4, C1 |
| `boeing-707-420` | Boeing 707-420 | 1960 | 141 | 4 (2 pilots + flight engineer + navigator) | 3 | F4, C1 - certificated minimum 3; navigator added for oceanic operation |
| `convair-cv880` | Convair 880 | 1960 | 88 | 3 (2 pilots + flight engineer) | 2 | F3, C1 |
| `vickers-vanguard-952` | Vickers Vanguard 952 | 1960 | 127 | 3 (2 pilots + flight engineer) | 3 | F3, C1 |
| `dh-comet-4c` | de Havilland Comet 4C | 1960 | 79 | 4 (2 pilots + flight engineer + radio operator/navigator) | 2 | F4, C1 |
| `convair-cv990` | Convair 990 Coronado | 1961 | 92 | 4 (2 pilots + flight engineer + navigator) | 2 | F4, C1 - four documented; the role of the fourth member is not stated |
| `vickers-vanguard-953` | Vickers Vanguard 953 | 1962 | 135 | 3 (2 pilots + flight engineer) | 3 | F3, C1 |
| `boeing-727-100` | Boeing 727-100 | 1964 | 122 | 3 (2 pilots + flight engineer) | 3 | F3, C1 |
| `hs-trident-1c` | Hawker Siddeley Trident 1C | 1964 | 88 | 3 (2 pilots + flight engineer) | 2 | F3, C1 |
| `super-caravelle` | Sud Aviation Super Caravelle | 1964 | 104 | 3 (2 pilots + flight engineer) | 3 | F3, C1 |
| `vickers-vc10` | Vickers VC10 | 1964 | 109 | 4 (2 pilots + flight engineer + navigator) | 3 | F4, C1 |
| `bac-1-11-200` | BAC One-Eleven 200 | 1965 | 89 | 2 (2 pilots) | 2 | F2, C1 |
| `vickers-super-vc10` | Vickers Super VC10 | 1965 | 139 | 4 (2 pilots + flight engineer + navigator) | 3 | F4, C1 |
| `boeing-727-200` | Boeing 727-200 | 1967 | 154 | 3 (2 pilots + flight engineer) | 4 | F3, C1 |
| `boeing-737-100` | Boeing 737-100 | 1967 | 85 | 2 (2 pilots) | 2 | F2, C1 |
| `Fokker-F27-500` | Fokker F27-500 | 1967 | 52 | 2 (2 pilots) | 2 | F2, C1 |
| `bac-1-11-500` | BAC One-Eleven 500 | 1968 | 119 | 2 (2 pilots) | 3 | F2, C1 |
| `boeing-737-200` | Boeing 737-200 | 1968 | 97 | 2 (2 pilots) | 2 | F2, C1 |
| `hs-trident-2e` | Hawker Siddeley Trident 2E | 1968 | 115 | 3 (2 pilots + flight engineer) | 3 | F3, C1 |
| `twin-otter-300` | de Havilland Canada DHC-6 Twin Otter 300 | 1969 | 20 | 1 (1 pilot) | 1 | F1, C1 - single-pilot certificated |
| `boeing-747-100` | Boeing 747-100 | 1970 | 352 | 3 (2 pilots + flight engineer) | 8 | F3, C1 |
| `boeing-747-200` | Boeing 747-200 | 1971 | 366 | 3 (2 pilots + flight engineer) | 8 | F3, C1 |
| `hs-trident-3b` | Hawker Siddeley Trident 3B | 1971 | 150 | 3 (2 pilots + flight engineer) | 3 | F3, C1 |
| `fairchild-metroliner` | Fairchild Swearingen Metro | 1972 | 19 | 2 (2 pilots) | 0 | F2, C0 |
| `tristar-1` | Lockheed L-1011 TriStar 1 | 1972 | 272 | 3 (2 pilots + flight engineer) | 6 | F3, C1 |
| `aerospatiale-bac-concorde` | Aerospatiale/BAC Concorde | 1973 | 100 | 3 (2 pilots + flight engineer) | 6 | F3, C2 - BEA: 3 flight crew and 6 cabin crew |
| `king-air-200` | Beechcraft King Air 200 | 1974 | 10 | 1 (1 pilot) | 0 | F1, C0 - light twin, single-pilot certificated |
| `tristar-200` | Lockheed L-1011 TriStar 200 | 1976 | 272 | 3 (2 pilots + flight engineer) | 6 | F3, C1 |
| `tristar-500` | Lockheed L-1011 TriStar 500 | 1979 | 241 | 3 (2 pilots + flight engineer) | 5 | F3, C1 |
| `dornier-do-228` | Dornier 228 | 1982 | 19 | 2 (2 pilots) | 0 | F2, C0 |
| `bae-146-100` | British Aerospace 146-100 | 1983 | 82 | 2 (2 pilots) | 2 | F2, C1 |
| `beechcraft-1900c` | Beechcraft 1900C | 1984 | 19 | 2 (2 pilots) | 0 | F2, C0 - airline operation; type is single-pilot certificated |
| `boeing-737-300` | Boeing 737-300 | 1984 | 126 | 2 (2 pilots) | 3 | F2, C1 |
| `atr-42-320` | ATR 42-320 | 1987 | 48 | 2 (2 pilots) | 1 | F2, C1 - TCDS minimum flight crew 2 |
| `fokker-f50` | Fokker 50 | 1987 | 50 | 2 (2 pilots) | 1 | F2, C1 |
| `airbus-a320` | Airbus A320 | 1988 | 150 | 2 (2 pilots) | 3 | F2, C1 |
| `boeing-737-400` | Boeing 737-400 | 1988 | 147 | 2 (2 pilots) | 3 | F2, C1 |
| `bae-146-300` | British Aerospace 146-300 | 1988 | 112 | 2 (2 pilots) | 3 | F2, C1 |
| `bae-atp` | British Aerospace ATP | 1988 | 64 | 2 (2 pilots) | 2 | F2, C1 |
| `atr-72-200` | ATR 72-200 | 1989 | 70 | 2 (2 pilots) | 2 | F2, C1 - TCDS minimum flight crew 2 |
| `boeing-747-400` | Boeing 747-400 | 1989 | 416 | 2 (2 pilots) | 9 | F6, C1 - flight engineer station deleted |
| `beechcraft-1900d` | Beechcraft 1900D | 1991 | 19 | 2 (2 pilots) | 0 | F2, C0 - airline operation; type is single-pilot certificated |
| `atr-42-500` | ATR 42-500 | 1994 | 48 | 2 (2 pilots) | 1 | F2, C1 - TCDS minimum flight crew 2 |
| `airbus-a321` | Airbus A321 | 1994 | 185 | 2 (2 pilots) | 4 | F2, C1 |
| `atr-72-500` | ATR 72-500 | 1997 | 70 | 2 (2 pilots) | 2 | F2, C1 - TCDS minimum flight crew 2 |
| `boeing-737-700` | Boeing 737-700 | 1997 | 128 | 2 (2 pilots) | 3 | F2, C1 |
| `erj-145` | Embraer ERJ-145 | 1997 | 50 | 2 (2 pilots) | 1 | F2, C1 |
| `boeing-737-800` | Boeing 737-800 | 1998 | 160 | 2 (2 pilots) | 4 | F2, C1 |
| `boeing-737-900er` | Boeing 737-900ER | 1998 | 177 | 2 (2 pilots) | 4 | F2, C1 - pakset year 1998 precedes the -900ER service entry in 2007 |
| `airbus-a319` | Airbus A319 | 1999 | 124 | 2 (2 pilots) | 3 | F2, C1 |
| `airbus-a318` | Airbus A318 | 2003 | 107 | 2 (2 pilots) | 3 | F2, C1 |
| `embraer-e-175` | Embraer E175 | 2004 | 78 | 2 (2 pilots) | 2 | F2, C1 |
| `embraer-e-190` | Embraer E190 | 2006 | 100 | 2 (2 pilots) | 2 | F2, C1 |
| `boeing-787-8` | Boeing 787-8 | 2011 | 214 | 2 (2 pilots) | 5 | F6, C1 |
| `boeing-747-8i` | Boeing 747-8i | 2012 | 364 | 2 (2 pilots) | 8 | F6, C1 |
| `boeing-787-9` | Boeing 787-9 | 2014 | 216 | 2 (2 pilots) | 5 | F6, C1 |
| `boeing-737-max-7` | Boeing 737 MAX 7 | 2017 | 138 | 2 (2 pilots) | 3 | F2, C1 |
| `boeing-737-max-8` | Boeing 737 MAX 8 | 2017 | 162 | 2 (2 pilots) | 4 | F2, C1 |
| `boeing-737-max-9` | Boeing 737 MAX 9 | 2017 | 178 | 2 (2 pilots) | 4 | F2, C1 |
| `boeing-787-10` | Boeing 787-10 | 2017 | 249 | 2 (2 pilots) | 5 | F6, C1 |


## Table 2: airframes with no passenger object

| Pakset object | Manufacturer and type | Year | Payload | Flight deck crew | Cabin crew | Basis |
|---|---|---:|---|---:|---:|---|
| `MailMonoPlane` | unidentified 1910 mail monoplane | 1910 | mail | 1 (1 pilot) | 0 | F1, C0 - estimate |
| `dhc3-otter` | de Havilland Canada DHC-3 Otter | 1953 | mail, 1,900 kg | 1 (1 pilot) | 0 | F1, C0 |
| `boeing-707-320c` | Boeing 707-320C | 1958 | mail, 17,800 kg | 4 (2 pilots + flight engineer + navigator) | 0 | F4, C0 - the pakset models this airframe as a mail carrier only |
| `atr-42-300f` | ATR 42-300F | 1985 | mail 4,800 kg; piece and cool 56 | 2 (2 pilots) | 0 | F2, C0 - three freight objects, no passenger counterpart |
