import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"


class WeatherAPIError(Exception):
    pass


def fetch_weather(city: str, days: int = 3) -> dict:
    url = f"{BASE_URL}/forecast.json"
    params = {"key": API_KEY, "q": city, "days": days, "aqi": "yes"}

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise WeatherAPIError(f"Network error: {e}")

    data = response.json()
    if "error" in data:
        raise WeatherAPIError(data["error"].get("message", "Unknown API error"))

    return _shape_weather_data(data)


def _shape_weather_data(data: dict) -> dict:
    local_time = datetime.strptime(data["location"]["localtime"], "%Y-%m-%d %H:%M")

    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "region": data["location"]["region"],
        "localtime": local_time.strftime("%a, %d %b %Y %I:%M %p"),

        "temperature": data["current"]["temp_c"],
        "feelslike": data["current"]["feelslike_c"],
        "condition": data["current"]["condition"]["text"],
        "icon": data["current"]["condition"]["icon"],

        "humidity": data["current"]["humidity"],
        "wind_speed": data["current"]["wind_kph"],
        "pressure": data["current"]["pressure_mb"],
        "visibility": data["current"]["vis_km"],
        "uv_index": data["current"]["uv"],
        "cloud": data["current"]["cloud"],
        "air_quality": data["current"].get("air_quality", {}),

        "forecast": _shape_forecast(data["forecast"]["forecastday"]),
        "sunrise": data["forecast"]["forecastday"][0]["astro"]["sunrise"],
        "sunset": data["forecast"]["forecastday"][0]["astro"]["sunset"],
    }


def _shape_forecast(forecast_days: list) -> list:
    return [
        {
            "label": datetime.strptime(day["date"], "%Y-%m-%d").strftime("%a"),
            "icon": day["day"]["condition"]["icon"],
            "condition": day["day"]["condition"]["text"],
            "high": day["day"]["maxtemp_c"],
            "low": day["day"]["mintemp_c"],
        }
        for day in forecast_days
    ]