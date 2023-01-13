import requests
from urllib.parse import urljoin

weather_api = "https://wttr.in/"
cities = ["Лондон", "Шереметьево", "Череповец"]
payload = {"nTqM": "", "lang": "ru"}
for city in cities:
    response = requests.get(urljoin(weather_api, city), params=payload)
    response.raise_for_status()
    print(response.text)