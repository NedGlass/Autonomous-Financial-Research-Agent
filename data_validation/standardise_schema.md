## Financials (yfinance)

Most tickers go back 5 years to 2021. A few are missing just the oldest year on one or two statements: SHEL.L's cash_flow, BP.L's balance_sheet, TTE.PA's income_statement, IBE.MC's balance_sheet and cash_flow. Never a whole statement missing, just 2021 (sometimes 2022) dropping off, and it's not consistent which statement each time. Not worth chasing. standardise.py doesn't assume the three statements share the same years anyway, it just passes through whatever's there.

Also: even when an early year shows up it's usually almost empty. Confirmed this on XOM and NEE, 2021's income_statement for both is like 2-3 fields instead of the usual 30ish. Just dropna() dropping anything NaN for that period. Not a bug.

SSE.L reports on a non-calendar fiscal year (Apr-Mar), so its year labels run one ahead of everyone else (2022-2026 instead of 2021-2025). This is handled now: fiscal_year_basis in standardise.py flags it as "non_calendar_apr_mar", tested for real and works.

ORSTED.CO is missing pe_ratio in market_data. Normal for a non-US listing.

## Reference data nulls

Still the same 5, all confirmed undisclosed (checked against primary sources):

- SHEL.L: emissions null
- XOM: capex split null, emissions null (total capex is known though, $29,000m, just the low-carbon split isn't disclosed)
- NEE: capex split null (total capex known, $24,606m)
- DRX.L: capex split null

## Commodity prices

All three series come back fine but get_commodity_prices() returns price as a string ("86.99"), not a number. Found this testing standardise.py. It casts to float before returning so anything going through the merge layer is fine.

## New stuff from testing standardise.py

SSE.L's market_data.currency is "GBp". Which is in pence, not pounds. price and market_cap end up on different scales because of it (they reconcile fine, just a unit thing). If Phase 3 ever mixes SSE.L's price with a per-share number sourced elsewhere, like EPS from the income statement which will be in pounds, need to remember the 100x difference. Similar to the BOE conversion mismatch between BP and XOM.

## Where this stands

standardise.py built and tested on all 10 tickers now, no failures. Schema holds, nulls come through right, NEE's emissions year vs reference year divergence survived the merge, SSE.L's non-calendar flag works.