from ObserverInterface import ObserverInterface

class MobileDevice(ObserverInterface):
    def __init__(self, name: str):
        self.__name = name

    def update(self, temperature) -> None:
        print(f"Temperature on Mobile Device {self.__name}: {temperature} C")