import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
import time

# Spotify credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'

# Initialize Spotify API client
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_track_ids(playlist_id):
    track_ids = []
    results = sp.playlist(playlist_id)
    for item in results['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids

def get_track_features(track_id):
    track_info = sp.track(track_id)
    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    release_date = track_info['album']['release_date']
    length = track_info['duration_ms']
    popularity = track_info['popularity']

    return [name, album, artist, release_date, length, popularity]

# Ensure output folder exists
os.makedirs("songs", exist_ok=True)

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
music_dist = {
    0: "0l9dAmBrUJLylii66JOsHB",
    1: "1n6cpWo9ant4WguEo91KZh",
    2: "4cllEPvFdoX6NIVWPKai9I",
    3: "0deORnapZgrxFY4nsKr9JA",
    4: "4kvSlabrnfRCQWfN0MgtgA",
    5: "1n6cpWo9ant4WguEo91KZh",
    6: "37i9dQZEVXbMDoHDwVN2tF"
}

# Loop through emotion playlists and save data
for emotion, playlist_id in music_dist.items():
    track_ids = get_track_ids(playlist_id)
    track_list = []
    for track_id in track_ids:
        time.sleep(0.3)  # To avoid rate limits
        track_data = get_track_features(track_id)
        track_list.append(track_data)
    
    # Save to CSV
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'Release_date', 'Length', 'Popularity'])
    df.to_csv(f'songs/{emotion_dict[emotion].lower()}.csv', index=False)
    print(f"CSV for {emotion_dict[emotion]} generated.")
