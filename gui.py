from tkinter import *

def onclick():
    text.configure(text=input.get(1.0, "end-1c"))

root = Tk()

root.title('PyTrade')
root.geometry('500x400')


button = Button(root, text="Enter", fg="black", command=onclick)
button.grid(column=1, row=1)

input = Text(root, height=5, width=20)
input.grid(column=1, row=3)

text = Label(text="")
text.grid(column=1, row=4)

root.mainloop()