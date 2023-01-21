from tkinter import *

# text is changed upon button click
def onclick():
    text.configure(text=input.get())

# initializing window
root = Tk()
root.title('PyTrade')
root.geometry('500x400')

# button
button = Button(root, text="Enter", fg="black", command=onclick)
button.grid(column=1, row=1)

# text box
input = Entry(root, width=20)
input.grid(column=1, row=3)

# text
text = Label(text="")
text.grid(column=1, row=4)


# runs window
root.mainloop()