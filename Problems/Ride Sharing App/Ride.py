from User import User
from Driver import Driver
from Passenger import Passenger
from RideStatus import RideStatus
from FareStrategy import FareStrategy
from typing import Dict

class Ride:
    def __init__(self, driver: Driver, passenger: Passenger, fare_strategy: FareStrategy, distance: float):
        self.__status = RideStatus.SCHEDULED

        if not isinstance(driver, Driver):
            raise TypeError(f"Expected Driver, got {type(driver).__name__}")
        
        if not isinstance(passenger, Passenger):
            raise TypeError(f"Expected Passenger, got {type(passenger).__name__}")
        
        if not isinstance(fare_strategy, FareStrategy):
            raise TypeError(f"Expected FareStrategy, got {type(fare_strategy).__name__}")

        self.__users: Dict[str, User] = {
            "driver": driver,
            "passenger": passenger
        }

        self.__fare_strategy = fare_strategy
        self.__distance = distance
    
    def set_status(self, status: RideStatus) -> None:
        if not isinstance(status, RideStatus):
            raise TypeError(f"Expected RideStatus, got {type(status).__name__}")
        
        self.__status = status
        self.notify_users()
    
    # Observer Pattern
    def notify_users(self) -> None:
        status_message = f"Your Ride is {self.__status}\n"
        fare_dist_message = f"Total Distance: {round(self.__distance, 2)} kms\nTotal Fare: Rs. {round(self.calculate_fare(), 2)}/-\n"
        self.__users["driver"].notify(status_message + str(self.__users["passenger"]) + fare_dist_message)
        self.__users["passenger"].notify(status_message + str(self.__users["driver"]) + fare_dist_message)
    
    def calculate_fare(self) -> float:
        return self.__fare_strategy.calc_fare(self.__users["driver"].get_vehicle(), self.__distance)
    
    def start_ride(self) -> None:
        self.set_status(RideStatus.ONGOING)
        self.complete_ride()

    def complete_ride(self) -> None:
        self.set_status(RideStatus.COMPLETED)