from UserService import UserService
from OrderService import OrderService
from PaymentService import PaymentService

class APIGateway:
    def __init__(self):
        self.__user_service = UserService()
        self.__order_service = OrderService()
        self.__payment_service = PaymentService()
    
    def get_all_details(self, user_id: int, order_id: int, payment_id: int) -> None:
        self.__user_service.get_user_details(user_id)
        self.__order_service.create_order(order_id)
        self.__payment_service.process_payment(payment_id)