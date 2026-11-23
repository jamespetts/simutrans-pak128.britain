# Road vehicle maintenance and repair costs, 1750-1980

**Status**: research pass, 2026-11-23. Evidence and recommendation only; no `.dat` value was read
or changed. Every row below states the scope of the figure (what is inside it and what is not),
because in this domain the scope matters more than the number.

**Question**: what does it cost per vehicle-year to maintain a British bus, coach, lorry, van or
horse-drawn vehicle, by era and by size, so that the pakset's flat per-class maintenance figure can
be replaced by one that scales with the vehicle.

**The defect being fixed**: the pakset currently carries one flat maintenance figure per
vehicle-year for all buses (interpolated 1915, 1955, 1983) and one for all lorries (1936, 1958,
1968, 2016). It does not scale with vehicle size. This pass found measured evidence on both the
level and the scaling.

---

## 1. Method

- One Exa web search per turn. The query named the subject, the constraint, the date window and
  the source preference. Every page used was fetched and read; no figure is taken from a search
  snippet.
- The main source is the *Commercial Motor* archive (`archive.commercialmotor.com`). Its article
  **body text is machine-readable; its cost tables are page images and are not**. This single fact
  governs the whole pass: figures were taken only where an article states them in prose. Where an
  article says "see the accompanying table", the table values were not recoverable and the article
  is recorded as a dead end rather than guessed at.
- Figures are recorded in the source's own unit and nominal money of the stated year. No index,
  exchange rate or other conversion has been applied anywhere in §2 to §6.
- Confidence: **MEASURED** = taken from an operator's or company's own account; **STATED** = a
  trade-press table, costing or historian's figure, not an account; **INFERRED** = derived here,
  with the derivation shown.
- OCR damage. The archive's OCR drops the pound sign and mistranscribes digits frequently. Every
  figure read through damaged text is marked `[OCR]` with the reading adopted and, where possible,
  an arithmetic check. Three such checks are decisive and are shown in the notes:
  Edinburgh's repairs total is confirmed by the sum of the four working-expense heads; Glasgow's
  1932 fleet total is confirmed by the depreciation rate; the 1947 coach fleet total is confirmed
  by its own pence-per-mile.
- No Simutrans `.dat` cost, `runningcost`, `fixed_cost` or `upgrade_cost` value was read, and no
  pakset object price is used anywhere. The only pakset file consulted is `config/prices.tab`,
  and only in §7, as the deflator, with the factor shown for every row.

---

## 2. The evidence

### 2.1 Buses and coaches

| Year | Class | Figure as stated | Unit | Scope: included / excluded | Source | Conf. |
|---|---|---|---|---|---|---|
| 1913-14 | Wolverhampton Corporation motorbuses (3 vehicles in service for the year, 48,511 miles) | "the inclusive running costs to date are 8.44d. per mile run" | pence per bus-mile | **All-in working cost, not maintenance.** The article states the figure "already includes depreciation and maintenance". A tyre cost of 1.2d. per mile is mentioned in the same analysis but the passage does not say explicitly whether it is inside the 8.44d. Fuel, wages, licences and general expenses are all inside. | "Other People's Costs", *The Commercial Motor*, 25 June 1914, p. 10 | MEASURED (municipal accounts, reported) |
| 1914 | London General Omnibus Co., whole motorbus fleet (about 2,750 motor buses in March 1913) | "maintenance expenses, £1,009,782" for the year ended 31 December 1914 | £ per fleet-year | **Maintenance head only**, separate from "traffic expenses" £1,501,700 and "general expenses" £153,746. The company's accounting head had historically bundled "rolling stock, tyres, harness, yard stock and losses on realisation of horses and horse omnibuses" (1910 report), so **tyres and possibly yard stock are inside**. Workshop labour and materials are inside because the company built and repaired its own buses at Walthamstow. | "The Wheels of Industry", *The Commercial Motor*, 18 February 1915, p. 10; fleet from "The Vindication of the Motorbus", *The Commercial Motor*, 8 May 1913, p. 17 | MEASURED (company accounts, reported) |
| 1924-25 | Edinburgh Corporation: 88 passenger vehicles (73 motorbuses, 15 charabancs; 31-seat single-deckers, 2 double-deckers of 54 seats), 1,742,909 bus-miles | "the cost of repairs and maintenance £27,353 (chassis £13,671, bodies £5,900)" | £ per fleet-year | **Repairs and maintenance head.** Petrol is a separate head (£22,390), traffic expenses and general expenses separate. Chassis £13,671 and bodies £5,900 are stated. The two sub-heads sum to £19,571, leaving **£7,782 unallocated**; tyres at the stated 0.55d. per bus-mile would be about £3,993, so the residual is probably tyres plus repairs to plant and buildings. **Arithmetic check:** traffic £49,321 + general £8,037 + repairs £27,353 + petrol £22,390 = £107,101, the printed total working expenses. `[OCR: "1.27,353" read as £27,353]` | "Bus Results in Scottish Cities", *The Commercial Motor*, 4 August 1925, p. 9 | MEASURED (municipal report, reported) |
| 1927-28 | Keighley Corporation trolleybuses, 308,578 vehicle-miles | "general repairs and maintenance, £3,048 (2.371d.)" | pence per vehicle-mile | Separate head of account; power expenses (£2,414, 1.878d.) excluded; traffic and general expenses excluded. **Trolleybus, not motorbus.** Whether tyres are inside is not stated. | "Profitable Bus Operation at Keighley", *The Commercial Motor*, 14 August 1928, p. 67 | MEASURED (municipal accounts, reported) |
| 1931-32 | Glasgow Corporation, municipal fleet of 332 vehicles (mostly 51-seat double-deckers), 11,329,652 bus-miles | "cost of repairs and maintenance, £122,214" | £ per fleet-year | Repairs and maintenance head; motor spirit £102,538 is separate, so **tyres are inside** this head by default (no separate tyre line is printed). Traffic expenses £208,887 and general £35,940 separate. Depreciation £100,678 is a separate appropriation, not in the head. | "Growing Receipts on Glasgow's Buses", *The Commercial Motor*, 23 August 1932, p. 61 | MEASURED (municipal accounts, reported) |
| 1933-34 | Glasgow Corporation, 324 buses in stock (average 228 in use daily), 12,223,516 bus-miles | "The cost of maintenance during the year was £121,626" | £ per fleet-year | As above: tyres inside, motor spirit separate, depreciation separate. Capital expenditure on the bus system to date £791,710. | "The Latest News of Important Events", *The Commercial Motor*, 17 August 1934, p. 54 | MEASURED (municipal accounts, reported) |
| 1933-34 | Wolverhampton Corporation motorbuses | "maintenance and repairs £10,977" within working expenses of £54,124 (11.433d. per bus-mile) | £ per fleet-year | Repairs and maintenance head; power £11,743 separate; licences £3,727 separate. **Fleet number is not given in the extract**, so no per-vehicle figure can be formed. | "Municipal Bus Results from Many Centres", *The Commercial Motor*, 22 June 1934, p. 58 | MEASURED, but unusable alone |
| 1947 | One operator's fleet of 12 32-seat coaches, 500 miles per vehicle per week, 48 weeks = 24,000 miles a year each (288,000 fleet-miles) | Chassis maintenance: labour £800 + materials £2,400. Engine overhauls: £120 each, alternate years = £60 per vehicle per year = £720. Body overhaul: £200 each, alternate years = £100 per vehicle per year = £1,200. **Total £5,120, or 4.27d. per mile** | £ per fleet-year and pence per mile | **Everything except fuel, lubricants, tyres, licences, insurance and depreciation.** Chassis labour and materials, engine reconditioning and body overhaul. Engine work was done by the manufacturer at £120 an engine; body work costed separately at £200 an overhaul. Both on a two-year cycle. | "Calculating Costs for Workmen's Services", *The Commercial Motor*, 2 May 1947, p. 50 | MEASURED (operator's figures, reported) |
| 1948 | 26-seat bus and 26-seat coach, 400 miles per week assumed | "an average expectation of expenditure on this item is 2½d. per mile in the case of the bus against 1½d. per mile in the case of the coach" | pence per mile | Maintenance only. Tyres costed separately (bus 0.72d., coach 1d.), fuel and wages separate. **The same seating capacity gives a 67 per cent. higher maintenance figure for the bus than for the coach**; the article's reason is stop-start service. | "Coach and Bus Costs Compared", *The Commercial Motor*, 6 February 1948, pp. 37-38 | STATED (trade-press costing) |
| 1955 | Manchester municipal buses | 3.08d. per vehicle-mile | pence per bus-mile | "maintenance costs per vehicle-mile". The quoted passage does not say whether tyres or maintenance wages are inside. | Chambers report on London Transport (1955), quoted in "Councils to Run All Stage Services?", *The Commercial Motor*, 12 September 1958, p. 71 | STATED (official report, quoted) |
| 1955 | Glasgow municipal buses | 3.50d. per vehicle-mile | pence per bus-mile | As above. | As above | STATED |
| 1955 | Birmingham municipal buses | 3.56d. per vehicle-mile | pence per bus-mile | As above. | As above | STATED |
| 1955 | Liverpool municipal buses | 3.88d. per vehicle-mile | pence per bus-mile | As above. | As above | STATED |
| 1955 | London Transport buses | 4.36d. per vehicle-mile | pence per bus-mile | As above. The article's point is that London's bespoke buses did not deliver the expected maintenance saving. | As above, p. 68 | STATED |
| 1955 | All municipal undertakings, average | 2.82d. per vehicle-mile | pence per bus-mile | As above. | As above, p. 68 | STATED |
| 1961 | 31-seat petrol single-decker, initial outlay £2,900 complete, 600 miles per week (30,000 a year) | "Maintenance adds 3.26d. per mile" | pence per mile | Maintenance item of the Commercial Motor system: washing, servicing and major repairs. Fuel 5.75d., lubricants 0.22d., tyres 1.02d. and depreciation 2.94d. are separate. **Tyres excluded.** | "Passenger Vehicle Operation", *The Commercial Motor*, 22 December 1961, p. 41 | STATED (trade-press costing) |
| 1961 | 41-seat petrol single-decker, 600 miles per week | "Maintenance reckoned a little higher at 3.50d. per mile" | pence per mile | As above. Tyres 1.11d. separate; fuel 6.57d. | As above | STATED |
| 1964 | 31-seater petrol-engined coach, 400 miles per week | "Maintenance, inclusive of washing, servicing and major repairs, is estimated to cost 3.05d. per mile" | pence per mile | Washing, servicing, major repairs. Fuel 4.90d., lubricants 0.24d., tyres 1.04d., depreciation 4.53d. separate. | "Coach Operation", *The Commercial Motor*, 13 November 1964, p. 83 | STATED |
| 1964 | 44-seater oil-engined coach, 800 miles per week | 3.07d. per mile | pence per mile | As above. Fuel 4.19d., lubricants 0.28d., tyres 1.27d., depreciation 5.34d. separate. | As above | STATED |
| 1965 | London Transport bus fleet, 8,060 vehicles, overhauls every four years | "an average of £2,000 per bus once every four years, excluding units overhauled at Chiswick" | £ per overhaul | **Body and chassis overhaul only** — body lift, body repair, chassis repair, repaint, seat trimming, accident repairs. **Excludes** engine, gearbox and electrical unit overhauls, which went to Chiswick and were exchanged as reconditioned units. | "Rating the Routemaster", *The Commercial Motor*, 22 January 1965, p. 59 | MEASURED (London Transport's own figure, quoted) |
| 1969 | 41-seater oil-engined coach, 400 miles per week | 4.34d. per mile | pence per mile | Tables' maintenance item. | "New cost tables: the principal changes", *The Commercial Motor*, 17 July 1970, p. 55 | STATED |
| 1970 | 41-seater oil-engined coach, 400 miles per week | 4.77d. per mile | pence per mile | Tables' maintenance item; the journal records a 10 per cent. addition to the item for the year. Fuel 5.35d., lubricants 0.30d., tyres 1.33d., depreciation 8.24d. separate. | As above | STATED |
| 1982-83 | Merseyside Passenger Transport Executive bus fleet | "operating cost per mile is 183.1p, of which ... 53.7p for repairs and maintenance" | pence per mile | "Repairs and maintenance" as a separate head of the undertaking's own cost analysis, alongside traffic operations 98.3p, management 24.5p and asset utilisation 6.6p. Tyres not stated. **The head is 29 per cent. of total operating cost, roughly double the 13 per cent. of the 1961 trade costing, so it is on a wider basis than the Tables' maintenance item** (depot and works overheads are the likely contents). | "Private work pays off", *The Commercial Motor*, 21 January 1984, p. 23, reporting the PTE's 1982-83 annual report | MEASURED (undertaking's report, reported) |
| 1959 | 14-seat, 31-seat and 44-seat buses compared at 200, 400 and 600 miles per week | Maintenance costs are "lines 9, 14 and 19" of a table, and "increase as the average weekly mileage decreases ... because this item consists of two elements ... repair work, which varies directly with the mileage run, and ... servicing and washing, which are normally scheduled on a time basis" | not stated in text | Definitions given; **values are in a page image and were not recovered**. Recorded because it is the clearest statement of the fixed/variable split inside a bus maintenance figure. | "Hidden Subsidies in Rural Bus Services", *The Commercial Motor*, 2 January 1959, p. 62 | DEAD END for values |

**Derived from the table (per vehicle-year, nominal, computed here):**

- Edinburgh 1925: £27,353 / 88 = **£310.8 per vehicle-year**; chassis £155.4, bodies £67.0.
  Per bus-mile 3.767d. (chassis 1.883d., bodies 0.812d.). Annual mileage 19,806 per vehicle.
- Glasgow 1932: £122,214 / 332 = **£368.1 per vehicle-year**; 2.589d. per bus-mile; annual
  mileage 34,125 per vehicle.
- Glasgow 1934: £121,626 / 324 = **£375.4 per vehicle-year**; 2.388d. per bus-mile; annual
  mileage 37,727 per bus in stock.
- 1947 coach fleet: £5,120 / 12 = **£426.7 per vehicle-year**; 4.267d. per mile at 24,000 miles.
- LGOC 1914: £1,009,782 / 2,750 = **£367.2 per bus-year** (or £336.6 on 3,000 buses).
- Keighley trolleybus 1928: the printed 2.371d. per vehicle-mile is confirmed by the arithmetic
  (£3,048 × 240 / 308,578 = 2.370d.). Fleet size is not printed, so no per-vehicle-year figure
  can be formed.

**The single most important thing in this table** is that Edinburgh and Glasgow, eleven years
apart, have almost the same maintenance per bus-mile (3.77d. and 2.59d.) but very different
maintenance per vehicle-year (£311 and £368-375), because Glasgow buses ran nearly twice the annual
mileage. Any pakset conversion must fix the annual mileage explicitly.

### 2.2 Lorries and vans

| Year | Class | Figure as stated | Unit | Scope: included / excluded | Source | Conf. |
|---|---|---|---|---|---|---|
| 1933 | 2-ton van, "one of the less expensive type", net cost without tyres £270 | "The average cost of maintenance of a vehicle of this type is 0.88d. per mile"; owner-driver doing his own work 0.44d. | pence per mile | Full scheme: washing, polishing, greasing, adjustments, overhauls and service operations, "maintained either by a separate staff or by some outside contractor". Fuel 1.50d., oil 0.05d., tyres 0.40d., depreciation 0.54d. separate. **Tyres and depreciation excluded.** | "Problems of the Haulier and Carrier", *The Commercial Motor*, 31 March 1933, p. 58 | STATED (Tables of Operating Costs) |
| 1933 | Rigid six-wheeled steam wagon, 12-13 tons | "maintenance, 1.80d." per mile in the Tables | pence per mile | Tables' maintenance item; fuel 1.80d., oil 0.30d., tyres 1.60d., depreciation 1.73d. separate. | "Users' Figures Reveal Possibilities of Economy Latent in New Types", *The Commercial Motor*, 10 March 1933, p. 48 | STATED |
| 1933 | One owner's 11 steam wagons: a six-wheeled steamer's year | "repairs, £75" within depreciation £195, insurance and tax £73, wages £400, total £743 for 254 working days | £ per vehicle-year | The owner's own repair account. **Four mechanics maintained 12 wagons at £2 to £2 2s. per vehicle per week**, but the owner could not say whether that covered overheads. Fuel and tyres separate. | As above | MEASURED (operator's figures, reported) |
| 1933 | One owner's steam wagon, annual overhaul by the maker | "the maker to do that work annually at a cost ... varying from £40 to £70" | £ per overhaul | Complete annual overhaul by the manufacturer, one wagon. | As above | MEASURED (operator, reported) |
| 1934 | 1-ton lorry, cost £240 including tyres, 200-300 miles per week | "we are going to take the figure of 0.55d. per mile for maintenance from the Tables" | pence per mile | Tables' maintenance item. Petrol 0.87d., oil 0.07d., tyres 0.36d., depreciation 0.34d. separate. **Arithmetic check:** 0.87 + 0.07 + 0.36 + 0.55 + 0.34 = 2.19d., the printed total. | "Problems of the Haulier and Carrier", *The Commercial Motor*, 1 June 1934, p. 64 | STATED |
| 1934 | 2-ton lorry | "on maintenance to 0.75d. per mile"; tyres 0.45d., depreciation 0.50d. | pence per mile | Tables' maintenance item; tyres and depreciation separate. | "Problems of the Haulier", *The Commercial Motor*, 7 September 1934, p. 60 | STATED |
| 1936 | 2-ton van, 250 miles per week | "the cost of maintenance per mile ... is 0.94d. per mile, which is equivalent ... to £1 per week" | pence per mile and £ per week | 28 itemised operations from washing to overhauls; "minimum cost figures". **Arithmetic check:** 0.94d. × 250 = 235d. = 19s. 7d., printed as £1. `[OCR: ".21 per week" read as £1]` | "Does Maintenance by Drivers Pay?", *The Commercial Motor*, 10 January 1936, p. 40 | STATED (trade-press schedule) |
| 1936 | A vehicle (type not stated) over its life | Cumulative repair bill £295 over 92,000 miles; an overhaul in the second half of 1933 cost £253; "repair bills ... will often amount to over twice its original cost" | £ per vehicle-life | Repairs only; fuel, oil and tyres excluded from this cumulative figure. Depreciation and repair together 1.57d. per mile at 92,000 miles. | "When is a Replacement Economically Essential?", *The Commercial Motor*, 17 January 1936, p. 50 | MEASURED (operator's cost record, reported) |
| 1938 | Light lorry of 4-5 tons capacity, complete maintenance cycle over 45,000 miles | Retailer charges 1.087d. per mile; operator's own workshop 0.863d.; weighted average (nine of ten operators doing their own work) **0.887d., read as seven-eighths of a penny** | pence per mile | The whole maintenance cycle: six scheduled operations, major overhaul at 45,000 miles, plus varnish and touch-up at 15,000-mile intervals and a repaint at 45,000 miles. The repaint provision is "£20, which is equivalent to approximately 0.1d. per mile". **Tyres, fuel, oil and depreciation excluded.** | "And Now Maintenance in Pence Per Mile", *The Commercial Motor*, 16 September 1938, pp. 34-35 | STATED (trade-press costing, fully worked) |
| 1950 | 6-ton petrol-engined goods vehicle, 600 miles per week | Maintenance (e) "£3 1s. 6d." per week | £ per week | **Maintenance (e) only, i.e. repairs and overhauls.** Maintenance (d), routine washing/greasing/repainting, is a separate line, so the two together are higher. Fuel £5 5s. per week. | "Keeping Track of Rising Expenses", *The Commercial Motor*, 10 February 1950, p. 48 | STATED |
| 1950 | Engine overhaul of a goods vehicle at 48,000 miles; complete overhaul at 90,000 miles | "an engine overhaul and a certain amount of chassis repair, costing, say, £80"; a reconditioned engine "in the region of £120 to £140", taken as £130 | £ per overhaul | Engine only (the £80 also includes "a certain amount of chassis repair"). Complete engine overhaul at 90,000 miles: rebore or reline, crank grind, new bearings, valves and springs. Engine maintenance then works out at 0.54d. to 0.67d. per mile. | "What an Engine Costs in Upkeep", *The Commercial Motor*, 11 August 1950, p. 46 | STATED (worked example) |
| 1952 | 5-6 tonner, one operator's own record, 200 miles per week | "His maintenance figure, £2 4s. 3d. per week ... 2.65d. per mile" | pence per mile | The operator's total maintenance spending for the year, not itemised. | "A Comparison in Costing", *The Commercial Motor*, 28 November 1952, p. 54 | MEASURED (operator, quoted) |
| 1953 | 6-ton oil-engined goods vehicle, 400 miles per week | "maintenance, (d) and (e), 1.89d." | pence per mile | Both maintenance subheads: routine operations (d) **and** repairs and overhauls (e). Fuel, lubricants, tyres and depreciation separate. | "Making Easy Money?", *The Commercial Motor*, 24 July 1953, p. 61 | STATED |
| 1955 | 7-tonner, petrol-engined | "the cost of maintenance to be 2.00d. per mile" | pence per mile | Maintenance from the Tables plus a small percentage for cost increases since compilation. Fuel 4.00d., lubricants 0.25d., tyres 1.75d. separate. | "Check Your Operating Costs", *The Commercial Motor*, 9 December 1955, p. 70 | STATED |
| 1955 | 7-tonner, oil-engined | "Maintenance can be taken as being 10 per cent. less for the oiler, that is, 1.80d. per mile" | pence per mile | As above. **A direct diesel-versus-petrol maintenance differential at the same date and size.** | As above | STATED |
| 1958 | Petrol-engined 5-tonner, platform body, 500 miles per week | Maintenance 1.95d. per mile | pence per mile | Tables' maintenance item; fuel, lubricants, tyres, depreciation separate; wages and licences are standing charges. | "Ten Years of Rising Costs", *The Commercial Motor*, 3 January 1958, pp. 64-65 | STATED |
| 1958 | Maximum-load oil-engined rigid eight-wheeler, platform body, 800 miles per week | Maintenance 2.47d. per mile | pence per mile | As above. | As above | STATED |
| 1959 | AEC exchange engine for bus or lorry | "Basic charges ... vary from £205 to £285 for current models" | £ per exchange engine | Complete exchange unit with new liners, pistons, rings, main and big-end bearings, crankshaft reground; one year's guarantee. **A reconditioned unit price, not a fitted price.** | "Engine Rebuilding to Plan", *The Commercial Motor*, 10 April 1959, p. 72 | MEASURED (manufacturer's published charges) |
| 1963 | 7-ton oil-engined goods vehicle, platform body, 600 miles per week | Maintenance 2.71d. per mile | pence per mile | Tables' maintenance item; fuel, lubricants, tyres and depreciation itemised separately. | "Three-year Comparison of Costs", *The Commercial Motor*, 13 August 1965, p. 85 | STATED |
| 1965 | 7-ton oil-engined goods vehicle | Maintenance 2.85d. per mile | pence per mile | As above. | As above | STATED |
| 1966 | 5-ton diesel-engined goods vehicle, 600 miles per week | "Maintenance, inclusive of washing, servicing and major repairs adds 2.43d." | pence per mile | Washing, servicing, major repairs. Fuel 3.10d., lubricants 0.27d., tyres 1.31d., depreciation 1.62d. separate. | "Relationship to Cost", *The Commercial Motor*, 18 March 1966, p. 116 | STATED |
| 1966 | 7-ton goods vehicle | Maintenance 2.85d. per mile | pence per mile | As above. | As above | STATED |
| 1966 | 10-ton articulated goods vehicle | Maintenance 3.13d. per mile | pence per mile | As above. | As above | STATED |
| 1967 | 8-ton goods vehicle, 600 miles a week or over | Maintenance 3.44d. per mile | pence per mile | Tables' maintenance item; fuel 4.27d., lubricants 0.3d., tyres 1.83d., depreciation 1.86d. separate. | "How do the operating costs of a mass-produced [vehicle compare]", *The Commercial Motor*, 25 August 1967, p. 53 | STATED |
| 1967 | 9-ton goods vehicle | Maintenance 3.13d. per mile | pence per mile | As above; lower than the 8-tonner in the same answer and the source does not explain it. | As above | STATED |
| 1968 | 16-ton rigid eight-wheeled tipper or haulage vehicle, 400 miles per week | Maintenance 5.06d. per mile | pence per mile | Tables' maintenance item; fuel 7.31d., lubricants 0.33d., tyres 2.75d., depreciation 3.99d. separate. The journal warns "you may need to allow more for maintenance and tyres" on tipper work. | "Could you please give me details of", *The Commercial Motor*, 13 September 1968, p. 205 | STATED |
| 1968 | 16-ton articulated platform vehicle, 400 miles per week | Maintenance 5.06d. per mile | pence per mile | As above; identical to the rigid figure. | As above | STATED |
| 1969 | 7-ton goods vehicle, 600 miles per week | Maintenance 4.04d. per mile | pence per mile | Tables' maintenance item. | "New cost tables", *The Commercial Motor*, 10 July 1970, p. 41 | STATED |
| 1970 | 7-ton goods vehicle | Maintenance 4.45d. per mile | pence per mile | Tables' maintenance item; a 10 per cent. addition was made to the item for the year. | As above | STATED |
| 1970 | 16-ton-gross four-wheeled goods vehicle, platform body, 800 miles per week | Maintenance 4.66d. per mile | pence per mile | Tables' maintenance item; fuel 6.57d., lubricants 0.32d., tyres 2.23d., depreciation 2.68d. separate. | "The costing column: Those extras", *The Commercial Motor*, 11 September 1970, p. 198 | STATED |
| 1973 | Class not named in the passage | "CM Tables quote an average maintenance cost per mile of 3.36p" | pence per mile | Tables' maintenance item. | "It pays to monitor", *The Commercial Motor*, 20 July 1973, p. 47 | STATED |
| 1974 | Volvo F88 tractive unit with low-loader trailer, 38 tons gross, 700 miles per week | Maintenance 1.48p. per mile | pence per mile | Sits in a running-cost list with fuel 5.38, oil 0.30, tyres 1.63, depreciation 3.10. **Less than half the 1973 Tables average for a heavier vehicle**; probably treats maintenance partly as overhead. Not a continuation of the series. | "Q: Could you supply me with the operating costs of", *The Commercial Motor*, 17 May 1974, p. 53 | MEASURED (operator data, journal costing) |
| 2016 | 4-axle rigid tipper, 32 tonnes GVW, 55,000 miles a year | Maintenance £11,751 a year, 21.37 pence per mile | £ per vehicle-year and pence per mile | Maintenance as a separate running-cost line; fuel £28,182, tyres £1,877, VED, insurance and depreciation separate. | Freight Transport Association, *Managers' Guide to Distribution Costs*, October 2016, reproduced in CLOCS, *Investigating the Construction Industry's Use of HGV Types*, fig. 6 | STATED (FTA table) |
| 2016 | 44-tonne articulated vehicle, 70,000 miles a year | Maintenance tractor £7,290 a year (10.41 p/mile); trailer £4,002 (5.72 p/mile) | £ per vehicle-year and pence per mile | Maintenance split tractor/trailer; fuel, tyres, depreciation and VED separate. | As above, fig. 7 | STATED |

### 2.3 Overhauls, repaints and body work in money

| Year | Item | Figure | Scope | Source | Conf. |
|---|---|---|---|---|---|
| 1933 | Annual overhaul of a steam wagon by the maker | £40-£70 per overhaul | Complete annual overhaul, one wagon, by the manufacturer | CM 10 March 1933, p. 48 | MEASURED |
| 1936 | Heavy overhaul of an older goods vehicle | £253 for one overhaul | Not itemised; the article uses it as the point at which repair cost per mile turns upward | CM 17 January 1936, p. 50 | MEASURED |
| 1938 | Repaint and varnish of a 4-5 ton lorry | £20 per 45,000 miles (varnish and touch-up at 15,000 miles, repaint at 45,000) = about 0.1d. per mile | Paint and varnish only, over the cycle | CM 16 September 1938, p. 35 | STATED |
| 1947 | Engine reconditioning, 32-seat coach | £120 per engine, alternate years (about 48,000 miles) | Engine only, returned to the manufacturer | CM 2 May 1947, p. 50 | MEASURED |
| 1947 | Coach body overhaul | £200 per body, alternate years | Body only | As above | MEASURED |
| 1950 | Engine overhaul at 48,000 miles | "say £80", including "a certain amount of chassis repair" | Engine plus minor chassis work | CM 11 August 1950, p. 46 | STATED |
| 1950 | Complete engine overhaul / reconditioned engine at 90,000 miles | £120-£140, taken as £130 | Exchange reconditioned engine, fitted by a specialist | As above | STATED |
| 1959 | AEC exchange engine | £205-£285 basic charge for current models | Exchange unit, not fitted; one year's guarantee | CM 10 April 1959, p. 72 | MEASURED |
| 1965 | London Transport Aldenham bus overhaul | £2,000 per bus every four years (about £500 per bus-year) | Body and chassis overhaul and repaint; excludes engine, gearbox and electrical units | CM 22 January 1965, p. 59 | MEASURED |

**Overhaul intervals, which the pakset needs as much as the prices:**

| Year | Operator | Interval structure | Source |
|---|---|---|---|
| 1933 | Steam wagon owner, 12 wagons | Thorough overhaul once a year; painted every other year; boilers retubed every three years | CM 10 March 1933, p. 48 |
| 1938 | Trade-press schedule for a 4-5 ton lorry | Six scheduled operations; major overhaul and repaint at 45,000 miles | CM 16 September 1938, p. 35 |
| 1947 | 12-coach fleet | Engine and body each on a two-year cycle at 24,000 miles a year, i.e. about 48,000 miles | CM 2 May 1947, p. 50 |
| 1948 | Birkenhead Corporation | Tune-up dock 15,000-20,000 miles; top overhaul 30,000-40,000; full overhaul 120,000 miles; repaint every two years; teak bodies stripped every seven years | CM 23 April 1948, p. 38 |
| 1950 | Trade-press costing | Engine overhaul at 48,000 miles; complete overhaul at 90,000 miles | CM 11 August 1950, p. 46 |
| 1953 | Aberdeen Corporation | Light dock 5,000 miles; medium dock 50,000; overhaul 100,000-130,000 by type | CM 13 November 1953, p. 123 |
| 1957 | Eastern National (700 buses) | Inspection and adjustment every 5,000 miles; docking at 50,000; unit change or major overhaul at 150,000 or more | CM 10 May 1957, p. 42 |
| 1960 | Birmingham and Midland Motor Omnibus | Oil change 8,000 miles; A dock 16,000; B dock 48,000; C dock 96,000; D dock and repaint at 192,000 (two-yearly); top overhauls at 24,000 | CM 3 June 1960, p. 57 |
| 1965 | London Transport | Complete overhaul every four years on a strict time basis regardless of mileage; engine and gearbox units exchanged as required | CM 22 January 1965, p. 59 |

### 2.4 Horse-drawn vehicles

| Year | Vehicle | Figure as stated | Unit | Scope | Source | Conf. |
|---|---|---|---|---|---|---|
| 1760 | Stage coach, Manchester-London service (John Hanforth) | "a good coach cost about £100, lasted about three years, and declined in value to about £40 after one year"; "keeping the coaches and harness in repair cost about £210 per year" for three coaches | £ per coach-year | **Coaches and harness together**, three coaches and their harness for 42 horses. Per coach £70. The same account puts "coaches and harness" at 10 per cent. of total operating cost. Coaches were the second largest capital item after horses. | Dorian Gerhold, "John Hanforth and Manchester's first stage-coaches", *Transactions of the Historic Society of Lancashire and Cheshire* 156 (2007), pp. 155-166, reporting TNA E 134/8 Geo. III Easter 10 | MEASURED (Chancery and Exchequer evidence, reported) |
| 1820 | Private carriage, Sir Philip Musgrave, Edenhall | Coachmaker's bill for one year's repairs: £10 19s. 6d., less 12s. for old iron = £10 7s. 6d. | £ per vehicle-year | Repairs only: a new plate-glass light, two lamps, lining the fore carriage, cutting the wheel joints, 2 cwt of iron for the wheels, new pole leather, cleaning and blacking, and carriage to and from the coachmaker. A lightly used private carriage, not a public service vehicle. | John Dawson, Penrith, coachmaker's account and receipt, 23 November 1820, Cumbria Archives (Edenhall estate papers), transcribed at rumbutter.net | MEASURED (coachmaker's bill) |
| 1879 | London General Omnibus Co., about 600 omnibuses and 6,000 horses | Coachbuilding department: 190 men, "whose average wages are two hundred and fifty pounds a week"; "all the omnibuses ... are built and repaired" there; "the trade or cost price of an ordinary omnibus is one hundred and thirty pounds"; large three-horse omnibuses £200; "the ordinary time of wear is ten years"; wheels renewed entirely every three years; tyres last a few months | £ per week (department) | Labour only, and the department **built new omnibuses as well as repairing them**, so the £250 a week is not a repair cost. Per omnibus it is £21 13s. 4d. a year in wages if all of it were repairs, which it was not. Materials, paint and timber are additional and not stated. | Edmund Yates, *The Business of Pleasure* (1879), ch. IV, "Riding London: Of Omnibuses", via victorianlondon.org | MEASURED (journalist's authorised inquiry) with a scope warning |
| 1901 | London omnibus | "Each omnibus costs from £150 to £160, and lasts for about twelve years. It is renovated every year previous to being inspected by the police"; licence £2 a year and Inland Revenue tax 15s. | £ per vehicle (capital) and interval | Capital price and the fact of an **annual renovation**, whose cost is not given. | Henry Charles Moore, *Omnibuses and Cabs* (1901), ch. XI, Wikisource | STATED (contemporary book) |
| 1831 | Stage coach, Gurney's calculation | "wear and tear about £5 per horse per annum"; "a horse a mile is the present calculation for doing the work" | £ per horse-year | Vehicle wear and tear stated per horse, not per coach. At the stated one horse per mile and a 4-horse coach, this implies about £20 per coach-year for a coach costing about £100, i.e. 20 per cent. | *Report from the Select Committee on Steam Carriages* (1831), evidence of Goldsworthy Gurney, 5 August 1831 | STATED (witness's calculation) |

**Comment on the horse-drawn evidence.** The 1760 figure and the 1831 figure agree in order of
magnitude (70 per cent. and 20 per cent. of coach price per year) only if the 1760 £70 is read as
covering harness as well and the coach as being worked to destruction. The 1820 private-carriage
bill (£10 7s. 6d. on a carriage of perhaps £150-£200) is about 6 per cent. a year, which is the
light-use end. The spread is therefore 6 to 70 per cent., and it is a spread of **utilisation**,
not of accounting.

### 2.5 What the figures imply per vehicle-year and per mile

Nominal money, computed here from the rows above. Annual mileage is the source's own where stated.

| Year | Vehicle | £ per vehicle-year | Annual miles used | Pence per mile |
|---|---|---|---|---|
| 1914 | LGOC motorbus (all-in maintenance head) | 367.2 | not stated | not computable |
| 1925 | Edinburgh 31-seat single-decker | 310.8 | 19,806 | 3.767 |
| 1932 | Glasgow 51-seat double-decker | 368.1 | 34,125 | 2.589 |
| 1934 | Glasgow 51-seat double-decker | 375.4 | 37,727 | 2.388 |
| 1933 | 2-ton van | 57.2 | 15,600 | 0.88 |
| 1934 | 1-ton lorry | 29.8 | 13,000 | 0.55 |
| 1934 | 2-ton lorry | 48.8 | 15,600 | 0.75 |
| 1936 | 2-ton van | 50.9 | 13,000 | 0.94 |
| 1938 | 4-5 ton lorry | 73.9 | 20,000 (assumed) | 0.887 |
| 1947 | 32-seat coach | 426.7 | 24,000 | 4.267 |
| 1950 | 6-ton lorry, maintenance (e) only | 159.9 | 31,200 | 1.23 |
| 1958 | 5-ton lorry | 203.1 | 25,000 | 1.95 |
| 1958 | 8-wheel lorry | 411.7 | 40,000 | 2.47 |
| 1961 | 31-seat bus | 407.5 | 30,000 | 3.26 |
| 1961 | 41-seat bus | 437.5 | 30,000 | 3.50 |
| 1965 | LT bus, body/chassis overhaul only | 500.0 | not stated | not computable |
| 1966 | 5-ton lorry | 303.8 | 30,000 | 2.43 |
| 1966 | 7-ton lorry | 356.2 | 30,000 | 2.85 |
| 1966 | 10-ton artic | 391.2 | 30,000 | 3.13 |
| 1970 | 16-ton lorry | 776.7 | 40,000 | 4.66 |

---

## 3. How maintenance scales with vehicle size

### 3.1 Direct matched pairs

| Pair | Date | Small figure | Large figure | Size ratio | Maintenance ratio | Implied exponent |
|---|---|---|---|---|---|---|
| 1-ton lorry vs 2-ton lorry (both from the Tables, same year) | 1934 | 0.55d. | 0.75d. | 2.00 | 1.36 | **0.45** |
| 2-ton lorry vs 12-13 ton six-wheel steam wagon | 1933-34 | 0.75d. | 1.80d. | 6.25 | 2.40 | **0.48** |
| 5-ton vs 7-ton lorry (same article, same mileage) | 1966 | 2.43d. | 2.85d. | 1.40 | 1.17 | **0.47** |
| 7-ton vs 10-ton lorry (same article, same mileage) | 1966 | 2.85d. | 3.13d. | 1.43 | 1.10 | **0.26** |
| 5-ton vs 10-ton lorry, end to end | 1966 | 2.43d. | 3.13d. | 2.00 | 1.29 | **0.37** |
| 31-seat vs 41-seat bus (same article, same fuel, same mileage) | 1961 | 3.26d. | 3.50d. | 1.32 | 1.07 | **0.25** |
| 31-seat vs 44-seat coach | 1964 | 3.05d. | 3.07d. | 1.42 | 1.01 | **0.02**, confounded: petrol vs oil and 400 vs 800 miles per week |

The implied exponent is the elasticity of maintenance per mile with respect to payload or seating:
`ln(maintenance ratio) / ln(size ratio)`.

### 3.2 The trade press's own statement

The *Commercial Motor*'s costing writer stated in 1935, on the Tables' figures for **every petrol
vehicle from 7 cwt. to 7 tons**:

> "The first point of interest to note about Fig. 1 is how closely the relative importance of the
> various items adheres to what I might term a fixed relation. The rise in each item with the
> increase in load capacity compares closely to the total increase in operating costs. Each of the
> five items continues to bear the same relation to each and all of the others."

and, for the average across that range, "the expenditure on petrol ... is rather more than 40 per
cent. of the whole, or nearly double that of maintenance". For oil-engined vehicles of 3 to 7 tons,
maintenance is 28.8 per cent. of running cost, fuel 22.8 per cent. and depreciation 27.3 per cent.
(CM, 7 June 1935, p. 44.)

Read strictly, this says maintenance per mile rises **in proportion to total running cost**, and
that total running cost rises with capacity. It does not say maintenance rises in proportion to
capacity, and the matched pairs above show that it does not: the exponent is about 0.45 for goods
vehicles and about 0.25 for buses.

### 3.3 The counter-evidence

Two findings cut against a strong size effect and must be carried:

1. **The bus pairs are nearly flat.** A 41-seat bus costs 7 per cent. more to maintain per mile
   than a 31-seat bus; a 44-seat coach costs 0.7 per cent. more than a 31-seat coach. If the pakset
   applies a strong size multiplier to buses it will overshoot the measured range.
2. **Bodies are a smaller share than expected.** Edinburgh in 1925 split its repairs £13,671
   chassis to £5,900 bodies, i.e. the body is 30 per cent. of the maintenance of a 31-seat bus. A
   double-decker's extra deck therefore adds well under half as much again to the total, not double.

### 3.4 The answer to the pakset's question

Maintenance **does** scale with size, but **sub-proportionally**:

- goods vehicles: maintenance per mile ≈ size^**0.4** (fitted range 0.26-0.48, central 0.45 for
  payloads up to about 7 tons, flattening above 10 tons);
- buses and coaches: maintenance per mile ≈ seats^**0.25** (one clean pair; treat as 0.2-0.3).

Worked consequences, which are the numbers the pakset needs:

| Comparison | Per mile | Per vehicle-year, allowing for utilisation |
|---|---|---|
| 30 cwt van vs 7-ton lorry | (7 / 1.5)^0.4 = **1.85×** (at 0.45, 2.00×) | 13,000 vs 25,000 miles a year: **3.6× to 3.8×** |
| 32-seat single-decker vs 70-seat double-decker | (70 / 32)^0.25 = **1.22×** | 30,000 vs 35,000 miles a year: **1.42×** |
| 5-ton vs 16-ton lorry | (16 / 5)^0.4 = **1.63×** | 25,000 vs 40,000 miles a year: **2.6×** |

So the pakset's flat figure is wrong in two ways at once. It is wrong because maintenance per mile
rises with size, and it is wrong again because big vehicles run more miles a year. The combined
error between a 30 cwt van and a 7-ton lorry is nearly a factor of four.

---

## 4. Recommended maintenance per vehicle-year

### 4.1 Why these are given in 1900 pounds, and the one conversion used

The pakset needs a 1900-pound figure, so the nominal figures are deflated here. The deflator is the
`general` series in `config/prices.tab` (1900 = 100), which is the series the cost-balancing
workbooks already use. **This is the only conversion in this document and it is applied nowhere in
§2, §3 or §5.** The factors used are:

| Year | 1760 | 1820 | 1831 | 1879 | 1914 | 1925 | 1932 | 1934 | 1936 | 1938 | 1947 | 1950 | 1953 | 1955 | 1958 | 1961 | 1965 | 1966 | 1969 | 1970 | 1982 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index | 61 | 127 | 119 | 99 | 107 | 202 | 176 | 172 | 174 | 183 | 314 | 359 | 440 | 468 | 526 | 552 | 635 | 660 | 747 | 795 | 3483 |
| Divide by (index ÷ 100) | 0.61 | 0.79 | 0.84 | 0.99 | 0.93 | 0.50 | 0.57 | 0.58 | 0.57 | 0.55 | 0.32 | 0.28 | 0.23 | 0.21 | 0.19 | 0.18 | 0.16 | 0.15 | 0.13 | 0.13 | 0.029 |

Two cautions. First, this is a consumer price index, not a vehicle or repair-cost index; road
vehicle costs and repair wages did not track it exactly, and in the 1970s bus costs ran well ahead
of it. Second, the figures below are therefore **1900-price levels of a nominal bill**, not a
statement that a 1960 operator's real burden equalled a 1900 operator's.

### 4.2 Deflated evidence, which is what the recommendation is built on

| Year | Vehicle | Nominal £/vehicle-year | 1900 £/vehicle-year | 1900 pence per mile |
|---|---|---|---|---|
| 1760 | Stage coach, coaches and harness | 70.0 | **114.8** | — |
| 1914 | LGOC motorbus, incl. tyres | 367.2 | **343.2** | — |
| 1925 | Edinburgh 31-seat single-decker | 310.8 | **153.9** | 1.86 |
| 1932 | Glasgow 51-seat double-decker | 368.1 | **209.1** | 1.47 |
| 1934 | Glasgow 51-seat double-decker | 375.4 | **218.3** | 1.39 |
| 1934 | 1-ton lorry | 29.8 | **17.3** | 0.32 |
| 1933 | 2-ton van | 57.2 | **33.3** | 0.51 |
| 1934 | 2-ton lorry | 48.8 | **28.3** | 0.44 |
| 1936 | 2-ton van | 50.9 | **29.3** | 0.54 |
| 1938 | 4-5 ton lorry | 73.9 | **40.4** | 0.49 |
| 1933 | 12-13 ton steam wagon (Tables) | 270.0 at 36,000 miles | **157.0** | 1.05 |
| 1933 | 12-13 ton steam wagon (owner's repairs) | 75.0 | **43.6** | 0.29 |
| 1947 | 32-seat coach | 426.7 | **135.9** | 1.36 |
| 1950 | 6-ton lorry, (e) only | 159.9 | **44.5** | 0.34 |
| 1953 | 6-ton lorry | 163.8 | **37.2** | 0.43 |
| 1955 | Municipal bus average, 2.82d. at 30,000 miles | 352.5 | **75.3** | 0.60 |
| 1955 | London bus, 4.36d. at 38,000 miles | 690.3 | **147.5** | 0.93 |
| 1958 | 5-ton lorry | 203.1 | **38.6** | 0.37 |
| 1958 | 8-wheel lorry | 411.7 | **78.3** | 0.47 |
| 1961 | 31-seat bus | 407.5 | **73.8** | 0.59 |
| 1961 | 41-seat bus | 437.5 | **79.3** | 0.63 |
| 1965 | LT bus, body and chassis overhaul only | 500.0 | **78.7** | — |
| 1966 | 5-ton lorry | 303.8 | **46.0** | 0.37 |
| 1966 | 7-ton lorry | 356.2 | **54.0** | 0.43 |
| 1966 | 10-ton lorry | 391.2 | **59.3** | 0.47 |
| 1969 | 41-seat coach, 20,000 miles | 361.7 | **48.4** | 0.58 |
| 1970 | 16-ton lorry | 776.7 | **97.7** | 0.59 |
| 1982 | Merseyside bus, 53.7p. at 40,000 miles | 21,480 | **616.7** | 1.54 |

The 1982 row is included for completeness and **is not used**. At 1.54d. per mile in 1900 money it
is two and a half times the 1961 bus figure and above every other bus and coach row, which cannot be
the same quantity: the PTE's "repairs and maintenance" head is 29 per cent. of operating cost against
13 per cent. in the 1961 trade costing, so it carries depot and works overheads the Tables exclude.
It is a different accounting object.

### 4.3 The recommendation

Per vehicle-year, 1900 pounds. "Basis" names the anchor and the arithmetic.

| Class | Era | Recommended £/vehicle-year (1900) | Range | Basis |
|---|---|---|---|---|
| Horse stage coach (4-horse, long-distance) | 1750-1830 | **115** | 90-140 | 1760: £70 per coach-year for coaches and harness (Gerhold); the index is 61, so £70 ÷ 0.61 = £114.8. The £70 includes harness for 42 horses, so it is an upper bound for the vehicle alone |
| Horse omnibus (2-horse, London) | 1830-1900 | **25** | 15-35 | 1879: coachbuilding wages £250 a week for 600 omnibuses = £21.7 per omnibus-year, labour only; materials and paint add perhaps a third. Consistent with the 1901 statement of an annual renovation on a £150-160 omnibus lasting 12 years |
| Horse goods van or cart | 1750-1900 | **15** (INFERRED) | 10-25 | No measured figure. Scaled from the omnibus at (1 horse / 2 horses)^0.4 ≈ 0.76, and from the smaller body. This is the weakest row in the table |
| Bus, single-deck 30-34 seats | 1900-1918 | **210** | 160-340 | 1914 LGOC £367 per bus incl. tyres × 0.93 = £343; less tyres at roughly 0.8-1.0d. per mile (about £100-125 a year) gives £220-245. The 1925 Edinburgh figure deflated (£154) is the lower bound. Central value set at 210 |
| Bus, single-deck 30-45 seats | 1919-1939 | **175** | 140-230 | 1925 Edinburgh £311 × 0.50 = £154; Glasgow's per-mile figure applied to a single-decker's lower mileage gives about £175. Upper bound is Glasgow deflated |
| Bus, double-deck 50-56 seats | 1919-1939 | **210** | 180-230 | 1932 Glasgow £368 × 0.57 = £209; 1934 £375 × 0.58 = £218 |
| Bus, single-deck | 1940-1959 | **80** | 60-110 | 1955 all-municipal 2.82d. × 30,000 miles = £352.5 × 0.21 = £75; Manchester 3.08d. gives £81; the range is the four undertakings' 2.82-3.88d. |
| Bus, double-deck | 1940-1959 | **145** | 115-160 | 1955 London 4.36d. × 38,000 = £690 × 0.21 = £148. London's cost level is itself high, so the size effect alone is smaller than the 1.9:1 this implies; 145 is the upper end of a defensible band |
| Coach, 32-44 seats | 1940-1959 | **135** | 100-160 | 1947 measured £426.7 × 0.32 = £136, at 24,000 miles a year |
| Bus, single-deck | 1960-1980 | **75** | 60-95 | 1961 measured £407.5 × 0.18 = £74; 41-seater £437.5 × 0.18 = £79 |
| Bus, double-deck | 1960-1980 | **110** (INFERRED) | 85-140 | Aldenham 1965 £500 a year × 0.16 = £79 for body and chassis overhaul alone; adding engine, gearbox and electrical units in proportion to the 1961 maintenance split gives about £110. Not a measured total |
| Coach, 32-44 seats | 1960-1980 | **60** | 45-80 | 1969 4.34d. × 25,000 miles = £452 × 0.13 = £59; 1970 4.77d. gives £65 |
| Van, 10 cwt to 1 ton | 1900-1918 | **20** (INFERRED) | 15-25 | No measured figure. Back-cast from 1934 (£17) allowing for the pre-1920 penalty in tyres, roads and workshop practice |
| Van, 10 cwt to 1 ton | 1919-1939 | **17** | 14-22 | 1934 1-ton: 0.55d. × 13,000 miles = £29.8 × 0.58 = £17.3 |
| Van, 10 cwt to 1 ton | 1940-1959 | **12** (INFERRED) | 9-16 | 1958 5-ton £38.6 × (1/5)^0.4 = 0.53, times 13,000/25,000 miles = £10.6; the 1953 6-ton basis gives £11.4 |
| Van, 10 cwt to 1 ton | 1960-1980 | **11** (INFERRED) | 9-15 | 1966 5-ton £46.0 × 0.53 × 13,000/30,000 = £10.6. The real fall from the 1930s is consistent with the bus series |
| Lorry, 30 cwt to 3 tons | 1900-1918 | **30** (INFERRED) | 22-40 | No measured figure; between the van and the 1919-39 lorry |
| Lorry, 30 cwt to 3 tons | 1919-1939 | **30** | 25-38 | 1933 0.88d. × 15,600 = £57.2 × 0.58 = £33; 1934 0.75d. gives £28; 1936 0.94d. × 13,000 gives £29 |
| Lorry, 30 cwt to 3 tons | 1940-1959 | **20** (INFERRED) | 17-30 | 1958 5-ton £38.6 × (2.5/5)^0.4 = 0.758, times 15,600/25,000 miles = £18.3; the 1953 6-ton basis gives £19.6 |
| Lorry, 30 cwt to 3 tons | 1960-1980 | **20** (INFERRED) | 17-30 | 1966 5-ton £46.0 × 0.758 × 15,600/30,000 = £18.1. The 1930s figure is higher because real maintenance per mile fell sharply between the two dates |
| Lorry, 5-7 tons | 1900-1918 | **40** (INFERRED) | 30-50 | No measured figure |
| Lorry, 5-7 tons | 1919-1939 | **40** | 33-48 | 1938 measured cycle 0.887d. × 20,000 = £73.9 × 0.55 = £40.4. This is the best-founded lorry figure of the era because the source shows the whole cycle |
| Lorry, 5-7 tons | 1940-1959 | **40** | 32-48 | 1958 5-ton 1.95d. × 25,000 = £203 × 0.19 = £38.6; 1953 6-ton £164 × 0.23 = £37 |
| Lorry, 5-7 tons | 1960-1980 | **52** | 45-65 | 1966 5-ton £304 × 0.15 = £46; 7-ton £356 × 0.15 = £54; 1970 7-ton 4.45d. × 30,000 = £556 × 0.13 = £72 (upper bound) |
| Lorry, 8-16 tons | 1900-1918 | **60** (INFERRED) | 45-80 | No measured figure |
| Lorry, 8-16 tons | 1919-1939 | **80** | 44-157 | The steam wagon is the only heavy vehicle measured: the Tables' allowance gives £157 deflated, the owner's own repairs £44. An oil-engined heavy lorry of the late 1930s would sit between; 80 adopted |
| Lorry, 8-16 tons | 1940-1959 | **78** | 60-95 | 1958 maximum-load eight-wheeler 2.47d. × 40,000 = £411.7 × 0.19 = £78.3 |
| Lorry, 8-16 tons | 1960-1980 | **80** | 62-98 | 1968 16-ton 5.06d. × 20,800 = £438 × 0.13 = £62; 1970 16-ton 4.66d. × 40,000 = £777 × 0.13 = £98. The spread is the annual-mileage assumption, not the maintenance rate |

**How to use the table.** The per-vehicle-year figure embeds an annual mileage. If the pakset's
vehicles run a different annual mileage, use the 1900 pence-per-mile column in §4.2 instead:
`£ per vehicle-year = pence per mile × annual miles / 240`. The two cleanest per-mile anchors in
1900 money are 0.32-0.54d. for a 1-2 ton lorry in the 1930s and 0.59-0.63d. for a 31-41 seat bus
in 1961.

**A structural alternative worth putting to the user.** Maintenance as a share of purchase price is
much more stable across eras than maintenance in pounds (see §5). If the pakset's capital values are
rebased first, maintenance could be set as a percentage of each vehicle's own capital cost, which
would remove the size problem automatically, because purchase price already scales with size. The
measured share is about 12-21 per cent. a year for motor road vehicles, with a mild downward taper
for large vehicles.

---

## 5. Maintenance as a share of purchase price

| Year | Vehicle | Annual maintenance | Purchase price | Share per year | Basis |
|---|---|---|---|---|---|
| 1760 | Stage coach | £70 (coaches and harness) | £100 | **70%** | Gerhold; the coach lost value to £40 in the first year, so repair and depreciation together were about 130% of first cost in year one |
| 1820 | Private carriage | £10 7s. 6d. | not stated (perhaps £150-200) | **about 6%** (INFERRED) | Coachmaker's bill; the price is not in the source |
| 1831 | Stage coach | £20 per coach (4 horses at £5) | about £100 | **20%** | Gurney's calculation, per horse converted to per coach |
| 1879 | London omnibus | £21.7 labour only | £130 | **17%** labour only | Yates; the department also built new omnibuses, so the true repair share is lower and the materials share unstated |
| 1914 | LGOC motorbus | £367 | not stated in the source; about £1,250 each on the road in 1907 ("800 motor-omnibuses ... had cost altogether to put on the road something like one million sterling") | **25-30%** (INFERRED) | Both figures are London and seven years apart; the price includes spare parts and putting the fleet on the road |
| 1925 | Edinburgh 31-seat bus | £311 | about £1,075 for a complete 24-30 seat bus in 1928 | **29%** | Price is a different year and a slightly smaller vehicle; treat as an upper bound |
| 1932 | Glasgow 51-seat double-decker | £368 | £1,733 (from the stated 17.5% depreciation charge of £100,678 on the bus fleet) | **21%** | Both figures are from the same accounts, which makes this the cleanest bus ratio in the file |
| 1934 | Glasgow 51-seat double-decker | £375 | £2,443 (capital expenditure £791,710 over 324 buses, including premises and plant) | **15%** | Capital includes land and buildings, so the true vehicle share is higher than 15% |
| 1933 | 2-ton van | £57.2 | £270 net of tyres | **21%** | Both from the same article |
| 1934 | 1-ton lorry | £29.8 | £240 including tyres | **12%** | Both from the same article |
| 1933 | 12-13 ton steam wagon | £75 repairs | £975 (from £195 depreciation over five years) | **8%** | Owner's accounts |
| 1938 | 4-5 ton lorry | £73.9 at 20,000 miles | not stated | — | — |
| 1947 | 32-seat coach | £426.7 | not stated | — | — |
| 1961 | 31-seat bus | £407.5 | £2,900 | **14%** | Both from the same article; the cleanest motor bus ratio |
| 1965 | LT bus, body and chassis overhaul only | £500 | not stated | — | — |
| 1966 | 7-ton lorry | £356 | not stated | — | — |

**Findings.**

1. For motor road vehicles the annual maintenance bill is **12 to 21 per cent. of purchase price**,
   with the 1932 Glasgow ratio (21 per cent.) and the 1961 bus ratio (14 per cent.) measured inside
   a single set of accounts on both sides.
2. Horse-drawn vehicles span **6 per cent. (private carriage) to 70 per cent. (stage coach worked to
   destruction)**, and the driver of the difference is utilisation, not construction.
3. The share **falls as vehicles get larger within an era**: 1-ton lorry 12 per cent., 2-ton lorry
   21 per cent. — but the 1-ton lorry in that pair cost £240 against £270 for the 2-tonner, so the
   price ratio, not the maintenance ratio, is doing most of the work. This is not evidence of a size
   taper in the share.
4. The 1936 trade statement that lifetime repair bills "will often amount to over twice [the
   vehicle's] original cost" is consistent with a 12-21 per cent. annual share over a 10-15 year
   life.

---

## 6. Dead ends and things not found

1. **The Commercial Motor cost tables themselves are page images.** Every "Tables of Operating
   Costs" article reproduces the table as an image with no machine-readable text, so the individual
   line values (licence, insurance, wages, rent and rates, fuel, lubricants, tyres, maintenance,
   depreciation) cannot be read from the archive even where the surrounding article is legible. The
   only values recovered are those the article states in prose. This blocked: the 1925 all-types
   table, the 1926 Morris 12-cwt van table, the Bent's Brewery 1925 fleet tables (4-ton and 5-ton
   Leylands, which would have been the best inter-war per-vehicle-year repair figures), the 1935
   Table I of 7 cwt to 7 tons, and the 1959 14/31/44-seat comparison.
2. **No measured pre-1914 motor bus maintenance figure.** The 1905-1914 material gives all-in
   running costs (Eastbourne 10.67d. per car-mile including capital charges; Bath 7.96d. in 1905;
   Sheffield 8.779d. in 1913-14 including 20 per cent. depreciation; Wolverhampton 8.44d. in
   1913-14 including depreciation) but never isolates maintenance. The London General accounts
   before 1914 bury maintenance inside a combined "omnibuses, harness, yard stock and fixtures"
   figure. The 1914 LGOC maintenance head is the only pre-war figure obtained.
3. **No municipal bus return equivalent to the tram returns.** The Ministry of Transport annual
   returns cover tramways and trackless trolleys, not omnibuses; Hansard (9 March 1926) confirms
   "No official return of omnibus services run by local authorities is issued". There is therefore
   no national per-bus-mile maintenance series to set beside the tram series in
   `vehicle-cost/tram-maintenance.md`.
4. **No horse-drawn goods vehicle repair account.** The 1760 coach, the 1820 private carriage and
   the 1879 omnibus workshop are passenger vehicles. No carrier's, brewer's or railway cartage
   account with a vehicle repair line was found.
5. **No 1900-1918 lorry maintenance figure.** Motor lorries were too few before 1914 for the trade
   press to carry a maintenance rate for them, and the 1914-18 war years are absent from the
   accessible material.
6. **The 1978 NBC/Maidstone bus trial was not re-found**, as instructed. It remains the only
   four-type bus comparison in the 1970s.
7. **No bus per-vehicle-year figure for 1940-1959 from a single operator's accounts.** The 1955
   Chambers figures are per bus-mile only, so the per-vehicle-year value in §4.3 depends on an
   assumed annual mileage.
8. **The 1982-83 Merseyside figure is not comparable** and is excluded from the recommendation;
   its "repairs and maintenance" head is on a wider basis than any other figure here.
9. **A 1913-14 Wolverhampton total of 8.44d. per bus-mile** is the only complete pre-war account
   found, but it cannot be decomposed into maintenance.

---

## 7. Sources

1. "Motor Omnibus Costs", *The Commercial Motor*, 22 June 1905, p. 1.
   https://archive.commercialmotor.com/article/22nd-june-1905/1/motor-omnibus-costs
2. "The Vindication of the Motorbus", *The Commercial Motor*, 8 May 1913, p. 17.
   https://archive.commercialmotor.com/article/8th-may-1913/19/the-vindication-of-the-motorbus
3. "Other People's Costs", *The Commercial Motor*, 25 June 1914, p. 10.
   https://archive.commercialmotor.com/article/25th-june-1914/10/other-people-s-costs
4. "The Wheels of Industry" (L.G.O.C. accounts), *The Commercial Motor*, 18 February 1915, p. 10.
   https://archive.commercialmotor.com/article/18th-february-1915/10/the-wheels-of-industry
5. "London General Omnibus Co.'s Accounts and Balance Sheet", *The Commercial Motor*, 1 December
   1910, p. 7. (For the composition of the maintenance head.)
   https://archive.commercialmotor.com/article/1st-december-1910/7/london-general-omnibus-cos-accounts-and-balance-sh
6. "Bus Results in Scottish Cities", *The Commercial Motor*, 4 August 1925, p. 9.
   https://archive.commercialmotor.com/article/4th-august-1925/10/bus-results-in-scottish-cities
7. "Profitable Bus Operation at Keighley", *The Commercial Motor*, 14 August 1928, p. 67.
   https://archive.commercialmotor.com/article/14th-august-1928/67/profitable-bus-operation-at-keighley
8. "Growing Receipts on Glasgow's Buses", *The Commercial Motor*, 23 August 1932, p. 61.
   https://archive.commercialmotor.com/article/23rd-august-1932/61/growing-receipts-on-glasgows-buses
9. "Users' Figures Reveal Possibilities of Economy Latent in New Types", *The Commercial Motor*,
   10 March 1933, p. 48.
   https://archive.commercialmotor.com/article/10th-march-1933/48/users-figures-reveal-possibilities-of-economy-late
10. "Problems of the Haulier and Carrier", *The Commercial Motor*, 31 March 1933, p. 58.
    https://archive.commercialmotor.com/article/31st-march-1933/58/problems-of-the
11. "Problems of the Haulier and Carrier", *The Commercial Motor*, 1 June 1934, p. 64.
    https://archive.commercialmotor.com/article/1st-june-1934/64/problems-of-the
12. "Municipal Bus Results from Many Centres", *The Commercial Motor*, 22 June 1934, p. 58.
    https://archive.commercialmotor.com/article/22nd-june-1934/58/municipal-bus-results-from-many-centres
13. "The Latest News of Important Events" (Glasgow), *The Commercial Motor*, 17 August 1934, p. 54.
    https://archive.commercialmotor.com/article/17th-august-1934/54/-the-latest-news-of-important-events
14. "Problems of the Haulier", *The Commercial Motor*, 7 September 1934, p. 60.
    https://archive.commercialmotor.com/article/7th-september-1934/61/problems-of-the
15. "The Highway to Low Costs", *The Commercial Motor*, 7 June 1935, p. 44.
    https://archive.commercialmotor.com/article/7th-june-1935/45/the-highway-to-low-costs
16. "Does Maintenance by Drivers Pay?", *The Commercial Motor*, 10 January 1936, p. 40.
    https://archive.commercialmotor.com/article/10th-january-1936/40/does-maintenance-by-drivers-pay
17. "When is a Replacement Economically Essential?", *The Commercial Motor*, 17 January 1936, p. 50.
    https://archive.commercialmotor.com/article/17th-january-1936/51/when-is-a-replacement-economically-essential
18. "And Now Maintenance in Pence Per Mile", *The Commercial Motor*, 16 September 1938, pp. 34-35.
    https://archive.commercialmotor.com/article/16th-september-1938/35/and-now-maintenance-in-ence-per-mile
19. "Calculating Costs for Workmen's Services", *The Commercial Motor*, 2 May 1947, p. 50.
    https://archive.commercialmotor.com/article/2nd-may-1947/50/calculating-costs-for-workmens-services
20. "The Birkenhead Deal", *The Commercial Motor*, 23 April 1948, p. 38.
    https://archive.commercialmotor.com/article/23rd-april-1948/38/lbirkenh-d-deal
21. "What an Engine Costs in Upkeep", *The Commercial Motor*, 11 August 1950, p. 46.
    https://archive.commercialmotor.com/article/11th-august-1950/46/what-an-engine-costs
22. "Social Influences on Aberdeen's Transport", *The Commercial Motor*, 13 November 1953, p. 123.
    https://archive.commercialmotor.com/article/13th-november-1953/123/social-influences-on-aberdeens-transport
23. "Overhauling 18 Buses at a Time", *The Commercial Motor*, 10 May 1957, p. 42.
    https://archive.commercialmotor.com/article/10th-may-1957/42/overhauling-18-buses-at-a-time
24. "Engine Rebuilding to Plan", *The Commercial Motor*, 10 April 1959, p. 72.
    https://archive.commercialmotor.com/article/10th-april-1959/72/engine-rebuilding-to-plan
25. "Hidden Subsidies in Rural Bus Services", *The Commercial Motor*, 2 January 1959, p. 62.
    https://archive.commercialmotor.com/article/2nd-january-1959/62/hidden-subsidies-in-rural-bus-services
26. "Maintenance 'As Required' is Best", *The Commercial Motor*, 3 June 1960, p. 57.
    https://archive.commercialmotor.com/article/3rd-june-1960/56/tenance-as-required-e-best
27. "Passenger Vehicle Operation", *The Commercial Motor*, 22 December 1961, p. 41.
    https://archive.commercialmotor.com/article/22nd-december-1961/42/passenger-vehicle-operation
28. "Rating the Routemaster", *The Commercial Motor*, 22 January 1965, p. 59.
    https://archive.commercialmotor.com/article/22nd-january-1965/59/ating-the-routemaster
29. Dorian Gerhold, "John Hanforth and Manchester's first stage-coaches", *Transactions of the
    Historic Society of Lancashire and Cheshire* 156 (2007), pp. 155-166, reporting TNA E 134/8
    Geo. III Easter 10 and C 12/2042/6. https://www.hslc.org.uk/wp-content/uploads/2018/01/156-8-Gerhold.pdf
30. Edmund Yates, *The Business of Pleasure* (London, 1879), ch. IV, "Riding London: Of Omnibuses".
    https://victorianlondon.org/publications5/business-04.htm
31. Henry Charles Moore, *Omnibuses and Cabs: Their Origin and History* (London, 1901), ch. XI.
    https://en.wikisource.org/wiki/Omnibuses_and_Cabs/Part_I/Chapter_XI
32. John Dawson, coachmaker, Penrith, account and receipt to Sir Philip Musgrave, 23 November 1820,
    Edenhall estate papers. Transcribed at
    http://www.rumbutter.net/cumb-res-edenhall-2/1820-11-23-01-detailed-coachmakers-account-for-repairs.html
33. *Report from the Select Committee on Steam Carriages* (1831), evidence of Goldsworthy Gurney,
    5 August 1831. https://en.wikisource.org/wiki/Report_from_the_Select_Committee_on_Steam_Carriages/Gurney2
34. Ministry of Transport, *Tramways and Light Railways (Street and Road) and Trackless Trolley
    Undertakings: Annual Return for 1930-31* (HMSO, 1931), for the confirmation that the omnibus
    return did not exist. https://www.ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf
35. *Hansard*, HC Deb 9 March 1926, vol. 192, cc. 2097-8, "Municipal Tramways and Omnibuses".
    https://api.parliament.uk/historic-hansard/commons/1926/mar/09/municipal-tramways-and-omnibuses

Rows taken from the existing knowledge base and reused here (source records there):
`New/ai/vehicle-cost/published-maintenance.md` for the 1948 bus and coach, the 1955 Chambers
figures, the 1950/1952/1953/1955/1958 lorry figures, the 1963-1974 lorry series and the 1969/1970
coach figures; `New/ai/vehicle-cost/road-maintenance-1959-2016.md` for the Merseyside 1982-83,
FTA 2016 and 1974 Volvo figures.
