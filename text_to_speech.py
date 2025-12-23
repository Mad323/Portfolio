'''
This Python program is a text-to-speech converter 
programmed using tkinter module
'''

from tkinter import *
from tkinter import messagebox
from playsound import playsound
import os
from gtts import gTTS

# setting up tkinter object 
root=Tk()
root.title("timer")
root.geometry("900x400+400+100")
root.minsize(200,300)
root.maxsize(1400,1600)
root.resizable(False,False)

# setting up design of GUI
Label(root, text="Text To Speech please enter", font=("Times New Roman", 10, "")).place(x=40,y=90)
Message=StringVar()
Entry(root, textvariable=Message,font=("cursive",16,""),width=10 ).place(x=200,y=90)#pack(side="bottom")

# convert text to speech by temporrarily creating "song15.mp3" to play the sound 
def Text_To_Speech():
    Msg=Message.get()
    speech= gTTS(text=Msg)
    speech.save('song15.mp3')
    playsound('song15.mp3')

# deletes "song15.mp3"
def fun1():
    os.remove('song15.mp3')
    Message.set("")

# Adding functionality of code to actual GUI
Button(root,text="Convert",bd=5,relief=RAISED, command=Text_To_Speech,font=("Times New Roman", 10,"")).place(x=70,y=120)#
Button(root,text="Exit",bd=5,relief=RAISED, command=quit,font=("Times New Roman", 10,"")).place(x=150,y=120)#
Button(root,text="Reset",bd=5,relief=RAISED, command=fun1,font=("Times New Roman", 10,"")).place(x=200,y=120)#

# Running it
root.mainloop()
