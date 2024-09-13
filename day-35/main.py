import requests

KEY = "2b877cfbea9f8de6577978ccdb62f0ba"
LATITUDE = 19.393345
LONGITUDE = 72.862427
URL = "https://api.openweathermap.org/data/2.5/forecast"
CNT = 4
weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": KEY,
    "cnt": 4
}

id_entries = []
weather_entries = []
response = requests.get(URL, params=weather_params)

for x in range(0, CNT):
    data_id = response.json()["list"][x]["weather"][0]["id"]
    data_weather = response.json()["list"][x]["weather"][0]["description"]
    id_entries.append(data_id)
    weather_entries.append(data_weather)

for x in id_entries:
    if x < 700:
        print("Bring an Umbrella")
        break