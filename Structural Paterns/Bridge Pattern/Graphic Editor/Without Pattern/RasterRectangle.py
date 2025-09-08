class RasterRectangle:
    def __init__(self, x, y, length, breadth):
        self.x = x
        self.y = y
        self.length = length
        self.breadth = breadth

    def draw(self):
        print("Rendering through Raster graphics")
        print(f"Drawing Rectangle at ({self.x}, {self.y}) with length {self.length} and breadth {self.breadth}\n")
