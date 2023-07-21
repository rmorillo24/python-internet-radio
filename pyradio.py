import argparse
import subprocess
import os
import signal
import csv
from pyfiglet import Figlet

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Radio stream player.')
parser.add_argument('--stations', type=str, default='radio_stations.csv',
                    help='Path to the CSV file with the radio stations.')
args = parser.parse_args()

# Load radio streams from the CSV file specified in the command-line arguments
radio_streams = []
with open(args.stations, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        radio_streams.append(row)


# ASCII Art function
def ascii_art(text):
    f = Figlet(font="big")
    print(f.renderText(text))

def print_stations():
    print("\nSelect a radio stream:\n")
    for i, stream in enumerate(radio_streams):
        if current_station is not None and i == current_station - 1:
            print(f"{i+1}. \033[1m{stream['name']}\033[0m")  # \033[1m is the ANSI code for bold, \033[0m resets to normal
        else:
            print(f"{i+1}. {stream['name']}")

def clear_screen():
    if os.name == 'posix':  # For Unix/Linux/MacOS
        os.system('clear')
    else:  # For Windows
        os.system('cls')

player = None
current_station = None
while True:
    clear_screen()
    ascii_art("Stopped" if current_station == None else radio_streams[choice-1]['name'])  # Print the ASCII art of the station name
    print_stations()
    print("----------------------------------------")
    print("[s] - Stop\t[n] - Next Station\t[x] - Exit\n")
    command = input("Enter your command: ")
    if command.isdigit():
        choice = int(command)
        if not 1 <= choice <= len(radio_streams):
            print("Invalid choice.")
        else:
            if player is not None and player.poll() is None:  # If a player is running, stop it
                player.terminate()
            current_station = choice
            stream_url = radio_streams[choice-1]['url']
            player = subprocess.Popen(["cvlc", stream_url], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, start_new_session=True)
            # ascii_art(radio_streams[choice-1]['name'])  # Print the ASCII art of the station name
    elif command.lower() == 's':
        if player is not None and player.poll() is None:
            player.terminate()
        current_station = None
        # ascii_art("Stopped")  # Print the ASCII art of "Stopped"
    elif command.lower() == 'n':
        if player is not None and player.poll() is None:
            player.terminate()
        choice = (choice % len(radio_streams)) + 1  # Next station, wrap around if it's the last station
        current_station = choice
        stream_url = radio_streams[choice-1]['url']
        player = subprocess.Popen(["cvlc", stream_url], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, start_new_session=True)
        # ascii_art(radio_streams[choice-1]['name'])  # Print the ASCII art of the station name
    elif command.lower() == 'x':
        if player is not None and player.poll() is None:
            player.terminate()
        current_station = None
        break
    else:
        print("Invalid command.")
