from abc import ABC, abstractmethod
from DocumentInterface import DocumentInterface

class DocumentFactoryInterface(ABC):
    @abstractmethod
    def create_document(self) -> DocumentInterface:
        pass