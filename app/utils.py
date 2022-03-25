
def calculate_rentability(init_value: float, final_value: float) -> float:
    f = (final_value / init_value)
    r = (f - 1) * 100
    return r

def calculate_profit(invest_value: float ,r: float) -> dict:
    rentability_value = (invest_value * r)/100
    invest_value += rentability_value
    return invest_value    
