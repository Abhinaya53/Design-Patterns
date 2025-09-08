from Shape import Shape
from Renderer import Renderer
from Rectangle import Rectangle
from Circle import Circle
from RasterRenderer import RasterRenderer
from VectorRenderer import VectorRenderer

class GraphicEditor:
    def render_shape(self, shape: Shape):
        shape.draw()
        shape.move(10, 10)
        shape.draw()
    
    def main(self):
        raster_renderer = RasterRenderer()
        vector_renderer = VectorRenderer()

        circle = Circle(raster_renderer, 10, 10, 5)
        rectangle = Rectangle(vector_renderer, 15, 21, 10, 5)

        self.render_shape(circle)
        self.render_shape(rectangle)

        # Changing renderer at runtime
        circle.set_renderer(vector_renderer)
        rectangle.set_renderer(raster_renderer)
        self.render_shape(circle)
        self.render_shape(rectangle)

if __name__ == "__main__":
    editor = GraphicEditor()
    editor.main()