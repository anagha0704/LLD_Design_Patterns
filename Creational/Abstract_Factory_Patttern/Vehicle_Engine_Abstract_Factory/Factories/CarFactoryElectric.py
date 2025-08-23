from AbsoluteFactory import AbsoluteFactory
from Vehicles.Car import Car
from Engines.ElectricEngine import ElectricEngine

class CarFactoryElectric(AbsoluteFactory):

    def create_vehicle(self): 
        return Car()
    
    def create_engine(self): 
        return ElectricEngine()