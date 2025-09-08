from HandlerBase import HandlerBase
from Rupee500Handler import Rupee500Handler

class Rupee2000Handler(HandlerBase):
    def __init__(self):
        self._next_handler = Rupee500Handler()

    def process_payment(self, total_cost): 
        balance = total_cost % 2000 
        print(f"\nRs. 2000 Notes: {total_cost // 2000}\nBalance: {balance}")
        if balance != 0:
            self._next_handler.process_payment(balance)