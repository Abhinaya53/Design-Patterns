from Book import Book 
from BookCollection import BookCollection

book1 = Book("Python Fundamentals")
book2 = Book("Data Structures and Algorithms")
book3 = Book("System Design")

books = BookCollection()
books.add_book(book1)
books.add_book(book2)
books.add_book(book3)

iter1 = books.create_iterator()
while iter1.has_next():
    print(iter1.next())