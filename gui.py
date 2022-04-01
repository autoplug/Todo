#!/usr/bin/python
from task import *
from tkinter import *

task = Task()

# main window
main = Tk()
main.geometry("285x490")
main.resizable(False, False)
main.title('TODO')
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)


# List
listbox = Listbox(main, width="30", height="20", bd="3")
listbox.place(x=5, y=5)


def fill_list():
    for i in range(listbox.size()):
        listbox.delete(0)

    for element in task.list:
        s = "[x]  " if element['complete'] else "[-]  "
        s += element['title']
        listbox.insert(END, s)


fill_list()

# input task
input_text = Entry(main, width="28")
input_text.place(x=10, y=355)


# Add button and function
def Add():
    task.Add(input_text.get())
    for x in input_text.get():
        input_text.delete(0)
    fill_list()


btn_add = Button(main, text="Add", width="25", command=Add)
btn_add.place(x=10, y=385)


# Remove button and function
def Remove():
    if len(listbox.curselection()) == 0:
        return

    if listbox.curselection()[0]:
        task.Remove(listbox.curselection()[0])
    fill_list()


btn_remove = Button(main, text="Remove", width="25", command=Remove)
btn_remove.place(x=10, y=415)


# Complete Button and function
def Complete():
    if len(listbox.curselection()) == 0:
        return

    if listbox.curselection()[0]:
        task.Complete(listbox.curselection()[0])
    fill_list()


btn_compelete = Button(main, text="complete", width="25", command=Complete)
btn_compelete.place(x=10, y=445)


# Start the main loop
main.mainloop()
