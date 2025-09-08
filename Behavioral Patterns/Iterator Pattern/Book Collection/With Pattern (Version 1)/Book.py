class Book:
    def __init__(self, title: str):
        self.__title = title
    
    def __str__(self):
        return self.__title