from abc import ABC, abstractmethod

class NetworkService(ABC):
    @abstractmethod
    def fetch_data(self, key):
        pass