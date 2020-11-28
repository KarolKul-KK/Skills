from tkinter import *

root = Tk()
#creating label widget
myLabel1 = Label(root, text='Hello World!').grid(row=0, column=2)
myLabel2 = Label(root, text='My name is Karol!').grid(row=0,column=0)
myLabel3 = Label(root, text='+_+_+').grid(row=2, column=2)
#showing it onto screen

#myLabel1.grid(row=0, column=2)
#myLabel2.grid(row=1, column=0)
#myLabel3.grid(row=2, column=3)

root.mainloop()
