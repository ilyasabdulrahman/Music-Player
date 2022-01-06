#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:44:42 2022
@author: ilyasabdulrahman
"""
#Music Player Simulator
#step1: initialize GUI
#step2: initialize pygame
#step3: create function open_file()
#step4: create function load_file()
#step5: create function play_file()
#step6: create function mute()
#step7: create function pause()
#step8: create function stop()
#step9: create function volume()
#step10: initialize all variables in the GUI
#step11: position all variables in the GUI



from tkinter import *
from tkinter import filedialog as fd
import pygame

#initialize GUI
root = Tk()
filename = ""
root.resizable(False, False)
root.title("Music Player Simulator")
root.configure(bg='blue')


#initialize pygame
pygame.init()


def open_file():
    '''
    Opens the user's directory so the user can select an audio file to play
    '''
    global filename
    filetypes=(('MP3 Files', '*.mp3'), ('WAV Files', '*.wav'))
    filename = fd.askopenfilename(title='Open Files', initialdir='/', \
                                  filetypes=filetypes)
    file_dir.configure(text=filename)

def load_file():
    '''
    This function will load a music filename and prepare it for
    playback
    '''
    global filename
    pygame.mixer.music.load(filename)

def play_file():
    '''
    Calls the function load_file() and will start the playback of
    the music stream
    '''
    load_file()
    pygame.mixer.music.play()
    
def mute():
    '''
    This function has the ability to temporarily mute/unmute the music playback
    '''
    r=muted.cget('text')
    if r=='Mute':
        pygame.mixer.music.set_volume(0)
        muted['text']="Unmute"
    else:
        pygame.mixer.music.set_volume(0.7)
        muted['text']="Mute"
    
def pause():
    '''
    This function has the ability to temporarily stop music playback
    '''
    t=paused.cget('text')
    if t=='Pause':
        pygame.mixer.music.pause()
        paused['text']="Unpause"
    else:
        pygame.mixer.music.unpause()
        paused['text']="Pause"

def stop():
    '''
    Stops the music playback if it is currently playing
    '''
    pygame.mixer.music.stop()

def volume(value):
    '''
    This function enables the user to set the volume of the mp3 player to a
    specific value
    '''
    pygame.mixer.music.set_volume(float(value))
    

#initialize all variables in the GUI
empty_space1 = Label(root, height = 3, width = 50, bg = "blue")
open = Button(root, height = 1, width = 14, text = "Open", highlightbackground\
              = "lightblue", command=open_file)
img = PhotoImage(file="music_note.png")
image = Label(root, image = img, height = 200, width = 250, bg = "white")
start = Button(root, text="Play", height = 1, width = 14, highlightbackground\
               = "lightblue", command=play_file)
muted = Button(root, text="Mute", height = 1, width = 14, highlightbackground\
               = "lightblue", command=mute)
paused = Button(root, text="Pause", height = 1, width = 14,\
                highlightbackground = "lightblue", command=pause)
stops = Button(root, text="Stop", height = 1, width = 14, highlightbackground\
               = "lightblue", command=stop)
v = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=.1, width=40,\
          bg="lightblue", fg = "black", command=volume)
empty_space2 = Label(root, height=2, width=50, bg="blue")
file_dir = Label(root, height=3, width=50, bg="cyan", fg="red", text="",\
                 borderwidth=3, relief="ridge")


#position all variables in the GUI
empty_space1.grid(row=2, column=1, columnspan=3)
image.grid(row=3, column=1, rowspan=6)
open.grid(row=3, column=3)
start.grid(row=4, column=3)
muted.grid(row=5, column=3)
paused.grid(row=6, column=3)
stops.grid(row=7, column=3)
v.grid(row=8, column=3)
empty_space2.grid(row=9, column=1, columnspan=3)
file_dir.grid(row=1, column=1, columnspan=3)


root.mainloop()