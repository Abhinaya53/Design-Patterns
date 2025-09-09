from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, number_plate: str):
        self._number_plate = number_plate
        self._fare_per_km = self.get_fare_per_km()

    def __str__(self) -> str:
        return f"Number Plate: {self._number_plate}"

    @abstractmethod
    def get_fare_per_km(self) -> float:
        pass

    def calculate_fare(self, distance: float) -> float:
        return distance * self.get_fare_per_km()
    
    def get_number_plate(self) -> str:
        return self._number_plate