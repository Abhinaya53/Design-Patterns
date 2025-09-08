from BuilderInterface import BuilderInterface
from AdditionalFeatureBuilderInterface import AdditionalFeatureBuilderInterface
from GarageBuilder import GarageBuilder
from SwimmingPoolBuilder import SwimmingPoolBuilder
from PorchBuilder import PorchBuilder

class Director:
    def __init__(self):
        self.__builder = None
    
    def set_builder(self, builder: BuilderInterface):
        self.__builder = builder
    
    def build_simple_house(self):
        self.__builder.build_walls()
        self.__builder.build_windows() 
        self.__builder.build_roof()
    
    def build_complete_house(self):
        self.__builder.build_walls()
        self.__builder.build_windows()
        self.__builder.build_roof()
        self.__builder.build_additional_feature(GarageBuilder())
        self.__builder.build_additional_feature(SwimmingPoolBuilder())
        self.__builder.build_additional_feature(PorchBuilder())

    def add_additional_feature(self, additional_feature_builder: AdditionalFeatureBuilderInterface):
        self.__builder.build_additional_feature(additional_feature_builder)
    
    def get_house(self):
        return self.__builder.get_result()
    

