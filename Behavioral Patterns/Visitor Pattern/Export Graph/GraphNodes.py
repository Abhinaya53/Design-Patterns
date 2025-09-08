from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class City(Node):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit(self)

class Industry(Node):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit(self)

class Road(Node):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit(self)

class PowerLine(Node):
    def __init__(self, name):
        self.name = name
        
    def accept(self, visitor):
        visitor.visit(self)
