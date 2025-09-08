from HandlerBase import HandlerBase
from Manager import Manager
import random

class Supervisor(HandlerBase):
    def handle_query(self, query):
        can_handle = random.choice([True, False])
        if can_handle:
            print(f"The following query is resolved by Supervisor...\n{query}")
        else:
            print(f"Query is being passed on to Manager...")
            self._next_handler.handle_query(query) 