from SubjectInterface import SubjectInterface
from ObserverInterface import ObserverInterface
from typing import List

class StockMarket(SubjectInterface):
    def __init__(self, price_change_threshold: float) -> None:
        self.__observers: List[ObserverInterface] = []
        self.__price_change_threshold = price_change_threshold

    def set_stock_price(self, stock_symbol: str, new_price: float, old_price: float) -> None:
        price_change = abs(old_price - new_price) / old_price * 100
        if price_change >= self.__price_change_threshold:
            self.notify_observers(stock_symbol, new_price, old_price)
    
    def register_observer(self, observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)
    
    def remove_observer(self, observer) -> None:
        self.__observers.remove(observer)
    
    def notify_observers(self, stock_symbol: str, new_price: float, old_price: float) -> None:
        for observer in self.__observers:
            observer.update(stock_symbol, new_price, old_price)             # Runtime Polymorphism because based on the oberserver device object this function will be called
    