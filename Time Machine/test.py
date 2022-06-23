from pprint import pprint

from bs4 import BeautifulSoup

import requests

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

songs=sp.search(type="track",q=f"track:{song_name}")
pprint(songs)