import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

is_pos = (longitude, latitude)
print(is_pos)
