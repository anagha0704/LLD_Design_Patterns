from Factories.CarFactoryElectric import CarFactoryElectric
from Factories.BikeFactoryPetrol import BikeFactoryPetrol
from Factories.CarFactoryPetrol import CarFactoryPetrol
from Factories.TruckFactoryDiesel import TruckFactoryDiesel

class VehicleEngineFactory:

    def run():
        factory = BikeFactoryPetrol()
        vehicle = factory.create_vehicle() # Bike()
        engine = factory.create_engine() # Petrol()
        print(vehicle.deliver())  
        print(engine.start())

if __name__ == "__main__":
    VehicleEngineFactory.run()