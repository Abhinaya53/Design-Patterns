from Book import Book 
from BookCollection import BookCollection

book1 = Book("Python Fundamentals")
book2 = Book("Data Structures and Algorithms")
book3 = Book("System Design")

books = BookCollection()
books.add_book(book1)
books.add_book(book2)
books.add_book(book3)

# One Way To Traverse:
it = iter(books)
while True:
    try:
        book = next(it)
        print(book)
    except StopIteration:
        break

# More Preferrable
for book in books:
    print(book)