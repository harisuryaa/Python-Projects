import requests
#
# base_url = "https://api.binance.com"
# path= '/api/v3/account'
#
#
#
# header={
#     'APIkey':'',
#     'SECRETkey':''
# }
#
# response = requests.get(url=base_url+path,headers=header)
# print(response.json())


url = 'https://api.wazirx.com/sapi/v1/ticker/24hr?symbol=wrxinr'

response = requests.get(url=url)
d=response.json()
print(d)