from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from tkinter import messagebox


root = tk.Tk()

WIDTH = 600
HEIGHT = 800
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(columnspan=1,rowspan=6)
root.title("Piano Practice")


def login_screen():
    print("login worked!!")
    
    #login button
    login_text = tk.StringVar()
    login_text.set("Login now")
    login_btn = tk.Button(root, textvariable=login_text, command=lambda:login_screen(), font="Raleway", bg="#275D38", fg="white", height=2, width=15)
    login_btn.grid(column=0, row=2)
    login_text.set("Login")

    #logo
    logo = Image.open('images/PianoPractice.png')
    logo = logo.resize((750, 320))
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

    entry2 = Entry(login_frame, bd=5, width="50")
    entry2.grid(column=1,row=1,padx=10,pady=10)

    def login():
        print("testing login")
        global username
        username = entry1.get()
        password = entry2.get()
        
        if username == "" and password == "":
            messagebox.showinfo("", "Please enter Username")
        elif username == "Test" and password == "Test123":
            messagebox.showinfo("", "Let's Practice!")
            login_frame.destroy()
            logo_label.destroy()
            login_btn.destroy()
            practice_screen()
        else:
            messagebox.showinfo("", "Incorrect username and password. Please try again.")

    root.title("Piano Practice Login Screen")
    login_btn.configure(command=login)





def practice_screen():
    
    #frame to hold the user pic and name/logout button
    top_frame = tk.Frame(root)
    top_frame.grid(column=0,row=0)
    user_frame = tk.Frame(top_frame)
    user_frame.grid(column=1,row=0)
    
    root.title("Piano Practice")

    practice_logo = Image.open('images//PianoPractice.png')
    practice_logo = practice_logo.resize((500,196))
    practice_logo = ImageTk.PhotoImage(practice_logo)
    practice_logo_lbl = tk.Label(top_frame, image=practice_logo)
    practice_logo_lbl.image = practice_logo
    practice_logo_lbl.grid(column=0, row=0)

    user_pic = Image.open('images//user.png')
    user_pic = user_pic.resize((100,100))
    user_pic = ImageTk.PhotoImage(user_pic)
    user_pic_lbl = tk.Label(user_frame, image=user_pic)
    user_pic_lbl.image = user_pic
    user_pic_lbl.pack()

    def logout():
        logout_msgbox = messagebox.askquestion("Logout", "Do you want to logout?", icon='warning')
        if logout_msgbox == 'yes':
            top_frame.destroy()
            record_frame.destroy()
            input_frame.destroy()
            button_frame.destroy()
            login_screen()
    
    logout_btn = tk.Label(user_frame, text=username, font=("Raleway",20), fg="black", height=2, width=15, cursor='hand2')
    logout_btn.pack()
    logout_btn.bind("<Button-1>", lambda e: logout())

    record_frame = tk.Frame(root)
    record_frame.grid(column=0,row=1)
    
    song_set = Treeview(record_frame)
    song_set.pack()

    song_set['columns']= ('date', 'song','time')
    song_set.column("#0", width=0,  stretch=NO)
    song_set.column("date",anchor=CENTER, width=150)
    song_set.column("song",anchor=CENTER, width=150)
    song_set.column("time",anchor=CENTER, width=150)


    song_set.heading("#0",text="",anchor=CENTER)
    song_set.heading("date",text="Date",anchor=CENTER)
    song_set.heading("song",text="Song",anchor=CENTER)
    song_set.heading("time",text="Minutes Practiced",anchor=CENTER)

    #data
    data  = [
        ['Monday',"Twinkle, Twinkle","15 minutes"],
        ['Tuesday',"Mary had a little lamb","15 minutes"]]

    global count
    count=0
        
    for record in data:
        
        song_set.insert(parent='',index='end',iid = count,text='',values=(record[0],record[1],record[2]))
        
        count += 1
    
    input_frame = tk.Frame(root)
    input_frame.grid(column=0,row=2)

    id = Label(input_frame,text="Date", fg="green")
    id.grid(row=0,column=0)

    full_Name= Label(input_frame,text="Song", fg="green")
    full_Name.grid(row=0,column=1)

    award = Label(input_frame,text="Time", fg="green")
    award.grid(row=0,column=2)

    id_entry = Entry(input_frame)
    id_entry.grid(row=1,column=0)

    fullname_entry = Entry(input_frame)
    fullname_entry.grid(row=1,column=1)

    award_entry = Entry(input_frame)
    award_entry.grid(row=1,column=2)

    def input_record():
        

        global count
    
        song_set.insert(parent='',index='end',iid = count,text='',values=(id_entry.get(),fullname_entry.get(),award_entry.get()))
        count += 1

    
        id_entry.delete(0,END)
        fullname_entry.delete(0,END)
        award_entry.delete(0,END)

    #Select Record
    def select_record():
        #clear entry boxes
        id_entry.delete(0,END)
        fullname_entry.delete(0,END)
        award_entry.delete(0,END)
        
        #grab record
        selected=song_set.focus()
        #grab record values
        values = song_set.item(selected,'values')
        #temp_label.config(text=selected)

        #output to entry boxes
        id_entry.insert(0,values[0])
        fullname_entry.insert(0,values[1])
        award_entry.insert(0,values[2])

    #save Record
    def update_record():
        selected=set.focus()
        #save new data 
        set.item(selected,text="",values=(id_entry.get(),fullname_entry.get(),award_entry.get()))
        
       #clear entry boxes
        id_entry.delete(0,END)
        fullname_entry.delete(0,END)
        award_entry.delete(0,END)
        
    #buttons
    button_frame = Frame(root)
    button_frame.grid(column=0,row=3)
    
    input_button = Button(button_frame,text = "Update Practice",command= input_record)
    input_button.grid(column=0,row=0,pady=10)

    select_button = Button(button_frame,text="Select Record", command=select_record)
    select_button.grid(column=0,row=1,pady=10)

    refresh_button = Button(button_frame,text="Refresh Record",command=update_record)
    refresh_button.grid(column=0,row=2,pady=10)

    

#run inital login screen on boot
login_screen()
root.mainloop()

# from tkinter import *
# from tkinter import ttk

# ws=Tk()

# ws.title('PythonGuides')
# ws.geometry('500x500')





# Input_frame = Frame(ws)
# Input_frame.pack()

# id = Label(Input_frame,text="Date", fg="green")
# id.grid(row=0,column=0)

# full_Name= Label(Input_frame,text="Song", fg="green")
# full_Name.grid(row=0,column=1)

# award = Label(Input_frame,text="Time", fg="green")
# award.grid(row=0,column=2)

# id_entry = Entry(Input_frame)
# id_entry.grid(row=1,column=0)

# fullname_entry = Entry(Input_frame)
# fullname_entry.grid(row=1,column=1)

# award_entry = Entry(Input_frame)
# award_entry.grid(row=1,column=2)

# def input_record():
    

#     global count
   
#     set.insert(parent='',index='end',iid = count,text='',values=(id_entry.get(),fullname_entry.get(),award_entry.get()))
#     count += 1

   
#     id_entry.delete(0,END)
#     fullname_entry.delete(0,END)
#     award_entry.delete(0,END)

# #Select Record
# def select_record():
#     #clear entry boxes
#     id_entry.delete(0,END)
#     fullname_entry.delete(0,END)
#     award_entry.delete(0,END)
    
#     #grab record
#     selected=set.focus()
#     #grab record values
#     values = set.item(selected,'values')
#     #temp_label.config(text=selected)

#     #output to entry boxes
#     id_entry.insert(0,values[0])
#     fullname_entry.insert(0,values[1])
#     award_entry.insert(0,values[2])

# #save Record
# def update_record():
#     selected=set.focus()
#     #save new data 
#     set.item(selected,text="",values=(id_entry.get(),fullname_entry.get(),award_entry.get()))
    
#    #clear entry boxes
#     id_entry.delete(0,END)
#     fullname_entry.delete(0,END)
#     award_entry.delete(0,END)
     
# #button
# Input_button = Button(ws,text = "Update Practice",command= input_record)

# Input_button.pack()

# select_button = Button(ws,text="Select Record", command=select_record)
# select_button.pack(pady =10)

# refresh_button = Button(ws,text="Refresh Record",command=update_record)
# refresh_button.pack(pady = 10)

# temp_label =Label(ws,text="")
# temp_label.pack()



# ws.mainloop()


