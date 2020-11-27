from tkinter import *
from PIL import ImageTk,ImageTk

root = Tk()
root.title('Learn to Code at home')

#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom" , "Mushroom"),
    ("Onion" , "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor='w')

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


#Radiobutton(root, text='Option1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text='Option2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

#my_label = Label(root, text=pizza.get())
#y_label.pack()

myButton = Button(root, text='Click Me!', command=lambda: clicked(pizza.get())).pack()

mainloop()