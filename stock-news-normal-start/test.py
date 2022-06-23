import csv
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?'
parameters = {
    "function": "TIME_SERIES_INTRADAY_EXTENDED",
                "symbol":"TSLA",
                         "interval":"60min",
                                    "slice":"year1month1",
                                            "apikey":""
}
with requests.Session() as s:
    download = s.get(url=CSV_URL,params=parameters)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)