import requests

responce = requests.get('https://api.chucknorris.io/jokes/random')
data = responce.json()

print(data['value'])