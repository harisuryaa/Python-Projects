import requests
from _datetime import datetime

from requests.auth import HTTPBasicAuth

APP_ID = ""
APP_KEY = ""
SHEET_ENDPOINT = "https://api.sheety.co/"
EXERCISES_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_USERNAME=""
SHEET_PASS = ""
header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
entry = input("Tell me what you did today ? ")

params = {
    "query": entry,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=EXERCISES_ENDPOINT, json=params, headers=header)
result = response.json()
print(result)
# upload data to gsheet
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
print(today_date)

#
for exercises in result['exercises']:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercises['name'].title(),
            "duration": exercises['duration_min'],
            "calories": exercises['nf_calories']
        }
    }

    response_1 = requests.post(url=SHEET_ENDPOINT, json=sheet_input,auth=HTTPBasicAuth(SHEET_USERNAME, SHEET_PASS))

print(response_1.text)
