from HandlerBase import HandlerBase
from TechSupport import TechSupport
import random

class ChatBot(HandlerBase):
    def handle_query(self, query):
        can_handle = random.choice([True, False])
        if can_handle: 
            print(f"The following query is resolved by ChatBot...\n{query}")
        else:
            print(f"Query is being passed on to Technical Support Team Member...")
            self._next_handler.handle_query(query)