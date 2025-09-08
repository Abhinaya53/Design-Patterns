from Director import Director
from CabinBuilder import CabinBuilder
from LakeHouseBuilder import LakeHouseBuilder
from GarageBuilder import GarageBuilder
from PorchBuilder import PorchBuilder
from House import House

director = Director()
cabin_builder = CabinBuilder()
lake_house_builder = LakeHouseBuilder()

director.set_builder(cabin_builder)
director.build_complete_house()
cabin = director.get_house()
print(cabin)

director.set_builder(lake_house_builder)
director.build_simple_house()
director.add_additional_feature(GarageBuilder()) 
director.add_additional_feature(PorchBuilder())
lake_house = director.get_house()
print(lake_house)