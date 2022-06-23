import requests
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = ""
USER_NAME = ""

user_params = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_ID = "graph1"
graph_params={
    "id":GRAPH_ID,
    "name":"graph-cycling",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers =header)
# print(response.text)


today = datetime(year=2022, month=4, day=21)
time_now=today.strftime("%Y%m%d")
print(time_now)

request_endpoint= f"{graph_endpoint}/{GRAPH_ID}"
body_params = {
    "date":time_now,
    "quantity":"9.0"
}
#
# response = requests.post(url=request_endpoint,json=body_params,headers=header)
# print(response.text)

put_param={
    "quantity":"1.0"
}

put_endpoint = f"{request_endpoint}/{time_now}"
response = requests.post(url=request_endpoint,headers=header,json=body_params)
print(response.text)