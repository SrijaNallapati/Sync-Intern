import sys
from tkinter import *
from tkinter import messagebox
import datetime
import time
from pygame import mixer
from PIL import Image,ImageTk

win=Tk()
win.title("Alarm Clock")
win.geometry("370x550")
win.config(bg="#54FF9F")
Font=("Times",35,"bold")

def setalarmfunc():
    global alarminputHr,alarminputMin
    window=Toplevel()
    window.geometry("550x480")
    window.config(bg="#54FF9F")
    
    forHour=Label(window,text="At What Hour Do You Want To Set",font=("Times",20,"bold"),bg="#54FF9F",padx=50)
    forHour.grid()

    alarminputHr=Entry(window,width=15,font=Font)
    alarminputHr.grid(pady=10,padx=15)

    forMin=Label(window,text="At What Minute Do You Want To Set",font=("Times",20,"bold"),bg="#54FF9F",padx=50)
    forMin.grid()

    alarminputMin=Entry(window,width=15,font=Font)
    alarminputMin.grid(pady=10,padx=15)

    Save=Button(window,text="Save",font=("Times",18,"bold"),command=alarm)
    Save.place(x=150,y=300)

    Cancel=Button(window,text="Cancel",font=("Times",18,"bold"),command=window.destroy)
    Cancel.place(x=350,y=300)

    stopmusic=Button(window,text="Dismiss",font=("Times",18,"bold"),command=stop)
    stopmusic.place(x=250,y=400)

def stop():
    mixer.init()
    mixer.music.stop()

def alarm():
    global alarminputHr,alarminputMin
    h=alarminputHr.get()
    m=alarminputMin.get()
    while(1):
        if(int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute):
            mixer.init()
            mixer.music.load('c:\\Users\\nalla\\Downloads\\AlarmTone.mp3')
            mixer.music.play()
            messagebox.showinfo("Alarm","Time Is Up!")
            break

heading=Label(win,text="Alarm Clock",font=Font,bg="#54FF9F",padx=50)
heading.grid()

SetAlarm=Button(text="To Set Alarm",font=("Times",20,"bold"),command=setalarmfunc)
SetAlarm.grid()

def gettime():
    timeVar=time.strftime("%H:%M:%S")
    clock.config(text=timeVar)
    clock.after(200,gettime)

clock=Label(win,text="Input Time",font=("Times",70,"bold"))
clock.grid(pady=50)

gettime()

win.mainloop()

