from Cart import Cart
from CartBuilder import CartBuilder

class Director:
    def __init__(self, builder: CartBuilder, products = []):
        self.builder = builder
        self.products = products
    
    def construct_simple_cart(self, products, instructions = None):
        self.builder.reset()
        self.add_products()
        self.builder.add_coupon(10)
        self.builder.print_cart()
    
    def construct_premium_cart(self, products, instructions = None):
        self.builder.reset()
        self.add_products()
        self.builder.add_coupon(20)
        self.builder.add_gift_wrap()
        self.builder.add_delivery_instructions(instructions)
        self.builder.print_cart()

    def add_products(self):
        for product in self.products:
            self.builder.add_product(product['name'], product['price'], product.get('quantity', 1))