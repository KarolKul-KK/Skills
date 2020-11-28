from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("code at home")



def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir ="/Users/karolkul/Desktop/PNG", title='Select a File', filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_img).pack()

my_btn = Button(root, text="Open File", command=open).pack()


root.mainloop()