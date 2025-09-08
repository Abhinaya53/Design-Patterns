from abc import ABC, abstractmethod

class DocumentInterface(ABC):
    @abstractmethod
    def open(self) -> str:
        pass

    @abstractmethod
    def save(self) -> str:
        pass

    @abstractmethod
    def close(self) -> str:
        pass