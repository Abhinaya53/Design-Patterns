from abc import ABC, abstractmethod
from AdditionalFeatureBuilderInterface import AdditionalFeatureBuilderInterface

# Interface
class BuilderInterface(ABC):
    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod 
    def build_roof(self):
        pass

    @abstractmethod
    def build_additional_feature(self, additional_feature_builder: AdditionalFeatureBuilderInterface):
        pass

    @abstractmethod
    def get_result(self):
        pass