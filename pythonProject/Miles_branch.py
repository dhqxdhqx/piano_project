# from logging import warning
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = tk.Tk()

WIDTH = 740
HEIGHT = 1334
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(columnspan=5, rowspan=5)
root.title("Piano Practice")
# global entry1
# global entry2






def login_screen():
    print("login worked!!")
    
    #login button
    login_text = tk.StringVar()
    login_text.set("Login now")
    login_btn = tk.Button(root, textvariable=login_text, command=lambda:login_screen(), font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    login_btn.grid(column=0, row=1)
    login_text.set("Login")

    #logo
    logo = Image.open('PianoPractice.png')
    logo = logo.resize((816, 320))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    # Login Buttons
    user_lbl = Label(root, text="Username", font="40", fg="#275D38")
    user_lbl.place(x=220, y=375)
    pass_lbl = Label(root, text="Password", font="40", fg="#275D38")
    pass_lbl.place(x=220, y=450)

    entry1 = Entry(root, bd=5, width="50")
    entry1.place(x=320, y=375)

    entry2 = Entry(root, bd=5, width="50")
    entry2.place(x=320, y=450)

    def login():
        print("testing login")
        global username
        username = entry1.get()
        password = entry2.get()
        
        if username == "" and password == "":
            messagebox.showinfo("", "Please enter Username")
        elif username == "Test" and password == "Test123":
            messagebox.showinfo("", "Let's Practice!")
            user_lbl.destroy()
            pass_lbl.destroy()
            entry1.destroy()
            entry2.destroy()
            logo_label.destroy()
            login_btn.destroy()
            practice_screen()
        else:
            messagebox.showinfo("", "Incorrect username and password. Please try again.")

    root.title("Piano Practice Login Screen")
    login_btn.configure(command=login)






#user name/logout

def practice_screen():
    
    user_frame = tk.Frame(root)
    user_frame.grid(column=2,row=0)
    root.title("Piano Practice")

    practice_logo = Image.open('PianoPractice.png')
    practice_logo = practice_logo.resize((500,196))
    practice_logo = ImageTk.PhotoImage(practice_logo)
    practice_logo_lbl = tk.Label(root, image=practice_logo)
    practice_logo_lbl.image = practice_logo
    practice_logo_lbl.grid(column=1, row=0)

    user_pic = Image.open('images//user.png')
    user_pic = user_pic.resize((100,100))
    user_pic = ImageTk.PhotoImage(user_pic)
    user_pic_lbl = tk.Label(user_frame, image=user_pic)
    user_pic_lbl.image = user_pic
    user_pic_lbl.pack()

    def logout():
        logout_msgbox = messagebox.askquestion("Logout", "Do you want to logout?", icon='warning')
        if logout_msgbox == 'yes':
            user_frame.destroy()
            practice_logo_lbl.destroy()
            logout_btn.destroy()
            login_screen()
    
    logout_btn = tk.Label(user_frame, text=username, font=("Raleway",20), fg="black", height=2, width=15, cursor='hand2')
    logout_btn.pack()
    logout_btn.bind("<Button-1>", lambda e: logout())

    
    
    

login_screen()
root.mainloop()
