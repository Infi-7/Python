import json

input_user = "Amazon"

with open("data.json", mode="r") as f:
    data = json.load(f)

print(data[input_user])

print(data[input_user]["password"])
