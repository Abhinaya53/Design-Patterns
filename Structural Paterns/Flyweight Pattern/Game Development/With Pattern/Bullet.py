from BulletFactory import BulletFactory
from BulletFlyweight import BulletFlyweight

class Bullet:
    def __init__(self, color: str, x: int, y: int, velocity: int):
        self.__type: BulletFlyweight = BulletFactory.get_bullet_type(color)
        self.__x = x
        self.__y = y
        self.__velocity = velocity
    
    def move(self, x: int, y: int):
        self.__x += x
        self.__y += y

    def render(self):
        print("Rendering Bullet with Properties:\n" +
              f"Color: {self.__type.get_type()}\n" +
              f"Position: ({self.__x}, {self.__y})\n" +
              f"Velocity: {self.__velocity}\n")