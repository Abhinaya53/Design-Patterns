from PaymentStrategyInterface import PaymentStrategyInterface

class UPIPayment(PaymentStrategyInterface):
    def process_payment(self, amount: float) -> None:
        print(f"\nMaking payment via UPI.\nAmount: {round(amount, 2)}\n")