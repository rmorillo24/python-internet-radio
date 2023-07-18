# Radio Stream Player

This is a command-line based Radio Stream Player that allows you to play audio streams from a list of internet radio stations.

## Requirements

- Python 3
- VLC media player
- cvlc command line interface
- The following Python libraries, which can be installed with `pip install -r requirements.txt`:
  - `pyfiglet`

## How to use

1. Make sure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).

2. Make sure you have VLC and cvlc installed. You can download VLC from [here](https://www.videolan.org/vlc/index.html). cvlc is usually included in the VLC installation.

3. The script uses a list of radio stations stored in a CSV file named `radio_stations.csv`. The CSV file should have two columns: `name` and `url`, where `name` is the name of the radio station and `url` is the corresponding stream URL.

4. Run the script in the terminal using the command `python radio_stream_player.py`.

## Controls

- Enter a number to select a station to play from the displayed list.
- Press `s` to stop the currently playing station.
- Press `n` to skip to the next station in the list.
- Press `x` to exit the script.

## Notes

- This script was developed for use on Unix/Linux/MacOS systems. It may work on Windows with modifications.
- The bold text in the list of stations indicates the currently playing station.

## Contact

For any issues or suggestions, feel free to open an issue on this repository.

