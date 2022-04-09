from tkinter import *
from tkinter import simpledialog
from chapter import new_chap

#initialize the window
root = Tk()
root.title("My Books")
root.geometry("800x500")
book_ctr = 0


#open new window with book title and chapters
def open_book(title):
    global add_chap
    global chap
    chap = Tk()
    chap.title(title)
    chap.geometry("800x500")
    add_chap = Button(chap, text="add chapter", command=lambda: new_chap(chap), height=5, width=10)
    add_chap.grid(row=0, column=0)
    return


#add a new book to the library
def new_book():
    title = simpledialog.askstring(title="", prompt="Book Name")
    new_book = Button(root, text=title,command= lambda: open_book(title), height=5, width=10)
    global book_ctr
    book_ctr += 1
    new_book.grid(row=0,column=book_ctr)
    return

#initialize the add book button
add_book = Button(root, text="add book", command=new_book, height=5, width=10)
add_book.grid(row=0,column=0)

root.mainloop()

