from pydantic import BaseModel


class Price(BaseModel):
    date: str
    price_usd: str


class Rentability(BaseModel):
    rentability: float
    profit_value: float
