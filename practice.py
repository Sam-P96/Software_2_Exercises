import requests
import json

# keyword = "girls"
# request = "https://api.tvmaze.com/search/shows?q=" + keyword # notice its not www, but api.?
# response = requests.get(request).json() #we still need to process this information more
# print(response)
# print()
# print(json.dumps(response, indent=1)) #Here we se ethe items in the
#
# for a in response:
#     print(a["show"]["name"])
#     print(f"show start: {a["show"]["premiered"]}")

# Error Handling

keyword = "girls"
request = "https://api.tvmaze.com/search/shows?q=" + keyword  # notice its not www, but api.?

try:
    response = requests.get(request)  # we still need to process this information more
    if response.status_code==200: #testing the status code
        json_response = response.json() #turning the json file into python
        for a in json_response:
            print(a["show"]["name"])
            print(f"show start: {a["show"]["premiered"]}")

except ValueError:
    print("Request could not be completed")

# First you use .get method
# Then you check the status code if its 200 (success)
# then you create a new variable that .json your original request (turning it into a python code)
# now you can use it, but you have to use it via the new variable