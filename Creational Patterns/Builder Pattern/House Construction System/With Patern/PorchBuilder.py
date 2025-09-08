from AdditionalFeatureBuilderInterface import AdditionalFeatureBuilderInterface
from House import House

class PorchBuilder(AdditionalFeatureBuilderInterface):
    def build(self, house: House):
        house.set_has_porch(True) 