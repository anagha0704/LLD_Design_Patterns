from AbsoluteFactory import AbsoluteFactory
from Vehicles.Bike import Bike
from Engines.PetrolEngine import PetrolEngine

class BikeFactoryPetrol(AbsoluteFactory):

    def create_vehicle(self): 
        return Bike()
    
    def create_engine(self): 
        return PetrolEngine()