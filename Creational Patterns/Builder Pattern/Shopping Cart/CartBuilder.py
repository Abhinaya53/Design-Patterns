from Cart import Cart
from Product import Product

class CartBuilder():
    def __init__(self):
        self.__cart = Cart()
    
    def add_product(self, name, price, quantity = 1):
        product = Product(name, price, quantity)
        self.__cart.add_new_product(product)
    
    def add_coupon(self, discount_percentage):
        self.__cart.add_coupon(self.__cart.calc_cart_total() * (discount_percentage / 100))
    
    def add_gift_wrap(self):
        self.__cart.add_gift_wrap()
    
    def add_delivery_instructions(self, instructions):
        self.__cart.add_delivery_instructions(instructions)

    def reset(self):
        self.__cart = Cart()
    
    def cart_total(self):
        return self.__cart.calc_cart_total()
    
    def print_cart(self):
        print(self.__cart)