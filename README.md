# 🎵 Media-Enhanced Python Music Library

A terminal-based music library manager built in Python. This upgraded version supports MP3 playback using `pygame`, file saving/loading, and a menu-driven user experience.

---

## ✨ Features

- ✅ Add new songs with title, artist, and audio filename  
- 🎧 Play audio files (MP3 support via `pygame`)  
- 🔍 Search songs by artist (case-insensitive)  
- 💾 Save and load your music library from a file  
- 🧹 Clear the entire saved music list with confirmation  
- 📃 Display all saved songs with numbering  
- 🧭 Menu-based navigation system  

---

## 📁 File Format

Songs are stored in `music_library.txt` with this structure:

Title,Artist,Filename

makefile
Kopieren
Bearbeiten

**Example:**
Stronger,Kanye West,stronger.mp3
Bohemian Rhapsody,Queen,bohemian.mp3

> ⚠️ Make sure the audio files are in the same folder as the Python script.

---

## 🔧 Requirements

- Python 3.8 or higher  
- `pygame` library (for audio playback)

### Install `pygame`:

```bash
pip install pygame
```
## ▶️ How to Use
Run the script:
python music_library.py
Then follow the menu prompts:

🎵 Music Library
1. Add songs
2. Show saved songs
3. Clear library
4. Search songs by artist
5. Play a song
6. Quit
## 📌 Example Flow
Add a song:
Provide title, artist, and MP3 filename (e.g. track1.mp3)

View saved songs:
Displays a numbered list of all songs in your library

Play a song:
Choose the number to start playback, press Enter to stop

Search by artist:
Case-insensitive search that lists all matches

## 🧠 Future Improvements
🎵 Playlist support (create, edit, delete)

🖥️ GUI with Tkinter or PyQt

📱 Web or mobile app version

📤 Upload/import songs from folders

⏯️ Add playback controls (pause, resume, skip)

## 📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and share.

## 👤 Author
Taylan Tekin
15 y/o Python learner — documenting progress one project at a time and exploring object-oriented programming and real-world app ideas
