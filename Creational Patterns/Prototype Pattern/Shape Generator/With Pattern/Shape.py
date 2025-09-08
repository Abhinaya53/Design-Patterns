from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self):
        pass
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getColor(self):
        return self.color
    
    @abstractmethod
    def clone(self):
        pass