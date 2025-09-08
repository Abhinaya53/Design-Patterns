from abc import ABC, abstractmethod

# Interface
class DataSource(ABC):
    @abstractmethod
    def read_file(self) -> str:
        pass

    @abstractmethod
    def write_file(self, data: str):
        pass