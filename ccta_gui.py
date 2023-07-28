# pseudocode
# import the tkinter
import tkinter as tk

# import the existed program for the new class
from main import Covid19ContactTracingApp

# implement the functions of the class with GUI
class Covid19ContactTracingApp:
    # establish constructor
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing App")
        self.root.geometry("400x200")

    # construct the labels and methods
    self.name_label = tk.Label(root, text="Name: ", font=("Times New Roman", 11, "bold"), bg="#8470FF")
    self.name_entry = tk.Entry(root)
    
# provide instance
# add entry
# search entry
# provide instance
# check errors
# run the program