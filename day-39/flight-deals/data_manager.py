import requests
from flight_search import *

sheety_url = "https://api.sheety.co/8530a807122d7886075f4e4ab96e350c/flightDeals/prices"
endpoint = '/v2/shopping/flight-offers'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, url):
        self.url = url
        self.response_json = None
        self.data = None

    def data_collector(self):
        response = requests.get(url=self.url)
        self.response_json = response.json()["prices"]
        return self.response_json

    def data_manager(self):
        if self.response_json is None:
            self.data = DataManager(sheety_url).data_collector()

            for x in range(len(self.data)):
                iata_code = self.data[x]["iataCode"]
                params = {
                    'originLocationCode': 'BOM',
                    'destinationLocationCode': f'{iata_code}',
                    'departureDate': '2024-10-10',
                    'adults': 1}
                current_lowest_price = self.data[x]["lowestPrice"]

                data = FlightSearch().make_request(endpoint, params)
                lst = [float(data["data"][x]["price"]["total"]) for x in range(len(data["data"]))]

                if current_lowest_price > min(lst):
                    print("new lowest!")  # and send notification


                '''if self.data[x]["lowestPrice"] > 
                price = self.data[x]["lowestPrice"]
                print(price)'''


        '''flight_search = FlightSearch().make_request(endpoint, params)
        flight_search_response = flight_search
        print(response)'''


DataManager(sheety_url).data_manager()
