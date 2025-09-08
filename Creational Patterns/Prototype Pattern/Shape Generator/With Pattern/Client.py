from Circle import Circle
from Rectangle import Rectangle

circle1 = Circle(10, 20, "Red", 15)
circle1.draw()

circle2 = circle1.clone()
circle2.draw()

rectangle1 = Rectangle(5, 10, "Blue", 20, 10)
rectangle1.draw()

rectangle2 = rectangle1.clone()
rectangle2.draw() 