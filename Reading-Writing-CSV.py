
import csv #import the module csv to work with CSVs

# Writing to a CSV file

field_names = ['name', 'age'] #Declare your headings that you want your CSV to have

data = [ # Create an list of dictionaries for the information you want to write to the CSVs file
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file: #opens the file 'team.csv' to write and saves the file as csv_file
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names) #declares what the headings are on the CSV

    spreadsheet.writeheader() #Writes the headings to the CSV - optional
    spreadsheet.writerows(data) #Writes the data to the CSV

# Reading a CSV
with open('team.csv', 'r') as csv_file: #opens the file 'team.csv' to read and saves the file as csv_file
    spreadsheet = csv.DictReader(csv_file) #Gets the contents of the file
    for row in spreadsheet: #Goes through each row of the spreadsheet
        print(dict(row)) #prints the content of each row