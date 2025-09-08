class EditorMemento:
    def __init__(self, shape_type, x, y, color, size) -> None:
        self.__shapeType = shape_type
        self.__x = x
        self.__y = y
        self.__color = color
        self.__size = size
    
    def get_shape_type(self) -> str:
        return self.__shapeType
    
    def get_x(self) -> int:
        return self.__x
    
    def get_y(self) -> int:
        return self.__y
    
    def get_color(self) -> int:
        return self.__color
    
    def get_size(self) -> int:
        return self.__size