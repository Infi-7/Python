import requests
from flight_search import *

sheety_url = "https://api.sheety.co/8530a807122d7886075f4e4ab96e350c/flightDeals/prices"
endpoint = '/v2/shopping/flight-offers'
params = {
    'originLocationCode': 'MAD',
    'destinationLocationCode': 'BKK',
    'departureDate': '2024-10-10',
    'adults': 1}

fl = FlightSearch()



class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, url):
        self.url = url
        self.response_json = None

    def data_collector(self):
        response = requests.get(url=self.url)
        self.response_json = response.json()["prices"]
        return self.response_json

    def data_manager(self):
        if self.response_json is None:
            data = DataManager(sheety_url).data_collector()

            flight_search = FlightSearch()
            response = flight_search.make_request(endpoint, params)
            print(response)

