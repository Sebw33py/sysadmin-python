import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth


basic = HTTPBasicAuth('go-spereira', "6w(A7wX+M6L'E3^")
url = "https://elastic-ingest.arkadin.com:9200/srelogs/_search"
params={"q":"CMDB_Product_Name: ELK","size":"10000","pretty":"true"}

response = requests.get(url, auth=basic, params=params)

pprint(response.json())  # Content in JSON format

