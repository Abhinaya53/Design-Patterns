from math import sqrt

class Location:
    def __init__(self, name: str, latitude: float, longitude: float):
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude

    def __str__(self) -> str:
        return self.get_name()
    
    def get_name(self) -> str:
        return self.__name
    
    def get_latitude(self) -> float:
        return self.__latitude
    
    def get_longitude(self) -> float:
        return self.__longitude
    
    def calc_distance(self, other) -> float:
        if not isinstance(other, Location):
            raise TypeError(f"Expected Location, got {type(other)}")
        
        dx = self.get_latitude() - other.get_latitude()
        dy = self.get_longitude() - other.get_longitude()
        return sqrt(dx * dx + dy * dy)