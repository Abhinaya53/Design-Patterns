from CharacterFlyweight import CharacterFlyweight

class ConcreteCharacter(CharacterFlyweight):
    def __init__(self, style: str, size: int, color: str):
        self.__style = style
        self.__size = size
        self.__color = color
    
    def display_character(self, character: str):
        print(f"Character: {character}\nFont Style: {self.__style}\nFont Size: {self.__size}\nColor: {self.__color}\n")