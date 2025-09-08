from abc import ABC, abstractmethod

class VisitorInterface(ABC):
    @abstractmethod
    def visit(self, node):
        pass