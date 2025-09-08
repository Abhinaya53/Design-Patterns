from UserService import UserService
from OrderService import OrderService
from PaymentService import PaymentService

user_service = UserService()
order_service = OrderService()
payment_service = PaymentService()

# Client code directly interacting with multiple services
user_service.get_user_details(192)
order_service.create_order(187)
payment_service.process_payment(532)