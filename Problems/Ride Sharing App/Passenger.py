from Location import Location
from User import User

class Passenger(User):
    def __init__(self, name: str, contact_num: str, location: Location):
        super().__init__(name, contact_num, location)
    
    def __str__(self):
        strng = f"Passenger Details:\n{super().__str__()}"
        return strng
    
    def notify(self, message: str) -> None:
        print(f"Passenger Notification:\n{message}")