from tkinter import *

class Window:
    def __init__(self, master):

        self.master = master
        self.master.title('PyTrade')
        self.master.geometry('400x500')

        # button
        self.button = Button(self.master, text="Enter", fg="black", command=self.onclick)
        self.button.bind('<Return>', self.onclick)
        self.button.pack()
        
        # text box
        self.input = Entry(self.master, width=20)
        self.input.pack()

        # text
        self.text = Label(self.master, text="")
        self.text.pack()

    def onclick(self):
        self.text.configure(text=self.input.get())

x = Tk()
window = Window(x)
x.mainloop()


