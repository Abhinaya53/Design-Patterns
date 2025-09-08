from Circle import Circle
from Square import Square
from Dot import Dot
from CompoundGraphic import CompoundGraphic

dot1 = Dot(1, 2)
dot2 = Dot(3, 4)
circle1 = Circle(5, 6, 10)
square1 = Square(7, 8, 4, 5)

graphic = CompoundGraphic()
graphic.add_component(dot1)
graphic.add_component(dot2)
graphic.add_component(circle1)
graphic.add_component(square1)

square2 = Square(10, 20, 30, 40)
circle2 = Circle(15, 25, 35)

graphic2 = CompoundGraphic()
graphic2.add_component(square1)
graphic2.add_component(circle1)
graphic2.add_component(square2)
graphic2.add_component(circle2)

graphic2.move(100, 200)

graphic.add_component(graphic2)

graphic.draw()