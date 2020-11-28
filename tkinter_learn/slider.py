from tkinter import *
from PIL import ImageTk, ImageTk


root = Tk()
root.title('Learn code at home')
root.geometry('400x400')

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))


vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


my_btn = Button(root, text="click me!", command=slide).pack()


root.mainloop()