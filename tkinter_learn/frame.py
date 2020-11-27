from tkinter import *
from PIL import ImageTk,ImageTk

root = Tk()
root.title('Learn to Code at home')
root.iconbitmap('/Users/karolkul/Desktop/PNG/Tester.png')

frame = LabelFrame(root, text='This is my frame', padx = 5, pady = 5)
frame.pack(padx=100, pady=100)

b = Button(frame, text='Dont click here!')
b2 = Button(frame, text='or here!')
b2.grid(row=1, column=1)
b.grid(row=0, column=0)




root.mainloop()
