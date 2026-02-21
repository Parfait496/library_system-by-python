from library_system.utils import track_access, permission_check

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        
        return isinstance(other, Book) and self.title == other.title and self.author == other.author
    

class Library:
    def __init__(self, user_role = "User"):
        self._books = []
        self.user_role = user_role
    

    #only Admin can add books
    @permission_check("Admin")
    def add_book(self, book):
        self._books.append(book)
        print('Book added')
    
    @track_access
    def borrow_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print("Book borrowed")
                return book
        print("Book not available")
        return None
    
    @track_access
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print("Book returned")
                return book
        print("Book was not borrowed")
        return None
        
    def __getitem__(self, index):
        return self._books[index]
    
    def __len__(self):
        return len(self._books)
