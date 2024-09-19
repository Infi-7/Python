import requests


class FlightData:

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            return access_token
        else:
            raise Exception(f"Error getting access token: {response.status_code}, {response.text}")
