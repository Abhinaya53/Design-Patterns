from HandlerBase import HandlerBase
from Rupee100Handler import Rupee100Handler

class Rupee500Handler(HandlerBase):
    def __init__(self):
        self._next_handler = Rupee100Handler()

    def process_payment(self, total_cost):
        balance = total_cost % 500
        print(f"\nRs. 500 Notes: {total_cost // 500}\nBalance: {balance}")
        if balance != 0:
            self._next_handler.process_payment(balance)