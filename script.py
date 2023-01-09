import requests

weather_api = "https://wttr.in/"
cities = ["Лондон", "Шереметьево", "Череповец"]
payload = {"nTqM": "", "lang": "ru"}
result = []
for city in cities:
    result.append(weather_api + city)
for url in result:
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
