from tkinter import *

class Window:
    def __init__(self, master):

        # window init
        self.master = master
        self.master.title('PyTrade')
        self.master.geometry('600x400')
        self.master.bind('<Return>', lambda e:self.onClick())

        # variables
        self.errorText = False
        self.options = [1, 2, "Select an industry"]

        # text
        self.title = Label(self.master, text="Welcome to PyTrade", font=('Arial', 24, 'bold'))
        self.title.grid(column=1, row=1)
        
        #self.errorText = Label(self.master, text="Please select all options", font=('Arial', 16), fg="red")
        #self.errorText.grid(column=1, row=7)


        # button
        self.button2= Button(self.master, text="New Window", fg="#000000", command=self.onClick)
        self.button2.grid(column=1, row=6)

        # risk selections
        self.riskOptions = ["Low Risk", "Medium Risk", "High Risk"]
        self.x = StringVar(self.master, "1")
        for i in range(len(self.riskOptions)):
            Radiobutton(master, text = self.riskOptions[i], variable = self.x, value = self.riskOptions[i],
                    command=self.setRisk, width=12).grid(column=0, row=3+i)

        # return selections
        self.returnOptions = ["Low Return", "Medium Return", "High Return"]
        self.y = StringVar(self.master, "2")
        for i in range(len(self.riskOptions)):
            Radiobutton(master, text = self.returnOptions[i], variable = self.y, value = self.returnOptions[i],
                command=self.setReturn, width=15).grid(column=1, row=3+i)

        # industry selection
        self.industryOptions = ['Advertising Agencies', 'Aerospace & Defense', 'Agricultural Inputs', 'Airlines', 'Airports & Air Services', 'Aluminum', 'Apparel Manufacturing', 'Apparel Retail', 'Asset Management', 'Auto & Truck Dealerships', 'Auto Components', 'Auto Manufacturers', 'Auto Parts', 'Banks', 'Banks - Diversified', 'Banks - Regional', 'Banks-Regional', 'Beverages - Brewers', 'Beverages - Non-Alcoholic', 'Beverages - Wineries & Distilleries', 'Biotechnology', 'Blank Check / SPAC', 'Broadcasting', 'Building Materials', 'Building Products & Equipment', 'Business Equipment & Supplies', 'Business Services', 'Capital Markets', 'Chemicals', 'Coking Coal', 'Communication Equipment', 'Computer Hardware', 'Confectioners', 'Conglomerates', 'Construction & Engineering', 'Consulting Services', 'Consumer Electronics', 'Consumer Finance', 'Copper', 'Credit Services', 'Department Stores', 'Diagnostics & Research', 'Discount Stores', 'Drug Manufacturers - General', 'Drug Manufacturers - Specialty & Generic', 'Drug Manufacturers-General', 'Drug Manufacturers-Specialty & Generic', 'Drug Manufacturers—General', 'Drug Manufacturers—Specialty & Generic', 'Education & Training Services', 'Electrical Equipment & Parts', 'Electronic Components', 'Electronic Gaming & Multimedia', 'Electronics & Computer Distribution', 'Energy Equipment & Services', 'Engineering & Construction', 'Entertainment', 'Equity Real Estate Investment Trusts (REITs)', 'Farm & Heavy Construction Machinery', 'Farm Products', 'Financial Conglomerates', 'Financial Data & Stock Exchanges', 'Food & Staples Retailing', 'Food Distribution', 'Footwear & Accessories', 'Furnishings, Fixtures & Appliances', 'Gambling', 'Gold', 'Grocery Stores', 'Health Care Equipment & Supplies', 'Health Care Providers & Services', 'Health Care Technology', 'Health Information Services', 'Healthcare Plans', 'Home Improvement Retail', 'Household & Personal Products', 'Household Durables', 'Industrial Distribution', 'Industry', 'Information Technology Services', 'Infrastructure Operations', 'Insurance', 'Insurance - Diversified', 'Insurance - Life', 'Insurance - Property & Casualty', 'Insurance - Reinsurance', 'Insurance - Specialty', 'Insurance Brokers', 'Insurance-Life', 'Integrated Freight & Logistics', 'Interactive Media & Services', 'Internet Content & Information', 'Internet Retail', 'Investment Holding Companies', 'Leisure', 'Lodging', 'Lumber & Wood Production', 'Luxury Goods', 'Machinery', 'Marine', 'Marine Shipping', 'Media', 'Medical Care Facilities', 'Medical Devices', 'Medical Distribution', 'Medical Instruments & Supplies', 'Metal Fabrication', 'Mortgage Finance', 'Oil & Gas Drilling', 'Oil & Gas E&P', 'Oil & Gas Equipment & Services', 'Oil & Gas Integrated', 'Oil & Gas Midstream', 'Oil & Gas Refining & Marketing', 'Other Industrial Metals & Mining', 'Other Precious Metals & Mining', 'Packaged Foods', 'Packaging & Containers', 'Paper & Paper Products', 'Personal Services', 'Pharmaceutical Retailers', 'Pharmaceuticals', 'Pollution & Treatment Controls', 'Professional Services', 'Publishing', 'REIT - Diversified', 'REIT - Healthcare Facilities', 'REIT - Hotel & Motel', 'REIT - Industrial', 'REIT - Mortgage', 'REIT - Office', 'REIT - Residential', 'REIT - Retail', 'REIT - Specialty', 'REIT—Diversified', 'REIT—Healthcare Facilities', 'REIT—Industrial', 'REIT—Mortgage', 'REIT—Residential', 'REIT—Retail', 'REIT—Specialty', 'Railroads', 'Real Estate - Development', 'Real Estate - Diversified', 'Real Estate Services', 'Recreational Vehicles', 'Rental & Leasing Services', 'Residential Construction', 'Resorts & Casinos', 'Restaurants', 'Scientific & Technical Instruments', 'Security & Protection Services', 'Semiconductor Equipment & Materials', 'Semiconductors', 'Shell Companies', 'Silver', 'Software - Application', 'Software - Infrastructure', 'Software-Application', 'Software-Infrastructure', 'Software—Application', 'Software—Infrastructure', 'Solar', 'Specialty Business Services', 'Specialty Chemicals', 'Specialty Industrial Machinery', 'Specialty Retail', 'Staffing & Employment Services', 'Steel', 'Telecom Services', 'Textile Manufacturing', 'Thermal Coal', 'Thrifts & Mortgage Finance', 'Tobacco', 'Tools & Accessories', 'Travel Services', 'Trucking', 'Uranium', 'Utilities - Diversified', 'Utilities - Independent Power Producers', 'Utilities - Regulated Electric', 'Utilities - Regulated Gas', 'Utilities - Regulated Water', 'Utilities - Renewable', 'Utilities-Diversified', 'Utilities-Renewable', 'Utilities—Regulated Electric', 'Utilities—Regulated Water', 'Utilities—Renewable', 'Waste Management']
        self.selectedIndustry = StringVar()
        self.selectedIndustry.set("Select an industry")
        
        self.industryMenu = OptionMenu(self.master, self.selectedIndustry, *self.industryOptions)
        self.industryMenu.grid(column=3, row=3)
    
    def setRisk(self):
        self.options[0] = self.x.get()
        print(self.x.get())

    def setReturn(self):
        self.options[1] = self.y.get()
        print(self.y.get())
    
    def onClick(self, event=None):
        self.options[2] = self.selectedIndustry.get()
        print(self.options[2])
        if (self.options[0] != 1 and self.options[1] != 2 and self.options [2] != "Select an industry"):
            if self.errorText:
                self.errorText.destroy()
            for i in self.options:
                print(i)
            self.subWindow()

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
            

#    def pickStocks(riskOp, returnOp, industryOp):


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = Tk()
window = Window(x)
x.mainloop()


