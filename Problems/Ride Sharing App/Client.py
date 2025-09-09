from User import User
from Ride import Ride
from Driver import Driver
from Passenger import Passenger
from FareStrategy import FareStrategy
from StandardFare import StandardFare
from SharedFare import SharedFare
from LuxuryFare import LuxuryFare
from Vehicle import Vehicle
from Car import Car
from Bike import Bike
from LuxuryCar import LuxuryCar
from RideMatch import RideMatch
from math import inf
from DriverStatus import DriverStatus
from Location import Location
from RideSharingApplication import RideSharingApplication

class Client:
    def main(self):
        source = Location("IndiraNagar", 68.0, 77.0)
        destination = Location("Whitefield", 49.2, 88.7)
        passenger1 = Passenger("Abhi", "9897969594", source)
        app1 = RideSharingApplication(passenger1)
        app1.request_ride(Car(), LuxuryFare(), destination)

        location = Location("JP Nagar", 96.3, 20.5)
        vehicle = LuxuryCar("KA 88 XX 8888")
        driver1 = Driver("Jake", "9999999999", location, vehicle)
        app2 = RideSharingApplication(driver1)
        app2.register_driver()

        location = Location("Koramangala", 47.3, 60.5)
        vehicle = Car("KA 99 XX 6666")
        driver1 = Driver("Terry", "2222222222", location, vehicle)
        app2 = RideSharingApplication(driver1)
        app2.register_driver()

        app1.request_ride(Car(), LuxuryFare(), destination)

client = Client()
client.main()