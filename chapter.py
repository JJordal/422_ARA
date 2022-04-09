from tkinter import *
from tkinter import simpledialog


chap_ctr = 0

#add a new chapter to a book
def new_chap(chap):
    global new_chap
    title = simpledialog.askstring(title="", prompt="Chapter Name")
    new_chap = Button(chap, text=title, height=5, width=10)
    global chap_ctr
    chap_ctr += 1
    new_chap.grid(row=0,column=chap_ctr)
    return
