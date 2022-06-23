import os
from twilio.rest import Client
import requests
account_sid =""
auth_token =""


# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

parameters = {
    "lat": 11.803750005558284,
    "lon": 77.73489632628073,
    "appid": "",
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][:12]

will_rain= False

for current in hourly_data:
    condition= current["weather"][0]["id"]
    print(condition)
    # if condition < 800:

will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="it will rain today ✨",
        from_='whatsapp:',
        to='whatsapp:+919944421125'
    )

    print(message.status)


api = ""
latt= 17.39950168802149
lonn=78.45691610074202

