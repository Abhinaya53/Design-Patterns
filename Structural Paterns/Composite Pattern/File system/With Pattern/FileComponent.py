from abc import ABC, abstractmethod

# Interface
class FileComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def get_details(self, prefix: str = "") -> str:
        pass