import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Replace with your Genius API key
genius = lyricsgenius.Genius("-p7ZrFh86lQka-FAyoHXM2idynCChzTYMLncxJRW-sklAp6FzgZw-NaP9SsKHyooN79VptwuQb5hFmoMWI1svQ")

def get_lyrics():
    song_title = entry_song.get()
    artist_name = entry_artist.get()
    
    if song_title and artist_name:
        try:
            song = genius.search_song(song_title, artist_name)
            if song:
                text_lyrics.delete(1.0, tk.END)  # Clear existing text
                text_lyrics.insert(tk.END, song.lyrics)  # Insert lyrics into the text box
            else:
                messagebox.showerror("Error", "Lyrics not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter both song title and artist name.")

# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")
root.geometry("500x500")

# Create labels and entry boxes for song title and artist
label_song = tk.Label(root, text="Song Title:")
label_song.pack(pady=5)
entry_song = tk.Entry(root, width=50)
entry_song.pack(pady=5)

label_artist = tk.Label(root, text="Artist Name:")
label_artist.pack(pady=5)
entry_artist = tk.Entry(root, width=50)
entry_artist.pack(pady=5)

# Create a button to fetch lyrics
button_get_lyrics = tk.Button(root, text="Get Lyrics", command=get_lyrics)
button_get_lyrics.pack(pady=10)

# Create a text box to display the lyrics
text_lyrics = tk.Text(root, wrap=tk.WORD, width=60, height=20)
text_lyrics.pack(pady=10)

# Start the GUI event loop
root.mainloop()
