from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn To code at home")
#root.iconbitmap('/Users/karkul/Desktop/icon.png')
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


my_img = ImageTk.PhotoImage(Image.open("/Users/karolkul/Desktop/icon.png"))
my_label = Label(image=my_img)
my_label.pack()





root.mainloop()