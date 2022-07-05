# program is going to be implemented as the reward user gets upon completing x amount of practice in their week
# program will generate a random quote for user as reward

import tkinter as tk
from tkinter import *
import requests
from threading import Thread

api = "http://api.quotable.io/random"
quotes = []
quote_number = 0

win = Tk()

win.geometry("750x270")

win.title("Reward Window")
win.grid_columnconfigure(0, weight=1)

win.resizable(False,False)
win.configure(bg="grey")


def preload_quotes():
    global quotes

    print("**Reward Loading**")
    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "By " + author
        print(content)

        quotes.append(quote)
    
    print("**Keep up the great work!**")

preload_quotes()


def get_random_quote():
    global quotes_label
    global quotes
    global quote_number
    
    quotes_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quotes)
        thread.start


# UI
quotes_label = tk.Label(win, text="Click button below to claim your reward!", height=6, pady=10, wraplength=800, font=("Helvetica", 14))

quotes_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text="Rewards here!", command=get_random_quote, bg="#0052cc", fg="#ffffff", activebackground="grey", font=("Helvetica", 14))

button.grid(row=1, column=0, stick="WE", padx=20, pady=20)

if __name__ == "__main__":
    win.mainloop()