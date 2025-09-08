from Shape import Shape

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        print(f"Drawing circle at ({self.x}, {self.y}) with color {self.color} and radius {self.radius}")
    
    def getRadius(self):
        return self.radius