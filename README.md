# Playlist converter

Playlist Converter is an all-in-one solution for effortlessly transforming your Spotify playlists into YouTube playlists.

Originally made to help a friend migrate from Spotify to YouTube Music without having to manually re-create their favourite playlists.

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

### YouTube/Google API Configuration

## License

[MIT](https://choosealicense.com/licenses/mit/)