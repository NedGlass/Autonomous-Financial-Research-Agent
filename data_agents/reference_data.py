import json
import os

REFERENCE_DATA_PATH = os.path.join(
    os.path.dirname(__file__), "..", "reference_data", "company_data.json"
)


def get_reference_data(ticker: str) -> dict:
    with open(REFERENCE_DATA_PATH) as f:
        data = json.load(f)
    return data.get(ticker, {})
