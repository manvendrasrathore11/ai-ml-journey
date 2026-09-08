from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

DATE = input("Which year do you want to travel to ? type the data in this format YYYY-MM-DD")

URL = f"https://www.billboard.com/charts/hot-100/{DATE}"



header = {
"USER-AGENT"	:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url= URL , params=header )

web_billboard = response.text

SOUP = BeautifulSoup(web_billboard,"html.parser")

song_names_spans = SOUP.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.org/callback",
        client_id="7ca4ee8bb991460daf21d5b6a01cb468",
        client_secret="5ee4b2d8afc3458096973b88210d3dc5",
        show_dialog=True,
        cache_path="token.txt",
        username="Manvendra Singh",
    )
)
user_id = sp.current_user()["id"]

print(user_id)

# song_names1 = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = DATE.split("-")[0]
print(year)
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
