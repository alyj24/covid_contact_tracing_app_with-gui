print("Final Project".center(38, "="))
print("\033[93m=" * 38)
print("\033[95mCOVID-19 CONTACT TRACING AP WITH GUI")
print("\033[93m=" * 38)

# pseudocode
# import a text file
'''A comma-separated values file is a text file that uses a comma to separate values, giving rise to the name of this file format.'''
import csv

# create the class that will represent the app
class CCTracingApp:
    def __init__(self):
        pass

    # establish the functions
    '''Record the gathered data in a CSV file.'''
    def add_entry(self, name, bday, gender, phone, email, address, date, result):
        with open("contact_tracing.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, bday, gender, phone, email, address, date, result])

    '''Extract data from the CSV file and look for a corresponding name.'''
    def search_entry(self, name):
        entries = []
        with open("contact_tracing.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

                '''Verify if the name corresponds and display a message indicating whether the entry is located or not.'''
                if row[0] == name:
                    entries.append(row)
        return entries