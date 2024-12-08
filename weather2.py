import requests
import json
import os
from api_mapping import ApiMapping

def weather_info(city, x, a):
    api_mapping_file = 'api_mapping.json'
    api_id = "default"
    if len(a) != 0:
        api_id = a
    api = ApiMapping(api_mapping_file)
    api.load_mapping()
    api_url = api.get_formed_url(api_id, city)
    api.load_fields(api_id)

    r = requests.get(api_url)
    api_json = json.loads(r.text)
    w = api.parse_fields(api_json)

    if x == 'r':
        print(f"The current weather in {city} is {w["temp"]} degrees Celsius.")
        print(f"The current weather in {city} is {w["temp_f"]} degrees Fahrenheit.")
        print(f"The current weather in {city} has {w["wind_mph"]} mph wind speed.")
        print(f"The current weather in {city} has {w["wind_kph"]} kph wind speed.")
        print(f"The current weather in {city} has {w["humidity"]}% humidity.")
        print(f"The current weather in {city} has {w["cloudcover"]}% cloud coverage.")
    elif x == 'l':
        os.system(f"say 'The current weather in {city} is {w["temp"]} degrees Celsius.'")
        os.system(f"say 'The current weather in {city} is {w["temp_f"]} degrees Fahrenheit.'")
        os.system(f"say 'The current weather in {city} has {w["wind_mph"]} mph wind speed.'")
        os.system(f"say 'The current weather in {city} has {w["wind_kph"]} kph wind speed.'")
        os.system(f"say 'The current weather in {city} has {w["humidity"]}% humidity.'")
        os.system(f"say 'The current weather in {city} has {w["coudcover"]}% cloud coverage.'")
    else:
        print("Please enter a valid option ('r' to read or 'l' to listen).")

# Example usage
city= input("Enter the name of the city:\n")
x = input("Enter 'r' to read the weather information or 'l' to listen:\n")
a = input("Enter/Return for the default api or the API id: \n")
weather_info(city, x, a)

# Example use cases
# 'PHL' / 'r' or 'l' / 'Enter' or 'default'
# 'Philadelphia' / 'r' or 'l' / 'visualcrossing.com'
# 'PHL' / 'r' or 'l' / 'weatherstack.com'