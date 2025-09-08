from Character import Character

class Warrior(Character):
    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        self.__defense = defense

    def display_character(self):
        print(f"Warrior Character Name: {self.__name}\nHealth: {self.__health}\nAttack Power: {self.__attack_power}\nDefense: {self.__defense}\n")

    def clone(self):
        return Warrior(self.__name, self.__health, self.__attack_power, self.__attack_power)