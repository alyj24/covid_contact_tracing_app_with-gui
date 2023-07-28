print("Final Project".center(38, "="))
print("\033[93m=" * 38)
print("\033[95mCOVID-19 CONTACT TRACING APP WITH GUI")
print("\033[93m=" * 38)

# pseudocode
# import a text file
import csv

# create the class that will represent the app
class ContactTracingApp:
    def __init__(self):
        pass
    # establish the functions
    '''Record the gathered data in a CSV file.'''

    def add_entry(self, name, bday, gender, phone, email, address, exposed, symptoms):
        with open("covid-19_contact_tracing_app.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, address, birthday, gender, phone, email, exposed, symptoms])

