import requests

url_api = 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=pa5B9u3YGrAtMfqXYULQ6fxPRZI900xW'
weather_req = requests.get(url_api)
weather_json = weather_req.json()

# Use the json response to show it works
print(weather_json)

# Read the data and figure out how to use the data for retail application
