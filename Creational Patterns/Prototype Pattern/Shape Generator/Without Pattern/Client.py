from Circle import Circle
from Rectangle import Rectangle

circle1 = Circle(10, 20, "Red", 15)
circle1.draw()

circle2 = Circle(circle1.getX(), circle1.getY(), circle1.getColor(), circle1.getRadius())
circle2.draw()

rectangle1 = Rectangle(5, 10, "Blue", 20, 10)
rectangle1.draw()

rectangle2 = Rectangle(rectangle1.getX(), rectangle1.getY(), rectangle1.getColor(), rectangle1.getLength(), rectangle1.getWidth())
rectangle2.draw()