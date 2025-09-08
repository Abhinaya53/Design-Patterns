class AppConfig:
    def __init__(self):
        self.__api_key = "12345-ABCDE"
        self.__db_url = "postgres://db1"
    
    def get_api_key(self):
        return self.__api_key
    
    def get_db_url(self):
        return self.__db_url 