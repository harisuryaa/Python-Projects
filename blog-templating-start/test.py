import requests

response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
data=response.json()
print(data)

