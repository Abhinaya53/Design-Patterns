from abc import ABC, abstractmethod

class CharacterFlyweight(ABC):
    @abstractmethod
    def display_character(self, character: str):
        pass