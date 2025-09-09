from abc import ABC, abstractmethod
from Location import Location

class User(ABC):
    def __init__(self, name: str, contact_num: str, location: Location):
        self._name = name
        self._contact_num = contact_num
        self._location = location
    
    def __str__(self) -> str:
        strng = f"Name: {self.get_name()}\n"
        strng += f"Contact Number: {self.get_contact_num()}\n"
        strng += f"Location: {self.get_location()}\n"
        return strng

    def get_name(self) -> str:
        return self._name

    def get_contact_num(self) -> str:
        return self._contact_num
    
    def get_location(self) -> Location:
        return self._location
    
    def set_location(self, location: Location) -> None:
        if not isinstance(location, Location):
            raise TypeError(f"Expected Location , got {type(location).__name__}")
        self._location = location

    @abstractmethod
    def notify(self, message: str) -> None:
        pass