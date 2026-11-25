---
status: draft
verified: New ex-15 @ 36a741673 (working tree)
date: 2026-11-25
---
# Research pass 57 - Gross tonnage for the 159 blank water objects

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `water-gross-tonnage-additions.csv`.
No `.dat` file, workbook, `evidence_data.py`, `build_workbooks.py` or existing document was
changed.

[Report 56](research-pricing-report-56.md) priced 57 of the 216 water objects by gross tonnage and
left 159 blank. The project has decided to price every water object by gross tonnage, so this pass
was sent to fill the blank rows where a defensible figure exists. The route that report 56 named
for the inland fleet - the National Historic Ships UK register - works: the register prints a
"Tonnage: Gross" field for many of its vessels, and it is the source of 96 of the 120 new figures.
The pass found figures for 120 of the 159 rows and left 39 without one: 9 hovercraft and 9 holds,
which have no gross tonnage of their own, 3 objects that are not vessels, and 18 hulls for which no
defensible figure was found. The 18 are named in §6 with the register that would close each.

## 1. What this pass found

1. **One hundred and twenty of the 159 blank rows now carry a gross tonnage, so 177 of the 216
   rows (82 per cent) have a figure.** By grade the new 120 are **MEASURED 96, STATED 2, DERIVED
   22**. With report 56's 57 rows the class stands at **MEASURED 98, STATED 56, DERIVED 23,
   UNAVAILABLE 39**. By type, the 120 new figures are barges 50, narrowboats 37, cargo ships 10,
   river boats 9, coasters 6, tugs 4, fishing and other craft 3, ferries 1. **MEASURED (register
   readings), DERIVED (bridges).**

2. **The National Historic Ships UK register prints gross tonnage.** Each register entry carries a
   "Dimensions" block with length, beam and **"Tonnage: Gross"**, for example *Basuto* 64.00,
   *Grimsby* 22.00, *Ironclad* 60.00, *Maybrent* 70.00, *Comrade* 69.00. Report 56 read the
   register for *President* and found dimensions but no tonnage; that entry is one of the entries
   where the field is empty, and many others are filled. The register is therefore the route for
   the inland fleet, and it was read directly rather than through a second-hand page.
   **MEASURED ([nationalhistoricships.org.uk](https://www.nationalhistoricships.org.uk/)).**

3. **The inland register figures cluster tightly enough to transfer by type.** The pass read more
   than 80 register entries. The readings that fix the types: 70 ft narrowboats and butties 20, 22,
   22, 24 GT with two 1930s large Woolwich motors at 40 and 45; wide-gauge motor canal boats 60 GT;
   dumb barges 59, 70, 70 GT; Humber keels 69, 70, 71 GT; narrow canal tugs 13 GT; wide canal and
   estuarine tugs 32 and 60 GT; harbour tugs 54, 62.61, 94, 166, 200, 261 GT. Every group except
   the harbour tugs is within about 30 per cent of its own median, which is what makes a type
   representative defensible for 105 of the 120 rows. **MEASURED.**

4. **Gross tonnage is a property of the hull, so every cargo fit of one hull carries the same
   figure.** Ninety-six of the 120 new rows repeat one hull's number across its fits: the seven
   narrowboat files carry 22 GT on 37 rows, the three wide-barge files carry 60 GT on 18 rows, the
   two dumb-barge files carry 70 GT on 12 rows, the canal boats carry 22 GT on 10, the Humber keels
   69 GT on 6, the puffers 64 GT on 6 and the seven Handysize fits 12,600 GT. The alternative -
   bridging each fit from its own capacity - would price one hull at seven to nine different
   tonnages, which is what report 56 already rejected when it gave the surviving Norfolk wherry's
   22.78 GRT to all six of its fits. **CODE (`.dat` capacity fields), MEASURED (register
   figures).**

5. **Only 16 distinct vessels stand behind the 120 new figures, and the coverage count overstates
   the evidence.** Fourteen register or article vessels cover 98 rows (*Grimsby* 42, *Ironclad* 18,
   *Maybrent* 12, *Comrade* 6, *Basuto* 6, *Xebec* 5, *Pacific* 2, and one row each for
   *Mayflower*, *Portwey*, *Isabella Fortuna*, *Veronica*, *Lydia Eva*, *Loch Shira* and
   *Madagascar*); two more (*Christina*, *Tuloma*) supply the Handysize ratio that covers 7 rows.
   A reader should treat the 177-row total as 55 distinct vessels (report 56's 39 and this pass's
   16) plus 15 bridged rows, not as 177 measurements. **DERIVED from the addition rows.**

6. **Report 56's coverage table sums to 225, not 216, because the nine holds are counted twice.**
   That table lists "Ferries (sea) 37" and "Holds 9" as separate groups, but the three ferry holds
   are already inside the 37 ferry rows: a hold carries its parent's `type` value in
   `water-gross-tonnage.csv` and is distinguished by its `kind` value of `hold`. The correct
   grouping is 34 ferries plus 3 ferry holds, 19 river boats plus 5 river holds, 10 other craft
   plus 1 other hold, and the 9 holds counted once. The counts in §4 use that grouping.
   **CODE (`water-gross-tonnage.csv`, `kind` and `type` columns).**

7. **The nine hovercraft have no gross tonnage, and their length and displacement are now
   recorded.** An air-cushion vehicle is not a registered ship: it displaces air on a cushion, has
   no enclosed-volume register and is measured by length and all-up weight. The figures read:
   AP1-88/200 24.5 m and 47.6 t full-load displacement; AP1-88/400 28.5 m and 69 t; BHT-130
   29.3 m and 70 t all-up; SR.N4 Mk 1 39.68 m and 165 t gross weight; SR.N4 Mk 3 56.38 m and
   320 t; SR.N6 17.78 m and 10.9 t. These are recorded in the `notes` column for the workbook's
   capacity rule. **STATED (builder and type articles), UNAVAILABLE (gross tonnage).**

8. **A modern handysize bulker is 0.63 GT a deadweight ton, so report 56's 1.6 cargo ratio cannot
   be carried to it.** Two registered bulkers give the ratio: *Christina* (2011) 20,969 GT on
   32,573 dwt = 0.644, and *Tuloma* (1984) 18,259 GT on 29,785 dwt = 0.613. The mean, 0.629, on
   the pakset's 20,000 t, gives **12,600 GT**. The pakset's 1.6 ratio would give 32,000 GT, two and
   a half times too high, because that ratio was fitted on sailing and early steam cargo ships
   whose hulls were large relative to their cargo. The Handysize rows are therefore the one cargo
   group priced from a ratio of two real ships rather than from report 56's bridge.
   **DERIVED (20,000 x 0.629 = 12,580, rounded).**

9. **The Clyde puffer is 64 GT.** *Basuto* (1902, 20.10 m, 4.80 m beam) is the oldest surviving
   puffer and prints "Tonnage: Gross 64.00". She closes the coaster gap that report 56 recorded as
   0 of 6, and she sits between the pakset's 9 t and 75 t capacity fits without strain.
   **MEASURED.**

10. **The bridges are used for 15 rows only, and each shows its arithmetic.** Six generic river
    steamers and three modern Thames river boats use the river ratio (6.2 GT a capacity tonne),
    two cargo hulls use the cargo ratio (1.6) and four Shropshire tub boats use the inland ratio
    (1.2). Every bridge row states the multiplication in its `notes` column and cites the report 56
    band. The river bridge gives 22 GT for a 51-passenger 1988 river bus and 217 GT for a
    500-passenger 1905 steamer, both inside the 3.1-9.3 band. **DERIVED.**

11. **Eighteen hulls still have no figure, and each has a named route or a stated reason.**
    The 5 ferries (two Channel steamers, the Tyne ferry, Island, Hydrocat), the 4 river-boat rows
    (the three PS Industry fits and ClydeSteamer), the 2 early tugs (1816 paddle, 1841 iron screw)
    and the 7 fishing and skiff rows (Dogger, six skiff wherries) are listed in §6. Report 56
    forbids bridging generic ferries and this pass did not find a vessel to anchor them.
    **UNAVAILABLE.**

12. **Result.** The water class now has a gross tonnage for 177 of its 216 objects. Thirty-nine
    rows have none: 9 hovercraft, which have no gross tonnage at all; 9 holds, whose figure is on
    the parent row; 18 hulls with no figure (5 ferries, 4 river boats, 2 tugs and 7 fishing and
    skiff craft); and 3 objects that are not vessels. The 120 new figures are strong for the
    inland and coastal fleet (96 register readings) and weaker where a type was transferred across
    eras: the 1864 steam seiner is priced from a 1930 steam drifter, and the wooden dumb barge from
    a 1920 steel one. Those two transfers are flagged in their rows.

## 2. Method

- **The rows.** The pass read `water-gross-tonnage.csv`, took the 159 rows whose `gross_tonnage`
  is blank, and wrote one addition row for each, keyed on the exact `name`. The join is exact: 159
  names out, 159 names in, no unmatched name on either side. `pakset_file` and `type` are copied
  from the master row so the two files cannot drift. `[CODE New ex-15 @ 36a741673:
  water-gross-tonnage.csv]`
- **The register reading.** National Historic Ships UK register entries were fetched directly and
  the "Dimensions" block read: `Length: Overall`, `Breadth: Beam`, `Tonnage: Gross`, plus
  `Vessel type`, `Built in` and `Hull material`. The register's own label is "Tonnage: Gross", so
  the measure is gross register tonnage for pre-1969 hulls and 1969-Convention gross tonnage for
  later ones; the `gross_tonnage_definition` column says which. `[LITERATURE:
  https://www.nationalhistoricships.org.uk/]`
- **Identity.** Four bases, recorded in `identity_basis`:
  - **named** - not used in this pass; report 56 exhausted the named-vessel rows.
  - **type representative** - the object is a generic type and the tonnage belongs to one
    documented vessel of that type. The `identity` string has the form "type (representative:
    vessel, year)" and the `notes` column repeats the vessel and its dimensions.
  - **capacity bridge** - no vessel could be tied to the row, the group is homogeneous, and the
    figure is the report 56 ratio applied to the pakset capacity. The arithmetic is in `notes`.
  - **type** - no figure at all; `notes` says why.
- **Definitions of tonnage.** Kept apart in `gross_tonnage_definition` exactly as report 56 does:
  - **GRT** - gross register tonnage, the pre-1969 measure of enclosed volume in units of 100
    cubic feet.
  - **GT** - gross tonnage under the 1969 Convention, a dimensionless index on the same volume.
  - **bm** - builder's old measurement, the pre-1836 capacity formula. No new row uses bm; the one
    1837 ship (*Madagascar*) is recorded as GRT because the register measure replaced bm in 1836.
  - **"GRT (bridge)"** marks a figure produced by arithmetic rather than read from a register.
- **Grades.** MEASURED = the figure is read from a register entry. STATED = printed in a type
  article or an infobox without the register visible. DERIVED = arithmetic from a stated ratio or
  range, shown in the row. UNAVAILABLE = no figure. Definitions: [claim tags](../claim-tags.md).
  A MEASURED row whose object is a type representative means that the *representative's* figure is
  measured, not the object's; §5 gives the transfer error by type.
- **The `year` column** is the build year of the vessel whose figure is used, not the pakset
  intro year. It is blank on bridge rows because a bridge has no vessel and therefore no year;
  the `identity` string carries the pakset type's own date instead.
- **No `.dat` price, workbook figure or pakset capacity is used as evidence of tonnage.** Capacity
  appears only inside a stated bridge, and only as the multiplier.
- **Order of resolution.** Own vessel first, sister second, type representative third, bridge
  fourth, blank last. Every blank row's `notes` gives the route that failed or the reason no route
  exists.

## 3. Evidence table

Every figure used as a row's gross tonnage. The URL is the page read. `Tonnage: Gross` is the
register's own label; the grade is against the figure, not the page.

| Vessel | Register type | Built | Tonnage | Definition | Grade | Source |
|---|---|---:|---:|---|---|---|
| *Basuto* | Clyde puffer | 1902 | 64.00 | GRT | MEASURED | [nhs/11](https://www.nationalhistoricships.org.uk/register/11/basuto) |
| *Ironclad* | Barge, Leeds & Liverpool longboat | 1933 | 60.00 | GRT | MEASURED | [nhs/2371](https://www.nationalhistoricships.org.uk/register/2371/ironclad) |
| *Maybrent* | Barge, dumb | 1920 | 70.00 | GRT | MEASURED | [nhs/3907](https://www.nationalhistoricships.org.uk/register/3907/maybrent) |
| *Comrade* | Keel, Humber | 1923 | 69.00 | GRT | MEASURED | [nhs/435](https://www.nationalhistoricships.org.uk/register/435/comrade) |
| *Grimsby* | Narrowboat, butty | 1910 | 22.00 | GRT | MEASURED | [nhs/1987](https://www.nationalhistoricships.org.uk/register/1987/grimsby) |
| *Xebec* | Narrowboat, day boat | 1910 | 22.00 | GRT | MEASURED | [nhs/2958](https://www.nationalhistoricships.org.uk/register/2958/xebec) |
| *Pacific* | Tug, inland/canal | 1934 | 13.00 | GRT | MEASURED | [nhs/2023](https://www.nationalhistoricships.org.uk/register/2023/pacific) |
| *Mayflower* | Tug, inland/canal | 1861 | 32.00 | GRT | MEASURED | [nhs/45](https://www.nationalhistoricships.org.uk/register/45/mayflower) |
| *Portwey* | Tug, harbour/coastal | 1927 | 94.00 | GRT | MEASURED | [nhs/54](https://www.nationalhistoricships.org.uk/register/54/portwey) |
| *Isabella Fortuna* | Lugger, fifie | 1890 | 25.00 | GRT | MEASURED | [nhs/705](https://www.nationalhistoricships.org.uk/register/705/isabella-fortuna) |
| *Veronica* | Netter, seine | 1932 | 21.00 | GRT | MEASURED | [nhs/1606](https://www.nationalhistoricships.org.uk/register/1606/veronica) |
| *Lydia Eva* | Drifter, steam | 1930 | 138.00 | GRT | MEASURED | [nhs/43](https://www.nationalhistoricships.org.uk/register/43/lydia-eva) |
| MV *Loch Shira* | Double-ended ferry | 2007 | 1,024 | GT | STATED | [MV Loch Shira](https://en.wikipedia.org/wiki/MV_Loch_Shira) |
| *Madagascar* | Blackwall frigate | 1837 | 951 | GRT | STATED | [Blackwall frigate](https://en.wikipedia.org/wiki/Blackwall_frigate) |
| *Christina* | Handysize bulker | 2011 | 20,969 GT on 32,573 dwt | GT | STATED | [vesselhunter 9584188](https://vesselhunter.io/vessels/9584188) |
| *Tuloma* | Handysize bulker | 1984 | 18,259 GT on 29,785 dwt | GT | STATED | [rynda 8123731](https://rynda.io/vessels/8123731-tuloma) |

Supporting register readings, quoted in the `notes` column to establish each type's range but not
used as a row's figure:

| Vessel | Type | Built | Tonnage | Source |
|---|---|---:|---:|---|
| *Hope* | Humber keel | 1908 | 71.00 | [nhs/2632](https://www.nationalhistoricships.org.uk/register/2632/hope) |
| *Goodwill* | Humber keel | 1953 | 70.00 | [nhs/2714](https://www.nationalhistoricships.org.uk/register/2714/goodwill) |
| *Laura* | Dumb barge | 1954 | 70.00 | [nhs/3475](https://www.nationalhistoricships.org.uk/register/3475/laura) |
| *Bigmere* | Dumb barge | 1948 | 59.00 | [nhs/126](https://www.nationalhistoricships.org.uk/register/126/bigmere) |
| *Kangaroo* | Narrowboat | 1928 | 24.00 | [nhs/3518](https://www.nationalhistoricships.org.uk/register/3518/kangaroo) |
| *Malvern* | Narrowboat, butty | 1928 | 20.00 | [nhs/2810](https://www.nationalhistoricships.org.uk/register/2810/malvern) |
| *Bletchley* | Narrowboat, Town class | 1936 | 40.00 | [nhs/3842](https://www.nationalhistoricships.org.uk/register/3842/bletchley) |
| *Southam* | Narrowboat, butty | 1936 | 45.00 | [nhs/673](https://www.nationalhistoricships.org.uk/register/673/southam) |
| *Hatfield* | Tug, inland/canal | 1955 | 60.00 | [nhs/1983](https://www.nationalhistoricships.org.uk/register/1983/hatfield) |
| *Brent* | Tug, harbour/coastal | 1945 | 54.00 | [nhs/3](https://www.nationalhistoricships.org.uk/register/3/brent) |
| *Kerne* | Tug, harbour/coastal | 1912 | 62.61 | [nhs/34](https://www.nationalhistoricships.org.uk/register/34/kerne) |
| *Eppleton Hall* | Tug, harbour/coastal | 1914 | 166.00 | [nhs/3021](https://www.nationalhistoricships.org.uk/register/3021/eppleton-hall) |
| *Canning* | Tug, harbour/coastal | 1954 | 200.00 | [nhs/4](https://www.nationalhistoricships.org.uk/register/4/canning) |
| *Flying Buzzard* | Tug, harbour/coastal | 1951 | 261.00 | [nhs/634](https://www.nationalhistoricships.org.uk/register/634/flying-buzzard) |
| *Reaper* | Fifie | 1901 | 61.00 | [nhs/172](https://www.nationalhistoricships.org.uk/register/172/reaper) |
| *Favourite* | Seine netter | 1947 | 5.00 | [nhs/1050](https://www.nationalhistoricships.org.uk/register/1050/favourite) |
| *Feasible* | Steam drifter | 1912 | 150.00 | [nhs/711](https://www.nationalhistoricships.org.uk/register/711/feasible) |

Notes on the rows where the figure needs explanation:

- **Narrowboats (37 rows, 22 GT).** *Grimsby* is a 1910 butty of 21.84 m. The register's 70 ft
  cargo boats run 20-24 GT (*Malvern* 20, *Grimsby* 22, *Kangaroo* 24) with two 1930s large
  Woolwich motors at 40 (*Bletchley*) and 45 (*Southam*), and modern leisure boats at 15-16
  (*Norway* 2023, *Redshank* 1975). 22 GT is the cluster's centre. The figure applies to the
  wooden, composite, steel, steam, semi-diesel and diesel hulls alike because the pakset gives them
  one 70 ft hull and the register shows no systematic difference by hull material.
- **Box boats and the market boat (5 rows, 22 GT).** *Xebec* is a 1910 open canal day boat of
  19.81 m. The pakset box boat is the same hull with a 7-17 t load, and the 4-length-unit market
  boat is shorter, so 22 GT is an upper bound for the market boat; the row says so.
- **Wide canal barges (18 rows, 60 GT).** *Ironclad* is a 1933 steel Leeds & Liverpool longboat of
  22.00 m and 4.45 m beam, under motor. The same figure covers the 1949 lightweight barges and the
  towed barges because they are the same wide-gauge hull.
- **Dumb barges (12 rows, 70 GT).** *Maybrent* (1920, steel, 22.86 m) is the representative.
  *Laura* (1954) is also 70 GT and *Bigmere* (1948) 59 GT. No wooden dumb barge with a printed
  tonnage was found; the wooden rows therefore use a steel figure and the row says so.
- **Humber keels (6 rows, 69 GT).** *Comrade* (1923, 18.68 m) is 69 GT against *Hope* 71 and
  *Goodwill* 70, so the type is 69-71 GT. The passenger fit carries the same hull figure.
- **Clyde puffers (6 rows, 64 GT).** *Basuto* is the oldest surviving puffer and the only one
  built near the pakset type's 1856 start; the surviving 1940s VIC puffers are a later variant and
  are not used.
- **Tugs (4 rows).** *Pacific* (13 GT) covers the bantam pusher and the narrowboat tug because it
  is the only narrow-beam canal tug in the register with a printed tonnage. *Mayflower* (32 GT,
  1861) covers the steam barge tug: she is a steam canal tug of the pakset object's own era.
  *Portwey* (94 GT, 1927) covers the 1933 diesel harbour tug; the register's harbour tugs run
  54-261 GT and *Portwey* is the nearest dated.
- **Fishing craft (3 rows).** *Isabella Fortuna* (25 GT, 1890, 13.26 m) is a small fifie, matching
  the pakset's 15 t capacity; *Reaper* (61 GT) is the large end. *Veronica* (21 GT, 1932) covers
  the diesel seine netter. *Lydia Eva* (138 GT, 1930) covers the 1864 steam seiner because no
  1860s steam fishing vessel is registered; the 66-year gap is a real error bar and the row says
  so.
- **MV Loch Shira (1 row).** 53.9 m, 1,024 GT, 250 passengers and 36 cars, which is the pakset
  Super-Loch's 250 passengers and 32.6 t of cargo. Wikipedia infobox figure.
- **Madagascar (1 row).** The Blackwall frigate article gives *Seringapatam* (1837) 871 tons,
  *Madagascar* (1837) 951 tons and *Melbourne* (1875) 1,857 tons. *Madagascar* is used because the
  pakset hull carries 899 t of cargo. The article prints "951-ton" without naming the measure; for
  an 1837 ship that is registered tonnage.
- **Handysize (7 rows, 12,600 GT).** Derived, not read: 20,969/32,573 = 0.644 and 18,259/29,785 =
  0.613; mean 0.629; 20,000 x 0.629 = 12,580, rounded to 12,600. The 20,000 t is the pakset
  payload, treated as deadweight. The seven fits carry different payloads from 480 to 20,000 t and
  all carry the hull's figure.

### 3.1 The bridge arithmetic

| Rows | Type | Capacity (t) | Ratio | Gross tons | Band |
|---|---|---:|---:|---:|---|
| IronPaddleSteamer | river boat | 23.4 | 6.2 | 145 | 3.1-9.3 |
| IronRiverSteamer | river boat | 24.5 | 6.2 | 152 | 3.1-9.3 |
| WoodenPaddleSteamer | river boat | 21.5 | 6.2 | 133 | 3.1-9.3 |
| WoodenRiverSteamer | river boat | 17.5 | 6.2 | 109 | 3.1-9.3 |
| SteelRiverSteamer | river boat | 28.0 | 6.2 | 174 | 3.1-9.3 |
| LargeSteelRiverSteamer | river boat | 35.0 | 6.2 | 217 | 3.1-9.3 |
| ThameslineRiverbus | river boat | 3.6 | 6.2 | 22 | 3.1-9.3 |
| River-Runner-150 | river boat | 9.7 | 6.2 | 60 | 3.1-9.3 |
| River-Runner-200 | river boat | 15.4 | 6.2 | 95 | 3.1-9.3 |
| ClydeCargoSteamerHull | cargo ship | 1,616.2 | 1.6 | 2,586 | 0.8-2.3 |
| SchoonerHull | cargo ship | 244.2 | 1.6 | 391 | 0.8-2.3 |
| TubBoatBulk | barge | 4.0 | 1.2 | 4.8 | 0.9-1.5 |
| TubBoatCool | barge | 2.0 | 1.2 | 2.4 | 0.9-1.5 |
| TubBoatLong | barge | 2.0 | 1.2 | 2.4 | 0.9-1.5 |
| TubBoatPiece | barge | 3.5 | 1.2 | 4.2 | 0.9-1.5 |

The capacity is `total_size_t` from `water-gross-tonnage.csv`: passengers at 0.075 t plus cargo
tonnes. The ratios and bands are report 56 §4.3. The two cargo rows are the least satisfactory
figures in the pass: the 1.6 ratio is the sample's midpoint, but the only steam ship in that
sample sits at 0.80, so 2,586 GT for a 1,616 t 1869 steamer is probably about twice its real
register tonnage, and 391 GT for a 244 t schooner is at the top of the plausible range. A named
vessel for either would replace both.

## 4. Coverage

### 4.1 Before and after, by type

"Holds" are counted separately here; their parent types are the 34 ferries, 19 river boats and 10
other craft, which is why those counts are lower than report 56's table (see §1 point 6).

| Group | Rows | With a figure before | Added | No figure by definition | Still blank |
|---|---:|---:|---:|---:|---:|
| Ferries (sea) | 34 | 28 | 1 | 0 | 5 |
| River boats | 19 | 6 | 9 | 0 | 4 |
| Cargo ships | 21 | 11 | 10 | 0 | 0 |
| Coasters | 6 | 0 | 6 | 0 | 0 |
| Barges | 62 | 12 | 50 | 0 | 0 |
| Narrowboats | 37 | 0 | 37 | 0 | 0 |
| Hovercraft | 9 | 0 | 0 | 9 | 0 |
| Tugs | 9 | 0 | 4 | 0 | 5 |
| Other (fishing, skiffs) | 10 | 0 | 3 | 0 | 7 |
| Holds | 9 | 0 | 0 | 0 | 9 |
| **Total** | **216** | **57** | **120** | **9** | **30** |

The 5 blank tugs are 2 tugs with no figure and the 3 objects that are not vessels (two horse teams
and a towpath tractor). The 30 blanks are therefore 18 hulls with no figure, 9 holds whose figure
is on the parent row and 3 objects that are not vessels; the 9 hovercraft are the "no figure by
definition" column, which with the 30 blanks makes 39 rows without a number.

### 4.2 Grades after the pass, by type

| Group | MEASURED | STATED | DERIVED | UNAVAILABLE | Rows |
|---|---:|---:|---:|---:|---:|
| Ferries (sea) | 1 | 28 | 0 | 5 | 34 |
| River boats | 1 | 5 | 9 | 4 | 19 |
| Cargo ships | 0 | 11 | 10 | 0 | 21 |
| Coasters | 6 | 0 | 0 | 0 | 6 |
| Barges | 46 | 12 | 4 | 0 | 62 |
| Narrowboats | 37 | 0 | 0 | 0 | 37 |
| Hovercraft | 0 | 0 | 0 | 9 | 9 |
| Tugs | 4 | 0 | 0 | 5 | 9 |
| Other | 3 | 0 | 0 | 7 | 10 |
| Holds | 0 | 0 | 0 | 9 | 9 |
| **Total** | **98** | **56** | **23** | **39** | **216** |

The 120 rows added by this pass are MEASURED 96, STATED 2, DERIVED 22. The 96 MEASURED rows rest
on 12 register entries, and the 22 DERIVED rows on 15 bridge calculations and 2 ratio ships.

## 5. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| Narrowboat, 70 ft (37 rows) | 22 GT | 20-24 GT; 15-45 across the register | seven register readings, two of them 1930s motors with cabins |
| Canal day boat / box boat (5 rows) | 22 GT | +/- 30% | one 65 ft day boat; the market boat is shorter |
| Wide canal barge (18 rows) | 60 GT | +/- 15% | one 1933 Hull boat; the 1949 lightweights are unmeasured |
| Dumb barge (12 rows) | 70 GT | 59-70 GT for steel; wooden unmeasured | three readings, all steel |
| Humber keel (6 rows) | 69 GT | 69-71 GT | three readings |
| Clyde puffer (6 rows) | 64 GT | +/- 20% | one 1902 hull against the 1940s VIC variant |
| Narrow canal tug (2 rows) | 13 GT | -50% / +130% | 13 GT narrow boat against 32 GT wide boat |
| Harbour tug (1 row) | 94 GT | 54-261 GT | six readings across 40 years |
| Fifie (1 row) | 25 GT | 25-61 GT | three readings, small to large |
| Seine netter (2 rows) | 21 GT motor, 138 GT steam | 5-21 GT; 138-150 GT | two motor boats and two steam drifters |
| Ferry, CalMac double-ender (1 row) | 1,024 GT | +/- 5% | one ship, infobox figure |
| Handysize bulker (7 rows) | 12,600 GT | +/- 5% | two ships, ratio 0.613-0.644 |
| River boat by bridge (9 rows) | 6.2 x capacity | 3.1-9.3 | n = 5, report 56 |
| Cargo ship by bridge (2 rows) | 1.6 x capacity | 0.8-2.3 | n = 5, report 56; the steam end is 0.80 |
| Tub boat by bridge (4 rows) | 1.2 x capacity | 0.9-1.5 | n = 2, report 56 |
| MEASURED rows generally | the register figure | +/- 2% on the reading | a register reading, not an estimate |

**Structural assumptions.** (i) The transfer from a representative to a type assumes the pakset
object is the representative's size; where the pakset capacity contradicts that (the 50 t seine
netter against a 21 GT hull), the capacity is wrong, not the tonnage, and the row says so. (ii) The
register is a preservation register, so it over-represents surviving hulls: canal boats that
survive are the well-built and often the larger ones, and no ordinary wooden day boat of 1761
survives at all. (iii) The register's "Tonnage: Gross" is a single field with no statement of which
convention was applied; pre-1969 hulls are read as GRT and post-1969 as GT, which is right for the
build years here but is an inference. (iv) The Handysize ratio treats the pakset payload as
deadweight; if the payload excludes bunkers and stores, the true GT is a few per cent lower.

## 6. Gaps and routes

In order of value, with the exact route to each.

1. **The two Channel steamers (2 rows: 1853 paddle, 1886 screw).** No named South Eastern Railway
   or London, Brighton and South Coast Railway steamer of those years with a printed register
   tonnage was found. Route: the companies' fleet lists in the *Railway Magazine* or the
   South Eastern Railway archives at The National Archives (BT 107 board of trade registers,
   1853-1886), which are not digitised. **UNAVAILABLE.**
2. **The Tyne ferry of 1940 (1 row).** The Shields Ferry article names its post-war vessels
   (*Freda Cunningham* 1972, *Shieldsman* 1976, *Pride of the Tyne* 1993, *Spirit of the Tyne*
   2007) without tonnages, and the register's small ferries are 5-50 GT, far below a 313-passenger
   vessel. Route: the Tyne Improvement Commission ferry registers, or the *Shipping Today &
   Yesterday* feature that the article cites. **UNAVAILABLE.**
3. **Island (1973) and the FBM Hydrocat (1991) (2 rows).** Neither name identifies a registered
   vessel. Route: FBM Marine's Hydrocat class particulars, or the operator's certificate for the
   1973 small car ferry. **UNAVAILABLE.**
4. **PS Industry and ClydeSteamer (4 rows).** The 1814 hull could not be matched to a verifiable
   vessel, and the three Industry rows are one hull with three cargo fits, so a capacity bridge
   would price the same ship at 0.6, 22 and 38 GT. ClydeSteamer is recorded by the `.dat` itself as
   an unknown ship. Route: the Clyde shipping registers for 1814. **UNAVAILABLE.**
5. **The two early tugs (1816 paddle, 1841 iron screw).** No example survives and no measured
   tonnage for a named 1816 or 1841 tug was found. Report 25's 150-250 GT assumption describes a
   20th-century harbour tug and would overstate an 1816 tug three to five times, so it is not
   applied. Route: Lloyd's Register of Shipping 1841 for a named iron screw tug's burthen.
   **UNAVAILABLE.**
6. **Dogger and the six skiff wherries (7 rows).** A 17th-century dogger predates the register and
   an open rowed boat of under 5 tons is below the registration threshold. No route is likely
   to produce a measured figure. **UNAVAILABLE.**
7. **A wooden dumb barge and an 1860s steam seiner.** Both are priced from a different material or
   era (a 1920 steel barge, a 1930 drifter). A single register entry for each would replace the
   transfer. **UNAVAILABLE.**
8. **The 1.6 cargo bridge.** The Clyde cargo steamer and the schooner are the two rows where the
   bridge is doing work it was not fitted for. A named 1860s Clyde steamer and a named 1820-1860
   topsail schooner would replace both. **UNAVAILABLE.**

## 7. What the new figures change

The water class now has a gross tonnage for 177 of 216 objects. That matters for report 56's three
rates, which that report showed to be capital prices per gross ton: the ferry ladder
84.1 x GT^0.90, coastal cargo at GBP 35 a gross ton and inland at GBP 17 a gross ton, all in 1900
money. The inland and coastal groups are now the best covered in the class, which is where the flat
GBP 38,958 ship anchor was least appropriate: a 22 GT narrowboat and a 64 GT puffer now price
differently, and they should.

Two cautions belong with the figures. First, the coverage count is not the evidence count: 120 new
rows rest on 16 vessels, and the inland types are transferred across 60 to 150 years of building.
Second, the figures are hull sizes, so the workbook should apply a hull's gross tonnage once per
vessel, not once per cargo fit. If the ladder is applied per object, a nine-fit hull will be
charged nine times for the same steel.
