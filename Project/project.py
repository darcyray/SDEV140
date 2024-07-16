'''
Author: Darcy Ralstin
Assignment: Final Project - MP3 Player
Description:
Note: Please install the imported libraries to run the program.
'''

from tkinter import *
from PIL import *
import pygame

root = Tk()
root.title('MP3 Player')
root.iconbitmap("mp3.ico")
root.geometry("500x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("Audio/01 - Good Luck, Babe!.mp3")
    pygame.mixer.music.play(loops=0)
    
def stop():
    pygame.mixer.music.stop()

play_button = Button(root, text="Play", font=("Arial", 28),command=play)
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Arial", 28), command=stop)
stop_button.pack(pady=20)

root.mainloop()
