from Book import Book

class BookCollection:
    def __init__(self):
        self.__books = set()
    
    def add_book(self, book: Book):
        self.__books.add(book)
    
    def get_books(self):
        return self.__books
    
    def __iter__(self):
        return self._BookIterator(sorted(self.__books))
    
    class _BookIterator:
        def __init__(self, books):
            self.__position = 0
            self.__books = books
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.__position < len(self.__books):
                book = self.__books[self.__position]
                self.__position += 1
                return book
            else:
                raise StopIteration