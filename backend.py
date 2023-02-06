import requests

API_KEY = "b0d5d278a13e92c486b4e8b577187103"


def get_data(place, forecaset_days=None):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        filtered_data = data["list"]
        nr_value = 8 * forecaset_days
        filtered_data = filtered_data[:nr_value]
        return filtered_data
