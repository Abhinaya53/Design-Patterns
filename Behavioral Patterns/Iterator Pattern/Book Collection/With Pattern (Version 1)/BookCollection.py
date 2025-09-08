from Book import Book
from Iterator import Iterator

class BookCollection:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book: Book):
        self.__books.append(book)
    
    def get_books(self):
        return self.__books
    
    def create_iterator(self):
        return self._BookIterator(self.__books)
    
    class _BookIterator(Iterator):
        def __init__(self, books):
            self.__position = 0
            self.__books = books
        
        def has_next(self):
            return len(self.__books) > self.__position
        
        def next(self):
            book = self.__books[self.__position]
            self.__position += 1
            return book