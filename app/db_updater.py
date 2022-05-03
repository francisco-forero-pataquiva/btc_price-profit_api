from app.database import MONGO_DETAILS, mongo_import
from app.utils import process_csv


def populate_db(event, lambda_context) -> None:
    _csv = process_csv(
        "https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv")
    print(MONGO_DETAILS)
    print("Csv processed!")
    mongo_import(_csv)
populate_db(1,2) 
# schedule.every().hour.do(populate_db)
