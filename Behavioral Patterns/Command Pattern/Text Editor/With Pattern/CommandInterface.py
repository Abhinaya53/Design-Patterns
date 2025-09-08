from abc import ABC, abstractmethod

class CommandInterface(ABC):
    def execute(self) -> None:
        pass