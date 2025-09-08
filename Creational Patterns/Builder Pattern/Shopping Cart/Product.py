class Product:
    def __init__(self, name, price, quantity = 1):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    def __str__(self):
        return f"{self.__name}\t\t{self.__quantity}\t\tRs. {self.__price}\t\tRs. {self.calculate_total_cost()}\n"
    
    def calculate_total_cost(self):
        return self.__price * self.__quantity

    def get_name(self):
        return self.__name
    
    def get_quantity(self):
        return self.__quantity