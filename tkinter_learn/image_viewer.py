from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Switcher")
root.resizable(width=True, height=True)

my_img1 = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/Tester.png'))
my_img2 = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/Right.png'))
my_img3 = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/Left.png'))
my_img4 = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/tester1.png'))
my_img5 = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/icon.png'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
 
view_image = Label(image=my_img1)
view_image.grid(row=0, column=0, columnspan = 3)


def forward(image_number):
    global view_image
    global right_button
    global left_button

    view_image.grid_forget()
    view_image = Label(image=image_list[image_number-1])
    right_button = Button(root, image=right_button, command=lambda:(image_number+1))
    right_button.grid(row=1, column=2)
    left_button = Button(root, image=left_image, command=lambda:(image_number-1))
    left_button.grid(row=1, column = 0)
    view_image.grid(row=0, column=0, columnspan = 3)


def back():
    global my_label
    global right_button
    global left_button




right_image = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/Right.png'))
left_image = ImageTk.PhotoImage(Image.open('/Users/karolkul/Desktop/PNG/Left.png'))
right_button = Button(root, image=right_image, command=lambda:forward(2))
right_button.grid(row=1, column=2)
left_button = Button(root, image=left_image, command=back)
left_button.grid(row=1, column = 0)
exit_button = Button(root, text="Exit", command=root.quit)
exit_button.grid(row=1, column=1)


root.mainloop()
