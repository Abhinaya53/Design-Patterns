from datetime import datetime
from threading import Lock

class Logger:
    __instance = None
    __lock = Lock()

    def __new__(cls):
        with cls.__lock:
            if not cls.__instance:
                cls.__instance = super(Logger, cls).__new__(cls)
            return cls.__instance

    def __init__(self):
        raise "Object creation is not allowed!"
    
    def info(self, message):
        self.__log("INFO", message)
    
    def warning(self, message):
        self.__log("WARNING", message)
    
    def error(self, message):
        self.__log("ERROR", message)

    def __log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} [{level}]: {message}")
    
    @classmethod
    def get_instance(cls):
        return cls.__new__(cls)