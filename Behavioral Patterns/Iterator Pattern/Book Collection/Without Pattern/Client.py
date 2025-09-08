from Book import Book 
from BookCollection import BookCollection

book1 = Book("Python Fundamentals")
book2 = Book("Data Structures and Algorithms")
book3 = Book("System Design")

books = BookCollection()
books.add_book(book1)
books.add_book(book2)
books.add_book(book3)

for i in range(3):
    print(books.get_books()[i])