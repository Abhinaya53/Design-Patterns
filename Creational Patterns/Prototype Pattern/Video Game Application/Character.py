from abc import ABC, abstractmethod

# Interface
class Character(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display_character(self):
        pass