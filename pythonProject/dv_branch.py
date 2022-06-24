from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from tkinter import messagebox
import pickle

# for setting default date as today
from datetime import date, timedelta

root = tk.Tk()

WIDTH = 650
HEIGHT = 800
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(columnspan=1,rowspan=6)

def main_screen():
    #login button
    login_text = tk.StringVar()
    login_text.set("Login Now")
    login_btn = tk.Button(root, textvariable=login_text, command=lambda:main_close(),
                          font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    login_btn.grid(column=0, row=2)
    
    #logo
    logo = Image.open('images/PianoPractice.png')
    logo = logo.resize((600, 220))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    def main_close():
        login_btn.destroy()
        logo_label.destroy()
        login_screen()

def login_screen():

    #login button
    login_text = tk.StringVar()
    login_text.set("Login")
    login_btn = tk.Button(root, textvariable=login_text, command=lambda:login(),
                          font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    login_btn.grid(column=0, row=2)
    
    #logo
    logo = Image.open('images/PianoPractice.png')
    logo = logo.resize((600, 220))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    # Login Buttons
    login_frame = tk.Frame(root)
    login_frame.grid(column=0,row=1)
    user_lbl = Label(login_frame, text="Username", font="50", fg="#275D38")
    user_lbl.grid(column=0,row=0,padx=10,pady=10)
    pass_lbl = Label(login_frame, text="Password", font="50", fg="#275D38")
    pass_lbl.grid(column=0,row=1,padx=10,pady=10)

    entry1 = Entry(login_frame, bd=5, width="50")
    entry1.grid(column=1,row=0,padx=10,pady=10)

    entry2 = Entry(login_frame, show="*", bd=5, width="50")
    entry2.grid(column=1,row=1,padx=10,pady=10)

    def login():

        global username
        #get values from entry fields
        username = entry1.get()
        password = entry2.get()

        if username == "" and password == "":
            messagebox.showinfo("", "Please enter Username")
        elif (username == "Test" and password == "Test123") or (username == "x" and password == "x"):
            messagebox.showinfo("Login Successful", "Let's Practice!")

            #remove old widgets
            login_frame.destroy()
            logo_label.destroy()
            login_btn.destroy()

            #load practice screen
            practice_screen()
        else:
            messagebox.showinfo("", "Incorrect username and password. Please try again.")

    root.title("Piano Practice Login Screen")


def practice_screen():
    #frame to hole logo and user_frame
    top_frame = tk.Frame(root)
    top_frame.grid(column=0,row=0)
    #frame to hold the user pic and name/logout button
    user_frame = tk.Frame(top_frame)
    user_frame.grid(column=1,row=0)
    
    #update the title
    root.title("Piano Practice")

    #logo resized
    practice_logo = Image.open('images//PianoPractice.png')
    practice_logo = practice_logo.resize((400,196))
    practice_logo = ImageTk.PhotoImage(practice_logo)
    practice_logo_lbl = tk.Label(top_frame, image=practice_logo)
    practice_logo_lbl.image = practice_logo
    practice_logo_lbl.grid(column=0, row=0)

    #generic user pic
    user_pic = Image.open('images//user.png')
    user_pic = user_pic.resize((100,100))
    user_pic = ImageTk.PhotoImage(user_pic)
    user_pic_lbl = tk.Label(user_frame, image=user_pic)
    user_pic_lbl.image = user_pic
    user_pic_lbl.pack()

    #action when user name is clicked
    def logout():
        logout_msgbox = messagebox.askquestion("Logout", "Do you want to logout?", icon='warning')
        if logout_msgbox == 'yes':
            top_frame.destroy()
            record_frame.destroy()
            input_frame.destroy()
            button_frame.destroy()
            main_screen()
    
    #displays as user name
    logout_btn = tk.Label(user_frame, text=username, font=("Raleway",20),
                          fg="black", height=2, width=15, cursor='hand2')
    logout_btn.pack()
    logout_btn.bind("<Button-1>", lambda e: logout())

    #frame to hold the Treeview object
    record_frame = tk.Frame(root)
    record_frame.grid(column=0,row=1)
    
    #data frame object
    song_set = Treeview(record_frame)
    song_set.pack()

    # # Add a scrollbar
    # scrollbar = tk.ttk.Scrollbar(root, orient=tk.VERTICAL, command=song_set.yview)
    # song_set.configure(yscroll=scrollbar.set)
    # scrollbar.grid(row=0, column=1, sticky='ns')

    #set up columns in data frame
    song_set['columns']= ('date', 'song','time')
    song_set.column("#0", width=0,  stretch=NO)
    song_set.column("date",anchor=CENTER, width=150)
    song_set.column("song",anchor=CENTER, width=150)
    song_set.column("time",anchor=CENTER, width=150)

    song_set.heading("#0",text="",anchor=CENTER)
    song_set.heading("date",text="Date",anchor=CENTER)
    song_set.heading("song",text="Song",anchor=CENTER)
    song_set.heading("time",text="Minutes Practiced",anchor=CENTER)
    
    # overall minutes display
    minutes_frame = Frame(root)
    minutes_frame.grid(column=0,row=5)
    
    # Create the current week to populate the date data field
    this_week = []
    today = date.today()
    today_day = today.weekday()
    for i in range(7):
        dte = (today - timedelta(days=today_day))
        this_week.append(dte.strftime("%a, %B %d"))
        today_day -= 1
#     print(this_week)

    #data
    def load_entries(this_week):
        '''Fills week display with dates and practice entries
           First clears table of all information, then fills each line
           with the date and song entry for that day, calls helper
           function to display reward info at bottom of screen.
           Retuns dictionary of user data.'''
        filename = "user_data"
        output_file = open(filename, 'rb')
        data = pickle.load(output_file)
        total, remain, practice_table = 0, data[username][1], data[username][2]

        #clear table
        for item in song_set.get_children():
            song_set.delete(item)

        #load week with dates and any entries        
        for day in range(len(this_week)):
            for ent in range(len(practice_table)):
                entry = practice_table[ent]
                if this_week[day] == entry[0]:
                    song_set.insert(parent='',index='end',iid = day,text='',
                                    values=(entry[0],entry[1],f"{entry[2]} minutes"))
                    total += entry[2]
                    remain -= entry[2]
                    break
                if this_week[day] != entry[0]:
                    if ent == len(practice_table)-1:
                        song_set.insert(parent='', index='end', iid= day,
                                        text='',values=(this_week[day], "", ""))
                    else:
                        continue
        #helper function to display reward info at bottom of screen
        minutes_help(total, remain)
        return data

    def minutes_help(total, remain):
        '''Receives weekly total minutes and remaining minutes,
           then displays them at bottom of screen.'''
        Label(minutes_frame, text=f"Total Minutes: {total}",font="Raleway",
              bg="white", fg="black", height=2, width=20).grid(column=0,row=0,sticky='w')
        Label(minutes_frame, text=f"Minutes to Reward: {remain}",font="Raleway",
              bg="white", fg="black", height=2, width=20).grid(column=2,row=0,sticky='e')

    #creates dictionary from dat file
    data = load_entries(this_week)
    print(f"Initial data load for {username}:\n{data[username]}")

    #frame for user to input new songs, dates, and times
    input_frame = tk.Frame(root)
    input_frame.grid(column=0,row=2)

    #input labels
    id = Label(input_frame,text="Date", fg="green")
    id.grid(row=0,column=0)

    full_Name= Label(input_frame,text="Song Name", fg="green")
    full_Name.grid(row=0,column=1)

    award = Label(input_frame,text="Time in minutes", fg="green")
    award.grid(row=0,column=2)

    # SONG DATE
    #song data input entry fields
    id_entry = Entry(input_frame)
    id_entry.grid(row=1,column=0)

    # set current date to date entry field
    today = date.today()
    day_string = today.strftime("%a, %B %d")
    # setup today as read only
    id_entry.insert(0, day_string)
    id_entry.config(state='readonly')

    # Beginning selection is set to current date
    selected = song_set.get_children()[today.weekday()]
    song_set.focus(selected)
    song_set.selection_set(selected)

    # grab record values
    values = song_set.item(today.weekday(), 'values')

    # SONG NAME
    fullname_entry = Entry(input_frame)
    fullname_entry.grid(row=1, column=1)
    fullname_entry.insert(0, values[1])

    # SONG TIME PRACTICED
    award_entry = Entry(input_frame)
    award_entry.grid(row=1, column=2)
    award_entry.insert(0, values[2][:-8])

    #functionality to input a new song record
    def input_record():
        '''insert new values into the data frame'''

        # Check if a song name was entered
        song_name = fullname_entry.get()

        # Check if the minutes are valid:
        minutes=""
        for char in award_entry.get():
            if char.isdigit():
                minutes += char

        # If invalid minutes, else valid
        if minutes=="":
            messagebox.showinfo("Error: invalid format: ", "Please enter a time in minutes. (ie. 15)")
            award_entry.delete(0, END)
        elif song_name == "":
            messagebox.showinfo("Error: no song name entered.", "Please enter a valid song name.")
        else:
            # update user data dictionary
            practice_table = data[username][2]
            for ent in range(len(practice_table)):
                entry = practice_table[ent]
                if this_week[today.weekday()] == entry[0]:
                    entry[1], entry[2] = fullname_entry.get(), int(award_entry.get())
                    break
                else:
                    if ent == len(practice_table)-1:
                        data[username][2].append([id_entry.get(), fullname_entry.get(),
                                                  int(award_entry.get())])
                    else:
                        continue
            # save user data to database and refresh display
            filename = "user_data"
            output_file = open(filename, 'wb')
            pickle.dump(data, output_file)
            output_file.close()
            load_entries(this_week)
            print(f"\nUpdated data load for {username}:\n{data[username]}")

    #buttons
    #To choose a session, click the practice session and press the button "Select Practice Session"
    #To update a past entry, modify the entry as you desire, then press "Refresh practice calendar"
    #For creating a new record, type information in box and then press "Update today's practice"
    button_frame = Frame(root)
    button_frame.grid(column=0, row=3)

    input_button = Button(button_frame, text="Edit today's practice session", command=input_record)
    input_button.grid(column=0, row=0, pady=10)

#run inital login screen on boot
main_screen()
root.mainloop()
