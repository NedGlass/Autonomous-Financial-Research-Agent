import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EIA_API_KEY")

def get_brent_price() -> dict:
    r = requests.get(
        'https://api.eia.gov/v2/petroleum/pri/spt/data/',
    params = {
        'api_key': API_KEY,
        'frequency': 'daily',
        'data[0]': 'value',
        'facets[series][]': 'RBRTE',
        'sort[0][column]': 'period',
        'sort[0][direction]': 'desc',
        'length': 1
        },
    )
    r.raise_for_status()
    rows = r.json()['response']['data']
    if not rows:
        return {}
    latest = rows[0]
    return {'date': latest['period'], 'price': latest['value']}

def get_wti_price() -> dict:
    r = requests.get(
        'https://api.eia.gov/v2/petroleum/pri/spt/data/',
    params = {
        'api_key': API_KEY,
        'frequency': 'daily',
        'data[0]': 'value',
        'facets[series][]': 'RWTC',
        'sort[0][column]': 'period',
        'sort[0][direction]': 'desc',
        'length': 1
        },
    )
    r.raise_for_status()
    rows = r.json()['response']['data']
    if not rows:
        return {}
    latest = rows[0]
    return {'date': latest['period'], 'price': latest['value']}

def get_henry_price() -> dict:
    r = requests.get(
        # route has both future and spot prices, despite 'fut' name, facet narrows to Henry Hub spot specifically
        'https://api.eia.gov/v2/natural-gas/pri/fut/data/', 
    params = {
        'api_key': API_KEY,
        'frequency': 'daily',
        'data[0]': 'value',
        'facets[series][]': 'RNGWHHD',
        'sort[0][column]': 'period',
        'sort[0][direction]': 'desc',
        'length': 1
        },
    )
    r.raise_for_status()
    rows = r.json()['response']['data']
    if not rows:
        return {}
    latest = rows[0]
    return {'date': latest['period'], 'price': latest['value']}

def get_commodity_prices() -> dict:
    return {
        "brent": get_brent_price(),
        "wti": get_wti_price(),
        "henry_hub": get_henry_price()
    }