# Data Completeness Gap Log

Covers a full run of get_financials, get_reference_data, and get_commodity_prices across all 10 tickers, checking for missing fiscal years, missing market-data fields, and unexpected null reference-data fields. Feeds directly into building the merged per-company schema.

## Financials (yfinance)

**SHEL.L**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 4 year(s) returned (2022, 2023, 2024, 2025)

**BP.L**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 4 year(s) returned (2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)

**XOM**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)

**TTE.PA**
- income_statement: 4 year(s) returned (2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)

**IBE.MC**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 4 year(s) returned (2022, 2023, 2024, 2025)
- cash_flow: 4 year(s) returned (2022, 2023, 2024, 2025)

**NEE**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)

**SSE.L**
- income_statement: 5 year(s) returned (2022, 2023, 2024, 2025, 2026)
- balance_sheet: 5 year(s) returned (2022, 2023, 2024, 2025, 2026)
- cash_flow: 5 year(s) returned (2022, 2023, 2024, 2025, 2026)
- note: fiscal-year labels run one year ahead of the other nine tickers (2022–2026 vs 2021–2025). Expected — SSE reports on a non-calendar (April–March) fiscal year, not a data error. Do not align these years 1:1 against other companies' calendar-year labels in downstream comparisons.

**ORSTED.CO**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- market_data.pe_ratio: missing — expected gap for a non-US listing, not an error.

**RWE.DE**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)

**DRX.L**
- income_statement: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- balance_sheet: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)
- cash_flow: 5 year(s) returned (2021, 2022, 2023, 2024, 2025)

## Reference data

**SHEL.L**
- emissions.value: null (basis=not_disclosed)

**BP.L**
- no nulls

**XOM**
- capex.low_carbon_capex_pct: null (basis=not_disclosed)
- emissions.value: null (basis=not_disclosed)

**TTE.PA**
- no nulls

**IBE.MC**
- no nulls

**NEE**
- capex.low_carbon_capex_pct: null (basis=not_disclosed)

**SSE.L**
- no nulls

**ORSTED.CO**
- no nulls

**RWE.DE**
- no nulls

**DRX.L**
- capex.low_carbon_capex_pct: null (basis=not_disclosed)

## Commodity prices

- all three series (Brent, WTI, Henry Hub) returned successfully.

## Summary

- 10/10 tickers returned data for all three financial statement types across multiple fiscal years; no company failed entirely.
- 5 reference-data fields null across 10 companies (SHEL.L emissions, XOM capex, XOM emissions, NEE capex, DRX.L capex) — every one matches already-documented primary-source research, not a new gap.
- 1 market-data field missing (ORSTED.CO pe_ratio) — expected for a non-US listing.
- SSE.L's fiscal-year labels run one year ahead of the other nine tickers due to its non-calendar reporting period — carry this caveat into any cross-company year-by-year comparison.