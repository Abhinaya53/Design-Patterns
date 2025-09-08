from abc import ABC, abstractmethod

# Interface
class DataProvider(ABC):
    @abstractmethod
    def get_results(self):
        pass