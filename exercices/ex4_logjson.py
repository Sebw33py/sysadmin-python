import pandas
import os
import pathlib

data = pandas.read_json("./winlog.json")

print(f"{data.to_json()}\n")
