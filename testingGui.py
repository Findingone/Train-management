from tkinter import *
from tkinter import ttk
import CreateDb as cd
import Queries as qu

class FeetToMeters:
    def __init__(self, root):

        root.title("Train management application")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ttk.Button(self.mainframe, text="Train finder", command=self.train_finder).grid(row=0, column=0, sticky=(N,S,W,E))
        ttk.Button(self.mainframe, text="Passenger list (date)", command=self.passengerList_date).grid(row=0, column=1, sticky=(N,S,W,E))
        ttk.Button(self.mainframe, text="Age passenger tracker", command=self.AgeTracker).grid(row=0, column=2, sticky=(N,S,W,E))
        ttk.Button(self.mainframe, text="Passenger count", command=self.createDb).grid(row=0, column=3, sticky=(N,S,W,E))
        ttk.Button(self.mainframe, text="Passenger list (train)", command=self.passengerList_train).grid(row=0, column=4, sticky=(N,S,W,E))
        ttk.Button(self.mainframe, text="Cancel ticket", command=self.cancelTicket).grid(row=0, column=5, sticky=(N,S,W,E))
        ttk.Button(self.mainframe, text="Create sample Db", command=self.createDb).grid(row=0, column=7, sticky=(N,S,W,E))
        self.train_finder()
        
    def createDb(self):
        cd.createDb()

    def train_finder(self):
        self.secondFrame = ttk.Frame(self.mainframe)
        self.secondFrame.grid(row=2, column=0, columnspan=8, sticky=(N,S,W,E))
        ttk.Label(self.secondFrame, text="Enter first name: ").grid(row=0, column=0)
        self.fname_entry = ttk.Entry(self.secondFrame)
        self.fname_entry.grid(row=0, column=1, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Label(self.secondFrame, text="Enter last name: ").grid(row=1, column=0)
        self.lname_entry = ttk.Entry(self.secondFrame)
        self.lname_entry.grid(row=1, column=1, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Button(self.secondFrame, text="Get Trains", command=self.findPassengersTrains).grid(row=3, column=1, sticky=(N,S,W,E))

        for child in self.secondFrame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        columns = ("Train number", "Train name", "Source", "Destination","Ticket type", "Status")
        self.tree = ttk.Treeview(self.secondFrame, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=(N,S,W,E))

        root.bind("<Return>", self.findPassengersTrains)
            
    def findPassengersTrains(self, *args):
        data = qu.findTrainsPassenger(self.fname_entry.get(), self.lname_entry.get())
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            self.tree.insert("", "end", values=row)

    def passengerList_date(self):
        self.secondFrame.destroy()
        self.secondFrame = ttk.Frame(self.mainframe)
        self.secondFrame.grid(row=2, column=0, columnspan=8)
        ttk.Label(self.secondFrame, text="Enter date of travel(yyyy-dd-mm): ").grid(row=0, column=0)
        self.date_entry = ttk.Entry(self.secondFrame)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10, sticky=(N,S,W,E))
        ttk.Button(self.secondFrame, text="Get passenger list", command=self.passengers_from_date).grid(row=3, column=1, sticky=(N,S,W,E))

        columns = ("First name", "Last name", "Address")
        self.tree = ttk.Treeview(self.secondFrame, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=(N,S,W,E))

        root.bind("<Return>", self.passengers_from_date)

    def passengers_from_date(self, *args):
        data = qu.passengers_from_date(self.date_entry.get())
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            self.tree.insert("", "end", values=row)



    def AgeTracker(self):
        self.secondFrame.destroy()
        self.secondFrame = ttk.Frame(self.mainframe)
        self.secondFrame.grid(row=2, column=0, columnspan=8, sticky=(N,S,W,E))
        ttk.Label(self.secondFrame, text="Enter starting age: ").grid(row=0, column=0)
        self.startAge_entry = ttk.Entry(self.secondFrame)
        self.startAge_entry.grid(row=0, column=1, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Label(self.secondFrame, text="Enter ending age: ").grid(row=1, column=0)
        self.endAge_entry = ttk.Entry(self.secondFrame)
        self.endAge_entry.grid(row=1, column=1, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Button(self.secondFrame, text="Get Trains", command=self.passengerAge_query).grid(row=3, column=1, sticky=(N,S,W,E))

        for child in self.secondFrame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        columns = ("Train number", "Train name", "Source", "Destination","Passenger first name", "Passenger last name", "Address", "Ticket type", "Status")
        self.tree = ttk.Treeview(self.secondFrame, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=(N,S,W,E))

        root.bind("<Return>", self.passengerAge_query)
            
    def passengerAge_query(self, *args):
        data = qu.passengers_age(int(self.startAge_entry.get()), int(self.endAge_entry.get()))
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            self.tree.insert("", "end", values=row)

    def passengerList_train(self):
        self.secondFrame.destroy()
        self.secondFrame = ttk.Frame(self.mainframe)
        self.secondFrame.grid(row=2, column=0, columnspan=8)
        ttk.Label(self.secondFrame, text="Enter train name: ").grid(row=0, column=0)
        self.date_entry = ttk.Entry(self.secondFrame)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10, sticky=(N,S,W,E))
        ttk.Button(self.secondFrame, text="Get passenger list", command=self.passengers_from_train).grid(row=3, column=1, sticky=(N,S,W,E))

        columns = ("First name", "Last name", "Address", "Train name", "Status")
        self.tree = ttk.Treeview(self.secondFrame, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=(N,S,W,E))

        root.bind("<Return>", self.passengers_from_train)

    def passengers_from_train(self, *args):
        data = qu.passengers_from_train(self.date_entry.get())
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            self.tree.insert("", "end", values=row)

    def cancelTicket(self):
        self.secondFrame.destroy()
        self.secondFrame = ttk.Frame(self.mainframe)
        self.secondFrame.grid(row=2, column=0, columnspan=8)
        ttk.Label(self.secondFrame, text="Enter passenger ssn: ").grid(row=0, column=0)
        self.pass_ssn = ttk.Entry(self.secondFrame)
        self.pass_ssn.grid(row=0, column=1, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Label(self.secondFrame, text="Enter train number: ").grid(row=1, column=0)
        self.train_num = ttk.Entry(self.secondFrame)
        self.train_num.grid(row=1, column=1, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Button(self.secondFrame, text="Cancel ticket", command=self.cancelTicket_query).grid(row=3, column=1, sticky=(N,S,W,E))

        root.bind("<Return>", self.cancelTicket_query)

    def cancelTicket_query(self, *args):
        data = qu.delete_record(int(self.pass_ssn.get()), int(self.train_num.get()))
        

root = Tk()
FeetToMeters(root)
root.mainloop()