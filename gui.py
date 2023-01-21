from tkinter import *

class Window:
    def __init__(self, master):

        self.master = master
        self.master.title('PyTrade')
        self.master.geometry('600x400')
        self.master.bind('<Return>', self.onClick)

        self.options = [1, 2, 3]

        # text
        self.title = Label(self.master, text="Welcome to PyTrade", font=('Arial', 24, 'bold'))
        self.title.grid(column=1, row=1)
        
        #self.errorText = Label(self.master, text="Please select all options", font=('Arial', 16), fg="red")
        #self.errorText.grid(column=1, row=7)


        # button
        self.button2= Button(self.master, text="New Window", fg="#000000", command=self.onClick)
        self.button2.grid(column=1, row=6)

        def setRisk():
            self.options[0] = self.x.get()
            print(self.x.get())

        def setReturn():
            self.options[1] = self.y.get()
            print(self.y.get())

        self.riskOptions = ["Low Risk", "Medium Risk", "High Risk"]
        self.x = StringVar(self.master, "1")
        for i in range(len(self.riskOptions)):
            Radiobutton(master, text = self.riskOptions[i], variable = self.x, value = self.riskOptions[i],
                    command=setRisk, width=12).grid(column=0, row=3+i)

        self.returnOptions = ["Low Return", "Medium Return", "High Return"]
        self.y = StringVar(self.master, "2")
        for i in range(len(self.riskOptions)):
            Radiobutton(master, text = self.returnOptions[i], variable = self.y, value = self.returnOptions[i],
                command=setReturn, width=15).grid(column=1, row=3+i)


        self.industryOptions = ["Select an industry", "Oil", "Tech", "Healthcare"]
        self.selectedIndustry = StringVar()
        self.selectedIndustry.set("Select an industry")

        self.industryMenu = OptionMenu(self.master, self.selectedIndustry, *self.industryOptions)
        self.industryMenu.grid(column=3, row=3)
    
    def onClick(self):
        self.options[2] = self.selectedIndustry.get()
        print(self.options[2])
        if (self.options[0] != 1 and self.options[1] != 2 and self.options [2] != "Select an industry"):
            for i in self.options:
                print(i)
            self.subWindow()
            self.errorText.configure(font=('Arial', 0))

        else:
            self.errorText = Label(self.master, text="Please select all options", font=('Arial', 16), fg="red")
            self.errorText.grid(column=1, row=7)
    
    def subWindow(self):
        win = Tk()
        win.title('Data')
        sub = Table(win, data)
        win.mainloop()


class Table:
    def __init__(self, root, data):
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.entry = Entry(root, width=10, fg='white')
                self.entry.grid(row=i, column=j)
                self.entry.insert(END, str(data[i][j]))



data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = Tk()
window = Window(x)
x.mainloop()


