import requests
import json

# lat = input("Enter latitude: ")
# lat = 60.32
# # lon = input("Enter longitude: ")
# lon = 24.96

# city_name = input("Enter City Name: ")
city_name = "Helsinki"
print(f"City Name: {city_name}")
API_key = "1ab1bbab81fe83b9cf25c36a6c1db3e9"

request = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
response = requests.get(request)

try:
    # print(response.status_code)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response))
        print(f"Weather: {json_response["weather"][0]["description"]}")
        print(f"Temperature: {round(json_response["main"]["temp"] - 273.15, 2)}°C")
    else:
        print("Error Code: ")
        print(response.status_code)
except ValueError:
    print("Value Error")
