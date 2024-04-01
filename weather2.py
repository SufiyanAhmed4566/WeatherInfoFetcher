import requests
import json
import os

def weather_info(city, x):
    url = f"http://api.weatherapi.com/v1/current.json?key=2f52d9bd7df943bfa5c110209242903&q={city}"
    r = requests.get(url)
    wdic = json.loads(r.text)

    w = wdic["current"]["temp_c"]
    w1 = wdic["current"]["temp_f"]
    w2 = wdic["current"]["wind_mph"]
    w3 = wdic["current"]["wind_kph"]
    w4 = wdic["current"]["humidity"]
    w5 = wdic["current"]["cloud"]

    if x == 'r':
        print(f"The current weather in {city} is {w} degrees Celsius.")
        print(f"The current weather in {city} is {w1} degrees Fahrenheit.")
        print(f"The current weather in {city} has {w2} mph wind speed.")
        print(f"The current weather in {city} has {w3} kph wind speed.")
        print(f"The current weather in {city} has {w4}% humidity.")
        print(f"The current weather in {city} has {w5}% cloud coverage.")
    elif x == 'l':
        os.system(f"say 'The current weather in {city} is {w} degrees Celsius.'")
        os.system(f"say 'The current weather in {city} is {w1} degrees Fahrenheit.'")
        os.system(f"say 'The current weather in {city} has {w2} mph wind speed.'")
        os.system(f"say 'The current weather in {city} has {w3} kph wind speed.'")
        os.system(f"say 'The current weather in {city} has {w4}% humidity.'")
        os.system(f"say 'The current weather in {city} has {w5}% cloud coverage.'")
    else:
        print("Please enter a valid option ('r' to read or 'l' to listen).")

# Example usage
city= input("Enter the name of the city:\n")
x = input("Enter 'r' to read the weather information or 'l' to listen:\n")
weather_info(city, x)

