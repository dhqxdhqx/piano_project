import tkinter as tk
from tkinter import *
#import PyPDF2
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
''' An app to track piano practice time'''

root = tk.Tk()

WIDTH = 740
HEIGHT = 1334
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(columnspan=5, rowspan=5)

# global entry1
# global entry2


def login_screen():
    print("login worked!!")
    login_text.set("Login")

    # Login Buttons
    Label(root, text="Username", font="40", fg="#275D38").place(x=220, y=375)
    Label(root, text="Password", font="40", fg="#275D38").place(x=220, y=450)

    entry1 = Entry(root, bd=5, width="50")
    entry1.place(x=320, y=375)

    entry2 = Entry(root, show="*", bd=5, width="50")
    entry2.place(x=320, y=450)

    def login():
        print("testing login")
        username = entry1.get()
        password = entry2.get()
        print(entry1, entry2)

        if username == "" and password == "":
            messagebox.showinfo("", "Please enter Username")
        elif username == "Test" and password == "Test123":
            messagebox.showinfo("", "Let's Practice!")
        else:
            messagebox.showinfo("", "Incorrect username and password. Please try again.")

    root.title("Piano Practice Login Screen")
    login_btn.configure(command=login)

# def main_screen():
print("Running the main screen worked!")
root.title("Piano Practice")

# logo
logo_orig = Image.open('images/PianoPractice.png')
logo = logo_orig.resize((816, 320))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# login button
login_text = tk.StringVar()
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

login_btn = tk.Button()

def main_screen():
    login_btn = tk.Button(root, textvariable=login_text, command=lambda: login_screen(), font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    login_text.set("Login now")
    login_btn.grid(column=1, row=1)


main_screen()
root.mainloop()
