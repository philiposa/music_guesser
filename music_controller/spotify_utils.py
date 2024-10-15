import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

# Initialize Spotify client with credentials from settings
def get_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET
    )
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example function to search for a track
def search_track(query):
    spotify = get_spotify_client()
    results = spotify.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'preview_url': track['preview_url']
        }
    return None
