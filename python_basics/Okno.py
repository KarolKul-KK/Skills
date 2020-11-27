from tkinter import *
from math import *

root = Tk()
root.title("Kalkulator")
up_window = Entry(root)
up_window.grid(row=0, column=0,padx=10, pady=10, columnspan=4)

number = []
result = []
sign = []

def Number_saver():
    number.append(up_window.get())
    up_window.delete(0, END)
     
def resolution():
    if sign[-1] == '+':
        for s in number:
            s = 0
            s = int(up_window.get()) + int(number[-1])
            result.append(s)
        print(result[-1])
        up_window.delete(0, END)
        up_window.insert(END, int(result[-1]))
    elif sign[-1] == '-':
        for s in number:
            s = 0
            s = int(up_window.get()) - int(number[-1])
            result.append(-s)
        print(result[-1])
        up_window.delete(0, END)
        up_window.insert(END, int(result[-1]))
    elif sign[-1] == '*':
        for s in number:
            s = 1
            s = int(up_window.get()) * int(number[-1])
            result.append(s)
        print(result[-1])
        up_window.delete(0, END)
        up_window.insert(END, int(result[-1]))
    elif sign[-1] == '/':
        for s in number:
            s = 1
            s = int(number[-1]) / int(up_window.get())
            result.append(s)
        print(result[-1])
        up_window.delete(0, END)
        up_window.insert(END, int(result[-1]))
    else:
        pass

class Interface:

    def Buttons():

        first_button = Button(root, text='1', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '1'))
        first_button.grid(row=2, column=0 )

        second_button = Button(root, text='2', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '2'))
        second_button.grid( row=2, column=1 )

        third_button = Button(root, text="3", fg="blue" ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '3'))
        third_button.grid( row=2, column=2 )

        fourth_button = Button(root, text='4', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '4'))
        fourth_button.grid( row=3, column=0 )

        fifth_button = Button(root, text='5', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '5'))
        fifth_button.grid( row=3, column=1 )

        sixth_button = Button(root, text='6', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '6'))
        sixth_button.grid( row=3, column=2 )

        seventh_button = Button(root, text='7', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '7'))
        seventh_button.grid( row=4, column=0 )

        eighth_button = Button(root, text='8', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '8'))
        eighth_button.grid( row=4, column=1 )

        ninth_button = Button(root, text='9', fg='blue', padx=20 ,pady=30, command=lambda: up_window.insert(END, '9'))
        ninth_button.grid( row=4, column=2 )

        backspace_button = Button(root, text='C', fg='blue', padx=20 ,pady=30, command=lambda: up_window.delete(0, END))
        backspace_button.grid( row=1, column=3)

        plus_button = Button(root, text='+', fg='blue', padx=20 ,pady=30, command=lambda:[ sign.append('+'), Number_saver()])
        plus_button.grid( row=2, column=3)

        minus_button = Button(root, text='-', fg='blue', padx=20 ,pady=30,command=lambda:[ sign.append('-'), Number_saver()])
        minus_button.grid( row=3, column=3)

        equal_button = Button(root, text='=', fg='blue' ,padx=20 ,pady=30, command=resolution)
        equal_button.grid( row=4, column=3)

        divide_button = Button(root, text='/', fg='blue' ,padx=20 ,pady=30, command=lambda:[ sign.append('/'), Number_saver()])
        divide_button.grid( row=1, column=1)

        multiplication_button = Button(root, text='*', fg='blue' ,padx=20 ,pady=30, command=lambda:[ sign.append('*'), Number_saver()])
        multiplication_button.grid( row=1, column=2)

        zero_button = Button(root, text='0', fg='blue' ,padx=20 ,pady=30, command=lambda: up_window.insert(END, '0'))
        zero_button.grid( row=1, column=0)


Interface.Buttons()
root.mainloop()
