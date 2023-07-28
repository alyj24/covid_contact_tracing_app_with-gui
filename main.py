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

    def add_entry(self, name, birthday, gender, number, email, address, exposed, symptoms):
        with open("covid-19_contact_tracing_app.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, address, birthday, gender, number, email, exposed, symptoms])

    '''Extract data from the CSV file and look for a corresponding name.'''
    def search_entry(self, name):
        entries = []
        with open("covid-19_contact_tracing_app.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

                '''Verify if the name corresponds and display a message indicating whether the entry is located or not.'''
                if row[0] == name:
                    entries.append(row)
        return entries
