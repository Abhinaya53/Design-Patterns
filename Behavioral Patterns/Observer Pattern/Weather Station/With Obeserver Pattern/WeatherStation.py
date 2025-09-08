from SubjectInterface import SubjectInterface
from ObserverInterface import ObserverInterface
from typing import List

class WeatherStation(SubjectInterface):
    def __init__(self) -> None:
        self.__observers: List[ObserverInterface] = []
        self.__temperature: float = None

    def set_temperature(self, temp: float) -> None:
        self.__temperature = temp
        self.notify()
    
    def get_temperature(self) -> float:
        return self.__temperature if self.__temperature else "Temperature not set yet!"
    
    def subscribe(self, observer: ObserverInterface) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def unsubscribe(self, observer: ObserverInterface) -> None:
        self.__observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self.__temperature)             # Runtime Polymorphism because based on the oberserver device object this function will be called
    