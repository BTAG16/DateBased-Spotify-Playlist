import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def get_track_uri(songer):
    results = sp.search(q=songer, limit=1, type="track")
    tracks = results["tracks"]["items"]
    if tracks:
        return tracks[0]["uri"]
    return None

hot_100 = []
DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "https://example.com/"
scope = "playlist-modify-private"

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope
    )
)
user_id = sp.current_user()["id"]

playlist = {
    "name": f"Hot 100 Songs from {DATE}",
    "description": "Listen and be Blessed",
    "public": False
}

URL = f"https://www.billboard.com/charts/hot-100/{DATE}"
response = requests.get(URL, headers=header)
chart_page = response.text

soup = BeautifulSoup(chart_page, "html.parser")
song_titles = soup.select("li h3")
for song in song_titles[:100]:
    song_title = song.getText().strip()
    hot_100.append(song_title)

new_playlist = sp.user_playlist_create(user=user_id, name=playlist["name"],
                                       description=playlist["description"],
                                       public=playlist["public"])

for music in hot_100:
    track_uri = get_track_uri(music)
    if track_uri:
        sp.playlist_add_items(playlist_id=new_playlist["id"],
                              items=[track_uri])

print(f"Playlist '{playlist['name']}' created successfully!")