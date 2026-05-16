#!/usr/bin/env python3
import requests
from datetime import datetime
def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=062d36d7d581afb49808db1a37fe0ab4&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = (
       f"\nCity: {city}\n"
       f"Temperature: {temp}°C\n"
       f"Humidity: {humidity}%\n"
       f"Weather: {description.capitalize()}\n"
       f"Fetched at: {timestamp}\n"
        )
        return result
    else:
        error_msg = "Error: Could not fetch weather data."
        return error_msg
if __name__ == "__main__":
    city = "Dusheti"
    output = fetch_weather(city)
    with open("/home/nikol/weatherprogram/weather_log.txt", "a") as inp:
        inp.write(output + "\n")
