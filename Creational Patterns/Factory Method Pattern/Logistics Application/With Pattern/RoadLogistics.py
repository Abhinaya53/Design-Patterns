from LogisticFactory import LogisticFactory
from Truck import Truck

class RoadLogistics(LogisticFactory):
    def createTransport(self):
        return Truck()