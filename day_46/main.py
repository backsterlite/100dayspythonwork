import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
# from pprint import pp
from collections import namedtuple

songs_date = input("Enter date in format YYYY-mm-dd: ")
SPOTIFY_CLIENT_ID = 'f0aecd704a1f4371bf3dbb5ffe69d648'
SPOTIFY_CLIENT_SECRET = '6546bebc1e2f4e6e9f0a64611e9a18e2'
SPOTIFY_REDIRECT_URL = 'http://example.com'
# Grab list of 100 most popular songs by date
url = f"https://www.billboard.com/charts/hot-100/{songs_date}/"
songs_page = requests.get(url).text
song_html = BeautifulSoup(songs_page, 'html.parser')
songs = [song.getText().strip() for song in song_html.select('.o-chart-results-list-row h3#title-of-a-story')]
artists = [artist.find_next().getText().strip() for artist in song_html.select('.o-chart-results-list-row h3#title-of-a-story')]

Song = namedtuple('Song', ('track', 'artist'))
album = [Song(track, artist) for track, artist in zip(songs, artists)]

scope = 'playlist-modify-private'
sp = spotipy.Spotify(
    oauth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URL,
            scope=scope,
            show_dialog=True
    ))
spotify_uris = []
user = sp.current_user()
year = songs_date.split('-')[0]
for song in songs:
    track = sp.search(f"track:{song} year:{year}", limit=1)
    try:
        spotify_uris.append(track['tracks']['items'][0]['uri'])
    except KeyError:
        continue


playlist = sp.user_playlist_create(user['id'], f'{songs_date} Billboard 100', public=False)
result = sp.playlist_add_items(playlist_id=playlist['id'], items=spotify_uris)
