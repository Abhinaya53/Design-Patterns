from BulletFlyweight import BulletFlyweight

class BulletType(BulletFlyweight):
    def __init__(self, color):
        self.__color = color
    
    def get_type(self):
        return self.__color