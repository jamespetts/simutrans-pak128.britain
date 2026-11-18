---
status: draft
verified: none
---
# Comfort register

**Covers**: every calibrated vehicle, its maximum comfortable and maximum tolerable journey
times in minutes, its intro and retire years, and a note on the calibration. Parent:
[comfort-calibration](../comfort-calibration.md). Generated from the `.dat` files and updated
when values change; the `.dat` files remain the authority.

How to read the note column: `line` means the tolerable time follows
`180 + 1.5 × comfortable` ([method](../comfort-calibration.md#the-line)); `line +5` or
`line −N` records a deviation; `open outfit: line − 30` is the motorcycle-outfit penalty
([private cars](private-cars.md#motorcycle-outfits)). The model-specific reasoning — era,
suspension, seating — is in each `.dat` header.

## Private cars

One row per model; every colourway of a model shares its values. `present` means the model is
still on the road in 2026 and its retire year is an estimate.

| Model | Comfortable | Tolerable | Intro | Retire | Note |
| --- | --- | --- | --- | --- | --- |
| AudiA4B6 | 150 | 405 | 2000 | 2029 | line |
| AustinLightTwelve | 45 | 250 | 1933 | 1950 | line |
| AustinMaestro | 70 | 285 | 1983 | 2002 | line |
| AustinMetro | 38 | 235 | 1980 | 2009 | line |
| AustinMetroMk2 | 50 | 255 | 1984 | 1998 | line |
| AustinMontego | 75 | 295 | 1984 | 1998 | line +5 |
| AustinPrincess | 80 | 300 | 1948 | 1969 | line |
| AustinSeven | 25 | 220 | 1922 | 1950 | line |
| AustinTen | 40 | 240 | 1932 | 1944 | line |
| AustinTen1937 | 45 | 250 | 1937 | 1953 | line |
| AustinTwelve | 50 | 255 | 1939 | 1957 | line |
| BMC1100 | 70 | 285 | 1962 | 1986 | line |
| BMCMini | 40 | 240 | 1965 | 2000 | low-end anchor (40/240) |
| BMW3E21 | 105 | 340 | 1975 | 1998 | line |
| BMW3E30 | 110 | 345 | 1982 | 2002 | line |
| BMW3E46 | 120 | 360 | 1998 | 2017 | line |
| BMW3E90 | 125 | 370 | 2005 | 2023 | line |
| BMW3G20 | 135 | 385 | 2019 | 2037 | line; present |
| BMW5E12 | 110 | 345 | 1972 | 1996 | line |
| BMW5E28 | 115 | 350 | 1981 | 2002 | line |
| BMW5E60 | 130 | 375 | 2003 | 2021 | line |
| BMW5G30 | 140 | 390 | 2017 | 2035 | line |
| BMW5G60 | 145 | 400 | 2023 | 2041 | line; present |
| BMW7E23 | 130 | 375 | 1977 | 2000 | line |
| BMW7G11 | 175 | 445 | 2015 | 2033 | line |
| BMW7G70 | 180 | 450 | 2022 | 2040 | line; highest in the register, present |
| BSA557Combo | 20 | 180 | 1921 | 1932 | open outfit: line -30 |
| BSAM21Combo | 25 | 190 | 1946 | 1966 | open outfit: line -30 |
| BSAM21MonacoCombo | 35 | 200 | 1960 | 1968 | open outfit: line -30 |
| BSASloperCombo | 25 | 190 | 1930 | 1939 | open outfit: line -30 |
| CitroenLight15 | 65 | 280 | 1938 | 1962 | line |
| CitroenTypeA | 25 | 220 | 1919 | 1925 | line |
| CitroenTypeB2 | 30 | 225 | 1921 | 1934 | line |
| CitroenTypeC | 18 | 205 | 1922 | 1933 | line |
| DaimlerWagonette | 15 | 205 | 1896 | 1918 | line +5 |
| FordAnglia100E | 45 | 250 | 1953 | 1967 | line |
| FordAnglia105E | 50 | 255 | 1959 | 1976 | line |
| FordCortina | 80 | 300 | 1962 | 1989 | line |
| FordEscort-mk1 | 55 | 265 | 1968 | 1989 | line +5 |
| FordEscort-mk2 | 60 | 270 | 1975 | 1990 | line |
| FordEscort-mk3 | 85 | 310 | 1981 | 1999 | line |
| FordEscort-mk4 | 100 | 330 | 1990 | 2018 | line |
| FordFiestaMk1 | 50 | 255 | 1977 | 1992 | line |
| FordFiestaMk2 | 55 | 265 | 1983 | 1999 | line +5 |
| FordFiestaMk3 | 65 | 280 | 1989 | 2004 | line |
| FordFiestaMk4 | 75 | 295 | 1995 | 2011 | line +5 |
| FordFiestaMk5 | 85 | 310 | 2002 | 2019 | line |
| FordFiestaMk6 | 100 | 330 | 2008 | 2026 | line |
| FordFiestaMk7 | 115 | 355 | 2017 | 2039 | line +5 |
| FordFocus | 125 | 370 | 1998 | present | line |
| FordGalaxyMk1 | 115 | 355 | 1995 | 2022 | line +5 |
| FordGalaxyMk3 | 135 | 385 | 2015 | present | line +5 |
| FordKa | 60 | 270 | 1996 | 2030 | line |
| FordModelA | 35 | 235 | 1927 | 1939 | line +5 |
| FordModelC | 40 | 240 | 1934 | 1956 | line |
| FordMondeoMk1 | 110 | 345 | 1993 | 2016 | line |
| FordMondeoMk4 | 135 | 385 | 2007 | present | line +5 |
| FordPrefectEarly | 40 | 240 | 1938 | 1966 | line |
| FordPrefectLate | 45 | 250 | 1953 | 1972 | line |
| FordT | 20 | 210 | 1908 | 1935 | line |
| HorseCarriageClosed | 30 | 225 | 1750 | 1911 | line |
| HorseCarriageOpen | 25 | 220 | 1750 | 1921 | line |
| HorseCart | 10 | 195 | 1750 | 1954 | line |
| Jaguar420 | 90 | 315 | 1966 | 1987 | line |
| JaguarSType | 90 | 315 | 1963 | 1985 | line |
| JaguarSTypeX200 | 110 | 345 | 1999 | 2024 | line |
| LandRoverSeries | 20 | 210 | 1948 | 1990 | line |
| LeylandPrincess | 85 | 310 | 1975 | 1989 | line |
| MorrisEight | 35 | 235 | 1935 | 1957 | line +5 |
| MorrisMarina | 55 | 265 | 1971 | 1988 | line +5 |
| MorrisMinor | 45 | 250 | 1948 | 1981 | line |
| MorrisMinor1928 | 28 | 220 | 1928 | 1942 | line |
| MorrisOxford2 | 60 | 270 | 1954 | 1960 | line |
| MorrisOxford3 | 60 | 270 | 1956 | 1959 | line |
| MorrisOxford4 | 70 | 285 | 1959 | 1977 | line |
| MorrisOxfordBullnose | 30 | 225 | 1913 | 1935 | line |
| MorrisOxfordFlatnose | 40 | 240 | 1926 | 1948 | line |
| MorrisOxfordMO | 55 | 265 | 1948 | 1963 | line +5 |
| NewMini | 100 | 330 | 2000 | present | line |
| NissanQashqai | 125 | 370 | 2006 | present | line |
| NortonBigFourCombo | 25 | 190 | 1940 | 1948 | open outfit: line -30 |
| park-drag-blue | 35 | 235 | 1832 | 1905 | line +5 |
| park-drag-green | 35 | 235 | 1837 | 1914 | line +5 |
| park-drag-yellow | 35 | 235 | 1830 | 1900 | line +5 |
| PeelP50 | 12 | 200 | 1962 | 1976 | line |
| RangeRover | 85 | 310 | 1970 | 1988 | line |
| ReliantRobin | 28 | 220 | 1973 | 1998 | line |
| Rover20 | 22 | 215 | 1907 | 1919 | line |
| Rover100 | 65 | 280 | 1994 | 2007 | line |
| Rover200R8 | 90 | 315 | 1989 | 2005 | line |
| Rover200R3 | 90 | 315 | 1995 | 2012 | line |
| Rover400R8 | 90 | 315 | 1990 | 2006 | line |
| Rover400HHR | 92 | 320 | 1995 | 2011 | line |
| Rover200SD3 | 85 | 310 | 1984 | 2000 | line |
| Rover75 | 105 | 340 | 1999 | 2015 | line |
| RoverMetro | 60 | 270 | 1990 | 2004 | line |
| Rover8 | 18 | 205 | 1904 | 1921 | line |
| Rover800 | 110 | 345 | 1986 | 2010 | line |
| Rover800R17 | 110 | 345 | 1991 | 2012 | line |
| Rover8-1919 | 30 | 225 | 1919 | 1933 | line |
| Rover9 | 32 | 230 | 1924 | 1939 | line |
| RoverSD1 | 95 | 325 | 1976 | 1991 | line +5 |
| StandardVanguard | 65 | 280 | 1947 | 1964 | line |
| StandardVanguardVignale | 70 | 285 | 1956 | 1970 | line |
| Triumph2000 | 85 | 310 | 1963 | 1987 | line |
| TriumphDolomite | 70 | 285 | 1972 | 1989 | line |
| TriumphHerald | 35 | 235 | 1959 | 1977 | line +5 |
| VauxhallCorsaB | 65 | 280 | 1993 | 2011 | line |
| VauxhallCorsaC | 80 | 300 | 2000 | 2018 | line |
| VauxhallCorsaD | 95 | 325 | 2006 | 2026 | line +5 |
| VauxhallCorsaE | 105 | 340 | 2015 | 2032 | line |
| VauxhallCorsaF | 115 | 355 | 2020 | 2039 | line +5 |
| VauxhallNova | 55 | 265 | 1983 | 2002 | line +5 |
| Volvo-240-Estate | 75 | 295 | 1974 | 1993 | line +5 |

## Player vehicles

Not yet populated. The method, the old 0–255 rating and the migration plan are in
[player vehicles](player-vehicles.md). The table will carry, per vehicle and accommodation
class: comfortable time, target tolerable time, intro, retire and the reason.

| Vehicle | Class | Comfortable | Tolerable (target) | Intro | Retire | Note |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | to be generated |

## Open questions

- Should the register be generated automatically from the `.dat` files at each review, or
  maintained by hand after the initial generation?
- Should player vehicles be listed per vehicle or per accommodation class? A Mk 1 coach with
  first and third class needs two rows.
