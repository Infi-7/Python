import requests
import datetime

today_datetime = datetime.datetime.now()
today_day = today_datetime.strftime("%d")
today_month = today_datetime.strftime("%m")
today_year = today_datetime.strftime("%Y")

individual_entry = f"{today_year}{today_month}{today_day}"
final_dates = individual_entry.replace(",", "")


USERNAME = "infi7"
TOKEN = "asdsafsfjpdfjsvmwmeor0756"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": ID,
    "name": "Characters Learned Graph",
    "unit": "commits",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
print(pixel_post_endpoint)
pixel_config = {
    "date": "20240913",
    "quantity": "20",
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
# print(response.text)
yes_date = "20240914"
# Update Pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{yes_date}"
print(update_endpoint)
update_config = {
    "quantity": "5",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{final_dates}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response)
