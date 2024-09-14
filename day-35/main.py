import requests
from twilio.rest import Client

KEY = "2b877cfbea9f8de6577978ccdb62f0ba"
LATITUDE = 19.393345
LONGITUDE = 72.862427
URL = "https://api.openweathermap.org/data/2.5/forecast"
CNT = 4
account_sid = "ACc145f1feaf6961edc7fddce6fa276666"
auth_token = "4c92718940e917ade54ade0664e5b6a4"


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
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔",
            from_="+12073557430",  # generated
            to="+917720834048",  # real
        )

        print(message.status)
        break
