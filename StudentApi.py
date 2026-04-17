import requests

rick_morty='https://rickandmortyapi.com/api/character/1,183,2'
response = requests.get(rick_morty)

if response.status_code == 200:
    data = response.json()
    
    filtered_data ={
        "name":data["name"],
        "status":data["status"],
        "species":data["species"],
        "gender":data["gender"]
    }
    print(filtered_data)
else:
    print('data not found')    
    print(response.status_code)