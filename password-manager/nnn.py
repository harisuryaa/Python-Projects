import json


with open("data.json") as file:
    dat = json.load(file)

print(dat)