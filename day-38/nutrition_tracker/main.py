import requests
import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "260286a7"
API_KEY = "7706b816a5f75ca8833a8e076d6a2088"

SHEETY_URL = "https://api.sheety.co/8530a807122d7886075f4e4ab96e350c/myWorkouts/workouts"
HOST = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"

user_input = input("Enter Query: ")

send_config = {
    "query": user_input
}

header = {
    "x-app-id": "260286a7",
    "x-app-key": "7706b816a5f75ca8833a8e076d6a2088"
}

response_nutri = requests.post(url=f"{HOST}{ENDPOINT}", headers=header, json=send_config)
result_nutri = response_nutri.json()

loc = result_nutri["exercises"][0]

task = loc["user_input"]
dur = loc["duration_min"]
calories = loc["nf_calories"]

day_time_info = datetime.datetime.now()
date_now = day_time_info.strftime(format=("%d/%m/%Y"))
time_now = day_time_info.strftime(format=("%H:%M:%S"))

name = "Infi_7"
password = "aniketpassword"
consumer_key = "Authorization"
consumer_secret = "bnVsbDpudWxs"

sheety_header = {
    'Content-Type': 'application/json',
    "Authorization": "Basic bnVsbDpudWxs"
}

basic = HTTPBasicAuth(username=name, password=password)

post_json = {
    "workout": {
    "date": date_now,
    "time": time_now,
    "exercise": task,
    "duration": dur,
    "calories": calories
    }
}

response_sheety = requests.post(url=SHEETY_URL, json=post_json, headers=sheety_header, auth=basic)
print(response_sheety.text)
