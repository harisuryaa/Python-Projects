import requests
from twilio.rest import Client
STOCK_NAME = "NFLX"
COMPANY_NAME = "Netflix Inc"

account_sid =""
auth_token = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK= ""
API_NEWS = ""

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":API_KEY_STOCK,
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


response = requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()
daily_data=data["Time Series (Daily)"]

close_value=  [value for (key, value) in daily_data.items()]
yesterday_close=close_value[0]['4. close']

daybefore_close=close_value[1]['4. close']
print(yesterday_close,daybefore_close)

difference = abs(float(yesterday_close)-float(daybefore_close))

print(difference)

diff_percent = (difference/float(yesterday_close))*100
print(diff_percent)



    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if difference >= 1.5 :
    news_params = {
        # "searchIn":"title",
        "apikey":API_NEWS,
        "q": COMPANY_NAME,
        # "qInTitle":COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_params)
    news_data=news_response.json()
    articles=news_data["articles"]




    first_3 = articles[:3]
# print(first_3)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    list_art = [f"Headline: {value['title']} \n Description: {value['description']}" for value in first_3]
    list_art.append(f" Yesterday close {yesterday_close}\nDaybefore close {daybefore_close}")
    # print(list_art)
    client = Client(account_sid, auth_token)
    for arti in list_art:
        message = client.messages.create(
            body=arti,
            from_='whatsapp:',
            to='whatsapp:+919944421125')

        print(message.status)
