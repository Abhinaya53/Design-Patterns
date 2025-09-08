from HandlerBase import HandlerBase
import random

class Manager(HandlerBase):
    def handle_query(self, query):
        print(f"The following query is resolved by Manager...\n{query}") 