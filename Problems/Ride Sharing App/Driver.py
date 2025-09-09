from Location import Location
from Vehicle import Vehicle
from User import User
from DriverStatus import DriverStatus

class Driver(User):
    def __init__(self, name: str, contact_num: str, location: Location, vehicle: Vehicle):
        super().__init__(name, contact_num, location)
        self.__vehicle = vehicle
        self.__status = DriverStatus.AVAILABLE
    
    def __str__(self):
        strng = f"Driver Details:\n"
        strng += f"Name: {self.get_name()}\n"
        strng += f"Contact Number: {self.get_contact_num()}\n"
        strng += f"Location: {self.get_location()}\n"
        strng += f"Vehicle: {self.get_vehicle()}\n"
        return strng
    
    def get_vehicle(self) -> Vehicle:
        return self.__vehicle
    
    def get_status(self) -> DriverStatus:
        return self.__status
    
    def set_vehicle(self, vehicle: Vehicle) -> None:
        if not isinstance(vehicle, Vehicle):
            raise TypeError(f"Expected Vehicle , got {type(vehicle).__name__}")
        
        self.__vehicle = vehicle
    
    def set_status(self, status: DriverStatus) -> None:
        if not isinstance(status, DriverStatus):
            raise TypeError(f"Expected DriverStatus , got {type(status).__name__}")
        
        self.__status = status
    
    def notify(self, message: str) -> None:
        print(f"Driver Notification:\n{message}")