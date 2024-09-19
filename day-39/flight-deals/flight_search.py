from flight_data import FlightData
import requests

api_key = "VAJdC2RCrxxxl4uGbsFfVnxT6k9EHJnf"
api_secret = "DAq7Zy9rReIe8BQt"


class FlightSearch:
    def __init__(self):
        self.access_token = None

    def make_request(self, endpoint, params):
        if self.access_token is None:
            self.access_token = FlightData(api_key, api_secret).get_token()

        url = f'https://test.api.amadeus.com{endpoint}'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error making API request: {response.status_code}, {response.text}")


    endpoint = '/v2/shopping/flight-offers'
    params = {
        'originLocationCode': 'MAD',
        'destinationLocationCode': 'BKK',
        'departureDate': '2024-10-10',
        'adults': 1}

    fl = FlightData(api_key, api_secret)

