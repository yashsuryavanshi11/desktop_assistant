from tkinter import *
from PIL import ImageTk,Image,ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root=Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes('-topmost', True)  # always on top
    global img 
    img=Image.open("pic.gif.crdownload")
    Lbl=Label(root)
    Lbl.place(x=0,y=0)
    i=0
    # mixer.music.load("spiderman.mp3")
    # mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img=img.resize((1000,500))
        img=ImageTk.PhotoImage(img)
        Lbl.config(image = img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()