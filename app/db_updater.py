from app.database import mongo_import
from app.utils import process_csv

from mangum import Mangum

def populate_db() -> None:
    _csv = process_csv(
        "https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv")
    mongo_import(_csv)
    

db_updater_handler = Mangum(populate_db)
    
# schedule.every().hour.do(populate_db)
