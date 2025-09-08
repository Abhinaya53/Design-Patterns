from PaymentStrategyInterface import PaymentStrategyInterface

class PaymentService:               # Context
    def __init__(self):
        self.__payment_strategy = None

    def set_payment_strategy(self, payment_strategy) -> None:
        self.__payment_strategy: PaymentStrategyInterface = payment_strategy
    
    def pay(self, amount: float) -> None:
        if not self.__payment_strategy:
            print("Please set a payment method first.")
        else:
            self.__payment_strategy.process_payment(amount)