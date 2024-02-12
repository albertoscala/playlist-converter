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

### Spotify API configuration

### YouTube/Google API Configuration

## License

[MIT](https://choosealicense.com/licenses/mit/)