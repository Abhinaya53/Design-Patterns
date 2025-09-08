from BulletType import BulletType

class BulletFactory:
    types = {}

    @classmethod
    def get_bullet_type(cls, color: str) -> BulletType:
        if color not in cls.types:
            cls.types[color] = BulletType(color)
        return cls.types[color]