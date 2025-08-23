from Factory import Factory
from Vehicles.Truck import Truck

class TruckFactory(Factory):

    def request_vehicle(self)->Truck:
        return Truck()