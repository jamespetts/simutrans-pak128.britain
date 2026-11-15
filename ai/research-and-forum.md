---
status: stub
verified: none
---
# Research and forum

**Covers**: sourcing historical or balancing data, and how to use and cite the Simutrans forum
and research material.

## Notes

- The Simutrans forum pak128.Britain board is
  https://forum.simutrans.com/index.php/board,75.0.html . It is the main community reference for
  the pakset. Cite forum-derived facts with `[FORUM:<url>]` and the post date where possible
  ([claim-tags](claim-tags.md)).
- Period manufacturer sales brochures on archive.org are a primary source for UK paint names
  and trim ranges (found via archive.org advancedsearch and the item `_djvu.txt` OCR text;
  used for the Ford Anglia and BMC 1100 colours on 2026-11-15). When web search is
  unavailable (an HTTP 402 outage across the search engines was observed that day), direct
  URL fetches, mwmbl.org/Marginalia and archive.org still worked.
  `[LITERATURE:https://archive.org/]`
- The base root contains loose research material (`.pdf`, `.xls`, `.ods`, `.csv`, images, and
  similar) and historical folders. Some of it is useful for balancing research but none of it is
  authoritative; verify against the checked-out data before relying on it. Read it only during a
  documentation or balancing run, or when docs or prompts say so ([repo-map](repo-map.md)).

## Web search tooling and provider pricing (2026-11-15)

Recorded for research-tooling decisions. Prices are from the vendors' own pricing pages
(2026-11-15); quality claims come from independent provider-swap benchmarks (Artificial
Analysis Search Index, <https://artificialanalysis.ai/agents/search-api>; openbenchmarks-labs
coding benchmark; cloro reproducible benchmark) `[LITERATURE:https://artificialanalysis.ai/agents/search-api]`.
Beware two traps when reading prices: benchmark "$/1k tasks" figures bundle several searches
per task and are NOT per-search prices, and vendors price different modes (basic/lite vs
advanced/auto) and volume tiers.

| Provider | Model | $ per 1,000 basic searches | Free allowance | Quality (independent benchmarks) |
| --- | --- | --- | --- | --- |
| OpenCode Hosted | $0.01 per delivered search, workspace balance | 10.00 | none | unbenchmarked (works; found photo sources in use) |
| TinyFish | free search + fetch | 0.00 | unlimited (limits unpublished) | 79% search+fetch (3rd/14, coding benchmark) |
| Exa | per-search dollar rate, prepaid dollar balance (no expiry) | 4.00 lite / 7.00 auto | $10 every month (≈2,500 lite searches) | top-2 on all five boards (≈80 AA index) |
| Parallel | per-search dollar rate, monthly allowances | from 1.00 (tiered) | Launch tier free; $5/month on Build | top on two boards (87% AIMultiple; 97.8% SimpleQA) |
| Tavily | credit points (1–2 per search by depth) | 8.00 basic / 16.00 advanced | 1,000 credits/month | weakest of the five on every independent board |
| Firecrawl | credit points (2 per 10 results) | 7.60–10.00 (2.00 on Standard) | 1,000 credits/month | weak search; strongest page/PDF scraping |

**Expiring-credit practice.** `[USER-DIRECTION:2026-11-15]` Selling credits that expire is a
dishonest charging practice and is a strike against a provider. Parallel Scale (paid monthly
credits expire), Firecrawl (plan credits expire monthly; top-up credits expire on
cancellation) and Tavily (monthly reset) all do this. Exa's paid balance is documented as a
draw-down balance with no expiry; the hosted search charges only for delivered results.

**Current decision (2026-11-15):** keep the OpenCode hosted search meanwhile; the user
intends to subscribe to Exa later. Firecrawl's free credits only, if brochure/PDF scraping
is needed. `[USER-DIRECTION:2026-11-15]`

## Planned sections

- The kinds of historical data needed for balancing and where to find them.
- How to record research sources and their reliability.
- Which loose research files are worth indexing.

## Open questions

- Which research material is reliable enough to cite, and under what tag?
