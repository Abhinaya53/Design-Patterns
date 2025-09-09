
from User import User
from Ride import Ride
from Driver import Driver
from Passenger import Passenger
from FareStrategy import FareStrategy
from Vehicle import Vehicle
from RideMatch import RideMatch
from math import inf
from Location import Location

class RideSharingApplication:
    def __init__(self, user: User):
        self.__user: User = user
        self.__ride_match: RideMatch = RideMatch.get_instance()
    
    def request_ride(self, vehicle: Vehicle, fare_strategy: FareStrategy, destination: Location) -> None:
        if not isinstance(self.__user, Passenger):
            raise TypeError(f"Expected Passenger, got {type(self.__user).__name__}")
        
        driver: Driver = self.__ride_match.find_nearest_driver(self.__user, vehicle)
        if not driver:
            return
        
        distance: float = driver.get_location().calc_distance(destination)
        ride: Ride = Ride(driver, self.__user, fare_strategy, distance)
        ride.start_ride()

    def register_driver(self) -> None:
        if not isinstance(self.__user, Driver):
            raise TypeError(f"Expected Driver, got {type(self.__user).__name__}")
        
        self.__ride_match.add_driver(self.__user)