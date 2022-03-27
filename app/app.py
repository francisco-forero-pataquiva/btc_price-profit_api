from fastapi import FastAPI
from app.schemas import Rentability
from app.database import fetch_price_history, fetch_price
from app.utils import calculate_rentability, calculate_profit
from typing import Optional
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
app = FastAPI(middleware=middleware, root_path="/dev/",)


@app.get('/')
async def root():
    return {'message': "CRYPTO API 🤑"}

@app.get("/bitcoin/")
async def get_bitcoin_price(_limit: int = 30, _skip: Optional[int] = 1):
    response = await fetch_price_history(_limit, _skip)
    return response
    
@app.get("/funds/bitcoin/rentability", response_model=Rentability)
async def get_bitcoin_rentability(init_date:str, end_date:str, invest_value: float):
    in_dt, en_dt = await fetch_price(init_date), await fetch_price(end_date)
    r = calculate_rentability(in_dt,en_dt)
    profit = calculate_profit(invest_value,r)
    response = {"rentability": r,
                "profit_value": profit}
    return response

handler = Mangum(app)