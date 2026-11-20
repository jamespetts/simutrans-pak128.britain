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
| AstonDB2 | 55 | 265 | 1950 | 1966 | line |
| AstonDBMkIII | 60 | 270 | 1957 | 1978 | line |
| AstonDB4 | 58 | 267 | 1958 | 1976 | line |
| AstonDBS | 65 | 280 | 1967 | 1986 | line |
| AstonDB5 | 60 | 270 | 1963 | 1981 | line |
| AstonDB6 | 65 | 280 | 1965 | 1983 | line |
| AstonV8Vantage | 68 | 282 | 1977 | 2002 | line |
| AstonVirage | 70 | 285 | 1989 | 2010 | line |
| AstonDB7 | 72 | 288 | 1994 | 2016 | line |
| AstonVanquish | 78 | 297 | 2001 | 2025 | line |
| AstonDB9 | 80 | 300 | 2004 | 2036 | line |
| AstonVantage2005 | 78 | 297 | 2005 | 2035 | line |
| AstonDBSV12 | 82 | 303 | 2007 | 2038 | line |
| AstonRapide | 88 | 312 | 2010 | 2039 | line |
| AstonDB11 | 90 | 315 | 2016 | 2045 | line |
| AstonVantage2018 | 88 | 312 | 2018 | 2046 | line |
| AstonDBX | 92 | 318 | 2020 | 2049 | line |
| Aston1HalfLitre | 25 | 218 | 1922 | 1943 | line |
| AstonInternational | 28 | 222 | 1929 | 1951 | line |
| AstonUlster | 30 | 225 | 1934 | 1955 | line |
| Aston2Litre | 32 | 228 | 1936 | 1958 | line |
| Aston15_98 | 35 | 232 | 1937 | 1959 | line |
| AudiA4B6 | 150 | 405 | 2000 | 2029 | line |
| AudiA6C4 | 85 | 307 | 1994 | 2020 | line |
| AudiA6C5 | 90 | 315 | 1997 | 2025 | line |
| AudiA6C6 | 92 | 318 | 2004 | 2031 | line |
| AudiA6C7 | 95 | 322 | 2011 | 2038 | line |
| AudiA6C8 | 98 | 327 | 2018 | 2045 | line |
| AudiA8D2 | 100 | 330 | 1994 | 2025 | line |
| AudiA8D4 | 105 | 337 | 2010 | 2037 | line |
| AudiA8D5 | 108 | 342 | 2017 | 2044 | line |
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
| BMWi3 | 75 | 292 | 2013 | 2041 | line |
| BMW1SeriesE87 | 75 | 292 | 2004 | 2029 | line |
| BMW1SeriesF20 | 80 | 300 | 2011 | 2037 | line |
| BMW1SeriesF40 | 85 | 307 | 2019 | 2045 | line |
| BMW1SeriesF70 | 88 | 312 | 2024 | 2049 | line |
| BMWX5E53 | 90 | 315 | 2000 | 2023 | line |
| BMWX5E70 | 95 | 322 | 2007 | 2030 | line |
| BMWX5F15 | 98 | 327 | 2013 | 2035 | line |
| BMWX5G05 | 100 | 330 | 2018 | 2041 | line |
| BMWiX3 | 100 | 330 | 2021 | 2044 | line |
| BSA557Combo | 20 | 180 | 1921 | 1932 | open outfit: line -30 |
| BSAM21Combo | 25 | 190 | 1946 | 1966 | open outfit: line -30 |
| BSAM21MonacoCombo | 35 | 200 | 1960 | 1968 | open outfit: line -30 |
| BSASloperCombo | 25 | 190 | 1930 | 1939 | open outfit: line -30 |
| CitroenCXSeries1 | 90 | 315 | 1975 | 1998 | line |
| CitroenCXSeries2 | 90 | 315 | 1986 | 2003 | line |
| CitroenDS1955 | 80 | 300 | 1955 | 1978 | line |
| CitroenDS1962 | 85 | 310 | 1962 | 1983 | line |
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
| FordPilot | 45 | 250 | 1947 | 1968 | line |
| FordConsulMk1 | 50 | 255 | 1951 | 1973 | line |
| FordConsulMk2 | 55 | 265 | 1956 | 1981 | line |
| FordConsulClassic | 55 | 265 | 1961 | 1981 | line |
| FordConsulCapri | 55 | 265 | 1962 | 1982 | line |
| FordZephyrMk1 | 55 | 265 | 1950 | 1973 | line |
| FordZodiacMk1 | 58 | 267 | 1953 | 1974 | line |
| FordZephyrMk2 | 58 | 267 | 1956 | 1981 | line |
| FordZodiacMk2 | 60 | 270 | 1956 | 1981 | line |
| FordZephyrMk3 | 62 | 273 | 1962 | 1985 | line |
| FordZodiacMk3 | 65 | 280 | 1962 | 1985 | line |
| FordZephyrMk4 | 65 | 280 | 1966 | 1991 | line |
| FordZodiacMk4 | 68 | 282 | 1966 | 1991 | line |
| FordGranadaMk3 | 90 | 315 | 1985 | 2013 | line |
| GWKCyclecar | 25 | 220 | 1911 | 1930 | line |
| HorseCarriageClosed | 30 | 225 | 1750 | 1911 | line |
| HorseCarriageOpen | 25 | 220 | 1750 | 1921 | line |
| HorseCart | 10 | 195 | 1750 | 1954 | line |
| Humberette | 30 | 225 | 1913 | 1933 | line |
| HillmanMinxPreWar | 45 | 250 | 1931 | 1956 | line |
| HillmanMinxMk1_8 | 50 | 255 | 1945 | 1973 | line |
| HillmanMinxSeries | 55 | 265 | 1956 | 1985 | line |
| HillmanMinxArrow | 60 | 270 | 1967 | 1988 | line |
| Jaguar420 | 90 | 315 | 1966 | 1987 | line |
| LandRoverDiscovery1 | 70 | 285 | 1989 | 2017 | line |
| LandRoverDiscovery2 | 75 | 292 | 1998 | 2023 | line |
| LandRoverDiscovery3 | 85 | 307 | 2004 | 2028 | line |
| LandRoverDiscovery4 | 90 | 315 | 2009 | 2034 | line |
| LandRoverDiscovery5 | 95 | 322 | 2017 | 2041 | line |
| JaguarXFX250 | 95 | 322 | 2008 | 2032 | line |
| JaguarXFX260 | 100 | 330 | 2015 | 2039 | line |
| LexusESXZ10 | 100 | 330 | 2019 | 2041 | line |
| JaguarSType | 90 | 315 | 1963 | 1985 | line |
| JaguarSTypeX200 | 110 | 345 | 1999 | 2024 | line |
| LandRoverSeries | 20 | 210 | 1948 | 1990 | line |
| KiaSportage1 | 70 | 285 | 1995 | 2017 | line |
| KiaSportage2 | 80 | 300 | 2005 | 2025 | line |
| KiaSportage3 | 85 | 307 | 2010 | 2031 | line |
| KiaSportage4 | 90 | 315 | 2016 | 2037 | line |
| KiaSportage5 | 95 | 322 | 2022 | 2045 | line |
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
| RoverP3 | 55 | 265 | 1948 | 1968 | line |
| RoverP460 | 60 | 270 | 1953 | 1978 | line |
| RoverP490 | 62 | 273 | 1953 | 1978 | line |
| RoverP495 | 65 | 280 | 1962 | 1983 | line |
| RoverP4100 | 65 | 280 | 1960 | 1981 | line |
| RoverP4105R | 65 | 280 | 1956 | 1977 | line |
| RoverP4110 | 68 | 282 | 1962 | 1983 | line |
| RoverP53Litre | 80 | 300 | 1958 | 1985 | line |
| RoverP5Coupe | 80 | 300 | 1962 | 1985 | line |
| RoverP5BCoupe | 120 | 360 | 1967 | 1989 | line |
| RoverP62200 | 110 | 345 | 1973 | 1993 | line |
| RoverP63500 | 115 | 352 | 1968 | 1991 | line |
| SingerTen | 35 | 235 | 1912 | 1932 | line |
| Standard95 | 35 | 235 | 1913 | 1932 | line |
| StandardVanguard | 65 | 280 | 1947 | 1964 | line |
| StandardVanguardVignale | 70 | 285 | 1956 | 1970 | line |
| ToyotaCorollaE100 | 80 | 300 | 1992 | 2008 | line |
| ToyotaCorollaE110 | 85 | 310 | 1997 | 2013 | line |
| ToyotaCorollaE120 | 95 | 325 | 2002 | 2018 | line |
| ToyotaPriusXW10 | 100 | 330 | 2000 | 2019 | line |
| ToyotaPriusXW20 | 105 | 340 | 2004 | 2019 | line |
| ToyotaPriusXW30 | 110 | 345 | 2009 | 2024 | line |
| ToyotaPriusXW50 | 115 | 355 | 2016 | 2031 | line |
| ToyotaPriusXW60 | 120 | 360 | 2024 | 2039 | line |
| ToyotaYarisXP10 | 65 | 280 | 1999 | 2014 | line |
| ToyotaYarisXP90 | 80 | 300 | 2006 | 2021 | line |
| ToyotaYarisXP210 | 105 | 340 | 2020 | 2035 | line |
| Renault15 | 50 | 255 | 1972 | 1991 | line |
| Renault17 | 55 | 265 | 1972 | 1992 | line |
| Renault19Phase1 | 70 | 285 | 1989 | 2004 | line |
| Renault19Phase2 | 70 | 285 | 1992 | 2008 | line |
| Renault21Phase1 | 75 | 295 | 1986 | 2003 | line |
| Renault21Phase2 | 75 | 295 | 1989 | 2007 | line |
| Renault25Phase1 | 90 | 315 | 1984 | 2001 | line |
| Renault25Phase2 | 90 | 315 | 1988 | 2005 | line |
| RenaultMeganeV | 115 | 355 | 2022 | 2039 | line |
| RenaultMeganeIV | 110 | 345 | 2016 | 2033 | line |
| RenaultMeganeIII | 100 | 330 | 2009 | 2027 | line |
| RenaultMeganeII | 90 | 315 | 2002 | 2021 | line |
| RenaultMeganeI | 80 | 300 | 1996 | 2015 | line |
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
| FiatPanda1 | 55 | 265 | 1981 | 2013 | line |
| FiatPanda2 | 60 | 270 | 2004 | 2023 | line |
| FiatPanda3 | 65 | 280 | 2012 | 2035 | line |
| VWUp | 65 | 280 | 2011 | 2037 | line |
| Wolseley8HPTonneau | 20 | 210 | 1902 | 1923 | line |
| WolseleyTen | 45 | 250 | 1939 | 1961 | line |
| Wolseley1460 | 55 | 265 | 1938 | 1961 | line |
| Wolseley1885 | 60 | 270 | 1938 | 1961 | line |
| Wolseley2160 | 55 | 265 | 1929 | 1953 | line |
| WolseleyHornet1930 | 45 | 250 | 1930 | 1953 | line |
| WolseleyHornetMini | 60 | 270 | 1961 | 1986 | line |
| WolseleyWasp | 45 | 250 | 1935 | 1956 | line |
| ToyotaAygoX | 65 | 280 | 2022 | 2045 | line |
| HyundaiI10Mk2 | 65 | 280 | 2014 | 2036 | line |
| HyundaiI10Mk3 | 70 | 285 | 2020 | 2043 | line |
| PorscheMacanElectric | 95 | 322 | 2024 | 2051 | line |
| TeslaModel3 | 90 | 315 | 2019 | 2045 | line |
| TeslaModelY | 95 | 322 | 2021 | 2047 | line |
| Jaecoo5 | 85 | 307 | 2025 | 2048 | line |
| Jaecoo7 | 90 | 315 | 2025 | 2048 | line |
| Jaecoo8 | 95 | 322 | 2026 | 2049 | line |
| Norton16HCombo | 25 | 190 | 1937 | 1958 | open outfit: line -30 |
| BSAM20Combo | 25 | 190 | 1939 | 1958 | open outfit: line -30 |
| TeslaModelS | 105 | 340 | 2016 | 2036 | line |
| NissanMicraK10 | 50 | 255 | 1983 | 2003 | line |
| NissanMicraK12 | 60 | 270 | 2003 | 2023 | line |
| NissanMicraK13 | 65 | 280 | 2010 | 2033 | line |
| DatsunCherryF10 | 40 | 240 | 1977 | 1994 | line |
| Datsun1200 | 40 | 240 | 1971 | 1990 | line |
| Datsun120Y | 40 | 240 | 1973 | 1992 | line |
| NissanSunnyN14 | 70 | 285 | 1991 | 2013 | line |
| NissanMicraK14 | 70 | 285 | 2017 | 2042 | line |
| NissanMicraK15 | 80 | 300 | 2025 | 2048 | line |
| FiatGrandePandaElectric | 75 | 292 | 2026 | 2049 | line |
| NissanSunnyB11 | 45 | 248 | 1982 | 1999 | line |
| FordGalaxyMk2 | 80 | 300 | 2006 | 2032 | line |
| BYDDolphin | 70 | 285 | 2023 | 2048 | line |
| BYDAtto3 | 80 | 300 | 2023 | 2049 | line |
| BYDSeal | 90 | 315 | 2023 | 2049 | line |
| BYDSealion7 | 95 | 322 | 2025 | 2051 | line |
| VauxhallLightSix | 30 | 225 | 1933 | 1956 | line |
| Vauxhall146 | 30 | 225 | 1939 | 1960 | line |
| VauxhallBigSix | 40 | 240 | 1934 | 1955 | line |
| VauxhallCadet | 25 | 218 | 1930 | 1950 | line |
| VauxhallAType | 20 | 210 | 1908 | 1932 | line |
| VauxhallBType | 22 | 213 | 1910 | 1932 | line |
| VauxhallCType | 25 | 218 | 1910 | 1932 | line |
| Vauxhall1440 | 30 | 225 | 1922 | 1942 | line |
| VauxhallTen | 25 | 218 | 1937 | 1958 | line |
| Vauxhall2060 | 30 | 225 | 1927 | 1950 | line |
| VauxhallWyvernVeloxL | 35 | 232 | 1948 | 1966 | line |
| VauxhallWyvernVeloxCrestaE | 40 | 240 | 1951 | 1970 | line |
| VauxhallVeloxCrestaPA | 50 | 255 | 1958 | 1976 | line |
| VauxhallVeloxCrestaPB | 55 | 262 | 1962 | 1979 | line |
| VauxhallCrestaPC | 65 | 280 | 1965 | 1982 | line |
| VauxhallZafiraA | 70 | 285 | 1999 | 2012 | line |
| VauxhallZafiraB | 75 | 292 | 2005 | 2017 | line |
| VauxhallZafiraC | 80 | 300 | 2012 | 2021 | line |
| VauxhallMokkaA | 70 | 285 | 2012 | 2019 | line |
| VauxhallMokkaX | 72 | 288 | 2016 | 2021 | line |
| VauxhallMokkaB | 80 | 300 | 2021 | 2043 | line |
| BentleyContinentalGT2 | 155 | 412 | 2011 | 2029 | line |
| BentleyContinentalGT3 | 160 | 420 | 2018 | 2035 | line |
| BentleyContinentalGT4 | 165 | 428 | 2024 | 2046 | line |
| VauxhallCarltonMk1 | 65 | 280 | 1978 | 1997 | line |
| VauxhallCarltonMk2 | 75 | 292 | 1986 | 2003 | line |
| VauxhallVectraB | 75 | 292 | 1995 | 2011 | line |
| VauxhallVectraC | 80 | 300 | 2002 | 2017 | line |
| VauxhallVivaHB | 50 | 255 | 1966 | 1982 | line |
| VauxhallVivaHC | 50 | 255 | 1970 | 1989 | line |
| VauxhallViva2015 | 60 | 270 | 2015 | 2030 | line |
| FordPuma1997 | 65 | 280 | 1997 | 2016 | line |
| FordPuma2019 | 75 | 292 | 2019 | 2043 | line |
| AustinAllegro | 50 | 255 | 1973 | 1995 | line |

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
