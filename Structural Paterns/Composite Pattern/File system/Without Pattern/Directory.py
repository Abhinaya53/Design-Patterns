from typing import List
from File import File

class Directory:
    def __init__(self, name):
        self.__name = name
        self.__files: List[File] = []
        self.__size = 0
    
    def add_file(self, file):
        self.__files.append(file)

    def get_size(self):
        total_size = 0
        for file in self.__files:
            total_size += file.get_size()
        return total_size
    
    def get_details(self, prefix = ""):
        details = f"{prefix}+ {self.__name}: {self.get_size()} KB\n"
        for file in self.__files:
            details += file.get_details(prefix + "\t") + "\n"
        return details[:-2] # Remove the last newline character