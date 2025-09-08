class Notification:
    def __init__(self, message: str):
        self.__message = message
    
    def get_message(self):
        return self.__message
    
    def __str__(self):
        return self.__message
    
    def __lt__(self, other):
        if not isinstance(other, Notification):
            return NotImplemented
        return self.__message < other.get_message()