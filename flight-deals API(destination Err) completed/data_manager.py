from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT ="https://api.sheety.co///"
SHEET_USER_ENDPOINT= "https://api.sheety.co///"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    def get_customer_email(self):
        response =requests.get(url=SHEET_USER_ENDPOINT)
        data = response.json()
        self.custmer_email = data["users"]
        return self.custmer_email

users = DataManager()
list_u=users.get_customer_email()

emails = [row["email"] for row in list_u ]
name = [row["firstName"] for row in list_u]
print(emails,name)