from abc import ABC, abstractmethod

class Parser(ABC):
    def parse(self):            # This method should not be overidden in subclasses, in Java it's declared with final keyword
        self._open_file()
        self._parse_data()
        self._close_file()

    def _open_file(self):
        print("\nOpening File")

    def _close_file(self):
        print("Closing File\n")
    
    @abstractmethod
    def _parse_data(self):
        pass