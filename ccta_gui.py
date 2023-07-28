# pseudocode
# import the tkinter
import tkinter as tk

# import the existed program for the new class
from main import Covid19ContactTracingApp

# implement the functions of the class with GUI
class C19CTAppGUI:
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

    self.symptoms_label = tk.Label(root, text="Do you experience currently symptoms of COVID-19? ", font=("Times New Roman", 11, "bold"), bg="#98F5FF")
    self.symptoms_entry = tk.Entry(root)

    # signify buttons
    self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
    self.search_button = tk.Button(root, text="Search Entry", command=self.search_entry)

    # initiate labels
    self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    self.name_entry.grid(row=0, column=1, pady=10, padx=5)

    self.address_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
    self.address_entry.grid(row=5, column=1, pady=10, padx=5)

    self.birthday_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    self.birthday_label_entry.grid(row=1, column=1, pady=10, padx=5)

    self.gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    self.gender_entry.grid(row=2, column=1, pady=10, padx=5)

    self.phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    self.phone_entry.grid(row=3, column=1, pady=10, padx=5)

    self.email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    self.email_entry.grid(row=4, column=1, pady=10, padx=5)

    self.exposed_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
    self.exposed_entry.grid(row=6, column=1, pady=10, padx=5)

    self.symptoms_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
    self.symptoms_entry.grid(row=7, column=1, pady=10, padx=5)

    self.add_button.grid(row=8, column=0, padx=10, pady=5)
    self.search_button.grid(row=8, column=1, padx=10, pady=5)

    # provide instance
    self.contact_tracing = C19CTAppGUI

    # add entry
    def add_entry(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        birthday = self.birthday_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        exposed = self.exposed_entry.get()
        symptoms = self.symptoms_entry.get()

        self.contact_tracing.add_entry(name, address, birthday, gender, phone, email, exposed, symptoms)

        self.clear_entries()
        print("The information entry is submitted successfully.")

    # search entry
    def search_entry(self):
        name = self.name_entry.get()

        # provide instance
        entry = self.contact_tracing.search_entry(name)

        if entry:
            print("Submitted Information Found:")
            for item in entry:
                print(item)
        else:
            print("Submitted Information not found")

    # check errors
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.birthday_label_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.exposed_entry.delete(0, tk.END)
        self.symptoms_entry.delete(0, tk.END)
                 
    # run the program