"""
Challenge 14

Create

class Book

Each book has

title
author
pages

Create three books.

Print them.

"""



class Book:
    # these three lines below are not needed, as __init__ will automatically create new variables if they don't exist
    title = ""
    author = ""
    pages = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def getAll(self):
        return f"{self.title} by {self.author}, {self.pages} pages\n"
    

def main():
    book1 = Book("Uhh", "ya mum", 32)
    book2 = Book("jo", "mama", 70000)
    book3 = Book("bruh", "type", 3)

    print(book1.getAll(), book2.getAll(), book3.getAll())

main()
