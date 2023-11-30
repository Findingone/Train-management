from tkinter import *
from tkinter import ttk
import CreateDb as cd
import Queries as qu

class FeetToMeters:

    def __init__(self, root):

        root.title("All trains of passengers")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        ttk.Button(mainframe, text="Create sample Db", command=self.createDb).grid(row=0, column=7, sticky=(N,S,W,E))

        ttk.Label(mainframe, text="Enter first name: ").grid(row=1, column=1, sticky=(N,S,W,E))
        self.fname_entry = ttk.Entry(mainframe)
        self.fname_entry.grid(row=1, column=2, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Label(mainframe, text="Enter last name: ").grid(row=2, column=1, sticky=(N,S,W,E))
        self.lname_entry = ttk.Entry(mainframe)
        self.lname_entry.grid(row=2, column=2, padx=10, pady=10, sticky=(N,S,W,E))

        ttk.Button(mainframe, text="Get Trains", command=self.findPassengersTrains).grid(row=3, column=2, sticky=(N,S,W,E))

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        columns = ("Train number", "Train name", "Source", "Destination","Ticket type", "Status")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=(N,S,W,E))

        root.bind("<Return>", self.findPassengersTrains)

            
    def createDb(self):
        cd.createDb()
    
    def findPassengersTrains(self, *args):
        data = qu.findTrainsPassenger(self.fname_entry.get(), self.lname_entry.get())
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            self.tree.insert("", "end", values=row)



root = Tk()
FeetToMeters(root)
root.mainloop()