import requests
import json

# Load data from input.json file
with open('app/input.json', 'r') as file:
    data = json.load(file)

# URL of deployed API
url = 'https://predict-khkn75yyfq-lm.a.run.app/predict'

# Sending a POST request
response = requests.post(url, json=data)

# Checking the success of the request
if response.status_code == 200:
    # Output of the result
    print('Response:', response.json())
else:
    print('Failed to get a valid response. Status code:', response.status_code)
    print('Response:', response.text)
