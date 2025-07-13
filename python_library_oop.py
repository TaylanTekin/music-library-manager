import os

library = []

class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def __str__(self):
        return f"{self.title.title()} by {self.artist.title()}"

def add_song():
    title = input("Enter the song title: ")
    artist = input("Enter the artist's name: ")
    
    song = Music(title, artist)
    library.append(song)
    save_song(song)
    
    print(f'Song "{song.title}" by {song.artist} added.')
    input("Press Enter to continue...")

def save_song(song):
    with open("music_library.txt", "a") as f:
        f.write(f"{song.title},{song.artist}\n")

def show_saved_songs():
    if not os.path.exists("music_library.txt"):
        print("No songs saved yet.")
        return
    with open("music_library.txt", "r") as f:
        print("Saved songs:")
        for line in f:
            title, artist = line.strip().split(",")
            print(f"{title.title()} by {artist.title()}")

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

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎵 Music Library")
    print("1. Add songs")
    print("2. Show saved songs")
    print("3. Clear library")
    print("4. Search songs by artist")
    print("5. Quit")
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
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
        input("Press Enter to continue...")