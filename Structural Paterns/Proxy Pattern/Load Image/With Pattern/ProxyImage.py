from Image import Image
from RealImage import RealImage

class ProxyImage(Image):
    def __init__(self, filename):
        self.__filename = filename
        self.__real_image = None
    
    def display(self):
        if not self.__real_image:
            self.__real_image = RealImage(self.__filename)      # Loading + Caching
        self.__real_image.display()