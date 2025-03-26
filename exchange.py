import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("EXCHANGE_API_KEY")

if not API_KEY:
    print("Error: API key not found in .env file.")
    exit()

# Define API endpoints and assign them to variables
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"
UR_URL = f"{BASE_URL}/pair/USD/RWF"
UN_URL = f"{BASE_URL}/pair/USD/NGN"
NR_URL = f"{BASE_URL}/pair/NGN/RWF"

def get_exchange_rates():
    # Make separate requests for each URL
    response_usd_rwf = requests.get(UR_URL)
    response_usd_ngn = requests.get(UN_URL)
    response_ngn_rwf = requests.get(NR_URL)

    # Check if each response is successful
    if response_usd_rwf.status_code == 200 and response_usd_ngn.status_code == 200 and response_ngn_rwf.status_code == 200:
       
        # Extract JSON data from each response
        data_usd_rwf = response_usd_rwf.json()
        data_usd_ngn = response_usd_ngn.json()
        data_ngn_rwf = response_ngn_rwf.json()

        # Extract conversion rates from the response data
        rates = {
            'USD/RWF': data_usd_rwf['conversion_rate'],
            'NGN/RWF': data_ngn_rwf['conversion_rate'],
            'USD/NGN': data_usd_ngn['conversion_rate']
        }
        # Get the current script directory
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Set the path for the JSON file in the script's directory
        json_file_path = os.path.join(script_directory, 'exchange_rates.json')

         # Write rates to a JSON file
        with open(json_file_path, 'w') as file:
            json.dump(rates, file)

        print(f"Exchange rates saved to {json_file_path}")
        
    else: 
        print(f"Error: Failed to fetch exchange rates. Status codes: {response_usd_rwf.status_code}, {response_usd_ngn.status_code}, {response_ngn_rwf.status_code}")
        exit()


# Fetch and save rates
if __name__ == '__main__':
    get_exchange_rates()