# spreadsheet = # Add code to open the csv file
#
# heights = []
#
# for row in spreadsheet:
#     tree_height = row['height']
#     heights.append(tree_height)
#
# shortest_height = min(heights)
# print(shortest_height)

import csv #Step 1 import CSV

with open('trees.csv', 'r') as csv_file: #Step 2 opens the file 'trees.csv' to read and saves the file as csv_file
    spreadsheet = csv.DictReader(csv_file) # Step 3 Gets the contents of the file

    heights = [] # Step 4 tab everything

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

    shortest_height = min(heights)
    print(shortest_height)