import requests

URL = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"

response = requests.get(URL)
question_data = response.json()["results"]
