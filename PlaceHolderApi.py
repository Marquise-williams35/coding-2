import requests

url= 'https://bored-api.appbrewery.com/random'
response = requests.get(url)

print(response.json())

url2= 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url2)

print(response.json())
