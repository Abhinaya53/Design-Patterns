from ObserverInterface import ObserverInterface

class TabletDevice(ObserverInterface):
    def __init__(self, name: str):
        self.__name = name

    def update(self, temperature) -> None:
        print(f"Temperature on Tablet Device {self.__name}: {temperature} C")