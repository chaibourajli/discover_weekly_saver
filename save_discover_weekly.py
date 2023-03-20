import spotipy
import datetime
from spotipy.oauth2 import SpotifyOAuth
import os

# Load the environment variables
from dotenv import load_dotenv
load_dotenv()

# Define the necessary environment variables
username = os.getenv('SPOTIFY_USERNAME')
playlist_id = os.getenv('SPOTIFY_PLAYLIST_ID')

# Authenticate with Spotify
scope = 'playlist-read-private playlist-modify-public'
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get the tracks from the Discover Weekly playlist
discover_weekly = sp.user_playlist_tracks(user=username, playlist_id=playlist_id)

# Extract the track URIs
track_uris = [track['track']['uri'] for track in discover_weekly['items']]

# Save the track URIs to a new playlist
today = datetime.datetime.now()
new_playlist_name = f"Discover Weekly {today.strftime('%m/%d/%Y')}"
new_playlist = sp.user_playlist_create(user=username, name=new_playlist_name)
sp.playlist_add_items(playlist_id=new_playlist['id'], items=track_uris)
