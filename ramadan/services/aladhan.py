import requests

ALADHAN_URL = "https://api.aladhan.com/v1/timingsByCity"

def fetch_prayer_data(city, country="Bangladesh", method=1):
    params = {
        "city": city,
        "country": country,
        "method": method
    }
    response = requests.get(ALADHAN_URL, params=params)
    response.raise_for_status()
    return response.json()["data"]
