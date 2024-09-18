import requests

# Amadeus API credentials
API_KEY = 'VAJdC2RCrxxxl4uGbsFfVnxT6k9EHJnf'
API_SECRET = 'DAq7Zy9rReIe8BQt'


# Step 1: Get access token
def get_access_token():
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': API_SECRET
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Error getting access token: {response.status_code}, {response.text}")


# Step 2: Make API request using the access token
def make_api_request():
    access_token = get_access_token()

    url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'  # Example endpoint
    headers = {
        'Authorization': f'Bearer {access_token}',  # Use Bearer token
        'Content-Type': 'application/json'
    }

    params = {
        # Example query parameters
        'originLocationCode': 'MAD',
        'destinationLocationCode': 'NYC',
        'departureDate': '2024-10-10',
        'adults': 1
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error making API request: {response.status_code}, {response.text}")


# Step 3: Execute the API request and print the result
if __name__ == "__main__":
    try:
        result = make_api_request()
        print(result)
    except Exception as e:
        print(str(e))
