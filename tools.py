from data_agents.financials import get_financials
from data_agents.eia_prices import get_commodity_prices
from data_agents.reference_data import get_reference_data

TOOLS = [
    {
        "name": "get_financials",
        "description": "Returns a multi-year income statement, balance sheet, cash flow, and market data for a given stock ticker.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker symbol, eg XOM or SHEL.L",
                }
            },
            "required": ["ticker"],
        },
    },
    {
        "name": "get_commodity_prices",
        "description": "Returns the latest Brent, WTI and Henry Hub spot prices. Takes no arguments.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "get_reference_data",
        "description": "Returns manually sourced reference data for a given ticker, reserves/production or generation capacity/mix, capex split, and emissions intensity, depending on sector.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker symbol, eg XOM or SHEL.L",
                }
            },
            "required": ["ticker"],
        },
    },
]


def call_tool(name: str, tool_input: dict):
    if name == "get_financials":
        return get_financials(tool_input["ticker"])
    if name == "get_commodity_prices":
        return get_commodity_prices()
    if name == "get_reference_data":
        return get_reference_data(tool_input["ticker"])
    raise ValueError(f"tool not recognised: {name}")
