import requests
from flight_search import *
from requests.auth import HTTPBasicAuth
from notification_manager import *

endpoint = '/v2/shopping/flight-offers'
return_list = []


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
            self.data = DataManager(self.url).data_collector()

            for x in range(len(self.data)):
                city = self.data[x]["city"]
                iata_code = self.data[x]["iataCode"]
                current_lowest_price = self.data[x]["lowestPrice"]
                params = {
                    'originLocationCode': 'BOM',
                    'destinationLocationCode': f'{iata_code}',
                    'departureDate': '2024-10-10',
                    'maxPrice': current_lowest_price,
                    'adults': 1}

                sheety_header = {
                    'Content-Type': 'application/json',
                    "Authorization": "Basic bnVsbDpudWxs"
                }

                name = "Infi_7"
                password = "aniketpassword"

                basic = HTTPBasicAuth(username=name, password=password)

                try:
                    data = FlightSearch().make_request(endpoint, params)
                except:
                    print("No flights under current lowest")
                else:
                    lst_price = [float(data["data"][x]["price"]["total"]) for x in range(len(data["data"]))]

                    if current_lowest_price > min(lst_price):
                        url = f"https://api.sheety.co/8530a807122d7886075f4e4ab96e350c/flightDeals/prices/{2 + x}"
                        body = {
                            "price": {
                                "city": city,
                                "iataCode": iata_code,
                                "lowestPrice": min(lst_price)
                            }
                        }

                        requests.put(url=url, json=body, headers=sheety_header, auth=basic)

                        formatted_body = f"\nNew Discount Offer\nThe flight to {body["price"]["city"]} with IATA Code {body["price"]["iataCode"]} has a discount totalling to {body["price"]["lowestPrice"]}."

                        notify = NotificationManager(formatted_body).notifier()

