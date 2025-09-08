class Book:
    def __init__(self, title: str):
        self.__title = title
    
    def __str__(self):
        return self.__title 
    
    def get_title(self):
        return self.__title
    
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.__title < other.get_title()