import pandas as pd


def process_csv(path:str) -> dict:
    df = pd.read_csv(path)
    df = df[["time","PriceUSD"]]
    df = df.rename({'time': 'date', 'PriceUSD': 'price_usd'}, axis=1)
    _dict = df.to_dict('records')
    return _dict

def calculate_markup(init_value: float, final_value: float) -> float:
    mk = 100 * (final_value / init_value)
    return mk

def calculate_profit(invest_value: float ,mk: float) -> dict:
    r = (mk - 1) * 100
    rentability_value = (invest_value * r)/100
    invest_value += rentability_value
    return invest_value    
