from fastapi import FastAPI
from src.schemas import Rentability
import logging
from src.database import fetch_price_history, fetch_price, mongo_import
from src.utils import calculate_rentability, calculate_profit, process_csv
from typing import Optional
from fastapi_utils.tasks import repeat_every


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
logger = logging.getLogger(__name__)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
@repeat_every(seconds=60*60*24)
def populate_db() -> None:
    _csv = process_csv("https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv")
    mongo_import(_csv)

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
