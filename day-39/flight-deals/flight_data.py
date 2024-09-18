import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, api_key, api_secret):
        self.ENDPOINT_TOKEN = 'https://test.api.amadeus.com'
        self.TOKEN_API_KEY = api_key
        self.TOKEN_API_SECRET = api_secret
        self.access_token = None

    def get_access_token(self):

        post_endpoint = f'{self.ENDPOINT_TOKEN}/v1/security/oauth2/token/'
        print(post_endpoint)

        token_header = {
            'content-type': 'application/x-www-form-urlencoded'
        }

        token_data = {
            'grant_type': 'client_credentials',
            'client_id': self.TOKEN_API_KEY,
            'client_secret': self.TOKEN_API_SECRET
        }

        response = requests.post(url=post_endpoint, headers=token_header, params=token_data)
        if response.status_code == 200:
            self.access_token = response.json().get('access_token')
        else:
            raise Exception(f"Error getting access token: {response.status_code}, {response.text}")

    def make_api_request(self, endpoint, params):
        if self.access_token is None:
            self.get_access_token()

        url = f"https://test.api.amadeus.com{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.access_token}',  # Use Bearer token
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error making API request: {response.status_code}, {response.text}")


if __name__ == "__main__":
    # Step 1: Initialize the API with your credentials
    api_key = 'VAJdC2RCrxxxl4uGbsFfVnxT6k9EHJnf'
    api_secret = 'DAq7Zy9rReIe8BQt'

    amadeus_api = FlightData(api_key, api_secret)

    # Step 2: Make a request to a specific API endpoint
    endpoint = '/v2/shopping/flight-offers'  # Example endpoint
    params = {
        "originLocationCode": "SYD",
        "destinationLocationCode ": "BKK",
        "departureDate": "2024-09-25",
        "adults": 1
    }

    try:
        response = amadeus_api.make_api_request(endpoint, params)
        print(response)
    except Exception as e:
        print(str(e))
