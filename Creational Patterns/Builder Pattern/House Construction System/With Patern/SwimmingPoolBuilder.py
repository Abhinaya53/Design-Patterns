from AdditionalFeatureBuilderInterface import AdditionalFeatureBuilderInterface
from House import House

class SwimmingPoolBuilder(AdditionalFeatureBuilderInterface):
    def build(self, house: House):
        house.set_has_swimming_pool(True) 