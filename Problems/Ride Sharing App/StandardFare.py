from FareStrategy import FareStrategy
from Vehicle import Vehicle

class StandardFare(FareStrategy):
    def calc_fare(self, vehicle: Vehicle, distance: float) -> float:
        return vehicle.get_fare_per_km() * distance