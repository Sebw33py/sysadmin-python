import pandas
import os
import pathlib


PATH_JSON=os.path.join(
    pathlib.Path(__file__).parent.resolve(),
    "winlog.json"    
)

print (PATH_JSON)

dataframeu = pandas.read_json(PATH_JSON)
# print(dataframeu)

hits = dataframeu["hits"]["hits"]
# print(hits)
for hit in hits:
    
    hit = set(hits)
    print(hit["_source"]["agent"]["name"])
   
