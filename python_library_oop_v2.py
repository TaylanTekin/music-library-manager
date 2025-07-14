import os
import pygame
import time

library = []

class Music:
    def __init__(self, title, artist, filename):
        self.title = title
        self.artist = artist
        self.filename = filename
        
    def play(self):
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(self.filename)
            pygame.mixer.music.play()
            print(f"Now playing: {self.title} by {self.artist}")
            input("Press Enter to stop...")
            pygame.mixer.music.stop()
        except Exception as e:
            print(f"Error playing file: {e}")
        
    
    def __str__(self):
        return f"{self.title.title()} by {self.artist.title()}"

def add_song():
    title = input("Enter the song title: ")
    artist = input("Enter the artist's name: ")
    filename = input("Enter the filename (e.g. song1.mp3): ")
    
    if not os.path.exists(filename):
        print("⚠️ File not found. Make sure the song file is in the same folder.")
        input("Press Enter to return...")
        return
    
    song = Music(title, artist, filename)
    library.append(song)
    save_song(song)
    
    print(f'Song "{song.title}" by {song.artist} added.')
    input("Press Enter to continue...")

def save_song(song):
    with open("music_library.txt", "a") as f:
        f.write(f"{song.title},{song.artist},{song.filename}\n")
        
def load_songs():
    global library
    library = []
    if os.path.exists("music_library.txt"):
        with open("music_library.txt", "r") as f:
            for line in f:
                title, artist, filename = line.strip().split(",")
                library.append(Music(title, artist, filename))
    return library

def show_saved_songs():
    if not library:
        print("No songs in your library.")
    else:
        print("Saved songs:")
        for i, song in enumerate(library, 1):
            print(f"{i}. {song}")
            
def clear_library():
    confirm = input("Are you sure you want to clear your library? (y/n): ").strip().lower()
    if confirm == "y":
        with open("music_library.txt", "w") as f:
            pass
        print("All titles have been cleared from your library.")
    else:
        print("Canceled.")

def find_by_artist(artist_name):
    found = False
    for song in library:
        if song.artist.lower() == artist_name.lower():
            print(song)
            found = True
    if not found:
        print("No songs found for that artist.")
        
load_songs()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎵 Music Library")
    print("1. Add songs")
    print("2. Show saved songs")
    print("3. Clear library")
    print("4. Search songs by artist")
    print("5. Play a song")
    print("6. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_song()
        
    elif choice == "2":
        show_saved_songs()
        input("Press Enter to continue...")
        
    elif choice == "3":
        clear_library()
        input("Press Enter to continue...")
        
    elif choice == "4":
        artist_name = input("What artist are you searching for? ")
        print("Songs found:")
        find_by_artist(artist_name)
        input("Press Enter to continue...")
        
    elif choice == "5":
        show_saved_songs()
        song_number = input("enter the number of the song to play: ")
        if song_number.isdigit():
            index = int(song_number) - 1
            if 0 <= index < len(library):
                library[index].play()
            else:
                print("Invalid song number.")
                
        else:
            print("Please enter a valid number.")
        input("Press Enter to continue...")
        
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
        input("Press Enter to continue...")