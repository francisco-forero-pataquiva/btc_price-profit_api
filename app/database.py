from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import Price
from decouple import config
from typing import list


MONGO_DETAILS = config('MONGO_DETAILS')

client = AsyncIOMotorClient(MONGO_DETAILS)

db = client["prices"]

coll = db["btc_price"]

async def fetch_price(date:str):
    document = await coll.find_one({"date": date})
    price = document["price_usd"]
    return price

async def fetch_price_history(_limit: int, _skip: int) -> List:
    prices = []
    cursor = coll.find({}).sort("date", -1 ).limit(_limit).skip(_skip)
    async for document in cursor:
        prices.append(Price(**document))
    return prices
    