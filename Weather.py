import requests

BASE_URL = "https://wttr.in"

def get_weather(city):
    url = f"{BASE_URL}/{city}?format=3"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text

        return "Sorry, I couldn't get the weather."

    except Exception:
        return "Weather service unavailable."
