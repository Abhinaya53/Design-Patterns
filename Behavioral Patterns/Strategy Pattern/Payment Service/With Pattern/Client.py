from PaymentService import PaymentService
from UPIPayment import UPIPayment
from CreditCardPayment import CreditCardPayment
from DebitCardPayment import DebitCardPayment

service = PaymentService()

service.set_payment_strategy(CreditCardPayment())
service.pay(300.0)

service.set_payment_strategy(DebitCardPayment())
service.pay(500.0)

service.set_payment_strategy(UPIPayment())
service.pay(200.0)