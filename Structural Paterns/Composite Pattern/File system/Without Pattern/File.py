class File:
    def __init__(self, name, size):
        self.__name = name
        self.__size = size
    
    def get_size(self):
        return self.__size
    
    def get_details(self, prefix = ""):
        return f"{prefix}- {self.__name}: {self.__size} KB"