from pprint import pprint

from binance.spot import Spot

client = Spot()

API_KEY = ""
SECRET_KEY=""

client = Spot(key=API_KEY, secret=SECRET_KEY)

# Get account and balance information
print(client.klines("BNBUSDT", "1h", limit=5))

data= client.account()

# pprint(data['balances'])
bal_data=data['balances']
print("hleeeeee")
for price in bal_data:
    if float(price['free']) >0:
        print(f"We have [{price['asset']} : {price['free']}] in wallet")