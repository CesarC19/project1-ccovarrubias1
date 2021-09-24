import flask
import os
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
cid = os.getenv("SPOTIPY_CLIENT_ID")
secret = os.getenv("SPOTIPY_CLIENT_SECRET")
BASE_URL = os.getenv("SPOTIPY_REDIRECT_URL")

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


app = flask.Flask(__name__)
#"Breaking Benjamin"
artList = ["Linkin Park", "Avenged Sevenfold", "Foo Fighters"]

LPURL = 'https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz?si=BPocwTzhSUWOKd3ZNX6vaA&dl_branch=1'
A7XURL = 'https://open.spotify.com/artist/0nmQIMXWTXfhgOBdNzhGOs?si=jL0sKoZ_QV6fVcSxmIsbvg&dl_branch=1'
FFURL = 'https://open.spotify.com/artist/7jy3rLJdDQY21OgRLCZ9sD?si=MxXrrzSmRz2oLpTuVHHIog&dl_branch=1'

randomArtist = random.choice(artList)

artistURL = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

if(randomArtist == "Linkin Park"):
    artistURL = LPURL

if(randomArtist == "Avenged Sevenfold"):
    artistURL = A7XURL

if(randomArtist == "Foo Fighters"):
    artistURL = FFURL


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artistURL)

for track in results['tracks'][:1]:
    trackName= track['name']
    preUrl= track['preview_url']
    coverArt= track['album']['images'][0]['url']

results = spotify.search(q='artist:' + randomArtist, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
    artistImage= artist['images'][0]['url']



@app.route("/")
def index():
    return flask.render_template("index.html", trackName=trackName, randomArtist=randomArtist, artistImage=artistImage,  preUrl=preUrl, coverArt=coverArt)



app.run(
    debug=True
)