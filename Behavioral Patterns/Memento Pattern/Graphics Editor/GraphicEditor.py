from EditorMemento import EditorMemento

class GraphicEditor:
    def set_shape(self, shape_type, x, y, color, size) -> None:
        self.__shape_type = shape_type
        self.__x = x
        self.__y = y
        self.__color = color
        self.__size = size

    def get_shape_type(self) -> str:
        return self.__shape_type
    
    def get_x(self) -> int:
        return self.__x
    
    def get_y(self) -> int:
        return self.__y
    
    def get_color(self) -> int:
        return self.__color
    
    def get_size(self) -> int:
        return self.__size
    
    def save_state(self) -> EditorMemento:
        return EditorMemento(self.__shape_type, self.__x, self.__y, self.__color, self.__size)
    
    def restore_state(self, memento: EditorMemento) -> None:
        self.set_shape(memento.get_shape_type(), memento.get_x(), memento.get_y(), memento.get_color(), memento.get_size())