from tkinter import *
from PIL import ImageTk, ImageTk


root = Tk()
root.title('Code at home')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

option = ["Monday",
         "Tuesday",
          "Wednesday",
           "Thursday",
            "Friday"]

var = StringVar()
var.set(option[0])


drop = OptionMenu(root, var,  *option)
drop.pack()

myButton = Button(root, text='Show Selection', command=show).pack()




root.mainloop()