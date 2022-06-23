import datetime
import time
import requests

now = datetime.datetime.now()

print(now.year)

name = ("hari").title()
inpt = {"name": name}

response = requests.get(url='https://api.agify.io?', params=inpt)
response2 = requests.get(url="https://api.genderize.io/?", params=inpt)

age_data = response.json()["age"]
gender_data = response2.json()['gender']

print(age_data, gender_data)
