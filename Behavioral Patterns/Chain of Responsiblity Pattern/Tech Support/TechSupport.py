from HandlerBase import HandlerBase
from Supervisor import Supervisor
import random

class TechSupport(HandlerBase):
    def handle_query(self, query):
        can_handle = random.choice([True, False])
        if can_handle:
            print(f"The following query is resolved by Tech Support...\n{query}")
        else:
            print(f"Query is being passed on to Supervisor...")
            self._next_handler.handle_query(query) 