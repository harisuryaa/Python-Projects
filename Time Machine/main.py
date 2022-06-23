from bs4 import BeautifulSoup

import requests


date = input("what year you would like to travel to in YYY-MM-DD format: ")

# URL= f"https://www.billboard.com/charts/hot-100/{date}/"
# print(URL)
URL= "https://www.billboard.com/charts/hot-100/2000-08-10/"

response = requests.get(URL)
webpage = response.text
# print(webpage)
soup= BeautifulSoup(webpage,"html.parser")
data=soup.find_all(name="h3")
song_names = [song.getText() for song in data]
# print(song_names)

list=[movie.replace("\n","") for movie in song_names]
list=[movie.replace("\t","") for movie in list]
list=[movie.replace("Songwriter(s):","") for movie in list]
list=[movie.replace("Producer(s):","") for movie in list]
list=[movie.replace("Imprint/Promotion Label:","") for movie in list]

# slice unwanted data
data= list[8::]
list_all=data[3::4]

#insert all songs
list_songs=[]
list_songs.append(list[0])
list_songs.extend(list_all)

#first 100 name
first_100=list_songs[:100:]

print(first_100)



# -----

from pprint import pprint

year = date.split("-")[0]

C_ID=""
C_SRT=""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=C_ID,
        client_secret=C_SRT,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)
songs_link=[]
for song_name in first_100:
    songs=sp.search(type="track",q=f"track:{song_name}")
    # pprint(songs)
    try:
        uri = songs["tracks"]["items"][0]["uri"]
        songs_link.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100 Hari", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_link)

# pl=sp.user_playlists(user=user_id)
# pprint(pl)
#     # songs_link.append(uri)
#
# print(songs_link)
# delete=[]