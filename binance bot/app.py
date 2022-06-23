from flask import Flask, render_template
app = Flask(__name__)
import csv
from binance.client import Client


API_KEY = ""
SECRET_KEY=""

client = Client(API_KEY, SECRET_KEY)
info= client.get_account()
balance = info['balances']
print(balance)

@app.route('/')
def home():
    title = "CoinView"

    info= client.get_account()
    balance = info['balances']
    print(balance)
    return render_template("index.html", title=title, my_balances=balance)

@app.route('/buy')
def buy():
    return "buy"

@app.route('/sell')
def sell():
    return "sell"

@app.route('/settings')
def settings():
    return "settings"

if __name__ == "__main__":
    app.run(debug=True)
