

# opens file 'people.txt'
# w+ allows one to overwrite in a file and will create a new file if a file does not exists
# saves the file as text_file
with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAmina' # \n is a new line

    text_file.write(people) # text_file.write() overwrites the file text_file with the content that is passed through

#opens the file 'people,txt' and saves it as text_file, if the file does not exist it throughs an error
with open('people.txt', 'r') as text_file:
    contents = text_file.read() #text_file.read() gets the content from the file as a string

print(contents)