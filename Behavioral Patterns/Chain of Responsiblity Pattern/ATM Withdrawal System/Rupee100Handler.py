from HandlerBase import HandlerBase
from Rupee10Handler import Rupee10Handler

class Rupee100Handler(HandlerBase):
    def __init__(self):
        self._next_handler = Rupee10Handler()

    def process_payment(self, total_cost):
        balance = total_cost % 100 
        print(f"\nRs. 100 Notes: {total_cost // 100}\nBalance: {balance}")
        if balance != 0:
            self._next_handler.process_payment(balance)