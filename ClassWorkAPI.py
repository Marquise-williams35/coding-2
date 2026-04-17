import requests

store = 'https://fake-store-api.mock.beeceptor.com/api/products'
response = requests.get(store)


if response.status_code == 200:
    data = response.json()
    
    filtered_data = {
        "product_id": data["product_id"],
        "name":data["name"],
        "description":data["description"],
        "price":data["price"]
     }
    print(filtered_data)
else:
    print('data not found')    
    print(response.status_code)