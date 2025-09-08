from Image import Image

class RealImage(Image):
    def __init__(self, filename: str):
        self.__filename = filename
        self.load_from_disk()   # Expensive Operation
    
    def load_from_disk(self):
        print(f"Loading image from disk {self.__filename}")

    def display(self):
        print(f"Displaying Image from {self.__filename}")