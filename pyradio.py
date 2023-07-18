import subprocess
import os
import signal
import csv

# Load radio streams from a CSV file
radio_streams = []
with open('radio_stations.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        radio_streams.append(row)

def print_stations():
    print("\nSelect a radio stream:")
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
    print_stations()
    print("'s' - Stop\t'n' - Next Station\t'x' - Exit")
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
    elif command.lower() == 's':
        if player is not None and player.poll() is None:
            player.terminate()
        current_station = None
    elif command.lower() == 'n':
        if player is not None and player.poll() is None:
            player.terminate()
        choice = (choice % len(radio_streams)) + 1  # Next station, wrap around if it's the last station
        current_station = choice
        stream_url = radio_streams[choice-1]['url']
        player = subprocess.Popen(["cvlc", stream_url], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, start_new_session=True)
    elif command.lower() == 'x':
        if player is not None and player.poll() is None:
            player.terminate()
        current_station = None
        break
    else:
        print("Invalid command.")
