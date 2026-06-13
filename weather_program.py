#!/usr/bin/env python3
import requests
import yagmail
import os
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
PASSWORD = os.getenv("PASSWORD")

def fetch_weather(latitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]
    else:
        print(f"Debug Info:  {response.status_code}, Response: {response.text}")
        return None



if __name__ == "__main__":
    lat = 44.69025828
    lon = 42.08468122
    temp = fetch_weather(lat, lon)
    if temp is not None:
        body = f"ტემპერატურა არის {temp}°C"
        yg = yagmail.SMTP("gorgadze420@gmail.com",f"{PASSWORD}")
        yg.send(
            to="avsajanishvilinikol@gmail.com",
            subject="შეტყობინება",
            contents=body
        )
        print("Email sent.")
    else:
        print("Failed to fetch weather data.")

