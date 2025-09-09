from Driver import Driver
from DriverStatus import DriverStatus
from Passenger import Passenger
from Vehicle import Vehicle
from typing import List
from math import inf

# Singleton Pattern
class RideMatch:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(RideMatch, cls).__new__(cls)
            cls.__instance.__drivers = []
        return cls.__instance
    
    def __init__(self):
        raise RuntimeError("Direct instantiation not allowed! Use RideMatch.get_instance() instead.")
    
    @classmethod
    def get_instance(cls) -> "RideMatch":
        return cls.__new__(cls)
    
    def add_driver(self, driver: Driver) -> None:
        if driver not in self.__drivers:
            self.__drivers.append(driver)
    
    def find_nearest_driver(self, passenger: Passenger, vehicle: Vehicle) -> Driver:
        min_dist = inf
        nearest_driver = None

        for driver in self.__drivers:
            if driver.get_status() == DriverStatus.ON_RIDE or not isinstance(driver.get_vehicle(), type(vehicle)):
                continue

            cur_dist = driver.get_location().calc_distance(passenger.get_location())
            if cur_dist < min_dist:
                min_dist = cur_dist
                nearest_driver = driver
        
        if not self.__drivers:
            print("No drivers available near you..\nWe are sorry for your inconvenience..\nPlease try again after some time...\n")
        
        return nearest_driver