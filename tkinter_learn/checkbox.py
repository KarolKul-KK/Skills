from tkinter import *
from PIL import ImageTk, ImageTk


root = Tk()
root.title('Code at home')
root.geometry('400x400')

def show():
    myLabel = Label(root, text=var.get()).pack()



#var = IntVar()
var = StringVar()

c = Checkbutton(root, text='Check this box.', variable=var, onvalue='on', offvalue='off')
c.deselect()
c.pack()


myButton = Button(root, text='Show selection', command=show).pack()




root.mainloop()