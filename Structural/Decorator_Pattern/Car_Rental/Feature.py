from Car import Car

class Feature(Car):

    def __init__(self, car: Car):
        self.car = car
    
    def get_description(self):
        return self.car.get_description()

    def get_price(self):
        return self.car.get_price()