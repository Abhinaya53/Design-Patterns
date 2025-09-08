from HandlerBase import HandlerBase

class Rupee10Handler(HandlerBase):
    def process_payment(self, total_cost):
        balance = total_cost % 10
        print(f"\nRs. 10 Notes: {total_cost // 10}\nBalance: {balance}")