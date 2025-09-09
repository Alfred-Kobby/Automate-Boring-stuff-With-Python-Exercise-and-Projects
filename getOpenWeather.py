#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
APPID = 'API_KEY'
import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.

url1 = 'http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=1&APPID=%s' % (location,APPID)
response1 = requests.get(url1)
response1.raise_for_status()
# Uncomment to see the raw JSON text:
print(response1.text)
# Load JSON data into a Python variable.
cordinateData = json.loads(response1.text)
# Print weather descriptions.
lat = cordinateData[0].get("lat")
long = cordinateData[0].get("lon")

url = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&cnt=1&APPID=%s' % (lat, long, APPID)
print(url1)
response = requests.get(url)
response.raise_for_status()
# Uncomment to see the raw JSON text:
print(response.text)
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData.get("weather")
print('Current weather in %s:' % location)
print(w[0].get("main"), '-', w[0].get("description"))
print()
# print('Tomorrow:')
# print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
# print()
# print('Day after tomorrow:')
# print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
