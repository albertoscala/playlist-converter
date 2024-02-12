import base64
import requests
import json


# Import credentials
from credentials import credentials


# ERRORS
class FailedAuthentication(Exception):
    pass


# SPOTIFY
CLIENT_ID_SPOTIFY = credentials.get('CLIENT_ID_SPOTIFY')
CLIENT_SECRET_SPOTIFY = credentials.get('CLIENT_SECRET_SPOTIFY')


# Get spotify api token
def get_spotify_token():
    auth_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Authorization': 'Basic ' + (base64.b64encode((CLIENT_ID_SPOTIFY + ':' + CLIENT_SECRET_SPOTIFY).encode('ascii'))).decode('ascii')
        },
        'form': {
            'grant_type': 'client_credentials'
        }
    }

    return requests.post(auth_options['url'], data=auth_options['form'], headers=auth_options['headers']).json()['access_token']


# Get playlist tracks
def get_playlist_tracks(playlist_id, spotify_token):
    tracks_request = {
        'url': 'https://api.spotify.com/v1/playlists/' + playlist_id,
        'headers': {
            'Authorization': 'Bearer ' + spotify_token,
        }
    }

    res = requests.get(tracks_request['url'], headers=tracks_request['headers']).json()
    
    # Create the list of tracks
    tracks = []
    for track in res['tracks']['items']:
        artist_name = ""
        for artist in track['track']['artists']:
            artist_name += artist['name'] + " "
        tracks.append(track['track']['name'] + " " + artist_name)    

    # Return the list of tracks
    return tracks


# YOUTUBE
API_KEY_YOUTUBE = credentials.get('API_KEY_YOUTUBE')
CLIENT_ID_YOUTUBE = credentials.get('CLIENT_ID_YOUTUBE')
CLIENT_SECRET_YOUTUBE = credentials.get('CLIENT_SECRET_YOUTUBE')
REDIRECT_URI_YOUTUBE = 'http://localhost:3001'

# AUTHORIZATION URL
AUTHORIZATION_BASE_URL = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
RESPONSE_TYPE = 'code'
SCOPE = 'https://www.googleapis.com/auth/youtube'


# Get youtube access token
def get_youtube_access_token():
    # Parameters for authorization request
    params = {
        'response_type': RESPONSE_TYPE,
        'client_id': CLIENT_ID_YOUTUBE,
        'redirect_uri': REDIRECT_URI_YOUTUBE,
        'scope': SCOPE,
    }

    # Redirect user to Google's OAuth 2.0 server
    authorization_url = AUTHORIZATION_BASE_URL + '?' + '&'.join([f'{key}={value}' for key, value in params.items()])

    print('Please go to this URL and authorize access:', authorization_url)
    authorization_code = input('Enter the authorization code: ')

    # Exchange authorization code for access token
    token_data = {
        'code': authorization_code,
        'client_id': CLIENT_ID_YOUTUBE,
        'client_secret': CLIENT_SECRET_YOUTUBE,
        'redirect_uri': REDIRECT_URI_YOUTUBE,
        'grant_type': 'authorization_code',
    }

    # Make a POST request to exchange the authorization code for an access token
    response = requests.post(TOKEN_URL, data=token_data)
    print(response)
    print(response.json())

    # Parse the JSON response
    token_response_data = response.json()

    # Check for errors
    access_token = token_response_data['access_token']

    return access_token


# Create youtube playlist
def create_youtube_playlist(access_token):
    create_pl = {
        'url': 'https://www.googleapis.com/youtube/v3/playlists?part=snippet,status&key=' + API_KEY_YOUTUBE,
        'headers': {
            'Authorization': 'Bearer ' + access_token
        },
    }

    body = {
        'snippet': {
            'title': 'Prova Spotify Playlist 2',
            'description': 'Playlist created from a spotify playlist'
        },
        'status': {
            'privacyStatus': 'private'
        }   
    }

    res = requests.post(create_pl['url'], headers=create_pl['headers'], data=json.dumps(body))

    return res.json()['id']


# Find the equivalent track in youtube
def find_track(track, access_token):
    search_track = {
        'url': 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=' + track + '&key=' + API_KEY_YOUTUBE,
        'headers': {
            'Authorization': 'Bearer ' + access_token
        },
    }

    res = requests.get(search_track['url'], headers=search_track['headers'])
    
    return res.json()['items'][0]['id']['videoId']


# Add track to youtube playlist
def add_track_to_playlist(track, playlist_id, access_token):
    video_id = find_track(track, access_token)

    add_track = {
        'url': 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&key=' + API_KEY_YOUTUBE,
        'headers': {
            'Authorization': 'Bearer ' + access_token
        },
    }

    body = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id
            }
        }
    }

    res = requests.post(add_track['url'], headers=add_track['headers'], data=json.dumps(body))


def transfer_playlist():
    # Get the spotify token
    spotify_token = get_spotify_token()
    print('Spotify auth done!')

    # Get the spotify playlist tracks
    playlist_tracks = get_playlist_tracks(credentials.get('SPOTIFY_PLAYLIST_ID'), spotify_token)
    print('Spotify tracks fetched!')

    # TODO: Check the order of tracks to maintain the order in the youtube playlist

    # Get the access token AKA auth process
    access_token = get_youtube_access_token()
    print('Youtube auth done!')

    # Create the youtube playlist
    playlist_id = create_youtube_playlist(access_token)
    print('Youtube playlist created!')

    # For each track in the spotify playlist, add it to the youtube playlist
    for track in playlist_tracks:
        add_track_to_playlist(track, playlist_id, access_token)

    print('Playlist transfer done!')


# Main function
if __name__ == '__main__':
    # Transfer playlist from spotify to youtube
    transfer_playlist()
