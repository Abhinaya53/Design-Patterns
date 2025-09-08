from HandlerInterface import HandlerInterface

class HandlerBase(HandlerInterface):
    def __init__(self):
        self._next_handler = None