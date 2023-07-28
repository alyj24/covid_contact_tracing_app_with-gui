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

    self.address_label = tk.Label(root, text="Address: ", font=("Times New Roman", 11, "bold"), bg="#FFB6C1")
    self.address_entry = tk.Entry(root)

    self.birthday_label = tk.Label(root, text="Date of Birth: ", font=("Times New Roman", 11, "bold"), bg="#B0E2FF")
    self.birthday_label_entry = tk.Entry(root)

    self.gender_label = tk.Label(root, text="Gender: ", font=("Times New Roman", 11, "bold"), bg="#EEA2AD")
    self.gender_entry = tk.Entry(root)

    self.number_label = tk.Label(root, text="Phone Number: ", font=("Times New Roman", 11, "bold"), bg="#F08080")
    self.number_entry = tk.Entry(root)

    self.email_label = tk.Label(root, text="Email Address: ", font=("Times New Roman", 11, "bold"), bg="#E4CCB4")
    self.email_entry = tk.Entry(root)

    self.exposed_label = tk.Label(root, text="Haye you ever been exposed recently with COVID-19 Patients? ", font=("Times New Roman", 11, "bold"), bg="#FFF68F")
    self.exposed_entry = tk.Entry(root)
    
# provide instance
# add entry
# search entry
# provide instance
# check errors
# run the program