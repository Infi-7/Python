import requests

class Flight_Data:

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = None

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
            self.access_token = response.json().get('access_token')
        else:
            raise Exception(f"Error getting access token: {response.status_code}, {response.text}")

    def make_request(self, endpoint, params):
        if self.access_token is None:
            access_token = self.get_token()

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


if __name__ == "__main__":
    api_key = "VAJdC2RCrxxxl4uGbsFfVnxT6k9EHJnf"
    api_secret = "DAq7Zy9rReIe8BQt"

    api = Flight_Data(api_key, api_secret)

    endpoint = '/v2/shopping/flight-offers'
    params = {
        'originLocationCode': 'MAD',
        'destinationLocationCode': 'NYC',
        'departureDate': '2024-10-10',
        'adults': 1
    }
    try:
        response = api.make_request(endpoint, params)
        print(response)
    except Exception as e:
        print(str(e))
