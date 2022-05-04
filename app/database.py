import imp
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import Price
from typing import List
import os
import pymongo



MONGO_DETAILS = os.getenv('MONGO_DETAILS')

client_sync = pymongo.MongoClient(MONGO_DETAILS)
client = AsyncIOMotorClient(MONGO_DETAILS)
db_sync = client_sync["prices"]
coll_sync = db_sync["btc_price"]
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

def mongo_import(_csv: dict) -> bool:
    print(MONGO_DETAILS)
    print(coll_sync.count())
    coll_sync.create_index([('date', 1)], unique=True)
    print(coll_sync.count())
    coll_sync.delete_many({})
    print(coll_sync.count())
    coll_sync.insert_many(_csv)
    print(coll_sync.count())
    print(coll)
    return True
    
