from AbsoluteFactory import AbsoluteFactory
from Vehicles.Truck import Truck
from Engines.DieselEngine import DieselEngine

class TruckFactoryDiesel(AbsoluteFactory):

    def create_vehicle(self): 
        return Truck()
    
    def create_engine(self): 
        return DieselEngine()