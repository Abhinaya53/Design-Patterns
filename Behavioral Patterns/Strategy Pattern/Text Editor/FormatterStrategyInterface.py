from abc import ABC, abstractmethod

class FormatterStrategyInterface(ABC):            #Strategy
    @abstractmethod
    def format(self, text: str) -> None:
        pass