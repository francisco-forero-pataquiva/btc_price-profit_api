from app.database import mongo_import
from app.utils import process_csv


def populate_db((event, lambda_context) -> None:
    lightID = event
    _csv = process_csv(
        "https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv")
    print("Csv processed!")
    mongo_import(_csv)
    
populate_db()
        
# schedule.every().hour.do(populate_db)
