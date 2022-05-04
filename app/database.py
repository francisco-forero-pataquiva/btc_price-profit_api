import os
from typing import List

from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import Price


MONGO_DETAILS = os.getenv('MONGO_DETAILS')


client_sync = MongoClient(MONGO_DETAILS)
db_sync = client_sync["prices"]
coll_sync = db_sync["btc_price"]

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


def mongo_import(len_csv: int,_csv: dict) -> int:
    if len_csv != coll_sync.count():
        coll_sync.create_index([('date', 1)], unique=True)
        coll_sync.delete_many({})
        coll_sync.insert_many(_csv)
    else:
        print("Data already synced!")
    return coll_sync.count()
    
