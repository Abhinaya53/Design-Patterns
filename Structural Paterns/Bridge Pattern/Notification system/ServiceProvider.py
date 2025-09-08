from abc import ABC, abstractmethod

class ServiceProvider(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass