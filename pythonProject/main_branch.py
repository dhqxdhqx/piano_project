# from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pickle

from os.path import exists
# imports and runs database creation element
import create_sample_database

# for setting default date as today
from datetime import date, timedelta, datetime

root = tk.Tk()

WIDTH = 650
HEIGHT = 800
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(columnspan=1, rowspan=6)


def main_screen():
    # login button
    root.title("UVU Piano Practice")
    login_text = tk.StringVar()
    login_text.set("Login Now")
    login_btn = tk.Button(root, textvariable=login_text, command=lambda: main_close_login(),
                          font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    login_btn.grid(column=0, row=2)

    #  registration button
    register_text = tk.StringVar()
    register_text.set("Create New Account")
    register_btn = tk.Button(root, textvariable=register_text, command=lambda: main_close_register(), font="Raleway",
                             bg="#275D38", fg="white", height=2, width=20)
    register_btn.grid(column=0, row=3)

    # logo
    logo = Image.open('images/PianoPractice.png')
    logo = logo.resize((600, 220))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    def main_close_login():
        login_btn.destroy()
        register_btn.destroy()
        logo_label.destroy()
        login_screen()

    def main_close_register():
        """
        Closes main screen and opens registration screen
        """
        login_btn.destroy()
        register_btn.destroy()
        logo_label.destroy()
        registration_screen()


def encrypt_password(text):
    """
    Function to encrypt/hash password
    """
    result = ""
    for char in text:
        # Encrypt uppercase characters in plain text
        if ord(char) > 75:
            if ord(char) % 3 == 0:
                ord_char = (ord(char) - 12)
            else:
                ord_char = (ord(char) - 21)
        else:
            if ord(char) % 4 == 0:
                ord_char = (ord(char) + 7)
            else:
                ord_char = (ord(char) + 18)

        result += chr(ord_char)
    return result


def login_screen():
    # login button
    login_text = tk.StringVar()
    login_text.set("Login")
    login_btn = tk.Button(root, textvariable=login_text, command=lambda: login(), font="Raleway", bg="#275D38",
                          fg="white", height=2, width=15)
    login_btn.grid(column=0, row=2)

    # back-to-main-screen button
    to_main_screen_text = tk.StringVar()
    to_main_screen_text.set("Back")
    to_main_screen_btn = tk.Button(root, textvariable=to_main_screen_text, command=lambda: to_main_screen(),
                                   font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    to_main_screen_btn.grid(column=0, row=3)

    # logo
    logo = Image.open('images/PianoPractice.png')
    logo = logo.resize((600, 220))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    # Login Buttons
    login_frame = tk.Frame(root)
    login_frame.grid(column=0, row=1)
    user_lbl = tk.Label(login_frame, text="Username", font="50", fg="#275D38")
    user_lbl.grid(column=0, row=0, padx=10, pady=10)
    pass_lbl = tk.Label(login_frame, text="Password", font="50", fg="#275D38")
    pass_lbl.grid(column=0, row=1, padx=10, pady=10)

    entry1 = tk.Entry(login_frame, bd=5, width="50")
    entry1.grid(column=1, row=0, padx=10, pady=10)

    entry2 = tk.Entry(login_frame, show="*", bd=5, width="50")
    entry2.grid(column=1, row=1, padx=10, pady=10)

    def to_main_screen():
        """
        Closes the login screen and returns to the main screen
        """
        login_frame.destroy()
        logo_label.destroy()
        login_btn.destroy()
        to_main_screen_btn.destroy()
        main_screen()

    def login():

        global username
        # get values from entry fields
        username = entry1.get()
        password = encrypt_password(entry2.get())

        # Accessing data in database
        filename = "user_data"
        if not exists(filename):  # If sample database has not been created
            create_sample_database.create_database()
        database_file = open(filename, 'rb')
        data = pickle.load(database_file)

        if username == "" or password == "":
            messagebox.showinfo("", "Please enter Username and Password")

        # If username and password are in database

        elif (username in data.keys()) and (password == data[username][0]):
            user_type = data[username][1]

            database_file.close()
            # remove old widgets
            login_frame.destroy()
            logo_label.destroy()
            login_btn.destroy()
            to_main_screen_btn.destroy()

            # load practice screen
            practice_screen(user_type)
            if user_type == 0:
                messagebox.showinfo("Login Successful", "Let's Practice!")
            else:
                messagebox.showinfo("Login Successful", "Teacher login successful.")

        else:
            messagebox.showinfo("", "Incorrect username and/or password. Please try again.")

    root.title("Piano Practice Login Screen")


def registration_screen():
    root.title("Piano Practice New Account Registration Screen")

    # user account type selection
    user_var = tk.IntVar()
    user_type = tk.Label(root, text="Account type:", font="50", fg="#275D38")
    user_type.grid(column=0, row=2)

    student_user = tk.Radiobutton(text="Student", font="50", fg="#275D38", variable=user_var, value=0)
    student_user.grid(column=0, row=3, sticky='n')
    teacher_user = tk.Radiobutton(text="Teacher", font="50", fg="#275D38", variable=user_var, value=1)
    teacher_user.grid(column=0, row=3, sticky='s')

    # registration button
    register_text = tk.StringVar()
    register_text.set("Register Now")
    register_btn = tk.Button(root, textvariable=register_text, command=lambda: register(), font="Raleway", bg="#275D38",
                             fg="white", height=2, width=15)
    register_btn.grid(column=0, row=4)

    # back-to-main-screen button
    to_main_screen_text = tk.StringVar()
    to_main_screen_text.set("Back")
    to_main_screen_btn = tk.Button(root, textvariable=to_main_screen_text, command=lambda: to_main_screen(),
                                   font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    to_main_screen_btn.grid(column=0, row=5)

    # logo
    logo = Image.open('images/PianoPractice.png')
    logo = logo.resize((600, 220))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    # Registration fields
    register_frame = tk.Frame(root)
    register_frame.grid(column=0, row=1)
    user_lbl = tk.Label(register_frame, text="New username", font="50", fg="#275D38")
    user_lbl.grid(column=0, row=0, padx=10, pady=10)
    pass_lbl = tk.Label(register_frame, text="New password", font="50", fg="#275D38")
    pass_lbl.grid(column=0, row=1, padx=10, pady=10)

    entry1 = tk.Entry(register_frame, bd=5, width="50")
    entry1.grid(column=1, row=0, padx=10, pady=10)

    entry2 = tk.Entry(register_frame, show="*", bd=5, width="50")
    entry2.grid(column=1, row=1, padx=10, pady=10)

    def to_main_screen():
        """
        Closes the login screen and returns to the main screen
        """
        register_frame.destroy()
        logo_label.destroy()
        register_btn.destroy()
        to_main_screen_btn.destroy()
        user_type.destroy()
        student_user.destroy()
        teacher_user.destroy()
        main_screen()

    def register():
        global username
        # get values from entry fields
        username = entry1.get()
        password = encrypt_password(entry2.get())  # Hashes password
        account_type = int(user_var.get())
        print(account_type)  # *************temp print to verify new account type: 0=student, 1=teacher*******

        # Accessing data in database
        filename = "user_data"
        if not exists(filename):  # If sample database has not been created
            create_sample_database.create_database()
        database_file = open(filename, 'rb')
        data = pickle.load(database_file)

        if username == "" or password == "":
            messagebox.showinfo("", "Please enter Username and password")

        elif username in data.keys():
            # if username already exists, print message saying so
            messagebox.showinfo("", "Username already in use. Please choose a different username.")

        else:
            # remove old widgets
            register_frame.destroy()
            logo_label.destroy()
            register_btn.destroy()
            to_main_screen_btn.destroy()
            user_type.destroy()
            student_user.destroy()
            teacher_user.destroy()

            # Success: Put username, hashed password, user type in the database.

            if account_type == 0:  #If student
                database_file.close()
                data[username] = [password, account_type, 0, [[date.today(), "", 0]]]
                # TODO: if we make it so student can select their teacher, change so that the student is only added to that teacher's list
                # Putting student's username in the list of students for each teacher
                for key, value in data.items():
                    if value[1] == 1:  # If the user is a teacher
                        value[2].append(username)
                database_file = open(filename, 'wb')
                pickle.dump(data, database_file)
                database_file.close()
                messagebox.showinfo("Registration Successful", "New student user registration successful. Let's Practice!")

            elif account_type == 1:  # If teacher
                student_list = []
                for key, value in data.items():
                    if value[1] == 0:  # If user entry is a student
                        student_list.append(key)  # Append their username to the student_list
                database_file.close()
                data[username] = [password, account_type, student_list]
                database_file = open(filename, 'wb')
                pickle.dump(data, database_file)
                database_file.close()
                messagebox.showinfo("Registration Successful", "New teacher user registration successful!")

            # load practice info screen
            practice_screen(account_type)

def practice_screen(user_type):
    # part that is same for teachers and students
    # frame to hold logo and user_frame
    top_frame = tk.Frame(root)
    top_frame.grid(column=0, row=0)
    # frame to hold the user pic and name/logout button
    user_frame = tk.Frame(top_frame)
    user_frame.grid(column=1, row=0)

    # update the title
    root.title("Piano Practice")

    # logo resized
    practice_logo = Image.open('images//PianoPractice.png')
    practice_logo = practice_logo.resize((400, 196))
    practice_logo = ImageTk.PhotoImage(practice_logo)
    practice_logo_lbl = tk.Label(top_frame, image=practice_logo)
    practice_logo_lbl.image = practice_logo
    practice_logo_lbl.grid(column=0, row=0)

    # generic user pic
    user_pic = Image.open('images//user.png')
    user_pic = user_pic.resize((100, 100))
    user_pic = ImageTk.PhotoImage(user_pic)
    user_pic_lbl = tk.Label(user_frame, image=user_pic)
    user_pic_lbl.image = user_pic
    user_pic_lbl.pack()

    # displays as user name
    user_options = tk.Label(user_frame, text=username, font=("Raleway", 20), fg="black", height=2, width=15,
                            cursor='hand2')
    user_options.pack()
    user_options.bind("<Button-1>", lambda e: user_menu())

    # action when user name is clicked
    def user_menu():

        user_menu_window = tk.Toplevel(root)
        layout = tk.Canvas(user_menu_window, width=300, height=200)
        user_menu_window.title("User Menu")
        layout.grid(columnspan=1, rowspan=3)
        user_menu_window.grab_set()
        logout_btn = tk.Button(user_menu_window, text="Log Out", command=lambda: logout(), font="Raleway", bg="#275D38",
                               fg="white", height=2, width=15)
        logout_btn.grid(column=0, row=0)

        def logout():
            logout_msgbox = messagebox.askquestion("Logout", "Do you want to logout?", icon='warning')
            if logout_msgbox == 'yes':
                user_menu_window.grab_release()
                top_frame.destroy()
                record_frame.destroy()
                user_menu_window.destroy()
                minutes_frame.destroy()
                if user_type == 0:
                    student_input_frame.destroy()
                    button_frame.destroy()
                if user_type == 1:
                    teacher_select_frame.destroy()
                main_screen()

    # frame to hold the Treeview object
    record_frame = tk.Frame(root)
    record_frame.grid(column=0, row=1)

    # data frame object
    song_set = ttk.Treeview(record_frame)
    song_set.pack()


    # # Add a scrollbar
    # scrollbar = tk.ttk.Scrollbar(root, orient=tk.VERTICAL, command=song_set.yview)
    # song_set.configure(yscroll=scrollbar.set)
    # scrollbar.grid(row=0, column=1, sticky='ns')

    # set up columns in data frame
    song_set['columns'] = ('date', 'song', 'time')
    song_set.column("#0", width=0, stretch=tk.NO)
    song_set.column("date", anchor=tk.CENTER, width=150)
    song_set.column("song", anchor=tk.CENTER, width=150)
    song_set.column("time", anchor=tk.CENTER, width=150)

    song_set.heading("#0", text="", anchor=tk.CENTER)
    song_set.heading("date", text="Date", anchor=tk.CENTER)
    song_set.heading("song", text="Song", anchor=tk.CENTER)
    song_set.heading("time", text="Minutes Practiced", anchor=tk.CENTER)

    # overall minutes display
    minutes_frame = tk.Frame(root)
    minutes_frame.grid(column=0, row=5)

    # TODO change from this point on for teacher user_type=1
    
    # frame for student user to input new songs, dates, and times
    if user_type == 0:
        student_input_frame = tk.Frame(root)
        student_input_frame.grid(column=0, row=2)
        button_frame = tk.Frame(root)
        button_frame.grid(column=0, row=3)

    # frame for teacheruser to select students
    if user_type == 1:
        teacher_select_frame = tk.Frame(root)
        teacher_select_frame.grid(column=0, row=2)
       
    def load_entries(un, wk):
        '''Fills week display with dates and practice entries
           First clears table of all information, then fills each line
           with the date and song entry for that day, calls helper
           function to display reward info at bottom of screen.
           Retuns dictionary of user data.'''

        filename = "user_data"
        output_file = open(filename, 'rb')
        data = pickle.load(output_file)
        total, remain, practice_table = 0, data[un][2], data[un][3]

        # clear table
        for item in song_set.get_children():
            song_set.delete(item)

        # load week with dates and any entries
        for day in range(len(wk)):
            for ent in range(len(practice_table)):
                entry = practice_table[ent]
                if wk[day] == entry[0]:
                    song_set.insert(parent='', index='end', iid=day, text='',
                                    values=(f"{entry[0]:%a, %B %d}", entry[1], f"{entry[2]} minutes"))
                    total += entry[2]
                    remain -= entry[2]
                    break
                if wk[day] != entry[0]:
                    if ent == len(practice_table) - 1:
                        song_set.insert(parent='', index='end', iid=day,
                                        text='', values=(f"{wk[day]:%a, %B %d}", "", ""))
                    else:
                        continue
        # helper function to display reward info at bottom of screen
        minutes_help(total, remain)
        return data

    def minutes_help(total, remain):
        '''Receives weekly total minutes and remaining minutes,
           then displays them at bottom of screen.'''
        tk.Label(minutes_frame, text=f"Total Minutes: {total}", font="Raleway",
                 bg="white", fg="black", height=2, width=20).grid(column=0, row=0, sticky='w')
        tk.Label(minutes_frame, text=f"Minutes to Reward: {remain}", font="Raleway",
                 bg="white", fg="black", height=2, width=20).grid(column=2, row=0, sticky='e')
    
    def input_record(un, wk, day, song, mins, dte, data):
        '''insert new values into the data frame'''

        # Check if a song name was entered
        song_name = song.get()

        # Check if the minutes are valid:
        minutes = ""
        for char in mins.get():
            if char.isdigit():
                minutes += char

        # If invalid minutes, else valid
        if minutes == "":
            messagebox.showinfo("Error: invalid format: ", "Please enter a time in minutes. (ie. 15)")
            mins.delete(0, tk.END)
        elif song_name == "":
            messagebox.showinfo("Error: no song name entered.", "Please enter a valid song name.")
        else:
            #  update user data dictionary
            practice_table = data[un][3]
            for ent in range(len(practice_table)):
                entry = practice_table[ent]
                if wk[day.weekday()] == entry[0]:
                    entry[1], entry[2] = song.get(), int(minutes)
                    break
                else:
                    for Tag in wk:
                        if f"{Tag:%a, %B %d}" == dte.get():
                            dia = Tag
                    if ent == len(practice_table) - 1:
                        data[un][3].append([dia, song.get(),int(minutes)])
                    else:
                        continue
            # save user data to database and refresh display
            filename = "user_data"
            output_file = open(filename, 'wb')
            pickle.dump(data, output_file)
            output_file.close()
            load_entries(un, wk)
            print(f"\nUpdated data load for {un}:\n{data[un]}")
 
    def teacher_dropdowns():
        
        filename = "user_data"
        output_file = open(filename, 'rb')
        data = pickle.load(output_file)

        students_list = data[username][2]


        def scan_students(event):
            val = event.widget.get()
            print(val)

            if val == '':
                students = students_list
            else:
                students = []
                for item in students_list:
                    if val.lower() in item.lower():
                        students.append(item)
            update(students)

        def update(students):
            student_dropdown.delete(0, 'end')

            # put new data
            for item in students:
                student_dropdown.insert('end', item)
            # update(students)

        student_entry = tk.Entry(teacher_select_frame, bg='gray', fg='white')
        student_entry.bind('<KeyRelease>', scan_students)
        student_dropdown = tk.Listbox(teacher_select_frame, bg='gray', fg='white', selectbackground="#275D38",
                                      selectmode='single')
        update(students_list)

        def student_button():
            '''button that is clicked for select student'''
            student_entry.grid(column=0, row=1)
            student_dropdown.grid(column=0, row=2)

        select_student_btn = tk.Button(teacher_select_frame, text="Select a student", bg="#275D38", fg='white', command=student_button)
        select_student_btn.grid(column=0, row=0)

        def student_selected(event):
            '''handles student selected from student_dropdown Listbox item'''
            selected = student_dropdown.get(tk.ANCHOR)
            print(selected)
            student_entry.delete(0, tk.END)
            student_entry.insert(0, selected)

            student_dropdown.grid_remove()
            week_dropdown_f(selected)


        student_dropdown.bind('<<ListboxSelect>>', student_selected)

        def week_dropdown_f(student):

            #access student 'data'
            #get list of song entries student[3]
            songs_list = data[student][3]
            #take each entry student[3][i]
            week_dict = {}
            for i in range(len(songs_list)):
                #create date range
                day = songs_list[i][0]
                print(day)
                start = day - timedelta(days=day.weekday())
                end = start + timedelta(days=6)
                week = f'{start.strftime("%a, %B %d")} - {end.strftime("%a, %B %d")}'
                print(week)
                #store a list of indices into value with week as key
                if week in week_dict.keys():
                    continue
                else:
                    week_dict[week] = []
                    for i in range(7):
                        dte = (start  + timedelta(days=i))
                        week_dict[week].append(dte)
            
            print(week_dict)
         
            def week_selected():
                selected_week = week_dropdown.get(tk.ANCHOR)
                print("week was selected: ", selected_week)
                # clear table
                for item in song_set.get_children():
                    song_set.delete(item)

                # load week with dates and any entries
                load_entries(student, week_dict[selected_week])

            # Pull up the week menu
            print("Student ", student, "was selected-")
            select_week = tk.Button(teacher_select_frame, text="Select a week", bg="#275D38", fg='white', command=week_selected)
            select_week.grid(column=1, row=0)

            # TODO: remove test_week and use actual practice weeks of the selected student.
            test_week = ["06/19/22-07/25/22", "06/26/22-07/02/22", "07/03/22-07/09/22", "07/10/22-07/16/22"]

            week_dropdown = tk.Listbox(teacher_select_frame, bg='gray', fg='white', selectbackground="#275D38",
                                      selectmode='single')
            for items in week_dict.keys():
                week_dropdown.insert('end', items)
            week_dropdown.grid(column=1, row=2)
    

    def student_page():
        # Create the current week to populate the date data field
        this_week = []
        today = date.today()
        today_day = today.weekday()
        for i in range(7):
            dte = (today - timedelta(days=today_day))
            this_week.append(dte)
            today_day -= 1

        #     print(this_week)

        # creates dictionary from dat file
        data = load_entries(username, this_week)
        print(f"Initial data load for {username}:\n{data[username]}")


        # input labels
        id = tk.Label(student_input_frame, text="Date", fg="green")
        id.grid(row=0, column=0)

        full_Name = tk.Label(student_input_frame, text="Song Name", fg="green")
        full_Name.grid(row=0, column=1)

        award = tk.Label(student_input_frame, text="Time in minutes", fg="green")
        award.grid(row=0, column=2)

        # SONG DATE
        # song data input entry fields
        id_entry = tk.Entry(student_input_frame)
        id_entry.grid(row=1, column=0)

        # set current date to date entry field
        today = date.today()
        #day_string = today.strftime("%a, %B %d")
        day_string = f"{today:%a, %B %d}"
        # setup today as read only
        id_entry.insert(0, day_string)
        id_entry.config(state='readonly')
        
        # Beginning selection is set to current date, if exists
        selected = song_set.get_children()[today.weekday()]
        song_set.focus(selected)
        song_set.selection_set(selected)

        # grab record values
        values = song_set.item(today.weekday(), 'values')

        # SONG NAME
        fullname_entry = tk.Entry(student_input_frame)
        fullname_entry.grid(row=1, column=1)
        fullname_entry.insert(0, values[1])

        # SONG TIME PRACTICED
        award_entry = tk.Entry(student_input_frame)
        award_entry.grid(row=1, column=2)
        award_entry.insert(0, values[2][:-8])

        # buttons
        # To choose a session, click the practice session and press the button "Select Practice Session"
        # To update a past entry, modify the entry as you desire, then press "Refresh practice calendar"
        # For creating a new record, type information in box and then press "Update today's practice"

        input_button = tk.Button(button_frame,text="Edit today's practice session",
                    command=lambda:input_record(username,this_week,today,fullname_entry,award_entry,id_entry,data))
        input_button.grid(column=0, row=0, pady=10)

    if user_type == 0:  # If a student
        student_page()
    else:  # If a teacher
        teacher_dropdowns()

# run inital login screen on boot
main_screen()
root.mainloop()
