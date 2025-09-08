from typing import List
from FileComponent import FileComponent

class Directory(FileComponent):
    def __init__(self, name):
        self.__name = name
        self.__components: List[FileComponent] = []
        self.__size = 0
    
    def add_component(self, component: FileComponent):
        self.__components.append(component)
        self.__size += component.get_size()

    def get_size(self):
        return self.__size
    
    def get_details(self, prefix = ""):
        details = f"{prefix}+ {self.__name}: {self.get_size()} KB\n"
        for component in self.__components:
            details += component.get_details(prefix + "\t") + "\n"
        return details.rstrip() # Remove the last newline character