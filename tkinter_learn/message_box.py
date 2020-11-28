from tkinter import *
from PIL import ImageTk, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Learn code at home')

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showerror('This is my popup', 'Hello World!')
    Label(root, text=response).pack()
    #if response == "yes":
    #    Label(root, text="You clicked yes!").pack()
    #else:
    #    Label(root, text="You clicked no!").pack()


Button(root, text="popup", command=popup).pack()




mainloop()