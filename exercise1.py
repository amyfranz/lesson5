# Exercise 5.1: Create a to-do list program that writes user input to a file
#
# The program should:
# Ask the user to input a new to-do item
# Read the contents of the existing to-do items
# Add the new to do item to the existing to-do items
# Save the updated to-do items
# You will need to manually create a new file called todo.txt in the same folder as your program before you start

userInput = input('What item do you want to add?') #asks the user for an item

with open('todo.txt', 'r') as text_file: #gets the file content
    contents = text_file.read()

contents += '{}\n'.format(userInput) #appends the new item to the file content

with open('todo.txt', 'w+') as text_file:
    text_file.write(contents) #overwrites the old file content with the new file content to the file

print(contents)