from tkinter import *
import pyshorteners
import pyperclip
from tkinter import messagebox

win=Tk()
win.title("URL Shortener")
win.geometry("700x550")
win.config(bg="#E9967A")

def shorturlfunc():
    if BigURL.get():
        url=pyshorteners.Shortener().tinyurl.short(BigURL.get())
        ShortURL.insert(0,url)

def toreset():
    if ShortURL.get():
        ShortURL.delete(0,END)
    if BigURL.get():
        BigURL.delete(0,END)

def copy_function():
    copyurl=ShortURL.get()
    pyperclip.copy(copyurl)

def showMessage():
    messagebox.showinfo("information","URL is being Successfully copied!")

heading=Label(win,text="URL Shortener",font=("Times",30,"bold"),bg="#E9967A")
heading.grid(pady=15)

BigURLInput=Label(win,text="Enter The URL That Need To Be Shorten",font=("Times",25,"bold"),bg="#E9967A")
BigURLInput.grid(padx=50,pady=10)

BigURL=Entry(win,width=40,font=("Times",20,"bold"))
BigURL.grid(padx=20)

Short=Button(win,text="Shortern",font=("Times",20,"bold"),bg="#E9967A",command=shorturlfunc)
Short.grid(pady=25)

ShortURLInput=Label(win,text="The Shortened URL is",font=("Times",25,"bold"),bg="#E9967A")
ShortURLInput.grid(padx=20)

ShortURL=Entry(win,width=40,font=("Times",20,"bold"))
ShortURL.grid(padx=20,pady=10)
 
Reset=Button(win,text="Reset",font=("Times",18,"bold"),command=toreset,bg="#E9967A")
Reset.place(x=200,y=450)

copy=Button(win,text="Copy",font=("Times",18,"bold"),bg="#E9967A",command = lambda:[copy_function(),showMessage()])
copy.place(x=400,y=450)

win.mainloop()