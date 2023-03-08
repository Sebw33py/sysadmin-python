from elasticsearch import Elasticsearch
from datetime import datetime
es = Elasticsearch("https://elastic-ingest-pp.arkadin.com:9200",api_key="LVBGaHdJWUJZb0psT0tFTUdudTc6QWNFRDl1eVpRVUtKYl9yYjVMVWx6QQ==")

print(es.info())

# doc = {
#     'author': 'seb',
#     'text': 'c\'est mon doc !',
#     'timestamp': datetime.now(),
# }
# resp = es.index(index="test-index", id=1, document=doc)
# print(resp['result'])

# resp = es.get(index="test-index", id=1)
# print(resp['_source'])

# es.indices.refresh(index="test-index")

resp = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])