import requests
import queue
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&languages=ta"

# Write your code below this line 👇
response = requests.get(url=URL)
web_data=response.text
# print(web_data)


soup = BeautifulSoup(web_data,"html.parser")

name = soup.find_all(name="h3",class_="lister-item-header")


movies =[movie.getText() for movie in name]

sp= [movie.replace("\n","") for movie in movies]

print(sp)

with open("tamil_movies.txt", "a")as f:
    for names in sp:
        f.write(f"{names}\n")
