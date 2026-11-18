---
status: draft
verified: New ex-15 @ 8d0603d81
---
# Ship maintenance costs

**Covers**: published repair, maintenance and dry-docking costs for ships, 1849 to 2026, with the
basis and denominator of each figure. Parent: [vehicle-cost-evidence](../vehicle-cost-evidence.md).
Inland boats are in [inland-boat-maintenance](inland-boat-maintenance.md).

# Ship and inland boat maintenance and repair costs — evidence file

Compiled 2026-11-17. Scope: maintenance and repair costs for sea-going ships (c.1800-2026) and
for inland and canal boats (c.1750-1960). Figures are recorded as the source states them. No
conversion, no deflation, no derived ratios except where a line is marked `[COMPUTED]`.

Conventions used in this file:

- `[P]` = primary (the document is the record itself: minute, account book, statute, regulation,
  company filing). `[S]` = secondary (a study, survey or compilation).
- "Spend" = money actually incurred. "Reserve" or "provision" = an accounting allocation that is
  not money spent in the period. The two are never combined in a row of this file.
- Where a source separates hull from machinery, the split is stated. Where it does not, the row
  says "not separated".
- Verification status is stated for each group. One group rests on a search-provider extraction of
  a PDF that could not be opened directly; it is marked `[UNVERIFIED EXTRACTION]` and is also
  flagged in the Assessment.

The file contains 51 numbered entries. Fifty of them (F1-F25 and F27-F51) are measured or stated
figures; F26 is a costing method published by Drewry and is numbered only for reference.

---

# A. Sea-going ships

## A1. Modern operating-cost survey with a repair line separated from stores, lubricants, insurance and crew

Source for F1-F8: Milojka Pocuca, "Methodology of Day-to-Day Ship Costs Assessment",
*Promet — Traffic & Transportation*, vol. 18, no. 5 (2006), pp. 337-345, Table 4 (p. 340), which
reproduces the Moore Stephens *OpCost 2004* database. The sample is described in the table itself:
handysize bulker, 20,000-40,000 dwt, 89 ships, average size of sample 28,909 dwt, average year of
build of sample 1985, world fleet of the group 2,156 ships in 2003. Daily figures are the annual
figure divided by 365, as the text states. `[S]` URL:
https://traffic2.fpz.hr/index.php/PROMTT/article/download/2188/1066

| # | Year | Vessel | Figure as stated | Includes / excludes | Denominator | Source |
|---|---|---|---|---|---|---|
| F1 | 2003 | Handysize bulker, 28,909 dwt sample, built 1985 | US$77,155 per year | "Repairs & maintenance". Excludes spares (separate line), lubricants, stores, insurance, crew, management | per vessel-year, 365 days | OpCost 2004 via Pocuca 2006, Table 4 |
| F2 | 2003 | as F1 | US$211 per day | as F1 | per vessel-day (365-day basis) | as F1 |
| F3 | 2003 | as F1 | US$85,041 per year = US$233 per day | "Spares" — separate from "Repairs & maintenance" | per vessel-year and per day | as F1 |
| F4 | 2003 | as F1 | US$162,196 per year = US$444 per day | "Repairs & maintenance total" = spares plus repairs & maintenance | per vessel-year and per day | as F1 |
| F5 | 2003 | as F1 | US$1,198,647 per year = US$3,284 per day | Total operating costs, all heads. Excludes depreciation, fuel, port charges, cargo handling | per vessel-year and per day | as F1 |
| F6 | 2003 | as F1 | US$60,019 per year = US$164 per day | "Lubricants" only | per vessel-year and per day | as F1 |
| F7 | 2003 | as F1 | US$131,923 per year = US$361 per day | "Insurance total", made up of two lines labelled in the table "P&I insurance" US$72,292 and "Insurance" US$59,631 | per vessel-year and per day | as F1 |
| F8 | 2003 | as F1 | US$548,791 per year = US$1,504 per day | "Total crew costs" (wages, victuals, other crew costs) | per vessel-year and per day | as F1 |

For comparison the same table gives 2002 total operating costs of US$1,108,136 per year =
US$3,033 per day. `[COMPUTED]` F4 as a share of F5 is 13.5 per cent. The source does not state
that share.

Two other lines in the same table, recorded because they are the heads the task asks to keep
separate: "Management fees" US$141,608 per year = US$388 per day; "Stores other" US$87,442 per
year = US$240 per day.

## A2. Moore Stephens OpCost 2011 — total daily operating cost by type and size

Source: Richard Greiner (Moore Stephens LLP), "Ship operating costs: current and future trends",
seminar slides, December 2011, slides 12, 13, 14. `[S]` URL:
https://www.moorestephens.gr/images/OpCost_Seminar.pdf

These are total operating costs. The slides do not give a repair figure in dollars per day; they
give repair and maintenance only as an index (see below). Recorded here because the totals are the
denominator against which a repair share has to be read.

| # | Year | Vessel | Figure as stated | Includes / excludes | Denominator | Source |
|---|---|---|---|---|---|---|
| F9 | OpCost 2011 (index series ends 2010) | Handysize bulker | US$5,278 per day | Total operating cost. Dry-docking is listed as a separate cost category of the survey | per vessel-day | Greiner 2011, slide 12 |
| F10 | as F9 | Capesize bulker | US$7,437 per day | as F9 | per vessel-day | slide 12 |
| F11 | as F9 | VLCC tanker | US$10,670 per day | as F9 | per vessel-day | slide 13 |
| F12 | as F9 | Feedermax container, 100-1,000 TEU | US$4,372 per day | as F9 | per vessel-day | slide 14 |
| F13 | as F9 | Main liner container, 2,000-6,000 TEU | US$7,549 per day | as F9 | per vessel-day | slide 14 |

The same deck gives repair and maintenance as an index, 2000 = 100, for 2010: bulker 156, tanker
129, container 135 (slide 19). Indices, not costs; no level in money is given.

## A3. Drewry repair and maintenance by vessel size, 1991-1998 `[UNVERIFIED EXTRACTION]`

Source: "The Greek-flagged fleet: a case study…", World Maritime University dissertation,
Table 10, captioned "Repairs and maintenance cost for bulkers and tankers. Source: Compiled by
Drewry, 1998b and Ocean Shipping Consultants." `[S]` URL:
https://commons.wmu.se/cgi/viewcontent.cgi?article=1386&context=all_dissertations

Verification: the PDF is behind a Cloudflare challenge and could not be opened on 2026-11-17. The
table text below is the search provider's extraction of that PDF, read in full and internally
consistent. It has not been checked against the document itself.

The table legend as extracted reads: "A1: Daily repair and maintenance cost in USD per day;
A2: Annual repair and maintenance cost in ,000 USD per day; B: Percentage of the cost in the
daily operating cost; C: Annually fluctuation of cost." The A2 wording is garbled in the source
and is not used here. Only A1 (dollars per day) and B (share of daily operating cost) are
recorded.

| # | Period | Vessel | Figure as stated | Includes / excludes | Denominator | Source |
|---|---|---|---|---|---|---|
| F14 | 1991 and 1998 | Tanker 45,000 dwt | US$1,300 per day (1991), US$1,190 per day (1998); 23 per cent and 21 per cent of daily operating cost | Repairs and maintenance. The source states it "is composed of the running repairs and maintenance as well as of the docking repairs and maintenance" | per vessel-day | Drewry 1998b via WMU Table 10 |
| F15 | 1991 and 1998 | Tanker 95,000 dwt | US$1,780 / US$1,550 per day; 27 / 24 per cent | as F14 | per vessel-day | as above |
| F16 | 1991 and 1998 | Tanker 150,000 dwt | US$2,150 / US$1,975 per day; 29 / 27 per cent | as F14 | per vessel-day | as above |
| F17 | 1991 and 1998 | Tanker 280,000 dwt | US$2,600 / US$2,535 per day; 27 / 25 per cent | as F14 | per vessel-day | as above |
| F18 | 1991 and 1998 | Bulker 25/50,000 dwt | US$286 / US$352 per day; 26 / 26 per cent | as F14 | per vessel-day | as above |
| F19 | 1991 and 1998 | Bulker 50/80,000 dwt | US$368 / US$475 per day; 27 / 29 per cent | as F14 | per vessel-day | as above |
| F20 | 1991 and 1998 | Bulker 80/150,000 dwt | US$439 / US$560 per day; 27 / 29 per cent | as F14 | per vessel-day | as above |
| F21 | 1991 and 1998 | Bulker 150,000 dwt | US$411 / US$535 per day; 26 / 29 per cent | as F14 | per vessel-day | as above |

The accompanying text states that repairs and maintenance "are representing 27% of the daily
operating cost, on average among all sizes of bulkers" and "25% on average" for tankers. The
sizerange labels are reproduced as printed; the third bulker band (80/150,000 dwt) and the fourth
(150,000 dwt) overlap, which is a defect in the source.

## A4. Dry-docking and survey costs, intervals and content

| # | Year | Vessel | Figure as stated | Includes / excludes | Denominator / interval | Source |
|---|---|---|---|---|---|---|
| F22 | 2013 | 6 vehicle carriers / car carriers, 1 LPG carrier, 1 bulker, managed by Wilhelmsen Ship Management | Average docking cost US$405,000 per docking; average yard quotation US$192,000 per docking | Total docking cost incurred against the yard's quoted price. Hull, machinery and survey items not separated in the abstract | per docking | Norwegian University of Science and Technology master's thesis, "Analysis of estimations, quotations and actual costs related to dry-docking" (2013), abstract, handle 11250/298579. `[S]` The PDF was not retrieved; the figure is taken from the repository's abstract record |
| F23 | 2023 (report year) | Containership fleet of Danaos Corporation (SEC CIK 1369241) | Deferred dry-docking and special survey costs: additions US$29,939k (2022) and US$31,121k (2023); amortisation US$12,170k (2022) and US$18,663k (2023); balance US$38,012k at 31 Dec 2023 | Dry-docking and special survey cost only. Not repairs generally, not stores, not lubricants | Amortised straight line "over the period until the next scheduled survey, which is two and a half years" | Danaos Corporation annual report, note 6 "Deferred Charges, net". `[P]` URL: https://www.sec.gov/Archives/edgar/data/1369241/000110465924029397/R14.htm |
| F24 | current (rev. 1996, in force) | All classed ships | Minimum of two examinations of the outside of the bottom in each five-year special survey period; one in conjunction with the special survey; interval between any two not to exceed 36 months; special surveys at five-year intervals to renew the class certificate | Examination of the bottom and related items. An in-water survey may be accepted in place of dry-docking except for ESP ships of 15 years and over | 5-year cycle; 36-month maximum gap | IACS Unified Requirement Z3, Z3.1.2 and Z3.1.3; special survey schedule at 2.1.1. `[P]` URL: https://iacs.s3.af-south-1.amazonaws.com/wp-content/uploads/2024/09/05120213/URZ.pdf |
| F25 | current | Ships operating in fresh water, certain harbour craft, non-self-propelled craft | The interval between bottom examinations "may be greater" than the 36-month rule | as F24 | interval not quantified in the text | IACS UR Z3.1.4. `[P]` |
| F26 | 2016 report | All types | Method: "take the total indicative cumulative cost of an intermediate survey and a dry docking and divide it by five to arrive at the annual cost" | Intermediate survey plus full dry docking; excludes routine running repair, and excludes extra crew carried for maintenance | 5-year cycle | Drewry, *Ship Operating Costs Annual Review and Forecast 2016-17*, Introduction. `[S]` URL: http://www.drewry.co.uk/AcuCustom/Sitename/DAM/006/Table%20of%20Contents%20Ship%20Operating%20Costs%202016-17.pdf |

What a docking includes, as the sources define it. Drewry lists "Repairs and maintenance (R&M)
(including allowances for intermediate surveys and full dry docking)" and, in the 2025/26 edition,
splits "Repair and maintenance" and "Dry-docking" into two separate cost heads. Its sub-cost head
list defines "Annual class fee" as "the contracted fee paid to the Class Society to cover annual,
intermediate and civil, structure and management (CSM) surveys" and "Class Society costs" as "fees
paid for classification surveyor". The 2025/26 contents list an "indicative dry-docking cost …
($ per 5-year period)" table for each sector (for example Table 4.28 for containerships, Table 5.25
for dry bulk carriers, Table 11.25 for other vessels), and Table 2.11 "Dry-docking regional costs
considerations". No value from those tables is printed in any accessible summary; the report is
paid. `[S]` URLs: https://www.drewry.co.uk/AfcMediaLibrary/Display/SecureDownload.cfm?code=48008
(contents) and the Drewry opinion page of 2026-11-11.

## A5. Classification and statutory survey fees

No published figure for an IACS member's class fee per vessel was found. Drewry treats it as a
separate sub-cost head (above) without printing a value, and the World Maritime University study
of classification societies states only that fees "are neither proportional to, nor connected with
the size of the asset value". What is published is flag-state and certifying-authority fee
schedules:

| # | Year | Vessel | Figure as stated | Includes / excludes | Denominator | Source |
|---|---|---|---|---|---|---|
| F27 | from 1 Jan 2026 | Vessels surveyed by the Norwegian Maritime Authority | NOK 1,714 per hour for surveys in Norway; NOK 3,050 per hour for surveys abroad; overtime NOK 1,436 per hour | Time-based survey fee only, excluding the annual fee and initial fee | per surveyor-hour | Norwegian Maritime Authority, "Fees that are not included in the fee calculator". `[P]` URL: https://www.sdir.no/en/vessels/for-shipowners/gebyrer-som-ikke-er-inkludert-i-gebyrkalkulatoren/ |
| F28 | 2026 | Small commercial vessel under UK MCA codes, certified by SCMS | Certificate issue £175 (under 7 m) to £375 (15 m and over); annual retention £120 (0-14.99 m) or £205 (15 m and over); certificate re-issue £90 | Statutory certification only. Not classification, not repair | per certificate and per year | SCMS (MCA appointed certifying authority), "Fees 2026". `[P]` URL: https://www.scmshq.org/fees/ |

## A6. Historical ships, c.1849-1914

| # | Year | Vessel | Figure as stated | Includes / excludes | Denominator / interval | Source |
|---|---|---|---|---|---|---|
| F29 | 1849 | Any vessel using the patent slip at Llanelly | "the charge for the use of the slipway for repair was 1/2d. per register ton per day" (one halfpenny) | Slipway hire only. Excludes labour, materials, and any dock company charge beyond the slip | per register ton per day of occupation | Robert Craig, "W H Nevill and the Llanelly Iron Shipping Company", *National Library of Wales Journal*, vol. X no. 3 (Summer 1958), footnote 3, quoting an 1849 Llanelly tide table. `[S]` URL: https://www.genuki.org.uk/big/wal/Archives/NLWjournals/NevillLlanelly |
| F30 | 1862 | Wooden or iron ship of 400-500 tons | "The actual cost per annum of sheathing a vessel of from 400 to 500 tons, may be set down, under ordinary circumstances, at not less than £120" | Metal sheathing and its renewal only. Excludes all other hull work, caulking, painting, machinery | per vessel-year | N. Mercer, "On the protection of wood and iron ships to prevent fouling", read 1 January 1862, p. 86. `[P]` URL: https://www.hslc.org.uk/wp-content/uploads/2017/08/14-6-Mercer.pdf |
| F31 | early 1870s | Second-hand softwood vessel of 150-500 gross tons, British North American built | "the cost of fitting, coppering and making ready for sea might be between £150 and £750" | One-off outfitting on purchase: fitting out, coppering, making ready for sea. Not annual maintenance | per vessel, on acquisition | Craig 1958, section III. `[S]` |
| F32 | 1913 | 50,000-ton passenger liner, building and equipment cost £1,500,000 | "annual overhaul … £30,000" | Overhaul only, stated separately from depreciation and from the 5 per cent return on capital in the same estimate | per vessel-year | A. W. Kirkaldy, *British Shipping: Its History, Organisation and Importance* (London: Kegan Paul, 1914), p. 211, quoting a *Times* article of June 1913. `[S]` URL: https://archive.org/details/britishshippingi0000kirk |
| F33 | 1910 and 1912 | Two unnamed tramp companies, "A" and "B" | A: depreciation £4,000 (1910) and £31,000 (1912); net profit £8,946 and £49,385; dividend £5,165 (6 per cent) and £9,025 (8 per cent). B: reserve £20,000 and £40,000; net profit £38,457 and £96,426; dividend £10,000 (5 per cent) and £50,000 (25 per cent) | Depreciation and reserve allocations. These are provisions, not repair spend. The accounts as quoted contain no repair line | per company-year | Kirkaldy 1914, p. 210. `[S]` |

`[COMPUTED]` F32 is 2.0 per cent of the stated capital cost of £1,500,000. The source states the
three elements (£75,000 at 5 per cent, £90,000 depreciation at 6 per cent, £30,000 overhaul,
totalling £195,000) but does not state the percentage that overhaul is of capital.

## A7. British shipping company accounts: what exists and what does not

No published repair figure was found in a British liner company's published accounts. The
position on each company named in the brief:

- **P&O.** The archive holds "ships' cost and repair ledgers, 1855-1859, 1864-1941", "summaries of
  ships' voyage expenses, 1881-1890" and "ships' voyage results and analysis, 1919-1965", plus
  "schedules to the annual accounts … 1856 to 1878 and 1905 to 1961". These are the records from
  which a per-voyage repair cost can be built. They are not published, and no compiled figure from
  them was found. Source: Royal Museums Greenwich archive description, P&O collection,
  https://www.rmg.co.uk/collections/archive/rmgc-object-492010 `[P]` (description of holdings).
- **Cunard.** "Report and accounts", 1903-1933, held at HathiTrust, catalogue record
  103099923, marked "Limited (search only)". No text was readable. `[P]` (description only).
- **Blue Funnel (Ocean Steam Ship Company).** Archive at National Museums Liverpool: "voyage books,
  freight accounts, statements of depreciation, earnings, taxation". No published repair series.
- **Elder Dempster, Ellerman, Furness Withy.** No published repair figure found. These companies'
  accounts are not available in full text in any repository reached.
- **Coastal operators.** No published repair figure found. The Maryport coaster study (1855-1889)
  records that a coaster could be under repair for a month or two (Farmer, January and much of
  February 1867) but gives no repair cost. `[S]`

The general point, stated plainly: British liner and tramp accounts of this period report
"working expenses" as one figure, or report depreciation and reserve allocations separately, and
do not print repairs as a line. F33 is an example of what is printed.

---

# B. Inland and canal boats
