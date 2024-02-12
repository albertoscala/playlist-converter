# Playlist converter

Playlist Converter is an all-in-one solution for effortlessly transforming your Spotify playlists into YouTube playlists.

Originally made to help a friend migrate from Spotify to YouTube Music without having to manually re-create their favourite playlists.

# Table of Contents
- [Playlist converter](#playlist-converter)
- [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Configuration](#configuration)
    - [Spotify API configuration](#spotify-api-configuration)
    - [YouTube/Google API Configuration](#youtubegoogle-api-configuration)
  - [Usage](#usage)
  - [License](#license)

## Installation

To use this project, you will need to first clone the repository to your local machine. Using git, you can do this by running the following command:

```bash
git clone https://github.com/albertoscala/playlist-converter.git
```

Then move into the project directory and install the required dependencies using pip:

```bash
cd playlist-converter
pip install -r requirements.txt
```

Note: If you are on arch-based linux, you can't use the requirements.txt file to install the dependencies. You will need to install the following packages manually using pacman typing the following command:

```bash
pacman -S python-namepackage

# Example
pacman -S python-requests
```

Or you can use `python -m venv .` to create a virtual environment in the current directory and then install the dependencies using pip. as i showed in the second step.

## Configuration

Before diving into the complex world of APIs, we will need to understand what we need and where we have to put it in order to make the project work.

The file **ONLY** file you have to modify is the `credentials.py` file. This file contains the various Spotify and YouTube/Google API keys, credentials and secret credentials. 

### Spotify API configuration

The first part of the configuration is accessing the Spotify API. To do this, you will need to create a Spotify Developer account and create a new application. Once you have done this, you will be given a `client_id` and a `client_secret`. You will need to put these into the `credentials.py` file.

```python
'CLIENT_ID_SPOTIFY':        'your_spotify_client_id_here',
'CLIENT_SECRET_SPOTIFY':    'your_spotify_client_secret_here',
```

NOTE: While you are creating the app, it will ask you to put an URI, just pust `http://localhost:3000` and it will work. We are not using a redirect URI, so it doesn't matter what you put there.

The last thing we have to get is the actual playlist ID. To do this, you will need to go to the playlist you want to convert and copy the URL. The URL will look something like this:

```
https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM?si=6e766bb25fe64347
```

The part we are interested in is the `0vvXsWCC9xrXsKd4FyS8kM` part. This is the playlist ID. You will need to put this into the `credentials.py` file.

```python
'PLAYLIST_ID_SPOTIFY':      'your_spotify_playlist_id_here',
```

### YouTube/Google API Configuration

Now the things will get much more complex thanks to the highly skilled google eginners. First of all, you will need to create a new project in the Google Cloud Console. 

Once you have done this, you will need to enable the YouTube Data API v3. You can do this by going to the API Library and searching for the YouTube Data API v3. Once you have found it, you will need to enable it. 

Now let's create the credentials. Go to the credentials section and create a new API key. Once you have done this, you will be given an API key. You will need to put this into the `credentials.py` file.

```python
'API_KEY_YOUTUBE':          'your_youtube_api_key_here',
```

Now we will need to create the OAuth 2.0 credentials. Before creating the actual credentials we need to create the OAuth consent screen. Go to the OAuth consent screen section and create a new consent screen. Once you have done this, you will need to fill in the required information.

As we did with the Spotify API, when they will request you the URI just put the same as spotify (NOTE: if you put something different, just because you feel alternative, it won't change anything).

Now we can go to the credentials section and create a new OAuth 2.0 client ID. Once you have done this, you will be given a `client_id` and a `client_secret`. You will need to put these into the `credentials.py` file.

```python
'CLIENT_ID_YOUTUBE':        'your_youtube_client_id_here',
'CLIENT_SECRET_YOUTUBE':    'your_youtube_client_secret_here',
```

## Usage

Now that we have everything set up, we can finally run the project. To do this, you will need to run the `main.py` file. You can do this by running the following command:

```bash
python main.py
```

Once you have done this, the program will start running. It will first authenticate with the Spotify API and then get the playlist. Once it has done this, it will authenticate with the YouTube API. 

Exactly for the youtube part, it will ask you to authenticate with your google account. Just follow the instructions and you will be able to authenticate. Click on the link and then copy the code and paste it in the terminal.

Once it has done this, it will start creating the playlist. It will first create the playlist and then add the songs to it.

## License

[MIT](https://choosealicense.com/licenses/mit/)