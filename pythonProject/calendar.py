from tkinter import *
from tkinter import ttk

ws=Tk()

ws.title('PythonGuides')
ws.geometry('500x500')

set = ttk.Treeview(ws)
set.pack()

set['columns']= ('date', 'song','time')
set.column("#0", width=0,  stretch=NO)
set.column("date",anchor=CENTER, width=150)
set.column("song",anchor=CENTER, width=150)
set.column("time",anchor=CENTER, width=150)


set.heading("#0",text="",anchor=CENTER)
set.heading("date",text="Date",anchor=CENTER)
set.heading("song",text="Song",anchor=CENTER)
set.heading("time",text="Minutes Practiced",anchor=CENTER)

#data
data  = [
    ['Monday',"Twinkle, Twinkle","15 minutes"],
    ['Tuesday',"Mary had a little lamb","15 minutes"]

]

global count
count=0
    
for record in data:
      
    set.insert(parent='',index='end',iid = count,text='',values=(record[0],record[1],record[2]))
       
    count += 1



Input_frame = Frame(ws)
Input_frame.pack()

id = Label(Input_frame,text="Date", fg="green")
id.grid(row=0,column=0)

full_Name= Label(Input_frame,text="Song", fg="green")
full_Name.grid(row=0,column=1)

award = Label(Input_frame,text="Time", fg="green")
award.grid(row=0,column=2)

id_entry = Entry(Input_frame)
id_entry.grid(row=1,column=0)

fullname_entry = Entry(Input_frame)
fullname_entry.grid(row=1,column=1)

award_entry = Entry(Input_frame)
award_entry.grid(row=1,column=2)

def input_record():
    

    global count
   
    set.insert(parent='',index='end',iid = count,text='',values=(id_entry.get(),fullname_entry.get(),award_entry.get()))
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
    selected=set.focus()
    #grab record values
    values = set.item(selected,'values')
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
     
#button
Input_button = Button(ws,text = "Update Practice",command= input_record)

Input_button.pack()

select_button = Button(ws,text="Select Record", command=select_record)
select_button.pack(pady =10)

refresh_button = Button(ws,text="Refresh Record",command=update_record)
refresh_button.pack(pady = 10)

temp_label =Label(ws,text="")
temp_label.pack()



ws.mainloop()