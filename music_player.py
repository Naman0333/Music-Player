#import  required  Library
import tkinter as tk
from pygame import mixer
from tkinter import filedialog
import os
import  pygame

#music player
class MusicPlayer:
    def __init__(self,window):
        window.geometry("320x100+0+0")
        window.title('Music Player')
        window.resizable(False,False)
        window.configure(bg = 'black')
        Load_Button = tk.Button(window, text= "Load", width= 10, font=('Times', 10, 'bold'),command= self.load).place(x= 0,y= 70)
        Play_Button = tk.Button(window, text= "Play", width= 10, font=('Times', 10, 'bold'),command = self.play).place(x=80, y= 70)
        Pause_Button = tk.Button(window, text= "Pause", width= 10, font=('Times',10,'bold'),command = self.pause).place(x=160, y= 70)
        Stop_Button = tk.Button(window, text = "Stop", width= 10, font=('Times', 10, 'bold'),command = self.stop).place(x=240, y= 70)
        self.playing_state = False
        self.music_file = False

    #load music function
    def load(self):
        self.music_file = filedialog.askopenfilename()

    #play music function
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    #pause music function
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    #stop music function
    def stop(self):
        mixer.music.stop()

root = tk.Tk()
app = MusicPlayer(root)
icon = pygame.image.load('music.png')
pygame.display.set_icon(icon)
root.mainloop()