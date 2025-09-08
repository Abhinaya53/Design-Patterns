from AdditionalFeatureBuilderInterface import AdditionalFeatureBuilderInterface
from House import House

class GarageBuilder(AdditionalFeatureBuilderInterface):
    def build(self, house: House):
        house.set_has_garage(True) 