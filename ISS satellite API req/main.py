import requests


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#
# data=response.json()
# long=data["iss_position"]["longitude"]
# lat=data["iss_position"]["latitude"]
# print((long,lat))
#
MY_LAT = 17.4168234206376
MY_LONG = 78.31061770706108

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
'formatted':0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()
sunraise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunset,sunraise)