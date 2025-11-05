import requests
import json

keyword = "x"

response = requests.get("https://api.chucknorris.io/jokes/random")

try:
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=1))
        print(json_response["value"])
except ValueError:
    print("Value Error")