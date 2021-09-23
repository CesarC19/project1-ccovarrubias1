import flask
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
cid = os.getenv("SPOTIPY_CLIENT_ID")
secret = os.getenv("SPOTIPY_CLIENT_SECRET")
BASE_URL = os.getenv("SPOTIPY_REDIRECT_URL")

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


app = flask.Flask(__name__)

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:1]:
    print('track    : ' + track['name'])
    trackName= track['name']
    print('audio    : ' + track['preview_url'])
    preUrl= track['preview_url']
    print('cover art: ' + track['album']['images'][0]['url'])
    coverArt= track['album']['images'][0]['url']
    print()

@app.route("/")
def index():
    return flask.render_template("index.html")
    return render_template("trackName")

app.run(
    debug=True
)