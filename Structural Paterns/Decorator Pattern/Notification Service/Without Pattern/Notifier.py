from abc import ABC, abstractmethod

# Interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass