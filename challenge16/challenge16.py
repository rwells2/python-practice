'''
Create a small command-line chatbot that:

asks the user for their name
remembers it
stores it in a dictionary
saves it as JSON
loads it the next time the program runs
greets the user by name

For example:

Welcome!

What's your name?

Alex

Later...

Welcome back Alex!

You'll use:

variables
functions
dictionaries
JSON
files
'''

import json

person = {}

def main():
    global person
    filename = "challenge16/storage.json"
    
    # if the file is empty
    if not read_file(filename):
        person.update({"name": input("What is your name? ")})
        write_to_file(filename, person)
    else:
        print(f"Welcome back {person["name"]}!")

        # automatically removes file contents to reset program
        with open(filename, 'w'):
            pass


def read_file(filename):
    global person
    with open(filename, 'r') as file:
        try:
            person = json.load(file)
            return True
        except json.JSONDecodeError:
            return False
        


def write_to_file(filename, json_text):
    with open(filename, 'w') as file:
        file.write(json.dumps(json_text))


main()