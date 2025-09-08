from CharacterFlyweight import CharacterFlyweight
from ConcreteCharacter import ConcreteCharacter
from typing import Dict

class CharacterFactory:
    formats: Dict[str, CharacterFlyweight] = {}
    
    @classmethod
    def get_font_format(cls, style: str, size: int, color: str):
        key = (style, size, color)
        if key not in cls.formats:
            cls.formats[key] = ConcreteCharacter(style, size, color)
        return cls.formats[key]