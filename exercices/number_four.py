import re, os, subprocess
from typing import List
from pandas import read_csv
from peewee import (
    SqliteDatabase,
    IPField,
    BooleanField,
    SmallIntegerField,
    IntegerField,
    CharField,
    DateTimeField,
    DateField,
    ForeignKeyField,
    FloatField,
    CompositeKey,
    Model
)
import datetime

path_to_db = "sqlite.db"
db = SqliteDatabase(path_to_db)

class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    id = SmallIntegerField(unique=True, primary_key=True)
    date = DateField()
    weekday = CharField()
    gain = IntegerField(default=0)
    prices = FloatField(default=0.0)
    up = BooleanField(default=False)
    creation_date = DateTimeField(default=datetime.datetime.now)


def parse_csv_file_into_database(csv_path: str, db_path: str):
    data = read_csv("./statics/excel_file.csv")
    # print(data)
    # Connect to our database.
    db.connect()
    # Create the tables ... if needed
    db.create_tables([Client])

    for index, row in data.iterrows():
        item = Client(
            date=row["date"],
            weekday=row["weekdays"],
            gain=row["gains"],
            prices=row["prices"],
            up=row["up"]
        )
        item.save()

    query = Client.select()
    for item in query.execute():
        print(f"id: {item}\ndate: {item.date}\nweekday: {item.weekday}\ngain: {item.gain}\nprices: {item.prices}\nup: {item.up}")
        print("_____________________________")

def display_errors() -> List[str]:
    # Use https://regex101.com/ to test your regex expression.
    """
    %ERROR  -->  ... string `%ERROR`
    .       -->  followed by ...
    *       -->  everything
    """
    error = re.compile("%ERROR.*")
    with open("./statics/logs.txt", "r") as log_file:
        lines_matched = error.findall(log_file.read())
    print("\n".join(lines_matched))
    return lines_matched

def create_tar_archive(csv_path: str, archive_path: str) -> bool:
    cmd = ["tar", "-zcvf", archive_path, csv_path]
    try:
        output = subprocess.run(cmd, capture_output=True)
    except subprocess.CalledProcessError as ex:
        print(f"Exception: {ex}")
        return False
    return True

def main():
    display_errors()
    csv_path = "./statics/excel_file.csv"
    parse_csv_file_into_database(csv_path, "")
    archive_path = "./statics/excel_file.tar.gz"
    if os.path.exists(archive_path):
        os.remove(archive_path)
    create_tar_archive(csv_path, archive_path)

if __name__ == '__main__':
    main()