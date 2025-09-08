class Bullet:
    def __init__(self, color: str, x: int, y: int, velocity: int):
        self.__color = color        # Intrinsic Properties
        self.__x = x                # Extrinsic Properties
        self.__y = y                # Extrinsic Properties
        self.__velocity = velocity  # Extrinsic Properties
    
    def move(self, x: int, y: int):
        self.__x += x
        self.__y += y

    def render(self):
        print("Rendering Bullet with Properties:\n" +
              f"Color: {self.__color}\n" +
              f"Position: ({self.__x}, {self.__y})\n" +
              f"Velocity: {self.__velocity}\n")