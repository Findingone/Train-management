from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, root):
       root.title("All trains of passengers")
       mainframe = ttk.Frame(root, padding="3 3 12 12")
       mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
       root.columnconfigure(0, weight=1)
       root.rowconfigure(0, weight=1)

       ttk.Button(mainframe, text="Create sample Db").grid(row=0, column=7, sticky=(N,S,W,E))
       
       self.secondFrame = ttk.Frame(mainframe)
       self.secondFrame.grid(row=2, column=2)
       ttk.Label(self.secondFrame, text="Enter first name: ").grid(row=1, column=1, sticky=(N,S,W,E))
       self.fname_entry = ttk.Entry(self.secondFrame)
       self.fname_entry.grid(row=1, column=2, padx=10, pady=10, sticky=(N,S,W,E))
       ttk.Label(self.secondFrame, text="Enter last name: ").grid(row=2, column=1, sticky=(N,S,W,E))
       self.lname_entry = ttk.Entry(self.secondFrame)
       self.lname_entry.grid(row=2, column=2, padx=10, pady=10, sticky=(N,S,W,E))

       ttk.Button(self.secondFrame, text="Destroy the worlds!!", command=self.changeSecond).grid(row=2, column=2)
    def changeSecond(self):
        print(self.secondFrame)
        self.secondFrame.destroy()
        
root = Tk()
App(root)
root.mainloop()