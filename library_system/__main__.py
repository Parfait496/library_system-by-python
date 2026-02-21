
from .core import Book, Library
from .utils import borrow_item

def main():
    library = Library(user_role="Admin")

    book1 = Book("Harry Potter", "J.K. Rowling", 500)
    book2 = Book("Python Basics", "John Doe", 300) 

    library.add_book(book1)
    library.add_book(book2)

    print("\nAll books:")
    for book in library:
        print(book, "- Pages:", len(book))

    print("\nBorrowing Harry Potter")
    library.borrow_book("Harry Potter")

    print("\nReturning Harry Potter")
    library.return_book("Harry Potter")

    print("\nDuck Typing Test:")

    class Magazine:
        def __init__(self, title):
            self.title = title

    mag = Magazine("Science Monthly")
    borrow_item(mag)


if __name__ == "__main__":
    main()