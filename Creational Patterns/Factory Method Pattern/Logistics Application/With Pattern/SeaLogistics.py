from LogisticFactory import LogisticFactory
from Ship import Ship

class SeaLogistics(LogisticFactory):
    def createTransport(self):
        return Ship()