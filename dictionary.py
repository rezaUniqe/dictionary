# -*- coding: UTF-8 -*-
from tkinter import *
import sqlite3
from kivy.app import App

conn = sqlite3.connect('dic.db')
c = conn.cursor()
root = Tk()
root.geometry('600x800')
root.resizable(height=False, width=False)
txt = Entry(root)
root.title("dictionary")
titleText = Label(root, text="Dictionary", font=("Arial Bold", 35))
first_click = True
search_btn = PhotoImage(file='images/search.png')
image_lbl = Label(image=search_btn)
listbox = Listbox(root)
listbox.place(x=160, y=400, width=300)


def read_from_db(word):
    w = "" + word
    listbox.delete(0, 'end')
    c.execute('SELECT * FROM EnglishPersianWordDatabase where EnglishWord="%s" or PersianWord="%s"' % (word, word))
    data = c.fetchall()
    print("rows")
    for row in data:
        listbox.insert(END, row)
        print(row)


def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global first_click

    if first_click:  # if this is the first time they clicked it
        first_click = False
        txt.delete(0, "end")  # delete all the text in the entry


def search():
    read_from_db(txt.get())


sea_btn = Button(root, image=search_btn, command=search, borderwidth=0)

titleText.place(x=200, y=100)
txt.insert(0, 'Enter your word...')
txt.bind('<FocusIn>', on_entry_click)
txt.pack(side="left")
txt.place(x=130, y=185, width=360, height=35)
sea_btn.place(x=500, y=185)
root.mainloop()
c.close()
conn.close()
