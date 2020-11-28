import tkinter as tk

def function(event):
    print(event.widget[button2 - button1])

root = tk.Tk()

button1 = tk.Button(root, text='1')
button1.pack()
button1.bind('<Button-1>', function)

button2 = tk.Button(root, text='2')
button2.pack()
button2.bind('<Button-1>', function)

root.mainloop()
