import requests
from geopy.geocoders import Nominatim

municipality = input("Enter a municipality: ")
geolocator = Nominatim(user_agent="my-app")
location = geolocator.geocode(municipality)

lat, lon = location.latitude, location.longitude
API_KEY = "38c827c937bb1760ede31b0082d5b688"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
weather_description = data["weather"][0]["description"]
temperature = data["main"]["temp"]
print(f"Weather description: {weather_description}")
print(f"Temperature: {temperature}")

