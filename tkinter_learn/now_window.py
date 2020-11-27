from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at home")

def open():
    global my_img
    top = Toplevel()
#lbl = Label(top, text='Hello World').pack()
    top.title("Top window")
    my_img = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/Tester.png'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close Window', command=top.destroy).pack()




btn = Button(root, text="Open second window", command=open).pack()






mainloop()