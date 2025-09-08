from CharacterFactory import CharacterFactory

class DocumentEditor:
    def __init__(self):
        self.__content = []
    
    def add_character(self, character: str, style: str, size: int, color: str):
        character_format = CharacterFactory.get_font_format(style, size, color)
        self.__content.append([character, character_format])
    
    def render(self):
        print("Content: \n")
        for character, character_format in self.__content:
            character_format.display_character(character)