import requests
from flask import current_app


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key = current_app.config['OPENWEATHER_KEY']

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru',
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None
