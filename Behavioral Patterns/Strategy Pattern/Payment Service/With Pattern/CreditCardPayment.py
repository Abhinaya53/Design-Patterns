from PaymentStrategyInterface import PaymentStrategyInterface

class CreditCardPayment(PaymentStrategyInterface):
    def process_payment(self, amount: float) -> None:
        print(f"\nMaking payment via Credit Card.\nAmount: {round(amount, 2)}\n")