import requests
from datetime import datetime

MY_LAT = [19.391928 - 5, 19.391928 + 5]
MY_LONG = [72.839729 - 5, 72.839729 + 5]
FORMAT = 0


response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
data_iss = response_iss.json()

longitude = response_iss.json()["iss_position"]["longitude"]
latitude = response_iss.json()["iss_position"]["latitude"]


is_pos = (longitude, latitude)
print(is_pos)

parameters = {
    "lat": 19.391928,
    "lng": 72.839729,
    "formatted": FORMAT,
}


response = requests.get("https://api.sunrise-sunset.org/json",
                       params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print("Sunrise: ", sunrise)
print("Sunset: ", sunset)

print("Time in hours: ", time_now.hour)


if MY_LAT[1] > round(float(latitude)) > MY_LAT[0] and MY_LONG[1] > round(float(longitude)) > MY_LONG[0]:
    print("over you")
