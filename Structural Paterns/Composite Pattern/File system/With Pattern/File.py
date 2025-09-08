from FileComponent import FileComponent

class File(FileComponent):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size
    
    def get_size(self) -> int:
        return self.__size
    
    def get_details(self, prefix: str = "") -> str:
        return f"{prefix}- {self.__name}: {self.__size} KB"