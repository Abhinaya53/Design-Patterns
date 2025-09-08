from Director import Director
from CartBuilder import CartBuilder

if __name__ == "__main__":
    products = [
        {'name': 'Laptop', 'price': 50000, 'quantity': 1},
        {'name': 'Mouse', 'price': 1500, 'quantity': 2},
        {'name': 'Shoe', 'price': 3000}
    ]
    
    builder = CartBuilder()
    director = Director(builder, products)
    director.construct_simple_cart(products, "Leave at the front door if not home.")
    director.construct_premium_cart(products, "Leave at the front door if not home.")