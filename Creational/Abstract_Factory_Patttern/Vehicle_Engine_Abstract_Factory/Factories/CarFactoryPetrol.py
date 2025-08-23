from AbsoluteFactory import AbsoluteFactory
from Vehicles.Car import Car
from Engines.PetrolEngine import PetrolEngine

class CarFactoryPetrol(AbsoluteFactory):

    def create_vehicle(self): 
        return Car()
    
    def create_engine(self): 
        return PetrolEngine()