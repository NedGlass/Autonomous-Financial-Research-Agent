import yfinance as yf

# splitting by statement type so that each can be wrapped in own Claude tool later
def get_income_statement(ticker: str) -> dict:
    df = yf.Ticker(ticker).income_stmt
    if df.empty:
        return {}
    return df.iloc[:, 0].dropna().to_dict

def get_balance_sheet(ticker: str) -> dict:
    df = yf.Ticker(ticker).balance_sheet
    if df.empty:
        return {}
    return df.iloc[:, 0].dropna().to_dict

def get_cash_flow(ticker: str) -> dict:
    df = yf.Ticker(ticker).cash_flow
    if df.empty:
        return {}
    return df.iloc[:, 0].dropna().to_dict

def get_market_data(ticker: str) -> dict:
    info = yf.Ticker(ticker).info
    return {
        'price': info.get('currentPrice') or info.get('regularMarketPrice'),
        'market_cap': info.get('marketCap'),
        'shares_outstanding': info.get('sharesOutstanding'),
        'pe_ratio': info.get('trailingPE'),
        'currency': info.get('currency'),
    }

# wrapping as one claude tool, rather than 4 separate tools
def get_financials(ticker: str) -> dict:
    return {
        'income_statement': get_income_statement(ticker),
        'balance_sheet': get_balance_sheet(ticker),
        'cash_flow': get_cash_flow(ticker),
        'market_data': get_market_data(ticker),
    }