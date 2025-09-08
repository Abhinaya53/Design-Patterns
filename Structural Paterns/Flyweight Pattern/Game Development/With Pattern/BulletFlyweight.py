from abc import ABC, abstractmethod

class BulletFlyweight(ABC):
    @abstractmethod
    def get_type(self):
        pass