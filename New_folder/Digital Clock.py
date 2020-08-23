from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
def time():
    string = strftime('%H:%H:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri',40,'bold'),background = 'red',foreground = 'white')
lbl.pack(anchor = 'center')
time()

mainloop()
