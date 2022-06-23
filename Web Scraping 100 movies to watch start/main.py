import requests_html
import queue
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_data=response.text
# print(web_data)


soup = BeautifulSoup(web_data,"html.parser")

name = soup.find_all(name="h3",class_="title")
movies =[movie.getText() for movie in name]
movie_formatted = movies[::-1]

with open("demofile2.txt", "a")as f:
    for names in movie_formatted:
        f.write(f"{names}\n")
