class PaymentService:
    def process_payment(self, payment_method: str) -> None:
        if payment_method == "Credit Card":
            print("Making payment via credit card")
        elif payment_method == "Debit Card":
            print("Making payment via debit card")
        elif payment_method == "UPI":
            print("Making payment via UPI")
        else:
            print("Unsupported Payment method")