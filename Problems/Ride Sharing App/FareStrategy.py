from abc import ABC, abstractmethod
from Vehicle import Vehicle

# Fare Strategy Interface
class FareStrategy(ABC):
    @abstractmethod
    def calc_fare(self, vehicle: Vehicle, distance: float) -> float:
        pass