from Book import Book
from typing import List

class BookCollection:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book: Book):
        self.__books.append(book)
    
    def get_books(self):
        return self.__books