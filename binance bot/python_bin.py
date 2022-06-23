import csv
from binance.client import Client


API_KEY = ""
SECRET_KEY=""

# client = Client(API_KEY, SECRET_KEY)

client = Client(API_KEY, SECRET_KEY)

# balance = client.get_asset_balance(asset='USDT')
#
# order = client.order_market_buy(
#     symbol='BTCUSDT',
#     quantity=0.00003)

interval = "1 day ago UTC"
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_15MINUTE, interval)

print(klines)

with open(f'{interval}.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    for data in klines:
        spamwriter.writerow(data)

