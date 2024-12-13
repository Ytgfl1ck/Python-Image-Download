import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the mixer
mixer.init()

# Music Player class
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        self.current_song = ""
        self.playing = False

        # UI Elements
        self.label = tk.Label(root, text="No song selected", wraplength=300, justify="center")
        self.label.pack(pady=20)

        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Song", command=self.load_song)
        self.load_button.pack(pady=10)

    def load_song(self):
        # Open file dialog to select a song
        song_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac")]
        )
        if song_path:
            self.current_song = song_path
            self.label.config(text=f"Loaded: {os.path.basename(song_path)}")
            mixer.music.load(self.current_song)

    def play_song(self):
        if self.current_song:
            mixer.music.play()
            self.playing = True
            self.label.config(text=f"Playing: {os.path.basename(self.current_song)}")

    def pause_song(self):
        if self.playing:
            mixer.music.pause()
            self.playing = False
            self.label.config(text="Paused")
        else:
            mixer.music.unpause()
            self.playing = True
            self.label.config(text=f"Playing: {os.path.basename(self.current_song)}")

    def stop_song(self):
        mixer.music.stop()
        self.playing = False
        self.label.config(text="Stopped")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
