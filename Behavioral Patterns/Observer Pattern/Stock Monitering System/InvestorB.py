from ObserverInterface import ObserverInterface

class InvestorB(ObserverInterface):
    def __init__(self, name: str, contact):
        self.__name = name
        self.__contact = contact

    def update(self, stock_symbol: str, new_price: float, old_price: float) -> None:
        print(f"\n{self.__name} (InvestorB) is being notified via {self.__contact}...")
        print(f"Stock Symbol: {stock_symbol}\nNew Price: Rs. {round(new_price, 2)}\nOld Price: Rs. {round(old_price, 2)}\n")