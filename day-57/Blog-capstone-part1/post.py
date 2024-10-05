import requests
from urllib3 import request


class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.url)

    def post_maker(self):
        data = self.response.json()
        body = data['body']