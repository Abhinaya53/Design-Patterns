from LogisticFactory import LogisticFactory
from Aircraft import Aircraft

class CargoLogistics(LogisticFactory):
    def createTransport(self):
        return Aircraft()