import spotipy
from spotipy.oauth2 import SpotifyOAuth
from playlist_logic import determine_next_song

class MusicController:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                                            client_secret="YOUR_CLIENT_SECRET",
                                                            redirect_uri="http://localhost:8888/callback",
                                                            scope="user-read-playback-state,user-modify-playback-state"))

    def get_next_song(self, telemetry_data):
        # Determine the next song based on telemetry
        next_song = determine_next_song(telemetry_data)
        # Play the song using Spotify API
        self.play_song(next_song)
        return next_song

    def play_song(self, song_uri):
        self.sp.start_playback(uris=[song_uri])
