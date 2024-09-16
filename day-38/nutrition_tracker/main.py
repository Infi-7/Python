import requests
import datetime

APP_ID = "260286a7"
API_KEY = "7706b816a5f75ca8833a8e076d6a2088"

SHEETY_URL = "https://api.sheety.co/8530a807122d7886075f4e4ab96e350c/myWorkouts/workouts"
HOST = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"
"""
user_input = input("Enter Query: ")

send_config = {
    "query": user_input
}
"""
header = {
    "x-app-id": "260286a7",
    "x-app-key": "7706b816a5f75ca8833a8e076d6a2088"
}
"""
response_nutri = requests.post(url=f"{HOST}{ENDPOINT}", headers=header, json=send_config)
result_nutri = response_nutri.json()
print(result_nutri)
"""

temp = {'exercises': [{'tag_id': 63, 'user_input': 'swam', 'duration_min': 60, 'met': 6, 'nf_calories': 420, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 18310, 'name': 'swimming', 'description': None, 'benefits': None}]}
dir = temp["exercises"][0]
print(dir)

task = dir["user_input"]
dur = dir["duration_min"]
calories = dir["nf_calories"]
print(task)
print(dur)
print(calories)

day_time_info = datetime.datetime.now()
date_now = day_time_info.strftime(format=("%d/%m/%Y"))
time_now = day_time_info.strftime(format=("%H:%M:%S"))

print(date_now)
print(time_now)

name = "Infi_7"
password = "aniketpassword"
consumer_key = "Authorization"
consumer_secret = "bnVsbDpudWxs"

sheety_header = {"Authorization","Basic bnVsbDpudWxs"}

data = {
    "password": password,
    "username": name,
    "password": password
}
post_json = {
    "Date": date_now,
    "Time": time_now,
    "Exercise": task,
    "Duration": dur,
    "Calories": calories
}


response_sheety = requests.post(url=SHEETY_URL, data=data, headers=sheety_header)
print(response_sheety.text)
