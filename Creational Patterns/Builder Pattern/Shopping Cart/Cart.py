from Product import Product

class Cart:
    def __init__(self):
        self.__products = {}
        self.__coupon = 0
        self.__gift_wrap = False
        self.__gift_wrap_cost = 50.0
        self.__delivery_instructions = None
    
    def __str__(self):
        res = "Shopping Cart:\nItem\t\tQty\t\tPrice\t\t\tTotal\n"
        for product in self.__products:
            res += str(self.__products[product])
        res += f"\nCoupon Discount: Rs. {self.__coupon}\n"
        res += f"Gift Wrap: {'Yes' if self.__gift_wrap else 'No'}\n"
        if self.__gift_wrap:
            res += f"Gift Wrap Cost: Rs. {self.__gift_wrap_cost}\n"
        res += f"Delivery Instructions: {self.__delivery_instructions if self.__delivery_instructions else 'None'}\n"
        res += f"Total Amount: Rs. {self.calc_cart_total()}\n"
        return res
    
    def add_new_product(self, product: Product):
        self.__products[product.get_name()] = product
        
    def add_coupon(self, coupon_amount):
        self.__coupon = coupon_amount
    
    def add_gift_wrap(self):
        self.__gift_wrap = True
    
    def add_delivery_instructions(self, instructions):
        self.__delivery_instructions = instructions
    
    def calc_cart_total(self):
        amount = 0.0

        for product_name in self.__products:
            amount += self.__products[product_name].calculate_total_cost()
        
        amount -= self.__coupon

        if self.__gift_wrap:
            amount += self.__gift_wrap_cost
            
        return round(amount, 2)
    
    def get_products(self):
        return self.__products