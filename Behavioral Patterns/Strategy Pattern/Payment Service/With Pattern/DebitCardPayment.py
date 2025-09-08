from PaymentStrategyInterface import PaymentStrategyInterface

class DebitCardPayment(PaymentStrategyInterface):
    def process_payment(self, amount: float) -> None:
        print(f"\nMaking payment via Debit Card.\nAmount: {round(amount, 2)}\n")