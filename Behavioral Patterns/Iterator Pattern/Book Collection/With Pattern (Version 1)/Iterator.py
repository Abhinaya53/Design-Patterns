from abc import ABC, abstractmethod
from Book import Book

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Book:
        pass