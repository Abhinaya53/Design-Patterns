from Shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, color, length, width):
        super().__init__(x, y, color)
        self.length = length
        self.width = width

    def draw(self):
        print(f"Drawing rectangle at ({self.x}, {self.y}) with color {self.color}, length {self.length}, and width {self.width}")
    
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width