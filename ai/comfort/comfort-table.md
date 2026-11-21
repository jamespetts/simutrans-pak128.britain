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
`330 + 1.5 × comfortable` for motor cars, capped at 600
([method](../comfort-calibration.md#the-line)); `horse-drawn carriage` means
`240 + 4 × comfortable`, capped at 600, and `horse-drawn cart` means
`180 + 6 × comfortable`, capped at 300; `open outfit: line − 30` is the motorcycle-outfit
penalty ([private cars](private-cars.md#motorcycle-outfits)). The model-specific reasoning —
era, suspension, seating — is in each `.dat` header.

## Private cars

`Obj=citycar` models, one row per model; each colourway has its own `class=` list, but every
colourway of a model shares both comfort values. The **Class** column is the union of the
colourway lists. Generated from the `.dat` files on 2026-11-20 (436 models, 1,767 objects).
The `.dat` files remain the authority. **Model** is the internal model stem, which usually
carries the generation where the English display name does not (the five Fiesta generations all
display as "Ford Fiesta", but are `FordFiestaMk1` to `FordFiestaMk7` here). The row `park-drag`
groups the three colour objects `park-drag-yellow`, `park-drag-blue` and `park-drag-green`, whose
colour is part of the object name rather than a suffix.

- **Class** is the passenger wealth class list: 0 Very low, 1 Low, 2 Medium, 3 High,
  4 Very high. The calibration rule is in [citycar-wealth-classes](../objects/citycar-wealth-classes.md).
- **Comfortable / Tolerable** are `maximum_comfortable_journey_minutes` and
  `maximum_tolerable_journey_minutes`. The motor-car line is `tolerable = 330 + 1.5 x comfortable`,
  capped at 600; horse-drawn passenger carriages use `240 + 4 x comfortable`, capped at 600, and
  working carts use `180 + 6 x comfortable`, capped at 300. The note records `line`,
  `open outfit: line -30`, `horse-drawn carriage` or `horse-drawn cart`.
- **Intro** is the first month any colourway appears; **Retire** is the last month any
  colourway is still regular on the roads. These are road-presence dates, not production
  dates: a model withdrawn from sale may remain in the table for a decade or more. Retire dates
  later than 2026 are estimates, not observations. `present` means no retire date is set; since
  the 2026-11-20 pass this includes models still in production in 2026 with no announced end.
- **Colours** is the number of colourway objects for the model.

Summary: 436 models — 425 cars, 7 motorcycle outfits, 4 horse-drawn. Class lists: 75 at `0,1`, 40 at `0,1,2`, 11 at `1`, 96 at `1,2`, 21 at `1,2,3`, 25 at `2`, 70 at `2,3`, 26 at `2,3,4`, 16 at `3`, 44 at `3,4`, 12 at `4`. Comfort values run from 10 to 180 comfortable and 240 to 600 tolerable.

**Class** lists are derived from the union of the new-price band and the five-year-old price
band, with a per-model running-cost floor on the lower bound. 407 of the 425 cars now have a
verified launch price; the 18 remaining fallbacks are listed in
[citycar-wealth-classes](../objects/citycar-wealth-classes.md). A model can therefore have one,
two or three bands; the calculation, thresholds, price verification, running-cost index and
retained-value evidence are in that doc. The `.dat` files remain the authority.

The retire dates follow the 2026-11-20 policy: models still in production in 2026 with no
announced end have their retire fields commented out and show `present`; out-of-production
models carry road-tail estimates, staggered by colourway. Where a model's date is still a
future estimate, that is because the shape is out of production but the road tail has not yet
run out.

| Model | Type | Class | Comfortable | Tolerable | Intro | Retire | Colours | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HorseCarriageClosed | Horse-drawn | 3,4 | 60 | 480 | 1750-01 | 1911-06 | 4 | horse-drawn carriage |
| HorseCarriageOpen | Horse-drawn | 3,4 | 30 | 360 | 1750-01 | 1921-06 | 7 | horse-drawn carriage |
| HorseCart | Horse-drawn | 0,1 | 10 | 240 | 1750-01 | 1954-05 | 3 | horse-drawn cart |
| park-drag | Horse-drawn | 3,4 | 40 | 400 | 1830-04 | 1914-09 | 3 | horse-drawn carriage |
| DaimlerWagonette | Car | 2,3,4 | 15 | 353 | 1896-05 | 1918-11 | 3 | line |
| Wolseley8HPTonneau | Car | 2,3 | 20 | 360 | 1902-01 | 1923-06 | 4 | line |
| DeDionTypeV | Car | 2,3 | 25 | 368 | 1902-05 | 1928-06 | 4 | line |
| Star7hp | Car | 2 | 25 | 368 | 1902-05 | 1925-06 | 4 | line |
| MercedesSimplex60 | Car | 4 | 55 | 413 | 1903-06 | 1932-06 | 4 | line |
| Rover8 | Car | 2,3 | 18 | 357 | 1904-08 | 1921-04 | 3 | line |
| PeugeotType69Bebe | Car | 2 | 25 | 368 | 1905-06 | 1932-06 | 4 | line |
| RollsRoyceSilverGhost | Car | 4 | 60 | 420 | 1907-07 | 1938-06 | 4 | line |
| Rover20 | Car | 2,3,4 | 22 | 363 | 1907-08 | 1919-10 | 3 | line |
| FordT | Car | 2 | 20 | 360 | 1908-10 | 1935-11 | 1 | line |
| VauxhallAType | Car | 2,3 | 20 | 360 | 1908-10 | 1932-06 | 4 | line |
| VauxhallBType | Car | 2,3 | 22 | 363 | 1910-01 | 1932-06 | 4 | line |
| Wolseley1620 | Car | 2,3,4 | 60 | 420 | 1910-01 | 1940-06 | 4 | line |
| VauxhallCType | Car | 2,3 | 25 | 368 | 1910-04 | 1932-06 | 4 | line |
| GWKCyclecar | Car | 2 | 25 | 368 | 1911-01 | 1930-06 | 4 | line |
| RoverTwelve | Car | 2,3 | 60 | 420 | 1912-01 | 1949-06 | 4 | line |
| Sunbeam1216 | Car | 2,3 | 60 | 420 | 1912-01 | 1946-06 | 4 | line |
| Argyll1530 | Car | 2,3 | 60 | 420 | 1912-04 | 1935-06 | 4 | line |
| SingerTen | Car | 2 | 35 | 383 | 1912-11 | 1932-06 | 4 | line |
| Humberette | Car | 2 | 30 | 375 | 1913-01 | 1933-06 | 4 | line |
| Standard95 | Car | 2 | 35 | 383 | 1913-01 | 1932-06 | 4 | line |
| DaimlerTE30 | Car | 2,3,4 | 65 | 428 | 1913-03 | 1938-06 | 4 | line |
| Vauxhall3098 | Car | 2,3,4 | 65 | 428 | 1913-06 | 1948-06 | 4 | line |
| MorrisOxfordBullnose | Car | 2,3 | 30 | 375 | 1913-07 | 1935-03 | 4 | line |
| CitroenTypeA | Car | 2,3,4 | 25 | 368 | 1919-02 | 1925-05 | 3 | line |
| Rover8-1919 | Car | 2,3 | 30 | 375 | 1919-08 | 1933-03 | 5 | line |
| BSA557Combo | Outfit | 0,1 | 20 | 330 | 1921-01 | 1932-06 | 2 | open outfit: line -30 |
| CitroenTypeB2 | Car | 2,3 | 30 | 375 | 1921-06 | 1934-01 | 3 | line |
| Aston1HalfLitre | Car | 2,3,4 | 25 | 368 | 1922-01 | 1943-06 | 4 | line |
| AustinSeven | Car | 1,2 | 25 | 368 | 1922-01 | 1950-01 | 5 | line |
| Vauxhall1440 | Car | 2,3,4 | 30 | 375 | 1922-01 | 1942-06 | 4 | line |
| CitroenTypeC | Car | 2,3 | 18 | 357 | 1922-04 | 1933-05 | 4 | line |
| Rover9 | Car | 2,3 | 32 | 378 | 1924-08 | 1939-02 | 5 | line |
| MorrisOxfordFlatnose | Car | 2,3 | 40 | 390 | 1926-08 | 1948-06 | 3 | line |
| FordModelA | Car | 2 | 35 | 383 | 1927-03 | 1939-01 | 4 | line |
| Vauxhall2060 | Car | 2,3,4 | 30 | 375 | 1927-10 | 1950-06 | 4 | line |
| MorrisMinor1928 | Car | 2 | 28 | 372 | 1928-08 | 1942-04 | 4 | line |
| AstonInternational | Car | 2,3,4 | 28 | 372 | 1929-01 | 1951-06 | 4 | line |
| RollsRoyce2025 | Car | 4 | 72 | 438 | 1929-01 | 1948-06 | 4 | line |
| Wolseley2160 | Car | 2,3,4 | 55 | 413 | 1929-01 | 1953-06 | 4 | line |
| RollsRoycePhantomII | Car | 4 | 75 | 443 | 1929-09 | 1955-06 | 4 | line |
| BSASloperCombo | Outfit | 0,1 | 25 | 338 | 1930-01 | 1939-06 | 2 | open outfit: line -30 |
| WolseleyHornet1930 | Car | 2,3 | 45 | 398 | 1930-01 | 1953-06 | 4 | line |
| VauxhallCadet | Car | 2,3 | 25 | 368 | 1930-10 | 1950-06 | 4 | line |
| HillmanMinxPreWar | Car | 1,2 | 45 | 398 | 1931-01 | 1956-06 | 4 | line |
| AustinTen | Car | 2 | 40 | 390 | 1932-04 | 1944-04 | 4 | line |
| FordModelY | Car | 1 | 25 | 368 | 1932-04 | 1955-06 | 4 | line |
| DaimlerFifteen | Car | 2,3,4 | 75 | 443 | 1932-08 | 1962-06 | 4 | line |
| AustinLightTwelve | Car | 2,3 | 45 | 398 | 1933-08 | 1950-06 | 4 | line |
| DerbyBentley | Car | 4 | 78 | 447 | 1933-09 | 1950-06 | 4 | line |
| VauxhallLightSix | Car | 1,2 | 30 | 375 | 1933-10 | 1956-06 | 4 | line |
| AstonUlster | Car | 2,3,4 | 30 | 375 | 1934-01 | 1955-06 | 4 | line |
| VauxhallBigSix | Car | 2,3 | 40 | 390 | 1934-01 | 1955-06 | 4 | line |
| FordModelC | Car | 1,2 | 40 | 390 | 1934-08 | 1956-02 | 4 | line |
| Rover12P2 | Car | 2,3 | 60 | 420 | 1934-10 | 1965-06 | 4 | line |
| Rover14P2 | Car | 2,3,4 | 65 | 428 | 1934-10 | 1965-06 | 4 | line |
| WolseleyWasp | Car | 2,3 | 45 | 398 | 1935-01 | 1956-06 | 4 | line |
| MorrisEight | Car | 1,2 | 35 | 383 | 1935-08 | 1957-01 | 4 | line |
| Aston2Litre | Car | 2,3,4 | 32 | 378 | 1936-01 | 1958-06 | 4 | line |
| RollsRoyce2530 | Car | 4 | 80 | 450 | 1936-04 | 1960-06 | 4 | line |
| Aston15_98 | Car | 2,3,4 | 35 | 383 | 1937-01 | 1959-06 | 4 | line |
| Norton16HCombo | Outfit | 0,1 | 25 | 338 | 1937-01 | 1958-06 | 1 | open outfit: line -30 |
| AustinTen1937 | Car | 1,2 | 45 | 398 | 1937-08 | 1953-03 | 5 | line |
| VauxhallTen | Car | 1,2 | 25 | 368 | 1937-11 | 1958-06 | 4 | line |
| CitroenLight15 | Car | 2,3 | 65 | 428 | 1938-03 | 1962-02 | 4 | line |
| FordPrefectEarly | Car | 1,2 | 40 | 390 | 1938-08 | 1966-07 | 4 | line |
| Wolseley1460 | Car | 1,2 | 55 | 413 | 1938-09 | 1961-06 | 4 | line |
| Wolseley1885 | Car | 2,3 | 60 | 420 | 1938-09 | 1961-06 | 4 | line |
| BSAM20Combo | Outfit | 0,1 | 25 | 338 | 1939-01 | 1958-06 | 1 | open outfit: line -30 |
| Vauxhall146 | Car | 1,2 | 30 | 375 | 1939-01 | 1960-06 | 4 | line |
| WolseleyTen | Car | 1,2 | 45 | 398 | 1939-01 | 1961-06 | 4 | line |
| AustinTwelve | Car | 1,2 | 50 | 405 | 1939-08 | 1957-07 | 4 | line |
| NortonBigFourCombo | Outfit | 0,1 | 25 | 338 | 1940-01 | 1948-06 | 1 | open outfit: line -30 |
| HillmanMinxMk1_8 | Car | 2,3 | 50 | 405 | 1945-01 | 1973-06 | 4 | line |
| BSAM21Combo | Outfit | 0,1 | 25 | 338 | 1946-01 | 1966-06 | 3 | open outfit: line -30 |
| BentleyMkVI | Car | 3,4 | 82 | 453 | 1946-06 | 1965-06 | 4 | line |
| StandardVanguard | Car | 2,3 | 65 | 428 | 1947-03 | 1964-10 | 5 | line |
| FordPilot | Car | 2,3 | 45 | 398 | 1947-08 | 1968-06 | 4 | line |
| RoverP3 | Car | 2,3,4 | 55 | 413 | 1948-02 | 1968-06 | 4 | line |
| LandRoverSeries | Car | 2 | 20 | 360 | 1948-06 | 1990-04 | 4 | line |
| MorrisMinor | Car | 2 | 45 | 398 | 1948-08 | 1981-01 | 5 | line |
| MorrisOxfordMO | Car | 2,3 | 55 | 413 | 1948-08 | 1963-09 | 4 | line |
| AustinPrincess | Car | 3,4 | 80 | 450 | 1948-09 | 1969-01 | 3 | line |
| Citroen2CV | Car | 1,2 | 45 | 398 | 1948-10 | 2000-06 | 4 | line |
| VauxhallWyvernVeloxL | Car | 2,3 | 35 | 383 | 1948-10 | 1966-06 | 4 | line |
| Wolseley680 | Car | 2,3 | 100 | 480 | 1948-10 | 1962-06 | 4 | line |
| RoverP475 | Car | 2,3,4 | 105 | 488 | 1949-09 | 1964-06 | 4 | line |
| VWBeetle | Car | 1,2,3 | 45 | 398 | 1950-01 | 1985-06 | 4 | line |
| AstonDB2 | Car | 4 | 55 | 413 | 1950-05 | 1966-06 | 4 | line |
| FordZephyrMk1 | Car | 2,3 | 55 | 413 | 1950-10 | 1973-06 | 4 | line |
| FordConsulMk1 | Car | 2 | 50 | 405 | 1951-01 | 1973-06 | 4 | line |
| AustinA30 | Car | 2 | 40 | 390 | 1951-10 | 1978-06 | 4 | line |
| VauxhallWyvernVeloxCrestaE | Car | 2,3 | 40 | 390 | 1951-10 | 1970-06 | 4 | line |
| BentleyRType | Car | 3,4 | 85 | 458 | 1952-09 | 1978-06 | 4 | line |
| FordPopular103E | Car | 1,2 | 35 | 383 | 1953-03 | 1972-06 | 4 | line |
| FordPrefectLate | Car | 2 | 45 | 398 | 1953-08 | 1972-12 | 5 | line |
| FordZodiacMk1 | Car | 2,3 | 58 | 417 | 1953-09 | 1974-06 | 3 | line |
| RoverP460 | Car | 2,3 | 60 | 420 | 1953-09 | 1978-06 | 4 | line |
| RoverP490 | Car | 2,3 | 62 | 423 | 1953-09 | 1978-06 | 4 | line |
| FordAnglia100E | Car | 2 | 45 | 398 | 1953-10 | 1967-06 | 5 | line |
| HumberHawkVI | Car | 2,3 | 100 | 480 | 1954-07 | 1967-06 | 4 | line |
| MorrisOxford2 | Car | 2,3 | 60 | 420 | 1954-08 | 1960-09 | 3 | line |
| RollsRoyceSilverCloudI | Car | 3,4 | 85 | 458 | 1955-04 | 1980-06 | 4 | line |
| BentleyS1 | Car | 3,4 | 85 | 458 | 1955-06 | 1980-06 | 4 | line |
| CitroenDS1955 | Car | 3 | 80 | 450 | 1955-10 | 1978-06 | 4 | line |
| HillmanMinxSeries | Car | 2 | 55 | 413 | 1956-01 | 1985-06 | 4 | line |
| FordConsulMk2 | Car | 2 | 55 | 413 | 1956-04 | 1981-06 | 4 | line |
| FordZephyrMk2 | Car | 2,3 | 58 | 417 | 1956-04 | 1981-06 | 4 | line |
| FordZodiacMk2 | Car | 2,3 | 60 | 420 | 1956-04 | 1981-06 | 4 | line |
| StandardVanguardVignale | Car | 2,3 | 70 | 435 | 1956-08 | 1970-03 | 3 | line |
| MorrisOxford3 | Car | 2,3 | 60 | 420 | 1956-10 | 1959-07 | 4 | line |
| RoverP4105R | Car | 2,3,4 | 65 | 428 | 1956-10 | 1977-06 | 4 | line |
| AstonDBMkIII | Car | 4 | 60 | 420 | 1957-01 | 1978-06 | 4 | line |
| AstonDB4 | Car | 4 | 58 | 417 | 1958-01 | 1976-06 | 4 | line |
| VauxhallVeloxCrestaPA | Car | 2,3 | 50 | 405 | 1958-01 | 1976-06 | 4 | line |
| RoverP53Litre | Car | 3 | 80 | 450 | 1958-09 | 1985-06 | 4 | line |
| MorrisOxford4 | Car | 2 | 70 | 435 | 1959-08 | 1977-07 | 4 | line |
| TriumphHerald | Car | 2 | 35 | 383 | 1959-08 | 1977-09 | 5 | line |
| FordAnglia105E | Car | 1,2 | 50 | 405 | 1959-09 | 1976-12 | 5 | line |
| RollsRoyceSilverCloudII | Car | 3,4 | 90 | 465 | 1959-09 | 1985-06 | 4 | line |
| JaguarMk2 | Car | 2,3 | 115 | 503 | 1959-10 | 1980-06 | 4 | line |
| BSAM21MonacoCombo | Outfit | 0,1 | 35 | 353 | 1960-01 | 1968-06 | 2 | open outfit: line -30 |
| RoverP4100 | Car | 2,3,4 | 65 | 428 | 1960-10 | 1981-06 | 4 | line |
| FordConsulClassic | Car | 1,2,3 | 55 | 413 | 1961-05 | 1981-06 | 4 | line |
| WolseleyHornetMini | Car | 1,2 | 60 | 420 | 1961-10 | 1986-06 | 4 | line |
| FordConsulCapri | Car | 1,2,3 | 55 | 413 | 1962-01 | 1982-06 | 4 | line |
| FordZephyrMk3 | Car | 1,2,3 | 62 | 423 | 1962-04 | 1985-06 | 4 | line |
| FordZodiacMk3 | Car | 1,2,3 | 65 | 428 | 1962-04 | 1985-06 | 4 | line |
| BMC1100 | Car | 1,2 | 70 | 435 | 1962-08 | 1986-06 | 5 | line |
| FordCortina | Car | 1,2 | 80 | 450 | 1962-08 | 1989-05 | 6 | line |
| PeelP50 | Car | 0,1 | 12 | 348 | 1962-08 | 1976-04 | 2 | line |
| CitroenDS1962 | Car | 2,3,4 | 85 | 458 | 1962-09 | 1983-06 | 4 | line |
| RoverP4110 | Car | 2,3 | 68 | 432 | 1962-09 | 1983-06 | 4 | line |
| RoverP495 | Car | 2,3 | 65 | 428 | 1962-09 | 1983-06 | 4 | line |
| RoverP5Coupe | Car | 2,3,4 | 80 | 450 | 1962-10 | 1985-06 | 4 | line |
| VauxhallVeloxCrestaPB | Car | 1,2,3 | 55 | 413 | 1962-10 | 1979-06 | 4 | line |
| AstonDB5 | Car | 3,4 | 60 | 420 | 1963-01 | 1981-06 | 4 | line |
| HillmanImp | Car | 1,2 | 55 | 413 | 1963-05 | 1986-06 | 4 | line |
| Triumph2000 | Car | 1,2,3 | 85 | 458 | 1963-08 | 1987-05 | 5 | line |
| VauxhallVivaHA | Car | 1,2 | 55 | 413 | 1963-09 | 1980-06 | 4 | line |
| JaguarSType | Car | 2,3,4 | 90 | 465 | 1963-10 | 1985-06 | 4 | line |
| RoverP6 | Car | 2,3 | 110 | 495 | 1963-10 | 1988-06 | 4 | line |
| AstonDB6 | Car | 3,4 | 65 | 428 | 1965-01 | 1983-06 | 4 | line |
| BMCMini | Car | 0,1 | 40 | 390 | 1965-01 | 2000-12 | 6 | line |
| RollsRoyceSilverShadow | Car | 3,4 | 150 | 555 | 1965-10 | 1995-06 | 4 | line |
| VauxhallCrestaPC | Car | 1,2,3 | 65 | 428 | 1965-10 | 1982-06 | 4 | line |
| FordZephyrMk4 | Car | 1,2 | 65 | 428 | 1966-04 | 1991-06 | 4 | line |
| FordZodiacMk4 | Car | 1,2,3 | 68 | 432 | 1966-04 | 1991-06 | 4 | line |
| Jaguar420 | Car | 1,2,3 | 90 | 465 | 1966-08 | 1987-06 | 4 | line |
| VauxhallVivaHB | Car | 1,2 | 50 | 405 | 1966-09 | 1982-06 | 4 | line |
| HillmanMinxArrow | Car | 1,2 | 60 | 420 | 1967-01 | 1988-06 | 4 | line |
| RoverP5B | Car | 2,3 | 120 | 510 | 1967-09 | 1986-06 | 4 | line |
| RoverP5BCoupe | Car | 2,3 | 120 | 510 | 1967-09 | 1989-06 | 4 | line |
| AstonDBS | Car | 3,4 | 65 | 428 | 1967-10 | 1986-06 | 4 | line |
| RoverP63500 | Car | 2,3 | 115 | 503 | 1968-04 | 1991-06 | 4 | line |
| FordEscort-mk1 | Car | 0,1,2 | 55 | 413 | 1968-08 | 1989-07 | 5 | line |
| JaguarXJ6Series1 | Car | 2,3 | 130 | 525 | 1968-09 | 1997-06 | 4 | line |
| Triumph2000Mk2 | Car | 1,2,3 | 85 | 458 | 1969-10 | 1989-06 | 4 | line |
| Triumph2500 | Car | 1,2,3 | 88 | 462 | 1969-10 | 1989-06 | 4 | line |
| VauxhallVivaHC | Car | 0,1,2 | 50 | 405 | 1970-01 | 1989-06 | 4 | line |
| TriumphStag | Car | 1,2,3 | 100 | 480 | 1970-06 | 1993-06 | 4 | line |
| Triumph1500 | Car | 1,2 | 70 | 435 | 1970-10 | 1988-06 | 4 | line |
| RangeRover | Car | 2,3 | 85 | 458 | 1970-11 | 2005-06 | 5 | line |
| Datsun100A | Car | 0,1 | 50 | 405 | 1971-01 | 1987-06 | 4 | line |
| Datsun1200 | Car | 0,1,2 | 40 | 390 | 1971-01 | 1990-06 | 4 | line |
| MorrisMarina | Car | 0,1,2 | 55 | 413 | 1971-08 | 1988-11 | 5 | line |
| Renault15 | Car | 0,1,2 | 50 | 405 | 1972-01 | 1991-06 | 4 | line |
| Renault17 | Car | 0,1,2 | 55 | 413 | 1972-01 | 1992-06 | 4 | line |
| FordGranadaMk1 | Car | 1,2 | 105 | 488 | 1972-03 | 1989-06 | 4 | line |
| BMW5E12 | Car | 2,3 | 110 | 495 | 1972-07 | 1996-06 | 4 | line |
| TriumphDolomite | Car | 0,1,2 | 70 | 435 | 1972-08 | 1989-09 | 7 | line |
| Fiat126 | Car | 0,1 | 35 | 383 | 1972-10 | 2008-06 | 4 | line |
| MercedesW116 | Car | 3,4 | 95 | 473 | 1972-10 | 2000-06 | 4 | line |
| ReliantRobin | Car | 0,1 | 28 | 372 | 1973-01 | 1998-12 | 4 | line |
| AustinAllegro | Car | 0,1 | 50 | 405 | 1973-05 | 1995-06 | 4 | line |
| Datsun120Y | Car | 0,1,2 | 40 | 390 | 1973-10 | 1992-06 | 4 | line |
| RoverP62200 | Car | 2,3 | 110 | 495 | 1973-10 | 1993-06 | 4 | line |
| VWGolfMk1 | Car | 0,1 | 90 | 465 | 1974-05 | 1994-06 | 4 | line |
| Volvo-240-Estate | Car | 1,2 | 75 | 443 | 1974-08 | 1993-12 | 4 | line |
| TriumphSpitfire1500 | Car | 1,2 | 50 | 405 | 1974-10 | 1998-06 | 4 | line |
| FordEscort-mk2 | Car | 0,1,2 | 60 | 420 | 1975-01 | 1990-06 | 5 | line |
| LeylandPrincess | Car | 0,1,2 | 85 | 458 | 1975-03 | 1989-02 | 7 | line |
| CitroenCXSeries1 | Car | 2,3 | 90 | 465 | 1975-05 | 1998-06 | 4 | line |
| BMW3E21 | Car | 1,2 | 105 | 488 | 1975-06 | 1998-06 | 4 | line |
| VauxhallCavalierMk1 | Car | 0,1,2 | 85 | 458 | 1975-09 | 1990-06 | 4 | line |
| VauxhallChevette | Car | 0,1,2 | 65 | 428 | 1975-09 | 1995-06 | 4 | line |
| Mercedes230EW123 | Car | 2,3 | 110 | 495 | 1976-01 | 1998-06 | 4 | line |
| RoverSD1 | Car | 1,2,3 | 95 | 473 | 1976-06 | 1991-07 | 8 | line |
| SkodaEstelle | Car | 0,1,2 | 45 | 398 | 1976-10 | 1998-06 | 4 | line |
| DatsunCherryF10 | Car | 0,1 | 40 | 390 | 1977-01 | 1994-06 | 4 | line |
| FordFiestaMk1 | Car | 0,1 | 50 | 405 | 1977-01 | 1992-12 | 4 | line |
| AstonV8Vantage | Car | 3,4 | 68 | 432 | 1977-02 | 2002-06 | 4 | line |
| BMW7E23 | Car | 3,4 | 130 | 525 | 1977-05 | 2000-06 | 4 | line |
| FordGranadaMk2 | Car | 1,2,3 | 110 | 495 | 1977-09 | 1995-06 | 4 | line |
| DatsunSunnyB310 | Car | 1,2 | 55 | 413 | 1978-01 | 1997-06 | 4 | line |
| DatsunCherryN10 | Car | 1,2 | 55 | 413 | 1978-09 | 1997-06 | 4 | line |
| VauxhallCarltonMk1 | Car | 1,2 | 65 | 428 | 1978-09 | 1997-06 | 4 | line |
| LadaRiva | Car | 0,1,2 | 50 | 405 | 1979-09 | 2016-06 | 4 | line |
| MercedesSClassW126 | Car | 3,4 | 140 | 540 | 1979-09 | 2005-06 | 4 | line |
| AustinMetro | Car | 0,1,2 | 38 | 387 | 1980-01 | 2009-12 | 7 | line |
| DatsunBluebird910 | Car | 0,1,2 | 65 | 428 | 1980-01 | 1999-06 | 4 | line |
| VauxhallAstraMk1 | Car | 0,1,2 | 95 | 473 | 1980-03 | 1994-06 | 4 | line |
| RollsRoyceSilverSpirit | Car | 3,4 | 150 | 555 | 1980-10 | 2012-06 | 4 | line |
| Yugo45 | Car | 0,1,2 | 45 | 398 | 1980-10 | 2014-06 | 4 | line |
| FiatPanda1 | Car | 0,1 | 55 | 413 | 1981-05 | 2013-06 | 4 | line |
| FordEscort-mk3 | Car | 0,1,2 | 85 | 458 | 1981-08 | 1999-08 | 6 | line |
| BMW5E28 | Car | 2,3 | 115 | 503 | 1981-09 | 2002-06 | 4 | line |
| VauxhallCavalierMk2 | Car | 0,1,2 | 100 | 480 | 1981-09 | 1995-06 | 4 | line |
| VWPoloMk2 | Car | 0,1,2 | 70 | 435 | 1981-10 | 2004-06 | 4 | line |
| DatsunStanzaT11 | Car | 0,1,2 | 70 | 435 | 1982-01 | 2001-06 | 4 | line |
| NissanSunnyB11 | Car | 0,1 | 45 | 398 | 1982-05 | 1999-06 | 4 | line |
| NissanCherryN12 | Car | 0,1,2 | 65 | 428 | 1982-09 | 2000-06 | 4 | line |
| FordSierraMk1 | Car | 0,1,2 | 120 | 510 | 1982-10 | 1994-06 | 4 | line |
| NissanMicraK10 | Car | 0,1 | 50 | 405 | 1983-01 | 2003-06 | 4 | line |
| VauxhallNova | Car | 0,1 | 55 | 413 | 1983-04 | 2002-06 | 4 | line |
| AustinMaestro | Car | 0,1,2 | 70 | 435 | 1983-08 | 2002-01 | 6 | line |
| FordFiestaMk2 | Car | 0,1 | 55 | 413 | 1983-08 | 1999-12 | 4 | line |
| Peugeot205 | Car | 0,1,2 | 70 | 435 | 1983-09 | 2006-06 | 4 | line |
| VWGolfMk2 | Car | 0,1,2 | 95 | 473 | 1983-10 | 2000-06 | 4 | line |
| Renault25Phase1 | Car | 2,3,4 | 90 | 465 | 1984-01 | 2001-06 | 4 | line |
| Rover200SD3 | Car | 1,2 | 85 | 458 | 1984-06 | 2000-06 | 4 | line |
| AustinMontego | Car | 0,1,2 | 75 | 443 | 1984-08 | 1998-02 | 6 | line |
| AustinMetroMk2 | Car | 0,1 | 50 | 405 | 1984-10 | 1998-06 | 4 | line |
| VauxhallAstraMk2 | Car | 0,1 | 95 | 473 | 1984-10 | 1999-06 | 4 | line |
| Mercedes230E | Car | 2,3 | 115 | 503 | 1985-01 | 2007-06 | 4 | line |
| NissanBluebirdT12 | Car | 1,2 | 80 | 450 | 1985-01 | 2004-06 | 4 | line |
| FordGranadaMk3 | Car | 0,1,2 | 90 | 465 | 1985-04 | 2013-06 | 4 | line |
| BMW3E30 | Car | 1,2 | 110 | 495 | 1985-09 | 2002-06 | 4 | line |
| BentleyTurboR | Car | 3,4 | 150 | 555 | 1985-10 | 2010-06 | 4 | line |
| CitroenCXSeries2 | Car | 2,3,4 | 90 | 465 | 1986-01 | 2003-06 | 4 | line |
| Renault21Phase1 | Car | 0,1,2 | 75 | 443 | 1986-06 | 2003-06 | 4 | line |
| NissanBluebirdT72 | Car | 1,2 | 82 | 453 | 1986-07 | 2005-06 | 4 | line |
| Rover800 | Car | 2,3 | 110 | 495 | 1986-07 | 2010-06 | 4 | line |
| JaguarXJ | Car | 3 | 150 | 555 | 1986-10 | 2016-06 | 4 | line |
| NissanSunnyN13 | Car | 1,2 | 80 | 450 | 1986-10 | 2004-06 | 4 | line |
| VauxhallCarltonMk2 | Car | 0,1,2 | 75 | 443 | 1986-11 | 2003-06 | 4 | line |
| FordSierraMk2 | Car | 1,2 | 125 | 518 | 1987-02 | 2001-06 | 4 | line |
| BMW7E32 | Car | 3 | 140 | 540 | 1987-06 | 2006-06 | 4 | line |
| Renault25Phase2 | Car | 2,3,4 | 90 | 465 | 1988-06 | 2005-06 | 4 | line |
| BMW5E34 | Car | 2,3 | 120 | 510 | 1988-10 | 2008-06 | 4 | line |
| VauxhallCavalierMk3 | Car | 0,1,2 | 110 | 495 | 1988-10 | 2002-06 | 4 | line |
| AstonVirage | Car | 4 | 70 | 435 | 1989-01 | 2010-06 | 4 | line |
| Renault19Phase1 | Car | 0,1 | 70 | 435 | 1989-01 | 2004-06 | 4 | line |
| FordFiestaMk3 | Car | 0,1 | 65 | 428 | 1989-04 | 2004-12 | 4 | line |
| Renault21Phase2 | Car | 1,2,3 | 75 | 443 | 1989-05 | 2007-06 | 4 | line |
| LandRoverDiscovery1 | Car | 2,3 | 70 | 435 | 1989-10 | 2017-06 | 4 | line |
| Rover200R8 | Car | 0,1,2 | 90 | 465 | 1989-10 | 2005-06 | 4 | line |
| Rover400R8 | Car | 0,1,2 | 90 | 465 | 1990-04 | 2006-06 | 4 | line |
| RoverMetro | Car | 0,1 | 60 | 420 | 1990-05 | 2004-06 | 4 | line |
| LexusLS400 | Car | 3,4 | 145 | 548 | 1990-06 | 2006-06 | 4 | line |
| RenaultClioI | Car | 0,1 | 80 | 450 | 1990-06 | 2008-06 | 4 | line |
| FordEscort-mk4 | Car | 0,1 | 100 | 480 | 1990-08 | 2018-01 | 5 | line |
| NissanPrimeraP10 | Car | 1,2 | 90 | 465 | 1990-09 | 2008-06 | 4 | line |
| NissanSunnyN14 | Car | 1,2 | 70 | 435 | 1991-03 | 2013-06 | 4 | line |
| BMW3E36 | Car | 1,2,3 | 115 | 503 | 1991-04 | 2009-06 | 4 | line |
| MercedesSClassW140 | Car | 3,4 | 170 | 585 | 1991-04 | 2010-06 | 4 | line |
| VauxhallAstraMk3 | Car | 1,2 | 105 | 488 | 1991-09 | 2006-06 | 4 | line |
| VWGolfMk3 | Car | 1,2 | 105 | 488 | 1991-09 | 2008-06 | 4 | line |
| Rover800R17 | Car | 2,3 | 110 | 495 | 1991-11 | 2012-06 | 4 | line |
| ToyotaCorollaE100 | Car | 1,2 | 80 | 450 | 1992-08 | 2008-06 | 4 | line |
| NissanMicra | Car | 0,1 | 75 | 443 | 1992-10 | 2011-06 | 4 | line |
| Renault19Phase2 | Car | 1,2 | 70 | 435 | 1992-10 | 2008-06 | 4 | line |
| FordSierraMk3 | Car | 1,2 | 130 | 525 | 1993-02 | 2002-06 | 3 | line |
| FordMondeoMk1 | Car | 1,2 | 110 | 495 | 1993-03 | 2016-08 | 6 | line |
| VauxhallCorsaB | Car | 0,1 | 65 | 428 | 1993-04 | 2011-12 | 4 | line |
| AudiA6C4 | Car | 2,3 | 85 | 458 | 1994-01 | 2020-06 | 4 | line |
| AudiA8D2 | Car | 3,4 | 100 | 480 | 1994-01 | 2025-06 | 4 | line |
| AstonDB7 | Car | 3,4 | 72 | 438 | 1994-09 | 2016-06 | 4 | line |
| RangeRoverP38 | Car | 3,4 | 140 | 540 | 1994-09 | 2012-06 | 4 | line |
| BMW7E38 | Car | 3,4 | 160 | 570 | 1994-10 | 2012-06 | 4 | line |
| Rover100 | Car | 0,1 | 65 | 428 | 1994-10 | 2007-06 | 4 | line |
| AudiA4B5 | Car | 1,2,3 | 115 | 503 | 1995-01 | 2010-06 | 4 | line |
| Rover400HHR | Car | 0,1,2 | 92 | 468 | 1995-06 | 2011-06 | 4 | line |
| FordGalaxyMk1 | Car | 1,2 | 115 | 503 | 1995-08 | 2022-02 | 6 | line |
| KiaSportage1 | Car | 1,2 | 70 | 435 | 1995-08 | 2017-06 | 4 | line |
| BMW5E39 | Car | 2,3 | 125 | 518 | 1995-09 | 2015-06 | 4 | line |
| FordFiestaMk4 | Car | 0,1 | 75 | 443 | 1995-10 | 2011-12 | 4 | line |
| Rover200R3 | Car | 0,1,2 | 90 | 465 | 1995-10 | 2012-06 | 4 | line |
| VauxhallVectraB | Car | 1,2 | 75 | 443 | 1995-10 | 2011-06 | 4 | line |
| RenaultMeganeI | Car | 0,1 | 80 | 450 | 1996-04 | 2015-06 | 4 | line |
| FordKa | Car | 0,1 | 60 | 420 | 1996-09 | 2016-12 | 6 | line |
| NissanPrimeraP11 | Car | 1,2 | 95 | 473 | 1996-10 | 2014-06 | 4 | line |
| AudiA6C5 | Car | 2,3 | 90 | 465 | 1997-01 | 2025-06 | 4 | line |
| ToyotaCorollaE110 | Car | 0,1 | 85 | 458 | 1997-06 | 2013-06 | 4 | line |
| FordPuma1997 | Car | 1,2 | 65 | 428 | 1997-07 | 2016-06 | 4 | line |
| VWGolfMk4 | Car | 1,2 | 110 | 495 | 1997-10 | 2012-06 | 4 | line |
| LandRoverDiscovery2 | Car | 2,3 | 75 | 443 | 1998-01 | 2023-06 | 4 | line |
| VauxhallAstraMk4 | Car | 0,1,2 | 110 | 495 | 1998-01 | 2013-06 | 4 | line |
| BMW3E46 | Car | 1,2,3 | 120 | 510 | 1998-03 | 2017-06 | 4 | line |
| VWNewBeetle | Car | 1,2 | 100 | 480 | 1998-06 | 2015-06 | 4 | line |
| FordFocus | Car | 1,2 | 125 | 518 | 1998-08 | 2017-12 | 7 | line |
| Peugeot206 | Car | 0,1 | 105 | 488 | 1998-09 | 2028-06 | 4 | line |
| MercedesSClassW220 | Car | 3,4 | 170 | 585 | 1998-10 | 2016-06 | 4 | line |
| JaguarSTypeX200 | Car | 2,3 | 110 | 495 | 1999-03 | 2024-06 | 4 | line |
| ToyotaYarisXP10 | Car | 0,1 | 65 | 428 | 1999-04 | 2014-06 | 4 | line |
| VauxhallZafiraA | Car | 1,2 | 70 | 435 | 1999-05 | 2012-06 | 4 | line |
| Rover75 | Car | 1,2 | 105 | 488 | 1999-06 | 2015-06 | 4 | line |
| Rover25 | Car | 0,1 | 100 | 480 | 1999-10 | 2015-06 | 4 | line |
| Rover45 | Car | 0,1,2 | 105 | 488 | 1999-10 | 2016-06 | 4 | line |
| BMWX5E53 | Car | 3 | 90 | 465 | 2000-01 | 2023-06 | 4 | line |
| NewMini | Car | 1 | 100 | 480 | 2000-10 | 2022-12 | 5 | line |
| ToyotaPriusXW10 | Car | 1,2 | 100 | 480 | 2000-10 | 2019-06 | 4 | line |
| VauxhallCorsaC | Car | 0,1 | 80 | 450 | 2000-10 | 2018-12 | 4 | line |
| AudiA4B6 | Car | 1,2 | 120 | 510 | 2000-11 | 2029-12 | 6 | line |
| AstonVanquish | Car | 4 | 78 | 447 | 2001-09 | 2025-06 | 4 | line |
| BMW7E65 | Car | 3,4 | 170 | 585 | 2001-09 | 2018-06 | 4 | line |
| ToyotaCorollaE120 | Car | 0,1 | 95 | 473 | 2002-01 | 2018-06 | 4 | line |
| NissanPrimeraP12 | Car | 1,2 | 100 | 480 | 2002-03 | 2020-06 | 4 | line |
| RangeRoverL322 | Car | 3,4 | 150 | 555 | 2002-03 | 2020-06 | 4 | line |
| VauxhallVectraC | Car | 0,1,2 | 80 | 450 | 2002-03 | 2017-06 | 4 | line |
| FordFiestaMk5 | Car | 0,1 | 85 | 458 | 2002-04 | 2019-12 | 4 | line |
| AudiA8D3 | Car | 3,4 | 150 | 555 | 2002-11 | 2022-06 | 4 | line |
| RenaultMeganeII | Car | 0,1 | 90 | 465 | 2002-12 | 2021-06 | 4 | line |
| NissanMicraK12 | Car | 0,1 | 60 | 420 | 2003-01 | 2023-06 | 4 | line |
| PorscheCayenne | Car | 3,4 | 125 | 518 | 2003-06 | 2022-06 | 4 | line |
| BMW5E60 | Car | 2,3 | 130 | 525 | 2003-07 | 2021-06 | 4 | line |
| BentleyContinentalGT | Car | 3,4 | 150 | 555 | 2003-09 | 2020-06 | 4 | line |
| AstonDB9 | Car | 3,4 | 80 | 450 | 2004-01 | 2036-06 | 4 | line |
| AudiA6C6 | Car | 2,3 | 92 | 468 | 2004-01 | 2031-06 | 4 | line |
| FiatPanda2 | Car | 0,1 | 60 | 420 | 2004-01 | 2023-06 | 4 | line |
| ToyotaPriusXW20 | Car | 1,2 | 105 | 488 | 2004-01 | 2019-06 | 4 | line |
| VWGolfMk5 | Car | 1,2 | 115 | 503 | 2004-01 | 2019-06 | 4 | line |
| VauxhallAstraMk5 | Car | 0,1 | 115 | 503 | 2004-03 | 2018-06 | 4 | line |
| KiaPicanto | Car | 0,1 | 75 | 443 | 2004-06 | 2020-06 | 4 | line |
| LandRoverDiscovery3 | Car | 3 | 85 | 458 | 2004-06 | 2028-06 | 4 | line |
| BMW1SeriesE87 | Car | 1,2 | 75 | 443 | 2004-09 | 2029-06 | 4 | line |
| AudiA4B7 | Car | 1,2 | 125 | 518 | 2005-01 | 2018-06 | 4 | line |
| KiaSportage2 | Car | 1 | 80 | 450 | 2005-01 | 2025-06 | 4 | line |
| AstonVantage2005 | Car | 3,4 | 78 | 447 | 2005-03 | 2035-06 | 4 | line |
| BMW3E90 | Car | 1,2 | 125 | 518 | 2005-03 | 2023-06 | 4 | line |
| ToyotaAygo | Car | 0,1 | 75 | 443 | 2005-07 | 2024-06 | 4 | line |
| VauxhallZafiraB | Car | 1,2 | 75 | 443 | 2005-07 | 2017-06 | 4 | line |
| MercedesSClassW221 | Car | 3,4 | 170 | 585 | 2005-09 | 2026-06 | 4 | line |
| ToyotaYarisXP90 | Car | 0,1 | 80 | 450 | 2006-01 | 2021-06 | 4 | line |
| NissanNoteE11 | Car | 0,1 | 85 | 458 | 2006-05 | 2024-06 | 4 | line |
| FordGalaxyMk2 | Car | 1,2 | 80 | 450 | 2006-06 | 2032-06 | 4 | line |
| NissanQashqai | Car | 1 | 125 | 518 | 2006-08 | 2024-12 | 5 | line |
| VauxhallCorsaD | Car | 0,1 | 95 | 473 | 2006-10 | 2026-12 | 4 | line |
| MercedesC200 | Car | 1,2 | 130 | 525 | 2007-03 | 2026-06 | 4 | line |
| BMWX5E70 | Car | 3 | 95 | 473 | 2007-04 | 2030-06 | 4 | line |
| FordMondeoMk4 | Car | 0,1,2 | 135 | 533 | 2007-04 | 2034-12 | 6 | line |
| AstonDBSV12 | Car | 4 | 82 | 453 | 2007-08 | 2038-06 | 4 | line |
| JaguarXFX250 | Car | 2,3 | 95 | 473 | 2008-03 | 2032-06 | 4 | line |
| AudiA4B8 | Car | 1,2 | 130 | 525 | 2008-06 | 2025-06 | 4 | line |
| HyundaiI10 | Car | 0,1 | 75 | 443 | 2008-09 | 2023-06 | 4 | line |
| FordFiestaMk6 | Car | 0,1 | 100 | 480 | 2008-10 | 2026-12 | 4 | line |
| VWGolfMk6 | Car | 1,2 | 120 | 510 | 2008-10 | 2023-06 | 4 | line |
| BMW7F01 | Car | 3 | 170 | 585 | 2008-11 | 2028-06 | 4 | line |
| RenaultMeganeIII | Car | 0,1 | 100 | 480 | 2009-01 | 2027-06 | 4 | line |
| ToyotaPriusXW30 | Car | 1,2 | 110 | 495 | 2009-08 | 2024-06 | 4 | line |
| LandRoverDiscovery4 | Car | 3 | 90 | 465 | 2009-09 | 2034-06 | 4 | line |
| VauxhallAstraMk6 | Car | 0,1 | 120 | 510 | 2009-09 | 2023-06 | 4 | line |
| AudiA8D4 | Car | 3 | 105 | 488 | 2010-01 | 2037-06 | 4 | line |
| BMW5F10 | Car | 2 | 135 | 533 | 2010-03 | 2028-06 | 4 | line |
| AstonRapide | Car | 3,4 | 88 | 462 | 2010-05 | 2039-06 | 4 | line |
| KiaSportage3 | Car | 1,2 | 85 | 458 | 2010-08 | 2031-06 | 4 | line |
| NissanJukeF15 | Car | 0,1 | 85 | 458 | 2010-09 | 2028-06 | 4 | line |
| NissanMicraK13 | Car | 0,1 | 65 | 428 | 2010-12 | 2033-06 | 4 | line |
| AudiA6C7 | Car | 2,3 | 95 | 473 | 2011-01 | 2038-06 | 4 | line |
| BentleyContinentalGT2 | Car | 3,4 | 155 | 563 | 2011-01 | 2029-06 | 4 | line |
| ToyotaYarisXP130 | Car | 0,1 | 95 | 473 | 2011-08 | 2029-12 | 4 | line |
| BMW1SeriesF20 | Car | 1,2 | 80 | 450 | 2011-09 | 2037-06 | 4 | line |
| BMW3F30 | Car | 1,2 | 135 | 533 | 2011-09 | 2030-06 | 4 | line |
| VWUp | Car | 0,1 | 65 | 428 | 2011-10 | 2037-06 | 4 | line |
| FiatPanda3 | Car | 0,1 | 65 | 428 | 2012-02 | present | 4 | line |
| VauxhallZafiraC | Car | 1,2 | 80 | 450 | 2012-03 | 2021-06 | 4 | line |
| RangeRoverL405 | Car | 3,4 | 160 | 570 | 2012-09 | 2028-06 | 4 | line |
| VWGolfMk7 | Car | 1,2 | 125 | 518 | 2012-10 | 2028-06 | 4 | line |
| VauxhallMokkaA | Car | 1 | 70 | 435 | 2012-11 | 2019-06 | 4 | line |
| DaciaSandero | Car | 0,1 | 85 | 458 | 2013-01 | 2030-06 | 4 | line |
| MercedesSClassW222 | Car | 3,4 | 175 | 593 | 2013-09 | 2032-06 | 4 | line |
| NissanNoteE12 | Car | 0,1 | 85 | 458 | 2013-09 | 2031-06 | 4 | line |
| BMWi3 | Car | 1,2 | 75 | 443 | 2013-11 | 2041-06 | 4 | line |
| BMWX5F15 | Car | 3 | 98 | 477 | 2013-11 | 2035-06 | 4 | line |
| HyundaiI10Mk2 | Car | 0,1 | 65 | 428 | 2014-01 | 2036-06 | 4 | line |
| NissanQashqaiJ11 | Car | 1,2 | 95 | 473 | 2014-01 | 2032-06 | 4 | line |
| JaguarXFX260 | Car | 2 | 100 | 480 | 2015-01 | 2039-06 | 4 | line |
| VauxhallCorsaE | Car | 0,1 | 105 | 488 | 2015-01 | 2032-12 | 4 | line |
| VauxhallViva2015 | Car | 0,1 | 60 | 420 | 2015-06 | 2030-06 | 4 | line |
| FordGalaxyMk3 | Car | 1,2 | 135 | 533 | 2015-08 | 2036-12 | 3 | line |
| VauxhallAstraMk7 | Car | 0,1 | 125 | 518 | 2015-09 | 2033-12 | 4 | line |
| BMW7G11 | Car | 3 | 175 | 593 | 2015-10 | 2033-06 | 4 | line |
| AudiA4B9 | Car | 1,2 | 135 | 533 | 2016-01 | 2033-06 | 4 | line |
| KiaSportage4 | Car | 1,2 | 90 | 465 | 2016-02 | 2037-06 | 4 | line |
| AstonDB11 | Car | 3,4 | 90 | 465 | 2016-03 | 2045-06 | 4 | line |
| ToyotaPriusXW50 | Car | 1,2 | 115 | 503 | 2016-03 | 2031-06 | 4 | line |
| RenaultMeganeIV | Car | 0,1 | 110 | 495 | 2016-07 | 2033-06 | 4 | line |
| TeslaModelS | Car | 1,2,3 | 105 | 488 | 2016-10 | 2036-06 | 4 | line |
| VauxhallMokkaX | Car | 1,2 | 72 | 438 | 2016-10 | 2021-06 | 4 | line |
| BMW5G30 | Car | 2 | 140 | 540 | 2017-03 | 2035-06 | 4 | line |
| NissanMicraK14 | Car | 0,1 | 70 | 435 | 2017-03 | 2042-06 | 4 | line |
| LandRoverDiscovery5 | Car | 3 | 95 | 473 | 2017-04 | present | 4 | line |
| FordFiestaMk7 | Car | 0,1 | 115 | 503 | 2017-07 | 2039-12 | 4 | line |
| AudiA8D5 | Car | 3 | 108 | 492 | 2017-10 | present | 4 | line |
| BentleyContinentalGT3 | Car | 3,4 | 160 | 570 | 2018-05 | 2035-06 | 4 | line |
| AstonVantage2018 | Car | 3,4 | 88 | 462 | 2018-06 | 2046-06 | 4 | line |
| AudiA6C8 | Car | 2,3 | 98 | 477 | 2018-06 | 2036-12 | 4 | line |
| BMWX5G05 | Car | 3 | 100 | 480 | 2018-12 | present | 4 | line |
| LexusESXZ10 | Car | 2 | 100 | 480 | 2019-01 | present | 4 | line |
| BMW3G20 | Car | 1,2 | 135 | 533 | 2019-03 | present | 4 | line |
| TeslaModel3 | Car | 1,2 | 90 | 465 | 2019-05 | present | 4 | line |
| BMW1SeriesF40 | Car | 1,2 | 85 | 458 | 2019-09 | 2037-12 | 4 | line |
| FordPuma2019 | Car | 1 | 75 | 443 | 2019-10 | present | 4 | line |
| NissanJukeF16 | Car | 0,1 | 95 | 473 | 2019-11 | present | 4 | line |
| HyundaiI10Mk3 | Car | 0,1 | 70 | 435 | 2020-01 | present | 4 | line |
| VauxhallCorsaF | Car | 0,1 | 115 | 503 | 2020-01 | present | 4 | line |
| VWGolfMk8 | Car | 1,2 | 130 | 525 | 2020-03 | present | 4 | line |
| AstonDBX | Car | 3,4 | 92 | 468 | 2020-07 | present | 4 | line |
| ToyotaYarisXP210 | Car | 0,1 | 105 | 488 | 2020-08 | present | 4 | line |
| VauxhallMokkaB | Car | 1 | 80 | 450 | 2021-04 | present | 4 | line |
| BMWiX3 | Car | 1,2,3 | 100 | 480 | 2021-07 | 2044-06 | 4 | line |
| NissanQashqaiJ12 | Car | 1,2 | 100 | 480 | 2021-07 | present | 4 | line |
| TeslaModelY | Car | 1,2 | 95 | 473 | 2021-10 | present | 4 | line |
| VauxhallAstraMk8 | Car | 1 | 130 | 525 | 2021-10 | present | 4 | line |
| KiaSportage5 | Car | 1,2 | 95 | 473 | 2022-01 | present | 4 | line |
| ToyotaAygoX | Car | 0,1 | 65 | 428 | 2022-03 | present | 4 | line |
| RenaultMeganeV | Car | 1,2 | 115 | 503 | 2022-07 | present | 4 | line |
| BMW7G70 | Car | 3,4 | 180 | 600 | 2022-12 | present | 4 | line |
| BYDAtto3 | Car | 1,2 | 80 | 450 | 2023-03 | present | 4 | line |
| BMW5G60 | Car | 2 | 145 | 548 | 2023-10 | present | 4 | line |
| BYDDolphin | Car | 0,1 | 70 | 435 | 2023-10 | present | 4 | line |
| BYDSeal | Car | 1,2 | 90 | 465 | 2023-11 | present | 4 | line |
| PorscheMacanElectric | Car | 3 | 95 | 473 | 2024-01 | present | 4 | line |
| BentleyContinentalGT4 | Car | 3,4 | 165 | 578 | 2024-07 | present | 4 | line |
| ToyotaPriusXW60 | Car | 1,2 | 120 | 510 | 2024-07 | present | 4 | line |
| BMW1SeriesF70 | Car | 1,2 | 88 | 462 | 2024-10 | present | 4 | line |
| BYDSealion7 | Car | 1,2 | 95 | 473 | 2025-01 | present | 4 | line |
| Jaecoo7 | Car | 1,2 | 90 | 465 | 2025-01 | present | 4 | line |
| NissanMicraK15 | Car | 1 | 80 | 450 | 2025-09 | present | 4 | line |
| Jaecoo5 | Car | 1 | 85 | 458 | 2025-10 | present | 4 | line |
| FiatGrandePandaElectric | Car | 1 | 75 | 443 | 2026-02 | present | 4 | line |
| Jaecoo8 | Car | 1,2 | 95 | 473 | 2026-05 | present | 4 | line |

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
