class AppConfig:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(AppConfig, cls).__new__(cls)
            cls.__instance.__api_key = "12345-ABCDE"
            cls.__instance.__db_url = "postgres://db1"
        return cls.__instance

    def __init__(self):
        raise "Object creation is not allowed!"
    
    def get_api_key(self):
        return self.__api_key
    
    def get_db_url(self):
        return self.__db_url
    
    @classmethod
    def get_instance(cls):
        return cls.__new__(cls)