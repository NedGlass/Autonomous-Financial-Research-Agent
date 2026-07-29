from datetime import date

from data_agents.financials import get_financials
from data_agents.reference_data import get_reference_data
from data_agents.eia_prices import get_commodity_prices

# SSE.L reports on a non-calendar (April-March) fiscal year, everyone else does calendar
NON_CALENDAR_FISCAL_YEAR = {"SSE.L"}


def get_standardised_data(ticker: str) -> dict:
    fin = get_financials(ticker)
    ref = get_reference_data(ticker)

    fiscal_year_basis = "calendar"
    if ticker in NON_CALENDAR_FISCAL_YEAR:
        fiscal_year_basis = "non_calendar_apr_mar"

    market_data = fin["market_data"].copy()
    market_data["as_of"] = date.today().isoformat()

    return {
        "sector_type": ref.get("sector_type"),
        "fiscal_year_basis": fiscal_year_basis,
        "reference_fiscal_year": ref.get("fiscal_year"),
        "reference_source": ref.get("source"),
        "financials": {
            "income_statement": fin["income_statement"],
            "balance_sheet": fin["balance_sheet"],
            "cash_flow": fin["cash_flow"],
        },
        "market_data": market_data,
        "oil_gas": ref.get("oil_gas"),
        "generation": ref.get("generation"),
        "capex": ref.get("capex"),
        "emissions": ref.get("emissions"),
    }


def get_standardised_commodity_context() -> dict:
    raw = get_commodity_prices()
    prices = {}
    for name, vals in raw.items():
        prices[name] = {"date": vals["date"], "price": float(vals["price"])}
    prices["as_of"] = date.today().isoformat()
    return prices