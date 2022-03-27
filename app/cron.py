import schedule
import time
from src.database import mongo_import
from src.utils import process_csv


def populate_db() -> None:
    _csv = process_csv(
        "https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv")
    mongo_import(_csv)
    
schedule.every().day.at("21:10").do(populate_db)

while True:
    schedule.run_pending()
    time.sleep(1)
