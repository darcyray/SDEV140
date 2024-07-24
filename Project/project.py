'''
Author: Darcy Ralstin
Assignment: Final Project - MP3 Player
Description:
Note: Please install the imported libraries to run the program.
'''

from tkinter import *
from PIL import *
import pygame
from tkinter import filedialog

#Main window
root = Tk()
root.title('MP3 Player')
root.iconbitmap("mp3.ico")
root.geometry("500x400")

#Initialize pygame mixer
pygame.mixer.init()

#Add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose a Song", filetypes=(('mp3 Files', '*.mp3'), ))
    song = song.replace("C:/Users/fayer/Documents/School/Summer 2024/Intro to Python/Project/Audio/", "")
    song_box.insert(END, song)

#Playlist box
song_box = Listbox(root, bg="teal", fg="white", width=60, selectbackground="#357180")
song_box.pack(pady=20)

#Player controls - images
back_btn_img = PhotoImage(file="C:/Users/fayer/Documents/School/Summer 2024/Intro to Python/Project/back.png")
pause_btn_img = PhotoImage(file="C:/Users/fayer/Documents/School/Summer 2024/Intro to Python/Project/pause.png")
play_btn_img = PhotoImage(file="C:/Users/fayer/Documents/School/Summer 2024/Intro to Python/Project/play.png")
forward_btn_img = PhotoImage(file="C:/Users/fayer/Documents/School/Summer 2024/Intro to Python/Project/forward.png")
stop_btn_img = PhotoImage(file="C:/Users/fayer/Documents/School/Summer 2024/Intro to Python/Project/stop.png")

#Player controls - frame
controls_frame = Frame(root)
controls_frame.pack()

#Player controls - buttons
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0)

back_btn.grid(row=0, column=0, padx=10)
pause_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
stop_btn .grid(row=0, column=3, padx=10)
forward_btn.grid(row=0, column=4, padx=10)

#Menu
menu_1 = Menu(root)
root.config(menu=menu_1)

#Add song to playlist
add_song_menu = Menu(menu_1)
menu_1.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add Song to Playlist", command=add_song)


root.mainloop()
