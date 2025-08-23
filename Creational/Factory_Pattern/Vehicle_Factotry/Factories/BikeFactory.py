from Factory import Factory
from Vehicles.Bike import Bike

class BikeFactory(Factory):

    def request_vehicle(self)->Bike:
        return Bike()