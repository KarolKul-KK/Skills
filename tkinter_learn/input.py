from tkinter import *

root=Tk()

e = Entry(root)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

mybutton = Button(text='Enter your name', padx=50, command=myClick)
mybutton.pack()



root.mainloop()