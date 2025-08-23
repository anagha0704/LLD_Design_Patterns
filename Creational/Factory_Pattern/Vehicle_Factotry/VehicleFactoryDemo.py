from Factories.BikeFactory import BikeFactory
from Factories.TruckFactory import TruckFactory
from Factories.CarFactory import CarFactory

class VehicleFactoryDemo:

    def run():
        car = CarFactory()
        vehicle1 = car.request_vehicle()
        print(vehicle1.deliver())

        truck = TruckFactory()
        vehicle2 = truck.request_vehicle()
        print(vehicle2.deliver())

        bike = BikeFactory()
        vehicle3 = bike.request_vehicle()
        print(vehicle3.deliver())

if __name__ == "__main__":
    VehicleFactoryDemo.run()