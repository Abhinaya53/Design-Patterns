from abc  import ABC, abstractmethod
from House import House

# Interface
class AdditionalFeatureBuilderInterface(ABC):
    @abstractmethod
    def build(self, house: House):
        pass 