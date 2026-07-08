"""
Challenge 15

Create a

Library

class.

It stores multiple books.

Methods

add_book()

remove_book()

list_books()

"""

class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        return self.__repr__()
    
    def __repr__(self):
        this_str = ""
        for book in self.books:
            this_str += str(book) + ",\n"
        return this_str.removesuffix(",\n")
    

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):
        return f"[{self.title}, {self.author}, {self.pages} pages]"

    

def main():
    book1 = Book("Odyssey", "Homer", 320)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 437)
    book3 = Book("The Merchant of Venice", "William Shakespeare", 298)

    this_library = Library([book1, book2, book3])

    this_library.remove_book(book2)

    this_library.add_book(Book("New book", "me", 1000))

    print(this_library.list_books())

    print(this_library)


main()
