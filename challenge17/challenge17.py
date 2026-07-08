'''
Personal Library Manager

This combines nearly everything you've learned.

Create a command-line application where a user can:

1 Add Book

2 Remove Book

3 Search Book

4 List Books

5 Save Library

6 Load Library

7 Exit

Each book should have:

title
author
year
genre
pages
whether it has been read

Requirements:

Store the books as a list of dictionaries (or a Book class if you want an extra challenge).
Save the library to a JSON file and load it when the program starts.
Organize your code into functions like add_book(), remove_book(), and save_library().
Handle invalid user input gracefully using try/except or while loops.
'''
import json

class Book:

    book = {}

    def __init__(self, title, author, year, genre, pages, read=False):
        self.book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "pages": pages,
            "read": read
        }

    def __repr__(self):
        return f"\"{self.book["title"]}\", {self.book["author"]}, {self.book["year"]}, {self.book["genre"]}, {self.book["pages"]}, {self.book["read"]}"

    def get_book_dictionary(self):
        return self.book
     
    def get_title(self):
        return self.book.get("title")

# ============================================================
def add_book(book_list, book):
    book_list.append(book)
    return book_list

def remove_book(book_list, book):
    book_list.remove(book)
    return book

def search_book(book_list, title):
    for this_book in book_list:
        if this_book.get_title() == title:
            return this_book
    return ""

def list_books(book_list):
    for this_book in book_list:
        print(this_book, '\n')

def save_library(book_list):
    if book_list:
        with open("challenge17/allbooks.json", 'w') as file:
            file.write("[")
            suffix = ", "
            for i in range(len(book_list)):
                if i == len(book_list) - 1:
                    suffix = "]"
                file.write(json.dumps({f'book{i+1}': book_list[i].get_book_dictionary()}) + suffix)


def load_library():
    book_list = []
    with open("challenge17/allbooks.json", 'r') as file:
        json_data = json.load(file)
        for this_book in json_data:
            # each item has one key: "book1", "book2", ...
            book_data = list(this_book.values())[0]
            add_book(book_list, Book(
                book_data["title"],
                book_data["author"],
                book_data["year"],
                book_data["genre"],
                book_data["pages"],
                book_data["read"]
    ))
    return book_list 

def get_book_information():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year = input("Enter the book's release year: ")
    genre = input("Enter the book's genre: ")
    pages = input("Enter the number of pages in the book: ")
    read_book = input('Enter "True" if you have read the book, otherwise enter "False": ')
    return Book(title, author, year, genre, pages, read_book)


def main():
    # Create 10 sample books inside a dictionary
    books = [
        Book("The Silent Forest", "Ava Greenwood", 1998, "Fantasy", 412),
        Book("Quantum Drift", "Leo Hartman", 2021, "Science Fiction", 336, False),
        Book("Beneath the Willow", "Clara James", 2005, "Drama", 289),
        Book("Iron Horizon", "Marcus Vale", 2017, "Thriller", 501),
        Book("The Last Ember", "Nora Flint", 2010, "Adventure", 377, True),
        Book("Echoes of Tomorrow", "Julian Crest", 2023, "Sci-Fi", 254),
        Book("Shattered Paths", "Elena Ward", 2015, "Mystery", 318),
        Book("Crimson Tide", "Rafael Stone", 2001, "Horror", 198),
        Book("Golden Atlas", "Mira Dalton", 1994, "Historical Fiction", 443, True),
        Book("Fragments of Light", "Theo Maren", 2020, "Literary Fiction", 265)
    ]

    save_library(books)
    books = []

    choice = ""
    while not(choice.lower() == "exit"):
        choice = input('\nWelcome to the command-line library!\n' +
                       'Say "add" to add a book, "remove" to remove a book, "search" to search for a book,' +
                       '"list" to list the available books, "save" to save the list to a file, "load" to load the list from a file, or "exit" to stop this program\n')
        while choice.lower() not in ["add", "remove", "search", "list", "save", "load", "exit"]:
            choice = input('\nInvalid input. Please say "add" to add a book, "remove" to remove a book, "search" to search for a book,' +
                       '"list" to list the available books, "save" to save the list to a file, "load" to load the list from a file, or "exit" to stop this program\n')
        

        match choice:
            case "add":
                add_book(books, get_book_information())
                print("Book has been added!")

            case "remove":
                title = input("What book are you looking to remove? ")
                this_book = search_book(books, title)
                if not this_book:
                    print("Book could not be found.")
                else:
                    remove_book(books, this_book)
                    print("Book has been removed!")

            case "search":
                title = input("What book are you looking for? ")
                this_book = search_book(books, title)
                if not this_book:
                    print("Book could not be found.")
                else:
                    print(this_book)

            case "list":
                list_books(books)
            
            case "save":
                save_library(books)
                print("List of books has been saved!")
            
            case "load":
                books = load_library()     
                print("List of books has been loaded!")

main()
