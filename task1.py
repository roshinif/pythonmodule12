import requests

url = "https://api.chucknorris.io/jokes/random"


response = requests.get(url)
data = response.json()
joke = data['value']
print(joke)