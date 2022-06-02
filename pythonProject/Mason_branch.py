import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("", "Please enter Username")
    elif (username=="Test" and password=="Test123"):
        messagebox.showinfo("", "Let's Practice!")
    else:
        messagebox.showinfo("", "Incorrect username and password. Please try again.")

root=Tk()
root.title("Piano Practice Login Screen")
root.geometry("700x500")
root.configure(bg="seashell1")

loginFont = ("Comic Sans MS", 17, "bold")


# --- Logo ... CAUTION: LOGO ISN'T PROPERLY UPLOADING ---

canvas = Canvas(root,width=1000,height=250)
canvas.pack()
imgLabel = ImageTk.PhotoImage(Image.open("images/PianoPractice.png"))
canvas.create_image(20,20,anchor=NW,image=imgLabel)

global entry1
global entry2


# Login Buttons

Label(root, text="Username", font="40",fg="green", bg="seashell1").place(x=420,y=300)
Label(root, text="Password", font="40", fg="green", bg="seashell1").place(x=420,y=375)

entry1=Entry(root, bd=5, width="50")
entry1.place(x=540,y=300)

entry2=Entry(root,bd=5, width="50")
entry2.place(x=540,y=375)

Button(root,text="Login", command=login,height=3,width=25,bd=6, bg="green", fg="white", font=loginFont).place(x=500,y=500)

root.mainloop()

