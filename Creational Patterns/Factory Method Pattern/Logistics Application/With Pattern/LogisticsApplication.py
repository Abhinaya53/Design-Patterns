from RoadLogistics import RoadLogistics
from SeaLogistics import SeaLogistics
from CargoLogistics import CargoLogistics

road_logistics = RoadLogistics()
sea_logistics = SeaLogistics()
cargo_logistics = CargoLogistics()

road_transport = road_logistics.createTransport()
sea_transport = sea_logistics.createTransport()
air_transport = cargo_logistics.createTransport()

road_transport.deliver()
sea_transport.deliver()
air_transport.deliver() 