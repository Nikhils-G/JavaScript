import os
import pygame
import tkinter as tk
from tkinter import filedialog
import eyed3
from random import shuffle
import threading

pygame.mixer.init()

current_song_index = -1
song_list = []
is_paused = False

def load_songs(directory):
    global song_list
    song_list = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.mp3')]
    shuffle(song_list)

def play_song(song_path):
    global current_song_index, is_paused
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    current_song_index = song_list.index(song_path)
    update_song_info(song_path)
    is_paused = False

def update_song_info(song_path):
    audiofile = eyed3.load(song_path)
    if audiofile.tag is not None:
        title = audiofile.tag.title if audiofile.tag.title else "Unknown Title"
        artist = audiofile.tag.artist if audiofile.tag.artist else "Unknown Artist"
        album = audiofile.tag.album if audiofile.tag.album else "Unknown Album"
    else:
        title = artist = album = "Unknown Info"
    song_info_label.config(text=f"Playing: {title} - {artist}\nAlbum: {album}")

def stop_song():
    pygame.mixer.music.stop()
    song_info_label.config(text="Stopped")
    global is_paused
    is_paused = False

def pause_song():
    pygame.mixer.music.pause()
    global is_paused
    is_paused = True
    song_info_label.config(text="Paused")

def unpause_song():
    pygame.mixer.music.unpause()
    global is_paused
    is_paused = False

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(song_list)
    play_song(song_list[current_song_index])

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(song_list)
    play_song(song_list[current_song_index])

def toggle_shuffle():
    global song_list
    song_list = list(song_list)
    shuffle(song_list)
    play_song(song_list[current_song_index])

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        load_songs(directory)
        play_song(song_list[0])

def gui_thread():
    root.mainloop()

root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")

song_info_label = tk.Label(root, text="Welcome to the Music Player!", font=("Arial", 14), justify="center")
song_info_label.pack(pady=20)

play_button = tk.Button(root, text="Play", command=lambda: play_song(song_list[current_song_index] if song_list else ""))
play_button.pack(fill="x")

pause_button = tk.Button(root, text="Pause", command=pause_song)
pause_button.pack(fill="x")

unpause_button = tk.Button(root, text="Unpause", command=unpause_song)
unpause_button.pack(fill="x")

stop_button = tk.Button(root, text="Stop", command=stop_song)
stop_button.pack(fill="x")

next_button = tk.Button(root, text="Next", command=next_song)
next_button.pack(fill="x")

prev_button = tk.Button(root, text="Previous", command=prev_song)
prev_button.pack(fill="x")

shuffle_button = tk.Button(root, text="Shuffle", command=toggle_shuffle)
shuffle_button.pack(fill="x")

open_button = tk.Button(root, text="Open Folder", command=open_directory)
open_button.pack(fill="x")

thread = threading.Thread(target=gui_thread, daemon=True)
thread.start()

while not song_list:
    pass

play_song(song_list[0])
