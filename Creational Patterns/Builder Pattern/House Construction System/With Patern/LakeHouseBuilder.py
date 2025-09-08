from BuilderInterface import BuilderInterface
from AdditionalFeatureBuilderInterface import AdditionalFeatureBuilderInterface
from House import House

class LakeHouseBuilder(BuilderInterface):
    def __init__(self):
        self.house = House()
        self.house.set_house_type("LakeHouse")
    
    def build_walls(self):
        self.house.set_num_walls(4)
    
    def build_windows(self):
        self.house.set_num_windows(6)
    
    def build_roof(self):
        self.house.set_roof_type("Gable")
    
    def build_additional_feature(self, additional_feature_builder: AdditionalFeatureBuilderInterface):
        additional_feature_builder.build(self.house)
    
    def get_result(self):
        return self.house 