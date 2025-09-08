class VectorCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print("Rendering through Vector graphics")
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}\n")