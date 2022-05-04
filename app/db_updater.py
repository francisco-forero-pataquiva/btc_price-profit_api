from app.database import mongo_import
from app.utils import process_csv


def populate_db(event, lambda_context) -> None:
    _csv = process_csv("https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv")
    len_csv =  len(_csv)
    mongo_import(len_csv,_csv)
