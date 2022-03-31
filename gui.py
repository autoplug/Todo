#!/usr/bin/python
from task import *
from tkinter import *


main = Tk()
main.geometry("300x500")
main.resizable(False, False)
main.title('TODO')

main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)


task = Task()


# List
list = Listbox(main, width="30", height="20", bd="3")
list.grid()


def fill_list():
    for i in range(len(task.list)):
        s = "[x] " if task.list[i]['complete'] else "[-] "
        s += task.list[i]['title']
        list.insert(i+1, s)


fill_list()

input_text = Entry(main, width="80")
input_text.grid()


def Add():
    Add.counter += 1
    if not input_text.get():
        return
    list.insert(Add.counter, input_text.get())
    for x in input_text.get():
        input_text.delete(0)


Add.counter = 0

btn_add = Button(main, text="Add", width="90", command=Add)
btn_add.grid()


def Remove():
    list.delete(list.curselection())
    pass


btn_remove = Button(main, text="Remove", width="90", command=Remove)
btn_remove.grid()


def Compelete():
    pass


btn_compelete = Button(main, text="Compelete", width="90", command=Compelete)
btn_compelete.grid()

main.mainloop()
