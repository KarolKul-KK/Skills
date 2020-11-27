import tkinter as tk


class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: qf("Check me out, I'm passing vars!"))
        button.pack()