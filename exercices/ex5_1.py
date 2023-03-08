import requests
from urllib3.exceptions import InsecureRequestWarning 
from pprint import pprint


def get_api():
    # try:
        response = requests.get("https://google.fr/get")
        print(response.status_code)
        ERROR_CODE=response.status_code
    # except requests.exceptions.HTTPError as exception :
        if ERROR_CODE >= 400 :
            print(f"wrong url")
        else:
            print (f"the else")
            
get_api()
