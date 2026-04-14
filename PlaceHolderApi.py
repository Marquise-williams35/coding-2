import requests

query = 'https://pokeapi.co/api/v2/pokemon/rattata/'
response = requests.get(query)


if response.status_code == 200:
    data = response.json()
    
    filtered_data = {
        "name": data["name"],
        "height":data["height"],
        "weight":data["weight"],
        "types":data["types"]
     }
    print(filtered_data)
else:
    print('data not found')    
    print(response.status_code)
    





#url= 'https://bored-api.appbrewery.com/random'
#response = requests.get(url)

#print(response.json())

#url2= 'https://pokeapi.co/api/v2/pokemon/Rattata '
#response2 = requests.get(url2)

#print(response2.json())








