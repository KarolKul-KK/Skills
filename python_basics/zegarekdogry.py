import tkinter as Tkinter


counter = -1
running = False
def counter_label(label):
    def count():
        if running:
            global counter

            if counter==-1:
                display="Starting..."
            else:
                display=str(counter)

            label['text']=display

            label.after(1000, count)
            counter += 1

    count()


def Start(label):
    global running
    running = True
    counter_label(label)
    start["state"]="disabled"
    stop["state"]="normal"


def Stop():
    global running
    start["state"]="normal"
    stop["state"]="disabled"
    running = False

root = Tkinter.Tk()
root.title("Stopwatch")


root.minsize(width=250, height=400)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
start = Tkinter.Button(root, text='Start',
width=15, command=lambda:Start(label))
stop = Tkinter.Button(root, text='Stop',
width=15, state='disabled', command=Stop)
start.pack()
stop.pack()
root.mainloop()
