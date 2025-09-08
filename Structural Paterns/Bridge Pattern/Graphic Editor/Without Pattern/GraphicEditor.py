from RasterCircle import RasterCircle
from VectorCircle import VectorCircle
from RasterRectangle import RasterRectangle
from VectorRectangle import VectorRectangle

circle1 = RasterCircle(10, 10, 5)
circle1.draw()

circle2 = VectorCircle(20, 20, 10)
circle2.draw()

rectangle1 = RasterRectangle(10, 10, 20, 15)
rectangle1.draw()

rectangle2 = VectorRectangle(30, 30, 25, 20)
rectangle2.draw()