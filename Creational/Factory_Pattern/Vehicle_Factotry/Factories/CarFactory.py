from Factory import Factory
from Vehicles.Car import Car

class CarFactory(Factory):

    def request_vehicle(self)->Car:
        return Car()