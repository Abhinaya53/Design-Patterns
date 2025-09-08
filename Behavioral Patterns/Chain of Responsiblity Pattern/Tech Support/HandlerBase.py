from HandlerInterface import HandlerInterface

class HandlerBase(HandlerInterface):
    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, handler: HandlerInterface):
        self._next_handler = handler