from tkinter import *

def onclick():
    button.configure(text="Clicked")

root = Tk()

root.title('PyTrade')
root.geometry('500x400')



button = Button(root, text="Hello World", fg="black", command=onclick)
button.grid(column=1, row=1)

root.mainloop()